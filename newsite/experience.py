# -*- coding: utf-8 -*-
"""Rich per-ship 'experience' sections — Onboard overview, Food & Dining, Drinks & packages,
Activities, Entertainment, Kids/Teens/Families, Decks & layout, Bridge cam — plus a self-hosted
photo strip. Each section renders ONLY when it has verified content (no fake placeholders).

Every list section renders as visual CARDS (emoji tile + name + description). Inputs are flexible:
activities / entertainment / kids_family may be a STRING (prose), a LIST of strings (name-only
cards), or a LIST of {name, desc} (rich cards). Dining is a LIST of {name, type, extra} where
`extra` is a bool (Included/Specialty pill) or a descriptive string. Per-ship content lives in
data/ships/<line>.json under each ship's "exp"; line-wide content in cruise-lines.json
"experience". NO PRICES. All prose is original — vivid but grounded in verified facts."""
from config import PHONE_HREF, PHONE_DISPLAY
from linepage import line_data

_H = {
    "photos": {"en": "On board", "es": "A bordo"},
    "overview": {"en": "The ship at a glance", "es": "El barco en resumen"},
    "dining": {"en": "Food & dining", "es": "Comida y restaurantes"},
    "drinks": {"en": "Drinks & packages", "es": "Bebidas y paquetes"},
    "activities": {"en": "Things to do", "es": "Qué hacer"},
    "entertainment": {"en": "Entertainment & nightlife", "es": "Entretenimiento y vida nocturna"},
    "family": {"en": "Kids, teens & families", "es": "Niños, adolescentes y familias"},
    "zones": {"en": "Districts & zones", "es": "Distritos y zonas"},
    "route": {"en": "Where & when it sails", "es": "Dónde y cuándo navega"},
    "decks": {"en": "Decks & layout", "es": "Cubiertas y distribución"},
    "cam": {"en": "Bridge cam", "es": "Cámara del puente"},
}
_IC = {"overview": "🚢", "dining": "🍽️", "drinks": "🍹", "activities": "🎢",
       "entertainment": "🎭", "family": "👨‍👩‍👧", "zones": "🧭", "route": "🗺️", "decks": "🛗", "cam": "📷"}
_DTYPE = {
    "main": {"en": "Main dining", "es": "Comedor principal"},
    "buffet": {"en": "Buffet", "es": "Bufé"},
    "casual": {"en": "Casual", "es": "Informal"},
    "specialty": {"en": "Specialty", "es": "Especialidad"},
}
_INC = {"en": "Included", "es": "Incluido"}
_EXT = {"en": "Extra", "es": "Extra"}

_FOOD_EMOJI = [
    (("pizza", "pizzeria"), "🍕"), (("burger",), "🍔"),
    (("sushi", "kaito", "robata"), "🍣"), (("teppanyaki",), "🍤"),
    (("steak", "butcher", "grill", "prime", "chophouse"), "🥩"), (("taco", "cantina", "mexican", "hola"), "🌮"),
    (("greek", "paxos"), "🥙"), (("seafood", "fish", "catch", "shack", "lobster", "far side"), "🦐"),
    (("italian", "eataly", "cucina", "pasta", "trattoria", "campo", "giovanni"), "🍝"),
    (("chicken",), "🍗"), (("coffee", "cafe", "café", "java", "emporium"), "☕"),
    (("chocolat", "sweet", "confection", "gelato", "ice cream", "dessert", "candy", "creamery"), "🍫"),
    (("buffet", "market", "marketplace", "lido", "horizon", "eats", "port of"), "🍽️"),
    (("sports bar", "all-star", "all star"), "🍺"),
    (("comedy", "karaoke", "loft", "piano"), "🎤"),
    (("gin", "cocktail", "mixolog", "champagne", "wine", "elixir", "bar", "lounge", "pub", "tavern", "brew", "tiki"), "🍸"),
    (("asian", "indochine", "wok", "noodle", "chibang"), "🥢"), (("bistro", "french", "brasserie", "atelier"), "🥐"),
    (("tapas", "spanish"), "🥘"), (("bbq", "smoke", "guy"), "🍖"), (("diner", "americana", "americas", "fins", "panini"), "🥞"),
    (("tea", "afternoon"), "🫖"), (("steakhouse", "jwb"), "🥩"),
]
_ACT_EMOJI = [
    (("thermal", "spa", "zen", "sanctuary", "aurea", "wellness", "sauna"), "💆"),
    (("water park", "waterpark", "aqua", "slide", "splash", "flowrider", "surf"), "🛝"),
    (("hot tub", "whirlpool", "jacuzzi"), "♨️"),
    (("pool", "swim", "solarium"), "🏊"),
    (("ropes", "climb", "zip", "sky", "adventure", "harbor", "ropes course", "go-kart", "kart"), "🧗"),
    (("sport", "court", "basketball", "track", "jog", "golf", "arcade", "bowl"), "⛳"),
    (("yacht club", "sundeck", "cabana", "retreat", "deck party", "top sail"), "🛥️"),
    (("gym", "fitness", "technogym", "yoga", "spin"), "🏋️"),
    (("kids", "playground", "family"), "🎠"),
    (("shop", "boutique", "retail", "mall"), "🛍️"),
]
_ENT_EMOJI = [
    (("theatre", "theater", "arena", "stage", "show", "production", "dome", "luna park", "cirque", "broadway"), "🎭"),
    (("comedy", "karaoke", "loft", "improv"), "🎤"),
    (("music", "band", "live", "jazz", "rock", "billboard", "piano", "big band"), "🎵"),
    (("casino",), "🎰"),
    (("sports bar",), "📺"),
    (("club", "disco", "night", "party", "dance"), "🪩"),
    (("cinema", "movie", "screen"), "🎬"),
    (("bar", "lounge", "pub"), "🍸"),
]


