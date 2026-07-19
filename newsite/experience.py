# -*- coding: utf-8 -*-
"""Rich per-ship 'experience' sections — Onboard overview, Food & Dining, Drinks & packages,
Activities, Entertainment, Kids/Teens/Families, Decks & layout, Bridge cam — plus a self-hosted
photo strip. Data-driven: each section renders ONLY when it has verified content (never a fake
'coming soon' block). Per-ship content lives in data/ships/<line>.json under each ship's "exp"
key; line-wide shared content (drink packages, kids programs) lives in data/cruise-lines.json
under "experience". NO PRICES. All prose is original — we store facts, not copied sentences."""
from config import PHONE_HREF, PHONE_DISPLAY
from linepage import line_data

_H = {
    "photos": {"en": "On board", "es": "A bordo"},
    "overview": {"en": "The ship at a glance", "es": "El barco en resumen"},
    "dining": {"en": "Food & dining", "es": "Comida y restaurantes"},
    "drinks": {"en": "Drinks & packages", "es": "Bebidas y paquetes"},
    "activities": {"en": "Activities", "es": "Actividades"},
    "entertainment": {"en": "Entertainment", "es": "Entretenimiento"},
    "family": {"en": "Kids, teens & families", "es": "Niños, adolescentes y familias"},
    "decks": {"en": "Decks & layout", "es": "Cubiertas y distribución"},
    "cam": {"en": "Bridge cam", "es": "Cámara del puente"},
}
_IC = {"overview": "🚢", "dining": "🍽️", "drinks": "🍹", "activities": "🎢",
       "entertainment": "🎭", "family": "👨‍👩‍👧", "decks": "🛗", "cam": "📷"}
_DTYPE = {  # dining venue type labels
    "main": {"en": "Main dining", "es": "Comedor principal"},
    "buffet": {"en": "Buffet", "es": "Bufé"},
    "casual": {"en": "Casual", "es": "Informal"},
    "specialty": {"en": "Specialty", "es": "Especialidad"},
}
_INC = {"en": "Included", "es": "Incluido"}
_EXT = {"en": "Extra", "es": "Extra"}


def _sec(key, lang, inner):
    return (f'<section id="x-{key}" class="section xsec"><div class="wrap">'
            f'<h2 class="rsec-h"><span class="xic" aria-hidden="true">{_IC[key]}</span>{_H[key][lang]}</h2>'
            f'{inner}</div></section>')


def _call(lang, txt):
    c = "Call now" if lang == "en" else "Llama ahora"
    return (f'<div class="nudge"><p>{txt}</p>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'ship-exp\')">'
            f'<span class="ic" aria-hidden="true">☎</span>{c} · {PHONE_DISPLAY}</a></div>')


def has_experience(line_slug, ship):
    exp = ship.get("exp") or {}
    le = (line_data(line_slug).get("experience") or {})
    return bool(exp) or bool(le.get("beverages") or le.get("kids"))


