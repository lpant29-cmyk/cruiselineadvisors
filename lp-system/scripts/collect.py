#!/usr/bin/env python3
"""collect.py — data collection for the ads-LP system (Blueprint Part 5,
Playbook §2 three-pass model).

Pass C (weekly, default)   : fetch each tracked itinerary's source URL,
                             cache the response, auto-extract candidate
                             fares, write a candidate diff with evidence.
Pass A (monthly, worklist) : emit the enumeration worklist + current
                             itinerary slugs so research-registrar can
                             diff new/retired itineraries per line.
Pass B (on demand, worklist): emit enrichment worklist (itineraries with
                             no day-by-day rows yet).

The script never writes into lp-system/data/ — everything lands in
lp-system/out/ as candidates for qa-auditor to gate.

Usage:
  python3 lp-system/scripts/collect.py --pass C [--line rci] [--delay 10]
  python3 lp-system/scripts/collect.py --pass A --line rci
  python3 lp-system/scripts/collect.py --pass B --line rci
"""

import argparse
import csv
import datetime as dt
import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "lp-system" / "data"
OUT = ROOT / "lp-system" / "out"
UA = "CruiseLineAdvisorsBot/1.0 (rate research; contact: site owner)"

# Rows whose source is one of these are not fetchable price sources and
# must be flagged for manual verification, never auto-updated.
NON_URL_SOURCES = {"", "public-site", "seed-example-VERIFY-BEFORE-PUBLISH"}

PRICE_RE = re.compile(r"\$\s?([1-9]\d{2,4})(?:[.,]\d{2})?")


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def today():
    return dt.date.today().isoformat()


def fetch(url, cache_dir, key, delay):
    """Polite sequential fetch with an on-disk cache (one file per row per day)."""
    cache_file = cache_dir / f"{key}.html"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8", errors="replace"), "cache"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    time.sleep(delay)  # rate limit BEFORE the request, sequential by design
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    cache_file.write_text(body, encoding="utf-8")
    return body, "live"


def pass_c(rows, line_filter, delay):
    run_date = today()
    cache_dir = OUT / "cache" / run_date
    cache_dir.mkdir(parents=True, exist_ok=True)
    out_file = OUT / f"candidates-{run_date}.csv"

    fields = [
        "itin_id", "name", "source", "fetch_status",
        "price_interior_current", "price_balcony_current",
        "prices_found_on_page", "candidate_interior", "candidate_balcony",
        "date_checked_current", "retrieved_at", "needs_manual", "note",
    ]
    written = 0
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            if line_filter and row["line_id"] != line_filter:
                continue
            rec = {
                "itin_id": row["itin_id"],
                "name": row["name"],
                "source": row["source"],
                "price_interior_current": row["price_interior"],
                "price_balcony_current": row["price_balcony"],
                "date_checked_current": row["date_checked"],
                "retrieved_at": dt.datetime.now().isoformat(timespec="seconds"),
            }
            src = row["source"].strip()
            if not src.startswith("http"):
                rec.update(fetch_status="not-a-url", needs_manual="yes",
                           note=f"source '{src or 'empty'}' is not fetchable; "
                                "pricing-scout must verify by hand")
                w.writerow(rec)
                written += 1
                continue
            try:
                body, status = fetch(src, cache_dir, row["itin_id"], delay)
                prices = sorted({int(m) for m in PRICE_RE.findall(body)})
                prices = [p for p in prices if 99 <= p <= 25000]
                rec["fetch_status"] = status
                rec["prices_found_on_page"] = ";".join(map(str, prices[:20]))
                # Heuristic only: the lowest sane price is the interior
                # candidate. pricing-scout confirms every value by reading
                # the cached page; qa-auditor re-verifies a sample.
                rec["candidate_interior"] = prices[0] if prices else ""
                rec["needs_manual"] = "no" if prices else "yes"
                rec["note"] = "" if prices else "no price pattern found; read cached page"
            except Exception as e:  # fetch failure is a flag, never a guess
                rec.update(fetch_status="error", needs_manual="yes", note=str(e))
            w.writerow(rec)
            written += 1
    print(f"Pass C: {written} rows -> {out_file}")
    print(f"Raw pages cached in {cache_dir}")
    print("Next: pricing-scout reads needs_manual rows, confirms candidates, "
          "writes the final candidate diff; qa-auditor gates.")


def pass_a(rows, line_filter):
    """Enumeration worklist: what exists now, so the registrar can diff."""
    lines = read_csv(DATA / "01_lines.csv")
    run_date = today()
    out_file = OUT / f"passA-worklist-{run_date}.md"
    OUT.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Pass A enumeration worklist — {run_date}\n\n")
        for line in lines:
            if line_filter and line["line_id"] != line_filter:
                continue
            if line.get("page_status") not in ("build", "live"):
                continue
            current = [r for r in rows if r["line_id"] == line["line_id"]]
            f.write(f"## {line['line_name']} ({line['line_id']})\n")
            f.write(f"Currently tracked itineraries: {len(current)}\n\n")
            f.write("Walk the line's public find-a-cruise listings port by port. "
                    "For each active itinerary record: name, ship(s), departure "
                    "port, nights, destination, sail months, public detail URL "
                    "(becomes the row's source). Diff against:\n\n")
            for r in current:
                f.write(f"- {r['slug']} ({r['port_slug']}, {r['nights']}n) src={r['source']}\n")
            f.write("\n")
    print(f"Pass A worklist -> {out_file}")


def pass_b(rows, line_filter):
    """Enrichment worklist: itineraries with no day-by-day rows yet."""
    days = read_csv(DATA / "04_itinerary_days.csv")
    have_days = {d["itin_id"] for d in days}
    missing = [r for r in rows
               if r["itin_id"] not in have_days
               and (not line_filter or r["line_id"] == line_filter)]
    run_date = today()
    out_file = OUT / f"passB-worklist-{run_date}.md"
    OUT.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Pass B enrichment worklist — {run_date}\n\n")
        f.write("Itineraries missing day-by-day rows (04_itinerary_days.csv). "
                "From each source URL extract: per-day ports, arrive/depart, "
                "private-island flag, quad availability. Create missing "
                "05_ports_content rows in OUR OWN words.\n\n")
        for r in missing:
            f.write(f"- {r['itin_id']} {r['slug']} src={r['source']}\n")
    print(f"Pass B: {len(missing)} itineraries need enrichment -> {out_file}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pass", dest="pass_", choices=["A", "B", "C"], default="C")
    ap.add_argument("--line", help="restrict to one line_id (e.g. rci)")
    ap.add_argument("--delay", type=float, default=10.0,
                    help="seconds between fetches (Pass C, polite default 10)")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    rows = read_csv(DATA / "03_itineraries.csv")
    if args.pass_ == "C":
        pass_c(rows, args.line, args.delay)
    elif args.pass_ == "A":
        pass_a(rows, args.line)
    else:
        pass_b(rows, args.line)


if __name__ == "__main__":
    sys.exit(main())
