# -*- coding: utf-8 -*-
"""Content page builders (everything except the homepage and legal). Each returns the inner
<main> HTML for a language; base.page() wraps head/header/footer/SEO. Original, compliant copy
only — no prices, real hours, per-line disclaimers, and unverified facts shown as visible gaps."""
import datetime
from config import PHONE_HREF, PHONE_DISPLAY, HOURS, SINCE_YEAR, BRAND
from data import LINES, DESTINATIONS
from facts import FACTS, LINE_FACTS, latest_verified
from badges import verified_stamp, verified_seal
from compare import compare_tool
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


def phero(lang, kicker, h1, sub, crumb):
    return f"""<section class="section navy phero"><div class="wrap">
  <p class="crumbs">{crumb}</p>
  <span class="eyebrow" style="color:#7FD4D0">{kicker}</span>
  <h1>{h1}</h1><p class="phero-sub">{sub}</p>
  <a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('phero')"><span class="ic">☎</span>{'Call now · ' if lang=='en' else 'Llama ahora · '}{PHONE_DISPLAY}</a>
</div></section>"""


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
def p_lines_hub(lang):
    from page_home import _pcard, ACCENTS
    cards = "".join(
        _pcard(f"/{lang}/lines/{L['slug']}.html", L['emo'], L['name'], L['cat'][lang], L['tag'][lang],
               ("Read the guide" if lang == "en" else "Leer la guía"), i)
        for i, L in enumerate(LINES))
    kick = "Cruise lines" if lang == "en" else "Líneas de crucero"
    h1 = "In-depth guides to every major line" if lang == "en" else "Guías detalladas de cada línea principal"
    sub = ("Honest, source-checked guides — ships class by class, what the fare covers, cabins, families, "
           "accessibility and timing. Then one call to a specialist who books it." if lang == "en"
           else "Guías honestas y verificadas — barcos clase por clase, qué cubre la tarifa, camarotes, familias, "
                "accesibilidad y temporada. Luego una llamada a un especialista que lo reserva.")
    note = ("These eight lines are our first in-depth guides. We cover 36 lines boardable from the Americas — "
            "call for any line not yet listed." if lang == "en"
            else "Estas ocho líneas son nuestras primeras guías. Cubrimos 36 líneas desde las Américas — "
                 "llama por cualquiera que aún no esté listada.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><div class="linegrid">{cards}</div>'
              f'<p class="note-line">{note}</p></div></section>'
            + directory_section(lang)
            + cta_band(lang, "Not sure which line fits?" if lang == "en" else "¿No sabes qué línea encaja?",
                       "Tell a specialist what you want — they'll match you to the right ship and sailing." if lang == "en"
                       else "Dile a un especialista qué quieres — te emparejará con el barco y la salida correctos."))


