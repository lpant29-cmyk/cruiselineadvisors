#!/usr/bin/env python3
"""Pass C 2026-10-16 writer: candidate diff + 03_itineraries.csv + 07_offers.csv.

Every number here comes from _final.json / _derived.json, which are built only
from the two independently shaped official cruiseSearch responses fetched this
run (cached beside this script), plus cruise-deals.html for the offer.
Nothing is typed from memory.
"""
import csv
import io
import json
import pathlib
import re

ROOT = pathlib.Path("/Users/lokesh29/cruiselineadvisors")
C = ROOT / "lp-system/out/cache/2026-10-16"
DATA = ROOT / "lp-system/data"
TODAY = "2026-10-16"
RETRIEVED = "A 2026-10-16T10:41:51Z / B 2026-10-16T10:42:09Z-10:42:20Z"
AGREE = ("Both independent fetches, the Galveston departure-port query and the "
         "fleet-wide by-ship query, return the same sailing set and agree to "
         "the cent on every month.")

fin = json.load(open(C / "_final.json"))
der = json.load(open(C / "_derived.json"))

# ------------------------------------------------- per-row notes. Every claim
# below was diffed against this run's _derived.json and the 2026-10-12 cached
# response; no claim is carried over untested.
NOTES = {
 "i0003": ("group returns the same 7 sailings across 2027-08, 2027-09 and 2027-10 "
   "as the 2026-10-12 run; nothing was added or lost. Row lead-ins re-derived from "
   "source: interior 1168.51 (2027-10, 2027-10-31), balcony 1359.51 (2027-10, "
   "2027-10-03, unchanged on that same sailing). The interior lead-in moves off "
   "2027-10-17 onto 2027-10-31, which fell 1230.01 to 1168.51 while 2027-10-17 fell "
   "1200.01 to 1178.01. Diffed against the stored overrides, two month-class tokens "
   "moved: the 2027-08 balcony rises 1609 to 1679 (2027-08-22, 1608.96 to 1678.96, "
   "that month's only mover) and the 2027-10 interior falls 1200 to 1169. 2027-09 is "
   "unchanged in both classes. " + AGREE),
 "i0004": ("group returns the same 6 sailings across 2027-08, 2027-09, 2027-10 and "
   "2027-11 as the 2026-10-12 run. Row lead-ins re-derived from source and unchanged: "
   "interior 1648.96 and balcony 1830.46, both still on 2027-10-23. All four months "
   "are unchanged in both classes. Two non-floor sailings did move, both interior-only: "
   "2027-09-11 fell 1699.93 to 1675.43 and 2027-10-09 fell 1800.46 to 1716.96, each "
   "still above its month's floor, so no token changes. Every balcony fare in the group "
   "is identical to last run. Re-verified from source and the stamp advanced. " + AGREE),
 "i0005": ("group STILL returns its one remaining sailing, 2026-10-17, which departs "
   "tomorrow. It was not withdrawn at 1 day out. Mariner of the Seas has exactly three "
   "Galveston departures left at source, 2026-10-17 here plus 2026-10-22 and 2026-10-26 "
   "on i0008; the fleet-wide Mariner query returns 50 itinerary groups and 97 sailings "
   "in total, of which exactly 3 leave Galveston, and its New Orleans season starts "
   "2026-11-01 (48 MSY departures), consistent with the permanent Galveston exit after "
   "2026-10-26. "
   "The 2026-10-17 interior rose 700.14 to 740.14, +5.7%. BALCONY has RETURNED on this "
   "sailing: it was null in both fetches last run and now quotes 1299.64 in both, so "
   "2026-10 gains a balcony token and price_balcony goes from empty to 1300. Its "
   "OUTSIDE fare moved the other way, 1050.14 to null. " + AGREE),
 "i0006": ("group returns 69 sailings, one fewer than the 70 it returned on 2026-10-12: "
   "the 2026-10-31 departure, which quoted interior 544.06 last run, is GONE from both "
   "fetches. It had not sailed yet (today is 2026-10-16) and the cause of its "
   "disappearance is unknown; it is simply no longer offered. It was this row's only "
   "October sailing, so 2026-10 drops out of month_price_overrides entirely and the "
   "earliest returning sailing is now 2026-11-09. season_note is corrected from Oct 2026 "
   "to Nov 2026 for that reason. Row lead-ins re-derived from source: interior 359.94 "
   "(2027-01, 2027-01-09, down from 394.44 on that sailing) and balcony 592.94 (2027-01, "
   "2027-01-23, down from 666.94 on that sailing); the balcony lead-in moves out of "
   "2026-12 into 2027-01. 2026-11-09 now returns a balcony of 1153.28 where it returned "
   "null last run, so no month in this row is balcony-null today. 7 of the 18 remaining "
   "months moved in at least one class (2026-11, 2026-12, 2027-01 to 2027-04 and "
   "2027-06, whose interior is unchanged at 831.10 while its balcony fell 1078 to 1056); "
   "the other 11, 2027-05, 2027-07 to 2027-12 and 2028-01 to 2028-04, are unchanged in "
   "both classes. " + AGREE),
 "i0007": ("group returns the same 39 sailings across 18 months, 2026-11 to 2028-04, as "
   "the 2026-10-12 run. Row lead-ins re-derived from source: interior 394.76 (2027-01, "
   "2027-01-28, down from 423.76 on that same sailing) and balcony 680.31 (2027-04, "
   "2027-04-22, down from 807.31 on that sailing); the balcony lead-in moves out of "
   "2027-10 into 2027-04. BOTH 2026-11 sailings, 2026-11-05 and 2026-11-19, now return a "
   "null BALCONY where they returned 1146.09 and 1366.49 last run, so 2026-11 becomes an "
   "interior-only token at i640 and its stored b1146 is removed. price_balcony is "
   "deliberately NOT cleared, because 680.31 is a real published floor in 2027-04 and "
   "months_without_balcony() suppresses the balcony on 2026-11 alone. In 2026-12 the "
   "balcony/interior inversion reported last run is gone: 2026-12-03's interior fell "
   "895.12 to 775.62 and its balcony rose 799.62 to 888.12, so that month's balcony floor "
   "now sits above its interior floor again. 6 of the 18 months moved (2026-11, 2026-12 "
   "and 2027-01 to 2027-04); the other 12, 2027-05 to 2027-12 and 2028-01 to 2028-04, are "
   "unchanged in both classes. " + AGREE),
 "i0008": ("group returns the same 2 sailings, 2026-10-22 and 2026-10-26, as the "
   "2026-10-12 run; these are the last two of Mariner of the Seas' three remaining "
   "Galveston departures and 2026-10-26 is the final one before the ship leaves Galveston "
   "permanently. 2026-10-26 has regained an INTERIOR fare, 711.98, where it returned null "
   "last run, but the month's interior floor stays on 2026-10-22, which rose 549.55 to "
   "557.05, +1.4%. The balcony floor stays on 2026-10-26 and rose 799.48 to 908.98, "
   "+13.8%; 2026-10-22's balcony also rose, 899.05 to 967.05. No month in this row is "
   "null in either class today. " + AGREE),
 "i0009": ("group returns the same 7 sailings across 2027-05, 2027-06 and 2027-07 as the "
   "2026-10-12 run. Row lead-ins re-derived from source: interior 659.00 and balcony "
   "735.00, both on 2027-05-02, the same sailing as last run, where the interior fell "
   "671.00 to 659.00 and the balcony rose 697.00 to 735.00. Two months moved: 2027-05 "
   "(i671 to i659, b697 to b735) and 2027-07, whose interior rose 1002 to 1026 on "
   "2027-07-25 with its balcony unchanged at 1064.00. 2027-06 is unchanged in both "
   "classes. " + AGREE),
 "i0010": ("group returns the same 28 sailings across 2026-10 to 2027-04 as the "
   "2026-10-12 run. Row lead-ins re-derived from source: interior 607.44 and balcony "
   "651.44, both on 2027-02-28, where the interior fell 626.44 to 607.44 and the balcony "
   "674.94 to 651.44; the interior lead-in moves out of 2027-01 into 2027-02. All seven "
   "months moved in at least one class. Three balcony tokens moved more than 25%: "
   "2026-10 falls 1024 to 697, -31.9%, because 2026-10-18's balcony fell 1079.82 to "
   "697.32 while 2026-10-25's rose 1024.30 to 1832.30; 2026-11 rises 1057 to 1360, "
   "+28.7%, on 2026-11-29 (1057.40 to 1359.90); and 2026-12 rises 1045 to 1564, +49.7%, "
   "on 2026-12-06 (1044.90 to 1564.40). The 2026-10 interior token rises 699 to 899, "
   "+28.6%, because 2026-10-18 now returns a null INTERIOR, leaving 2026-10-25's 899.30 "
   "as the month floor; so in 2026-10 the balcony floor (2026-10-18) sits below the "
   "interior floor (2026-10-25), on two different sailings, and both fetches agree to the "
   "cent on both numbers, so the month publishes as returned rather than being held. "
   "2026-11-01, 2026-12-06 and 2026-12-20 also return null interiors, and 2026-11-15 a "
   "null balcony, but each of those months keeps a real floor in both classes from "
   "another sailing. " + AGREE),
 "i0012": ("group returns its 1 sailing, 2028-02-04, at interior 666.59 and balcony "
   "967.59, both identical to the 2026-10-12 run; re-verified from source and the stamp "
   "advanced. " + AGREE),
 "i0013": ("group returns the same 2 sailings, 2027-12-24 and 2028-04-15, and all four "
   "fares are identical to the 2026-10-12 run: 2027-12-24 interior 1096.72 and balcony "
   "1469.22, 2028-04-15 interior 741.61 and balcony 1042.11. Both months and both row "
   "lead-ins unchanged; re-verified from source and the stamp advanced. " + AGREE),
 "i0014": ("group returns its 1 sailing, 2026-12-21. Both classes fell on that sailing: "
   "interior 889.61 to 810.61, -8.9%, and balcony 1238.11 to 1153.11, -6.9%. " + AGREE),
 "i0015": ("group returns the same 7 sailings across 2027-05, 2027-06 and 2027-07 as the "
   "2026-10-12 run. Row lead-ins re-derived from source: interior 1238.20 and balcony "
   "1409.70, both still on 2027-07-31, where the interior rose 1209.20 to 1238.20 and the "
   "balcony is unchanged. Two months moved: 2027-06 (i1440 to i1410 and b1484 to b1473, "
   "both on 2027-06-19) and 2027-07 (interior only, 1209 to 1238). 2027-05 is unchanged "
   "in both classes. " + AGREE),
 "i0016": ("group returns its 1 sailing, 2027-08-12. Interior rose 1062.52 to 1162.52, "
   "+9.4%, and balcony 1693.02 to 1793.02, +5.9%. " + AGREE),
 "i0017": ("group returns the same 23 sailings across 2027-11 to 2028-04 as the "
   "2026-10-12 run. Row lead-ins re-derived from source and unchanged: interior 1101.70 "
   "and balcony 1302.20, both still on 2028-01-09. 2027-11 is the only month whose tokens "
   "moved, i1217 to i1266 and b1400 to b1449, both on 2027-11-28 (1216.70 to 1266.20 and "
   "1399.70 to 1449.20); 2027-11-14's interior fell 1349.81 to 1266.31, which is above "
   "the new floor. 2027-12 and 2028-01 to 2028-04 are unchanged in both classes. "
   + AGREE),
 "i0018": ("group returns its 1 sailing, 2027-08-08. Interior is unchanged at 981.63; "
   "balcony fell 1074.63 to 1072.63, -0.2%. " + AGREE),
}

