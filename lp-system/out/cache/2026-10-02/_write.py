#!/usr/bin/env python3
"""Pass C 2026-10-02 writer: candidate diff + 03_itineraries.csv + 07_offers.csv.

Every value here comes from _final.json / _derived.json, which are built only
from the two official cruiseSearch responses fetched this run (cached beside
this script). Nothing is typed in from memory.
"""
import csv
import io
import json
import pathlib
import re

ROOT = pathlib.Path("/Users/lokesh29/cruiselineadvisors")
C = ROOT / "lp-system/out/cache/2026-10-02"
DATA = ROOT / "lp-system/data"
TODAY = "2026-10-02"
RETRIEVED = "A 2026-10-02T14:00:35Z / B 2026-10-02T14:00:52Z-14:01:19Z"
AGREE = ("Both independent fetches, the Galveston departure-port query and the "
         "fleet-wide by-ship query, return the same sailing set and agree to "
         "the cent on every month.")

fin = json.load(open(C / "_final.json"))
der = json.load(open(C / "_derived.json"))

# ------------------------------------------------- per-row notes (hand-written,
# every claim checked against _derived.json/_final.json for THIS run)
NOTES = {
 "i0003": ("group returns 7 sailings across 2027-08, 2027-09 and 2027-10, the same "
   "seven sail dates as the 2026-09-22 run. Row lead-ins re-derived from source: "
   "interior 1158.51 (2027-10, 2027-10-03), balcony 1359.51 (2027-10, 2027-10-03). "
   "Diffed against the stored overrides, 2027-08 is unchanged at i1349/b1549, "
   "2027-09 reprices higher in both classes, and in 2027-10 the interior falls "
   "while the balcony holds at 1359.51. " + AGREE),
 "i0004": ("group returns 6 sailings across 2027-08, 2027-09, 2027-10 and 2027-11, "
   "the same six sail dates as the 2026-09-22 run. Row lead-ins re-derived from "
   "source: interior 1629.46 (2027-09, 2027-09-25), balcony 1809.46 (2027-09, "
   "2027-09-25), both unchanged. Diffed against the stored overrides, 2027-09 and "
   "2027-10 are unchanged, 2027-08 rises one dollar in each class, and 2027-11 "
   "rises to i1718/b1909. " + AGREE),
 "i0005": ("group returns 1 sailing, 2026-10-17, down from 3. The 2026-10-03 and "
   "2026-10-12 departures no longer return from source although neither date has "
   "passed. The surviving sailing quotes interior 506.14 against 466.14 last run "
   "and returns a null balcony where it quoted 1046.64, so 2026-10 carries an "
   "interior-only token and price_balcony is left EMPTY on purpose: no sailing in "
   "this row publishes a balcony fare today, and validate.py's 'price missing' "
   "flag on that field is the accurate state. " + AGREE),
 "i0006": ("group returns 70 sailings across 19 months, 2026-10 to 2028-04. Row "
   "lead-ins re-derived from source: interior 368.94 (2027-01, 2027-01-09), balcony "
   "671.94 (2027-01, 2027-01-09). The single 2026-10 departure, 2026-10-31, now "
   "returns a balcony fare of 1036.06 where it returned null last run, so 2026-10 "
   "carries both tokens again and price_balcony is a real published floor. Diffed "
   "against the stored overrides, 6 of the 19 months are unchanged (2027-08, "
   "2027-10, 2027-11, 2027-12, 2028-01, 2028-02). " + AGREE),
 "i0007": ("group returns 39 sailings across 18 months, 2026-11 to 2028-04. Row "
   "lead-ins re-derived from source: interior 403.76 (2027-01, 2027-01-28), balcony "
   "699.05 (2027-10, 2027-10-21). The balcony lead-in is the same 699.05 as last "
   "run but now floors on 2027-10-21 rather than 2027-09-09. Diffed against the "
   "stored overrides, 6 of the 18 months are unchanged (2027-06, 2027-07, 2027-10, "
   "2027-11, 2027-12, 2028-01). " + AGREE),
 "i0008": ("group returns 2 sailings, both in 2026-10, down from 4. The 2026-09-24 "
   "departure has sailed and no longer returns; the 2026-10-08 departure no longer "
   "returns although its date has not passed. 2026-09 is dropped from sail_months, "
   "from the overrides and from season_note, and no September floor is carried "
   "forward. 2026-10 floors on 2026-10-26 at interior 542.98 and balcony 750.98, "
   "the same two values as last run; the other October departure, 2026-10-22, "
   "returns interior 616.55 and a null balcony. " + AGREE),
 "i0009": ("group returns 7 sailings across 2027-05, 2027-06 and 2027-07. The "
   "2026-10-04 departure no longer returns from source although its date has not "
   "passed, so 2026-10 is dropped from sail_months, from the overrides and from "
   "season_note and its interior floor is not carried forward. Row lead-ins "
   "re-derived from source: interior 677.50 (2027-05, 2027-05-02), balcony 745.50 "
   "(2027-05, 2027-05-02). The interior lead-in rounds to the same 678 as last run "
   "but comes from a different sailing: last run's 678.01 was the 2026-10-04 "
   "departure. 2027-05 falls in both classes; 2027-06 and 2027-07 hold their "
   "interiors and fall in balcony. " + AGREE),
 "i0010": ("group returns 28 sailings across 7 months, 2026-10 to 2027-04, the same "
   "28 sail dates as the 2026-09-22 run. Row lead-ins re-derived from source: "
   "interior 607.48 (2027-01, 2027-01-17), balcony 687.98 (2027-01, 2027-01-17). "
   "Diffed against the stored overrides, all seven months changed in at least one "
   "class. The 2026-10 balcony token rises from 729 to 1676 because 2026-10-25, "
   "which held the October balcony floor at 728.80 last run, now returns a null "
   "balcony, leaving 2026-10-18's 1676.32 as October's only balcony fare at "
   "source. " + AGREE + " The row balcony lead-in is unaffected; it sits in "
   "2027-01."),
 "i0011": ("UNVERIFIED: the group SY08GAL-3243125536 returns ZERO sailings today. "
   "It is absent from the Galveston departure-port query and from the fleet-wide "
   "Symphony query, and package code SY08W063 appears nowhere in either response. "
   "The 2026-10-10 departure that was the group's only sailing last run has not "
   "sailed but no longer returns from source. No fare could be verified this run, "
   "so sail_months, both prices, the overrides and the 2026-09-22 date_checked "
   "stamp are left exactly as last verified and the row is flagged UNVERIFIED so "
   "it cannot publish. Hand to research-registrar for a Pass A retire decision."),
 "i0012": ("group returns 1 sailing, 2028-02-04. Row lead-ins re-derived from "
   "source: interior 666.59, balcony 967.59, each about a dollar above last run's "
   "665.59 and 966.09. " + AGREE),
 "i0013": ("group returns 2 sailings, 2027-12-24 and 2028-04-15. Row lead-ins "
   "re-derived from source: interior 741.61 (2028-04, 2028-04-15), balcony 1042.11 "
   "(2028-04, 2028-04-15). Diffed against the stored overrides, both months are "
   "unchanged; re-verified from source and the stamp advanced. " + AGREE),
 "i0014": ("group returns 1 sailing, 2026-12-21, at interior 838.11 and balcony "
   "1238.11, both identical to the 2026-09-22 run; re-verified from source and the "
   "stamp advanced. " + AGREE),
 "i0015": ("group returns 7 sailings across 2027-05, 2027-06 and 2027-07, the same "
   "seven sail dates as the 2026-09-22 run. Row lead-ins re-derived from source: "
   "interior 1209.20 (2027-07, 2027-07-31), balcony 1409.70 (2027-07, 2027-07-31). "
   "Both lead-ins move off 2027-05-08 onto 2027-07-31: 2027-05-08, which held both "
   "floors last run at 985.20 and 1072.20, now quotes 1413.70 and 1466.70. The row "
   "balcony lead-in therefore rises 1072 to 1410, +31.5%, and the interior 985 to "
   "1209. 2027-06 and 2027-07 reprice lower in both classes. " + AGREE + " The "
   "move publishes."),
 "i0016": ("group returns 1 sailing, 2027-08-12. Row lead-ins re-derived from "
   "source: interior 1010.52, unchanged, and balcony 1602.52 against 1683.02 last "
   "run. " + AGREE),
 "i0017": ("group returns 23 sailings across 2027-11 to 2028-04, the same 23 sail "
   "dates as the 2026-09-22 run. Row lead-ins re-derived from source: interior "
   "1026.06 (2028-02, 2028-02-20) and balcony 1302.20 (2028-01, 2028-01-09); both "
   "round to the same 1026 and 1302 as last run. Diffed against the stored "
   "overrides, all six months changed in at least one class, the largest being "
   "2027-12, i1179 to i1226 and b1380 to b1438. " + AGREE),
 "i0018": ("group returns 1 sailing, 2027-08-08. Row lead-ins re-derived from "
   "source: interior 981.63 and balcony 1084.13, against 999.13 and 1099.63 last "
   "run. " + AGREE),
}

