# -*- coding: utf-8 -*-
"""Rich per-ship 'experience' sections — Onboard overview, Food & Dining, Drinks & packages,
Activities, Entertainment, Kids/Teens/Families, Decks & layout, Bridge cam — plus a self-hosted
photo strip. Data-driven: each section renders ONLY when it has verified content (no fake
'coming soon' blocks). Per-ship content lives in data/ships/<line>.json under each ship's "exp"
key; line-wide shared content (drink packages, kids programs) in data/cruise-lines.json under
"experience".

Flexible inputs — activities / entertainment / kids_family may be a STRING (rendered as a
paragraph) or a LIST (rendered as chips); dining "extra" may be a bool (Included/Extra tag) or a
descriptive string (rendered as a note). NO PRICES. All prose is original — we store facts."""
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
_DTYPE = {
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


_FOOD_EMOJI = [
    (("pizza", "pizzeria"), "🍕"), (("burger",), "🍔"),
    (("sushi", "kaito", "robata"), "🍣"), (("teppanyaki",), "🍤"),
    (("steak", "butcher", "grill", "prime"), "🥩"), (("taco", "cantina", "mexican", "hola"), "🌮"),
    (("greek", "paxos"), "🥙"), (("seafood", "fish", "catch", "shack", "lobster"), "🦐"),
    (("italian", "eataly", "cucina", "pasta", "trattoria", "campo"), "🍝"),
    (("chicken",), "🍗"), (("coffee", "cafe", "café", "java", "emporium"), "☕"),
    (("chocolat", "sweet", "confection", "gelato", "ice cream", "dessert", "candy"), "🍫"),
    (("buffet", "market", "marketplace", "lido", "horizon", "eats"), "🍽️"),
    (("sports bar", "all-star", "all star"), "🍺"),
    (("comedy", "karaoke", "loft", "piano"), "🎤"),
    (("gin", "cocktail", "mixolog", "champagne", "wine", "elixir", "bar", "lounge", "pub", "tavern", "brew"), "🍸"),
    (("asian", "indochine", "wok", "noodle"), "🥢"), (("bistro", "french", "brasserie", "atelier"), "🥐"),
    (("tapas", "spanish"), "🥘"), (("bbq", "smoke", "guy"), "🍖"), (("diner", "americana", "americas"), "🥞"),
    (("tea", "afternoon"), "🫖"),
]


def _food_emoji(name, t):
    s = f"{name or ''} {t or ''}".lower()
    for keys, emo in _FOOD_EMOJI:
        if any(k in s for k in keys):
            return emo
    return "🍴"


def _chips_or_p(val):
    """Render a string as a paragraph, or a list as chips. Empty → ''."""
    if isinstance(val, str) and val.strip():
        return f'<p class="rsec-sub">{val}</p>'
    if isinstance(val, (list, tuple)):
        chips = "".join(f'<span class="ft">{x}</span>' for x in val if x)
        return f'<div class="ship-feats">{chips}</div>' if chips else ""
    return ""


def has_experience(line_slug, ship):
    exp = ship.get("exp") or {}
    le = (line_data(line_slug).get("experience") or {})
    return bool(exp) or bool(le.get("beverages") or le.get("kids"))


def experience_sections(lang, line_slug, ship):
    exp = ship.get("exp") or {}
    le = line_data(line_slug).get("experience") or {}
    name = ship["name"]
    out = ""

    # ── Photo strip (self-hosted, illustrative or licensed) ──
    photos = exp.get("photos") or []
    if photos:
        cards = "".join(
            f'<figure class="xphoto"><img src="{p["src"]}" alt="{p.get("alt","")}" loading="lazy">'
            + (f'<figcaption>{p["credit"]}</figcaption>' if p.get("credit") else "")
            + "</figure>" for p in photos if p.get("src"))
        note = ("Photos are illustrative." if lang == "en" else "Fotos ilustrativas.")
        out += _sec("photos", lang, f'<div class="xphotos">{cards}</div><p class="xnote">{note}</p>')

    # ── Overview ──
    ov = exp.get("overview")
    if ov:
        out += _sec("overview", lang, f'<p class="intro">{ov}</p>')

    # ── Food & dining ── rich, appetizing cards (emoji tile, cuisine, description, included/specialty)
    dining = [d for d in (exp.get("dining") or []) if d.get("name")]
    if dining:
        inc = sum(1 for d in dining if d.get("extra") is False)
        spec = sum(1 for d in dining if d.get("extra") is True)
        if inc or spec:
            sub = (f"{len(dining)} places to eat — {inc} included in your fare, {spec} specialty."
                   if lang == "en" else
                   f"{len(dining)} lugares para comer — {inc} incluidos, {spec} de especialidad.")
        else:
            sub = (f"{len(dining)} places to eat on board." if lang == "en"
                   else f"{len(dining)} lugares para comer a bordo.")
        cards = ""
        for d in dining:
            nm = d.get("name")
            t = d.get("type")
            tb = f'<span class="xd-cuisine">{_DTYPE[t][lang] if t in _DTYPE else t}</span>' if t else ""
            ex = d.get("extra")
            pill, desc = "", ""
            if ex is True:
                pill = f'<span class="xd-pill xd-spec">{_EXT[lang]}</span>'
            elif ex is False:
                pill = f'<span class="xd-pill xd-inc">{_INC[lang]}</span>'
            elif isinstance(ex, str) and ex.strip():
                desc = f'<p class="xd-desc">{ex}</p>'
            cards += (f'<article class="xd-card"><div class="xd-top"><span class="xd-emoji">{_food_emoji(nm, t)}</span>'
                      f'<div class="xd-h"><h3>{nm}</h3>{tb}</div>{pill}</div>'
                      f'<div class="xd-b">{desc}</div></article>')
        nudge = (_call(lang, "Want a specialty table booked before you sail? Our team sets it up when you call.")
                 if lang == "en" else
                 _call(lang, "¿Quieres reservar un restaurante de especialidad antes de zarpar? Lo hacemos por teléfono."))
        out += _sec("dining", lang, f'<p class="xsub">{sub}</p><div class="xd-grid">{cards}</div>{nudge}')

    # ── Drinks & packages (line-wide) ──
    bev = le.get("beverages") or []
    if bev:
        cards = "".join(
            f'<div class="xpkg"><h3>{b["name"]}</h3><p>{b.get("includes","")}</p></div>'
            for b in bev if b.get("name"))
        out += _sec("drinks", lang, f'<div class="xpkgs">{cards}</div>')

    # ── Activities ──
    acts = exp.get("activities")
    ai = _chips_or_p(acts)
    if ai:
        nudge = (_call(lang, f"A specialist knows which {name} activities book up fast and how to lock them in.")
                 if lang == "en" else
                 _call(lang, f"Un especialista sabe qué actividades de {name} se agotan rápido y cómo asegurarlas."))
        out += _sec("activities", lang, f'{ai}{nudge}')

    # ── Entertainment ──
    ent = _chips_or_p(exp.get("entertainment"))
    if ent:
        out += _sec("entertainment", lang, ent)

    # ── Kids, teens & families (line-wide dict + any ship note) ──
    kids = le.get("kids") or {}
    krows = ""
    for k, lbl in (("nursery", {"en": "Nursery", "es": "Guardería"}),
                   ("kids_club", {"en": "Kids club", "es": "Club infantil"}),
                   ("teens", {"en": "Teens", "es": "Adolescentes"}),
                   ("family", {"en": "Family cabins & notes", "es": "Camarotes familiares"})):
        v = kids.get(k)
        if v:
            krows += f'<div class="glance-cell"><b>{lbl[lang]}</b><span>{v}</span></div>'
    grid = f'<div class="glance-grid">{krows}</div>' if krows else ""
    ship_kids = _chips_or_p(exp.get("kids_family"))
    if grid or ship_kids:
        out += _sec("family", lang, f'{grid}{ship_kids}')

    # ── Decks & layout ──
    decks = exp.get("decks")
    nbh = exp.get("neighbourhoods") or exp.get("neighborhoods") or []
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

    # ── Bridge cam (availability only) ──
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
