# -*- coding: utf-8 -*-
"""The comparison data sheet, SINGLE SOURCE OF TRUTH for the money/complex facts.

Powers BOTH the comparison tool AND the deep line pages, so re-verifying here every 30 days
updates every page automatically.

Each per-line value is {"v": {en,es} | None, "src": url | None, "verified": "YYYY-MM-DD" | None}.
v=None renders as a visible "Not yet verified" gap, NEVER invent a value (Hard Rule 3).
Fill these during the facts-sourcing pass by actually reading each source; record the source URL
and verified date. If a source page can't be read, leave it None and ask the user."""
from data import LINES

# The 12 approved comparison facts (order = display order). imp=True → highlighted as costly/complex.
FACTS = [
    {"key": "gratuities", "imp": True, "fee": True,
     "label": {"en": "Daily gratuities", "es": "Propinas diarias"},
     "note": {"en": "A published service charge added to your onboard account each day",
              "es": "Un cargo por servicio publicado que se añade a tu cuenta a bordo cada día"}},
    {"key": "included", "imp": True,
     "label": {"en": "What's included vs. extra", "es": "Qué se incluye vs. extra"},
     "note": {"en": "Dining and entertainment vs. specialty dining, drinks, wifi, excursions",
              "es": "Comida y entretenimiento vs. restaurantes especiales, bebidas, wifi, excursiones"}},
    {"key": "drink_pkg", "imp": True,
     "label": {"en": "Drink package rule", "es": "Regla del paquete de bebidas"},
     "note": {"en": "Whether all adults in the cabin must buy it",
              "es": "Si todos los adultos del camarote deben comprarlo"}},
    {"key": "wifi",
     "label": {"en": "Wi-Fi", "es": "Wi-Fi"},
     "note": {"en": "Included, or tiered packages at extra cost",
              "es": "Incluido, o paquetes por niveles con costo adicional"}},
    {"key": "deposit", "imp": True,
     "label": {"en": "Deposit & final payment", "es": "Depósito y pago final"},
     "note": {"en": "When the balance is due before sailing",
              "es": "Cuándo vence el saldo antes de zarpar"}},
    {"key": "cancel", "imp": True,
     "label": {"en": "Cancellation & refunds", "es": "Cancelación y reembolsos"},
     "note": {"en": "Penalty schedule as the sailing gets closer",
              "es": "Calendario de penalidades a medida que se acerca la salida"}},
    {"key": "refundable", "imp": True,
     "label": {"en": "Refundable vs non-refundable", "es": "Reembolsable vs no reembolsable"},
     "note": {"en": "Fare/deposit types and what you forfeit",
              "es": "Tipos de tarifa/depósito y qué pierdes"}},
    {"key": "solo",
     "label": {"en": "Solo traveller supplement", "es": "Suplemento para viajero solo"},
     "note": {"en": "Single supplement and whether solo cabins exist",
              "es": "Suplemento individual y si existen camarotes para solos"}},
    {"key": "kids",
     "label": {"en": "Kids, minimum age & clubs", "es": "Niños, edad mínima y clubes"},
     "note": {"en": "Minimum age to sail and kids-club age bands",
              "es": "Edad mínima para navegar y bandas de edad del club infantil"}},
    {"key": "obc",
     "label": {"en": "Onboard credit terms", "es": "Términos del crédito a bordo"},
     "note": {"en": "Refundable vs non-refundable onboard credit",
              "es": "Crédito a bordo reembolsable vs no reembolsable"}},
    {"key": "loyalty",
     "label": {"en": "Loyalty programme", "es": "Programa de fidelidad"},
     "note": {"en": "Programme name and how tiers work",
              "es": "Nombre del programa y cómo funcionan los niveles"}},
    {"key": "docs", "imp": True,
     "label": {"en": "Travel documents", "es": "Documentos de viaje"},
     "note": {"en": "Passport vs birth certificate on closed-loop sailings",
              "es": "Pasaporte vs acta de nacimiento en cruceros de ida y vuelta"}},
]

FACT_KEYS = [f["key"] for f in FACTS]

# All values start unverified. Sourcing fills v/src/verified per (line, fact).
LINE_FACTS = {
    L["slug"]: {k: {"v": None, "src": None, "verified": None} for k in FACT_KEYS}
    for L in LINES
}

# ── VERIFIED FACTS (sourced by actually reading the page; re-verify every 30 days) ──
# 2026-07-18, gratuities read directly from each line's official page (readable ones only).
LINE_FACTS["royal-caribbean"]["gratuities"] = {
    "v": {"en": "$21.00/day in suites; $18.50/day in all other staterooms (per guest)",
          "es": "$21.00/día en suites; $18.50/día en los demás camarotes (por huésped)"},
    "src": "https://www.royalcaribbean.com/faq/questions/onboard-service-gratuity-expense",
    "verified": "2026-09-15",
}
LINE_FACTS["celebrity"]["gratuities"] = {
    "v": {"en": "$19.50/day standard (Inside/Oceanview/Veranda); $20.50/day Concierge & AquaClass; $24.50/day The Retreat suites (per guest)",
          "es": "$19.50/día estándar (Inside/Oceanview/Veranda); $20.50/día Concierge y AquaClass; $24.50/día suites The Retreat (por huésped)"},
    "src": "https://www.celebritycruises.com/faqs/gratuity-program",
    "verified": "2026-09-15",
}
LINE_FACTS["celebrity"]["drink_pkg"] = {
    "v": {"en": "All guests of legal drinking age in the same stateroom must buy the same alcoholic package (exceptions for children, teens with a zero-proof package, and pregnant/medical cases).",
          "es": "Todos los adultos en edad legal del mismo camarote deben comprar el mismo paquete alcohólico (excepciones para niños, adolescentes con paquete sin alcohol y casos de embarazo/médicos)."},
    "src": "https://www.celebritycruises.com/faqs/beverage-packages", "verified": "2026-07-18"}
