# -*- coding: utf-8 -*-
"""Rich destination guides.

Each US/Canada region page is a decision guide built from data we already hold: the home ports you
sail from (deployment.json + self-hosted port photos), the ships that actually sail the region
(derived from each ship's own itinerary — the same source the finder uses), the lines strong there,
best time to sail, marquee ports of call, and travel-document practicalities. No prices anywhere;
descriptive copy is original. Regions not in deployment.json (e.g. Mediterranean) get a lighter guide
via the caller's fallback.
"""
import json
import os

from config import PHONE_HREF, PHONE_DISPLAY
from data import LINES
from metasearch import ship_regions
from ships import all_ships, slugify

_DEP = {r["id"]: r for r in json.load(
    open(os.path.join(os.path.dirname(__file__), "data", "deployment.json"), encoding="utf-8"))["regions"]}
_LINE = {L["slug"]: L for L in LINES}
_PORTS_DIR = os.path.join(os.path.dirname(__file__), "assets", "ports")
_MONTHS = {"en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
           "es": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]}


def has_region_guide(slug):
    return slug in _DEP


def _port_photo(city):
    """Resolve 'Fort Lauderdale, FL' / 'Port Canaveral (Orlando), FL' to an existing port photo slug."""
    base = city.split(",")[0].strip()
    cands = []
    main = base.split("(")[0].strip()
    cands.append(main.lower().replace(" ", "-").replace(".", ""))
    if "(" in base:  # try the metro name in parentheses (e.g. Cape Liberty (New York) -> new-york)
        inside = base[base.find("(") + 1:base.find(")")].strip()
        cands.append(inside.lower().replace(" ", "-").replace(".", ""))
    for c in cands:
        if os.path.exists(os.path.join(_PORTS_DIR, c + ".jpg")):
            return c + ".jpg"
    return None


def _ships_by_line(slug):
    """Ships whose own itinerary includes this region, grouped by line (preserving line order)."""
    out = {}
    for line_slug, s in all_ships():
        if slug in ship_regions(line_slug, s.get("exp") or {}):
            out.setdefault(line_slug, []).append(s)
    return out


