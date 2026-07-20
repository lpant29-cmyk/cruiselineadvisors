# -*- coding: utf-8 -*-
"""Bug 1 guard: a ship's finder region tags must be derived from its own itinerary (deploy_note),
never a line-level tag that drifts. Run: python3 tests/test_regions.py"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import ships
import metasearch


def test_finder_regions_subset_of_itinerary():
    """No ship with a published itinerary may be finder-matched to a region it doesn't sail."""
    fails = []
    for line_slug, s in ships.all_ships():
        exp = s.get("exp") or {}
        note = exp.get("deploy_note")
        if not note:
            continue  # no itinerary data -> line-level fallback (best-effort, excluded from this check)
        finder = set(metasearch.ship_regions(line_slug, exp))
        itinerary = set(metasearch.region_ids_for_note(note))
        extra = finder - itinerary
        if extra:
            fails.append((s["name"], sorted(extra)))
    assert not fails, f"{len(fails)} ships tagged regions absent from their itinerary: {fails[:6]}"


def test_icon_and_star_not_alaska():
    """Regression for the reported case: Caribbean-only RC ships must not appear under Alaska."""
    for line_slug, s in ships.all_ships():
        if s["name"] in ("Icon of the Seas", "Star of the Seas", "Utopia of the Seas"):
            regs = metasearch.ship_regions(line_slug, s.get("exp") or {})
            assert "alaska" not in regs, f"{s['name']} wrongly tagged Alaska: {regs}"


if __name__ == "__main__":
    test_finder_regions_subset_of_itinerary()
    test_icon_and_star_not_alaska()
    print("test_regions: PASS")
