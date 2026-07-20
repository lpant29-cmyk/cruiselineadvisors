# -*- coding: utf-8 -*-
"""Rich per-line content sections, rebuilt from data/cruise-lines.json (the fact store the old
detailed pages used): at-a-glance, who-it's-for, the fleet, what's included, cabins, families,
accessibility, where/when it sails, what drives cost, FAQ. Heavy call CTAs throughout.

Unverified fields (VERIFY/PENDING) render as visible "Not yet verified" gaps — never guessed.
NOTE: the JSON prose is English; ES pages show English deep content for now (headings/labels are
bilingual) — full ES translation of this content is a flagged follow-up."""
import json
import os
from config import PHONE_HREF, PHONE_DISPLAY
from ships import ships_for, slugify as ship_slug

_CL = {L["slug"]: L for L in json.load(
    open(os.path.join(os.path.dirname(__file__), "data", "cruise-lines.json"), encoding="utf-8"))["lines"]}

GAP = {"en": "Not yet verified", "es": "No verificado aún"}
_H = {
    "glance": {"en": "At a glance", "es": "De un vistazo"},
    "fit": {"en": "Is this the right line for you?", "es": "¿Es la línea adecuada para ti?"},
    "fityes": {"en": "A strong fit for", "es": "Una buena opción para"},
    "fitno": {"en": "Probably not for", "es": "Probablemente no para"},
    "fleet": {"en": "The fleet, class by class", "es": "La flota, clase por clase"},
    "incl": {"en": "What's included — and what isn't", "es": "Qué se incluye — y qué no"},
    "inclyes": {"en": "Included in your fare", "es": "Incluido en tu tarifa"},
    "inclno": {"en": "Costs extra", "es": "Cuesta extra"},
    "cabins": {"en": "Choosing a cabin", "es": "Elegir camarote"},
    "family": {"en": "Cruising with children", "es": "Cruceros con niños"},
    "access": {"en": "Accessibility", "es": "Accesibilidad"},
    "sails": {"en": "Where and when it sails", "es": "Dónde y cuándo navega"},
    "cost": {"en": "What actually drives the cost", "es": "Qué determina realmente el costo"},
    "faq": {"en": "Questions people actually ask", "es": "Preguntas que la gente hace"},
}
_L = {  # small bilingual labels
    "founded": {"en": "Founded", "es": "Fundada"}, "hq": {"en": "Headquarters", "es": "Sede"},
    "parent": {"en": "Parent company", "es": "Grupo propietario"}, "fleet_n": {"en": "Ships in fleet", "es": "Barcos en flota"},
    "loyalty": {"en": "Loyalty programme", "es": "Programa de fidelidad"}, "style": {"en": "Style", "es": "Estilo"},
    "ships": {"en": "Ships", "es": "Barcos"}, "regions": {"en": "Regions", "es": "Regiones"},
    "lengths": {"en": "Typical lengths", "es": "Duraciones típicas"}, "ports": {"en": "Home ports", "es": "Puertos base"},
    "kidsclub": {"en": "Kids club", "es": "Club infantil"}, "minage": {"en": "Minimum sailing age", "es": "Edad mínima"},
    "cats": {"en": "Categories offered", "es": "Categorías ofrecidas"},
}


def _gap(v):
    return v is None or (isinstance(v, str) and (v.strip() == "" or v.startswith("VERIFY") or v == "PENDING"))


def _v(v, lang):
    if _gap(v):
        return f'<span class="cmp-gap">{GAP[lang]}</span>'
    if isinstance(v, list):
        vv = ", ".join(str(x) for x in v if not _gap(x) and not isinstance(x, dict))
        return vv or f'<span class="cmp-gap">{GAP[lang]}</span>'
    return str(v)


def _note(n):
    """Render an item note, but hide it if it's empty, a gap, or carries a VERIFY marker."""
    return f' — {n}' if (n and not _gap(n) and "VERIFY" not in n) else ""


def _nudge(lang, txt):
    call = "Call now" if lang == "en" else "Llama ahora"
    return (f'<div class="nudge"><p>{txt}</p>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'line-nudge\')">'
            f'<span class="ic" aria-hidden="true">☎</span>{call} · {PHONE_DISPLAY}</a></div>')


