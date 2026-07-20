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
# expect: 1–2 sentence "what to expect". calls: marquee ports of call as {name, desc} — factual,
# well-known geographic stops described in our own words (NO prices).
def _c(name, en, es):
    return {"name": name, "desc": {"en": en, "es": es}}


DEST_COPY = {
    "caribbean": {
        "expect": {"en": "Warm water, short flights to the port, and a mix of beach days and island stops. Eastern routes lean to lush, hilly islands; western routes add Mexico and Central America; southern routes reach the quieter, further-out islands.",
                   "es": "Agua cálida, vuelos cortos al puerto y una mezcla de días de playa y paradas en islas. Las rutas del este tienden a islas verdes; las del oeste añaden México y Centroamérica; las del sur llegan a islas más lejanas y tranquilas."},
        "calls": [
            _c("Cozumel", "Mexico's dive-and-beach island off the Yucatán — a Western-Caribbean staple.", "La isla de buceo y playa de México frente a Yucatán — clásica del Caribe occidental."),
            _c("Grand Cayman", "Tender port known for Seven Mile Beach and Stingray City.", "Puerto de fondeo famoso por Seven Mile Beach y Stingray City."),
            _c("Nassau", "The Bahamian capital — forts, markets and Paradise Island next door.", "La capital de Bahamas — fuertes, mercados y Paradise Island al lado."),
            _c("Perfect Day at CocoCay", "Royal Caribbean's private Bahamian island with a waterpark and beaches.", "La isla privada de Royal Caribbean en Bahamas, con parque acuático y playas."),
            _c("St. Thomas", "US Virgin Islands port known for Magens Bay and duty-free shopping.", "Puerto de las Islas Vírgenes de EE.UU., famoso por Magens Bay y compras libres de impuestos."),
            _c("St. Maarten", "Half-Dutch, half-French island with beaches and lively Philipsburg.", "Isla mitad holandesa, mitad francesa, con playas y el animado Philipsburg."),
            _c("San Juan", "Old San Juan's blue-cobbled streets and Spanish forts, in Puerto Rico.", "Las calles empedradas y fuertes españoles del Viejo San Juan, en Puerto Rico."),
            _c("Roatán", "Honduran island on the Mesoamerican Reef — snorkelling and beaches.", "Isla hondureña en el Arrecife Mesoamericano — snorkel y playas."),
        ],
    },
    "bahamas": {
        "expect": {"en": "The quickest warm-weather cruise from Florida — often 3–5 nights, heavy on private islands and easy first-timer itineraries.",
                   "es": "El crucero cálido más rápido desde Florida — a menudo de 3–5 noches, con muchas islas privadas e itinerarios fáciles para primerizos."},
        "calls": [
            _c("Nassau", "The capital — forts, beaches and Paradise Island a bridge away.", "La capital — fuertes, playas y Paradise Island a un puente de distancia."),
            _c("Freeport", "Grand Bahama's port for beaches, markets and reef trips.", "El puerto de Gran Bahama para playas, mercados y excursiones al arrecife."),
            _c("Perfect Day at CocoCay", "Royal Caribbean's private-island waterpark and beaches.", "El parque acuático y las playas de la isla privada de Royal Caribbean."),
            _c("Ocean Cay", "MSC's private Bahamian marine-reserve island.", "La isla-reserva marina privada de MSC en Bahamas."),
            _c("Great Stirrup Cay", "Norwegian's private out-island beach day.", "El día de playa en la isla privada de Norwegian."),
            _c("Half Moon Cay", "Holland America and Carnival's private crescent-beach island.", "La isla privada de playa en media luna de Holland America y Carnival."),
        ],
    },
    "alaska": {
        "expect": {"en": "Glaciers, whales and green-mountain fjords on a tight May–September window. Choose a round-trip (usually from Seattle or Vancouver) or a one-way Gulf cruise that pairs with a land tour.",
                   "es": "Glaciares, ballenas y fiordos de montañas verdes en una ventana corta de mayo a septiembre. Elige ida y vuelta (normalmente desde Seattle o Vancouver) o un crucero de una vía por el Golfo que se combina con un tour terrestre."},
        "calls": [
            _c("Juneau", "The capital, reachable only by sea or air — Mendenhall Glacier and whale-watching.", "La capital, a la que solo se llega por mar o aire — el glaciar Mendenhall y avistamiento de ballenas."),
            _c("Ketchikan", "Totem poles, salmon runs and the Misty Fjords.", "Tótems, salmón y los Misty Fjords."),
            _c("Skagway", "Gold-Rush town and the historic White Pass railway.", "Pueblo de la fiebre del oro y el histórico ferrocarril del White Pass."),
            _c("Glacier Bay", "A national park of tidewater glaciers seen by scenic cruising (no dock).", "Un parque nacional de glaciares de marea que se ve navegando (sin muelle)."),
            _c("Icy Strait Point", "Native-owned port near Hoonah — whales and the world's longest zipline.", "Puerto de propiedad nativa cerca de Hoonah — ballenas y la tirolesa más larga del mundo."),
            _c("Sitka", "Russian-Alaskan history on the wilder outer coast.", "Historia ruso-alaskeña en la costa exterior más salvaje."),
            _c("Hubbard Glacier", "A huge, actively calving glacier visited by scenic cruising.", "Un glaciar enorme y activo que se visita navegando."),
        ],
    },
    "bermuda": {
        "expect": {"en": "Pink-sand beaches and turquoise water a short hop off the US East Coast. Ships usually dock for multiple days at the Royal Naval Dockyard, so it feels part-cruise, part-resort.",
                   "es": "Playas de arena rosada y agua turquesa a poca distancia de la costa este de EE.UU. Los barcos suelen atracar varios días en el Royal Naval Dockyard, así que es parte crucero, parte resort."},
        "calls": [
            _c("King's Wharf (Royal Naval Dockyard)", "The main cruise port — museum, beaches and ferries to town.", "El puerto principal — museo, playas y ferris al centro."),
            _c("Hamilton", "The capital, with shops along pastel Front Street.", "La capital, con tiendas en la colorida Front Street."),
            _c("St. George's", "A UNESCO-listed old town, Bermuda's original settlement.", "Un casco antiguo declarado por la UNESCO, el primer asentamiento de Bermudas."),
        ],
    },
    "mexican-riviera": {
        "expect": {"en": "Pacific-coast Mexico from Southern California — beaches, tacos and desert-meets-sea scenery, usually on round-trips from Los Angeles or San Diego.",
                   "es": "El Pacífico mexicano desde el sur de California — playas, tacos y paisaje de desierto y mar, normalmente en cruceros de ida y vuelta desde Los Ángeles o San Diego."},
        "calls": [
            _c("Cabo San Lucas", "Land's End, the famous arch and Baja beaches (a tender port).", "Land's End, el famoso arco y las playas de Baja (puerto de fondeo)."),
            _c("Puerto Vallarta", "Banderas Bay beaches and the Malecón boardwalk.", "Las playas de Bahía de Banderas y el Malecón."),
            _c("Mazatlán", "A historic centre, the Malecón and Pacific beaches.", "Un centro histórico, el Malecón y playas del Pacífico."),
            _c("Ensenada", "Baja wine country and La Bufadora blowhole, near San Diego.", "La región vinícola de Baja y el bufadero La Bufadora, cerca de San Diego."),
        ],
    },
    "canada-new-england": {
        "expect": {"en": "Lighthouses, lobster and fall colour from New York or Boston up to the Canadian Maritimes and the St. Lawrence. September–October is the classic leaf-peeping window.",
                   "es": "Faros, langosta y colores de otoño desde Nueva York o Boston hasta las Marítimas canadienses y el San Lorenzo. Septiembre–octubre es la ventana clásica del follaje otoñal."},
        "calls": [
            _c("Halifax", "Nova Scotia's harbour city — the Citadel, waterfront and Peggy's Cove nearby.", "La ciudad portuaria de Nueva Escocia — la Ciudadela, el paseo marítimo y Peggy's Cove cerca."),
            _c("Saint John", "New Brunswick port for the Bay of Fundy's record tides.", "Puerto de Nuevo Brunswick para las mareas récord de la Bahía de Fundy."),
            _c("Bar Harbor", "Gateway to Maine's Acadia National Park (a tender port).", "Puerta de entrada al Parque Nacional Acadia de Maine (puerto de fondeo)."),
            _c("Portland", "Maine lighthouses, lobster and the Old Port district.", "Faros de Maine, langosta y el distrito Old Port."),
            _c("Quebec City", "A walled French-Canadian old town on the St. Lawrence.", "Un casco antiguo francocanadiense amurallado sobre el San Lorenzo."),
            _c("Sydney", "A Cape Breton port and gateway to the Cabot Trail.", "Un puerto de Cape Breton y puerta al Cabot Trail."),
        ],
    },
    "hawaii": {
        "expect": {"en": "Multiple islands on one trip, with more sea days than a Caribbean cruise. Round-trips from the mainland are long; inter-island sailings pack four islands into a week.",
                   "es": "Varias islas en un viaje, con más días de mar que un crucero por el Caribe. Los cruceros de ida y vuelta desde el continente son largos; los inter-islas reúnen cuatro islas en una semana."},
        "calls": [
            _c("Honolulu (Oahu)", "Waikiki, Pearl Harbor and Diamond Head.", "Waikiki, Pearl Harbor y Diamond Head."),
            _c("Kahului (Maui)", "The Road to Hana, Haleakalā and Lahaina.", "La carretera a Hana, Haleakalā y Lahaina."),
            _c("Kona", "Big Island coffee, snorkelling and volcano country (a tender port).", "Café de Big Island, snorkel y tierra de volcanes (puerto de fondeo)."),
            _c("Hilo", "The lush gateway to Volcanoes National Park and waterfalls.", "La puerta verde al Parque Nacional de los Volcanes y las cascadas."),
            _c("Nawiliwili (Kauai)", "The Garden Isle — the Na Pali coast and canyons.", "La Isla Jardín — la costa Na Pali y sus cañones."),
            _c("Ensenada", "A required foreign stop in Mexico on round-trip Hawaii sailings.", "Una escala extranjera obligatoria en México en los cruceros de ida y vuelta a Hawái."),
        ],
    },
    "panama-canal": {
        "expect": {"en": "A bucket-list transit through the locks, on either a full ocean-to-ocean crossing or a partial round-trip that enters the canal and turns back. Best in the drier October–April window.",
                   "es": "Un tránsito de lista de deseos por las esclusas, en un cruce completo de océano a océano o en un ida y vuelta parcial que entra al canal y regresa. Mejor en la ventana más seca de octubre a abril."},
        "calls": [
            _c("Panama Canal / Gatún Lake", "The transit itself — a century-old marvel of locks and lakes.", "El tránsito en sí — una maravilla centenaria de esclusas y lagos."),
            _c("Cartagena", "Colombia's walled Caribbean colonial city.", "La ciudad colonial amurallada del Caribe colombiano."),
            _c("Colón", "Panama's Caribbean gateway, near the locks.", "La puerta caribeña de Panamá, cerca de las esclusas."),
            _c("Puntarenas", "Costa Rica's Pacific port for rainforest and wildlife.", "El puerto pacífico de Costa Rica para selva y fauna."),
            _c("Cabo San Lucas", "Baja's arch and beaches on full crossings.", "El arco y las playas de Baja en los cruces completos."),
            _c("Aruba", "Dutch-Caribbean beaches on some routings.", "Playas del Caribe holandés en algunas rutas."),
        ],
    },
    "pacific-coastal": {
        "expect": {"en": "Short repositioning sailings up and down the US West Coast in spring and fall, as ships move between Alaska and Mexico seasons. A relaxed, scenery-first, mostly sea-day trip.",
                   "es": "Cruceros cortos de reposicionamiento por la costa oeste de EE.UU. en primavera y otoño, cuando los barcos se mueven entre las temporadas de Alaska y México. Un viaje relajado, de paisaje y días de mar."},
        "calls": [
            _c("San Francisco", "The Golden Gate, cable cars and the bay.", "El Golden Gate, los tranvías y la bahía."),
            _c("San Diego", "A harbour city with beaches and Balboa Park.", "Una ciudad portuaria con playas y Balboa Park."),
            _c("Astoria", "The Columbia River mouth in Oregon.", "La desembocadura del río Columbia en Oregón."),
            _c("Victoria, BC", "British-flavoured Butchart Gardens and Inner Harbour.", "Los jardines Butchart de aire británico y el Inner Harbour."),
            _c("Santa Barbara", "California's palm-lined 'American Riviera' (a tender port).", "La 'Riviera americana' de California, con palmeras (puerto de fondeo)."),
            _c("Ensenada", "A Baja wine-country stop.", "Una escala en la región vinícola de Baja."),
        ],
    },
    "transatlantic": {
        "expect": {"en": "A classic ocean crossing between North America and Europe — lots of sea days, a slower pace, and a repositioning-season timing. Great if the voyage itself is the point.",
                   "es": "Un cruce oceánico clásico entre Norteamérica y Europa — muchos días de mar, ritmo pausado y en temporada de reposicionamiento. Ideal si el viaje en sí es lo importante."},
        "calls": [
            _c("Southampton", "The classic English departure port for ocean crossings.", "El clásico puerto de salida inglés para los cruces oceánicos."),
            _c("Ponta Delgada (Azores)", "A mid-Atlantic Portuguese island stop.", "Una escala en las islas portuguesas del Atlántico medio."),
            _c("Bermuda", "Pink beaches on some crossings.", "Playas rosadas en algunos cruces."),
            _c("New York", "The Manhattan skyline as you arrive or depart.", "El horizonte de Manhattan al llegar o partir."),
            _c("Halifax", "A Nova Scotia gateway on some routings.", "Una puerta de Nueva Escocia en algunas rutas."),
        ],
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

    ships_by_line = _ships_by_line(slug)
    n_ships = sum(len(v) for v in ships_by_line.values())

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

    # typical ports of call — described cards
    if copy.get("calls"):
        cards = "".join(_card("📍", c["name"], "", c["desc"][lang]) for c in copy["calls"])
        pnote = ("Exact stops vary by ship and sailing — a specialist matches the itinerary to what you want to see."
                 if en else
                 "Las paradas exactas varían por barco y salida — un especialista ajusta el itinerario a lo que quieres ver.")
        out += _sec("cream", ("Typical ports of call" if en else "Puertos de escala típicos"), "📍",
                    f'<div class="xr-grid">{cards}</div><p class="note-line" style="margin-top:14px">{pnote}</p>')

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


# region -> hero background image (self-hosted). Some reuse existing region shots; the rest are
# sourced separately. Missing files fall back to the gradient hero automatically.
_HERO_IMG = {
    "caribbean": "caribbean.jpg", "bahamas": "bahamas.jpg", "alaska": "alaska.jpg",
    "bermuda": "bermuda.jpg", "mexican-riviera": "mexican-riviera.jpg",
    "canada-new-england": "newengland.jpg", "hawaii": "hawaii.jpg",
    "panama-canal": "panama-canal.jpg", "pacific-coastal": "california.jpg",
    "transatlantic": "transatlantic.jpg", "mediterranean": "mediterranean.jpg",
    "northern-europe": "northern-europe.jpg",
}


def hero_image(slug):
    """Return the hero image filename for a region if the file exists on disk, else None."""
    img = _HERO_IMG.get(slug)
    if img and os.path.exists(os.path.join(_PORTS_DIR, img)):
        return img
    return None


def dest_hero(lang, slug, name, sub, crumb):
    """A photo hero for destination pages: self-hosted region image, dark overlay, heading, sub,
    a quick-stat strip and a call button. Falls back to the standard gradient hero if no image."""
    en = lang == "en"
    img = hero_image(slug)
    kick = "Destination" if en else "Destino"
    stats = ""
    if slug in _DEP:
        r = _DEP[slug]
        n_ships = sum(len(v) for v in _ships_by_line(slug).values())
        chips = [
            (r["season"], "🗓️"),
            (f'{len(r["ports"])} ' + ("home ports" if en else "puertos"), "⚓"),
            (f'{n_ships} ' + ("ships" if en else "barcos"), "🚢"),
        ]
        stats = '<div class="dhero-stats">' + "".join(
            f'<span class="dhero-stat"><span aria-hidden="true">{e}</span> {t}</span>' for t, e in chips) + '</div>'
    call = "Call now" if en else "Llama ahora"
    cta = (f'<a class="btn btn-call dhero-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'dest-hero\')">'
           f'<span class="ic" aria-hidden="true">☎</span>{call} · {PHONE_DISPLAY}</a>')
    inner = (f'<p class="crumbs">{crumb}</p>'
             f'<span class="eyebrow" style="color:#7FD4D0">{kick}</span>'
             f'<h1>{name}</h1><p class="phero-sub">{sub}</p>{stats}'
             f'<div class="dhero-cta">{cta}</div>')
    if not img:  # gradient fallback (matches the standard hero)
        return f'<section class="section navy phero dhero"><div class="wrap">{inner}</div></section>'
    return (f'<section class="section phero dhero dhero-photo" style="--dhero-img:url(/ports/{img})">'
            f'<div class="dhero-scrim"></div><div class="wrap">{inner}</div></section>')


def more_destinations(lang, current_slug, dests):
    """A cross-link card grid of OTHER destinations, each with its region photo, name and best time —
    so a visitor can hop from one destination to a similar one. `dests` is the DESTINATIONS list."""
    en = lang == "en"
    cards = ""
    for d in dests:
        if d["slug"] == current_slug:
            continue
        img = hero_image(d["slug"])
        media = (f'<img src="/ports/{img}" alt="{d["name"][lang]}" loading="lazy" decoding="async">'
                 if img else "")
        best = d.get("best", {}).get(lang, "")
        best_html = f'<small>{("Best" if en else "Mejor")}: {best}</small>' if best else ""
        cards += (f'<a class="port-card destx-card" href="/{lang}/destinations/{d["slug"]}/">{media}'
                  f'<span class="port-nm">{d["emo"]} {d["name"][lang]}{best_html}</span></a>')
    h = "Explore more destinations" if en else "Explora más destinos"
    return (f'<section class="section cream"><div class="wrap"><h2 class="rsec-h">{h}</h2>'
            f'<div class="port-grid destx-grid">{cards}</div></div></section>')


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
