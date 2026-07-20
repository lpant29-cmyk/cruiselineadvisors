# -*- coding: utf-8 -*-
"""Gap 3 guard: site-wide search must return the expected page for representative queries.
Mirrors the JS scoring in search.py exactly so the two can't drift. Run: python3 tests/test_search.py"""
import sys
import os
import re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import search

IDX = search.build_index("en")
for e in IDX:
    e["_t"] = e["t"].lower()


def score(e, ql, toks):
    t, k = e["_t"], e["k"]
    if t == ql:
        return 1000
    if t.startswith(ql):
        return 600 - len(t) * 0.1
    s, all_hit = 0, True
    if ql in t:
        s += 200
    for tk in toks:
        if tk in t:
            s += 40
        elif tk in k:
            s += 15
        else:
            all_hit = False
    if not all_hit:
        return 0
    return s - len(t) * 0.1


def query(q, n=5):
    ql = q.strip().lower()
    toks = [x for x in re.split(r"\s+", ql) if x]
    scored = [(score(e, ql, toks), e) for e in IDX]
    scored = [x for x in scored if x[0] > 0]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [e["t"] for _, e in scored[:n]]


# (query, expected exact title of the top result)
CASES = [
    ("icon of the seas", "Icon of the Seas"),
    ("icon", "Icon of the Seas"),
    ("royal caribbean", "Royal Caribbean"),
    ("carnival jubilee", "Carnival Jubilee"),
    ("gratuities", "Daily gratuities"),
    ("alaska", "Alaska"),
    ("cabin", "Choosing a cabin"),
    ("mardi gras", "Mardi Gras"),
]


def test_top_result_matches():
    fails = []
    for q, expected in CASES:
        top = query(q)
        if not top or top[0] != expected:
            fails.append((q, expected, top[:3]))
    assert not fails, f"search returned the wrong top result for: {fails}"


def test_gibberish_returns_nothing():
    assert query("zzxqwv") == [], "gibberish query should return no results"


def test_index_covers_every_type():
    subs = [e["s"] for e in IDX]
    for label in ("Cruise line", "Ship", "Cruise fact", "Destination", "Guide"):
        assert any(label in s for s in subs), f"search index is missing any {label!r} entries"


if __name__ == "__main__":
    test_top_result_matches()
    test_gibberish_returns_nothing()
    test_index_covers_every_type()
    print("test_search: PASS")
