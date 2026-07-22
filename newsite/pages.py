# -*- coding: utf-8 -*-
"""Content page builders (everything except the homepage and legal). Each returns the inner
<main> HTML for a language; base.page() wraps head/header/footer/SEO. Original, compliant copy
only, no prices, real hours, per-line disclaimers, and unverified facts shown as visible gaps."""
import datetime
from config import PHONE_HREF, PHONE_DISPLAY, HOURS, SINCE_YEAR, BRAND
from data import LINES, DESTINATIONS
from facts import FACTS, LINE_FACTS, latest_verified
from badges import verified_stamp, verified_seal
from compare import compare_tool, line_compare_hero
from metasearch import metasearch_tool
from interactive import when_to_go, cabin_guide, SEASONS
from updates import all_updates, updates_for, update_cards, get_update
from directory import directory_section
from linepage import rich_sections, faq_section, sections_present, line_toc
from ships import ships_for, get_ship, sister_ships, slugify as ship_slug, source_of as ship_source
from shipcompare import ship_compare_tool, has_ship_compare, compare_hero
from experience import experience_sections, has_experience
from illus import ship_banner

YEAR = datetime.date.today().year
_L = {L["slug"]: L for L in LINES}
_D = {d["slug"]: d for d in DESTINATIONS}


def phero(lang, kicker, h1, sub, crumb, seal=""):
    seal_html = f'<div class="phero-seal">{seal}</div>' if seal else ""
    return f"""<section class="section navy phero"><div class="wrap">{seal_html}
  <p class="crumbs">{crumb}</p>
  <span class="eyebrow" style="color:#7FD4D0">{kicker}</span>
  <h1>{h1}</h1><p class="phero-sub">{sub}</p>
  <a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('phero')"><span class="ic">☎</span>{'Call now · ' if lang=='en' else 'Llama ahora · '}{PHONE_DISPLAY}</a>
</div></section>"""


def _guide_photo_hero(lang, kick, h1, sub, crumb, img):
    """Photo hero for a rich guide, self-hosted image + scrim + heading + call button."""
    inner = (f'<p class="crumbs">{crumb}</p><span class="eyebrow" style="color:#7FD4D0">{kick}</span>'
             f'<h1>{h1}</h1><p class="phero-sub">{sub}</p>'
             f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'guide-hero\')">'
             f'<span class="ic">☎</span>{"Call now · " if lang=="en" else "Llama ahora · "}{PHONE_DISPLAY}</a>')
    return (f'<section class="section phero dhero dhero-photo" style="--dhero-img:url(/guides/{img})">'
            f'<div class="dhero-scrim"></div><div class="wrap">{inner}</div></section>')


def cta_band(lang, title, sub):
    return f"""<section class="section cream"><div class="wrap"><div class="ctaband">
  <div><h2>{title}</h2><p>{sub}</p></div>
  <a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('band')"><span class="ic">☎</span>{PHONE_DISPLAY}</a>
</div></div></section>"""


def _crumb(lang, *parts):
    home = "Home" if lang == "en" else "Inicio"
    items = [f'<a href="/{lang}/index.html">{home}</a>'] + list(parts)
    return " › ".join(items)


def facts_table(lang, slug):
    gap = "Not yet verified" if lang == "en" else "No verificado aún"
    rows = ""
    for f in FACTS:
        cell = LINE_FACTS[slug][f["key"]]
        v = cell["v"]
        if v:
            val = v.get(lang, v.get("en")) if isinstance(v, dict) else v
            core = f"<b>{val}</b>"
            valhtml = f'<span class="fee">{core}</span>' if f.get("fee") else core
        else:
            valhtml = f'<span class="cmp-gap">{gap}</span>'
        imp = ' class="imp"' if f.get("imp") else ""
        rows += (f'<tr{imp}><th class="fact">{f["label"][lang]}<small>{f["note"][lang]}</small></th>'
                 f'<td class="cmp-cell">{valhtml}</td></tr>')
    return f'<div class="cmp-scroll"><table class="cmp-table facts-1col"><tbody>{rows}</tbody></table></div>'


# ─────────────────────────── cruise lines ───────────────────────────
def p_ships_dir(lang):
    """Full ship directory, every ship we cover, grouped by line, each linking to its own page.
    Reached from the Cruise Lines nav submenu and the lines hub."""
    guestsw = "guests" if lang == "en" else "huéspedes"
    view = "View ship" if lang == "en" else "Ver barco"
    kick = "Ship directory" if lang == "en" else "Directorio de barcos"
    h1 = "Every ship we cover, by line" if lang == "en" else "Cada barco que cubrimos, por línea"
    sub = ("Jump straight to any ship's verified guide, size, capacity, what's on board and where it "
           "sails. Then one call books the cabin." if lang == "en"
           else "Ve directo a la guía verificada de cualquier barco, tamaño, capacidad, qué hay a bordo y "
                "dónde navega. Luego una llamada reserva el camarote.")

    total = sum(len(ships_for(L["slug"])) for L in LINES)
    # quick-jump chips to each line's block
    chips = "".join(
        f'<a class="ship-jump" href="#line-{L["slug"]}">{L["emo"]} {L["name"]} '
        f'<b>{len(ships_for(L["slug"]))}</b></a>'
        for L in LINES if ships_for(L["slug"]))
    jump = f'<div class="ship-jumps">{chips}</div>'

    blocks = ""
    for L in LINES:
        ships = ships_for(L["slug"])
        if not ships:
            continue
        cards = ""
        for s in ships:
            meta = " · ".join(x for x in [
                str(s["year"]) if s.get("year") else None,
                f'{_num(s["guests"])} {guestsw}' if s.get("guests") else None,
            ] if x)
            cards += (
                f'<a class="ship-card lk" href="/{lang}/lines/{L["slug"]}/ships/{ship_slug(s["name"])}/">'
                f'<h3>{s["name"]}</h3>'
                f'<p class="ship-ships">{meta or "&nbsp;"}</p>'
                f'<span class="ship-more">{view} →</span></a>')
        allw = f'All {L["name"]} →' if lang == "en" else f'Todo {L["name"]} →'
        blocks += (
            f'<section class="section" id="line-{L["slug"]}"><div class="wrap">'
            f'<div class="shipdir-head"><h2 class="rsec-h">{L["emo"]} {L["name"]} '
            f'<span class="shipdir-n">{len(ships)}</span></h2>'
            f'<a class="shipdir-all" href="/{lang}/lines/{L["slug"]}/">{allw}</a></div>'
            f'<div class="ship-grid">{cards}</div></div></section>')

    intro = (f'<section class="section"><div class="wrap"><p class="note-line">'
             f'{"We cover " if lang == "en" else "Cubrimos "}<b>{total}</b>'
             f'{" ships across " if lang == "en" else " barcos en "}<b>{sum(1 for L in LINES if ships_for(L["slug"]))}</b>'
             f'{" lines." if lang == "en" else " líneas."}</p>{jump}</div></section>')

    return (phero(lang, kick, h1, sub, _crumb(lang,
                  f'<a href="/{lang}/cruise-lines/">{"Cruise lines" if lang == "en" else "Líneas"}</a>', kick))
            + intro + blocks
            + cta_band(lang, "Not sure which ship fits?" if lang == "en" else "¿No sabes qué barco encaja?",
                       "Tell a specialist your dates and who's travelling, they'll match the right ship." if lang == "en"
                       else "Dile a un especialista tus fechas y quién viaja, te emparejará con el barco correcto."))