LINE_FACTS["celebrity"]["loyalty"] = {
    "v": {"en": "Captain's Club, tiers Preview, Classic, Select, Elite, Elite Plus, Zenith; points earned each sailing by stateroom category and cruise length.",
          "es": "Captain's Club, niveles Preview, Classic, Select, Elite, Elite Plus, Zenith; puntos por cada crucero según categoría de camarote y duración."},
    "src": "https://www.celebritycruises.com/captains-club/tiers-and-benefits", "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["gratuities"] = {
    "v": {"en": "$20.00/day for suites; $18.00/day for all other staterooms (per guest, Crew Appreciation)",
          "es": "$20.00/día en suites; $18.00/día en los demás camarotes (por huésped, Crew Appreciation)"},
    "src": "https://www.hollandamerica.com/en/us/faq/onboard-cruise-experience/onboard-information/is-there-a-crew-appreciation-charge-gratuity-tip",
    "verified": "2026-09-15",
}
LINE_FACTS["holland-america"]["drink_pkg"] = {
    "v": {"en": "All guests of legal drinking age in the same stateroom must buy the same package for the whole cruise (Signature or Elite).",
          "es": "Todos los adultos en edad legal del mismo camarote deben comprar el mismo paquete durante todo el crucero (Signature o Elite)."},
    "src": "https://www.hollandamerica.com/en/us/faq/onboard-cruise-experience/beverage/what-if-my-traveling-companion-doesnt-drink-do-they-still-have-to-purchase-a-beverage-package",
    "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["deposit"] = {
    "v": {"en": "Final payment due 90 days before departure for cruises of 13 days or less (excluding Asia, Australia and South America). Bookings opened from 29 Sep 2026 departing 2027 or later: 120 days.",
          "es": "Pago final 90 días antes de la salida en cruceros de 13 días o menos (excepto Asia, Australia y Sudamérica). Reservas abiertas desde el 29 sep 2026 con salida en 2027 o después: 120 días."},
    "src": "https://www.hollandamerica.com/en/us/legal-privacy/cancellation-policy-US-default", "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["cancel"] = {
    "v": {"en": "Cruises of 13 days or less booked now: 90+ days before departure = full refund; 89-83 days = full refund less the deposit; 82-46 days = 50% refunded; 45 days or fewer = no refund. Bookings opened from 29 Sep 2026 departing 2027 or later: 120+ days = full refund; 119-91 = 75% refunded; 90-61 = 50% refunded; 60 or fewer = no refund. Grand World and Grand Voyages differ.",
          "es": "Cruceros de 13 días o menos reservados ahora: 90+ días antes = reembolso completo; 89-83 días = reembolso completo menos el depósito; 82-46 días = 50% reembolsado; 45 días o menos = sin reembolso. Reservas abiertas desde el 29 sep 2026 con salida en 2027 o después: 120+ días = completo; 119-91 = 75%; 90-61 = 50%; 60 o menos = sin reembolso. Grand World y Grand Voyages difieren."},
    "src": "https://www.hollandamerica.com/en/us/legal-privacy/cancellation-policy-US-default", "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["loyalty"] = {
    "v": {"en": "Mariner Society, Cruise Day credits from cruise days, onboard purchases and double days in suites; five Star Mariner tiers.",
          "es": "Mariner Society, Cruise Day credits por días de crucero, compras a bordo y días dobles en suites; cinco niveles Star Mariner."},
    "src": "https://www.hollandamerica.com/en/us/faq/loyalty-program/loyalty-program-general-information/what-is-the-mariner-society-rewards-program",
    "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["kids"] = {
    "v": {"en": "Infants must be at least 6 months old to sail; 12 months for transoceanic, South America, Asia, South Pacific and Hawaii voyages. Kids programmes ages 3-17: Kids Club 3-6, Tweens 7-11, Teens 12-17.",
          "es": "Los bebés deben tener al menos 6 meses; 12 meses en travesías transoceánicas, Sudamérica, Asia, Pacífico Sur y Hawái. Programas infantiles de 3 a 17 años: Kids Club 3-6, Tweens 7-11, Teens 12-17."},
    "src": "https://www.hollandamerica.com/en/us/faq/cruise-planning/family-travel/is-there-a-minimum-age-for-cruising-on-holland-america-line",
    "verified": "2026-07-18"}
LINE_FACTS["margaritaville-at-sea"]["gratuities"] = {
    "v": {"en": "$25.00/night for Suites; $22.00/night for all other staterooms (per person)",
          "es": "$25.00/noche en Suites; $22.00/noche en los demás camarotes (por persona)"},
    "src": "https://www.margaritavilleatsea.com/policies/onboard-charges",
    "verified": "2026-09-15",
}
# 2026-07-18, user-supplied from each official page (fetch tool couldn't read these).
LINE_FACTS["carnival"]["gratuities"] = {
    "v": {"en": "$19.00/day for suites; $17.00/day for standard staterooms (per person)",
          "es": "$19.00/día en suites; $17.00/día en camarotes estándar (por persona)"},
    "src": "https://www.carnival.com/help?topicid=1123",
    "verified": "2026-07-18",
}
LINE_FACTS["princess"]["gratuities"] = {
    "v": {"en": "$20.00/day suites; $19.00/day mini-suites, cabanas & Reserve Collection; $18.00/day all other staterooms (per guest, Crew Appreciation)",
          "es": "$20.00/día suites; $19.00/día mini-suites, cabanas y Reserve Collection; $18.00/día los demás camarotes (por huésped)"},
    "src": "https://www.princess.com/static/html/global/disclaimers/crew-appreciation/index.html",
    "verified": "2026-07-18",
}
LINE_FACTS["cunard"]["gratuities"] = {
    "v": {"en": "$19.00/day Queens & Princess Grill Suites; $18.00/day Britannia & Britannia Club (per person)",
          "es": "$19.00/día Queens y Princess Grill Suites; $18.00/día Britannia y Britannia Club (por persona)"},
    "src": "https://www.cunard.com/en-gb/the-cunard-experience/service-charges",
    "verified": "2026-07-18",
}
LINE_FACTS["msc"]["gratuities"] = {
    "v": {"en": "$23.00/night Yacht Club; $17.00/night standard (per person; US/Caribbean, bookings from 11 May 2026)",
          "es": "$23.00/noche Yacht Club; $17.00/noche estándar (por persona; EE.UU./Caribe, reservas desde 11 may 2026)"},
    "src": "https://www.msccruisesusa.com/manage-booking/before-you-go/service-charges",
    "verified": "2026-07-18",
}