def experience_sections(lang, line_slug, ship):
    exp = ship.get("exp") or {}
    le = line_data(line_slug).get("experience") or {}
    name = ship["name"]
    out = ""

    # ── Photo strip (self-hosted, royalty-free/licensed; illustrative) ──
    photos = exp.get("photos") or []
    if photos:
        cards = "".join(
            f'<figure class="xphoto"><img src="{p["src"]}" alt="{p.get("alt","")}" loading="lazy">'
            + (f'<figcaption>{p["credit"]}</figcaption>' if p.get("credit") else "")
            + "</figure>" for p in photos if p.get("src"))
        note = ("Photos are illustrative." if lang == "en" else "Fotos ilustrativas.")
        out += _sec("photos", lang, f'<div class="xphotos">{cards}</div><p class="xnote">{note}</p>')

    # ── Overview (original prose) ──
    ov = exp.get("overview")
    if ov:
        out += _sec("overview", lang, f'<p class="intro">{ov}</p>')

    # ── Food & dining ──
    dining = exp.get("dining") or []
    if dining:
        rows = ""
        for d in dining:
            if not d.get("name"):
                continue
            t = d.get("type")
            badge = f'<span class="xtag">{_DTYPE[t][lang]}</span>' if t in _DTYPE else ""
            cost = (f'<span class="xtag xtag-x">{_EXT[lang]}</span>' if d.get("extra")
                    else f'<span class="xtag xtag-i">{_INC[lang]}</span>')
            rows += f'<li><b>{d["name"]}</b>{badge}{cost}</li>'
        nudge = (_call(lang, f"Want a specialty table booked before you sail? Our team sets it up when you call.")
                 if lang == "en" else
                 _call(lang, "¿Quieres reservar un restaurante de especialidad antes de zarpar? Lo hacemos por teléfono."))
        out += _sec("dining", lang, f'<ul class="xdine">{rows}</ul>{nudge}')

    # ── Drinks & packages (line-wide) ──
    bev = le.get("beverages") or []
    if bev:
        cards = "".join(
            f'<div class="xpkg"><h3>{b["name"]}</h3><p>{b.get("includes","")}</p></div>'
            for b in bev if b.get("name"))
        out += _sec("drinks", lang, f'<div class="xpkgs">{cards}</div>')

    # ── Activities ──
    acts = exp.get("activities") or []
    if acts:
        chips = "".join(f'<span class="ft">{a}</span>' for a in acts if a)
        nudge = (_call(lang, f"A specialist knows which {name} activities book up fast and how to lock them in.")
                 if lang == "en" else
                 _call(lang, f"Un especialista sabe qué actividades de {name} se agotan rápido y cómo asegurarlas."))
        out += _sec("activities", lang, f'<div class="ship-feats">{chips}</div>{nudge}')

    # ── Entertainment ──
    ent = exp.get("entertainment") or []
    if ent:
        chips = "".join(f'<span class="ft">{e}</span>' for e in ent if e)
        out += _sec("entertainment", lang, f'<div class="ship-feats">{chips}</div>')

    # ── Kids, teens & families (line-wide, with any ship note) ──
    kids = le.get("kids") or {}
    krows = ""
    for k, lbl in (("nursery", {"en": "Nursery", "es": "Guardería"}),
                   ("kids_club", {"en": "Kids club", "es": "Club infantil"}),
                   ("teens", {"en": "Teens", "es": "Adolescentes"}),
                   ("family", {"en": "Family cabins & notes", "es": "Camarotes familiares"})):
        v = kids.get(k)
        if v:
            krows += f'<div class="glance-cell"><b>{lbl[lang]}</b><span>{v}</span></div>'
    if krows:
        out += _sec("family", lang, f'<div class="glance-grid">{krows}</div>')

    # ── Decks & layout ──
    decks = exp.get("decks")
    nbh = exp.get("neighborhoods") or []
    if decks or nbh:
        bits = ""
        if decks:
            lbl = "Passenger decks" if lang == "en" else "Cubiertas"
            bits += f'<div class="glance-cell"><b>{lbl}</b><span>{decks}</span></div>'
        inner = f'<div class="glance-grid">{bits}</div>' if bits else ""
        if nbh:
            lbl = "Neighbourhoods & zones" if lang == "en" else "Zonas y barrios"
            chips = "".join(f'<span class="ft">{n}</span>' for n in nbh if n)
            inner += f'<p class="rsec-sub" style="margin-top:16px"><b>{lbl}:</b></p><div class="ship-feats">{chips}</div>'
        out += _sec("decks", lang, inner)

    # ── Bridge cam (availability only — we don't re-host the line's live stream) ──
    cam = exp.get("bridge_cam")
    if cam is not None:
        if cam:
            txt = (f"{name} has a live bridge cam on board — ask us what the view and itinerary look like for your dates."
                   if lang == "en" else
                   f"{name} tiene cámara del puente en vivo a bordo — pregúntanos por la vista y el itinerario de tus fechas.")
        else:
            txt = ("No bridge cam published for this ship." if lang == "en"
                   else "No hay cámara del puente publicada para este barco.")
        out += _sec("cam", lang, f'<p class="rsec-sub">{txt}</p>')

    return out