SEASON = {
 "i0008": "Mariner sails this route in Oct 2026",
 "i0009": "Summer 2027 season, May to Jul",
}

# ------------------------------------------------- read current CSV verbatim
raw = (DATA / "03_itineraries.csv").read_text(encoding="utf-8")
rows = list(csv.reader(io.StringIO(raw, newline="")))
header, body = rows[0], rows[1:]
ix = {name: i for i, name in enumerate(header)}


def pov(s):
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


def pct(old, new):
    if not old or new is None:
        return "n/a"
    return f"{100 * (new - int(old)) / int(old):+.1f}%"


cand = [["itin_id", "slug", "field", "old_value", "new_value", "pct_change",
         "queryA_value", "queryB_value", "queries_agree", "literal_value_seen",
         "sailing_id", "source_url", "retrieved_at", "status", "note"]]

changed_rows, verified_rows = [], []

for r in body:
    rid = r[ix["itin_id"]]
    if rid not in fin:
        continue                      # i0001/i0002 are not Galveston rows
    f, d = fin[rid], der[rid]
    slug, src = r[ix["slug"]], r[ix["source"]]

    def ev(field, old, new, literal, sail, note="", status="verified",
           qa="", qb="", agree="yes", p=None):
        cand.append([rid, slug, field, old, new,
                     p if p is not None else pct(old, new),
                     qa, qb, agree, literal, sail, src, RETRIEVED, status, note])

    if f["gone"]:
        ev("group", f"{d['nA']} sailing(s) at 2026-09-22", "0 sailings returned",
           "group id absent from both responses; no 'SY08W063' match in either",
           "2026-10-10 (last known sailing, not departed, no longer returned)",
           "group no longer returns from source; row frozen at its last verified "
           "values and 2026-09-22 stamp, flagged UNVERIFIED so it cannot publish",
           status="group-gone", qa="absent", qb="absent", agree="yes", p="n/a")
        r[ix["notes"]] = r[ix["notes"]] + f" | {TODAY}: " + NOTES[rid]
        changed_rows.append(rid)
        continue

    months = f["sail_months"]
    newov = f["ov"]
    oldov = r[ix["month_price_overrides"]]

    # price_interior
    oi = r[ix["price_interior"]].strip()
    ni = f["pi"]
    if str(ni) != oi:
        ev("price_interior", oi, ni,
           f'"price":{{"value":{f["ifloor_raw"]}}}',
           f'{f["ifloor_m"]} floor, {f["ifloor_d"]}',
           qa=f["ifloor_raw"], qb=f["ifloor_raw"])
    # price_balcony
    ob = r[ix["price_balcony"]].strip()
    nb = f["pb"]
    if nb is None:
        ev("price_balcony", ob, "",
           '"BALCONY" price is null on every returned sailing',
           f'{months[0]} (no balcony at source)',
           "left empty: this row publishes no balcony fare at source today; the "
           "month carries an interior-only token and months_without_balcony() "
           "stops any fallback",
           qa="null", qb="null", p="n/a")
    elif str(nb) != ob:
        ev("price_balcony", ob, nb,
           f'"price":{{"value":{f["bfloor_raw"]}}}',
           f'{f["bfloor_m"]} floor, {f["bfloor_d"]}',
           qa=f["bfloor_raw"], qb=f["bfloor_raw"])

    if newov != oldov:
        dropped = [m for m in pov(oldov) if m not in pov(newov)]
        note = f"{len(months)} month(s) re-derived from source"
        if dropped:
            note += f"; dropped: {', '.join(sorted(dropped))}"
        ev("month_price_overrides", oldov, newov, "n/a", note, p="n/a")

    oldsm = r[ix["sail_months"]]
    newsm = oldsm if oldsm == "year-round" else ";".join(months)
    if newsm != oldsm:
        ev("sail_months", oldsm, newsm, "n/a",
           "months returning from source: " + ", ".join(months), p="n/a")

    if rid in SEASON and SEASON[rid] != r[ix["season_note"]]:
        ev("season_note", r[ix["season_note"]], SEASON[rid], "n/a",
           "month purge made the previous wording false", p="n/a")

    ev("date_checked", r[ix["date_checked"]], TODAY, "n/a",
       f'row re-verified from source this run ({d["nA"]} sailing(s))', p="n/a")

    # ---- apply to the row
    r[ix["sail_months"]] = newsm
    r[ix["price_interior"]] = str(ni)
    r[ix["price_balcony"]] = "" if nb is None else str(nb)
    r[ix["month_price_overrides"]] = newov
    if rid in SEASON:
        r[ix["season_note"]] = SEASON[rid]
    r[ix["date_checked"]] = TODAY
    r[ix["notes"]] = r[ix["notes"]] + f" | {TODAY}: " + NOTES[rid]
    verified_rows.append(rid)