# season_note edits. i0006 loses its only October sailing this run (2026-10-31
# gone from source), so its 2026-10 month token disappears and the stored
# "Oct 2026" wording is now false. No other Galveston row's month set changed.
SEASON = {
 "i0006": "Sails continuously Nov 2026 through Apr 2028",
}

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

frozen_rows, verified_rows = [], []

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
        ev("group", "0 sailings at 2026-09-22 (frozen)", "0 sailings returned",
           "group id absent from both responses; no 'SY08W063' match in either",
           "none (2026-10-10, its last known sailing, passed before this run)",
           "third consecutive run with zero sailings; the group has NOT returned "
           "from source. Row stays frozen at its last verified values and its "
           "2026-09-22 stamp, flagged UNVERIFIED so it cannot publish",
           status="group-gone", qa="absent", qb="absent", agree="yes", p="n/a")
        r[ix["notes"]] = r[ix["notes"]] + f" | {TODAY}: " + (
          "group SY08GAL-3243125536 again returns zero sailings. It is absent from "
          "the Galveston departure-port query and from the fleet-wide Symphony "
          "query, and package code SY08W063 appears in neither response. This is "
          "the third consecutive run with the group gone; it has NOT returned. "
          "sail_months, both prices, the overrides and the 2026-09-22 date_checked "
          "stamp are left exactly as last verified and the row stays flagged "
          "UNVERIFIED so it cannot publish. Still awaiting a Pass A retire "
          "decision from research-registrar.")
        frozen_rows.append(rid)
        continue

    months = f["sail_months"]
    newov = f["ov"]
    oldov = r[ix["month_price_overrides"]]

    oi = r[ix["price_interior"]].strip()
    ni = f["pi"]
    if str(ni) != oi:
        ev("price_interior", oi, ni,
           f'"price":{{"value":{f["ifloor_raw"]}}}',
           f'{f["ifloor_m"]} floor, {f["ifloor_d"]}',
           qa=f["ifloor_raw"], qb=f["ifloor_raw"])

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
           qa=f["bfloor_raw"], qb=f["bfloor_raw"],
           p=pct(ob, nb) if ob else "n/a (was empty)")

    if newov != oldov:
        o, n = pov(oldov), pov(newov)
        dropped = [m for m in o if m not in n]
        nullified = [f"{m}:{c}" for m in sorted(set(o) & set(n))
                     for c in "ib" if c in o[m] and c not in n[m]]
        appeared = [f"{m}:{c}" for m in sorted(set(o) & set(n))
                    for c in "ib" if c not in o[m] and c in n[m]]
        note = f"{len(months)} month(s) re-derived from source"
        if dropped:
            note += f"; months dropped: {', '.join(sorted(dropped))}"
        if nullified:
            note += f"; class token removed (null at source): {', '.join(nullified)}"
        if appeared:
            note += f"; class token returned at source: {', '.join(appeared)}"
        ev("month_price_overrides", oldov, newov, "n/a", note, p="n/a")

    oldsm = r[ix["sail_months"]]
    newsm = oldsm if oldsm == "year-round" else ";".join(months)
    if newsm != oldsm:
        ev("sail_months", oldsm, newsm, "n/a",
           "months returning from source: " + ", ".join(months), p="n/a")

    if rid in SEASON and SEASON[rid] != r[ix["season_note"]]:
        ev("season_note", r[ix["season_note"]], SEASON[rid], "n/a",
           "the row's only 2026-10 sailing (2026-10-31) is gone from source, so "
           "2026-10 no longer appears in month_price_overrides and the previous "
           "wording is false", p="n/a")

    ev("date_checked", r[ix["date_checked"]], TODAY, "n/a",
       f'row re-verified from source this run ({d["nA"]} sailing(s))', p="n/a")

    # ---- apply
    r[ix["sail_months"]] = newsm
    r[ix["price_interior"]] = str(ni)
    r[ix["price_balcony"]] = "" if nb is None else str(nb)
    r[ix["month_price_overrides"]] = newov
    if rid in SEASON:
        r[ix["season_note"]] = SEASON[rid]
    r[ix["date_checked"]] = TODAY
    r[ix["notes"]] = r[ix["notes"]] + f" | {TODAY}: " + NOTES[rid]
    verified_rows.append(rid)

