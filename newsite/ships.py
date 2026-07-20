# -*- coding: utf-8 -*-
"""Verified ship rosters, per line. Single source for the fleet listings on line pages, the
dedicated per-ship pages, and the ship-compare tool.

Each field is either a real, sourced value or None (renders as a visible "Not yet verified" gap, 
never guessed). `source`/`verified` record where the roster came from and when it was checked;
per Hard Rule 7, ships are re-checked on the normal refresh window. NO prices anywhere.

SHIPS[line_slug] = {
    "source":   "<url the roster was read from>",
    "verified": "YYYY-MM-DD",
    "ships": [
        {"name": str, "class": str|None, "year": int|None,
         "tonnage": int|None, "guests": int|None,
         "features": [str...], "notes": str|None},
        ...
    ],
}
Populated by the sourcing pass (see scratchpad/ships-*.json). Empty lines fall back to the
class-level fleet cards from data/cruise-lines.json.
"""
import re
import os
import json

# Rosters load from data/ships/*.json, the official-sourced files written by the sourcing pass
# (one per line). Each: {line, roster_source, specs_source, verified, ships:[...], needs_manual, flag}.
# Drop a new official file in and the build picks it up; no hand-transcription. NO PRICES in these.
SHIPS = {}
_SHIP_DIR = os.path.join(os.path.dirname(__file__), "data", "ships")
if os.path.isdir(_SHIP_DIR):
    for _fn in sorted(os.listdir(_SHIP_DIR)):
        if not _fn.endswith(".json"):
            continue
        with open(os.path.join(_SHIP_DIR, _fn), encoding="utf-8") as _f:
            _d = json.load(_f)
        _slug = _d.get("line") or _fn[:-5]
        SHIPS[_slug] = {
            "source": _d.get("roster_source") or _d.get("specs_source"),
            "specs_source": _d.get("specs_source"),
            "verified": _d.get("verified"),
            "needs_manual": _d.get("needs_manual", []),
            "ships": [s for s in _d.get("ships", []) if s.get("name")],
        }


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")


# A handful of ships carry an internal sourcing note (e.g. "…not confirmed on the pages read - see
# needs.") in kids_family, from the enrichment pass. That phrasing is for us, not visitors, it must
# never render. kids_family_display() swaps it for a clear, honest message; rich list data (named
# venues) and normal prose pass through untouched.
_KIDS_GAP_MARKERS = ("not confirmed on the pages read", "see needs", "not verified", "the pages read")
_KIDS_GAP_MSG = {
    "en": ("Family programming runs across the ship. We haven't yet verified this ship's exact "
           "kids-club, nursery and teen venue names from the line's official page, call and an "
           "advisor will confirm what's on board for your dates."),
    "es": ("Hay programación familiar en todo el barco. Aún no hemos verificado los nombres exactos "
           "del club infantil, la guardería y los espacios para adolescentes de este barco en la "
           "página oficial de la línea, llama y un asesor confirmará qué hay a bordo para tus fechas."),
}
_KIDS_GAP_MSG_SHORT = {
    "en": "Family programming on board, specific venue names confirmed by phone.",
    "es": "Programación familiar a bordo, nombres de locales confirmados por teléfono.",
}


def _kids_is_gap(kf):
    return isinstance(kf, str) and any(m in kf.lower() for m in _KIDS_GAP_MARKERS)


def kids_family_display(kf, lang="en", short=False):
    """Visitor-facing kids_family. Internal sourcing-gap phrasing becomes a clear honest message;
    lists (named venues) and ordinary prose are returned unchanged."""
    if _kids_is_gap(kf):
        return (_KIDS_GAP_MSG_SHORT if short else _KIDS_GAP_MSG).get(lang, _KIDS_GAP_MSG["en"])
    return kf


def ships_for(line_slug):
    return SHIPS.get(line_slug, {}).get("ships", [])


def get_ship(line_slug, ship_slug):
    for s in ships_for(line_slug):
        if slugify(s["name"]) == ship_slug:
            return s
    return None


def sister_ships(line_slug, ship):
    """Other ships in the same line sharing this ship's class."""
    cls = ship.get("class")
    if not cls:
        return []
    return [s for s in ships_for(line_slug)
            if s.get("class") == cls and s["name"] != ship["name"]]


def all_ships():
    """Yield (line_slug, ship) for every verified ship, for build-time page emission."""
    for line_slug, blob in SHIPS.items():
        for s in blob.get("ships", []):
            yield line_slug, s


def source_of(line_slug):
    b = SHIPS.get(line_slug, {})
    return b.get("source"), b.get("verified")


def coverage():
    """(lines with a roster, total verified ships), printed by the build."""
    lines = sum(1 for v in SHIPS.values() if v.get("ships"))
    total = sum(len(v.get("ships", [])) for v in SHIPS.values())
    return lines, total
