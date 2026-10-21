#!/usr/bin/env python3
"""auto_rates.py — unattended Pass C fare refresh for the /go/ pages.

This is the scheduled, no-human version of the /rate-update skill. It exists
because the refresh gates in generate.py all run at BUILD time: nothing on a
deployed page expires by itself, so a missed run leaves stale fares live. The
cadence IS the safety mechanism, which makes "I forgot" a publishing risk.

WHAT IT DELIBERATELY DOES NOT DO
--------------------------------
It writes no prose. Every manual run so far produced a paragraph of narrative
per row, and twice qa-auditor caught that narrative asserting things about
previous runs that were not true. An unattended process cannot be trusted to
write history, so it does not: `notes` is left exactly as the humans left it
and the per-run evidence goes to out/auto-rates-<date>.csv instead. It also
never writes an offer. Offer text is a legal claim in our own words, so this
script can only RETIRE an offer whose end_date has passed (pure arithmetic)
and report that the promotions page moved.

THE GATE
--------
Two independently shaped official queries are fetched every run:

  A  filters "departurePort:GAL"   one call, every Galveston sailing
  B  filters "ship:<code>"         one call per ship, fleet-wide, then
                                   filtered back down to Galveston

Both must return the same sailing set and the same fare to the cent before a
value publishes. That agreement is the automated stand-in for a human going
back to source, and it is the only thing here that can promote a number.

Per row, the outcome is one of:

  publish  A and B agree on every month and class, and no published value
           moved more than SWING_PCT. New values, today's date_checked.
  hold     A and B disagree, their sailing sets differ, or something moved
           more than SWING_PCT. The row keeps its last verified values AND
           its older, honest date_checked stamp. Because the stamp does not
           advance, generate.py's 3-day fuse withholds that fare within three
           days on its own, so an un-actioned hold degrades to "Fare on
           request" rather than to a wrong price.
  frozen   the group is absent from both queries. Same freeze, plus
           auto_status is set so the row cannot publish at all.

A hold is per ROW, not per field: a row whose balcony is suspect does not get
to publish its interior either, because the two came from the same response.

Exit codes: 0 nothing needed / clean, 10 something was held or frozen and
wants a human, 2 the run could not be completed (fetch or parse failed, and
NOTHING was written).

Usage:
  python3 lp-system/scripts/auto_rates.py            # fetch, gate, write
  python3 lp-system/scripts/auto_rates.py --dry-run  # fetch, gate, write nothing
  python3 lp-system/scripts/auto_rates.py --offline   # reuse today's cache
"""

import argparse
import collections
import gzip
import csv
import datetime as dt
import io
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "lp-system" / "data"
OUT = ROOT / "lp-system" / "out"

ENDPOINT = "https://www.royalcaribbean.com/cruises/graph"
UA = "CruiseLineAdvisorsBot/1.0 (rate research; +https://cruiselineadvisors.com)"
# Two thresholds, not one. Operator ruling 2026-10-20, replacing the single
# 25% hold of 2026-10-17.
#
# REPORT_PCT  a move this big is worth telling you about, and publishes.
# HOLD_PCT    a move this big is not credible even with agreement, and holds.
#
# Why it changed: the 25% hold was costing more than it bought. This inventory
# reprices hard close to departure, which is the line clearing cabins and is
# completely normal: inside one week i0008's October interior went 557 -> 498
# -> 349 and i0010's November balcony 1057 -> 1360 -> 975, every step confirmed
# to the cent by both independent queries. Holding those meant the correct
# number never published, the stamp never advanced, and the fuse then withheld
# the fare entirely. The page went call-only on exactly its best-moving
# sailings while the stale figure stayed live until it timed out.
#
# The second query is the proof the 25% rule was asking for, so agreement
# publishes. HOLD_PCT stays as a ceiling for the case agreement cannot rule
# out: both queries reading the same upstream mistake, a decimal shift or a
# currency change, where the number is consistent and still wrong.
REPORT_PCT = 25.0
HOLD_PCT = 60.0

QUERY = (
    "query cruiseSearch($filters: String, $sort: CruiseSearchSort, "
    "$pagination: CruiseSearchPagination) { cruiseSearch(filters: $filters, "
    "sort: $sort, pagination: $pagination) { results { total cruises { id "
    "productViewLink sailings { id sailDate startDate endDate taxesAndFees "
    "{ value } taxesAndFeesIncluded stateroomClassPricing { stateroomClass "
    "{ id name } price { value currency { code } } } itinerary { name code "
    "totalNights departurePort { code } ship { code name } } } } } } }"
)