# ── Royal Caribbean (read from official FAQ pages 2026-07-18) ──
LINE_FACTS["royal-caribbean"]["drink_pkg"] = {
    "v": {"en": "Alcohol (Deluxe) package: every guest of legal drinking age in the same stateroom must buy it. Not sold on 2-4 night sailings departing Australia.",
          "es": "Paquete de alcohol (Deluxe): todos los adultos en edad legal del mismo camarote deben comprarlo. No se vende en salidas de 2-4 noches desde Australia."},
    "src": "https://www.royalcaribbean.com/faq/questions/does-everyone-need-to-buy-the-deluxe-beverage-package",
    "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["deposit"] = {
    "v": {"en": "Final payment due 75 days before sailing (1-4 nights), 90 days (5-14 nights), 120 days (15+ nights).",
          "es": "Pago final 75 días antes (1-4 noches), 90 días (5-14 noches), 120 días (15+ noches)."},
    "src": "https://www.royalcaribbean.com/faq/questions/final-payment-schedule-policy",
    "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["loyalty"] = {
    "v": {"en": "Crown & Anchor Society, 1 point per night; 2 per night in a suite; 3 per night sailing solo in a suite.",
          "es": "Crown & Anchor Society, 1 punto por noche; 2 por noche en suite; 3 por noche viajando solo en suite."},
    "src": "https://www.royalcaribbean.com/faq/questions/cruise-points-benefits",
    "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["docs"] = {
    "v": {"en": "US citizens born in the US can sail most (not all) closed-loop US departures with a state-certified birth certificate + government photo ID; a passport is recommended and is required for some sailings.",
          "es": "Los ciudadanos de EE.UU. nacidos en EE.UU. pueden viajar en la mayoría (no todas) de las salidas cerradas desde EE.UU. con acta de nacimiento estatal + identificación con foto; se recomienda pasaporte y es obligatorio en algunas salidas."},
    "src": "https://www.royalcaribbean.com/faq/questions/can-i-cruise-with-a-birth-certificate-as-my-identification",
    "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["wifi"] = {
    "v": {"en": "VOOM high-speed internet, a paid add-on, not included in the base fare; cost varies by number of devices and package tier.",
          "es": "VOOM internet de alta velocidad, un extra de pago, no incluido en la tarifa base; el costo varía según el número de dispositivos y el nivel del paquete."},
    "src": "https://www.royalcaribbean.com/faq/questions/onboard-internet-wifi-device-policy", "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["kids"] = {
    "v": {"en": "Infants must be at least 6 months old to sail; 12 months for transatlantic, transpacific, Hawaii, select South American and any cruise with 3+ consecutive sea days. Kids programme: Adventure Ocean.",
          "es": "Los bebés deben tener al menos 6 meses para navegar; 12 meses en transatlánticos, transpacíficos, Hawái, ciertos cruceros a Sudamérica y cualquier crucero con 3+ días consecutivos en el mar. Programa infantil: Adventure Ocean."},
    "src": "https://www.royalcaribbean.com/faq/questions/international-age-policy", "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["cancel"] = {
    "v": {"en": "By cruise length (US ticket contract): 1-4 nights, 75+ days = no charge, 74-61 = 50%, 60-31 = 75%, 30 or fewer = 100%. 5-14 nights, 90+ = none, 89-75 = 25%, 74-61 = 50%, 60-31 = 75%, 30 or fewer = 100%. 15+ nights, 120+ = none, 119-61 = 25%, 60-41 = 50%, 40-25 = 75%, 24 or fewer = 100%.",
          "es": "Por duración (contrato de EE.UU.): 1-4 noches, 75+ días = sin cargo, 74-61 = 50%, 60-31 = 75%, 30 o menos = 100%. 5-14 noches, 90+ = sin cargo, 89-75 = 25%, 74-61 = 50%, 60-31 = 75%, 30 o menos = 100%. 15+ noches, 120+ = sin cargo, 119-61 = 25%, 60-41 = 50%, 40-25 = 75%, 24 o menos = 100%."},
    "src": "https://www.royalcaribbean.com/guest-terms/us/united-states-english/", "verified": "2026-07-18"}
LINE_FACTS["celebrity"]["deposit"] = {
    "v": {"en": "Celebrity does not publish a final-payment day count on its FAQ or ticket contract. The contract's no-charge cancellation cutoffs are 75 days (1-4 nights), 90 days (5-14 nights) and 120 days (15+ nights); confirm your own due date with the agency that books you.",
          "es": "Celebrity no publica un plazo de pago final en su FAQ ni en su contrato. Los cortes de cancelación sin cargo del contrato son 75 días (1-4 noches), 90 días (5-14 noches) y 120 días (15+ noches); confirma tu fecha con la agencia que te reserve."},
    "src": "https://www.celebritycruises.com/guest-terms/united-states-english/", "verified": "2026-07-18"}
LINE_FACTS["celebrity"]["cancel"] = {
    "v": {"en": "By cruise length (US ticket contract): 1-4 nights, 75+ days = no charge, 74-61 = 50%, 60-31 = 75%, 30 or fewer = 100%. 5-14 nights, 90+ = none, 89-75 = 25%, 74-61 = 50%, 60-31 = 75%, 30 or fewer = 100%. 15+ nights, 120+ = none, 119-75 = 25%, 74-61 = 50%, 60-31 = 75%, 30 or fewer = 100%.",
          "es": "Por duración (contrato de EE.UU.): 1-4 noches, 75+ días = sin cargo, 74-61 = 50%, 60-31 = 75%, 30 o menos = 100%. 5-14 noches, 90+ = sin cargo, 89-75 = 25%, 74-61 = 50%, 60-31 = 75%, 30 o menos = 100%. 15+ noches, 120+ = sin cargo, 119-75 = 25%, 74-61 = 50%, 60-31 = 75%, 30 o menos = 100%."},
    "src": "https://www.celebritycruises.com/guest-terms/united-states-english/", "verified": "2026-07-18"}


