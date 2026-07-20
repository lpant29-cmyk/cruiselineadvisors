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


def ranked(region, party, n=3):
    lst = [s for s in D["ships"] if region in s["regions"]]
    lst.sort(key=lambda s: (pmatch(s, party), bscore(s)), reverse=True)
    return [s["name"] for s in lst[:n]]


def test_solo_and_couple_differ_from_default():
    """Solo and Couple must reorder the top vs 'just exploring' in a big, diverse region."""
    region = "caribbean"
    default = ranked(region, "any")
    assert ranked(region, "solo") != default, "Solo did not change the ranking"
    assert ranked(region, "couple") != default, "Couple did not change the ranking"


def test_data_supports_each_persona():
    """Sanity: the fleet actually contains ships that distinguish each persona (else the control
    would be cosmetic). If any of these is 0, the corresponding option should be relabelled/removed."""
    ships = D["ships"]
    assert sum(1 for s in ships if s["solo"]) > 0, "no solo-cabin ships -> Solo is meaningless"
    assert sum(1 for s in ships if s["cpl"] and not s["fam"]) > 0, "no adults-leaning ships -> Couple is meaningless"
    assert sum(1 for s in ships if s["fam"]) > 0, "no family ships -> Family is meaningless"


if __name__ == "__main__":
    test_solo_and_couple_differ_from_default()
    test_data_supports_each_persona()
    print("test_party: PASS")
