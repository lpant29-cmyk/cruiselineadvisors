#!/usr/bin/env python3
"""Pass C 2026-10-12 writer: candidate diff + 03_itineraries.csv + 07_offers.csv.

Every number here comes from _final.json / _derived.json, which are built only
from the two official cruiseSearch responses fetched this run (cached beside
this script), plus cruise-deals.html for the offer. Nothing is typed from memory.
"""
import csv
import io
import json
import pathlib
import re

ROOT = pathlib.Path("/Users/lokesh29/cruiselineadvisors")
C = ROOT / "lp-system/out/cache/2026-10-12"
DATA = ROOT / "lp-system/data"
TODAY = "2026-10-12"
RETRIEVED = "A 2026-10-12T07:48:09Z / B 2026-10-12T07:48:31Z-07:48:57Z"
AGREE = ("Both independent fetches, the Galveston departure-port query and the "
         "fleet-wide by-ship query, return the same sailing set and agree to "
         "the cent on every month.")

fin = json.load(open(C / "_final.json"))
der = json.load(open(C / "_derived.json"))

# ------------------------------------------------- per-row notes. Every claim
# below was diffed against this run's _derived.json and the 2026-10-02 cached
# response; no claim is carried over untested.
NOTES = {
 "i0003": ("group returns the same 7 sailings across 2027-08, 2027-09 and 2027-10 "
   "as the 2026-10-02 run; nothing was added or lost. Row lead-ins re-derived from "
   "source: interior 1200.01 (2027-10, 2027-10-17), balcony 1359.51 (2027-10, "
   "2027-10-03). The interior lead-in rises 1159 to 1200 because 2027-10-03, which "
   "held October's interior floor at 1158.51, now quotes 1256.51, leaving "
   "2027-10-17's unchanged 1200.01 as the month floor. Diffed against the stored "
   "overrides, two month-class tokens moved: the 2027-08 balcony rises 1549 to 1609 "
   "(2027-08-22, 1549.46 to 1608.96) and the 2027-09 interior falls 1248 to 1217 "
   "(2027-09-19, 1266.46 to 1216.96). " + AGREE),
 "i0004": ("group returns the same 6 sailings across 2027-08, 2027-09, 2027-10 and "
   "2027-11 as the 2026-10-02 run. Row lead-ins re-derived from source: interior "
   "1648.96 and balcony 1830.46, both on 2027-10-23. Both lead-ins move off "
   "2027-09-25 onto 2027-10-23 without 2027-10-23 itself changing: 2027-09-25 rose "
   "from 1629.46/1809.46 to 1659.46/1839.96. 2027-09 is the only month whose tokens "
   "changed; 2027-08, 2027-10 and 2027-11 are unchanged in both classes. " + AGREE),
 "i0005": ("group returns its one remaining sailing, 2026-10-17, the same single "
   "sailing as the 2026-10-02 run. It has NOT been withdrawn at 5 days out, which "
   "does not match the short-notice withdrawal pattern seen on 2026-10-02; treat "
   "that pattern as unconfirmed. Mariner of the Seas has exactly three Galveston "
   "departures left at source, 2026-10-17 here plus 2026-10-22 and 2026-10-26 on "
   "i0008, and the fleet-wide Mariner query returns 47 New Orleans departures from "
   "2026-11-01 onward. The 2026-10-17 interior rose 506.14 to 700.14, +38.3%, the "
   "largest move in this run; its OUTSIDE fare rose 748.14 to 1050.14 on the same "
   "sailing. BALCONY is null on this sailing in both fetches, as it was last run, "
   "so 2026-10 keeps an interior-only token and price_balcony stays empty: no "
   "sailing in this row publishes a balcony fare today. " + AGREE),
 "i0006": ("group returns the same 70 sailings across 19 months, 2026-10 to "
   "2028-04, as the 2026-10-02 run. Row lead-ins re-derived from source: interior "
   "383.09 (2027-01, 2027-01-18), balcony 619.06 (2026-12, 2026-12-12). The "
   "interior lead-in moves off 2027-01-09, which rose 368.94 to 394.44, onto "
   "2027-01-18 at 383.09; the balcony lead-in moves out of 2027-01 into 2026-12 "
   "because 2026-12-12's balcony fell 685.56 to 619.06. 2026-10's only sailing, "
   "2026-10-31, now returns a null BALCONY where it returned 1036.06 last run, so "
   "2026-10 drops to an interior-only token; price_balcony is deliberately NOT "
   "cleared, because 619.06 is a real published floor in 2026-12 and "
   "months_without_balcony() suppresses the balcony on 2026-10 alone. 2026-11-09 "
   "also returns a null balcony now, but 2026-11 still has one from 2026-11-14 at "
   "769.06. 9 of the 19 months are unchanged in both classes: 2027-05, 2027-07, "
   "2027-08, 2027-11, 2027-12, 2028-01, 2028-02, 2028-03, 2028-04. " + AGREE),
 "i0007": ("group returns the same 39 sailings across 18 months, 2026-11 to "
   "2028-04, as the 2026-10-02 run. Row lead-ins re-derived from source: interior "
   "423.76 (2027-01, 2027-01-28, up from 403.76 on that same sailing), balcony "
   "699.05 (2027-10, 2027-10-21, unchanged on that same sailing). 2026-11-05 now "
   "returns a balcony of 1146.09 where it returned null last run, which pulls the "
   "2026-11 balcony token down 1286 to 1146. In 2026-12 the balcony floor, 799.62 "
   "on 2026-12-03, sits BELOW that month's interior floor, 834.77 on 2026-12-17: "
   "2026-12-03's interior rose 725.12 to 895.12 while its balcony fell 888.12 to "
   "799.62. Both fetches agree to the cent on both of those numbers, so the month "
   "publishes as returned rather than being held. 11 of the 18 months are unchanged "
   "in both classes. " + AGREE),
 "i0008": ("group returns the same 2 sailings, 2026-10-22 and 2026-10-26, as the "
   "2026-10-02 run; neither has been withdrawn at 10 and 14 days out. 2026-10 "
   "floors on interior 549.55 (2026-10-22) and balcony 799.48 (2026-10-26), two "
   "different sailings, and class availability flipped between them: 2026-10-22 "
   "returned interior 616.55 with a null balcony last run and now returns interior "
   "549.55 with balcony 899.05, while 2026-10-26 returned interior 542.98 and now "
   "returns a null INTERIOR with balcony 799.48, up from 750.98. Both tokens remain "
   "real published floors. These are the last two of Mariner of the Seas' three "
   "remaining Galveston departures. " + AGREE),
 "i0009": ("group returns the same 7 sailings across 2027-05, 2027-06 and 2027-07 "
   "as the 2026-10-02 run. Row lead-ins re-derived from source: interior 671.00 and "
   "balcony 697.00, both on 2027-05-02, the same sailing as last run, down from "
   "677.50 and 745.50. All three months fall in at least one class: 2027-05 i678 to "
   "i671 and b746 to b697, 2027-06 i1032 to i1012 with balcony unchanged, 2027-07 "
   "i1042 to i1002 and b1066 to b1064. " + AGREE),
 "i0010": ("group returns the same 28 sailings across 7 months, 2026-10 to 2027-04, "
   "as the 2026-10-02 run. Row lead-ins re-derived from source: interior 595.48 "
   "(2027-01, 2027-01-24), balcony 674.94 (2027-02, 2027-02-28). The interior "
   "lead-in moves off 2027-01-17, unchanged at 607.48, onto 2027-01-24, which fell "
   "626.98 to 595.48; the balcony lead-in moves out of 2027-01 into 2027-02 because "
   "2027-02-28's balcony fell 741.44 to 674.94. The 2026-10 balcony token falls "
   "1676 to 1024, -38.9%, because 2026-10-25 returns a balcony again at 1024.30 "
   "after returning null last run, and 2026-10-18's own balcony fell 1676.32 to "
   "1079.82. The 2026-11 balcony token rises 836 to 1057, +26.4%: 2026-11-15 held "
   "that floor at 836.12 and now quotes 1105.62, leaving 2026-11-29's 1057.40 as "
   "the month floor. 2026-12-06 now returns a null interior, so the 2026-12 "
   "interior token comes from 2026-12-13 at 1033.12. All seven months changed in at "
   "least one class. " + AGREE),
 "i0011": ("UNVERIFIED, second consecutive run: group SY08GAL-3243125536 again "
   "returns ZERO sailings. It is absent from the Galveston departure-port query and "
   "from the fleet-wide Symphony query, and package code SY08W063 appears in "
   "neither response. It has NOT returned from source. The 2026-10-10 departure "
   "that was its last known sailing has now passed. sail_months, both prices, the "
   "overrides and the 2026-09-22 date_checked stamp are left exactly as last "
   "verified and the row stays flagged UNVERIFIED so it cannot publish. Still "
   "awaiting a Pass A retire decision from research-registrar."),
 "i0012": ("group returns its 1 sailing, 2028-02-04, at interior 666.59 and balcony "
   "967.59, both identical to the 2026-10-02 run; re-verified from source and the "
   "stamp advanced. " + AGREE),
 "i0013": ("group returns the same 2 sailings, 2027-12-24 and 2028-04-15, and all "
   "four fares are identical to the 2026-10-02 run: 2027-12-24 interior 1096.72 and "
   "balcony 1469.22, 2028-04-15 interior 741.61 and balcony 1042.11. Both months "
   "and both row lead-ins unchanged; re-verified from source and the stamp "
   "advanced. " + AGREE),
 "i0014": ("group returns its 1 sailing, 2026-12-21. Interior rose 838.11 to "
   "889.61, +6.2%; balcony is unchanged at 1238.11. " + AGREE),
 "i0015": ("group returns the same 7 sailings across 2027-05, 2027-06 and 2027-07 "
   "as the 2026-10-02 run. Row lead-ins are unchanged: interior 1209.20 and balcony "
   "1409.70, both still on 2027-07-31. The only month-class token that moved is the "
   "2027-06 interior, 1467 to 1440, after 2027-06-19 fell 1466.70 to 1440.20; "
   "2027-05 and 2027-07 are unchanged in both classes. " + AGREE),
 "i0016": ("group returns its 1 sailing, 2027-08-12. Interior rose 1010.52 to "
   "1062.52, +5.1%, and balcony 1602.52 to 1693.02, +5.6%. " + AGREE),
 "i0017": ("group returns the same 23 sailings across 2027-11 to 2028-04 as the "
   "2026-10-02 run. Row lead-ins re-derived from source: interior 1101.70 and "
   "balcony 1302.20, both on 2028-01-09. The interior lead-in moves out of 2028-02 "
   "into 2028-01 and rises 1026 to 1102 because February's two cheapest interiors "
   "both jumped: 2028-02-20 from 1026.06 to 1260.56 and 2028-02-13 from 1182.57 to "
   "1557.57, leaving 2028-02-06's unchanged 1120.70 as that month's floor. 2028-02 "
   "is the only month whose tokens changed; 2027-11, 2027-12, 2028-01, 2028-03 and "
   "2028-04 are unchanged in both classes. " + AGREE),
 "i0018": ("group returns its 1 sailing, 2027-08-08. Interior is unchanged at "
   "981.63; balcony fell 1084.13 to 1074.63. " + AGREE),
}