# the past-month purge: source returned no month before 2026-10 for any tracked
# group, so the purge is a no-op this run and every surviving month is >= 2026-10
assert all(not f["dropped_past"] for f in fin.values()), "a past month WAS dropped"
assert all(all(m >= "2026-10" for m in f["sail_months"]) for f in fin.values())

buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\r\n")
w.writerows([header] + body)
(DATA / "03_itineraries.csv").write_bytes(buf.getvalue().encode("utf-8"))

buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\r\n")
w.writerows(cand)
(ROOT / "lp-system/out/candidates-2026-10-16.csv").write_bytes(
    buf.getvalue().encode("utf-8"))

# ------------------------------------------------- offers (LF endings)
# o010 (Weekend Sale) ended 2026-10-12 -> retire the banner.
# o011 from this run's cruise-deals.html: the page carries exactly ONE distinct
# data-promotion payload, reading type "flash_sale", title "Short Caribbean
# Getaways Sale", startDate 2026-10-14T04:00:00.000Z, endDate
# 2026-10-23T04:00:00.000Z (04:00Z = 00:00 ET in October), extended false,
# countdownEnabled true with countdownStartDate 2026-10-19T04:00:00.000Z, perks
# "Cruises as low as $299" and "+ 3rd and 4th guests sail free". The only other
# percent-off/second-guest strings on the page are empty i18n templates
# ("{0}% off second guest"), not a live offer. end_date 2026-10-22 because
# generate.py:383 gates inclusively and 2026-10-22 is the sale's last full ET day.
praw = (DATA / "07_offers.csv").read_text(encoding="utf-8")
orows = list(csv.reader(io.StringIO(praw, newline="")))
ohead, obody = orows[0], orows[1:]
oi = {n: i for i, n in enumerate(ohead)}
for o in obody:
    if o[oi["offer_id"]] == "o010":
        o[oi["show_banner"]] = "no"
        o[oi["status"]] = "expired"