# ── User-sourced (read in-browser) 2026-07-18. Prices stripped for compliance (tiers/rules kept). ──
_BULK = {
    # Carnival
    ("carnival", "included"): ({"en": "Included: main & Lido dining, entertainment, pools, fitness, youth programs. Extra: specialty dining, bar drinks, Wi-Fi, spa, casino, shore excursions, gratuities.",
                                 "es": "Incluye: comedor principal y Lido, entretenimiento, piscinas, gimnasio, programas juveniles. Extra: restaurantes especiales, bebidas, Wi-Fi, spa, casino, excursiones, propinas."},
                                "https://help.carnival.com/app/answers/detail/a_id/3861"),
    ("carnival", "drink_pkg"): ({"en": "Yes, CHEERS! must be bought for every adult (21+) in the stateroom.",
                                  "es": "Sí, CHEERS! debe comprarse para todos los adultos (21+) del camarote."},
                                 "https://help.carnival.com"),
    ("carnival", "wifi"): ({"en": "Paid tiers only: Social, Value and Premium. No tier is included in the fare. Each plan covers one device at a time; advance plans run the whole cruise, daily plans are sold on board.",
                             "es": "Solo niveles de pago: Social, Value y Premium. Ninguno se incluye en la tarifa. Cada plan cubre un dispositivo a la vez; los planes anticipados cubren todo el crucero y los diarios se venden a bordo."},
                            "https://help.carnival.com"),
    ("carnival", "deposit"): ({"en": "Final payment 76 days out (cruises ≤5 days); 91 days out (6+ days, and Alaska/Europe/Panama/Transatlantic/Transpacific).",
                                "es": "Pago final 76 días antes (cruceros ≤5 días); 91 días antes (6+ días, y Alaska/Europa/Panamá/Transatlántico/Transpacífico)."},
                               "https://help.carnival.com/app/answers/detail/a_id/481"),
    ("carnival", "cancel"): ({"en": "Deposit only until 56 days out; 50% penalty (55-30 days); 75% (29-15 days); 100% (14-0 days).",
                               "es": "Solo depósito hasta 56 días antes; 50% (55-30 días); 75% (29-15 días); 100% (14-0 días)."},
                              "https://help.carnival.com/app/answers/detail/a_id/3401"),
    ("carnival", "kids"): ({"en": "Min age 6 months (domestic) / 12 months (transoceanic). Camp Ocean: Turtles under 2, Penguins 2-5, Stingrays 6-8, Sharks 9-11; Circle 'C' 12-14; Club O2 15-17.",
                             "es": "Edad mínima 6 meses (nacional) / 12 meses (transoceánico). Camp Ocean: Turtles <2, Penguins 2-5, Stingrays 6-8, Sharks 9-11; Circle 'C' 12-14; Club O2 15-17."},
                            "https://help.carnival.com/app/answers/detail/a_id/2545"),
    ("carnival", "loyalty"): ({"en": "Carnival Rewards, which replaced VIFP in September 2026. Tiers: Red, Gold, Platinum, Diamond. Status is earned with Status Qualifying Stars from eligible spending and casino play, no longer by nights or cruises sailed. The first earning window runs 1 Sep 2026 to 31 Dec 2028 and Stars reset at the start of each window.",
                                "es": "Carnival Rewards, que sustituyó a VIFP en septiembre de 2026. Niveles: Red, Gold, Platinum, Diamond. El estatus se gana con Status Qualifying Stars por gasto elegible y casino, ya no por noches ni cruceros. La primera ventana va del 1 sep 2026 al 31 dic 2028 y las Stars se reinician en cada ventana."},
                               "https://www.carnival.com/vifp/benefits"),
    ("carnival", "docs"): ({"en": "Passport strongly recommended; birth certificate + government photo ID accepted on closed-loop U.S. domestic sailings.",
                             "es": "Pasaporte muy recomendado; acta de nacimiento + identificación con foto aceptadas en cruceros nacionales de ida y vuelta desde EE.UU."},
                            "https://help.carnival.com"),
    # Princess
    ("princess", "included"): ({"en": "Two packages, Princess Plus and Princess Premier, bundle drinks, casual & specialty dining, Wi-Fi and crew appreciation; without a package these are paid separately.",
                                 "es": "Dos paquetes, Princess Plus y Princess Premier, incluyen bebidas, comedor casual y especial, Wi-Fi y propinas; sin paquete se pagan por separado."},
                                "https://www.princess.com/en-int/cruise-deals-promotions/plus-premier-cruise-packages"),
    ("princess", "drink_pkg"): ({"en": "The package applies to the first two guests on the booking, both must buy in.",
                                  "es": "El paquete aplica a los dos primeros huéspedes de la reserva, ambos deben comprarlo."},
                                 "https://www.princess.com/en-int/cruise-deals-promotions/plus-premier-cruise-packages"),
    ("princess", "wifi"): ({"en": "MedallionNet Max is included with Princess Premier (4 devices per guest) and Princess Plus (1 device). Without a package, MedallionNet Classic is bought separately. No Wi-Fi is included in the base Standard fare.",
                             "es": "MedallionNet Max se incluye con Princess Premier (4 dispositivos por huésped) y Princess Plus (1 dispositivo). Sin paquete, MedallionNet Classic se compra aparte. La tarifa Standard no incluye Wi-Fi."},
                            "https://www.princess.com/en-int/cruise-deals-promotions/plus-premier-cruise-packages"),
    ("princess", "deposit"): ({"en": "Bookings made from 2 Sep 2026: final payment 120 days before departure for every cruise length. Booked before then: 90 days (1-13 day cruises), 120 days (14+ days). Cruises of 45+ days also take 10% at booking and a further 20% at 320 days out.",
                                "es": "Reservas desde el 2 sep 2026: pago final 120 días antes de la salida para cualquier duración. Reservado antes: 90 días (cruceros de 1-13 días), 120 días (14+ días). Los cruceros de 45+ días pagan además 10% al reservar y otro 20% a 320 días."},
                               "https://www.princess.com/en-int/plan/standard-cancellation-refund-policy"),
    ("princess", "cancel"): ({"en": "Bookings from 2 Sep 2026, cruises up to 44 days: 120+ days = deposit; 113-119 = 25%; 91-112 = 50%; 61-90 = 75%; 60 or fewer = 100%. Booked before then, 1-13 day cruises: 90+ days = deposit; 75-89 = 25%; 61-74 = 50%; 31-60 = 75%; 30 or fewer = 100%. Cruises of 45+ days run a longer schedule.",
                               "es": "Reservas desde el 2 sep 2026, cruceros de hasta 44 días: 120+ días = depósito; 113-119 = 25%; 91-112 = 50%; 61-90 = 75%; 60 o menos = 100%. Reservado antes, cruceros de 1-13 días: 90+ días = depósito; 75-89 = 25%; 61-74 = 50%; 31-60 = 75%; 30 o menos = 100%. Los de 45+ días tienen un calendario más largo."},
                              "https://www.princess.com/en-int/plan/standard-cancellation-refund-policy"),
    ("princess", "kids"): ({"en": "Infants must be at least 6 months old; 12 months for trans-ocean crossings and remote itineraries with more than two consecutive sea days. Clubs: The Treehouse 3-7, The Lodge 8-12, The Beach House 13-17.",
                             "es": "Los bebés deben tener al menos 6 meses; 12 meses en travesías transoceánicas e itinerarios remotos con más de dos días de mar seguidos. Clubes: The Treehouse 3-7, The Lodge 8-12, The Beach House 13-17."},
                            "https://www.princess.com/en-int/faq/pre-cruise"),
    ("princess", "loyalty"): ({"en": "Captain's Circle, Gold (1st cruise), Ruby (3 cruises / 30 days), Platinum (5 / 50), Elite (15 / 150).",
                                "es": "Captain's Circle, Gold (1er crucero), Ruby (3 cruceros / 30 días), Platinum (5 / 50), Elite (15 / 150)."},
                               "https://book.princess.com/captaincircle/membershipBenefits.page"),
    ("princess", "docs"): ({"en": "Passport required for international; birth certificate + photo ID accepted on select closed-loop U.S. sailings (Alaska, Canada/New England, Caribbean, Hawaii, Mexico).",
                             "es": "Pasaporte obligatorio para internacional; acta de nacimiento + identificación con foto en ciertos cruceros de ida y vuelta desde EE.UU. (Alaska, Canadá/Nueva Inglaterra, Caribe, Hawái, México)."},
                            "https://www.princess.com/en-int/faq/pre-cruise"),
    # Cunard (D & E flagged by user, left as gaps)
    ("cunard", "included"): ({"en": "Included: main dining, buffet, gala nights, tea/coffee/juice/water, entertainment, enrichment (library, classes, gym, pools, kids' clubs), basic My Voyage app access. Extra: alcohol, specialty dining, full Wi-Fi packages, spa.",
                               "es": "Incluye: comedor principal, buffet, noches de gala, té/café/jugo/agua, entretenimiento, enriquecimiento (biblioteca, clases, gimnasio, piscinas, clubes infantiles), acceso básico a la app My Voyage. Extra: alcohol, restaurantes especiales, paquetes completos de Wi-Fi, spa."},
                              "https://www.cunard.com/en-gb/the-cunard-experience/whats-included"),
    ("cunard", "drink_pkg"): ({"en": "Each adult in the same stateroom must buy the same World of Drinks collection, and collections cannot be shared. Minimum purchase age 18, though port laws may raise the age for service. The alcohol-free collections are open to all ages and infants of 3 and under are exempt.",
                                "es": "Cada adulto del mismo camarote debe comprar la misma colección World of Drinks, y no se pueden compartir. Edad mínima de compra 18 años, aunque las leyes de cada puerto pueden elevar la edad de servicio. Las colecciones sin alcohol no tienen límite de edad y los menores de 3 años están exentos."},
                               "https://www.cunard.com/en-gb/the-cunard-experience/activity-types/bars-and-lounges/a-world-of-drinks"),
    ("cunard", "wifi"): ({"en": "Two paid plans: Essential (email, social, images and text) and Premium (adds music and video streaming and video calls). Neither is in the base fare, though the Signature packages bundle one. The My Voyage app is free, and Gold, Platinum and Diamond World Club members receive internet credit.",
                           "es": "Dos planes de pago: Essential (correo, redes, imágenes y texto) y Premium (añade streaming de música y vídeo y videollamadas). Ninguno va en la tarifa base, aunque los paquetes Signature incluyen uno. La app My Voyage es gratuita y los miembros Gold, Platinum y Diamond reciben crédito de internet."},
                          "https://www.cunard.com/en-gb/the-cunard-experience/whats-included"),
    ("cunard", "kids"): ({"en": "Minimum age 6 months; 12 months on cruises with more than two consecutive sea days. Clubs: The Play Zone 2-7 and The Kids' Zone 8-12, with supervised play for 6-23 months alongside a parent. The Youth Team covers 2-17, but no separate teen club is named.",
                           "es": "Edad mínima 6 meses; 12 meses en cruceros con más de dos días de mar seguidos. Clubes: The Play Zone 2-7 y The Kids' Zone 8-12, con juego supervisado de 6 a 23 meses acompañados de un adulto. El Youth Team cubre de 2 a 17, pero no se nombra un club de adolescentes aparte."},
                          "https://www.cunard.com/en-gb/the-cunard-experience/activity-types/Children"),
    ("cunard", "loyalty"): ({"en": "Cunard World Club, Silver (1 voyage), Gold (2 voyages / 20 nights), Platinum (7 / 70), Diamond (15 / 150).",
                              "es": "Cunard World Club, Silver (1 viaje), Gold (2 viajes / 20 noches), Platinum (7 / 70), Diamond (15 / 150)."},
                             "https://www.cunard.com/en-gb/the-cunard-experience/cunard-world-club"),
    ("cunard", "docs"): ({"en": "Passport strongly recommended. The specific closed-loop birth-certificate policy isn't published on a readable page, confirm before booking.",
                           "es": "Pasaporte muy recomendado. La política específica de acta de nacimiento en cruceros de ida y vuelta no está publicada claramente, confírmala antes de reservar."},
                          None),
    # MSC (D & E flagged by user, left as gaps)
    ("msc", "included"): ({"en": "Included: main & buffet dining, entertainment, pools/sports/gym, kids & teens clubs. Extra: specialty dining, drinks, Wi-Fi, spa.",
                            "es": "Incluye: comedor principal y buffet, entretenimiento, piscinas/deportes/gimnasio, clubes de niños y adolescentes. Extra: restaurantes especiales, bebidas, Wi-Fi, spa."},
                           "https://www.msccruisesusa.com/on-board/dining-drinks"),
    ("msc", "drink_pkg"): ({"en": "Underage guests must buy the Minors Package if an adult in the cabin has a drinks package.",
                             "es": "Los menores deben comprar el Paquete de Menores si un adulto del camarote tiene paquete de bebidas."},
                            "https://www.msccruisesusa.com/on-board/dining-drinks/drinks-packages"),
    ("msc", "wifi"): ({"en": "Two paid tiers, Browse Cruise and Browse & Stream, with no free tier beyond the app. MSC publishes these tier names on its EU site; the US site confirms only that Wi-Fi is available on all ships.",
                        "es": "Dos niveles de pago, Browse Cruise y Browse & Stream, sin opción gratuita más allá de la app. MSC publica estos nombres en su sitio europeo; el sitio de EE.UU. solo confirma que hay Wi-Fi en todos los barcos."},
                       "https://www.msccruisesusa.com/on-board/internet-apps/wifi"),
    ("msc", "kids"): ({"en": "Infants under 2 may sail, except on cruises of 11 nights or more where every guest must be at least 2. Clubs: Mini 3-6, Junior 7-11, Young 12-14, Teen 15-17, plus a Baby Club for which no age range is published.",
                        "es": "Los menores de 2 años pueden navegar, salvo en cruceros de 11 noches o más, donde todos deben tener al menos 2. Clubes: Mini 3-6, Junior 7-11, Young 12-14, Teen 15-17, más un Baby Club cuyo rango de edad no se publica."},
                       "https://www.msccruisesusa.com/on-board/cruise-for-kids/clubs"),
    ("msc", "loyalty"): ({"en": "MSC Voyagers Club, Welcome, Classic, Silver, Gold, Diamond and Blue Diamond (by points; Blue Diamond 25,000+).",
                           "es": "MSC Voyagers Club, Welcome, Classic, Silver, Gold, Diamond y Blue Diamond (por puntos; Blue Diamond 25,000+)."},
                          "https://www.msccruisesusa.com/msc-voyagers-club"),
    ("msc", "docs"): ({"en": "Passport required for international; on U.S. closed-loop sailings a birth certificate + photo ID is accepted (16+ needs passport/passport card/birth certificate + photo ID; under 16 just a birth certificate).",
                        "es": "Pasaporte obligatorio para internacional; en cruceros de ida y vuelta desde EE.UU. se acepta acta de nacimiento + identificación con foto (16+ necesita pasaporte/tarjeta/acta + foto; menores de 16 solo acta)."},
                       "https://www.msccruisesusa.com/manage-booking/before-you-go/travel-documents-visas"),
}
for (_slug, _key), (_v, _src) in _BULK.items():
    LINE_FACTS[_slug][_key] = {"v": _v, "src": _src, "verified": "2026-07-18"}

