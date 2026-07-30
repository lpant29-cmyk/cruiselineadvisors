# -*- coding: utf-8 -*-
"""THE shared legal-disclosure partial (operator ruling 2026-07-29).

Single source of truth for the legally load-bearing footer blocks
(what-we-are, trademarks, pricing, verification, photography), consumed by
BOTH the main site footer (newsite/footer.py) and the ads-LP generator
(lp-system/scripts/generate.py). A future legal edit here updates every
page on both surfaces in one place.

Pricing wording per ADS-LP-BRIEF section 6b (sitewide sentence) and 6a
(fares paragraph, appended only on fare-showing /go/ pages). The 6a taxes
clause keeps the brief's canonical wording pending the operator's
taxes-included arbitration; that decision lands HERE when made.
"""
from config import BRAND

DISC = {
    "en": [
        ("What we are", f"{BRAND} is a marketing and referral service. We are not a cruise line, "
         "travel agency, tour operator or seller of travel. We do not sell, book, ticket or take "
         "payment for travel, and we do not set prices or hold inventory. Calls may be connected to "
         "one of several independent, licensed third-party travel agencies, and we may receive a "
         "referral fee. All quotes, bookings and customer service are provided by that agency under its own terms."),
        ("Trademarks", "All cruise line names, ship names and marks are the property of their respective "
         "owners, used here descriptively only. We are not affiliated with, sponsored by, endorsed by, "
         "authorised by, or an agent of any cruise line."),
        ("Pricing", "Fares shown anywhere on this site are indicative, observed from public sources on "
         "the date stamped, and are not an offer to sell travel; all quotes and bookings are provided "
         "by independent licensed agencies."),
        ("How we verify", "The facts shown on this site are gathered from each cruise line's official website "
         "and public policies and re-checked every 30 days. Anything not yet verified is shown as a visible gap, "
         "never guessed. Always confirm the details that matter to you with the licensed agency that books your trip."),
        ("Photography", "Destination, port and ship photos are illustrative stock images from royalty-free sources "
         "(Pexels and Unsplash), used under their licenses, which permit commercial use without attribution. We credit "
         "the sources here as a courtesy. Images are representative only and may not show the exact ship, port, view or "
         "sailing; any private-island or venue names are for reference."),
    ],
    "es": [
        ("Qué somos", f"{BRAND} es un servicio de marketing y referencia. No somos una línea de crucero, "
         "agencia de viajes, operador turístico ni vendedor de viajes. No vendemos, reservamos, emitimos "
         "boletos ni cobramos por viajes, y no fijamos precios ni tenemos inventario. Las llamadas pueden "
         "conectarse con una de varias agencias de viajes independientes y con licencia, y podemos recibir "
         "una comisión de referencia. Todas las cotizaciones, reservas y atención al cliente las proporciona "
         "esa agencia según sus propios términos."),
        ("Marcas registradas", "Todos los nombres de líneas de crucero, nombres de barcos y marcas son "
         "propiedad de sus respectivos dueños, usados aquí solo de forma descriptiva. No estamos afiliados, "
         "patrocinados, respaldados, autorizados por, ni somos agentes de ninguna línea de crucero."),
        ("Precios", "Las tarifas mostradas en cualquier parte de este sitio son indicativas, observadas de "
         "fuentes públicas en la fecha indicada, y no constituyen una oferta de venta de viajes; todas las "
         "cotizaciones y reservas las proporcionan agencias independientes con licencia."),
        ("Cómo verificamos", "Los datos de este sitio se obtienen del sitio web oficial y las políticas públicas de "
         "cada línea de crucero y se revisan cada 30 días. Lo que aún no está verificado se muestra como un vacío "
         "visible, nunca se adivina. Confirma siempre los detalles importantes con la agencia con licencia que reserve tu viaje."),
        ("Fotografía", "Las fotos de destinos, puertos y barcos son imágenes ilustrativas de archivo de fuentes libres "
         "de regalías (Pexels y Unsplash), usadas según sus licencias, que permiten el uso comercial sin atribución. "
         "Damos crédito a las fuentes aquí por cortesía. Las imágenes son solo representativas y pueden no mostrar el "
         "barco, puerto, vista o salida exactos; los nombres de islas privadas o lugares son de referencia."),
    ],
}

# ADS-LP-BRIEF 6a: appended ONLY on fare-showing /go/ pages.
# Wording corrected 2026-07-30: the original said fares exclude taxes and
# fees, but the sourced Galveston fares are taxes-included and each fare
# says so inline. A footer contradicting the fare beside it is the exact
# pricing-accuracy exposure the hard rules exist to prevent. This version
# states what is true of each fare and does not overclaim.
FARES_PARA = {
    "en": ("Fares shown", "Prices shown are per-person lead-in fares based on double occupancy, observed "
           "from publicly available sources on the date stamped with each offer. What each fare covers is "
           "stated with the fare: where the source includes taxes and fees, we show that. Fares exclude "
           "gratuities, onboard spending and travel insurance, change frequently, and are not an offer to "
           "sell travel. All quotes, availability, bookings and payments are handled by independent "
           "licensed travel agencies. We do not sell, book or take payment for travel."),
    "es": ("Tarifas mostradas", "Los precios mostrados son tarifas iniciales por persona en ocupación doble, "
           "observadas de fuentes públicas en la fecha indicada junto a cada oferta. Lo que cubre cada "
           "tarifa se indica junto a ella: cuando la fuente incluye impuestos y tasas, lo mostramos. Las "
           "tarifas excluyen propinas, gastos a bordo y seguro de viaje, cambian con frecuencia y no "
           "constituyen una oferta de venta de viajes. Todas las cotizaciones, disponibilidad, reservas y "
           "pagos los gestionan agencias de viajes independientes con licencia. No vendemos, reservamos ni "
           "cobramos por viajes."),
}

LEGAL = [  # (en label, es label, filename)
    ("Terms", "Términos", "terms.html"),
    ("Privacy", "Privacidad", "privacy.html"),
    ("Calling & SMS Consent", "Consentimiento de llamadas y SMS", "consent.html"),
    ("Do Not Sell or Share", "No vender ni compartir", "do-not-sell.html"),
]

SITE_ORIGIN = ""  # main site renders same-origin; LP generator may set an absolute origin


def legal_blocks_html(lang, include_fares_paragraph=False):
    """The disclosure paragraphs. include_fares_paragraph adds the 6a text
    (fare-showing /go/ pages only)."""
    blocks = list(DISC[lang])
    if include_fares_paragraph:
        blocks = blocks + [FARES_PARA[lang]]
    return "".join(f"<p><b>{h}:</b> {b}</p>" for h, b in blocks)


def legal_links_html(lang, origin=""):
    """Terms / Privacy / Consent / Do-not-sell links to the main site's real
    legal pages. Emits the CLEAN directory URLs the host actually serves
    (/en/legal/terms/), matching the site's no-.html link convention —
    qa audit #7 D1: raw .html paths 404 on the served tree. origin='' for
    same-host; set an absolute origin if /go/ ever moves host."""
    return "".join(
        f'<a href="{origin}/{lang}/legal/{f.removesuffix(".html")}/">{en if lang == "en" else es}</a>'
        for en, es, f in LEGAL)