# ── per-region editorial copy (facts only; original wording) ─────────────────────────────────────
# expect: 1–2 sentence "what to expect". calls: marquee ports of call (well-known geographic stops).
DEST_COPY = {
    "caribbean": {
        "expect": {"en": "Warm water, short flights to the port, and a mix of beach days and island stops. Eastern routes lean to lush, hilly islands; western routes add Mexico and Central America; southern routes reach the quieter, further-out islands.",
                   "es": "Agua cálida, vuelos cortos al puerto y una mezcla de días de playa y paradas en islas. Las rutas del este tienden a islas verdes; las del oeste añaden México y Centroamérica; las del sur llegan a islas más lejanas y tranquilas."},
        "calls": ["Cozumel", "Grand Cayman", "Nassau", "Perfect Day at CocoCay", "St. Thomas", "St. Maarten", "San Juan", "Roatán"],
    },
    "bahamas": {
        "expect": {"en": "The quickest warm-weather cruise from Florida — often 3–5 nights, heavy on private islands and easy first-timer itineraries.",
                   "es": "El crucero cálido más rápido desde Florida — a menudo de 3–5 noches, con muchas islas privadas e itinerarios fáciles para primerizos."},
        "calls": ["Nassau", "Freeport", "Perfect Day at CocoCay", "Ocean Cay", "Great Stirrup Cay", "Half Moon Cay"],
    },
    "alaska": {
        "expect": {"en": "Glaciers, whales and green-mountain fjords on a tight May–September window. Choose a round-trip (usually from Seattle or Vancouver) or a one-way Gulf cruise that pairs with a land tour.",
                   "es": "Glaciares, ballenas y fiordos de montañas verdes en una ventana corta de mayo a septiembre. Elige ida y vuelta (normalmente desde Seattle o Vancouver) o un crucero de una vía por el Golfo que se combina con un tour terrestre."},
        "calls": ["Juneau", "Ketchikan", "Skagway", "Glacier Bay", "Icy Strait Point", "Sitka", "Hubbard Glacier"],
    },
    "bermuda": {
        "expect": {"en": "Pink-sand beaches and turquoise water a short hop off the US East Coast. Ships usually dock for multiple days at the Royal Naval Dockyard, so it feels part-cruise, part-resort.",
                   "es": "Playas de arena rosada y agua turquesa a poca distancia de la costa este de EE.UU. Los barcos suelen atracar varios días en el Royal Naval Dockyard, así que es parte crucero, parte resort."},
        "calls": ["King's Wharf (Royal Naval Dockyard)", "Hamilton", "St. George's"],
    },
    "mexican-riviera": {
        "expect": {"en": "Pacific-coast Mexico from Southern California — beaches, tacos and desert-meets-sea scenery, usually on round-trips from Los Angeles or San Diego.",
                   "es": "El Pacífico mexicano desde el sur de California — playas, tacos y paisaje de desierto y mar, normalmente en cruceros de ida y vuelta desde Los Ángeles o San Diego."},
        "calls": ["Cabo San Lucas", "Puerto Vallarta", "Mazatlán", "Ensenada"],
    },
    "canada-new-england": {
        "expect": {"en": "Lighthouses, lobster and fall colour from New York or Boston up to the Canadian Maritimes and the St. Lawrence. September–October is the classic leaf-peeping window.",
                   "es": "Faros, langosta y colores de otoño desde Nueva York o Boston hasta las Marítimas canadienses y el San Lorenzo. Septiembre–octubre es la ventana clásica del follaje otoñal."},
        "calls": ["Halifax", "Saint John", "Bar Harbor", "Portland", "Quebec City", "Sydney"],
    },
    "hawaii": {
        "expect": {"en": "Multiple islands on one trip, with more sea days than a Caribbean cruise. Round-trips from the mainland are long; inter-island sailings pack four islands into a week.",
                   "es": "Varias islas en un viaje, con más días de mar que un crucero por el Caribe. Los cruceros de ida y vuelta desde el continente son largos; los inter-islas reúnen cuatro islas en una semana."},
        "calls": ["Honolulu (Oahu)", "Kahului (Maui)", "Kona", "Hilo", "Nawiliwili (Kauai)", "Ensenada"],
    },
    "panama-canal": {
        "expect": {"en": "A bucket-list transit through the locks, on either a full ocean-to-ocean crossing or a partial round-trip that enters the canal and turns back. Best in the drier October–April window.",
                   "es": "Un tránsito de lista de deseos por las esclusas, en un cruce completo de océano a océano o en un ida y vuelta parcial que entra al canal y regresa. Mejor en la ventana más seca de octubre a abril."},
        "calls": ["Panama Canal / Gatún Lake", "Cartagena", "Colón", "Puntarenas", "Cabo San Lucas", "Aruba"],
    },
    "pacific-coastal": {
        "expect": {"en": "Short repositioning sailings up and down the US West Coast in spring and fall, as ships move between Alaska and Mexico seasons. A relaxed, scenery-first, mostly sea-day trip.",
                   "es": "Cruceros cortos de reposicionamiento por la costa oeste de EE.UU. en primavera y otoño, cuando los barcos se mueven entre las temporadas de Alaska y México. Un viaje relajado, de paisaje y días de mar."},
        "calls": ["San Francisco", "San Diego", "Astoria", "Victoria, BC", "Santa Barbara", "Ensenada"],
    },
    "transatlantic": {
        "expect": {"en": "A classic ocean crossing between North America and Europe — lots of sea days, a slower pace, and a repositioning-season price of admission. Great if the voyage itself is the point.",
                   "es": "Un cruce oceánico clásico entre Norteamérica y Europa — muchos días de mar, ritmo pausado y en temporada de reposicionamiento. Ideal si el viaje en sí es lo importante."},
        "calls": ["Southampton", "Ponta Delgada (Azores)", "Bermuda", "New York", "Halifax"],
    },
}


def _card(emoji, title, meta, desc):
    body = f'<div class="xr-b"><p class="xr-desc">{desc}</p></div>' if desc else ""
    metah = f'<span class="xr-meta">{meta}</span>' if meta else ""
    return (f'<article class="xr-card"><div class="xr-top"><span class="xr-emoji">{emoji}</span>'
            f'<div class="xr-h"><h3>{title}</h3>{metah}</div></div>{body}</article>')


def _call(lang, txt, tag):
    c = "Call now" if lang == "en" else "Llama ahora"
    return (f'<div class="nudge"><p>{txt}</p>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'{tag}\')">'
            f'<span class="ic" aria-hidden="true">☎</span>{c} · {PHONE_DISPLAY}</a></div>')


def _sec(cls, title, emoji, inner):
    return (f'<section class="section {cls}"><div class="wrap">'
            f'<h2 class="rsec-h"><span class="xic" aria-hidden="true">{emoji}</span>{title}</h2>'
            f'{inner}</div></section>')