# ── Margaritaville (read from its FAQ page 2026-07-18) ──
LINE_FACTS["margaritaville-at-sea"]["wifi"] = {
    "v": {"en": "Paid internet only. Two voyage-long tiers, Coconut Telegraph Basic (Surf) and Coconut Telegraph Premium (Stream); hourly, daily and multi-day plans also sold on board.",
          "es": "Solo internet de pago. Dos niveles por viaje, Coconut Telegraph Basic (Surf) y Coconut Telegraph Premium (Stream); también planes por hora, día y varios días a bordo."},
    "src": "https://www.margaritavilleatsea.com/policies/faq", "verified": "2026-07-18"}
LINE_FACTS["margaritaville-at-sea"]["kids"] = {
    "v": {"en": "Three supervised kids' programs (ages 3-17). The guest completing the booking must be 18 or older.",
          "es": "Tres programas infantiles supervisados (3-17 años). El huésped que hace la reserva debe tener 18 años o más."},
    "src": "https://www.margaritavilleatsea.com/policies/faq", "verified": "2026-07-18"}
LINE_FACTS["celebrity"]["wifi"] = {
    "v": {"en": "Two tiers, Basic Wi-Fi (browsing, email, messaging; included with eligible All Included rates) and Premium Wi-Fi (adds social, video calls, streaming and large files; a paid upgrade).",
          "es": "Dos niveles, Basic Wi-Fi (navegación, correo, mensajería; incluido con tarifas All Included elegibles) y Premium Wi-Fi (añade redes sociales, videollamadas, streaming y archivos grandes; mejora de pago)."},
    "src": "https://www.celebritycruises.com/faqs/wifi-onboard", "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["wifi"] = {
    "v": {"en": "Not included in the base fare, three paid plans: Surf (web, email, messaging), Premium (adds audio/messaging apps) and Stream (streaming). The Surf plan is included with the Have It All fare.",
          "es": "No incluido en la tarifa base, tres planes de pago: Surf (web, correo, mensajería), Premium (añade apps de audio/mensajería) y Stream (streaming). El plan Surf está incluido con la tarifa Have It All."},
    "src": "https://www.hollandamerica.com/en/us/onboard-packages/cruise-ship-wifi", "verified": "2026-07-18"}
