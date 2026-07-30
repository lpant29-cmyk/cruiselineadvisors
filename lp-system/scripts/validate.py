#!/usr/bin/env python3
"""validate.py — the QA gate for the ads-LP system (Blueprint Part 5 stage 3,
ADS-LP-BRIEF §6 operational rules).

Checks:
  1. Every price present, numeric, USD, within the sanity band $99–$25,000.
  2. Change vs the last committed version (git HEAD) within ±25%, else flag.
  3. Every row whose price changed vs HEAD carries date_checked = today.
  4. Offers past end_date must have show_banner=no (reported; --fix-offers
     rewrites 07_offers.csv, the one auto-fix the blueprint allows).
  5. Every buildable page in 09_pages.csv has >=3 live matching deal rows
     (>=1 for itinerary-type pages), none of them VERIFY-BEFORE-PUBLISH.
  6. Stale check: any itinerary row with date_checked older than 10 days.
  7. DATA PROVENANCE (strict): a row may publish only if its source is an
     http(s) URL on a domain whitelisted in lp-system/data/
     source_whitelist.txt (exact domain or subdomain) and the row is not
     flagged UNVERIFIED in notes. Off-whitelist or UNVERIFIED rows never
     count as publishable inventory, and any buildable page referencing
     one gets a per-row provenance flag. Live offer banners are held to
     the same source rule.

Exit 0 = clean (safe to publish). Exit 1 = flags -> HOLD-{date}.md written
to lp-system/ with per-row evidence. qa-auditor attaches this output to
its verdict; the manager publishes only clean rows on a flagged run.
"""

import csv
import datetime as dt
import io
import pathlib
import subprocess
import sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "lp-system" / "data"
WHITELIST_FILE = DATA / "source_whitelist.txt"
PRICE_MIN, PRICE_MAX = 99, 25000
MAX_SWING = 0.25
STALE_DAYS = 10
VERIFY_MARK = "VERIFY-BEFORE-PUBLISH"
UNVERIFIED_MARK = "UNVERIFIED"


def load_whitelist():
    domains = []
    for line in WHITELIST_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            domains.append(line.lower())
    return domains


def source_ok(url, whitelist):
    """True only for http(s) URLs on a whitelisted domain or its subdomain."""
    if not str(url).startswith(("http://", "https://")):
        return False
    host = (urlparse(url).netloc or "").lower().split(":")[0]
    return any(host == d or host.endswith("." + d) for d in whitelist)


def provenance_ok(row, whitelist):
    if UNVERIFIED_MARK in row.get("notes", "").upper():
        return False
    return source_ok(row.get("source", ""), whitelist)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def head_version(relpath):
    """The file as of the last commit, for week-over-week comparison."""
    try:
        blob = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"HEAD:{relpath}"],
            capture_output=True, text=True, check=True).stdout
        return list(csv.DictReader(io.StringIO(blob)))
    except subprocess.CalledProcessError:
        return None


def parse_price(val):
    try:
        return int(str(val).strip().lstrip("$").replace(",", ""))
    except (ValueError, AttributeError):
        return None


def targets_of(row):
    return {t.strip() for t in row.get("page_targets", "").split(";") if t.strip()}