def region_guide(lang, slug, name):
    r = _DEP[slug]
    copy = DEST_COPY.get(slug, {})
    en = lang == "en"
    out = ""

    # quick facts bar
    ships_by_line = _ships_by_line(slug)
    n_ships = sum(len(v) for v in ships_by_line.values())
    facts = [
        (("Best time" if en else "Mejor época"), r["season"]),
        (("Sail from" if en else "Sales desde"), f'{len(r["ports"])} ' + ("US/Canada ports" if en else "puertos EE.UU./Canadá")),
        (("Ships that sail here" if en else "Barcos que navegan aquí"), str(n_ships)),
        (("Lines" if en else "Líneas"), str(len(r["lines"]))),
    ]
    fcells = "".join(f'<div class="glance-cell"><b>{k}</b><span>{v}</span></div>' for k, v in facts)
    out += f'<section class="section"><div class="wrap"><div class="glance-grid dest-facts">{fcells}</div></div></section>'

    # what to expect
    if copy.get("expect"):
        out += _sec("", ("What to expect" if en else "Qué esperar"), "🧭",
                    f'<p class="intro">{copy["expect"][lang]}</p>')

    # best time — month strip
    months = set(r.get("months") or [])
    strip = "".join(
        f'<span class="whn-m{" on" if (i + 1) in months else ""}">{_MONTHS[lang][i]}</span>'
        for i in range(12))
    warn = ""
    if slug in ("caribbean", "bahamas"):
        warn = ('<p class="whn-warn" style="margin-top:14px">⚠ ' +
                ("Atlantic hurricane season runs 1 Jun–30 Nov. Sailings still operate and reroute when needed — travel insurance matters more in these months."
                 if en else
                 "La temporada de huracanes del Atlántico va del 1 jun al 30 nov. Los cruceros operan y se redirigen cuando hace falta — el seguro de viaje importa más en estos meses.") + '</p>')
    out += _sec("cream", ("Best time to sail" if en else "Mejor época para navegar"), "🗓️",
                f'<p class="rsec-sub">{r["season"]}.</p><div class="whn-months dest-months">{strip}</div>{warn}')

    # where you sail from — port cards with photos
    pcards = ""
    for p in r["ports"]:
        img = _port_photo(p)
        city = p.split("(")[0].split(",")[0].strip()
        region_state = p.split(",")[-1].strip() if "," in p else ""
        media = (f'<img src="/ports/{img}" alt="{city}" loading="lazy" decoding="async">' if img else "")
        state_html = f'<small>{region_state}</small>' if region_state else ""
        pcards += (f'<article class="port-card">{media}'
                   f'<span class="port-nm">{city}{state_html}</span></article>')
    ports_note = ("These are the US and Canada home ports ships depart from for this region — drive or fly in the day before."
                  if en else
                  "Estos son los puertos base de EE.UU. y Canadá desde donde zarpan los barcos de esta región — llega en auto o avión el día antes.")
    out += _sec("", ("Where you sail from" if en else "Desde dónde zarpas"), "⚓",
                f'<div class="port-grid">{pcards}</div><p class="note-line" style="margin-top:16px">{ports_note}</p>')

    # typical ports of call
    if copy.get("calls"):
        chips = "".join(f'<span class="ft">{c}</span>' for c in copy["calls"])
        pnote = ("Exact stops vary by ship and sailing — a specialist matches the itinerary to what you want to see."
                 if en else
                 "Las paradas exactas varían por barco y salida — un especialista ajusta el itinerario a lo que quieres ver.")
        out += _sec("cream", ("Typical ports of call" if en else "Puertos de escala típicos"), "📍",
                    f'<div class="ship-feats dest-calls">{chips}</div><p class="note-line" style="margin-top:14px">{pnote}</p>')

    # ships that sail here — grouped by line
    if n_ships:
        blocks = ""
        for line_slug in r["lines"]:
            ships = ships_by_line.get(line_slug)
            if not ships:
                continue
            L = _LINE.get(line_slug, {"name": line_slug, "emo": "🚢"})
            cards = "".join(
                f'<a class="ship-card lk" href="/{lang}/lines/{line_slug}/ships/{slugify(s["name"])}/">'
                f'<h3>{s["name"]}</h3>'
                f'<p class="ship-ships">{(str(s["year"]) if s.get("year") else "&nbsp;")}</p>'
                f'<span class="ship-more">{"View ship" if en else "Ver barco"} →</span></a>'
                for s in ships)
            blocks += (f'<h3 class="fleet-class">{L["emo"]} {L["name"]} '
                       f'<span class="shipdir-n">{len(ships)}</span></h3>'
                       f'<div class="ship-grid">{cards}</div>')
        snote = ("Every ship above sails this region on its own published itinerary. Availability by date changes constantly — one call confirms what's open for you."
                 if en else
                 "Cada barco de arriba navega esta región según su propio itinerario publicado. La disponibilidad por fecha cambia constantemente — una llamada confirma qué hay para ti.")
        out += _sec("", ("Ships that sail here" if en else "Barcos que navegan aquí"), "🚢",
                    f'{blocks}<p class="note-line" style="margin-top:8px">{snote}</p>')

    # which line fits
    lcards = ""
    for line_slug in r["lines"]:
        L = _LINE.get(line_slug)
        if not L:
            continue
        lcards += _card(L["emo"], L["name"], L["cat"][lang], L["tag"][lang]
                        + f' <a class="dest-linelink" href="/{lang}/lines/{line_slug}/">'
                        + ("Guide →" if en else "Guía →") + "</a>")
    out += _sec("cream", ("Which line fits this trip" if en else "Qué línea encaja"), "🧭",
                f'<div class="xr-grid">{lcards}</div>')

    # documents & practicalities (general, compliant)
    docs = ("On most round-trips that start and end at the same US port (closed-loop), US citizens can sail on a "
            "birth certificate plus government photo ID — but a passport is strongly recommended and is required for "
            "any cruise that starts or ends abroad, and for flying home if you miss the ship. Confirm requirements for "
            "your exact itinerary and nationality before you book." if en else
            "En la mayoría de los cruceros de ida y vuelta que empiezan y terminan en el mismo puerto de EE.UU. "
            "(closed-loop), los ciudadanos estadounidenses pueden viajar con acta de nacimiento y una identificación "
            "con foto — pero se recomienda un pasaporte, y es obligatorio para cualquier crucero que empiece o termine "
            "en el extranjero. Confirma los requisitos de tu itinerario y nacionalidad antes de reservar.")
    out += _sec("", ("Documents & practicalities" if en else "Documentos y logística"), "🛂",
                f'<p class="rsec-sub">{docs}</p>'
                f'<p class="note-line" style="margin-top:12px"><a href="/{lang}/cruise-facts/">'
                + ("See all the cruise facts that cost you money →" if en else "Ve todos los datos que cuestan dinero →")
                + "</a></p>")

    # finder + call CTA
    finder = ("Ready to see real sailings? Use the finder to line up the ships for this region — then one call books the right one."
              if en else "¿Listo para ver salidas reales? Usa el buscador para alinear los barcos de esta región — luego una llamada reserva el correcto.")
    out += _sec("", ("Find your sailing" if en else "Encuentra tu salida"), "🔎",
                f'<p class="rsec-sub">{finder}</p>'
                f'<p style="margin-top:14px"><a class="btn btn-ghost" href="/{lang}/compare/">'
                + ("Open the cruise finder →" if en else "Abrir el buscador →") + "</a></p>"
                + _call(lang, (f"Prefer to just ask? Tell us your dates and party for {name} — we'll match the ship and the best rate our partners can offer."
                               if en else
                               f"¿Prefieres preguntar? Dinos tus fechas y con quién viajas para {name} — emparejamos el barco y la mejor tarifa."), "dest-cta"))
    return out


def region_faqs(lang, slug, name):
    """Data-driven FAQ (also emitted as FAQPage JSON-LD by the caller)."""
    if slug not in _DEP:
        return []
    r = _DEP[slug]
    en = lang == "en"
    n_lines = len(r["lines"])
    faqs = [
        (("When is the best time to cruise " + name + "?" if en else "¿Cuándo es la mejor época para navegar a " + name + "?"),
         (f"The season runs {r['season']}." if en else f"La temporada es {r['season']}.")),
        (("Which ports do " + name + " cruises leave from?" if en else "¿Desde qué puertos salen los cruceros a " + name + "?"),
         (("You can sail from " + ", ".join(r["ports"]) + ".") if en else ("Puedes zarpar desde " + ", ".join(r["ports"]) + "."))),
        (("Which cruise lines sail " + name + "?" if en else "¿Qué líneas navegan a " + name + "?"),
         ((f"{n_lines} lines we cover sail this region: " + ", ".join(_LINE[l]["name"] for l in r["lines"] if l in _LINE) + ".")
          if en else (f"{n_lines} líneas que cubrimos navegan esta región: " + ", ".join(_LINE[l]["name"] for l in r["lines"] if l in _LINE) + "."))),
    ]
    return faqs