LINE_FACTS["royal-caribbean"]["included"] = {
    "v": {"en": "Included: main dining & buffet, casual venues, water/tea/select juices/classic coffee, pools & whirlpools, thrill activities, fitness centre, Adventure Ocean youth program, shows & entertainment, private-destination access. Extra: beverage packages, specialty dining, shore excursions, Wi-Fi, spa, arcade, casino.",
          "es": "Incluye: comedor principal y buffet, opciones casuales, agua/té/jugos selectos/café clásico, piscinas y jacuzzis, actividades de aventura, gimnasio, programa juvenil Adventure Ocean, espectáculos y entretenimiento, acceso a destinos privados. Extra: paquetes de bebidas, restaurantes especiales, excursiones, Wi-Fi, spa, arcade, casino."},
    "src": "https://www.royalcaribbean.com/faq/questions/cruise-vacation-price", "verified": "2026-09-15"}
LINE_FACTS["celebrity"]["included"] = {
    "v": {"en": "Main dining, entertainment, pools and fitness are included. The optional 'All Included' rate adds a Classic Drinks Package and unlimited Basic Wi-Fi, and can only be added at the time of booking; otherwise drinks, Wi-Fi and specialty dining cost extra.",
          "es": "Comedor principal, entretenimiento, piscinas y gimnasio incluidos. La tarifa opcional 'All Included' añade un Classic Drinks Package y Wi-Fi básico ilimitado, y solo puede contratarse al reservar; de lo contrario bebidas, Wi-Fi y restaurantes especiales son extra."},
    "src": "https://www.celebritycruises.com/things-to-do-onboard/onboard-packages/all-included", "verified": "2026-09-15"}
LINE_FACTS["margaritaville-at-sea"]["deposit"] = {
    "v": {"en": "Final payment: 76 days before sailing (2-5 nights); 91 days (6-7 nights); 121 days (8+ nights).",
          "es": "Pago final: 76 días antes (2-5 noches); 91 días (6-7 noches); 121 días (8+ noches)."},
    "src": "https://www.margaritavilleatsea.com/policies/cancellation-policy", "verified": "2026-07-18"}
LINE_FACTS["margaritaville-at-sea"]["cancel"] = {
    "v": {"en": "Penalty rises closer to sailing and varies by length; e.g. 2-5 nights: full refund until 76 days, then deposit/50% (75-61 days), deposit/75% (60-31), 100% (0-30 days).",
          "es": "La penalidad aumenta al acercarse y varía por duración; ej. 2-5 noches: reembolso completo hasta 76 días, luego depósito/50% (75-61 días), depósito/75% (60-31), 100% (0-30 días)."},
    "src": "https://www.margaritavilleatsea.com/policies/cancellation-policy", "verified": "2026-07-18"}
LINE_FACTS["celebrity"]["kids"] = {
    "v": {"en": "Infants must be at least 6 months old to sail. Camp at Sea (ages 3-12): Shipmates 3-5, Cadets 6-9, Captains 10-12; separate Teen Club 13-17.",
          "es": "Los bebés deben tener al menos 6 meses. Camp at Sea (3-12 años): Shipmates 3-5, Cadets 6-9, Captains 10-12; Club de adolescentes 13-17."},
    "src": "https://www.celebritycruises.com/things-to-do-onboard/camp-at-sea", "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["docs"] = {
    "v": {"en": "On closed-loop US sailings, US citizens can sail with a US passport or an original/certified US birth certificate plus a government photo ID; a passport is preferred.",
          "es": "En cruceros de ida y vuelta desde EE.UU., los ciudadanos pueden viajar con pasaporte o con acta de nacimiento original/certificada más identificación con foto; se prefiere el pasaporte."},
    "src": "https://www.hollandamerica.com/en/us/faq/cruise-planning/identification-passports-visa/identification-requirements",
    "verified": "2026-07-18"}
LINE_FACTS["holland-america"]["included"] = {
    "v": {"en": "Dining and entertainment are included, and all taxes/fees are in the advertised fare. Extra: shore excursions, spa, beverage packages, Wi-Fi, specialty dining.",
          "es": "Comida y entretenimiento incluidos, y todos los impuestos/tasas están en la tarifa anunciada. Extra: excursiones, spa, paquetes de bebidas, Wi-Fi, restaurantes especiales."},
    "src": "https://www.hollandamerica.com/en/us/faq/cruise-planning/general-information/how-much-does-it-cost-to-go-on-a-cruise",
    "verified": "2026-09-15"}
LINE_FACTS["margaritaville-at-sea"]["drink_pkg"] = {
    "v": {"en": "Yes, all guests 21+ in the same stateroom must buy the beverage package (limited exceptions for documented medical conditions).",
          "es": "Sí, todos los adultos 21+ del mismo camarote deben comprar el paquete de bebidas (excepciones limitadas por condiciones médicas documentadas)."},
    "src": "https://www.margaritavilleatsea.com/current-offers/ultimate-beverage-chill", "verified": "2026-07-18"}
LINE_FACTS["celebrity"]["docs"] = {
    "v": {"en": "On closed-loop US sailings a US birth certificate plus a valid government photo ID is accepted instead of a passport (children 15 and under need only the birth certificate); a passport is preferred.",
          "es": "En cruceros de ida y vuelta desde EE.UU. se acepta un acta de nacimiento de EE.UU. más una identificación oficial con foto en lugar del pasaporte (menores de 15 solo el acta); se prefiere el pasaporte."},
    "src": "https://www.celebritycruises.com/travel-documents", "verified": "2026-07-18"}