def p_lines_hub(lang):
    from page_home import _pcard, ACCENTS
    cards = "".join(
        _pcard(f"/{lang}/lines/{L['slug']}.html", L['emo'], L['name'], L['cat'][lang], L['tag'][lang],
               ("Read the guide" if lang == "en" else "Leer la guía"), i)
        for i, L in enumerate(LINES))
    kick = "Cruise lines" if lang == "en" else "Líneas de crucero"
    h1 = "In-depth guides to every major line" if lang == "en" else "Guías detalladas de cada línea principal"
    sub = ("Honest, source-checked guides, ships class by class, what the fare covers, cabins, families, "
           "accessibility and timing. Then one call to a specialist who books it." if lang == "en"
           else "Guías honestas y verificadas, barcos clase por clase, qué cubre la tarifa, camarotes, familias, "
                "accesibilidad y temporada. Luego una llamada a un especialista que lo reserva.")
    note = ("These eight lines are our first in-depth guides. We cover 36 lines boardable from the Americas, "
            "call for any line not yet listed." if lang == "en"
            else "Estas ocho líneas son nuestras primeras guías. Cubrimos 36 líneas desde las Américas, "
                 "llama por cualquiera que aún no esté listada.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><div class="linegrid">{cards}</div>'
              f'<p class="note-line">{note}</p></div></section>'
            + directory_section(lang)
            + cta_band(lang, "Not sure which line fits?" if lang == "en" else "¿No sabes qué línea encaja?",
                       "Tell a specialist what you want, they'll match you to the right ship and sailing." if lang == "en"
                       else "Dile a un especialista qué quieres, te emparejará con el barco y la salida correctos."))


def p_line(lang, slug):
    L = _L[slug]
    kick = L["cat"][lang]
    crumb = _crumb(lang, f'<a href="/{lang}/cruise-lines.html">{"Cruise lines" if lang=="en" else "Líneas"}</a>', L["name"])
    if lang == "en":
        intro = (f"{L['name']} is best described as <b>{L['cat']['en'].lower()}</b>. {L['tag']['en']} "
                 f"Below is an independent, source-checked look at what actually matters before you book, "
                 f"and the money-and-complexity details worth a phone call.")
        who_h = "Is it right for you?"
        facts_h = "The facts that cost money"
        facts_sub = ("These are the details that quietly change your final bill and vary by fare, cabin and sailing. "
                     "We verify each from its source and re-check every 30 days; anything not yet verified is shown "
                     "as a gap rather than guessed.")
        disc = (f"We are an independent referral service. We are not affiliated with, sponsored by, endorsed by, "
                f"authorised by, or an agent of {L['name']}. {L['name']} and its ship names and logos are trademarks "
                f"of their owner, used here descriptively only.")
        cta_t, cta_s = f"Talk to a {L['name']} specialist", "Free, no obligation, and we never take payment for travel."
    else:
        intro = (f"{L['name']} se describe mejor como <b>{L['cat']['es'].lower()}</b>. {L['tag']['es']} "
                 f"A continuación, una mirada independiente y verificada a lo que realmente importa antes de reservar, "
                 f"y los detalles de dinero y complejidad que merecen una llamada.")
        who_h = "¿Es adecuada para ti?"
        facts_h = "Los datos que cuestan dinero"
        facts_sub = ("Son los detalles que cambian tu factura final y varían por tarifa, camarote y salida. "
                     "Verificamos cada uno desde su fuente y lo revisamos cada 30 días; lo que aún no está verificado "
                     "se muestra como un vacío, no se adivina.")
        disc = (f"Somos un servicio de referencia independiente. No estamos afiliados, patrocinados, respaldados, "
                f"autorizados por, ni somos agentes de {L['name']}. {L['name']} y sus nombres de barcos y logotipos "
                f"son marcas de su propietario, usadas aquí solo de forma descriptiva.")
        cta_t, cta_s = f"Habla con un especialista en {L['name']}", "Gratis, sin compromiso, y nunca cobramos por el viaje."
    name = L["name"]
    cmp_kick = "Compare" if lang == "en" else "Comparar"
    cmp_h2 = f"How does {name} compare?" if lang == "en" else f"¿Cómo se compara {name}?"
    cmp_sub = (f"Put {name} head-to-head with another line on the facts that cost money, then let an advisor apply them to your sailing."
               if lang == "en" else
               f"Compara {name} con otra línea en los datos que cuestan dinero, luego deja que un asesor los aplique a tu crucero.")
    upd_kick = "Updates" if lang == "en" else "Novedades"
    upd_h2 = f"Latest {name} updates" if lang == "en" else f"Últimas novedades de {name}"
    rich = rich_sections(lang, slug)  # sets sections_present(slug) as a side effect
    faq = faq_section(lang, slug)
    toc_keys = ["facts"] + sections_present(slug) + ["updates"] + (["faq"] if faq else [])
    facts_cta = ("These are exactly the details that surprise people at the pier and on the final bill. "
                 "Call and we'll confirm every one for your ship, cabin and dates, and the best rate our partners can offer."
                 if lang == "en" else
                 "Son justo los detalles que sorprenden en el muelle y en la factura final. Llama y confirmamos cada uno "
                 "para tu barco, camarote y fechas, y la mejor tarifa que nuestros socios pueden ofrecer.")
    # "The facts that cost money", moved high on the page (a strong attention section) with its own CTA.
    facts_section = (f'<section id="s-facts" class="section foam"><div class="wrap">'
                     f'<div class="sec-head"><span class="eyebrow">{kick}</span>'
                     f'<h2>{facts_h}</h2><p>{facts_sub}</p></div>{facts_table(lang, slug)}'
                     f'<div class="nudge"><p>{facts_cta}</p>'
                     f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'facts\')">'
                     f'<span class="ic" aria-hidden="true">☎</span>{"Call now" if lang == "en" else "Llama ahora"} · {PHONE_DISPLAY}</a></div>'
                     f'</div></section>')
    return (phero(lang, kick, L["name"], L["tag"][lang], crumb, seal=verified_seal(lang, latest_verified(slug)))
            + line_compare_hero(lang, slug, name)
            + f'<section class="section"><div class="wrap blk"><p class="intro">{intro}</p></div></section>'
            + line_toc(lang, toc_keys)
            + facts_section
            + rich
            + f'<section id="s-updates" class="section"><div class="wrap"><div class="sec-head"><span class="eyebrow">{upd_kick}</span>'
              f'<h2>{upd_h2}</h2></div>{update_cards(lang, updates_for(slug), show_line_tags=False)}</div></section>'
            + faq
            + related_guides(lang, "line", slug)
            + cta_band(lang, cta_t, cta_s)
            + f'<section class="section"><div class="wrap"><p class="disclaimer">{disc}</p></div></section>')


