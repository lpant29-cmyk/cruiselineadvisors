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
    return (f'<section class="section {cls}"><div class="wrap"><h2 class="rsec-h">{_H[key][lang]}</h2>{inner}</div></section>')


def rich_sections(lang, slug):
    L = _CL.get(slug)
    if not L:
        return ""
    name = L["name"]
    out = ""

    # ── At a glance ──
    c = L.get("company", {})
    rows = [("founded", c.get("founded")), ("hq", c.get("headquarters")), ("parent", c.get("parent")),
            ("fleet_n", c.get("fleet_size")), ("loyalty", c.get("loyalty_program")),
            ("style", L.get("positioning", "").replace("-", " ").title())]
    grid = "".join(f'<div class="glance-cell"><b>{_L[k][lang]}</b><span>{_v(v, lang)}</span></div>' for k, v in rows)
    out += _sec("cream", "glance", lang, f'<div class="glance-grid">{grid}</div>')

    # ── Who it's for / not for ──
    ed = L.get("editorial", {})
    yes = "".join(f"<li>{x}</li>" for x in ed.get("who_its_for", []) if not _gap(x))
    no = "".join(f"<li>{x}</li>" for x in ed.get("who_its_not_for", []) if not _gap(x))
    if yes or no:
        out += _sec("", "fit", lang,
                    f'<div class="fit-grid"><div class="fit-col yes"><h3>✓ {_H["fityes"][lang]}</h3><ul>{yes}</ul></div>'
                    f'<div class="fit-col no"><h3>✕ {_H["fitno"][lang]}</h3><ul>{no}</ul></div></div>')

    # ── The fleet ──
    classes = L.get("ship_classes", [])
    if classes:
        cards = ""
        for s in classes:
            feats = "".join(f'<span class="ft">{f}</span>' for f in s.get("features", []) if not _gap(f))
            cards += (f'<article class="ship-card"><h3>{_v(s.get("class"), lang)} {"class" if lang=="en" else "clase"}</h3>'
                      f'<p class="ship-ships"><b>{_L["ships"][lang]}:</b> {_v(s.get("ships"), lang)}</p>'
                      f'<div class="ship-feats">{feats}</div></article>')
        nudge = (_nudge(lang, f"Not sure which {name} ship fits your trip? A specialist knows which ships sail where — and when."
                 if lang == "en" else
                 f"¿No sabes qué barco de {name} encaja? Un especialista sabe qué barcos navegan dónde — y cuándo."))
        out += _sec("cream", "fleet", lang, f'<div class="ship-grid">{cards}</div>{nudge}')

    # ── What's included ──
    inc = L.get("inclusions", {})
    yy = "".join(f'<li><b>{_v(i.get("item"), lang)}</b>{_note(i.get("note"))}</li>' for i in inc.get("included", []))
    nn = "".join(f'<li><b>{_v(i.get("item"), lang)}</b>{_note(i.get("note"))}</li>' for i in inc.get("extra_cost", []))
    if yy or nn:
        out += _sec("", "incl", lang,
                    f'<div class="incl-grid"><div class="incl-col yes"><h3>{_H["inclyes"][lang]}</h3><ul>{yy}</ul></div>'
                    f'<div class="incl-col no"><h3>{_H["inclno"][lang]}</h3><ul>{nn}</ul></div></div>')

    # ── Cabins ──
    cab = L.get("cabins", {})
    cats = cab.get("categories", [])
    if cats:
        chips = "".join(f'<span class="ft">{x}</span>' for x in cats if not _gap(x)) or f'<span class="cmp-gap">{GAP[lang]}</span>'
        nudge = (_nudge(lang, "The right cabin — and the numbers to avoid on each ship — is exactly what an advisor knows."
                 if lang == "en" else
                 "El camarote correcto — y los números a evitar en cada barco — es justo lo que sabe un asesor."))
        out += _sec("cream", "cabins", lang,
                    f'<p class="rsec-sub"><b>{_L["cats"][lang]}:</b></p><div class="ship-feats">{chips}</div>{nudge}')

    # ── Families ──
    fam = L.get("family", {})
    frows = [("kidsclub", fam.get("kids_club_name")), ("minage", fam.get("minimum_sailing_age"))]
    fgrid = "".join(f'<div class="glance-cell"><b>{_L[k][lang]}</b><span>{_v(v, lang)}</span></div>' for k, v in frows)
    out += _sec("", "family", lang, f'<div class="glance-grid">{fgrid}</div>')

    # ── Accessibility ──
    acc = L.get("accessibility", {})
    note = acc.get("tender_port_note")
    acc_inner = f'<p class="rsec-sub">{note}</p>' if note and not _gap(note) else f'<p class="rsec-sub cmp-gap">{GAP[lang]}</p>'
    out += _sec("cream", "access", lang, acc_inner)

    # ── Where & when ──
    it = L.get("itineraries", {})
    regs = [r.get("region") for r in it.get("regions", []) if isinstance(r, dict) and not _gap(r.get("region"))]
    irows = [("regions", regs or None), ("lengths", it.get("typical_lengths")), ("ports", it.get("home_ports"))]
    igrid = "".join(f'<div class="glance-cell"><b>{_L[k][lang]}</b><span>{_v(v, lang)}</span></div>' for k, v in irows)
    out += _sec("", "sails", lang, f'<div class="glance-grid">{igrid}</div>')

    # ── Cost drivers ──
    cd = ed.get("cost_drivers", [])
    if cd:
        items = "".join(f'<div class="cd-row"><b>{d.get("factor")}</b><span>{d.get("detail")}</span></div>'
                        for d in cd if isinstance(d, dict) and not _gap(d.get("factor")))
        nudge = (_nudge(lang, "Prices move daily by ship, date and cabin. One call gets you the real number for your trip — and the best rate our partners can offer."
                 if lang == "en" else
                 "Los precios cambian a diario por barco, fecha y camarote. Una llamada te da el número real — y la mejor tarifa que nuestros socios pueden ofrecer."))
        out += _sec("cream", "cost", lang, f'<div class="cd-list">{items}</div>{nudge}')

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