def _sec(cls, key, lang, inner):
    return (f'<section id="s-{key}" class="section {cls}"><div class="wrap">'
            f'<h2 class="rsec-h">{_H[key][lang]}</h2>{inner}</div></section>')


# Short bilingual labels for the line-page table of contents (jump nav). Covers the rich sections
# here plus the facts/updates/compare/faq sections added in pages.py p_line.
TOC_LABELS = {
    "glance": {"en": "Overview", "es": "Resumen"},
    "fit": {"en": "Right for you?", "es": "¿Para ti?"},
    "fleet": {"en": "Ships", "es": "Barcos"},
    "incl": {"en": "Included", "es": "Incluido"},
    "cabins": {"en": "Cabins", "es": "Camarotes"},
    "family": {"en": "Families", "es": "Familias"},
    "access": {"en": "Accessibility", "es": "Accesibilidad"},
    "sails": {"en": "Where & when", "es": "Dónde y cuándo"},
    "cost": {"en": "Cost", "es": "Costo"},
    "facts": {"en": "The facts", "es": "Los datos"},
    "updates": {"en": "Updates", "es": "Novedades"},
    "compare": {"en": "Compare", "es": "Comparar"},
    "faq": {"en": "FAQ", "es": "Preguntas"},
}


def line_toc(lang, keys):
    """Jump nav over the sections that actually render on this line page."""
    if len(keys) < 3:
        return ""
    label = "On this page" if lang == "en" else "En esta página"
    items = "".join(f'<li><a href="#s-{k}">{TOC_LABELS[k][lang]}</a></li>'
                    for k in keys if k in TOC_LABELS)
    return (f'<section class="section" style="padding-top:0"><div class="wrap"><nav class="toc" aria-label="{label}">'
            f'<p class="toc-h">{label}</p><ul class="toc-list">{items}</ul></nav></div></section>')


def _num(n):
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)


def _fleet_inner(lang, slug, name, classes):
    """The fleet section body. Prefers the verified per-ship roster (ships.py) — each ship a card
    linking to its own page — and only falls back to class-level cards when no roster exists yet."""
    clsw = "class" if lang == "en" else "clase"
    guestsw = "guests" if lang == "en" else "huéspedes"
    view = "View ship" if lang == "en" else "Ver barco"
    ships = ships_for(slug)
    if ships:
        # group by class, preserving first-seen order; null class → "Other"
        order, groups = [], {}
        for s in ships:
            k = s.get("class") or ("Other" if lang == "en" else "Otros")
            if k not in groups:
                groups[k] = []
                order.append(k)
            groups[k].append(s)
        blocks = ""
        for k in order:
            cards = ""
            for s in groups[k]:
                meta = " · ".join(x for x in [
                    str(s["year"]) if s.get("year") else None,
                    f'{_num(s["guests"])} {guestsw}' if s.get("guests") else None,
                ] if x)
                cards += (
                    f'<a class="ship-card lk" href="/{lang}/lines/{slug}/ships/{ship_slug(s["name"])}/">'
                    f'<h3>{s["name"]}</h3>'
                    f'<p class="ship-ships">{meta or "&nbsp;"}</p>'
                    f'<span class="ship-more">{view} →</span></a>')
            head = (f'<h3 class="fleet-class">{k} {clsw}</h3>'
                    if k not in ("Other", "Otros") else "")
            blocks += f'{head}<div class="ship-grid">{cards}</div>'
        nudge = (_nudge(lang, f"Not sure which {name} ship fits your trip? A specialist knows which ships sail where — and when."
                 if lang == "en" else
                 f"¿No sabes qué barco de {name} encaja? Un especialista sabe qué barcos navegan dónde — y cuándo."))
        return f'{blocks}{nudge}'

    # fallback: class-level cards from cruise-lines.json
    if not classes:
        return ""
    cards = ""
    for s in classes:
        feats = "".join(f'<span class="ft">{f}</span>' for f in s.get("features", []) if not _gap(f))
        cards += (f'<article class="ship-card"><h3>{_v(s.get("class"), lang)} {clsw}</h3>'
                  f'<p class="ship-ships"><b>{_L["ships"][lang]}:</b> {_v(s.get("ships"), lang)}</p>'
                  f'<div class="ship-feats">{feats}</div></article>')
    nudge = (_nudge(lang, f"Not sure which {name} ship fits your trip? A specialist knows which ships sail where — and when."
             if lang == "en" else
             f"¿No sabes qué barco de {name} encaja? Un especialista sabe qué barcos navegan dónde — y cuándo."))
    return f'<div class="ship-grid">{cards}</div>{nudge}'