def main():
    fix_offers = "--fix-offers" in sys.argv
    today = dt.date.today()
    flags = []

    itins = read_csv(DATA / "03_itineraries.csv")
    offers = read_csv(DATA / "07_offers.csv")
    pages = read_csv(DATA / "09_pages.csv")
    prev = {r["itin_id"]: r for r in (head_version("lp-system/data/03_itineraries.csv") or [])}

    # --- 1-3: per-row price checks -------------------------------------
    for r in itins:
        rid = r["itin_id"]
        for field in ("price_interior", "price_balcony"):
            raw = r.get(field, "").strip()
            if not raw:
                flags.append((rid, field, "price missing"))
                continue
            p = parse_price(raw)
            if p is None:
                flags.append((rid, field, f"not numeric: {raw!r}"))
            elif not (PRICE_MIN <= p <= PRICE_MAX):
                flags.append((rid, field, f"${p} outside sanity band ${PRICE_MIN}-${PRICE_MAX}"))
            elif rid in prev:
                old = parse_price(prev[rid].get(field, ""))
                if old and abs(p - old) / old > MAX_SWING:
                    flags.append((rid, field,
                                  f"moved {100 * (p - old) / old:+.0f}% (${old} -> ${p}); "
                                  f"needs source evidence, hold"))
        # rows whose prices changed must be stamped today
        if rid in prev:
            changed = any(r.get(f) != prev[rid].get(f)
                          for f in ("price_interior", "price_balcony", "month_price_overrides"))
            if changed and r.get("date_checked") != today.isoformat():
                flags.append((rid, "date_checked",
                              f"price changed but stamp is {r.get('date_checked')!r}, not today"))
        # stale stamps
        try:
            checked = dt.date.fromisoformat(r.get("date_checked", ""))
            if (today - checked).days > STALE_DAYS:
                flags.append((rid, "date_checked",
                              f"stale: {checked} is {(today - checked).days} days old (>{STALE_DAYS})"))
        except ValueError:
            flags.append((rid, "date_checked", f"bad/missing date: {r.get('date_checked')!r}"))

    # --- 4: expired offers ---------------------------------------------
    dirty_offers = False
    for o in offers:
        try:
            expired = dt.date.fromisoformat(o["end_date"]) < today
        except ValueError:
            flags.append((o["offer_id"], "end_date", f"bad date {o.get('end_date')!r}"))
            continue
        if expired and o.get("show_banner") == "yes":
            if fix_offers:
                o["show_banner"] = "no"
                dirty_offers = True
                print(f"fixed: {o['offer_id']} past end_date -> show_banner=no")
            else:
                flags.append((o["offer_id"], "show_banner",
                              f"past end_date {o['end_date']} but still yes "
                              "(run with --fix-offers)"))
    if dirty_offers:
        with open(DATA / "07_offers.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=offers[0].keys())
            w.writeheader()
            w.writerows(offers)

    # --- 5 + 7: page inventory under provenance rules -------------------
    whitelist = load_whitelist()
    live_statuses = {"approved", "building", "built", "built-template", "live", "pilot"}
    for p in pages:
        if p.get("status") not in live_statuses:
            continue
        flt = p.get("deal_filter", "").strip()
        matching = [r for r in itins if flt in targets_of(r)]
        # itinerary pages need >=1 verified priced row; ship pages likewise
        # (structure-guard SHIP PAGES rule) — category pages need >=3
        need = 1 if p.get("page_type") in ("itinerary", "ship") else 3
        clean = []
        for r in matching:
            if VERIFY_MARK in r.get("source", ""):
                flags.append((r["itin_id"], "provenance",
                              f"feeds {p['page_id']} but is marked {VERIFY_MARK}"))
            elif UNVERIFIED_MARK in r.get("notes", "").upper():
                flags.append((r["itin_id"], "provenance",
                              f"feeds {p['page_id']} but is flagged {UNVERIFIED_MARK}; "
                              "empty stays empty until verified at an official source"))
            elif not source_ok(r.get("source", ""), whitelist):
                flags.append((r["itin_id"], "provenance",
                              f"feeds {p['page_id']} but source {r.get('source', '')!r} "
                              "is not an official whitelisted URL "
                              "(lp-system/data/source_whitelist.txt)"))
            else:
                clean.append(r)
        if len(clean) < need:
            flags.append((p["page_id"], "inventory",
                          f"{p['url']} has {len(clean)} publishable deal rows "
                          f"for filter {flt!r}, needs >={need} "
                          f"({len(matching) - len(clean)} matching row(s) blocked on provenance)"))

    # --- 7: live offer banners must cite an official source -------------
    for o in offers:
        if o.get("show_banner") == "yes" and not source_ok(o.get("source", ""), whitelist):
            flags.append((o["offer_id"], "provenance",
                          f"banner offer source {o.get('source', '')!r} is not an "
                          "official whitelisted URL"))

    # --- verdict --------------------------------------------------------
    if not flags:
        print("VALIDATE: clean. Safe to publish.")
        return 0

    # Append, never overwrite: qa-auditor and pricing-scout annotate this file
    # with arbitrations (CONFIRMED-AT-SOURCE etc.) that a re-run must not wipe.
    hold = ROOT / "lp-system" / f"HOLD-{today.isoformat()}.md"
    fresh = not hold.exists()
    with open(hold, "a", encoding="utf-8") as f:
        if fresh:
            f.write(f"# HOLD — validation flags, {today.isoformat()}\n\n")
            f.write("Flagged rows keep their last verified value and honest older "
                    "stamp. Publish clean rows only. Agents append arbitration "
                    "notes below flags; validate.py re-runs append new sections "
                    "and never rewrite earlier ones.\n")
        f.write(f"\n## validate.py run {dt.datetime.now().isoformat(timespec='seconds')}"
                f" — {len(flags)} flag(s)\n\n")
        for rid, field, msg in flags:
            f.write(f"- **{rid}** `{field}`: {msg}\n")
    print(f"VALIDATE: {len(flags)} flag(s) -> {hold}")
    for rid, field, msg in flags:
        print(f"  FLAG {rid} {field}: {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