# ─────────────────────────── ships ───────────────────────────
_SHIP_L = {
    "class": {"en": "Ship class", "es": "Clase"},
    "year": {"en": "Entered service", "es": "En servicio desde"},
    "guests": {"en": "Guests", "es": "Huéspedes"},
    "tonnage": {"en": "Gross tonnage", "es": "Tonelaje bruto"},
    "crew": {"en": "Crew", "es": "Tripulación"},
    "length": {"en": "Length", "es": "Eslora"},
}


def _num(n):
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)


def _spec(label, val, lang, gap):
    inner = f"<b>{val}</b>" if val not in (None, "") else f'<span class="cmp-gap">{gap}</span>'
    return f'<div class="glance-cell"><b>{label}</b><span>{inner}</span></div>'


def p_ship(lang, line_slug, sslug):
    L = _L[line_slug]
    s = get_ship(line_slug, sslug)
    name = s["name"]
    _has_specs = bool(s.get("tonnage") or s.get("guests") or s.get("year"))
    gap = "Not yet verified" if lang == "en" else "No verificado aún"
    cls = s.get("class")
    linesw = "Cruise lines" if lang == "en" else "Líneas"
    crumb = _crumb(lang,
                   f'<a href="/{lang}/cruise-lines.html">{linesw}</a>',
                   f'<a href="/{lang}/lines/{line_slug}.html">{L["name"]}</a>', name)
    if cls:
        sub = (f'{cls} class · {L["name"]}' if lang == "en" else f'Clase {cls} · {L["name"]}')
    else:
        sub = L["name"]
    kick = L["cat"][lang]

    # verified specs, core four always shown (gap if missing); crew/length only when present
    cells = [(_SHIP_L["class"][lang], cls),
             (_SHIP_L["year"][lang], s.get("year")),
             (_SHIP_L["guests"][lang], _num(s["guests"]) if s.get("guests") else None),
             (_SHIP_L["tonnage"][lang], _num(s["tonnage"]) if s.get("tonnage") else None)]
    if s.get("crew"):
        cells.append((_SHIP_L["crew"][lang], _num(s["crew"])))
    if s.get("length"):
        cells.append((_SHIP_L["length"][lang], s["length"]))
    specs = "".join(_spec(lbl, val, lang, gap) for lbl, val in cells)
    # When a ship has rich experience content, that carries the on-board detail; otherwise show the
    # simple features list inside the specs block.
    _exp = has_experience(line_slug, s)
    feats = "".join(f'<li>{f}</li>' for f in s.get("features", []) if f)
    feats_h = "On board" if lang == "en" else "A bordo"
    feats_block = (f'<h2 class="rsec-h" style="margin-top:36px">{feats_h}</h2>'
                   f'<ul class="ship-feat-list">{feats}</ul>') if (feats and not _exp) else ""

    if lang == "en":
        intro = (f"{name} is part of {L['name']}'s fleet"
                 + (f", built to the {cls} class" if cls else "") + ". "
                 "Below are the verified basics; sailings, itineraries, cabins and the current rate change "
                 "constantly, one call to a specialist confirms exactly what's open for your dates and the best "
                 "rate our partners can offer.")
        specs_h = "The basics, verified"
        note = ("Every figure here traces to a published source and is re-checked on our normal schedule. Anything "
                "we haven't confirmed shows as a gap rather than a guess.")
        sisters_h = f"Other {cls} ships" if cls else f"More {L['name']} ships"
        nudge_txt = (f"Want {name} for your dates? A specialist checks live availability and holds the best cabin "
                     "for you, call now.")
        cta_t, cta_s = f"Sail on {name}?", "Free, no obligation, and we never take payment for travel."
        disc = (f"Independent referral service, not affiliated with, sponsored by, endorsed by or an agent of "
                f"{L['name']}. {L['name']}, {name} and related names and logos are trademarks of their owner, used "
                f"here descriptively only.")
    else:
        intro = (f"{name} forma parte de la flota de {L['name']}"
                 + (f", de la clase {cls}" if cls else "") + ". "
                 "Abajo están los datos verificados; las salidas, itinerarios, camarotes y la tarifa actual cambian "
                 "constantemente, una llamada a un especialista confirma qué hay disponible para tus fechas y la "
                 "mejor tarifa que nuestros socios pueden ofrecer.")
        specs_h = "Los datos, verificados"
        note = ("Cada cifra proviene de una fuente publicada y se revisa en nuestro calendario habitual. Lo que no "
                "hemos confirmado se muestra como un vacío, no como una suposición.")
        sisters_h = f"Otros barcos clase {cls}" if cls else f"Más barcos de {L['name']}"
        nudge_txt = (f"¿Quieres {name} para tus fechas? Un especialista revisa la disponibilidad en vivo y te reserva "
                     "el mejor camarote, llama ahora.")
        cta_t, cta_s = f"¿Navegar en {name}?", "Gratis, sin compromiso, y nunca cobramos por el viaje."
        disc = (f"Servicio de referencia independiente, no afiliado, patrocinado, respaldado ni agente de "
                f"{L['name']}. {L['name']}, {name} y los nombres y logotipos relacionados son marcas de su "
                f"propietario, usados aquí solo de forma descriptiva.")

    # sister ships
    sisters = sister_ships(line_slug, s)
    sisters_block = ""
    if sisters:
        cards = "".join(
            f'<a class="ship-card lk" href="/{lang}/lines/{line_slug}/ships/{ship_slug(x["name"])}/">'
            f'<h3>{x["name"]}</h3>'
            f'<p class="ship-ships">{(str(x["year"]) if x.get("year") else "&nbsp;")}</p>'
            f'<span class="ship-more">{"View ship" if lang=="en" else "Ver barco"} →</span></a>'
            for x in sisters)
        sisters_block = (f'<section class="section" id="ship-sisters"><div class="wrap"><h2 class="rsec-h">{sisters_h}</h2>'
                         f'<div class="ship-grid">{cards}</div></div></section>')

    back = (f'<a class="ship-back" href="/{lang}/lines/{line_slug}/">'
            f'← {"All " + L["name"] + " ships" if lang=="en" else "Todos los barcos de " + L["name"]}</a>')

    # the ship-compare tool now lives in the Compare-hero band at the top of the page.
    # Build the experience sections first so the table of contents can list exactly what rendered.
    from experience import ship_toc
    exp_html = experience_sections(lang, line_slug, s)
    toc_tail = [("#ship-sisters", sisters_h)] if sisters else []
    toc = ship_toc(lang, "ship-basics", specs_h, tail=toc_tail)
    return (phero(lang, kick, name, sub, crumb, seal=(verified_seal(lang, ship_source(line_slug)[1]) if _has_specs else ""))
            + compare_hero(lang, default_a=f"{line_slug}::{sslug}", ship_name=name)
            + f'<section class="section"><div class="wrap blk"><p class="intro">{intro}</p></div></section>'
            + ship_banner(lang)
            + toc
            + f'<section class="section cream" id="ship-basics"><div class="wrap">'
              f'<h2 class="rsec-h">{specs_h}</h2>'
              f'<div class="glance-grid">{specs}</div>{feats_block}'
              f'<p class="note-line" style="margin-top:20px">{note}</p>'
              f'{_ship_nudge(lang, nudge_txt)}</div></section>'
            + exp_html
            + sisters_block
            + related_guides(lang, "ship", sslug)
            + f'<section class="section"><div class="wrap">{back}</div></section>'
            + cta_band(lang, cta_t, cta_s)
            + f'<section class="section"><div class="wrap"><p class="disclaimer">{disc}</p></div></section>')