LINE_FACTS["margaritaville-at-sea"]["docs"] = {
    "v": {"en": "On US sailings a US birth certificate is accepted; guests 16+ also need a valid government photo ID; children 15 and under need only the birth certificate. A passport is strongly recommended.",
          "es": "En cruceros desde EE.UU. se acepta un acta de nacimiento de EE.UU.; los huéspedes de 16+ también necesitan una identificación oficial con foto; los menores de 15 solo el acta. Se recomienda pasaporte."},
    "src": "https://www.margaritavilleatsea.com/resort-at-sea/travel-requirements", "verified": "2026-07-18"}
# Cunard D/E user-sourced from Cunard's UK Booking Conditions PDF (US-specific doc not found, verify).
LINE_FACTS["cunard"]["deposit"] = {
    "v": {"en": "Cunard does not publish a final-payment day count for the US market: it is absent from the US Passage Contract, and the US FAQ is not reachable. The figures circulating elsewhere come from Cunard's UK booking conditions, which need not match US terms, so we do not publish them. Confirm your own due date with the agency that books you.",
          "es": "Cunard no publica un plazo de pago final para el mercado de EE.UU.: no aparece en el contrato de pasaje estadounidense y su FAQ de EE.UU. no es accesible. Las cifras que circulan provienen de las condiciones del Reino Unido, que no tienen por qué coincidir, así que no las publicamos. Confirma tu fecha con la agencia que te reserve."},
    "src": "https://www.cunard.com/content/dam/cunard/marketing-assets/pdf/booking-condition-pdf/cunard-gb-booking-conditions-may2026.pdf",
    "verified": "2026-07-18"}
LINE_FACTS["cunard"]["cancel"] = {
    "v": {"en": "From the US Passage Contract. Voyages of 30 nights or fewer: 121+ days = no fee; 120-90 = 25% or the deposit; 89-61 = 40%; 60-31 = 50%; 30-15 = 75%; 14 or fewer, or no-show = 100%. Voyages of 31+ nights: 151+ days = no fee; 150-120 = 20% or the deposit; 119-91 = 40%; 90-64 = 50%; 63-43 = 75%; 42 or fewer = 100%.",
          "es": "Del contrato de pasaje de EE.UU. Viajes de 30 noches o menos: 121+ días = sin cargo; 120-90 = 25% o el depósito; 89-61 = 40%; 60-31 = 50%; 30-15 = 75%; 14 o menos, o no presentarse = 100%. Viajes de 31+ noches: 151+ días = sin cargo; 150-120 = 20% o el depósito; 119-91 = 40%; 90-64 = 50%; 63-43 = 75%; 42 o menos = 100%."},
    "src": "https://www.cunard.com/content/dam/cunard/marketing-assets/pdf/booking-condition-pdf/cunard-gb-booking-conditions-may2026.pdf",
    "verified": "2026-07-18"}
LINE_FACTS["msc"]["deposit"] = {
    "v": {"en": "Full payment due 75 days before departure (≤4 nights); 90 days (5-14 nights); 110 days (15+ nights); World Cruise 120 days.",
          "es": "Pago completo 75 días antes (≤4 noches); 90 días (5-14 noches); 110 días (15+ noches); Vuelta al Mundo 120 días."},
    "src": "https://www.msccruisesusa.com/-/media/US/Documents/booking-terms-and-conditions", "verified": "2026-07-18"}
LINE_FACTS["msc"]["cancel"] = {
    "v": {"en": "e.g. 5-14 nights: 89-61 days = deposit; 60-46 = 50%; 45-16 = 75%; 15-0 = 100%. Shorter (≤4 nights) and longer (15+ nights) sailings have their own tiers; Yacht Club is slightly tighter.",
          "es": "ej. 5-14 noches: 89-61 días = depósito; 60-46 = 50%; 45-16 = 75%; 15-0 = 100%. Los cruceros más cortos (≤4 noches) y más largos (15+ noches) tienen sus propios tramos; Yacht Club es algo más estricto."},
    "src": "https://www.msccruisesusa.com/-/media/US/Documents/booking-terms-and-conditions", "verified": "2026-07-18"}


# ── Margaritaville: included + loyalty (read from its FAQ) ──
LINE_FACTS["margaritaville-at-sea"]["included"] = {
    "v": {"en": "Main dining, buffet and entertainment are included. Extra: specialty dining, drinks, Wi-Fi, spa and gratuities.",
          "es": "Comedor principal, buffet y entretenimiento incluidos. Extra: restaurantes especiales, bebidas, Wi-Fi, spa y propinas."},
    "src": "https://www.margaritavilleatsea.com/policies/faq", "verified": "2026-09-15"}
LINE_FACTS["margaritaville-at-sea"]["loyalty"] = {
    "v": {"en": "No general cruise-loyalty tier programme; a casino Players Club is available.",
          "es": "Sin programa general de fidelidad por niveles; hay un Players Club de casino."},
    "src": "https://www.margaritavilleatsea.com/policies/faq", "verified": "2026-07-18"}

# ── General industry facts (refundable / solo / onboard credit) ──
# These aren't published as fixed per-line values, they're industry-uniform mechanics. Filled with
# accurate GENERAL statements (src=None, marked "General") for every line. Truthful, not invented.
_GENERAL = {
    "refundable": {"en": "Most lines sell both a refundable-deposit fare and a lower non-refundable-deposit fare; a non-refundable deposit is forfeited if you cancel and change fees can apply. (General, fare types vary by sailing.)",
                   "es": "La mayoría vende una tarifa con depósito reembolsable y otra más baja no reembolsable; el depósito no reembolsable se pierde al cancelar y pueden aplicarse cargos por cambio. (General, varía por crucero.)"},
    "solo": {"en": "A single supplement usually applies to solo travellers (roughly the cost of two fares); some ships offer dedicated solo cabins. Availability varies by ship and sailing, an advisor can find the solo-friendly options.",
             "es": "Suele aplicarse un suplemento individual al viajero solo (aprox. el costo de dos tarifas); algunos barcos tienen camarotes individuales. La disponibilidad varía por barco y crucero, un asesor encuentra las opciones."},
    "obc": {"en": "Onboard credit comes from promotions or loyalty status, not the base fare. Refundable credit can be withdrawn as cash at the end of the sailing; non-refundable credit must be spent onboard. (General, amounts and terms vary by offer.)",
            "es": "El crédito a bordo proviene de promociones o del nivel de fidelidad, no de la tarifa base. El reembolsable puede retirarse como efectivo al final; el no reembolsable debe gastarse a bordo. (General, varía por oferta.)"},
}
for _s in LINE_FACTS:
    for _k, _v in _GENERAL.items():
        if not LINE_FACTS[_s][_k]["v"]:
            LINE_FACTS[_s][_k] = {"v": _v, "src": None, "verified": "2026-07-18", "general": True}

