# -*- coding: utf-8 -*-
"""Full directory of every cruise line boardable from the Americas (data/directory.json).
Lines with covered=true have an in-depth guide (linked); the rest are listed as "coming soon".
To activate a line as you publish its guide: set covered=true in data/directory.json (and add its
page). It links automatically on the next build."""
import json
import os

_DIR = json.load(open(os.path.join(os.path.dirname(__file__), "data", "directory.json"), encoding="utf-8"))
CATEGORIES = _DIR["categories"]
LINES = _DIR["lines"]

_CAT_ES = {"mainstream": "Populares", "premium": "Premium", "luxury": "Lujo",
           "expedition": "Expedición y barcos pequeños", "river-coastal": "Ríos y costas de EE.UU."}
_CAT_EN = {c["id"]: c["name"] for c in CATEGORIES}

_T = {
    "en": {"kick": "All cruise lines", "h2": "Every major line boardable from the Americas",
           "sub": "We publish in-depth, verified guides as we go. The lines with a guide are live below; the rest are on the way — call for any line, listed or not.",
           "done": "Guide ›", "soon": "Coming soon"},
    "es": {"kick": "Todas las líneas de crucero", "h2": "Todas las líneas principales desde las Américas",
           "sub": "Publicamos guías detalladas y verificadas a medida que avanzamos. Las líneas con guía están activas abajo; las demás llegan pronto — llama por cualquier línea, esté o no listada.",
           "done": "Ver guía ›", "soon": "Próximamente"},
}


def directory_section(lang):
    t = _T[lang]
    catname = _CAT_EN if lang == "en" else {c: _CAT_ES.get(c, _CAT_EN[c]) for c in _CAT_EN}
    blocks = ""
    for c in CATEGORIES:
        rows = [l for l in LINES if l["cat"] == c["id"]]
        if not rows:
            continue
        cards = ""
        for l in rows:
            emo = l.get("emoji", "🚢")
            if l.get("covered"):
                cards += (f'<a class="dir-line" href="/{lang}/lines/{l["slug"]}/">'
                          f'<span class="dir-emo">{emo}</span><b>{l["name"]}</b>'
                          f'<span class="dir-tag done">{t["done"]}</span></a>')
            else:
                cards += (f'<div class="dir-line soon-row"><span class="dir-emo">{emo}</span>'
                          f'<b>{l["name"]}</b><span class="dir-tag soon">{t["soon"]}</span></div>')
        blocks += f'<div class="dir-cat"><h3>{catname[c["id"]]}</h3><div class="dir-grid">{cards}</div></div>'
    return (f'<section class="section cream" id="directory"><div class="wrap">'
            f'<div class="sec-head"><span class="eyebrow">{t["kick"]}</span><h2>{t["h2"]}</h2><p>{t["sub"]}</p></div>'
            f'{blocks}</div></section>')
