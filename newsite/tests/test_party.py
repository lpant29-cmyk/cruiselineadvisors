# -*- coding: utf-8 -*-
"""Bug 2 guard: the "Who's travelling?" control must actually change the ranked results where the
data supports a difference. Mirrors the finder's client-side ranking (bscore + pmatch) so it stays
in lock-step with metasearch.py's JS. Run: python3 tests/test_party.py"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import metasearch

D = metasearch._payload("en")


def bscore(s):
    sc = 0.0
    if s["year"]:
        sc += max(0, (s["year"] - 1995)) / 30
    if s["guests"]:
        sc += min(1, s["guests"] / 6000) * 0.6
    if s["dine"]:
        sc += min(1, s["dine"] / 20) * 0.4
    return sc


def pmatch(s, party):
    if party == "family":
        return 2 if s["fam"] else 0
    if party == "couple":
        return 2 if (s["cpl"] and not s["fam"]) else (1 if s["cpl"] else 0)
    if party == "solo":
        return 2 if s["solo"] else (1 if s["cpl"] else 0)
    if party == "friends":
        return 2 if (s["val"] or (s["guests"] or 0) >= 3800) else (1 if (s["guests"] or 0) >= 3000 else 0)
    return 0


def spread(arr):
    """Mirror of the JS 'Just exploring' line-diversity spread."""
    by, order = {}, []
    for s in arr:
        by.setdefault(s["line"], []).append(s)
        if s["line"] not in order:
            order.append(s["line"])
    out, added = [], True
    while added:
        added = False
        for ln in order:
            if by[ln]:
                out.append(by[ln].pop(0))
                added = True
    return out


def ranked(region, party, n=3):
    lst = [s for s in D["ships"] if region in s["regions"]]
    lst.sort(key=lambda s: (pmatch(s, party), bscore(s)), reverse=True)
    if party == "any":
        lst = spread(lst)
    return [s["name"] for s in lst[:n]]


def test_every_persona_differs_from_default():
    """Family, Couple and Solo must each reorder the top vs 'just exploring' in a diverse region."""
    region = "caribbean"
    default = ranked(region, "any")
    for party in ("family", "couple", "solo"):
        assert ranked(region, party) != default, f"{party} did not change the ranking vs default"


def test_data_supports_each_persona():
    """Sanity: the fleet actually contains ships that distinguish each persona (else the control
    would be cosmetic). If any of these is 0, the corresponding option should be relabelled/removed."""
    ships = D["ships"]
    assert sum(1 for s in ships if s["solo"]) > 0, "no solo-cabin ships -> Solo is meaningless"
    assert sum(1 for s in ships if s["cpl"] and not s["fam"]) > 0, "no adults-leaning ships -> Couple is meaningless"
    assert sum(1 for s in ships if s["fam"]) > 0, "no family ships -> Family is meaningless"


if __name__ == "__main__":
    test_every_persona_differs_from_default()
    test_data_supports_each_persona()
    print("test_party: PASS")
