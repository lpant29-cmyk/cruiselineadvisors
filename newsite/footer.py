# -*- coding: utf-8 -*-
"""Site footer, one file. Link columns + the compliance disclaimers (bilingual).
The disclaimers are legally load-bearing; edit with care."""
from config import PHONE_DISPLAY, PHONE_HREF, HOURS, BRAND, COMPANY
from i18n import T
from badges import verified_seal
from facts import latest_verified_all
import datetime

YEAR = datetime.date.today().year

_SEAL_CAP = {
    "en": "All facts &amp; ship data verified from official cruise-line sites",
    "es": "Todos los datos verificados de sitios oficiales de las líneas",
}

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
        ("Pricing", "This site displays no fares, rates, discounts or savings."),
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
        ("Precios", "Este sitio no muestra tarifas, precios, descuentos ni ahorros."),
        ("Cómo verificamos", "Los datos de este sitio se obtienen del sitio web oficial y las políticas públicas de "
         "cada línea de crucero y se revisan cada 30 días. Lo que aún no está verificado se muestra como un vacío "
         "visible, nunca se adivina. Confirma siempre los detalles importantes con la agencia con licencia que reserve tu viaje."),
        ("Fotografía", "Las fotos de destinos, puertos y barcos son imágenes ilustrativas de archivo de fuentes libres "
         "de regalías (Pexels y Unsplash), usadas según sus licencias, que permiten el uso comercial sin atribución. "
         "Damos crédito a las fuentes aquí por cortesía. Las imágenes son solo representativas y pueden no mostrar el "
         "barco, puerto, vista o salida exactos; los nombres de islas privadas o lugares son de referencia."),
    ],
}

LEGAL = [  # (en label, es label, filename)
    ("Terms", "Términos", "terms.html"),
    ("Privacy", "Privacidad", "privacy.html"),
    ("Calling & SMS Consent", "Consentimiento de llamadas y SMS", "consent.html"),
    ("Do Not Sell or Share", "No vender ni compartir", "do-not-sell.html"),
]


def footer(lang):
    t = T[lang]
    disc = "".join(f"<p><b>{h}:</b> {b}</p>" for h, b in DISC[lang])
    legal = "".join(f'<a href="/{lang}/legal/{f}">{en if lang=="en" else es}</a>'
                    for en, es, f in LEGAL)
    return f"""<footer class="ftr">
  <div class="wrap">
    <div class="cols">
      <div class="foot-brand">
        <b style="color:#fff;font-family:'Fraunces',serif;font-size:1.2rem">CruiseLine<span style="color:#E0A84E">Advisors</span></b>
        <p>{t['foot_tag']} <b style="color:#C9DBE5">{t['foot_hours']}:</b> {HOURS[lang]}.</p>
        <p><a href="tel:{PHONE_HREF}" style="color:#E0A84E;font-weight:800;display:inline">☎ {PHONE_DISPLAY}</a></p>
        <div class="foot-seal">{verified_seal(lang, latest_verified_all())}<small>{_SEAL_CAP[lang]}</small></div>
      </div>
      <div>
        <h4>{t['foot_col_lines']}</h4>
        <a href="/{lang}/cruise-lines.html">{t['lines_all']}</a>
        <a href="/{lang}/lines/royal-caribbean.html">Royal Caribbean</a>
        <a href="/{lang}/lines/carnival.html">Carnival</a>
        <a href="/{lang}/lines/princess.html">Princess</a>
      </div>
      <div>
        <h4>{t['foot_col_res']}</h4>
        <a href="/{lang}/compare.html">{t['nav_compare']}</a>
        <a href="/{lang}/cruise-facts.html">{t['nav_facts']}</a>
        <a href="/{lang}/destinations.html">{t['nav_dest']}</a>
        <a href="/{lang}/guides.html">{t['nav_guides']}</a>
        <a href="/{lang}/updates.html">{t['nav_updates']}</a>
      </div>
      <div>
        <h4>{t['foot_col_legal']}</h4>
        {legal}
      </div>
      <div class="disc">
        {disc}
        <div class="legalrow">{legal}</div>
        <p style="margin-top:.6rem">© {YEAR} {COMPANY}. Florida, USA.</p>
      </div>
    </div>
  </div>
</footer>"""