def _ship_nudge(lang, txt):
    call = "Call now" if lang == "en" else "Llama ahora"
    return (f'<div class="nudge"><p>{txt}</p>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'ship-nudge\')">'
            f'<span class="ic" aria-hidden="true">☎</span>{call} · {PHONE_DISPLAY}</a></div>')


# ─────────────────────────── compare + facts ───────────────────────────
def p_compare(lang):
    kick = "Find a cruise" if lang == "en" else "Encuentra tu crucero"
    h1 = "Find your cruise, then call to book it" if lang == "en" else "Encuentra tu crucero, luego llama para reservar"
    sub = ("Skip scrolling hundreds of pages. Tell us where and when, we'll line up the ships that fit, and one "
           "call books the right one at the best rate our partners can offer." if lang == "en"
           else "Sin revisar cientos de páginas. Dinos dónde y cuándo, alineamos los barcos que encajan, y una "
                "llamada reserva el correcto a la mejor tarifa que nuestros socios pueden ofrecer.")
    also = ("Prefer to compare two lines head-to-head? Every line and ship page has its own compare tool at the top."
            if lang == "en" else
            "¿Prefieres comparar dos líneas? Cada página de línea y barco tiene su comparador arriba.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap">{metasearch_tool(lang)}'
              f'<p class="note-line" style="margin-top:22px">{also}</p></div></section>')


def p_facts(lang):
    kick = "Cruise facts" if lang == "en" else "Datos de cruceros"
    h1 = "The cruise facts that cost you money" if lang == "en" else "Los datos de crucero que te cuestan dinero"
    sub = ("The details cruise sites bury, gratuities, what's included, cancellation, documents. Here's what each "
           "one means and what to ask." if lang == "en"
           else "Los detalles que los sitios esconden, propinas, qué se incluye, cancelación, documentos. Esto es "
                "lo que significa cada uno y qué preguntar.")
    items = "".join(
        f'<div class="card"><div class="ic-badge">{"💸" if f.get("imp") else "🧭"}</div>'
        f'<h3>{f["label"][lang]}</h3><p>{f["note"][lang]}.</p></div>' for f in FACTS)
    facts_intro = ("We verify each of these from its source and re-check every 30 days. Compare any two lines below."
                   if lang == "en" else
                   "Verificamos cada uno desde su fuente y lo revisamos cada 30 días. Compara dos líneas abajo.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><p class="intro">{facts_intro}</p>'
              f'<div class="grid3" style="margin-top:18px">{items}</div></div></section>'
            + f'<section class="section foam"><div class="wrap">{compare_tool(lang)}</div></section>'
            + cta_band(lang, "Which of these applies to your trip?" if lang == "en" else "¿Cuáles aplican a tu viaje?",
                       "An advisor checks every one against your dates, cabin and party." if lang == "en"
                       else "Un asesor revisa cada uno según tus fechas, camarote y grupo."))


# ─────────────────────────── destinations ───────────────────────────
def p_dest_hub(lang):
    from destpage import hero_image
    cards = ""
    for d in DESTINATIONS:
        img = hero_image(d["slug"])
        media = (f'<img src="/ports/{img}" alt="{d["name"][lang]}" loading="lazy" decoding="async">'
                 if img else "")
        best = d.get("best", {}).get(lang, "")
        best_html = f'<small>{("Best" if lang == "en" else "Mejor")}: {best}</small>' if best else ""
        cards += (f'<a class="port-card destx-card" href="/{lang}/destinations/{d["slug"]}/">{media}'
                  f'<span class="port-nm">{d["emo"]} {d["name"][lang]}{best_html}</span></a>')
    kick = "Destinations" if lang == "en" else "Destinos"
    h1 = "Where do you want to sail?" if lang == "en" else "¿A dónde quieres navegar?"
    sub = ("Every region runs on a season. Pick the right month and the whole trip gets better." if lang == "en"
           else "Cada región tiene su temporada. Elige el mes correcto y todo el viaje mejora.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><div class="port-grid destx-grid">{cards}</div></div></section>'
            + when_to_go(lang)
            + cta_band(lang, "Not sure when to go?" if lang == "en" else "¿No sabes cuándo ir?",
                       "An advisor matches your dates to the region that's actually in season." if lang == "en"
                       else "Un asesor ajusta tus fechas a la región que está en temporada."))


def _faq_block(lang, faqs):
    """Render an FAQ accordion + matching FAQPage JSON-LD for rich results."""
    if not faqs:
        return ""
    import json as _json
    h = "Common questions" if lang == "en" else "Preguntas frecuentes"
    items = "".join(
        f'<details class="faq-item"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>'
        for q, a in faqs)
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    script = '<script type="application/ld+json">' + _json.dumps(ld, ensure_ascii=False) + '</script>'
    return (f'<section class="section" id="d-faq"><div class="wrap"><h2 class="rsec-h">{h}</h2>'
            f'<div class="faq-list">{items}</div>{script}</div></section>')


