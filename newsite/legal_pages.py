# -*- coding: utf-8 -*-
"""Legal pages, Terms, Privacy, Calling & SMS Consent (TCPA), Do Not Sell or Share.
Bilingual. Compliance-critical: keep the disclaimers intact. Placeholders in [brackets]
must be filled before launch ([Your Company] LLC, address, privacy email)."""
import datetime
from config import PHONE_DISPLAY, PHONE_HREF, HOURS, BRAND, SITE_URL, COMPANY, COMPANY_ADDR, PRIVACY_EMAIL

YEAR = datetime.date.today().year
TODAY = datetime.date.today().isoformat()


def _crumb(lang, title):
    home = "Home" if lang == "en" else "Inicio"
    return f'<a href="/{lang}/index.html">{home}</a> › {title}'


LEGAL = {
    "terms": {
        "title": {"en": "Terms of Use", "es": "Términos de uso"},
        "sec": [
            ({"en": "What we are", "es": "Qué somos"},
             {"en": f"{BRAND} is a marketing and referral service. We are not a cruise line, travel agency, tour "
                    "operator or seller of travel. We do not sell, book, ticket or take payment for travel, and we do "
                    "not set prices or hold inventory. When you call, you may be connected to one of several independent, "
                    "licensed third-party travel agencies. All quotes, bookings, payments and customer service are "
                    "provided by that agency under its own terms, and we may receive a referral fee.",
              "es": f"{BRAND} es un servicio de marketing y referencia. No somos una línea de crucero, agencia de "
                    "viajes, operador turístico ni vendedor de viajes. No vendemos, reservamos, emitimos boletos ni "
                    "cobramos por viajes, y no fijamos precios ni tenemos inventario. Cuando llamas, puedes ser "
                    "conectado con una de varias agencias de viajes independientes y con licencia. Todas las "
                    "cotizaciones, reservas, pagos y atención al cliente los proporciona esa agencia según sus propios "
                    "términos, y podemos recibir una comisión de referencia."}),
            ({"en": "Information, not advice or offers", "es": "Información, no asesoría ni ofertas"},
             {"en": "The information on this site is general and for planning purposes only. It is not a quote, an "
                    "offer, or professional advice, and it does not display fares, rates or savings. Cruise "
                    "line policies change; we verify facts against their sources and mark anything unverified as such, "
                    "but you should confirm details that matter to you with the agency that books your trip.",
              "es": "La información de este sitio es general y solo para fines de planificación. No es una cotización, "
                    "una oferta ni asesoría profesional, y no muestra tarifas, precios, descuentos ni ahorros. Las "
                    "políticas de las líneas cambian; verificamos los datos con sus fuentes y marcamos lo no verificado, "
                    "pero debes confirmar los detalles importantes con la agencia que reserve tu viaje."}),
            ({"en": "Trademarks", "es": "Marcas registradas"},
             {"en": "All cruise line names, ship names, logos and trademarks are the property of their respective "
                    "owners and are used only descriptively to identify lines our partner agencies can book. We are not "
                    "affiliated with, sponsored by, endorsed by, authorised by, or an agent of any cruise line, and this "
                    "is not an official site of any cruise line.",
              "es": "Todos los nombres de líneas de crucero, nombres de barcos, logotipos y marcas son propiedad de sus "
                    "respectivos dueños y se usan solo de forma descriptiva para identificar líneas que nuestras "
                    "agencias asociadas pueden reservar. No estamos afiliados, patrocinados, respaldados, autorizados "
                    "por, ni somos agentes de ninguna línea, y este no es un sitio oficial de ninguna línea."}),
            ({"en": "Coverage hours", "es": "Horario de atención"},
             {"en": f"Advisors are available {HOURS['en']}. We do not claim 24/7 availability.",
              "es": f"Los asesores están disponibles {HOURS['es']}. No afirmamos disponibilidad 24/7."}),
            ({"en": "Contact", "es": "Contacto"},
             {"en": f"[Your Company] LLC, [Street Address], Florida, USA. Telephone {PHONE_DISPLAY}. "
                    "Email [privacy@yourdomain.com].",
              "es": f"[Your Company] LLC, [Dirección], Florida, EE. UU. Teléfono {PHONE_DISPLAY}. "
                    "Correo [privacy@yourdomain.com]."}),
        ]},
    "privacy": {
        "title": {"en": "Privacy Policy", "es": "Política de privacidad"},
        "sec": [
            ({"en": "What we collect", "es": "Qué recopilamos"},
             {"en": "If you call or submit a request, we may collect the phone number and name you provide and details "
                    "of the trip you're asking about. Our site may use standard analytics (such as pages viewed and "
                    "call-button clicks) to measure performance.",
              "es": "Si llamas o envías una solicitud, podemos recopilar el número de teléfono y el nombre que "
                    "proporciones y los detalles del viaje que consultas. Nuestro sitio puede usar analíticas estándar "
                    "(como páginas vistas y clics en el botón de llamada) para medir el rendimiento."}),
            ({"en": "How we use and share it", "es": "Cómo lo usamos y compartimos"},
             {"en": "We use your information to connect you with a licensed partner travel agency and to improve our "
                    "service. Because we share enquiry details with independent partner agencies so they can assist you, "
                    "this sharing may be treated as a 'sale' or 'share' under some state privacy laws. See Do Not Sell "
                    "or Share to opt out.",
              "es": "Usamos tu información para conectarte con una agencia de viajes asociada con licencia y para mejorar "
                    "nuestro servicio. Como compartimos los detalles de la consulta con agencias asociadas "
                    "independientes para que te ayuden, este intercambio puede considerarse una 'venta' o 'compartición' "
                    "bajo algunas leyes estatales. Consulta No vender ni compartir para excluirte."}),
            ({"en": "Retention & your rights", "es": "Conservación y tus derechos"},
             {"en": "We keep enquiry records only as long as needed for the purposes above or as required by law. "
                    "Depending on where you live, you may have rights to access, correct or delete your information. "
                    "Contact us at [privacy@yourdomain.com].",
              "es": "Conservamos los registros solo el tiempo necesario para los fines anteriores o según lo exija la "
                    "ley. Según dónde vivas, puedes tener derechos para acceder, corregir o eliminar tu información. "
                    "Contáctanos en [privacy@yourdomain.com]."}),
        ]},
    "consent": {
        "title": {"en": "Calling & SMS Consent", "es": "Consentimiento de llamadas y SMS"},
        "sec": [
            ({"en": "Contact consent", "es": "Consentimiento de contacto"},
             {"en": "By calling us or providing your phone number, you agree that we and our independent partner travel "
                    "agencies may contact you by phone and text message about your cruise enquiry, including by automated "
                    "means. Consent is not a condition of any purchase. Message and data rates may apply.",
              "es": "Al llamarnos o proporcionar tu número, aceptas que nosotros y nuestras agencias asociadas "
                    "independientes podamos contactarte por teléfono y mensaje de texto sobre tu consulta de crucero, "
                    "incluso por medios automatizados. El consentimiento no es condición de ninguna compra. Pueden "
                    "aplicarse tarifas de mensajes y datos."}),
            ({"en": "How to opt out", "es": "Cómo darte de baja"},
             {"en": "Reply STOP to any text message to stop texts. Ask any caller to place you on our internal "
                    "do-not-call list. We scrub against the National Do Not Call Registry and honour opt-out requests "
                    "promptly.",
              "es": "Responde STOP a cualquier mensaje para detener los textos. Pide a cualquier operador que te incluya "
                    "en nuestra lista interna de no llamar. Cotejamos con el Registro Nacional No Llame y atendemos las "
                    "solicitudes de baja con prontitud."}),
            ({"en": "Records", "es": "Registros"},
             {"en": "We retain a record of the consent language shown to you, the date and time you provided consent, "
                    "and the page on which it was given.",
              "es": "Conservamos un registro del texto de consentimiento mostrado, la fecha y hora en que lo diste, y la "
                    "página en la que se dio."}),
        ]},
    "do-not-sell": {
        "title": {"en": "Do Not Sell or Share My Personal Information", "es": "No vender ni compartir mi información"},
        "sec": [
            ({"en": "Your right to opt out", "es": "Tu derecho a excluirte"},
             {"en": "Certain state privacy laws give you the right to opt out of the sale or sharing of your personal "
                    "information. Because we share enquiry details with independent partner travel agencies so they can "
                    "assist you, this activity may be treated as a sale or share.",
              "es": "Ciertas leyes estatales te dan derecho a excluirte de la venta o compartición de tu información "
                    "personal. Como compartimos detalles de la consulta con agencias asociadas independientes para que "
                    "te ayuden, esta actividad puede considerarse una venta o compartición."}),
            ({"en": "How to opt out", "es": "Cómo excluirte"},
             {"en": "Contact us at [privacy@yourdomain.com] with the subject 'Do Not Sell or Share' and the phone "
                    "number and name you provided, so we can locate your record and process your request. Opting out "
                    "does not delete information already shared with a partner agency, contact that agency directly to "
                    "request deletion.",
              "es": "Contáctanos en [privacy@yourdomain.com] con el asunto 'No vender ni compartir' y el número y nombre "
                    "que proporcionaste, para localizar tu registro y procesar tu solicitud. Excluirte no elimina la "
                    "información ya compartida con una agencia asociada, contáctala directamente para solicitar la "
                    "eliminación."}),
            ({"en": "No discrimination", "es": "Sin discriminación"},
             {"en": "We will not deny you services, or provide a different level of service, because you exercised your "
                    "privacy rights.",
              "es": "No te negaremos servicios ni te daremos un nivel de servicio diferente por ejercer tus derechos de "
                    "privacidad."}),
        ]},
}


# Fill legal placeholders from config (company/address/email) across all legal copy.
_SUB = {"[Your Company] LLC": COMPANY, "[Street Address]": COMPANY_ADDR,
        "[Dirección]": COMPANY_ADDR, "[privacy@yourdomain.com]": PRIVACY_EMAIL}
for _page in LEGAL.values():
    for _h, _b in _page["sec"]:
        for _l in ("en", "es"):
            for _k, _v in _SUB.items():
                _b[_l] = _b[_l].replace(_k, _v)


def p_legal(lang, key):
    page = LEGAL[key]
    title = page["title"][lang]
    updated = ("Last updated" if lang == "en" else "Última actualización") + " " + TODAY
    secs = "".join(
        f'<section class="blk"><h2>{h[lang]}</h2><p class="intro">{b[lang]}</p></section>'
        for h, b in page["sec"])
    return (f'<section class="section navy phero"><div class="wrap">'
            f'<p class="crumbs">{_crumb(lang, title)}</p>'
            f'<h1>{title}</h1><p class="phero-sub">{updated}</p></div></section>'
            f'<section class="section"><div class="wrap legal-body">{secs}</div></section>')