def _emoji(name, mapping, default):
    s = (name or "").lower()
    for keys, emo in mapping:
        if any(k in s for k in keys):
            return emo
    return default


def _food_emoji(name, t):
    return _emoji(f"{name or ''} {t or ''}", _FOOD_EMOJI, "🍴")


def _sec(key, lang, inner):
    return (f'<section id="x-{key}" class="section xsec xsec-{key}"><div class="wrap">'
            f'<h2 class="rsec-h"><span class="xic" aria-hidden="true">{_IC[key]}</span>{_H[key][lang]}</h2>'
            f'{inner}</div></section>')


def _call(lang, txt):
    c = "Call now" if lang == "en" else "Llama ahora"
    return (f'<div class="nudge"><p>{txt}</p>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'ship-exp\')">'
            f'<span class="ic" aria-hidden="true">☎</span>{c} · {PHONE_DISPLAY}</a></div>')


def _card(emoji, name, meta="", desc="", pill=""):
    body = f'<div class="xr-b"><p class="xr-desc">{desc}</p></div>' if desc else ""
    return (f'<article class="xr-card"><div class="xr-top"><span class="xr-emoji">{emoji}</span>'
            f'<div class="xr-h"><h3>{name}</h3>{meta}</div>{pill}</div>{body}</article>')


def _item_cards(items, emoji_map, default_emo):
    """Render a list of strings or {name,desc} dicts as a grid of rich cards."""
    cards = ""
    for it in items:
        if isinstance(it, dict):
            nm = it.get("name")
            if not nm:
                continue
            cards += _card(_emoji(nm, emoji_map, default_emo), nm, "", it.get("desc", ""))
        elif isinstance(it, str) and it.strip():
            cards += _card(_emoji(it, emoji_map, default_emo), it, "", "")
    return f'<div class="xr-grid">{cards}</div>' if cards else ""


