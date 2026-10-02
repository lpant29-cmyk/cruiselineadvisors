#!/usr/bin/env python3
"""Pass C 2026-10-02 derivation: build per-row, per-month floors from the two
independently shaped official cruiseSearch responses fetched this run.

A = filters "departurePort:GAL"      (one call)
B = filters "ship:IC|LB|MA|SY"       (four calls, fleet-wide, reconciled back
                                      to the GAL groups)
Months strictly before CUTOFF are dropped (purge of past months).
"""
import json
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
CUTOFF = "2026-10"          # today is 2026-10-02; anything earlier is past
GIDMAP = json.load(open(HERE.parent / "2026-09-22" / "_gidmap.json"))


def load(fn):
    return json.load(open(HERE / fn))["data"]["cruiseSearch"]["results"]


def index(results, gal_only):
    """gid -> {sailDate -> {class -> price}} plus link/code bookkeeping."""
    out = {}
    for c in results["cruises"]:
        gid = c["id"]
        for s in c["sailings"]:
            it = s["itinerary"]
            if gal_only and it["departurePort"]["code"] != "GAL":
                continue
            rec = out.setdefault(gid, {"sail": {}, "link": c.get("productViewLink", ""),
                                       "codes": set(), "nights": set(), "ship": set()})
            prices = {}
            for p in s["stateroomClassPricing"] or []:
                v = (p.get("price") or {}).get("value")
                prices[p["stateroomClass"]["id"]] = v
            rec["sail"][s["sailDate"]] = prices
            rec["codes"].add(it["code"])
            rec["nights"].add(it["totalNights"])
            rec["ship"].add(it["ship"]["code"])
    return out


A = index(load("graph-departurePort-GAL.json"), gal_only=False)
B = {}
for ship in ("IC", "LB", "MA", "SY"):
    B.update(index(load(f"graph-confirm-ship-{ship}.json"), gal_only=True))


def months(rec):
    m = collections.defaultdict(dict)
    for d, pr in rec["sail"].items():
        m[d[:7]][d] = pr
    return m


def floor(sails, cls):
    """(value, date) of the lowest non-null fare for cls, or (None, None)."""
    cands = [(pr[cls], d) for d, pr in sorted(sails.items())
             if pr.get(cls) is not None]
    return min(cands) if cands else (None, None)


derived = {}
for itin, gid in GIDMAP.items():
    ra, rb = A.get(gid), B.get(gid)
    row = {"gid": gid,
           "in_A": ra is not None, "in_B": rb is not None,
           "link": (ra or rb or {}).get("link", ""),
           "codes": sorted((ra or rb or {"codes": set()})["codes"]),
           "nA": len(ra["sail"]) if ra else 0,
           "nB": len(rb["sail"]) if rb else 0,
           "sails_A": sorted(ra["sail"]) if ra else [],
           "sails_B": sorted(rb["sail"]) if rb else [],
           "months": {}}
    ma = months(ra) if ra else {}
    mb = months(rb) if rb else {}
    for mo in sorted(set(ma) | set(mb)):
        sa, sb = ma.get(mo, {}), mb.get(mo, {})
        ai, aid = floor(sa, "INTERIOR")
        ab, abd = floor(sa, "BALCONY")
        bi, bid = floor(sb, "INTERIOR")
        bb, bbd = floor(sb, "BALCONY")
        ao, _ = floor(sa, "OUTSIDE")
        row["months"][mo] = {
            "past": mo < CUTOFF,
            "A_sails": sorted(sa), "B_sails": sorted(sb),
            "A_i": ai, "A_ifloor": aid, "A_b": ab, "A_bfloor": abd, "A_o": ao,
            "B_i": bi, "B_ifloor": bid, "B_b": bb, "B_bfloor": bbd,
            "agree_i": ai == bi, "agree_b": ab == bb,
            "sails_match": sorted(sa) == sorted(sb),
        }
    derived[itin] = row

json.dump(derived, open(HERE / "_derived.json", "w"), indent=1, default=str)

# --------------------------------------------------------------- final shape
def r(v):
    return None if v is None else int(round(v))


final = {}
for itin, row in derived.items():
    keep = {m: v for m, v in row["months"].items() if not v["past"]}
    toks, sm, nullb, nulli, hold = [], [], [], [], []
    for m in sorted(keep):
        v = keep[m]
        if not v["sails_match"]:
            hold.append(f"{m}:sail-set-mismatch")
        i_ok = v["agree_i"]
        b_ok = v["agree_b"]
        if not i_ok:
            hold.append(f"{m}:interior A={v['A_i']} B={v['B_i']}")
        if not b_ok:
            hold.append(f"{m}:balcony A={v['A_b']} B={v['B_b']}")
        i_v = r(v["A_i"]) if i_ok else None
        b_v = r(v["A_b"]) if b_ok else None
        if i_v is None and b_v is None:
            continue                      # no publishable fare -> month dropped
        sm.append(m)
        parts = []
        if i_v is not None:
            parts.append(f"i{i_v}")
        else:
            nulli.append(m)
        if b_v is not None:
            parts.append(f"b{b_v}")
        else:
            nullb.append(m)
        toks.append(m + ":" + "|".join(parts))
    # row lead-ins = lowest month floor across kept months, from raw cents
    icands = [(keep[m]["A_i"], m, keep[m]["A_ifloor"]) for m in sm
              if keep[m]["A_i"] is not None and keep[m]["agree_i"]]
    bcands = [(keep[m]["A_b"], m, keep[m]["A_bfloor"]) for m in sm
              if keep[m]["A_b"] is not None and keep[m]["agree_b"]]
    iv = min(icands) if icands else None
    bv = min(bcands) if bcands else None
    final[itin] = {
        "gone": not row["in_A"] and not row["in_B"],
        "in_A": row["in_A"], "in_B": row["in_B"],
        "n": row["nA"], "nB": row["nB"],
        "sail_months": sm,
        "dropped_past": sorted(m for m, v in row["months"].items() if v["past"]),
        "ov": "|".join(toks),
        "pi": r(iv[0]) if iv else None,
        "pb": r(bv[0]) if bv else None,
        "ifloor_raw": iv[0] if iv else None, "ifloor_m": iv[1] if iv else None,
        "ifloor_d": iv[2] if iv else None,
        "bfloor_raw": bv[0] if bv else None, "bfloor_m": bv[1] if bv else None,
        "bfloor_d": bv[2] if bv else None,
        "nullb": nullb, "nulli": nulli, "hold": hold,
        "codes": row["codes"],
    }

json.dump(final, open(HERE / "_final.json", "w"), indent=1, default=str)
print(f"groups in A: {len(A)}   groups in B(GAL): {len(B)}")
missing = [i for i, f in final.items() if f["gone"]]
print("tracked groups absent from BOTH queries:", missing or "none")
print("tracked groups in A only:", [i for i, f in final.items() if f["in_A"] and not f["in_B"]])
print("tracked groups in B only:", [i for i, f in final.items() if f["in_B"] and not f["in_A"]])
untracked = sorted(set(A) - set(GIDMAP.values()))
print("GAL groups returned but not tracked:", untracked)