# Generic cabin-type descriptions (standard cruise knowledge — applies across lines). Matched by
# keyword against each line's published cabin category names.
_CABIN_DESC = [
    (("interior", "inside"), "🛏️",
     {"en": "The most affordable rooms — no window, but the same comfy beds, bathroom and service. Perfect if you plan to be out exploring.",
      "es": "Los camarotes más económicos — sin ventana, pero con las mismas camas, baño y servicio. Ideales si planeas estar fuera explorando."}),
    (("ocean view", "oceanview", "porthole", "outside", "obstructed"), "🪟",
     {"en": "A sealed window or porthole onto the sea — natural light and a view, without the extra of a balcony.",
      "es": "Una ventana o portilla sellada al mar — luz natural y vistas, sin el costo de un balcón."}),
    (("balcony", "veranda", "verandah", "infinite", "lanai"), "🌅",
     {"en": "Your own private outdoor space for morning coffee and sail-aways — the most popular choice for good reason.",
      "es": "Tu propio espacio exterior privado para el café de la mañana y las salidas — la opción más popular."}),
    (("yacht club", "retreat", "haven", "grill", "neptune", "pinnacle", "signature", "reserve", "sanctuary", "suite"), "👑",
     {"en": "The top tier — more space and usually extra perks like priority boarding, a private lounge, sundeck or concierge service.",
      "es": "La categoría superior — más espacio y ventajas como embarque prioritario, salón privado o servicio de conserje."}),
    (("spa", "aqua"), "💆",
     {"en": "Wellness-focused cabins with spa perks or thermal-suite access, usually in a quieter part of the ship.",
      "es": "Camarotes de bienestar con acceso al spa o suite térmica, en una zona más tranquila del barco."}),
    (("family", "harbor", "harbour"), "👨‍👩‍👧",
     {"en": "Roomier layouts and connecting options designed with families in mind.",
      "es": "Distribuciones más amplias y opciones conectadas pensadas para familias."}),
    (("solo", "single", "studio"), "🧍",
     {"en": "Cabins designed and priced for one traveller — no paying for an empty second bed.",
      "es": "Camarotes diseñados y con precio para una persona — sin pagar por una segunda cama vacía."}),
    (("concierge", "club", "premium"), "✨",
     {"en": "An enhanced category with upgraded perks and service, sitting between standard rooms and full suites.",
      "es": "Una categoría mejorada con ventajas y servicio superiores, entre los camarotes estándar y las suites."}),
]


def _cabin_card(name, lang):
    s = name.lower()
    emo, desc = "🛏️", {"en": "A distinct room category on this line — ask us exactly what it includes.",
                        "es": "Una categoría de camarote de esta línea — pregúntanos qué incluye."}
    for keys, e, d in _CABIN_DESC:
        if any(k in s for k in keys):
            emo, desc = e, d
            break
    return (f'<article class="cab-card"><span class="cab-emo">{emo}</span>'
            f'<div class="cab-b"><h3>{name}</h3><p>{desc[lang]}</p></div></article>')


# Self-hosted, Unsplash-licensed scenery (free for commercial use, no attribution). A per-port city
# image is used when available; otherwise a regional photo. Never claimed to be the exact terminal.
_ASSETS_PORTS = os.path.join(os.path.dirname(__file__), "assets", "ports")
_PORT_SLUG = [
    (("fort lauderdale", "lauderdale"), "fort-lauderdale"), (("port canaveral", "canaveral"), "port-canaveral"),
    (("palm beach",), "palm-beach"), (("miami",), "miami"), (("tampa",), "tampa"), (("jacksonville",), "jacksonville"),
    (("galveston",), "galveston"), (("new orleans",), "new-orleans"), (("mobile",), "mobile"),
    (("cape liberty", "new york", "brooklyn", "manhattan"), "new-york"),
    (("boston",), "boston"), (("baltimore",), "baltimore"), (("norfolk",), "norfolk"),
    (("long beach", "los angeles", "san pedro"), "los-angeles"), (("san diego",), "san-diego"), (("san francisco",), "san-francisco"),
    (("seattle",), "seattle"), (("vancouver",), "vancouver"), (("victoria",), "victoria"),
    (("seward",), "seward"), (("whittier",), "whittier"), (("honolulu",), "honolulu"),
    (("quebec",), "quebec-city"), (("montreal",), "montreal"), (("san juan",), "san-juan"),
]
_PORT_REGION = [
    (("miami", "lauderdale", "canaveral", "tampa", "palm beach", "jacksonville", "orlando"), "florida.jpg"),
    (("san juan", "puerto rico"), "caribbean.jpg"),
    (("seattle", "vancouver", "seward", "whittier", "victoria", "alaska"), "alaska.jpg"),
    (("new york", "cape liberty", "brooklyn", "manhattan"), "newyork.jpg"),
    (("los angeles", "long beach", "san diego", "san francisco", "san pedro"), "california.jpg"),
    (("honolulu", "hawaii", "oahu"), "hawaii.jpg"),
    (("boston", "baltimore", "norfolk", "quebec", "montreal", "portland"), "newengland.jpg"),
    (("galveston", "new orleans", "mobile"), "gulf.jpg"),
]