def p_region(lang, slug):
    from destpage import has_region_guide, region_guide, region_faqs, dest_hero, more_destinations, dest_toc
    d = _D[slug]
    if has_region_guide(slug):
        crumb = _crumb(lang, f'<a href="/{lang}/destinations.html">{"Destinations" if lang=="en" else "Destinos"}</a>', d["name"][lang])
        sub = (f"When to sail, where you leave from, which ships go, and one call to book."
               if lang == "en" else "Cuándo navegar, desde dónde sales, qué barcos van, y una llamada para reservar.")
        guide = region_guide(lang, slug, d["name"][lang])  # populates the section list for the TOC
        faqs = region_faqs(lang, slug, d["name"][lang])
        toc_extra = [("d-faq", "Common questions" if lang == "en" else "Preguntas frecuentes")] if faqs else []
        return (dest_hero(lang, slug, d["name"][lang], sub, crumb)
                + dest_toc(lang, extra=toc_extra)
                + guide
                + _faq_block(lang, faqs)
                + related_guides(lang, "dest", slug)
                + more_destinations(lang, slug, DESTINATIONS))
    s = SEASONS.get(slug, {})
    peak = s.get("peak", {}).get(lang, "") if isinstance(s.get("peak"), dict) else ""
    kick = "Destination" if lang == "en" else "Destino"
    crumb = _crumb(lang, f'<a href="/{lang}/destinations.html">{"Destinations" if lang=="en" else "Destinos"}</a>', d["name"][lang])
    if lang == "en":
        body = (f"<b>Best time to sail:</b> {d['best']['en']}" + (f" (peak {peak})" if peak else "") + ". "
                "Seasons decide far more than the ship does, the right month means better weather, calmer seas and "
                "the itineraries you actually want. An advisor confirms which ships sail your dates and matches the "
                "sailing to your party.")
        warn = ("This is an Atlantic hurricane-season region (1 June-30 November). Sailings still operate and reroute "
                "when needed, but travel insurance matters more in these months." if s.get("warn") else "")
    else:
        body = (f"<b>Mejor época para navegar:</b> {d['best']['es']}" + (f" (pico {peak})" if peak else "") + ". "
                "La temporada decide mucho más que el barco, el mes correcto significa mejor clima, mares más "
                "tranquilos y los itinerarios que quieres. Un asesor confirma qué barcos navegan en tus fechas.")
        warn = ("Es una región de temporada de huracanes del Atlántico (1 jun-30 nov). Los cruceros operan y se "
                "redirigen cuando es necesario, pero el seguro de viaje importa más en estos meses." if s.get("warn") else "")
    warn_html = f'<div class="whn-warn" style="margin-top:16px">⚠ {warn}</div>' if warn else ""
    return (phero(lang, kick, d["name"][lang], (f"Best: {d['best'][lang]}" if lang == "en" else f"Mejor: {d['best'][lang]}"), crumb)
            + f'<section class="section"><div class="wrap blk"><p class="intro">{body}</p>{warn_html}</div></section>'
            + cta_band(lang, f"Sail {d['name'][lang]}?" if lang == "en" else f"¿Navegar a {d['name'][lang]}?",
                       "Call and we'll line up the lines and dates that fit." if lang == "en"
                       else "Llama y alineamos las líneas y fechas que encajan."))


# ─────────────────────────── guides ───────────────────────────
GUIDES = [
    {"slug": "first-time-cruisers", "emo": "🧭",
     "t": {"en": "First-time cruisers", "es": "Primer crucero"},
     "d": {"en": "What nobody tells you before your first sailing, from boarding to disembark.",
           "es": "Lo que nadie te dice antes de tu primer crucero, del embarque al desembarque."}},
    {"slug": "choosing-a-cabin", "emo": "🛏️",
     "t": {"en": "Choosing a cabin", "es": "Elegir camarote"},
     "d": {"en": "Interior to suite, what you get, what to watch for, and the cabins to avoid.",
           "es": "De interior a suite, qué obtienes, qué vigilar y los camarotes a evitar."}},
    {"slug": "whats-included", "emo": "🧾",
     "t": {"en": "What's included", "es": "Qué se incluye"},
     "d": {"en": "The gap between the fare and your final bill, explained plainly.",
           "es": "La diferencia entre la tarifa y tu factura final, explicada con claridad."}},
    {"slug": "cruise-gratuities-explained", "emo": "🧾",
     "t": {"en": "Cruise gratuities explained", "es": "Propinas de crucero, explicadas"},
     "d": {"en": "The daily service charge, how it works, who it goes to, and how to plan for it.",
           "es": "El cargo por servicio diario, cómo funciona, a quién va y cómo planearlo."}},
    {"slug": "how-to-find-affordable-cruise", "emo": "💰",
     "t": {"en": "Find an affordable cruise", "es": "Encontrar un crucero accesible"},
     "d": {"en": "The real levers that move the price, without the fake-deal gimmicks.",
           "es": "Las palancas reales que mueven el precio, sin trucos de ofertas falsas."}},
    {"slug": "cruise-deposit-payment-cancellation", "emo": "📆",
     "t": {"en": "Deposits, payment & cancellation", "es": "Depósitos, pago y cancelación"},
     "d": {"en": "The booking timeline that keeps you in control of your money.",
           "es": "El calendario de reserva que te mantiene en control de tu dinero."}},
    {"slug": "drink-packages-worth-it", "emo": "🍸",
     "t": {"en": "Are drink packages worth it?", "es": "¿Valen la pena los paquetes de bebidas?"},
     "d": {"en": "How to tell, plus the whole-cabin rule that catches people out.",
           "es": "Cómo saberlo, y la regla de todo el camarote que sorprende a muchos."}},
    {"slug": "cruise-wifi-explained", "emo": "📶",
     "t": {"en": "Cruise Wi-Fi explained", "es": "Wi-Fi en crucero, explicado"},
     "d": {"en": "Packages, tiers and what to realistically expect at sea.",
           "es": "Paquetes, niveles y qué esperar de verdad en el mar."}},
    {"slug": "refundable-vs-non-refundable", "emo": "🔄",
     "t": {"en": "Refundable vs non-refundable", "es": "Reembolsable vs no reembolsable"},
     "d": {"en": "Which fare type fits your plans, and where insurance helps.",
           "es": "Qué tipo de tarifa encaja con tus planes, y dónde ayuda el seguro."}},
    {"slug": "hidden-cruise-costs", "emo": "🔍",
     "t": {"en": "Hidden cruise costs", "es": "Costos ocultos de un crucero"},
     "d": {"en": "The extras first-timers forget to budget for, in one checklist.",
           "es": "Los extras que los primerizos olvidan presupuestar, en una lista."}},
    {"slug": "how-cruise-pricing-works", "emo": "📈",
     "t": {"en": "How cruise pricing works", "es": "Cómo funciona el precio de un crucero"},
     "d": {"en": "Why fares vary, how lines price a sailing, and how to time it right.",
           "es": "Por qué varían las tarifas, cómo fijan precios y cómo elegir el momento."}},
    {"slug": "what-to-pack-for-a-cruise", "emo": "🧳",
     "t": {"en": "What to pack for a cruise", "es": "Qué llevar a un crucero"},
     "d": {"en": "The smart carry-on and cabin checklist, plus what not to bring.",
           "es": "La lista inteligente de equipaje de mano y camarote, y qué no llevar."}},
    {"slug": "cruise-embarkation-day", "emo": "🛳️",
     "t": {"en": "Cruise embarkation day", "es": "Día de embarque"},
     "d": {"en": "What to expect on day one, step by step, from terminal to sailaway.",
           "es": "Qué esperar el primer día, paso a paso, de la terminal al sailaway."}},
    {"slug": "big-ship-vs-small-ship", "emo": "🚢",
     "t": {"en": "Big ship vs small ship", "es": "Barco grande vs pequeño"},
     "d": {"en": "Floating resort or intimate vessel? How to pick the size that fits.",
           "es": "¿Resort flotante o barco íntimo? Cómo elegir el tamaño que encaja."}},
    {"slug": "avoid-cruise-scams", "emo": "🛡️",
     "t": {"en": "Avoid cruise scams & robocalls", "es": "Evitar estafas y llamadas automáticas"},
     "d": {"en": "The red flags behind fake offers and robocalls, and how to stay safe.",
           "es": "Las señales de alarma tras ofertas falsas y llamadas, y cómo protegerte."}},
    {"slug": "free-cruise-offer-red-flags", "emo": "🎣",
     "t": {"en": "Is that free cruise offer real?", "es": "¿Es real esa oferta de crucero gratis?"},
     "d": {"en": "Tell a genuine promotion from the bait that is after your card number.",
           "es": "Distingue una promoción genuina del cebo que busca tu tarjeta."}},
    {"slug": "cruise-documents-id", "emo": "🛂",
     "t": {"en": "Cruise documents & ID", "es": "Documentos e identificación"},
     "d": {"en": "Passport vs birth certificate, and what you need to board.",
           "es": "Pasaporte vs acta de nacimiento, y qué necesitas para embarcar."}},
    {"slug": "how-to-choose-a-cruise-line", "emo": "🚢",
     "t": {"en": "How to choose a cruise line", "es": "Cómo elegir una línea de crucero"},
     "d": {"en": "Match the line to how you travel, in three quick steps.",
           "es": "Ajusta la línea a cómo viajas, en tres pasos rápidos."}},
    {"slug": "solo-cruising", "emo": "🧍",
     "t": {"en": "Solo cruising", "es": "Cruceros para solos"},
     "d": {"en": "The single supplement, solo cabins, and how to travel alone well.",
           "es": "El suplemento individual, camarotes para solos y cómo viajar solo bien."}},
    {"slug": "how-to-choose-a-destination", "emo": "🗺️",
     "t": {"en": "How to choose a destination", "es": "Cómo elegir un destino"},
     "d": {"en": "Let the season point you to the region that fits your trip.",
           "es": "Deja que la temporada te señale la región que encaja."}},
    {"slug": "when-to-cruise", "emo": "🗓️",
     "t": {"en": "When to cruise", "es": "Cuándo hacer un crucero"},
     "d": {"en": "Season by season, region by region, timing beats everything.",
           "es": "Temporada por temporada, región por región, el momento lo es todo."}},
    {"slug": "groups-and-families", "emo": "👨‍👩‍👧",
     "t": {"en": "Groups & families", "es": "Grupos y familias"},
     "d": {"en": "Connecting cabins, kids' clubs, group dining and split payments, sorted.",
           "es": "Camarotes conectados, clubes infantiles, comida en grupo y pagos divididos."}},
    {"slug": "accessibility", "emo": "♿",
     "t": {"en": "Accessible cruising", "es": "Cruceros accesibles"},
     "d": {"en": "Accessible cabins, tendering, and what to confirm before you book.",
           "es": "Camarotes accesibles, transbordos y qué confirmar antes de reservar."}},
]
_G = {g["slug"]: g for g in GUIDES}

