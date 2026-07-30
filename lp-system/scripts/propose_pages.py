#!/usr/bin/env python3
"""propose_pages.py — computes candidate pages from real inventory
(SCALING-PLAYBOOK §3). Combos are computed, never hand-listed.

Runs after every Pass A enumeration:
  1. Compute all facet combos over 03_itineraries.csv: line x port,
     dest x port, duration x dest, line x dest, line x port x nights,
     port-only, dest-only, duration-only.
  2. Keep a combo only if:
       - >=3 matching itineraries (>=1 for line x port x nights),
       - at least one sailing in the next 6 months,
       - no other combo already covers the identical itinerary set with
         fewer facets (the broader page wins; the thinner one is noted).
  3. Write lp-system/data/pages_proposed.csv (slug, url, h1, deal_filter,
     itinerary_count). structure-guard approves rows into 09_pages.csv;
     this script NEVER touches 09_pages.csv itself.
  4. Retire check: existing buildable pages whose publishable itinerary
     count fell below threshold are listed in pages_retire_suggestions.csv
     (status flips are structure-guard's call: 30-day grace with call CTA,
     then redirect to the parent facet).

Duration bands follow the taxonomy: 2-5, 6-8, 9+ nights.
"""

import csv
import datetime as dt
import pathlib
import sys
from itertools import combinations

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "lp-system" / "data"
VERIFY_MARK = "VERIFY-BEFORE-PUBLISH"
HORIZON_MONTHS = 6


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def band(nights):
    n = int(nights)
    if n <= 5:
        return "2-5"
    if n <= 8:
        return "6-8"
    return "9-plus"


def sails_soon(row, today):
    months = row.get("sail_months", "").strip()
    if months == "year-round":
        return True
    horizon = []
    y, m = today.year, today.month
    for _ in range(HORIZON_MONTHS + 1):
        horizon.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return any(tok.strip() in horizon for tok in months.split(";"))


def main():
    today = dt.date.today()
    itins = read_csv(DATA / "03_itineraries.csv")
    lines = {r["line_id"]: r for r in read_csv(DATA / "01_lines.csv")}
    pages = read_csv(DATA / "09_pages.csv")

    live = [r for r in itins if VERIFY_MARK not in r.get("source", "")]

    # combo key -> (url, h1, deal_filter) builders keyed by facet tuple
    def line_slug(r):
        return lines[r["line_id"]]["slug"]

    def line_name(r):
        return lines[r["line_id"]]["line_name"]

    combos = {}  # key -> {itin_ids, url, h1, deal_filter, facets}

    def add(key, facets, url, h1, deal_filter, row):
        c = combos.setdefault(key, {
            "itin_ids": set(), "url": url, "h1": h1,
            "deal_filter": deal_filter, "facets": facets})
        c["itin_ids"].add(row["itin_id"])

    for r in live:
        if not sails_soon(r, today):
            continue
        ls, ln = line_slug(r), line_name(r)
        p, pl = r["port_slug"], r["port_label"].rsplit(" ", 1)[0]
        d, dl = r["dest"], r["dest_label"]
        b = band(r["nights"])
        bl = b.replace("-plus", "+").replace("-", " to ")
        add(f"line:{ls}", 1, f"/en/go/lines/{ls}/",
            f"{ln} Cruises", f"line:{ls}", r)
        add(f"port:{p}", 1, f"/en/go/from/{p}/",
            f"Cruises from {pl}", f"port:{p}", r)
        add(f"dest:{d}", 1, f"/en/go/to/{d}/",
            f"{dl} Cruises", f"dest:{d}", r)
        add(f"dur:{b}", 1, f"/en/go/{b}-night-cruises/",
            f"{bl} Night Cruises", f"dur:{b}", r)
        add(f"combo:{ls}-{p}", 2, f"/en/go/lines/{ls}/from/{p}/",
            f"{ln} Cruises from {pl}", f"combo:{ls}-{p}", r)
        add(f"destport:{d}-{p}", 2, f"/en/go/to/{d}/from/{p}/",
            f"{dl} Cruises from {pl}", f"destport:{d}-{p}", r)
        add(f"linedest:{ls}-{d}", 2, f"/en/go/lines/{ls}/to/{d}/",
            f"{ln} {dl} Cruises", f"linedest:{ls}-{d}", r)
        add(f"durdest:{b}-{d}", 2, f"/en/go/{b}-night-{d}-cruises/",
            f"{bl} Night {dl} Cruises", f"durdest:{b}-{d}", r)
        add(f"lpn:{ls}-{p}-{r['nights']}n", 3,
            f"/en/go/lines/{ls}/from/{p}/{r['nights']}-night/",
            f"{r['nights']}-Night {ln} Cruises from {pl}",
            f"lpn:{ls}-{p}-{r['nights']}n", r)

    # thresholds
    kept = {}
    for key, c in combos.items():
        need = 1 if key.startswith("lpn:") else 3
        if len(c["itin_ids"]) >= need:
            kept[key] = c

    # identical-set dedupe: fewest facets wins, others noted
    by_set = {}
    for key, c in kept.items():
        by_set.setdefault(frozenset(c["itin_ids"]), []).append((key, c))
    dropped = []
    for iset, group in by_set.items():
        if len(group) < 2:
            continue
        group.sort(key=lambda kc: kc[1]["facets"])
        for key, c in group[1:]:
            dropped.append((key, group[0][0]))
            kept.pop(key, None)

    existing_filters = {p["deal_filter"].strip() for p in pages}
    out_file = DATA / "pages_proposed.csv"
    proposed = 0
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["slug", "url", "h1", "deal_filter", "itinerary_count", "note"])
        for key, c in sorted(kept.items(), key=lambda kc: -len(kc[1]["itin_ids"])):
            note = "already-registered" if c["deal_filter"] in existing_filters else ""
            slug = c["url"].strip("/").replace("en/go/", "").replace("/", "-")
            w.writerow([slug, c["url"], c["h1"], c["deal_filter"],
                        len(c["itin_ids"]), note])
            proposed += 1

    # retire suggestions for existing pages
    retire_file = DATA / "pages_retire_suggestions.csv"
    buildable = {"approved", "building", "built", "built-template", "live", "pilot"}
    retire = []
    for p in pages:
        if p.get("status") not in buildable:
            continue
        flt = p["deal_filter"].strip()
        count = sum(1 for r in live
                    if flt in {t.strip() for t in r.get("page_targets", "").split(";")}
                    and sails_soon(r, today))
        need = 1 if p.get("page_type") == "itinerary" else 3
        if count < need:
            retire.append((p["page_id"], p["url"], count, need))
    with open(retire_file, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["page_id", "url", "itinerary_count", "needed",
                    "suggested_action"])
        for pid, url, count, need in retire:
            w.writerow([pid, url, count, need,
                        "status=retire: 30-day grace with call CTA, then redirect to parent facet"])

    print(f"{proposed} combo(s) proposed -> {out_file}")
    for key, winner in dropped:
        print(f"  dedupe: {key} covers the same itineraries as {winner}; broader page wins")
    if retire:
        print(f"{len(retire)} page(s) below inventory threshold -> {retire_file}")
        for pid, url, count, need in retire:
            print(f"  RETIRE? {pid} {url}: {count}/{need} itineraries")
    print("structure-guard approves proposals into 09_pages.csv; nothing was auto-added.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