def _port_img(port):
    s = port.lower()
    for keys, slug in _PORT_SLUG:
        if any(k in s for k in keys):
            if os.path.exists(os.path.join(_ASSETS_PORTS, slug + ".jpg")):
                return slug + ".jpg"
            break
    for keys, img in _PORT_REGION:
        if any(k in s for k in keys):
            return img
    return "gulf.jpg"


def _port_card(port):
    return (f'<article class="port-card"><img src="/ports/{_port_img(port)}" alt="" loading="lazy">'
            f'<span class="port-nm">{port}</span></article>')


_LAST_SECTIONS = {}


def line_data(slug):
    """Full cruise-lines.json record for a line (used by experience.py for shared line-wide content)."""
    return _CL.get(slug, {})


def sections_present(slug):
    """Ordered rich-section keys that rendered for this line (set by rich_sections) — for the TOC."""
    return _LAST_SECTIONS.get(slug, [])


def rich_sections(lang, slug):
    L = _CL.get(slug)
    if not L:
        return ""
    name = L["name"]
    out = ""
    pres = []

    # ── At a glance ──
    c = L.get("company", {})
    # Ships-in-fleet is derived from our verified ship roster when the JSON field is unset.
    fleet_v = c.get("fleet_size")
    if _gap(fleet_v):
        _n = len(ships_for(slug))
        fleet_v = str(_n) if _n else None
    rows = [("founded", c.get("founded")), ("hq", c.get("headquarters")), ("parent", c.get("parent")),
            ("fleet_n", fleet_v), ("loyalty", c.get("loyalty_program")),
            ("style", L.get("positioning", "").replace("-", " ").title())]
    grid = "".join(f'<div class="glance-cell"><b>{_L[k][lang]}</b><span>{_v(v, lang)}</span></div>' for k, v in rows)
    out += _sec("cream", "glance", lang, f'<div class="glance-grid">{grid}</div>'); pres.append("glance")

    # ── Who it's for / not for ──
    ed = L.get("editorial", {})
    yes = "".join(f"<li>{x}</li>" for x in ed.get("who_its_for", []) if not _gap(x))
    no = "".join(f"<li>{x}</li>" for x in ed.get("who_its_not_for", []) if not _gap(x))
    if yes or no:
        out += _sec("", "fit", lang,
                    f'<div class="fit-grid"><div class="fit-col yes"><h3>✓ {_H["fityes"][lang]}</h3><ul>{yes}</ul></div>'
                    f'<div class="fit-col no"><h3>✕ {_H["fitno"][lang]}</h3><ul>{no}</ul></div></div>'); pres.append("fit")

    # ── The fleet ── real per-ship roster (linked) when we have it; else class-level cards.
    fleet = _fleet_inner(lang, slug, name, L.get("ship_classes", []))
    if fleet:
        out += _sec("cream", "fleet", lang, fleet); pres.append("fleet")

    # ── What's included ──
    inc = L.get("inclusions", {})
    yy = "".join(f'<li><b>{_v(i.get("item"), lang)}</b>{_note(i.get("note"))}</li>' for i in inc.get("included", []))
    nn = "".join(f'<li><b>{_v(i.get("item"), lang)}</b>{_note(i.get("note"))}</li>' for i in inc.get("extra_cost", []))
    if yy or nn:
        out += _sec("", "incl", lang,
                    f'<div class="incl-grid"><div class="incl-col yes"><h3>{_H["inclyes"][lang]}</h3><ul>{yy}</ul></div>'
                    f'<div class="incl-col no"><h3>{_H["inclno"][lang]}</h3><ul>{nn}</ul></div></div>'); pres.append("incl")

    # ── Cabins ──
    cab = L.get("cabins", {})
    cats = [x for x in cab.get("categories", []) if not _gap(x)]
    if cats:
        cards = "".join(_cabin_card(x, lang) for x in cats)
        nudge = (_nudge(lang, "The right cabin — and the numbers to avoid on each ship — is exactly what an advisor knows."
                 if lang == "en" else
                 "El camarote correcto — y los números a evitar en cada barco — es justo lo que sabe un asesor."))
        out += _sec("cream", "cabins", lang, f'<div class="cab-grid">{cards}</div>{nudge}'); pres.append("cabins")

    # ── Families ──
    fam = L.get("family", {})
    frows = [("kidsclub", fam.get("kids_club_name")), ("minage", fam.get("minimum_sailing_age"))]
    fgrid = "".join(f'<div class="glance-cell"><b>{_L[k][lang]}</b><span>{_v(v, lang)}</span></div>' for k, v in frows)
    out += _sec("", "family", lang, f'<div class="glance-grid">{fgrid}</div>'); pres.append("family")

    # ── Accessibility ──
    acc = L.get("accessibility", {})
    note = acc.get("tender_port_note")
    acc_inner = f'<p class="rsec-sub">{note}</p>' if note and not _gap(note) else f'<p class="rsec-sub cmp-gap">{GAP[lang]}</p>'
    out += _sec("cream", "access", lang, acc_inner); pres.append("access")

    # ── Where & when ── regions + lengths as cells; home ports as chips (readable for long lists)
    it = L.get("itineraries", {})
    regs = [r.get("region") for r in it.get("regions", []) if isinstance(r, dict) and not _gap(r.get("region"))]
    irows = [("regions", regs or None), ("lengths", it.get("typical_lengths"))]
    igrid = "".join(f'<div class="glance-cell"><b>{_L[k][lang]}</b><span>{_v(v, lang)}</span></div>' for k, v in irows)
    hp = [x for x in (it.get("home_ports") or []) if not _gap(x)]
    if hp:
        cards = "".join(_port_card(x) for x in hp)
        ports_html = f'<p class="rsec-sub" style="margin-top:16px"><b>{_L["ports"][lang]}:</b></p><div class="port-grid">{cards}</div>'
    else:
        ports_html = f'<p class="rsec-sub" style="margin-top:16px"><b>{_L["ports"][lang]}:</b> <span class="cmp-gap">{GAP[lang]}</span></p>'
    out += _sec("", "sails", lang, f'<div class="glance-grid">{igrid}</div>{ports_html}'); pres.append("sails")

    # ── Cost drivers ──
    cd = ed.get("cost_drivers", [])
    if cd:
        items = "".join(f'<div class="cd-row"><b>{d.get("factor")}</b><span>{d.get("detail")}</span></div>'
                        for d in cd if isinstance(d, dict) and not _gap(d.get("factor")))
        nudge = (_nudge(lang, "Prices move daily by ship, date and cabin. One call gets you the real number for your trip — and the best rate our partners can offer."
                 if lang == "en" else
                 "Los precios cambian a diario por barco, fecha y camarote. Una llamada te da el número real — y la mejor tarifa que nuestros socios pueden ofrecer."))
        out += _sec("cream", "cost", lang, f'<div class="cd-list">{items}</div>{nudge}'); pres.append("cost")

    _LAST_SECTIONS[slug] = pres
    return out


def faq_section(lang, slug):
    L = _CL.get(slug)
    if not L:
        return ""
    faqs = L.get("faqs", [])
    if not faqs:
        return ""
    items = "".join(f'<details class="faq2"><summary>{q.get("q")}</summary><p>{q.get("a")}</p></details>'
                    for q in faqs if isinstance(q, dict) and not _gap(q.get("q")) and not _gap(q.get("a")))
    if not items:
        return ""
    return _sec("", "faq", lang, f'<div class="faqwrap">{items}</div>')