# ------------------------------------------------- write itineraries (CRLF)
buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\r\n")
w.writerows([header] + body)
(DATA / "03_itineraries.csv").write_bytes(buf.getvalue().encode("utf-8"))

# ------------------------------------------------- candidates
buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\r\n")
w.writerows(cand)
(ROOT / "lp-system/out/candidates-2026-10-02.csv").write_bytes(
    buf.getvalue().encode("utf-8"))

# ------------------------------------------------- offers (LF endings)
praw = (DATA / "07_offers.csv").read_text(encoding="utf-8")
orows = list(csv.reader(io.StringIO(praw, newline="")))
ohead, obody = orows[0], orows[1:]
oi = {n: i for i, n in enumerate(ohead)}
for o in obody:
    if o[oi["offer_id"]] == "o008":
        o[oi["show_banner"]] = "no"
        o[oi["status"]] = "expired"
obody.append([
  "o009", "rci",
  ("Royal Caribbean promotion, seen 2026-10-02: the line's own cruise-deals page "
   "is running a limited-time flash sale it labels the Score More Sale, listing up "
   "to $850 off, up to $100 more off Caribbean and West Coast sailings through "
   "April 2027, and 3rd and 4th guests sail free. Royal Caribbean's own listing "
   "dates the sale from 2026-10-02 to 2026-10-06 at 00:00 ET, so 2026-10-05 is its "
   "last full day. No other promotion appeared on the page in this fetch. Royal "
   "Caribbean sets the terms and decides which sailings and guests qualify; ask on "
   "the call."),
  "2026-10-02", "2026-10-05", "yes",
  "combo:royal-caribbean-galveston;line:royal-caribbean",
  "https://www.royalcaribbean.com/cruise-deals", "2026-10-02", "verified"])
buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\n")
w.writerows([ohead] + obody)
(DATA / "07_offers.csv").write_bytes(buf.getvalue().encode("utf-8"))

print("verified rows:", len(verified_rows), verified_rows)
print("frozen rows  :", len(changed_rows), changed_rows)
print("candidate evidence lines:", len(cand) - 1)