def p_line(lang, slug):
    L = _L[slug]
    kick = L["cat"][lang]
    crumb = _crumb(lang, f'<a href="/{lang}/cruise-lines.html">{"Cruise lines" if lang=="en" else "Líneas"}</a>', L["name"])
    if lang == "en":
        intro = (f"{L['name']} is best described as <b>{L['cat']['en'].lower()}</b>. {L['tag']['en']} "
                 f"Below is an independent, source-checked look at what actually matters before you book — "
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
                 f"A continuación, una mirada independiente y verificada a lo que realmente importa antes de reservar — "
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
    cmp_sub = (f"Put {name} head-to-head with another line on the facts that cost money — then let an advisor apply them to your sailing."
               if lang == "en" else
               f"Compara {name} con otra línea en los datos que cuestan dinero — luego deja que un asesor los aplique a tu crucero.")
    upd_kick = "Updates" if lang == "en" else "Novedades"
    upd_h2 = f"Latest {name} updates" if lang == "en" else f"Últimas novedades de {name}"
    rich = rich_sections(lang, slug)  # sets sections_present(slug) as a side effect
    faq = faq_section(lang, slug)
    toc_keys = sections_present(slug) + ["facts", "updates", "compare"] + (["faq"] if faq else [])
    return (phero(lang, kick, L["name"], L["tag"][lang], crumb)
            + f'<section class="section"><div class="wrap blk"><p class="intro">{intro}</p></div></section>'
            + line_toc(lang, toc_keys)
            + rich
            + f'<section id="s-facts" class="section foam stamped"><div class="wrap">{verified_seal(lang, latest_verified(slug))}'
              f'<div class="sec-head"><span class="eyebrow">{kick}</span>'
              f'<h2>{facts_h}</h2><p>{facts_sub}</p></div>{facts_table(lang, slug)}</div></section>'
            + f'<section id="s-updates" class="section"><div class="wrap"><div class="sec-head"><span class="eyebrow">{upd_kick}</span>'
              f'<h2>{upd_h2}</h2></div>{update_cards(lang, updates_for(slug), show_line_tags=False)}</div></section>'
            + f'<section id="s-compare" class="section foam"><div class="wrap"><div class="sec-head"><span class="eyebrow">{cmp_kick}</span>'
              f'<h2>{cmp_h2}</h2><p>{cmp_sub}</p></div>{compare_tool(lang, default_a=slug)}</div></section>'
            + faq
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

    # verified specs — core four always shown (gap if missing); crew/length only when present
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
                 "constantly — one call to a specialist confirms exactly what's open for your dates and the best "
                 "rate our partners can offer.")
        specs_h = "The basics, verified"
        note = ("Every figure here traces to a published source and is re-checked on our normal schedule. Anything "
                "we haven't confirmed shows as a gap rather than a guess.")
        sisters_h = f"Other {cls} ships" if cls else f"More {L['name']} ships"
        nudge_txt = (f"Want {name} for your dates? A specialist checks live availability and holds the best cabin "
                     "for you — call now.")
        cta_t, cta_s = f"Sail on {name}?", "Free, no obligation, and we never take payment for travel."
        disc = (f"Independent referral service — not affiliated with, sponsored by, endorsed by or an agent of "
                f"{L['name']}. {L['name']}, {name} and related names and logos are trademarks of their owner, used "
                f"here descriptively only.")
    else:
        intro = (f"{name} forma parte de la flota de {L['name']}"
                 + (f", de la clase {cls}" if cls else "") + ". "
                 "Abajo están los datos verificados; las salidas, itinerarios, camarotes y la tarifa actual cambian "
                 "constantemente — una llamada a un especialista confirma qué hay disponible para tus fechas y la "
                 "mejor tarifa que nuestros socios pueden ofrecer.")
        specs_h = "Los datos, verificados"
        note = ("Cada cifra proviene de una fuente publicada y se revisa en nuestro calendario habitual. Lo que no "
                "hemos confirmado se muestra como un vacío, no como una suposición.")
        sisters_h = f"Otros barcos clase {cls}" if cls else f"Más barcos de {L['name']}"
        nudge_txt = (f"¿Quieres {name} para tus fechas? Un especialista revisa la disponibilidad en vivo y te reserva "
                     "el mejor camarote — llama ahora.")
        cta_t, cta_s = f"¿Navegar en {name}?", "Gratis, sin compromiso, y nunca cobramos por el viaje."
        disc = (f"Servicio de referencia independiente — no afiliado, patrocinado, respaldado ni agente de "
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
        sisters_block = (f'<section class="section"><div class="wrap"><h2 class="rsec-h">{sisters_h}</h2>'
                         f'<div class="ship-grid">{cards}</div></div></section>')

    back = (f'<a class="ship-back" href="/{lang}/lines/{line_slug}/">'
            f'← {"All " + L["name"] + " ships" if lang=="en" else "Todos los barcos de " + L["name"]}</a>')

    # the ship-compare tool now lives in the Compare-hero band at the top of the page.
    return (phero(lang, kick, name, sub, crumb)
            + compare_hero(lang, default_a=f"{line_slug}::{sslug}")
            + f'<section class="section"><div class="wrap blk"><p class="intro">{intro}</p></div></section>'
            + ship_banner(lang)
            + f'<section class="section cream{" stamped" if _has_specs else ""}"><div class="wrap">'
              f'{verified_seal(lang, ship_source(line_slug)[1]) if _has_specs else ""}'
              f'<h2 class="rsec-h">{specs_h}</h2>'
              f'<div class="glance-grid">{specs}</div>{feats_block}'
              f'<p class="note-line" style="margin-top:20px">{note}</p>'
              f'{_ship_nudge(lang, nudge_txt)}</div></section>'
            + experience_sections(lang, line_slug, s)
            + sisters_block
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
    kick = "Compare" if lang == "en" else "Comparar"
    h1 = "Compare cruise lines on what matters" if lang == "en" else "Compara líneas de crucero en lo que importa"
    sub = ("Pick any two lines and see the money-and-complexity facts side by side — then let an advisor apply "
           "them to your exact sailing." if lang == "en"
           else "Elige dos líneas y ve los datos de dinero y complejidad lado a lado — luego deja que un asesor "
                "los aplique a tu crucero exacto.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap">{compare_tool(lang)}</div></section>')


def p_facts(lang):
    kick = "Cruise facts" if lang == "en" else "Datos de cruceros"
    h1 = "The cruise facts that cost you money" if lang == "en" else "Los datos de crucero que te cuestan dinero"
    sub = ("The details cruise sites bury — gratuities, what's included, cancellation, documents. Here's what each "
           "one means and what to ask." if lang == "en"
           else "Los detalles que los sitios esconden — propinas, qué se incluye, cancelación, documentos. Esto es "
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
    from page_home import _pcard
    cards = "".join(
        _pcard(f"/{lang}/destinations/{d['slug']}.html", d['emo'], d['name'][lang],
               f"{'Best' if lang=='en' else 'Mejor'}: {d['best'][lang]}", "",
               ("Explore" if lang == "en" else "Explorar"), i)
        for i, d in enumerate(DESTINATIONS))
    kick = "Destinations" if lang == "en" else "Destinos"
    h1 = "Where do you want to sail?" if lang == "en" else "¿A dónde quieres navegar?"
    sub = ("Every region runs on a season. Pick the right month and the whole trip gets better." if lang == "en"
           else "Cada región tiene su temporada. Elige el mes correcto y todo el viaje mejora.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><div class="linegrid">{cards}</div></div></section>'
            + when_to_go(lang)
            + cta_band(lang, "Not sure when to go?" if lang == "en" else "¿No sabes cuándo ir?",
                       "An advisor matches your dates to the region that's actually in season." if lang == "en"
                       else "Un asesor ajusta tus fechas a la región que está en temporada."))


def p_region(lang, slug):
    d = _D[slug]
    s = SEASONS.get(slug, {})
    peak = s.get("peak", {}).get(lang, "") if isinstance(s.get("peak"), dict) else ""
    kick = "Destination" if lang == "en" else "Destino"
    crumb = _crumb(lang, f'<a href="/{lang}/destinations.html">{"Destinations" if lang=="en" else "Destinos"}</a>', d["name"][lang])
    if lang == "en":
        body = (f"<b>Best time to sail:</b> {d['best']['en']}" + (f" (peak {peak})" if peak else "") + ". "
                "Seasons decide far more than the ship does — the right month means better weather, calmer seas and "
                "the itineraries you actually want. An advisor confirms which ships sail your dates and matches the "
                "sailing to your party.")
        warn = ("This is an Atlantic hurricane-season region (1 June–30 November). Sailings still operate and reroute "
                "when needed, but travel insurance matters more in these months." if s.get("warn") else "")
    else:
        body = (f"<b>Mejor época para navegar:</b> {d['best']['es']}" + (f" (pico {peak})" if peak else "") + ". "
                "La temporada decide mucho más que el barco — el mes correcto significa mejor clima, mares más "
                "tranquilos y los itinerarios que quieres. Un asesor confirma qué barcos navegan en tus fechas.")
        warn = ("Es una región de temporada de huracanes del Atlántico (1 jun–30 nov). Los cruceros operan y se "
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
     "d": {"en": "What nobody tells you before your first sailing — from boarding to disembark.",
           "es": "Lo que nadie te dice antes de tu primer crucero — del embarque al desembarque."}},
    {"slug": "choosing-a-cabin", "emo": "🛏️",
     "t": {"en": "Choosing a cabin", "es": "Elegir camarote"},
     "d": {"en": "Interior to suite — what you get, what to watch for, and the cabins to avoid.",
           "es": "De interior a suite — qué obtienes, qué vigilar y los camarotes a evitar."}},
    {"slug": "whats-included", "emo": "🧾",
     "t": {"en": "What's included", "es": "Qué se incluye"},
     "d": {"en": "The gap between the fare and your final bill — explained plainly.",
           "es": "La diferencia entre la tarifa y tu factura final — explicada con claridad."}},
    {"slug": "when-to-cruise", "emo": "🗓️",
     "t": {"en": "When to cruise", "es": "Cuándo hacer un crucero"},
     "d": {"en": "Season by season, region by region — timing beats everything.",
           "es": "Temporada por temporada, región por región — el momento lo es todo."}},
    {"slug": "groups-and-families", "emo": "👨‍👩‍👧",
     "t": {"en": "Groups & families", "es": "Grupos y familias"},
     "d": {"en": "Linked cabins, dining, kids clubs and split payments — the phone-work parts.",
           "es": "Camarotes conectados, comidas, clubes infantiles y pagos divididos."}},
    {"slug": "accessibility", "emo": "♿",
     "t": {"en": "Accessibility", "es": "Accesibilidad"},
     "d": {"en": "Accessible cabins, tendering, and what to confirm before you book.",
           "es": "Camarotes accesibles, transbordos y qué confirmar antes de reservar."}},
]
_G = {g["slug"]: g for g in GUIDES}

# Original planning content (general cruise knowledge; compliant — no invented specifics).
GUIDE_BODY = {
    "first-time-cruisers": {
        "en": ["Your fare covers your cabin, most dining, entertainment and getting from port to port. Almost "
               "everything else — drinks, wifi, specialty restaurants, shore excursions, the spa — is extra. Knowing "
               "that split up front is the single biggest thing that keeps a first cruise on budget.",
               "Gratuities are added to your onboard account automatically, per guest, per day. You can prepay them. "
               "Documents matter too: on most closed-loop sailings a birth certificate plus ID can work, but a passport "
               "is safer and sometimes required — get this wrong and you don't board.",
               "The rest is easier than it looks. An advisor walks you through cabin choice, dining, and what to book "
               "before you sail versus onboard — in one call."],
        "es": ["Tu tarifa cubre el camarote, la mayoría de las comidas, el entretenimiento y el transporte entre "
               "puertos. Casi todo lo demás — bebidas, wifi, restaurantes especiales, excursiones, spa — es adicional. "
               "Saber esa diferencia por adelantado es lo que más ayuda a mantener el presupuesto.",
               "Las propinas se añaden a tu cuenta automáticamente, por huésped y por día. Puedes pagarlas por "
               "adelantado. Los documentos también importan: en muchos cruceros de ida y vuelta un acta de nacimiento "
               "con identificación puede servir, pero un pasaporte es más seguro y a veces obligatorio.",
               "El resto es más fácil de lo que parece. Un asesor te guía por la elección de camarote, comidas y qué "
               "reservar antes de zarpar — en una llamada."]},
}
_GUIDE_FALLBACK = {
    "en": ["This guide is being written. In the meantime, the fastest way to get the answer for your specific trip "
           "is a quick call — free, no obligation, and we never take payment for travel."],
    "es": ["Esta guía se está escribiendo. Mientras tanto, la forma más rápida de obtener la respuesta para tu viaje "
           "es una llamada rápida — gratis, sin compromiso, y nunca cobramos por el viaje."]}


def p_guides_hub(lang):
    from page_home import _pcard
    cards = "".join(
        _pcard(f"/{lang}/guides/{g['slug']}.html", g['emo'], g['t'][lang], "", g['d'][lang],
               ("Read" if lang == "en" else "Leer"), i) for i, g in enumerate(GUIDES))
    kick = "Guides" if lang == "en" else "Guías"
    h1 = "Practical cruise planning guides" if lang == "en" else "Guías prácticas para planear tu crucero"
    sub = ("Cabins, budgets, families, accessibility and timing — the real questions, answered plainly." if lang == "en"
           else "Camarotes, presupuestos, familias, accesibilidad y temporada — las preguntas reales, con claridad.")
    return (phero(lang, kick, h1, sub, _crumb(lang, kick))
            + f'<section class="section"><div class="wrap"><div class="linegrid">{cards}</div></div></section>')


def p_guide(lang, slug):
    g = _G[slug]
    kick = "Guide" if lang == "en" else "Guía"
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
                       "Call a specialist — they'll answer it in minutes." if lang == "en"
                       else "Llama a un especialista — te responde en minutos."))


# ─────────────────────────── updates ───────────────────────────
def p_updates(lang):
    kick = "Updates" if lang == "en" else "Novedades"
    h1 = "Cruise policy & industry updates" if lang == "en" else "Novedades de políticas e industria"
    sub = ("Dated, sourced changes to cruise-line policies and requirements. We only post what we can verify." if lang == "en"
           else "Cambios fechados y con fuente en políticas y requisitos de cruceros. Solo publicamos lo que podemos verificar.")
    intro = ("Dated, sourced changes to cruise-line policies and requirements — we only post what we can verify. "
             "Each update is also shown on the affected line's page." if lang == "en" else
             "Cambios fechados y con fuente en políticas y requisitos — solo publicamos lo que podemos verificar. "
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