# ── Secondary sources, 2026-09-23 re-verification ──────────────────────────
# Two "kids" values combine an age policy and a programme name that live on
# DIFFERENT official pages. The schema holds one src per fact, so src points at
# the age policy (the load-bearing claim) and the programme-name source is
# recorded here so the trail is not lost:
#   royal-caribbean/kids  programme name "Adventure Ocean Youth Program, ages 3-17"
#     verified at https://www.royalcaribbean.com/faq/questions/children-teen-activities
#   holland-america/kids  programme names "Kids Club 3-6, Tweens 7-11, Teens 12-17"
#     verified at https://www.hollandamerica.com/en/us/onboard-experiences/activities/kids-club
#     ("Club HAL" is retired consumer-facing branding and no longer appears.)

# ── 30-day re-verification, 2026-09-15 ──────────────────────────────────────
# Read on each line's own site this date and confirmed against the page before
# stamping. Applied here rather than at the definitions because several of
# these live in _BULK, which stamps its whole set at once.
#
# Retrieval notes recorded for the audit trail:
#   princess  gratuities: princess.com served en-int for an en-us request. The
#             page labels its figures "Amounts shown above are in USD" and the
#             session country was United States. AMOUNTS CONFIRMED UNCHANGED at
#             $20/$19/$18. The en-int page labels the middle tier "Club Class",
#             but our own verified cabin taxonomy (data/cruise-lines.json and
#             data/ships/princess.json) calls that tier "Reserve Collection",
#             and those render on the same site. Two official Princess pages
#             therefore disagree on the label while agreeing on the amount, so
#             the label is LEFT AS-IS for site-wide consistency rather than
#             switched on the strength of a non-US page. Settle against a US
#             princess.com page before changing it.
#   cunard    both: cunard.com served en-gb for an en-us request, but quotes the
#             service charge in US dollars explicitly. Same locale caveat as the
#             deposit/cancel facts already carry.
#   msc       both: msccruisesusa.com geo-redirects browsers to the EU site, so
#             these were read from the live HTML of the official US URLs direct
#             from MSC's own server. Official first-party source, different
#             retrieval route, no snippet or third party involved.
#   carnival  gratuities: value confirmed ($17 standard / $19 suite) but the
#             reporting conflated two help-centre answers under one a_id, so the
#             recorded src is left pointing at the topic page rather than being
#             overwritten with a URL that may address the wrong answer.
for _ln, _fld in [("carnival", "gratuities"), ("carnival", "included"),
                  ("princess", "gratuities"), ("princess", "included"),
                  ("cunard", "gratuities"), ("cunard", "included"),
                  ("msc", "gratuities"), ("msc", "included")]:
    LINE_FACTS[_ln][_fld]["verified"] = "2026-09-15"


def fact_value(slug, key, lang):
    """Rendered value or a visible 'Not yet verified' gap. Never invents."""
    cell = LINE_FACTS.get(slug, {}).get(key)
    if not cell or not cell.get("v"):
        return None  # caller renders the gap
    v = cell["v"]
    return v.get(lang, v.get("en")) if isinstance(v, dict) else v


def fact_source(slug, key):
    cell = LINE_FACTS.get(slug, {}).get(key)
    return (cell or {}).get("src"), (cell or {}).get("verified")


def coverage():
    """(verified_count, total), how many line×fact cells are filled."""
    total = len(LINE_FACTS) * len(FACT_KEYS)
    done = sum(1 for s in LINE_FACTS.values() for c in s.values() if c.get("v"))
    return done, total


def latest_verified(slug):
    """Most recent verified date among a line's filled facts (ISO strings compare lexically)."""
    ds = [c["verified"] for c in LINE_FACTS.get(slug, {}).values()
          if c.get("v") and c.get("verified")]
    return max(ds) if ds else None


def latest_verified_all():
    """Most recent verified date across every line, for the shared compare tool stamp."""
    ds = [c["verified"] for s in LINE_FACTS.values() for c in s.values()
          if c.get("v") and c.get("verified")]
    return max(ds) if ds else None

# ── Re-verification, 2026-09-23 ────────────────────────────────────────────
# All 28 read on each line's own site this date; 22 unchanged, 5 corrected,
# 1 (celebrity/deposit) rewritten because no Celebrity page publishes a
# final-payment day count. Nothing stamped that was not actually re-read.
for _ln, _fld in [('royal-caribbean', 'drink_pkg'), ('royal-caribbean', 'wifi'), ('royal-caribbean', 'deposit'), ('royal-caribbean', 'cancel'), ('royal-caribbean', 'kids'), ('royal-caribbean', 'loyalty'), ('royal-caribbean', 'docs'), ('celebrity', 'drink_pkg'), ('celebrity', 'wifi'), ('celebrity', 'deposit'), ('celebrity', 'cancel'), ('celebrity', 'kids'), ('celebrity', 'loyalty'), ('celebrity', 'docs'), ('holland-america', 'drink_pkg'), ('holland-america', 'wifi'), ('holland-america', 'deposit'), ('holland-america', 'cancel'), ('holland-america', 'kids'), ('holland-america', 'loyalty'), ('holland-america', 'docs'), ('margaritaville-at-sea', 'drink_pkg'), ('margaritaville-at-sea', 'wifi'), ('margaritaville-at-sea', 'deposit'), ('margaritaville-at-sea', 'cancel'), ('margaritaville-at-sea', 'kids'), ('margaritaville-at-sea', 'loyalty'), ('margaritaville-at-sea', 'docs')]:
    LINE_FACTS[_ln][_fld]["verified"] = "2026-09-23"

# ── Re-verification, 2026-09-23 (operator-supplied browser read) ───────────
# The four lines our fetch cannot reach. Read in a browser on each line's own
# site. Locale caveats recorded because they are load-bearing: princess.com and
# cunard.com force en-int/en-gb, and msccruisesusa.com geo-redirects to the EU
# site, so US figures for those came from the US pages via a direct fetcher.
# Biggest finds: Carnival retired VIFP entirely for Carnival Rewards, and our
# Cunard cancellation schedule was UK terms shown to US customers.
for _ln, _fld in [('carnival', 'drink_pkg'), ('carnival', 'wifi'), ('carnival', 'deposit'), ('carnival', 'cancel'), ('carnival', 'kids'), ('carnival', 'loyalty'), ('carnival', 'docs'), ('princess', 'drink_pkg'), ('princess', 'wifi'), ('princess', 'deposit'), ('princess', 'cancel'), ('princess', 'kids'), ('princess', 'loyalty'), ('princess', 'docs'), ('cunard', 'drink_pkg'), ('cunard', 'wifi'), ('cunard', 'deposit'), ('cunard', 'cancel'), ('cunard', 'kids'), ('cunard', 'loyalty'), ('cunard', 'docs'), ('msc', 'drink_pkg'), ('msc', 'wifi'), ('msc', 'deposit'), ('msc', 'cancel'), ('msc', 'kids'), ('msc', 'loyalty'), ('msc', 'docs')]:
    LINE_FACTS[_ln][_fld]["verified"] = "2026-09-23"