# ── Guide categorisation + contextual interlinking ────────────────────────────────────────────────
# Categories for the guides hub (ordered). Contexts (ctx) decide where a guide surfaces around the
# site: "home", "line", "ship", "dest". For a guide about a SPECIFIC line/ship/destination, add its
# slug to for_lines / for_ships / for_dests and it auto-attaches to that page (future-proofing).
GUIDE_CATS = [
    ("costs", {"en": "Cruise costs & money", "es": "Costos y dinero"}),
    ("planning", {"en": "Planning your cruise", "es": "Planea tu crucero"}),
    ("who", {"en": "Who's travelling", "es": "Quién viaja"}),
    ("line", {"en": "Choosing a line & ship", "es": "Elegir línea y barco"}),
    ("dest", {"en": "Destinations & timing", "es": "Destinos y temporada"}),
    ("safety", {"en": "Smart & safe booking", "es": "Reserva inteligente y segura"}),
]
_CAT_TITLE = dict(GUIDE_CATS)

GUIDE_META = {
    "first-time-cruisers": {"cat": "planning", "ctx": ["home", "ship", "dest"]},
    "choosing-a-cabin": {"cat": "planning", "ctx": ["line", "ship"]},
    "whats-included": {"cat": "costs", "ctx": ["home", "line", "ship", "dest"]},
    "cruise-gratuities-explained": {"cat": "costs", "ctx": ["line", "ship"]},
    "how-to-find-affordable-cruise": {"cat": "costs", "ctx": ["home", "line", "dest"]},
    "cruise-deposit-payment-cancellation": {"cat": "costs", "ctx": ["line"]},
    "drink-packages-worth-it": {"cat": "costs", "ctx": ["line", "ship"]},
    "cruise-wifi-explained": {"cat": "costs", "ctx": ["line", "ship"]},
    "refundable-vs-non-refundable": {"cat": "costs", "ctx": ["line"]},
    "hidden-cruise-costs": {"cat": "costs", "ctx": ["home", "line", "ship"]},
    "how-cruise-pricing-works": {"cat": "costs", "ctx": ["home", "line"]},
    "what-to-pack-for-a-cruise": {"cat": "planning", "ctx": ["ship"]},
    "cruise-embarkation-day": {"cat": "planning", "ctx": ["ship"]},
    "big-ship-vs-small-ship": {"cat": "line", "ctx": ["line", "ship"]},
    "avoid-cruise-scams": {"cat": "safety", "ctx": ["home"]},
    "free-cruise-offer-red-flags": {"cat": "safety", "ctx": ["home"]},
    "cruise-documents-id": {"cat": "planning", "ctx": ["dest"]},
    "how-to-choose-a-cruise-line": {"cat": "line", "ctx": ["home", "line"]},
    "solo-cruising": {"cat": "who", "ctx": ["line", "ship"]},
    "how-to-choose-a-destination": {"cat": "dest", "ctx": ["home", "dest"]},
    "when-to-cruise": {"cat": "dest", "ctx": ["dest"]},
    "groups-and-families": {"cat": "who", "ctx": ["ship", "line"]},
    "accessibility": {"cat": "who", "ctx": ["ship", "line"]},
}
_CTX_FORKEY = {"line": "for_lines", "ship": "for_ships", "dest": "for_dests"}