class RunFailed(Exception):
    """Raised before anything is written. Nothing on disk has changed."""


# ───────────────────────────────────────────────────────── fetch

def graph(filters, dest, cache_dir, offline):
    """One polite curl against the official endpoint.

    curl, not urllib: Python's SSL stack cannot complete Royal Caribbean's
    certificate chain on this machine, which is why collect.py's urllib path
    has never worked against this host.
    """
    if offline:
        # committed runs keep the raw responses gzipped (16x smaller, and this
        # job writes one every three days forever)
        if dest.exists():
            return json.loads(dest.read_text(encoding="utf-8")), "cache"
        gz = dest.with_suffix(dest.suffix + ".gz")
        if gz.exists():
            with gzip.open(gz, "rt", encoding="utf-8") as f:
                return json.load(f), "cache"
        raise RunFailed(f"--offline but no cached response for {filters}")

    payload = cache_dir / (dest.stem + "-payload.json")
    payload.write_text(json.dumps({
        "operationName": "cruiseSearch",
        "variables": {"filters": filters,
                      "pagination": {"count": 500, "skip": 0},
                      "sort": {"by": "RECOMMENDED", "order": "ASC"}},
        "query": QUERY,
    }), encoding="utf-8")

    proc = subprocess.run(
        ["curl", "-sS", "-m", "90", "--retry", "2", "--retry-delay", "5",
         "-o", str(dest), "-w", "%{http_code}", ENDPOINT,
         "-H", "content-type: application/json",
         "-H", "accept: application/json",
         "-H", f"user-agent: {UA}",
         "--data-binary", f"@{payload}"],
        capture_output=True, text=True, timeout=180)
    code = (proc.stdout or "").strip()
    if proc.returncode != 0 or code != "200":
        raise RunFailed(f"{filters}: curl rc={proc.returncode} http={code} "
                        f"{(proc.stderr or '').strip()[:200]}")
    try:
        doc = json.loads(dest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RunFailed(f"{filters}: response is not JSON ({exc})")
    if doc.get("errors"):
        raise RunFailed(f"{filters}: GraphQL errors {doc['errors'][:1]}")
    try:
        doc["data"]["cruiseSearch"]["results"]["cruises"]
    except (KeyError, TypeError):
        raise RunFailed(f"{filters}: response shape changed, no results.cruises")
    return doc, "fetched"


def ports_of(cfg):
    """Every departure port this job refreshes.

    _port was a single code when Galveston was the only port we priced. Miami
    and Port Canaveral joined on 2026-10-21, so the job reads _ports (slug ->
    code) and falls back to _port, which keeps an older config file working.
    """
    codes = list((cfg.get("_ports") or {}).values())
    if cfg.get("_port") and cfg["_port"] not in codes:
        codes.insert(0, cfg["_port"])
    return codes


def fetch_all(cache_dir, cfg, offline):
    """Query A once PER PORT, query B once per ship. Any failure aborts the run."""
    stamps = {}
    a_docs = []
    for code in ports_of(cfg):
        doc, how = graph(f"departurePort:{code}",
                         cache_dir / f"graph-departurePort-{code}.json",
                         cache_dir, offline)
        a_docs.append((code, doc))
        stamps[f"A:{code}"] = how
    a_doc = a_docs[0][1] if a_docs else None
    b_docs = {}
    for ship in cfg["_ships"]:
        b_docs[ship], how = graph(f"ship:{ship}",
                                  cache_dir / f"graph-ship-{ship}.json",
                                  cache_dir, offline)
        stamps[f"B:{ship}"] = how
    return a_docs, b_docs, stamps


# ───────────────────────────────────────────────────────── derive

def index(doc, port=None):
    """group id -> {sailDate -> {class -> price}} plus link/codes/nights."""
    out = {}
    for c in doc["data"]["cruiseSearch"]["results"]["cruises"]:
        for s in c["sailings"]:
            it = s["itinerary"]
            if port and it["departurePort"]["code"] != port:
                continue
            rec = out.setdefault(c["id"], {
                "sail": {}, "link": c.get("productViewLink", ""),
                "codes": set(), "nights": set(), "ship": set()})
            rec["sail"][s["sailDate"]] = {
                p["stateroomClass"]["id"]: (p.get("price") or {}).get("value")
                for p in s["stateroomClassPricing"] or []}
            rec["codes"].add(it["code"])
            rec["nights"].add(it["totalNights"])
            rec["ship"].add(it["ship"]["code"])
    return out


def by_month(rec):
    m = collections.defaultdict(dict)
    for d, pr in rec["sail"].items():
        m[d[:7]][d] = pr
    return m


def floor(sails, cls):
    """Cheapest published fare in a month for one class, and which sailing."""
    cands = [(pr[cls], d) for d, pr in sorted(sails.items())
             if pr.get(cls) is not None]
    return min(cands) if cands else (None, None)


def derive(a_idx, b_idx, groups, cutoff):
    """Per row: the month table both queries agree on, and why not if they don't."""
    out = {}
    for itin, gid in groups.items():
        ra, rb = a_idx.get(gid), b_idx.get(gid)
        row = {"gid": gid, "in_a": ra is not None, "in_b": rb is not None,
               "n_a": len(ra["sail"]) if ra else 0,
               "n_b": len(rb["sail"]) if rb else 0,
               "sails": sorted(ra["sail"]) if ra else [],
               "months": {}, "disagree": [], "dropped_past": []}
        if ra is None and rb is None:
            out[itin] = row
            continue
        ma, mb = (by_month(ra) if ra else {}), (by_month(rb) if rb else {})
        for mo in sorted(set(ma) | set(mb)):
            sa, sb = ma.get(mo, {}), mb.get(mo, {})
            if mo < cutoff:
                row["dropped_past"].append(mo)
                continue
            ai, aid = floor(sa, "INTERIOR")
            ab, abd = floor(sa, "BALCONY")
            bi, _ = floor(sb, "INTERIOR")
            bb, _ = floor(sb, "BALCONY")
            if sorted(sa) != sorted(sb):
                row["disagree"].append(
                    f"{mo} sailing sets differ (A {len(sa)}, B {len(sb)})")
            if ai != bi:
                row["disagree"].append(f"{mo} interior A={ai} B={bi}")
            if ab != bb:
                row["disagree"].append(f"{mo} balcony A={ab} B={bb}")
            row["months"][mo] = {"i": ai, "i_sail": aid, "b": ab, "b_sail": abd,
                                 "sails": sorted(sa)}
        # the row's own lead-in fares: cheapest month floor in each class
        for cls, key in (("i", "interior"), ("b", "balcony")):
            cands = [(v[cls], mo) for mo, v in row["months"].items()
                     if v[cls] is not None]
            best = min(cands) if cands else (None, None)
            row[f"lead_{key}"] = best[0]
            row[f"lead_{key}_month"] = best[1]
        out[itin] = row
    return out


def tokens(months):
    """month_price_overrides text, and the months that survive into it."""
    toks, keep = [], []
    for mo in sorted(months):
        v = months[mo]
        parts = []
        if v["i"] is not None:
            parts.append(f"i{round(v['i'])}")
        if v["b"] is not None:
            parts.append(f"b{round(v['b'])}")
        if not parts:
            continue           # no publishable fare in either class, month drops
        keep.append(mo)
        toks.append(mo + ":" + "|".join(parts))
    return "|".join(toks), keep


def last_sail_table(months):
    """month_last_sail: the date each month's final sailing leaves port."""
    return ";".join(f"{mo}:{max(months[mo]['sails'])}"
                    for mo in sorted(months) if months[mo]["sails"])


# ───────────────────────────────────────────────────────── gate

def parse_overrides(s):
    out, cur = {}, None
    for tok in s.split("|"):
        tok = tok.strip()
        if not tok:
            continue
        m = re.match(r"(\d{4}-\d{2}):([ib])(\d+)$", tok)
        if m:
            cur = m.group(1)
            out.setdefault(cur, {})[m.group(2)] = int(m.group(3))
            continue
        m = re.match(r"([ib])(\d+)$", tok)
        if m and cur:
            out.setdefault(cur, {})[m.group(1)] = int(m.group(2))
    return out


def swing(old, new):
    if not old or new is None:
        return None
    try:
        o = int(old)
    except (TypeError, ValueError):
        return None
    if o == 0:
        return None
    return 100.0 * (round(new) - o) / o


def gate(row, d):
    """publish / hold / frozen, with every reason spelled out."""
    if not d["in_a"] and not d["in_b"]:
        return "frozen", ["group absent from both queries"], {}

    reasons = list(d["disagree"])
    newov, keep = tokens(d["months"])

    moves = []
    old_ov = parse_overrides(row["month_price_overrides"])
    new_ov = parse_overrides(newov)
    for mo in sorted(set(old_ov) & set(new_ov)):
        for cls in "ib":
            if cls in old_ov[mo] and cls in new_ov[mo]:
                pc = swing(old_ov[mo][cls], new_ov[mo][cls])
                if pc is not None:
                    moves.append((abs(pc), f"{mo} {cls} {old_ov[mo][cls]}"
                                           f"->{new_ov[mo][cls]} {pc:+.1f}%"))
    for field, val in (("price_interior", d["lead_interior"]),
                       ("price_balcony", d["lead_balcony"])):
        pc = swing(row[field].strip(), val)
        if pc is not None:
            moves.append((abs(pc), f"{field} {row[field].strip()}"
                                   f"->{round(val)} {pc:+.1f}%"))

    # over HOLD_PCT the row does not publish; between the two it publishes and
    # is reported. Both lists are built from the same moves.
    reasons += [f"moved more than {HOLD_PCT:.0f}%, not published: {t}"
                for mag, t in moves if mag > HOLD_PCT]
    noted = [f"moved more than {REPORT_PCT:.0f}%: {t}" for mag, t in moves
             if REPORT_PCT < mag <= HOLD_PCT]

    proposed = {
        "sail_months": (row["sail_months"] if row["sail_months"] == "year-round"
                        else ";".join(keep)),
        "month_last_sail": last_sail_table(d["months"]),
        "month_price_overrides": newov,
        "price_interior": ("" if d["lead_interior"] is None
                           else str(round(d["lead_interior"]))),
        "price_balcony": ("" if d["lead_balcony"] is None
                          else str(round(d["lead_balcony"]))),
    }
    decision = "hold" if reasons else "publish"
    # a move both queries confirmed still gets reported even when it publishes,
    # so the notification never hides it
    return decision, reasons or noted, proposed


# ───────────────────────────────────────────────────────── write

def read_rows(path):
    raw = path.read_text(encoding="utf-8")
    rows = list(csv.reader(io.StringIO(raw, newline="")))
    return rows[0], rows[1:]


def write_rows(path, header, body, eol="\r\n"):
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator=eol).writerows([header] + body)
    path.write_bytes(buf.getvalue().encode("utf-8"))