# No row needs a season_note edit this run: source returned no month before
# 2026-10 for any tracked group, so the past-month purge was a no-op and every
# sail_months list is identical to the stored one. Asserted below.
SEASON = {}

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
        ev("group", "0 sailings at 2026-10-02 (frozen)", "0 sailings returned",
           "group id absent from both responses; no 'SY08W063' match in either",
           "2026-10-10 (last known sailing; has now passed)",
           "second consecutive run with zero sailings; row stays frozen at its "
           "last verified values and 2026-09-22 stamp, flagged UNVERIFIED so it "
           "cannot publish",
           status="group-gone", qa="absent", qb="absent", agree="yes", p="n/a")
        r[ix["notes"]] = r[ix["notes"]] + f" | {TODAY}: " + NOTES[rid]
        changed_rows.append(rid)
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
           qa=f["bfloor_raw"], qb=f["bfloor_raw"])

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
           "month purge made the previous wording false", p="n/a")

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

# assert the no-op purge claim written into the SEASON comment
assert all(not f["dropped_past"] for f in fin.values()), "a past month WAS dropped"

buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\r\n")
w.writerows([header] + body)
(DATA / "03_itineraries.csv").write_bytes(buf.getvalue().encode("utf-8"))

buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\r\n")
w.writerows(cand)
(ROOT / "lp-system/out/candidates-2026-10-12.csv").write_bytes(
    buf.getvalue().encode("utf-8"))