obody.append([
  "o011", "rci",
  ("Royal Caribbean promotion, seen 2026-10-16: the line's own cruise-deals page "
   "is running a limited-time flash sale its promotion data titles the Short "
   "Caribbean Getaways Sale, listing cruises from as low as $299 and 3rd and 4th "
   "guests sail free. Royal Caribbean's own listing dates the sale from "
   "2026-10-14 to 2026-10-23 at 00:00 ET, so 2026-10-22 is its last full day, and "
   "enables a countdown clock that starts 2026-10-19. The perks are not the ones "
   "this page carried under the Weekend Sale on 2026-10-12: the up-to-$850-off and "
   "Caribbean-and-West-Coast perks are gone and a $299 lead-in price claim has "
   "replaced them; 3rd and 4th guests sail free carries over. No other promotion "
   "appeared on the page in this fetch. The $299 figure is Royal Caribbean's own "
   "advertised claim, not our quote. Royal Caribbean sets the terms and decides "
   "which sailings and guests qualify; ask on the call."),
  "2026-10-14", "2026-10-22", "yes",
  "combo:royal-caribbean-galveston;line:royal-caribbean",
  "https://www.royalcaribbean.com/cruise-deals", "2026-10-16", "verified"])
buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\n")
w.writerows([ohead] + obody)
(DATA / "07_offers.csv").write_bytes(buf.getvalue().encode("utf-8"))

print("verified rows:", len(verified_rows), verified_rows)
print("frozen rows  :", len(frozen_rows), frozen_rows)
print("candidate evidence lines:", len(cand) - 1)