def retire_offers(today, dry):
    """Pure date arithmetic: an offer past its end_date stops showing.

    This script never ADDS an offer. Offer copy is a legal claim written in
    our own words and it is not something an unattended process should author.
    """
    path = DATA / "07_offers.csv"
    header, body = read_rows(path)
    ix = {n: i for i, n in enumerate(header)}
    retired = []
    for o in body:
        end = o[ix["end_date"]].strip()
        if (end and end < today and o[ix["show_banner"]].strip() == "yes"):
            o[ix["show_banner"]] = "no"
            o[ix["status"]] = "expired"
            retired.append(f"{o[ix['offer_id']]} (ended {end})")
    if retired and not dry:
        write_rows(path, header, body, eol="\n")
    return retired


# ───────────────────────────────────────────────────────── run

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="fetch and gate, write nothing")
    ap.add_argument("--offline", action="store_true",
                    help="reuse today's cached responses instead of fetching")
    ap.add_argument("--date", default=None, help="override today (testing)")
    args = ap.parse_args()

    today = args.date or dt.date.today().isoformat()
    cutoff = today[:7]
    cfg = json.loads((DATA / "08_group_ids.json").read_text(encoding="utf-8"))
    groups = cfg["groups"]

    cache_dir = OUT / "cache" / today
    cache_dir.mkdir(parents=True, exist_ok=True)

    started = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        a_doc, b_docs, how = fetch_all(cache_dir, cfg, args.offline)
    except (RunFailed, subprocess.TimeoutExpired) as exc:
        print(f"FETCH FAILED, nothing written: {exc}", file=sys.stderr)
        report = {"date": today, "ok": False, "error": str(exc),
                  "rows": {}, "retired_offers": []}
        (OUT / f"auto-rates-{today}.json").write_text(
            json.dumps(report, indent=1), encoding="utf-8")
        return 2

    # Query A is now one response per port; merge their indexes. Query B is per
    # ship and spans ports, so it is filtered to the ports we actually price
    # rather than to one of them.
    a_idx = {}
    for _code, _doc in a_doc:
        a_idx.update(index(_doc))
    b_idx = {}
    _codes = set(ports_of(cfg))
    for ship, doc in b_docs.items():
        for _code in _codes:
            b_idx.update(index(doc, port=_code))
    derived = derive(a_idx, b_idx, groups, cutoff)
    (cache_dir / "_derived.json").write_text(
        json.dumps(derived, indent=1, default=str), encoding="utf-8")

    header, body = read_rows(DATA / "03_itineraries.csv")
    if "auto_status" not in header:
        header.append("auto_status")
        for r in body:
            r.append("")
    ix = {n: i for i, n in enumerate(header)}

    cand = [["itin_id", "field", "old_value", "new_value", "pct_change",
             "queryA", "queryB", "decision", "reason", "retrieved_at"]]
    rows_report, changed = {}, 0

    for r in body:
        rid = r[ix["itin_id"]]
        if rid not in derived:
            continue                      # i0001/i0002 are not Galveston rows
        d = derived[rid]
        decision, reasons, proposed = gate({k: r[ix[k]] for k in ix}, d)
        moved = []

        if decision == "publish":
            for field, val in proposed.items():
                if r[ix[field]] != val:
                    pc = (swing(r[ix[field]], float(val))
                          if field.startswith("price_") and val else None)
                    cand.append([rid, field, r[ix[field]], val,
                                 "" if pc is None else f"{pc:+.1f}%",
                                 "agree", "agree", "publish", "", started])
                    moved.append(f"{field}: {r[ix[field]] or '(empty)'} -> "
                                 f"{val or '(empty)'}")
                    r[ix[field]] = val
            cand.append([rid, "date_checked", r[ix["date_checked"]], today, "",
                         f"{d['n_a']} sailings", f"{d['n_b']} sailings",
                         "publish", "both queries agree", started])
            r[ix["date_checked"]] = today
            r[ix["auto_status"]] = (f"ok {today}" + (f" (reported: {'; '.join(reasons)})"
                                                      if reasons else ""))
            changed += 1 if moved else 0
        else:
            cand.append([rid, "(row)", f"held at {r[ix['date_checked']]}",
                         "(unchanged)", "", f"{d['n_a']} sailings",
                         f"{d['n_b']} sailings", decision,
                         "; ".join(reasons), started])
            r[ix["auto_status"]] = f"{decision} {today}: {'; '.join(reasons)}"

        rows_report[rid] = {"decision": decision, "reasons": reasons,
                            "moved": moved, "sailings": d["n_a"],
                            "stamp": r[ix["date_checked"]]}

    untracked = sorted(set(a_idx) - set(groups.values()))
    retired = retire_offers(today, args.dry_run)

    if not args.dry_run:
        write_rows(DATA / "03_itineraries.csv", header, body)
        write_rows(OUT / f"auto-rates-{today}.csv", cand[0], cand[1:])

    report = {
        "date": today, "ok": True, "started": started, "fetch": how,
        "published": sorted(k for k, v in rows_report.items()
                            if v["decision"] == "publish"),
        "held": sorted(k for k, v in rows_report.items()
                       if v["decision"] == "hold"),
        "frozen": sorted(k for k, v in rows_report.items()
                         if v["decision"] == "frozen"),
        "fields_changed": changed,
        "notable": sorted(k for k, v in rows_report.items()
                          if v["decision"] == "publish" and v["reasons"]),
        "untracked_groups": untracked,
        "retired_offers": retired,
        "rows": rows_report,
    }
    (OUT / f"auto-rates-{today}.json").write_text(
        json.dumps(report, indent=1), encoding="utf-8")

    # Keep the raw responses as evidence but not at full size: a 470 KB cache
    # every three days is 56 MB a year in a repo the host re-clones on every
    # deploy. Gzipped it is about 30 KB. _derived.json stays plain text,
    # because that is the file anyone actually reads to check a number.
    for f in sorted(cache_dir.glob("graph-*.json")):
        if f.name.endswith("-payload.json"):
            f.unlink()                 # the query is in this file, not evidence
            continue
        with open(f, "rb") as src, gzip.open(str(f) + ".gz", "wb", 9) as dst:
            dst.write(src.read())
        f.unlink()

    print(f"published {len(report['published'])}  held {len(report['held'])}  "
          f"frozen {len(report['frozen'])}  rows with new values {changed}")
    for rid in report["held"] + report["frozen"]:
        print(f"  {rid}: {rows_report[rid]['decision']} "
              f"(stamp stays {rows_report[rid]['stamp']}) "
              f"- {'; '.join(rows_report[rid]['reasons'])}")
    for rid in report["notable"]:
        print(f"  {rid}: published, both queries agree, worth a look "
              f"- {'; '.join(rows_report[rid]['reasons'])}")
    if untracked:
        print(f"  untracked groups at source: {', '.join(untracked)}")
    for o in retired:
        print(f"  offer retired: {o}")

    return 10 if (report["held"] or report["frozen"] or untracked) else 0


if __name__ == "__main__":
    sys.exit(main())