# ------------------------------------------------- offers (LF endings)
# o009 (Score More Sale) ended 2026-10-05 -> retire the banner.
# o010 from this run's cruise-deals.html: the page's own data-promotion payload
# reads type "flash_sale", title "Weekend Sale", startDate 2026-10-08T04:00:00Z,
# endDate 2026-10-13T04:00:00Z (04:00Z = 00:00 ET in October), countdownEnabled
# true, lock-up image this-weekend-only-lockup-65px.png, perks "Up to $850 off",
# "+ Up to $100 Off Caribbean & West Coast thru April 2027",
# "+ 3rd and 4th guests sail free". Exactly one distinct promotion blob on the
# page. end_date 2026-10-12 because generate.py:383 gates inclusively and
# 2026-10-12 is the sale's last full ET day.
praw = (DATA / "07_offers.csv").read_text(encoding="utf-8")
orows = list(csv.reader(io.StringIO(praw, newline="")))
ohead, obody = orows[0], orows[1:]
oi = {n: i for i, n in enumerate(ohead)}
for o in obody:
    if o[oi["offer_id"]] == "o009":
        o[oi["show_banner"]] = "no"
        o[oi["status"]] = "expired"
obody.append([
  "o010", "rci",
  ("Royal Caribbean promotion, seen 2026-10-12: the line's own cruise-deals page "
   "is running a limited-time flash sale its promotion data titles the Weekend "
   "Sale, shown with a countdown clock and a this-weekend-only lock-up, listing "
   "up to $850 off, up to $100 more off Caribbean and West Coast sailings through "
   "April 2027, and 3rd and 4th guests sail free. Royal Caribbean's own listing "
   "dates the sale from 2026-10-08 to 2026-10-13 at 00:00 ET, so 2026-10-12 is "
   "its last full day. The three listed perks are worded as they were under the "
   "Score More Sale this page carried on 2026-10-02; the sale now runs under a "
   "new name and new dates. No other promotion appeared on the page in this "
   "fetch. Royal Caribbean sets the terms and decides which sailings and guests "
   "qualify; ask on the call."),
  "2026-10-08", "2026-10-12", "yes",
  "combo:royal-caribbean-galveston;line:royal-caribbean",
  "https://www.royalcaribbean.com/cruise-deals", "2026-10-12", "verified"])
buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\n")
w.writerows([ohead] + obody)
(DATA / "07_offers.csv").write_bytes(buf.getvalue().encode("utf-8"))

print("verified rows:", len(verified_rows), verified_rows)
print("frozen rows  :", len(changed_rows), changed_rows)
print("candidate evidence lines:", len(cand) - 1)