def _guide_thumb(slug):
    """The guide's hero image filename for a thumbnail, or None (then we show an emoji tile)."""
    import guides_content  # noqa: F401 — ensure RICH_GUIDES (with per-guide hero overrides) is populated
    from guidepage import RICH_GUIDES, guide_hero_img
    return guide_hero_img(slug, RICH_GUIDES.get(slug, {}).get("hero"))


def guide_card(lang, slug):
    """A guide card with a self-hosted thumbnail (or emoji tile) + title + one-liner."""
    g = _G.get(slug)
    if not g:
        return ""
    thumb = _guide_thumb(slug)
    media = (f'<span class="gcard-media"><img src="/guides/{thumb}" alt="" loading="lazy" decoding="async"></span>'
             if thumb else f'<span class="gcard-media gcard-emo"><span aria-hidden="true">{g["emo"]}</span></span>')
    read = "Read guide" if lang == "en" else "Leer guía"
    return (f'<a class="gcard" href="/{lang}/guides/{slug}/">{media}'
            f'<span class="gcard-body"><span class="gcard-t">{g["t"][lang]}</span>'
            f'<span class="gcard-d">{g["d"][lang]}</span>'
            f'<span class="gcard-read">{read} →</span></span></a>')


def related_pages_for_guide(lang, slug):
    """Reverse links: if a guide is tagged as being about specific line(s), ship(s) or destination(s)
    via for_lines / for_ships / for_dests in GUIDE_META, show cards linking to those pages. Renders
    nothing when a guide isn't tied to a specific entity."""
    from ships import get_ship, slugify as _sslug
    m = GUIDE_META.get(slug, {})
    en = lang == "en"
    cards = ""
    for lslug in (m.get("for_lines") or []):
        L = next((x for x in LINES if x["slug"] == lslug), None)
        if L:
            cards += (f'<a class="xr-card gd-rel" href="/{lang}/lines/{lslug}/"><div class="xr-top">'
                      f'<span class="xr-emoji">{L["emo"]}</span><div class="xr-h"><h3>{L["name"]}</h3></div></div>'
                      f'<div class="xr-b"><p class="xr-desc">{L["tag"][lang]}</p></div></a>')
    for pair in (m.get("for_ships") or []):
        lslug, ss = (pair.split("/", 1) + [""])[:2] if isinstance(pair, str) else pair
        sh = get_ship(lslug, ss)
        if sh:
            L = next((x for x in LINES if x["slug"] == lslug), None)
            emo = L["emo"] if L else "🚢"
            cards += (f'<a class="xr-card gd-rel" href="/{lang}/lines/{lslug}/ships/{_sslug(sh["name"])}/">'
                      f'<div class="xr-top"><span class="xr-emoji">{emo}</span>'
                      f'<div class="xr-h"><h3>{sh["name"]}</h3></div></div>'
                      f'<div class="xr-b"><p class="xr-desc">{("Ship guide" if en else "Guía del barco")}</p></div></a>')
    for dslug in (m.get("for_dests") or []):
        d = next((x for x in DESTINATIONS if x["slug"] == dslug), None)
        if d:
            cards += (f'<a class="xr-card gd-rel" href="/{lang}/destinations/{dslug}/"><div class="xr-top">'
                      f'<span class="xr-emoji">{d["emo"]}</span><div class="xr-h"><h3>{d["name"][lang]}</h3></div></div>'
                      f'<div class="xr-b"><p class="xr-desc">{("Destination guide" if en else "Guía del destino")}</p></div></a>')
    if not cards:
        return ""
    h = "Related on CruiseLine Advisors" if en else "Relacionado en CruiseLine Advisors"
    return (f'<section class="section"><div class="wrap"><h2 class="rsec-h">{h}</h2>'
            f'<div class="xr-grid">{cards}</div></div></section>')


def guides_hub_grouped(lang):
    """The Guides hub, grouped by category."""
    out = ""
    for key, title in GUIDE_CATS:
        slugs = [g["slug"] for g in GUIDES if GUIDE_META.get(g["slug"], {}).get("cat") == key]
        if not slugs:
            continue
        cards = "".join(guide_card(lang, s) for s in slugs)
        out += (f'<section class="section"><div class="wrap">'
                f'<h2 class="gcat-h">{title[lang]}</h2><div class="gcard-grid">{cards}</div></div></section>')
    return out


def related_guides(lang, ctx, slug=None, heading=None, limit=None):
    """A 'Helpful guides' section for a page. Includes every guide tagged for this context, and any
    guide targeted at this specific line/ship/destination slug (those come first). limit=None shows
    all relevant guides so each page connects to its full, relevant set."""
    forkey = _CTX_FORKEY.get(ctx)
    specific, general = [], []
    for g in GUIDES:
        m = GUIDE_META.get(g["slug"], {})
        if slug and forkey and slug in (m.get(forkey) or []):
            specific.append(g["slug"])
        elif ctx in (m.get("ctx") or []):
            general.append(g["slug"])
    ordered, seen = [], set()
    for s in specific + general:
        if s not in seen:
            seen.add(s)
            ordered.append(s)
    if limit:
        ordered = ordered[:limit]
    if not ordered:
        return ""
    cards = "".join(guide_card(lang, s) for s in ordered)
    h = heading or ("Helpful guides" if lang == "en" else "Guías útiles")
    sub = ("Free, factual reading to help you decide, then one call books it." if lang == "en"
           else "Lectura gratuita y con datos para ayudarte a decidir, luego una llamada reserva.")
    return (f'<section class="section cream"><div class="wrap">'
            f'<div class="sec-head"><h2 class="rsec-h">{h}</h2><p class="rsec-sub">{sub}</p></div>'
            f'<div class="gcard-grid">{cards}</div></div></section>')