def _flex(val, emoji_map, default_emo):
    """String -> prose; list -> rich cards. Returns ('', kind) if empty."""
    if isinstance(val, str) and val.strip():
        return f'<p class="xsub xsub-lead">{val}</p>'
    if isinstance(val, (list, tuple)) and val:
        return _item_cards(val, emoji_map, default_emo)
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

    # ── Photo strip ──
    photos = exp.get("photos") or []
    if photos:
        cards = "".join(
            f'<figure class="xphoto"><img src="{p["src"]}" alt="{p.get("alt","")}" loading="lazy">'
            + (f'<figcaption>{p["credit"]}</figcaption>' if p.get("credit") else "")
            + "</figure>" for p in photos if p.get("src"))
        note = ("Photos are illustrative." if lang == "en" else "Fotos ilustrativas.")
        out += _sec("photos", lang, f'<div class="xphotos">{cards}</div><p class="xnote">{note}</p>')

    # ── Overview + "Who it's for" ──
    ov = exp.get("overview")
    wf = exp.get("who_for")
    if ov or wf:
        inner = f'<p class="intro">{ov}</p>' if ov else ""
        if wf:
            lbl = "Who it's for" if lang == "en" else "Para quién es"
            inner += (f'<div class="whofor"><span class="whofor-ic" aria-hidden="true">🧭</span>'
                      f'<div><b>{lbl}</b><p>{wf}</p></div></div>')
        out += _sec("overview", lang, inner)

    # ── Where & when it sails (current-season deployment note) ──
    route = exp.get("deploy_note")
    if route:
        nudge = (_call(lang, "Not sailing your dates or from your port? Call — we'll find the ship that is.")
                 if lang == "en" else
                 _call(lang, "¿No navega en tus fechas o desde tu puerto? Llama — encontramos el barco que sí."))
        out += _sec("route", lang, f'<p class="rsec-sub">{route}</p>{nudge}')

    # ── Food & dining ──
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
            nm, t, ex = d.get("name"), d.get("type"), d.get("extra")
            meta = f'<span class="xr-meta">{_DTYPE[t][lang] if t in _DTYPE else t}</span>' if t else ""
            desc = (d.get("desc") or "").strip()
            pill = ""
            if ex is True:
                pill = f'<span class="xr-pill xr-spec">{_EXT[lang]}</span>'
            elif ex is False:
                pill = f'<span class="xr-pill xr-inc">{_INC[lang]}</span>'
            elif isinstance(ex, str) and ex.strip() and not desc:
                desc = ex.strip()
            cards += _card(_food_emoji(nm, t), nm, meta, desc, pill)
        nudge = (_call(lang, "Want a specialty table booked before you sail? Our team sets it up when you call.")
                 if lang == "en" else
                 _call(lang, "¿Quieres reservar un restaurante de especialidad? Lo hacemos por teléfono."))
        out += _sec("dining", lang, f'<p class="xsub">{sub}</p><div class="xr-grid">{cards}</div>{nudge}')

    # ── Drinks & packages (line-wide) ──
    bev = le.get("beverages") or []
    if bev:
        cards = "".join(
            f'<div class="xpkg"><h3>{b["name"]}</h3><p>{b.get("includes","")}</p></div>'
            for b in bev if b.get("name"))
        out += _sec("drinks", lang, f'<div class="xpkgs">{cards}</div>')

    # ── Things to do ──
    ai = _flex(exp.get("activities"), _ACT_EMOJI, "✨")
    if ai:
        nudge = (_call(lang, f"A specialist knows which {name} experiences book up fast — and locks them in for you.")
                 if lang == "en" else
                 _call(lang, f"Un especialista sabe qué experiencias de {name} se agotan rápido — y te las asegura."))
        out += _sec("activities", lang, f'{ai}{nudge}')

    # ── Entertainment ──
    ent = _flex(exp.get("entertainment"), _ENT_EMOJI, "🎭")
    if ent:
        out += _sec("entertainment", lang, ent)

    # ── Kids, teens & families ──
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
    ship_kids = _flex(exp.get("kids_family"), _ACT_EMOJI, "🧒")
    if grid or ship_kids:
        out += _sec("family", lang, f'{grid}{ship_kids}')

    # ── Districts & zones (own section — described cards when we have descriptions) ──
    nbh = exp.get("neighbourhoods") or exp.get("neighborhoods") or []
    if nbh:
        if isinstance(nbh[0], dict):
            inner = _item_cards(nbh, _ACT_EMOJI, "📍")
        else:
            chips = "".join(f'<span class="ft">{n}</span>' for n in nbh if n)
            inner = f'<div class="ship-feats">{chips}</div>'
        out += _sec("zones", lang, inner)

    # ── Decks & layout ──
    decks = exp.get("decks")
    if decks:
        lbl = "Passenger decks" if lang == "en" else "Cubiertas"
        out += _sec("decks", lang,
                    f'<div class="glance-grid"><div class="glance-cell"><b>{lbl}</b><span>{decks}</span></div></div>')

    # ── Bridge cam ──
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