# Original planning content (general cruise knowledge; compliant, no invented specifics).
GUIDE_BODY = {
    "first-time-cruisers": {
        "en": ["Your fare covers your cabin, most dining, entertainment and getting from port to port. Almost "
               "everything else, drinks, wifi, specialty restaurants, shore excursions, the spa, is extra. Knowing "
               "that split up front is the single biggest thing that keeps a first cruise on budget.",
               "Gratuities are added to your onboard account automatically, per guest, per day. You can prepay them. "
               "Documents matter too: on most closed-loop sailings a birth certificate plus ID can work, but a passport "
               "is safer and sometimes required, get this wrong and you don't board.",
               "The rest is easier than it looks. An advisor walks you through cabin choice, dining, and what to book "
               "before you sail versus onboard, in one call."],
        "es": ["Tu tarifa cubre el camarote, la mayoría de las comidas, el entretenimiento y el transporte entre "
               "puertos. Casi todo lo demás, bebidas, wifi, restaurantes especiales, excursiones, spa, es adicional. "
               "Saber esa diferencia por adelantado es lo que más ayuda a mantener el presupuesto.",
               "Las propinas se añaden a tu cuenta automáticamente, por huésped y por día. Puedes pagarlas por "
               "adelantado. Los documentos también importan: en muchos cruceros de ida y vuelta un acta de nacimiento "
               "con identificación puede servir, pero un pasaporte es más seguro y a veces obligatorio.",
               "El resto es más fácil de lo que parece. Un asesor te guía por la elección de camarote, comidas y qué "
               "reservar antes de zarpar, en una llamada."]},
}
_GUIDE_FALLBACK = {
    "en": ["This guide is being written. In the meantime, the fastest way to get the answer for your specific trip "
           "is a quick call, free, no obligation, and we never take payment for travel."],
    "es": ["Esta guía se está escribiendo. Mientras tanto, la forma más rápida de obtener la respuesta para tu viaje "
           "es una llamada rápida, gratis, sin compromiso, y nunca cobramos por el viaje."]}


def p_guides_hub(lang):
    kick = "Guides" if lang == "en" else "Guías"
    h1 = "Practical cruise planning guides" if lang == "en" else "Guías prácticas para planear tu crucero"
    sub = ("Cabins, budgets, families, accessibility and timing, the real questions, answered plainly." if lang == "en"
           else "Camarotes, presupuestos, familias, accesibilidad y temporada, las preguntas reales, con claridad.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + guides_hub_grouped(lang)
            + cta_band(lang, "Still have a question about your trip?" if lang == "en" else "¿Aún tienes una pregunta?",
                       "Call a specialist, they'll answer it in minutes, free." if lang == "en"
                       else "Llama a un especialista, te responde en minutos, gratis."))


def p_guide(lang, slug):
    from guidepage import has_rich_guide, render_rich_guide, RICH_GUIDES
    import guides_content  # noqa: F401, side-effect import registers the rich guides
    g = _G[slug]
    kick = "Guide" if lang == "en" else "Guía"
    if has_rich_guide(slug):
        from guidepage import guide_hero_img
        rg = RICH_GUIDES[slug]
        title, dek = rg["title"][lang], rg["dek"][lang]
        crumb = _crumb(lang, f'<a href="/{lang}/guides.html">{"Guides" if lang=="en" else "Guías"}</a>', title)
        himg = guide_hero_img(slug, rg.get("hero"))
        hero = _guide_photo_hero(lang, kick, title, dek, crumb, himg) if himg else phero(lang, kick, title, dek, crumb)
        tool = ""  # keep the interactive explainers embedded on these two rich guides
        if slug == "choosing-a-cabin":
            tool = cabin_guide(lang)
        elif slug == "when-to-cruise":
            tool = when_to_go(lang)
        return (hero
                + render_rich_guide(lang, slug)
                + tool
                + related_pages_for_guide(lang, slug)
                + cta_band(lang, "Ready to price a real sailing?" if lang == "en" else "¿Listo para cotizar un crucero real?",
                           "Call a specialist, they'll give you the all-in number for your dates." if lang == "en"
                           else "Llama a un especialista, te da la cifra completa para tus fechas."))
    crumb = _crumb(lang, f'<a href="/{lang}/guides.html">{"Guides" if lang=="en" else "Guías"}</a>', g["t"][lang])
    paras = GUIDE_BODY.get(slug, {}).get(lang) or _GUIDE_FALLBACK[lang]
    body = "".join(f"<p>{p}</p>" for p in paras)
    extra = ""
    if slug == "choosing-a-cabin":
        extra = cabin_guide(lang)
    elif slug == "when-to-cruise":
        extra = when_to_go(lang)
    return (phero(lang, kick, g["t"][lang], g["d"][lang], crumb)
            + f'<section class="section"><div class="wrap blk">{body}</div></section>'
            + extra
            + cta_band(lang, "Have a question about your trip?" if lang == "en" else "¿Tienes una pregunta sobre tu viaje?",
                       "Call a specialist, they'll answer it in minutes." if lang == "en"
                       else "Llama a un especialista, te responde en minutos."))


# ─────────────────────────── updates ───────────────────────────
def p_updates(lang):
    kick = "Updates" if lang == "en" else "Novedades"
    h1 = "Cruise policy & industry updates" if lang == "en" else "Novedades de políticas e industria"
    sub = ("Dated, sourced changes to cruise-line policies and requirements. We only post what we can verify." if lang == "en"
           else "Cambios fechados y con fuente en políticas y requisitos de cruceros. Solo publicamos lo que podemos verificar.")
    intro = ("Dated, sourced changes to cruise-line policies and requirements, we only post what we can verify. "
             "Each update is also shown on the affected line's page." if lang == "en" else
             "Cambios fechados y con fuente en políticas y requisitos, solo publicamos lo que podemos verificar. "
             "Cada novedad también aparece en la página de la línea afectada.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><p class="intro">{intro}</p>'
              f'<div style="margin-top:18px">{update_cards(lang, all_updates())}</div></div></section>'
            + cta_band(lang, "Need the latest on a policy?" if lang == "en" else "¿Necesitas lo último de una política?",
                       "Call and we'll confirm the current rule from the source." if lang == "en"
                       else "Llama y confirmamos la regla actual desde la fuente."))


def p_update_detail(lang, slug):
    u = get_update(slug)
    kick = "Update" if lang == "en" else "Novedad"
    updates_l = "Updates" if lang == "en" else "Novedades"
    crumb = _crumb(lang, f'<a href="/{lang}/updates/">{updates_l}</a>', u["title"][lang])
    try:
        date = datetime.date.fromisoformat(u["date"]).strftime("%B %d, %Y").replace(" 0", " ")
    except Exception:
        date = u["date"]
    tags = ""
    if u.get("lines"):
        tags = '<div class="upd-tags" style="margin-bottom:1rem">' + "".join(
            f'<a class="upd-tag" href="/{lang}/lines/{s}/">{_L[s]["emo"]} {_L[s]["name"]}</a>'
            for s in u["lines"] if s in _L) + '</div>'
    body = (u.get("detail") or u["body"])[lang]
    return (phero(lang, kick, u["title"][lang], date, crumb)
            + f'<section class="section"><div class="wrap blk">{tags}<p class="intro">{body}</p></div></section>'
            + cta_band(lang, "Questions about this?" if lang == "en" else "¿Preguntas sobre esto?",
                       "Call and we'll confirm what it means for your exact sailing." if lang == "en"
                       else "Llama y confirmamos qué significa para tu crucero exacto."))
