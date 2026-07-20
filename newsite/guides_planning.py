# -*- coding: utf-8 -*-
"""Rich guides cluster: planning. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("cruise-documents-id", {
    "cat": "planning",
    "hero": "cruise-planning.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "Cruise documents & ID: passport vs birth certificate",
        "es": "Documentos e identificación para crucero: pasaporte vs acta de nacimiento",
    },
    "dek": {
        "en": "The single fastest way to be turned away at the pier is the wrong paperwork. Here is "
              "what you need to board a cruise, when a passport is required, and why it is the safer "
              "choice even when it is not strictly mandatory.",
        "es": "La forma más rápida de que te rechacen en el muelle es llevar los documentos "
              "equivocados. Esto es lo que necesitas para embarcar, cuándo se exige pasaporte, y por "
              "qué es la opción más segura aun cuando no es estrictamente obligatorio.",
    },
    "takeaways": {
        "en": [
            "A valid passport is the safest, simplest document for any cruise, and it is required for most sailings that begin or end outside your home country.",
            "On many closed-loop cruises (round-trips from the same US port), US citizens can sail on a birth certificate plus government photo ID, but a passport is still strongly recommended.",
            "Names on your booking must match your ID exactly; a mismatch can stop you boarding.",
            "Children have their own document rules; check requirements for every traveller, not just the adults.",
            "Some destinations need a visa or extra paperwork on top of your passport; confirm for your exact itinerary and nationality before you sail.",
        ],
        "es": [
            "Un pasaporte vigente es el documento más seguro y sencillo para cualquier crucero, y se exige en la mayoría de los cruceros que empiezan o terminan fuera de tu país.",
            "En muchos cruceros de ida y vuelta (closed-loop, desde el mismo puerto de EE.UU.), los ciudadanos estadounidenses pueden viajar con acta de nacimiento y una identificación oficial con foto, pero se recomienda un pasaporte.",
            "Los nombres de tu reserva deben coincidir exactamente con tu identificación; una diferencia puede impedir el embarque.",
            "Los niños tienen sus propias reglas de documentos; revisa los requisitos de cada viajero, no solo los adultos.",
            "Algunos destinos requieren visa o papeleo extra además del pasaporte; confírmalo para tu itinerario y nacionalidad exactos antes de zarpar.",
        ],
    },
    "sections": [
        {
            "id": "closed-loop",
            "h2": {"en": "Closed-loop cruises and the birth-certificate option", "es": "Cruceros closed-loop y la opción del acta de nacimiento"},
            "html": {
                "en": define("Closed-loop cruise",
                             "a round-trip that begins and ends at the same US port, for example Miami to the Caribbean "
                             "and back to Miami.")
                      + "<p>On many closed-loop sailings, US citizens are permitted to travel with a "
                      "<b>birth certificate</b> (an original or certified copy) plus a <b>government-issued photo ID</b>, "
                      "instead of a passport. It is a real option, and for some families it is the practical one.</p>"
                      + watch("The birth-certificate route has catches: it does not cover a cruise that starts or ends "
                              "abroad, and if you miss the ship in a foreign port or have an emergency, you generally "
                              "cannot fly home without a passport. Rules can also change, so confirm current "
                              "requirements before you rely on it.")
                      ,
                "es": define("Crucero closed-loop (ida y vuelta)",
                             "un viaje que empieza y termina en el mismo puerto de EE.UU., por ejemplo Miami al Caribe y "
                             "de vuelta a Miami.")
                      + "<p>En muchos cruceros closed-loop, los ciudadanos estadounidenses pueden viajar con <b>acta de "
                      "nacimiento</b> (original o copia certificada) más una <b>identificación oficial con foto</b>, en "
                      "lugar de pasaporte. Es una opción real, y para algunas familias es la práctica.</p>"
                      + watch("La opción del acta tiene condiciones: no cubre un crucero que empiece o termine en el "
                              "extranjero, y si pierdes el barco en un puerto extranjero o tienes una emergencia, "
                              "normalmente no puedes volar a casa sin pasaporte. Las reglas también pueden cambiar, así "
                              "que confirma los requisitos actuales antes de depender de ella.")
                      ,
            },
        },
        {
            "id": "why-passport",
            "h2": {"en": "Why a passport is the safer choice", "es": "Por qué un pasaporte es la opción más segura"},
            "html": {
                "en": "<p>Even when a birth certificate is technically allowed, a passport is the choice that removes "
                      "risk:</p>"
                      + vcards([
                          ("✈️", "Fly home if you miss the ship", "Miss a departure in a foreign port and you need a passport to fly back. A birth certificate will not do it."),
                          ("🌎", "Works on every itinerary", "One document covers closed-loop, one-way, and cruises that touch countries with stricter entry rules."),
                          ("⚡", "Faster, smoother boarding", "A passport is the universally recognised travel document, so check-in and any port immigration is simpler."),
                          ("🛟", "Emergencies abroad", "If plans change or something goes wrong overseas, a passport is what gets you moving again."),
                      ])
                      + "<p>Passports take time to arrive, so if you are leaning that way, apply well before your "
                      "final-payment date.</p>",
                "es": "<p>Aun cuando un acta de nacimiento se permite técnicamente, un pasaporte es la opción que "
                      "elimina el riesgo:</p>"
                      + vcards([
                          ("✈️", "Volar a casa si pierdes el barco", "Si pierdes una salida en un puerto extranjero, necesitas pasaporte para volar. Un acta no sirve."),
                          ("🌎", "Sirve en todo itinerario", "Un solo documento cubre closed-loop, de una vía, y cruceros que tocan países con reglas de entrada más estrictas."),
                          ("⚡", "Embarque más rápido", "El pasaporte es el documento de viaje reconocido universalmente, así que el check-in y la inmigración en puerto son más simples."),
                          ("🛟", "Emergencias en el extranjero", "Si los planes cambian o algo sale mal fuera, un pasaporte es lo que te pone en movimiento de nuevo."),
                      ])
                      + "<p>Los pasaportes tardan en llegar, así que si te inclinas por esa opción, tramítalo mucho "
                      "antes de tu fecha de pago final.</p>",
            },
        },
        {
            "id": "names-kids",
            "h2": {"en": "Names, children and the details that trip people up", "es": "Nombres, niños y los detalles que confunden"},
            "html": {
                "en": "<ul>"
                      "<li><b>Names must match.</b> The name on your booking has to match your travel document exactly. "
                      "Recently married or changed your name? Sort the paperwork out well before you sail.</li>"
                      "<li><b>Every traveller needs documents,</b> children included. Minors can have different ID and "
                      "consent requirements, especially when not travelling with both parents.</li>"
                      "<li><b>Some ports need more.</b> Certain countries on an itinerary may require a visa or extra "
                      "form even for a short port call.</li>"
                      "</ul>"
                      "<p>Requirements depend on your itinerary and your nationality, and they do change. We flag the "
                      "general document topic in the verified " + link("/en/cruise-facts/", "cruise facts") + ", and a "
                      "specialist confirms exactly what your party needs for your specific sailing.</p>",
                "es": "<ul>"
                      "<li><b>Los nombres deben coincidir.</b> El nombre de tu reserva debe coincidir exactamente con "
                      "tu documento de viaje. ¿Te casaste o cambiaste de nombre hace poco? Arregla el papeleo mucho "
                      "antes de zarpar.</li>"
                      "<li><b>Cada viajero necesita documentos,</b> niños incluidos. Los menores pueden tener "
                      "requisitos distintos de identificación y consentimiento, sobre todo si no viajan con ambos "
                      "padres.</li>"
                      "<li><b>Algunos puertos piden más.</b> Ciertos países del itinerario pueden requerir visa o un "
                      "formulario extra incluso para una escala corta.</li>"
                      "</ul>"
                      "<p>Los requisitos dependen de tu itinerario y tu nacionalidad, y sí cambian. Señalamos el tema "
                      "general de documentos en los " + link("/es/cruise-facts/", "datos de crucero") + " verificados, y "
                      "un especialista confirma exactamente qué necesita tu grupo para tu crucero específico.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>If you take one thing away: <b>get passports if you can.</b> They work on every itinerary, "
                      "cover you in an emergency, and take the guesswork out of the pier. If you sail closed-loop on a "
                      "birth certificate, understand the limits before you rely on it.</p>"
                      "<p>Not sure what your exact sailing and party need? A specialist confirms it, and the rest of "
                      "the planning, in one call. It also helps to read "
                      + link("/en/guides/first-time-cruisers/", "the first-time cruiser guide") + " next.</p>",
                "es": "<p>Si te llevas una sola cosa: <b>consigue pasaportes si puedes.</b> Sirven en todo itinerario, "
                      "te cubren en una emergencia y quitan la incertidumbre del muelle. Si navegas closed-loop con "
                      "acta de nacimiento, entiende los límites antes de depender de ella.</p>"
                      "<p>¿No sabes qué necesitan tu crucero y tu grupo exactos? Un especialista lo confirma, y el "
                      "resto de la planificación, en una llamada. También ayuda leer "
                      + link("/es/guides/first-time-cruisers/", "la guía para primer crucero") + " a continuación.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("Do I need a passport for a cruise?", "For most sailings that begin or end outside your home country, yes. On many closed-loop cruises (round-trips from the same US port) US citizens can use a birth certificate plus photo ID, but a passport is strongly recommended for everyone."),
            ("Can I cruise with just a birth certificate?", "On many closed-loop US sailings, US citizens can travel with an original or certified birth certificate plus a government photo ID. It does not cover cruises that start or end abroad, and you cannot fly home without a passport if you miss the ship, so weigh the risk."),
            ("What ID do children need for a cruise?", "Children need their own documents, and rules differ from adults. Minors may face extra ID or consent requirements, especially when not travelling with both parents. Confirm for every child before you sail."),
            ("What happens if the name on my booking does not match my ID?", "It can stop you boarding. The name on your reservation must match your travel document exactly, so fix any discrepancy (for example after a marriage or name change) well before departure."),
            ("Do I need a visa for cruise ports?", "Sometimes. Certain countries on an itinerary require a visa or extra form even for a short port call, depending on your nationality. Confirm the requirements for your exact itinerary before you sail."),
        ],
        "es": [
            ("¿Necesito pasaporte para un crucero?", "Para la mayoría de los cruceros que empiezan o terminan fuera de tu país, sí. En muchos cruceros closed-loop (ida y vuelta desde el mismo puerto de EE.UU.) los ciudadanos estadounidenses pueden usar acta de nacimiento más identificación con foto, pero se recomienda pasaporte para todos."),
            ("¿Puedo hacer un crucero solo con acta de nacimiento?", "En muchos cruceros closed-loop de EE.UU., los ciudadanos estadounidenses pueden viajar con acta de nacimiento original o certificada más identificación oficial con foto. No cubre cruceros que empiezan o terminan en el extranjero, y no puedes volar a casa sin pasaporte si pierdes el barco, así que evalúa el riesgo."),
            ("¿Qué identificación necesitan los niños?", "Los niños necesitan sus propios documentos, y las reglas difieren de los adultos. Los menores pueden tener requisitos extra de identificación o consentimiento, sobre todo si no viajan con ambos padres. Confírmalo para cada niño antes de zarpar."),
            ("¿Qué pasa si el nombre de mi reserva no coincide con mi identificación?", "Puede impedirte embarcar. El nombre de tu reserva debe coincidir exactamente con tu documento de viaje, así que corrige cualquier diferencia (por ejemplo tras un matrimonio o cambio de nombre) mucho antes de la salida."),
            ("¿Necesito visa para los puertos del crucero?", "A veces. Ciertos países del itinerario requieren visa o un formulario extra incluso para una escala corta, según tu nacionalidad. Confirma los requisitos para tu itinerario exacto antes de zarpar."),
        ],
    },
    "related": {
        "en": [
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "Everything else nobody tells you before your first sailing."),
            ("💸", "The cruise facts that cost you money", "/en/cruise-facts/", "Documents, gratuities, cancellation and more, verified per line."),
            ("🗺️", "How to choose a cruise destination", "/en/guides/how-to-choose-a-destination/", "Where you sail shapes the documents you need."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "One call confirms exactly what your party needs."),
        ],
        "es": [
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "Todo lo demás que nadie te dice antes de tu primer crucero."),
            ("💸", "Datos de crucero que cuestan dinero", "/es/cruise-facts/", "Documentos, propinas, cancelación y más, verificados por línea."),
            ("🗺️", "Cómo elegir un destino de crucero", "/es/guides/how-to-choose-a-destination/", "A dónde navegas define los documentos que necesitas."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Una llamada confirma exactamente qué necesita tu grupo."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("what-to-pack-for-a-cruise", {
    "cat": "planning", "hero": "cruise-planning.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "What to pack for a cruise (the smart checklist)", "es": "Qué llevar a un crucero (la lista inteligente)"},
    "dek": {
        "en": "Cruise packing is its own art: a few things you must not forget, a few the ship does not "
              "provide, and a few rules that catch people out at the pier. Here is the checklist that "
              "keeps embarkation smooth and your cabin clutter-free.",
        "es": "Empacar para un crucero es su propio arte: algunas cosas que no debes olvidar, algunas "
              "que el barco no ofrece, y algunas reglas que sorprenden en el muelle. Aquí está la lista "
              "que hace el embarque fácil y tu camarote ordenado.",
    },
    "takeaways": {
        "en": [
            "Carry-on the essentials: travel documents, medications, and anything you need before your checked bag reaches the cabin.",
            "Pack a mix of casual daywear, swimwear and at least one smarter outfit for evening; check whether your ship has a formal night.",
            "Bring things ships often do not provide: a power bank, a lanyard for your key card, motion-sickness remedies and any specialty toiletries.",
            "Know the rules: no irons or extension cords with surge protectors, and alcohol/beverage limits vary by line.",
            "Leave room for what you bring home, and pack light. Cabins and storage are compact.",
        ],
        "es": [
            "Lleva lo esencial en el equipaje de mano: documentos, medicamentos y lo que necesites antes de que tu maleta llegue al camarote.",
            "Empaca ropa casual de día, traje de baño y al menos un atuendo más elegante para la noche; revisa si tu barco tiene noche de gala.",
            "Lleva cosas que los barcos a menudo no ofrecen: batería portátil, un cordón para la tarjeta llave, remedios para el mareo y artículos de aseo especiales.",
            "Conoce las reglas: nada de planchas ni regletas con supresor de picos, y los límites de alcohol y bebidas varían por línea.",
            "Deja espacio para lo que traes de vuelta, y empaca ligero. Los camarotes y el almacenamiento son compactos.",
        ],
    },
    "sections": [
        {"id": "carry-on", "h2": {"en": "Your carry-on (the do-not-lose bag)", "es": "Tu equipaje de mano (la bolsa que no pierdes)"},
         "html": {
            "en": "<p>On embarkation day your checked luggage is delivered to your cabin later, sometimes a few hours "
                  "later, so anything you need right away goes in a carry-on you keep with you:</p>"
                  + vcards([
                      ("🪪", "Documents & ID", "Passport or birth certificate plus photo ID, booking confirmation, and any visas. Do not pack these in a checked bag."),
                      ("💊", "Medications", "All prescriptions in their original packaging, enough for the whole trip plus a few spare days."),
                      ("👙", "Day-one basics", "Swimwear and a change of clothes so you can enjoy the ship before your bags arrive."),
                      ("🔌", "Chargers & a power bank", "Cabins have limited outlets; a power bank and a USB charger earn their space."),
                  ]),
            "es": "<p>El día de embarque tu maleta se entrega en el camarote más tarde, a veces varias horas después, así "
                  "que lo que necesites de inmediato va en un equipaje de mano que llevas contigo:</p>"
                  + vcards([
                      ("🪪", "Documentos e identificación", "Pasaporte o acta de nacimiento más identificación con foto, la confirmación de reserva y visas. No los pongas en la maleta facturada."),
                      ("💊", "Medicamentos", "Todas las recetas en su empaque original, suficientes para todo el viaje más unos días extra."),
                      ("👙", "Básicos del primer día", "Traje de baño y una muda para disfrutar el barco antes de que lleguen tus maletas."),
                      ("🔌", "Cargadores y batería portátil", "Los camarotes tienen pocos enchufes; una batería portátil y un cargador USB valen su espacio."),
                  ]),
         }},
        {"id": "clothing", "h2": {"en": "Clothing: day, evening and dress codes", "es": "Ropa: día, noche y códigos de vestimenta"},
         "html": {
            "en": "<p>Days are casual, resort wear and swimwear. Evenings step it up a little, and many ships still hold "
                  "one or two smarter or formal nights on a weeklong sailing. Pack:</p>"
                  "<ul>"
                  "<li><b>Casual daywear</b> and comfortable shoes for ports and decks.</li>"
                  "<li><b>Swimwear</b> (two if you can, so one can dry).</li>"
                  "<li><b>Smart-casual evening outfits,</b> plus one dressier option if your ship has a formal night.</li>"
                  "<li><b>A light jacket or layers,</b> even in warm regions, indoor air-conditioning is cool.</li>"
                  "</ul>"
                  + tip("Dress codes vary by line and ship. If a formal night matters to you, confirm what your sailing does before you pack the tuxedo or the cocktail dress."),
            "es": "<p>Los días son casuales, ropa de resort y traje de baño. Las noches suben un poco, y muchos barcos "
                  "aún tienen una o dos noches más elegantes o de gala en un crucero de una semana. Empaca:</p>"
                  "<ul>"
                  "<li><b>Ropa casual de día</b> y zapatos cómodos para puertos y cubiertas.</li>"
                  "<li><b>Traje de baño</b> (dos si puedes, para que uno seque).</li>"
                  "<li><b>Atuendos de noche smart-casual,</b> más una opción más elegante si tu barco tiene noche de gala.</li>"
                  "<li><b>Una chaqueta ligera o capas,</b> incluso en regiones cálidas, el aire acondicionado interior es fresco.</li>"
                  "</ul>"
                  + tip("Los códigos de vestimenta varían por línea y barco. Si una noche de gala te importa, confirma qué hace tu crucero antes de empacar el esmoquin o el vestido de coctel."),
         }},
        {"id": "rules", "h2": {"en": "What not to pack (the rules)", "es": "Qué no empacar (las reglas)"},
         "html": {
            "en": watch("Most lines prohibit irons and steamers (fire risk), and surge-protector power strips. Cabins "
                        "usually have limited outlets, so a simple non-surge USB strip is the safe choice if allowed. "
                        "Alcohol and beverage limits vary a lot by line, so check yours before you pack drinks.")
                  + "<p>Also skip anything sharp, candles, drones (often restricted), and hoverboards. When in doubt, "
                  "the line's website lists prohibited items, and a specialist can confirm the current rules for your "
                  "ship.</p>",
            "es": watch("La mayoría de líneas prohíben planchas y vaporizadores (riesgo de incendio) y regletas con "
                        "supresor de picos. Los camarotes suelen tener pocos enchufes, así que una regleta USB simple "
                        "sin supresor es la opción segura si se permite. Los límites de alcohol y bebidas varían mucho "
                        "por línea, así que revisa el tuyo antes de empacar bebidas.")
                  + "<p>También evita objetos afilados, velas, drones (a menudo restringidos) y hoverboards. Ante la "
                  "duda, el sitio de la línea lista los artículos prohibidos, y un especialista puede confirmar las "
                  "reglas actuales de tu barco.</p>",
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>Carry on your documents, medication and day-one basics, pack a mix of casual and one smarter "
                  "outfit, bring the small things ships do not provide, and leave the prohibited items at home. Do that "
                  "and embarkation is a breeze.</p>"
                  "<p>New to all this? Read " + link("/en/guides/first-time-cruisers/", "the first-time cruiser guide") +
                  " next, and call us any time with a packing question.</p>",
            "es": "<p>Lleva en la mano tus documentos, medicamentos y básicos del primer día, empaca ropa casual y un "
                  "atuendo más elegante, trae las cosas pequeñas que los barcos no ofrecen, y deja en casa los "
                  "artículos prohibidos. Haz eso y el embarque es pan comido.</p>"
                  "<p>¿Nuevo en esto? Lee " + link("/es/guides/first-time-cruisers/", "la guía para primer crucero") +
                  " a continuación, y llámanos cuando quieras con una duda de equipaje.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("What should I pack in my cruise carry-on?", "Anything you need before your checked luggage reaches the cabin: travel documents and ID, all medications in their original packaging, swimwear and a change of clothes, chargers and a power bank. Never check your passport or medication."),
            ("What is the dress code on a cruise?", "Days are casual (resort wear and swimwear). Evenings are smart-casual, and many ships hold one or two dressier or formal nights on a weeklong cruise. Codes vary by line and ship, so confirm what your sailing does."),
            ("What is not allowed on a cruise?", "Most lines prohibit irons and steamers, surge-protector power strips, candles, sharp objects, and often drones and hoverboards. Alcohol limits vary by line. Check the line's prohibited-items list before you pack."),
            ("Do cruise cabins have enough electrical outlets?", "Usually only a few, so a power bank and a non-surge USB charging strip (if your line allows it) are worth packing. Do not bring surge-protected power strips, they are commonly banned."),
            ("Should I pack a formal outfit for a cruise?", "If your ship holds a formal or smarter night and you want to take part, yes, pack one dressier option. Otherwise smart-casual evening wear is plenty. Confirm your sailing's dress nights before you decide."),
        ],
        "es": [
            ("¿Qué llevo en el equipaje de mano de un crucero?", "Lo que necesites antes de que tu maleta llegue al camarote: documentos e identificación, todos los medicamentos en su empaque original, traje de baño y una muda, cargadores y una batería portátil. Nunca factures tu pasaporte ni tus medicamentos."),
            ("¿Cuál es el código de vestimenta en un crucero?", "Los días son casuales (ropa de resort y traje de baño). Las noches son smart-casual, y muchos barcos tienen una o dos noches más elegantes o de gala en un crucero de una semana. Los códigos varían por línea y barco, así que confirma qué hace tu crucero."),
            ("¿Qué no se permite en un crucero?", "La mayoría de líneas prohíben planchas y vaporizadores, regletas con supresor de picos, velas, objetos afilados, y a menudo drones y hoverboards. Los límites de alcohol varían por línea. Revisa la lista de artículos prohibidos antes de empacar."),
            ("¿Los camarotes tienen suficientes enchufes?", "Normalmente solo unos pocos, así que vale la pena llevar una batería portátil y una regleta USB sin supresor (si tu línea lo permite). No lleves regletas con supresor de picos, suelen estar prohibidas."),
            ("¿Debo empacar ropa formal para un crucero?", "Si tu barco tiene una noche de gala o más elegante y quieres participar, sí, empaca una opción más elegante. Si no, la ropa de noche smart-casual es suficiente. Confirma las noches de vestimenta de tu crucero antes de decidir."),
        ],
    },
    "related": {
        "en": [
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "Everything else nobody tells you before your first sailing."),
            ("🛂", "Cruise documents & ID", "/en/guides/cruise-documents-id/", "The paperwork that must be in your carry-on."),
            ("🚢", "Cruise embarkation day", "/en/guides/cruise-embarkation-day/", "What actually happens when you board."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Call us with any packing or dress-code question."),
        ],
        "es": [
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "Todo lo demás que nadie te dice antes de tu primer crucero."),
            ("🛂", "Documentos e identificación", "/es/guides/cruise-documents-id/", "El papeleo que debe ir en tu equipaje de mano."),
            ("🚢", "Día de embarque", "/es/guides/cruise-embarkation-day/", "Qué pasa realmente cuando embarcas."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Llámanos con cualquier duda de equipaje o vestimenta."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("cruise-embarkation-day", {
    "cat": "planning", "hero": "cruise-port.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "Cruise embarkation day: what to expect, step by step", "es": "Día de embarque: qué esperar, paso a paso"},
    "dek": {
        "en": "The first day sets the tone for the whole cruise. Know the flow of embarkation, from "
              "arriving at the terminal to your first lunch on board, and you skip the stress and start "
              "your holiday the moment you step on the ship.",
        "es": "El primer día marca el tono de todo el crucero. Conoce el flujo del embarque, de llegar a "
              "la terminal a tu primer almuerzo a bordo, y te ahorras el estrés y empiezas tus "
              "vacaciones en cuanto pisas el barco.",
    },
    "takeaways": {
        "en": [
            "Check in online before you travel and book an arrival time slot if your line offers one; it speeds everything up.",
            "Arrive in the assigned window, not hours early; too early often just means a longer wait.",
            "Your checked bags are dropped at the terminal and delivered to your cabin later, so keep essentials with you.",
            "Security and check-in are like an airport, then you board, cabins usually open a little later in the afternoon.",
            "Do not miss the muster drill (the mandatory safety briefing) or the all-aboard time before the ship sails.",
        ],
        "es": [
            "Haz el check-in en línea antes de viajar y reserva una franja de llegada si tu línea la ofrece; acelera todo.",
            "Llega en la ventana asignada, no horas antes; demasiado temprano suele significar solo una espera más larga.",
            "Tus maletas facturadas se dejan en la terminal y se entregan al camarote más tarde, así que lleva lo esencial contigo.",
            "La seguridad y el check-in son como un aeropuerto, luego embarcas, los camarotes suelen abrir un poco más tarde por la tarde.",
            "No te pierdas el simulacro de seguridad (obligatorio) ni la hora de all-aboard antes de que el barco zarpe.",
        ],
    },
    "sections": [
        {"id": "before", "h2": {"en": "Before you arrive", "es": "Antes de llegar"},
         "html": {
            "en": "<p>Most of embarkation day is won in advance. In the weeks before you sail, complete <b>online "
                  "check-in</b>: upload your documents and photo, add payment for your onboard account, and, on many "
                  "lines, choose an <b>arrival time slot</b>. That slot is your friend, it staggers the crowd so you "
                  "are not queueing for an hour.</p>"
                  + tip("Plan to be in the embarkation city the night before if you are flying in. A delayed flight is the most common reason people miss the ship, and it does not wait."),
            "es": "<p>La mayor parte del día de embarque se gana con anticipación. En las semanas previas, completa el "
                  "<b>check-in en línea</b>: sube tus documentos y foto, añade el pago de tu cuenta a bordo y, en muchas "
                  "líneas, elige una <b>franja de llegada</b>. Esa franja es tu amiga, escalona a la gente para que no "
                  "hagas fila una hora.</p>"
                  + tip("Planea estar en la ciudad de embarque la noche anterior si llegas en avión. Un vuelo retrasado es la razón más común por la que la gente pierde el barco, y este no espera."),
         }},
        {"id": "at-terminal", "h2": {"en": "At the terminal", "es": "En la terminal"},
         "html": {
            "en": vcards([
                ("🧳", "Drop your bags", "Porters take your checked luggage at the terminal; it is delivered to your cabin later. Tag it with your cabin number first."),
                ("🛂", "Check in & security", "Show documents, get your key card, and pass an airport-style security screening."),
                ("🚢", "Board the ship", "Walk aboard and you are on holiday. Cabins often open a little later, so explore, grab lunch, and settle in."),
            ]) + "<p>Keep your carry-on with the essentials on you until your bags arrive, and enjoy the ship straight "
            "away. There is no need to wait by your cabin door.</p>",
            "es": vcards([
                ("🧳", "Deja tus maletas", "Los maleteros toman tu equipaje facturado en la terminal; se entrega al camarote más tarde. Etiquétalo con tu número de camarote primero."),
                ("🛂", "Check-in y seguridad", "Muestra documentos, recibe tu tarjeta llave y pasa un control de seguridad tipo aeropuerto."),
                ("🚢", "Embarca", "Sube al barco y ya estás de vacaciones. Los camarotes suelen abrir un poco más tarde, así que explora, almuerza e instálate."),
            ]) + "<p>Mantén contigo tu equipaje de mano con lo esencial hasta que lleguen tus maletas, y disfruta el "
            "barco de inmediato. No hace falta esperar junto a la puerta del camarote.</p>",
         }},
        {"id": "onboard", "h2": {"en": "Your first hours on board", "es": "Tus primeras horas a bordo"},
         "html": {
            "en": "<ul>"
                  "<li><b>Lunch is served</b> as soon as you board, usually at the buffet, a great first stop.</li>"
                  "<li><b>Explore the ship</b> while it is quiet, find your dining room, the pools and the theatre.</li>"
                  "<li><b>The muster drill</b> is a short, mandatory safety briefing before sailaway. On most lines you "
                  "watch a video and check in at your station via the app or in person. Do not skip it.</li>"
                  "<li><b>Sailaway</b> is the fun part, head to an open deck as the ship leaves port.</li>"
                  "</ul>"
                  + watch("Note the all-aboard time (usually 30 to 60 minutes before departure) and never be late back to the ship on port days either, it will sail without you."),
            "es": "<ul>"
                  "<li><b>El almuerzo se sirve</b> en cuanto embarcas, normalmente en el bufé, una gran primera parada.</li>"
                  "<li><b>Explora el barco</b> mientras está tranquilo, encuentra tu comedor, las piscinas y el teatro.</li>"
                  "<li><b>El simulacro de seguridad</b> es una breve sesión obligatoria antes de zarpar. En la mayoría "
                  "de líneas ves un video y te registras en tu estación por la app o en persona. No te lo saltes.</li>"
                  "<li><b>El sailaway</b> es la parte divertida, ve a una cubierta abierta cuando el barco deja el "
                  "puerto.</li>"
                  "</ul>"
                  + watch("Anota la hora de all-aboard (normalmente 30 a 60 minutos antes de zarpar) y nunca llegues tarde al barco en los días de puerto tampoco, zarpará sin ti."),
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>Check in online, arrive in your window, hand off your bags, and walk aboard into lunch. Do the "
                  "muster drill, watch the sailaway, and your cruise is off to a relaxed start.</p>"
                  "<p>First cruise? Pair this with " + link("/en/guides/what-to-pack-for-a-cruise/", "what to pack") +
                  " and " + link("/en/guides/first-time-cruisers/", "the first-time cruiser guide") + ".</p>",
            "es": "<p>Haz el check-in en línea, llega en tu franja, entrega tus maletas y sube a almorzar. Haz el "
                  "simulacro, mira el sailaway, y tu crucero arranca relajado.</p>"
                  "<p>¿Primer crucero? Combina esto con " + link("/es/guides/what-to-pack-for-a-cruise/", "qué llevar") +
                  " y " + link("/es/guides/first-time-cruisers/", "la guía para primer crucero") + ".</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("What time should I arrive for cruise embarkation?", "Arrive within the check-in time slot your line assigns, not hours early. Turning up too early usually just means a longer wait; the staggered slots exist to keep boarding smooth."),
            ("How does cruise check-in work?", "Complete online check-in in advance (documents, photo, payment). At the terminal you drop your checked bags, show your documents, collect your key card, and pass an airport-style security screening, then you board."),
            ("When can I get into my cabin on embarkation day?", "Cabins usually open a little later in the afternoon, not the moment you board. Keep your carry-on with you, enjoy lunch and explore the ship in the meantime; your checked bags arrive at the cabin later too."),
            ("What is the muster drill?", "A short, mandatory safety briefing before the ship sails. On most lines you watch a safety video and check in at your assigned station via the app or in person. Every guest must complete it."),
            ("What happens if I am late for the ship?", "The ship sails at its scheduled time and does not wait, on embarkation day or at ports. Note the all-aboard time (usually 30 to 60 minutes before departure) and always allow a buffer."),
        ],
        "es": [
            ("¿A qué hora debo llegar para el embarque?", "Llega dentro de la franja de check-in que tu línea asigna, no horas antes. Llegar muy temprano suele significar solo una espera más larga; las franjas escalonadas existen para que el embarque sea fluido."),
            ("¿Cómo funciona el check-in del crucero?", "Completa el check-in en línea con anticipación (documentos, foto, pago). En la terminal dejas tus maletas facturadas, muestras documentos, recoges tu tarjeta llave y pasas un control de seguridad tipo aeropuerto, luego embarcas."),
            ("¿Cuándo puedo entrar a mi camarote el día de embarque?", "Los camarotes suelen abrir un poco más tarde por la tarde, no en cuanto embarcas. Mantén contigo tu equipaje de mano, disfruta el almuerzo y explora el barco mientras tanto; tus maletas facturadas llegan al camarote después."),
            ("¿Qué es el simulacro de seguridad (muster drill)?", "Una breve sesión de seguridad obligatoria antes de que el barco zarpe. En la mayoría de líneas ves un video de seguridad y te registras en tu estación asignada por la app o en persona. Todo huésped debe completarlo."),
            ("¿Qué pasa si llego tarde al barco?", "El barco zarpa a su hora programada y no espera, ni el día de embarque ni en los puertos. Anota la hora de all-aboard (normalmente 30 a 60 minutos antes de zarpar) y deja siempre un margen."),
        ],
    },
    "related": {
        "en": [
            ("🧳", "What to pack for a cruise", "/en/guides/what-to-pack-for-a-cruise/", "The carry-on and cabin checklist for day one."),
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "The big picture for your first sailing."),
            ("🛂", "Cruise documents & ID", "/en/guides/cruise-documents-id/", "What you need at the terminal to board."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Questions about your embarkation day? Just call."),
        ],
        "es": [
            ("🧳", "Qué llevar a un crucero", "/es/guides/what-to-pack-for-a-cruise/", "La lista de equipaje de mano y camarote para el primer día."),
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "El panorama completo para tu primer crucero."),
            ("🛂", "Documentos e identificación", "/es/guides/cruise-documents-id/", "Lo que necesitas en la terminal para embarcar."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "¿Dudas sobre tu día de embarque? Solo llama."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("first-time-cruisers", {
    "cat": "planning", "hero": "cruise-deck.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "First-time cruiser guide: everything nobody tells you", "es": "Guía para primer crucero: todo lo que nadie te dice"},
    "dek": {
        "en": "Your first cruise is easier than it looks once you know how it works. Here is the whole "
              "picture, from what your fare covers to boarding day, dining, ports and the handful of "
              "things that trip newcomers up, so you sail relaxed and confident.",
        "es": "Tu primer crucero es más fácil de lo que parece una vez que sabes cómo funciona. Aquí "
              "está el panorama completo, de lo que cubre tu tarifa al día de embarque, la comida, los "
              "puertos y las pocas cosas que confunden a los nuevos, para que navegues relajado.",
    },
    "takeaways": {
        "en": [
            "Your fare covers your cabin, most dining, entertainment and the sailing itself; drinks, Wi-Fi, specialty dining and excursions are extra.",
            "A daily gratuity is added automatically, per guest per day; budget for it from the start.",
            "Get your documents right: a passport is safest, and names must match your booking exactly.",
            "On boarding day, check in online, arrive in your time slot, and keep essentials in a carry-on until your bags arrive.",
            "Book what sells out (specialty dining, popular excursions, spa) early; the rest you can decide on board.",
        ],
        "es": [
            "Tu tarifa cubre el camarote, la mayoría de la comida, el entretenimiento y la navegación; bebidas, Wi-Fi, restaurantes de especialidad y excursiones son aparte.",
            "Se añade una propina diaria automáticamente, por huésped y por día; presupuéstala desde el principio.",
            "Ten bien tus documentos: un pasaporte es lo más seguro, y los nombres deben coincidir exactamente con tu reserva.",
            "El día de embarque, haz el check-in en línea, llega en tu franja, y guarda lo esencial en un equipaje de mano hasta que lleguen tus maletas.",
            "Reserva pronto lo que se agota (restaurantes de especialidad, excursiones populares, spa); el resto lo decides a bordo.",
        ],
    },
    "sections": [
        {"id": "how-it-works", "h2": {"en": "How a cruise actually works", "es": "Cómo funciona un crucero"},
         "html": {
            "en": "<p>A cruise is a floating hotel that moves between destinations while you sleep. One fare bundles "
                  "your room, most of your food, the entertainment and the transport between ports, so you unpack once "
                  "and wake up somewhere new. The extras (drinks, Wi-Fi, specialty restaurants, shore excursions) are "
                  "optional add-ons billed to your onboard account.</p>"
                  + tip("The single most useful thing to learn first is the split between what your fare includes and "
                        "what costs extra. Read " + link("/en/guides/whats-included/", "what is included in a cruise fare") +
                        " and you are already ahead of most first-timers."),
            "es": "<p>Un crucero es un hotel flotante que se mueve entre destinos mientras duermes. Una tarifa reúne tu "
                  "habitación, la mayoría de tu comida, el entretenimiento y el transporte entre puertos, así que "
                  "desempacas una vez y amaneces en un lugar nuevo. Los extras (bebidas, Wi-Fi, restaurantes de "
                  "especialidad, excursiones) son opcionales y se cargan a tu cuenta a bordo.</p>"
                  + tip("Lo más útil que puedes aprender primero es la diferencia entre lo que incluye tu tarifa y lo "
                        "que cuesta aparte. Lee " + link("/es/guides/whats-included/", "qué incluye la tarifa de un crucero") +
                        " y ya vas por delante de la mayoría de primerizos."),
         }},
        {"id": "before-you-go", "h2": {"en": "Before you go: money and documents", "es": "Antes de ir: dinero y documentos"},
         "html": {
            "en": vcards([
                ("🧾", "Gratuities", "A daily service charge, automatic, per guest. Prepay it to keep your onboard account tidy. See the gratuities guide."),
                ("🪪", "Documents", "A passport is safest; on some closed-loop US sailings a birth certificate plus ID works. Names must match your booking."),
                ("📆", "Payment timeline", "A deposit holds your cabin; the balance is due by the final-payment date. Do not miss it."),
                ("🛡️", "Insurance", "Worth considering for non-refundable bookings and hurricane season."),
            ]) + "<p>Two guides cover the details: " + link("/en/guides/cruise-documents-id/", "cruise documents & ID") +
            " and " + link("/en/guides/cruise-deposit-payment-cancellation/", "deposits, payment & cancellation") + ".</p>",
            "es": vcards([
                ("🧾", "Propinas", "Un cargo por servicio diario, automático, por huésped. Págalo por adelantado para mantener tu cuenta ordenada. Ve la guía de propinas."),
                ("🪪", "Documentos", "Un pasaporte es lo más seguro; en algunos cruceros closed-loop de EE.UU. sirve un acta de nacimiento más identificación. Los nombres deben coincidir."),
                ("📆", "Calendario de pago", "Un depósito reserva tu camarote; el saldo vence en la fecha de pago final. No la pierdas."),
                ("🛡️", "Seguro", "Vale considerarlo en reservas no reembolsables y temporada de huracanes."),
            ]) + "<p>Dos guías cubren los detalles: " + link("/es/guides/cruise-documents-id/", "documentos e identificación") +
            " y " + link("/es/guides/cruise-deposit-payment-cancellation/", "depósitos, pago y cancelación") + ".</p>",
         }},
        {"id": "boarding-day", "h2": {"en": "Boarding day and life on board", "es": "Día de embarque y vida a bordo"},
         "html": {
            "en": "<p>Check in online before you travel, arrive at the terminal in your assigned window, hand your "
                  "checked bags to the porters, and walk aboard into lunch. Cabins usually open a little later, so "
                  "explore the ship, then do the short mandatory safety drill before sailaway.</p>"
                  "<p>Onboard, days are casual and evenings a little smarter. You will find a main dining room, a "
                  "buffet, pools, shows and kids' clubs all included. The full step-by-step is in "
                  + link("/en/guides/cruise-embarkation-day/", "cruise embarkation day") + ", and "
                  + link("/en/guides/what-to-pack-for-a-cruise/", "what to pack") + " gets your bags right.</p>",
            "es": "<p>Haz el check-in en línea antes de viajar, llega a la terminal en tu franja asignada, entrega tus "
                  "maletas a los maleteros y sube a almorzar. Los camarotes suelen abrir un poco más tarde, así que "
                  "explora el barco y luego haz el breve simulacro de seguridad obligatorio antes de zarpar.</p>"
                  "<p>A bordo, los días son casuales y las noches un poco más elegantes. Encontrarás comedor principal, "
                  "bufé, piscinas, espectáculos y clubes infantiles, todo incluido. El paso a paso está en "
                  + link("/es/guides/cruise-embarkation-day/", "día de embarque") + ", y "
                  + link("/es/guides/what-to-pack-for-a-cruise/", "qué llevar") + " deja tus maletas listas.</p>",
         }},
        {"id": "ports", "h2": {"en": "Ports, excursions and sea days", "es": "Puertos, excursiones y días de mar"},
         "html": {
            "en": "<p>Some days you are in port, some are relaxing sea days. In port you can take a line-run shore "
                  "excursion (convenient, and the ship waits for its own tours) or explore independently. Always note "
                  "the all-aboard time; the ship sails without latecomers.</p>"
                  + watch("On port days, the ship leaves at its posted all-aboard time and will not wait if you are exploring on your own. Give yourself a generous buffer to get back."),
            "es": "<p>Algunos días estás en puerto, otros son días de mar para relajarte. En puerto puedes tomar una "
                  "excursión de la línea (cómoda, y el barco espera a sus propios tours) o explorar por tu cuenta. "
                  "Anota siempre la hora de all-aboard; el barco zarpa sin los que llegan tarde.</p>"
                  + watch("En los días de puerto, el barco sale a la hora de all-aboard publicada y no espera si exploras por tu cuenta. Date un margen amplio para volver."),
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>Learn the fare-versus-extras split, sort your documents and payment dates, arrive prepared on "
                  "boarding day, and respect the all-aboard time. Do that and your first cruise runs like clockwork.</p>"
                  "<p>Nervous about any of it? That is exactly what a specialist is for: they walk you through your "
                  "specific ship and sailing, in one call, free and with no obligation.</p>",
            "es": "<p>Aprende la diferencia entre tarifa y extras, arregla tus documentos y fechas de pago, llega "
                  "preparado el día de embarque, y respeta la hora de all-aboard. Haz eso y tu primer crucero funciona "
                  "a la perfección.</p>"
                  "<p>¿Te pone nervioso algo? Para eso está un especialista: te guía por tu barco y crucero "
                  "específicos, en una llamada, gratis y sin compromiso.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("Is a cruise good for first-timers?", "Yes. A cruise is one of the easiest holidays for beginners: you unpack once, most of your food and entertainment is included, and everything is in one place. Warm, short itineraries like the Caribbean or Bahamas are ideal for a first sailing."),
            ("What is included in a first cruise?", "Your cabin, main dining and the buffet, daytime activities, most entertainment and kids' clubs, and the sailing itself. Drinks, Wi-Fi, specialty restaurants, shore excursions, the spa and photos are extra."),
            ("Do I need a passport for my first cruise?", "A passport is the safest choice and is required for most sailings that begin or end abroad. On many closed-loop US cruises a birth certificate plus photo ID works, but a passport removes all risk. Names must match your booking exactly."),
            ("How much should I budget beyond the fare?", "Plan for the near-universal extras: daily gratuities, drinks, Wi-Fi and any shore excursions, plus getting to the port. Decide on packages before you sail and set an onboard spending number."),
            ("What should I book before I sail versus on board?", "Book anything that sells out early, popular specialty restaurants, in-demand shore excursions and spa slots, before you sail. Casual dining, most activities and relaxing can wait until you are on board."),
        ],
        "es": [
            ("¿Un crucero es bueno para primerizos?", "Sí. Un crucero es una de las vacaciones más fáciles para principiantes: desempacas una vez, la mayoría de tu comida y entretenimiento está incluido, y todo está en un lugar. Itinerarios cálidos y cortos como el Caribe o Bahamas son ideales para el primero."),
            ("¿Qué incluye un primer crucero?", "Tu camarote, comedor principal y bufé, actividades de día, la mayoría del entretenimiento y clubes infantiles, y la navegación. Bebidas, Wi-Fi, restaurantes de especialidad, excursiones, spa y fotos son aparte."),
            ("¿Necesito pasaporte para mi primer crucero?", "Un pasaporte es lo más seguro y se exige en la mayoría de cruceros que empiezan o terminan en el extranjero. En muchos cruceros closed-loop de EE.UU. sirve un acta más identificación, pero el pasaporte elimina el riesgo. Los nombres deben coincidir con tu reserva."),
            ("¿Cuánto debo presupuestar además de la tarifa?", "Planea los extras casi universales: propinas diarias, bebidas, Wi-Fi y excursiones, más llegar al puerto. Decide los paquetes antes de zarpar y fija un monto de gasto a bordo."),
            ("¿Qué reservo antes de zarpar y qué a bordo?", "Reserva antes lo que se agota: restaurantes de especialidad populares, excursiones muy demandadas y citas de spa. La comida informal, la mayoría de actividades y relajarte pueden esperar hasta estar a bordo."),
        ],
    },
    "related": {
        "en": [
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "The first thing every new cruiser should read."),
            ("🧳", "What to pack for a cruise", "/en/guides/what-to-pack-for-a-cruise/", "The carry-on and cabin checklist."),
            ("🛳️", "Cruise embarkation day", "/en/guides/cruise-embarkation-day/", "Exactly what happens on day one."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us you're new; we'll match an easy first sailing."),
        ],
        "es": [
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Lo primero que todo nuevo crucerista debe leer."),
            ("🧳", "Qué llevar a un crucero", "/es/guides/what-to-pack-for-a-cruise/", "La lista de equipaje de mano y camarote."),
            ("🛳️", "Día de embarque", "/es/guides/cruise-embarkation-day/", "Exactamente qué pasa el primer día."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos que eres nuevo; emparejamos un primer crucero fácil."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("choosing-a-cabin", {
    "cat": "planning", "hero": "cruise-cabin.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "Choosing a cruise cabin: interior to suite, explained", "es": "Elegir camarote: de interior a suite, explicado"},
    "dek": {
        "en": "Your cabin is the one choice that shapes both your budget and your comfort. Here is what "
              "each type gives you, who each suits, the locations to seek out and the ones to avoid, so "
              "you pick the right room the first time.",
        "es": "Tu camarote es la decisión que más moldea tu presupuesto y tu comodidad. Aquí verás qué "
              "te da cada tipo, para quién es cada uno, las ubicaciones a buscar y las que evitar, para "
              "que elijas la habitación correcta a la primera.",
    },
    "takeaways": {
        "en": [
            "Four main types: interior (no window), oceanview (window), balcony (private veranda) and suite (space plus perks).",
            "Interiors are the best value and you spend little waking time in the room; balconies are the popular sweet spot for the view.",
            "Location matters: midship is steadiest, higher decks are handier for pools, and cabins near lifts or under busy venues can be noisier.",
            "A guarantee cabin (you pick the category, the line assigns the room) can come at a friendlier fare in exchange for less control.",
            "Match the cabin to how you travel: how much time you'll spend in the room, motion sensitivity, and budget.",
        ],
        "es": [
            "Cuatro tipos principales: interior (sin ventana), vista al mar (ventana), balcón (veranda privada) y suite (espacio y beneficios).",
            "Los interiores son el mejor valor y pasas poco tiempo despierto en la habitación; los balcones son el punto ideal popular por la vista.",
            "La ubicación importa: el centro del barco es el más estable, las cubiertas altas están cerca de las piscinas, y los camarotes junto a ascensores o bajo lugares concurridos pueden ser más ruidosos.",
            "Un camarote garantizado (eliges la categoría, la línea asigna la habitación) puede tener una tarifa más amable a cambio de menos control.",
            "Ajusta el camarote a cómo viajas: cuánto tiempo pasarás en la habitación, sensibilidad al movimiento y presupuesto.",
        ],
    },
    "sections": [
        {"id": "types", "h2": {"en": "The four cabin types", "es": "Los cuatro tipos de camarote"},
         "html": {
            "en": vcards([
                ("🛏️", "Interior", "No window, the most budget-friendly room. Great if you treat the cabin as a place to sleep and shower."),
                ("🪟", "Oceanview", "A window or porthole for natural light and a sea view, without a balcony's price."),
                ("🌅", "Balcony", "A private veranda, the popular sweet spot: your own outdoor space and morning coffee with a view."),
                ("🛎️", "Suite", "The most space, plus perks that vary by line (priority boarding, a lounge, concierge, better location)."),
            ]) + "<p>Use the interactive breakdown below to compare them side by side, then read on for how to pick a "
            "good location.</p>",
            "es": vcards([
                ("🛏️", "Interior", "Sin ventana, la habitación más económica. Ideal si usas el camarote solo para dormir y ducharte."),
                ("🪟", "Vista al mar", "Una ventana u ojo de buey para luz natural y vista al mar, sin el precio de un balcón."),
                ("🌅", "Balcón", "Una veranda privada, el punto ideal popular: tu propio espacio al aire libre y el café de la mañana con vista."),
                ("🛎️", "Suite", "El mayor espacio, más beneficios que varían por línea (embarque prioritario, salón, conserjería, mejor ubicación)."),
            ]) + "<p>Usa el desglose interactivo de abajo para compararlos, y luego sigue leyendo para elegir una buena "
            "ubicación.</p>",
         }},
        {"id": "location", "h2": {"en": "Location: the cabins to seek and avoid", "es": "Ubicación: los camarotes a buscar y evitar"},
         "html": {
            "en": "<p>Two cabins of the same type can feel very different depending on where they sit:</p>"
                  "<ul>"
                  "<li><b>Midship</b> is the steadiest spot in any motion, and central for getting around, a smart pick if you are prone to seasickness.</li>"
                  "<li><b>Higher decks</b> are handy for pools and buffet; <b>lower decks</b> feel the least motion and are often gentler on the wallet.</li>"
                  "<li><b>Avoid</b> cabins directly above or below busy venues (theatres, nightclubs, the pool deck), and rooms right by the lifts, which can be noisier.</li>"
                  "<li><b>Check the deck plan</b> for anything obstructing a balcony view (lifeboats) or connecting-door cabins if you want quiet.</li>"
                  "</ul>"
                  + tip("A guarantee cabin gives the line the final say on your exact room in exchange for a friendlier fare. Fine for flexible travellers; avoid it if location is critical to you."),
            "es": "<p>Dos camarotes del mismo tipo pueden sentirse muy distintos según dónde estén:</p>"
                  "<ul>"
                  "<li>El <b>centro del barco</b> es el punto más estable ante cualquier movimiento, y central para moverte, una elección inteligente si te mareas.</li>"
                  "<li>Las <b>cubiertas altas</b> están cerca de piscinas y bufé; las <b>bajas</b> sienten menos movimiento y suelen ser más suaves para el bolsillo.</li>"
                  "<li><b>Evita</b> camarotes justo encima o debajo de lugares concurridos (teatros, discotecas, la cubierta de piscina), y las habitaciones junto a los ascensores, que pueden ser más ruidosas.</li>"
                  "<li><b>Revisa el plano de cubiertas</b> por si algo obstruye la vista del balcón (botes salvavidas) o por camarotes con puerta conectada si quieres tranquilidad.</li>"
                  "</ul>"
                  + tip("Un camarote garantizado deja a la línea la última palabra sobre tu habitación exacta a cambio de una tarifa más amable. Bien para viajeros flexibles; evítalo si la ubicación es crítica para ti."),
         }},
        {"id": "which-for-you", "h2": {"en": "Which cabin is right for you?", "es": "¿Qué camarote es para ti?"},
         "html": {
            "en": "<p>Answer honestly: how much waking time will you spend in the room?</p>"
                  "<ul>"
                  "<li><b>Barely any?</b> An interior stretches your budget furthest, and you will not miss the window.</li>"
                  "<li><b>Some downtime and love a view?</b> A balcony is the classic sweet spot and the most popular choice.</li>"
                  "<li><b>Want light without the balcony price?</b> An oceanview splits the difference.</li>"
                  "<li><b>Celebrating, or want space and perks?</b> A suite delivers, especially for families or a special trip.</li>"
                  "</ul>"
                  "<p>Budget-focused? See " + link("/en/guides/how-to-find-affordable-cruise/", "how to find an affordable cruise") +
                  "; the cabin choice is one of the biggest levers.</p>",
            "es": "<p>Responde con honestidad: ¿cuánto tiempo despierto pasarás en la habitación?</p>"
                  "<ul>"
                  "<li><b>¿Casi nada?</b> Un interior estira más tu presupuesto, y no extrañarás la ventana.</li>"
                  "<li><b>¿Algo de descanso y te encanta la vista?</b> Un balcón es el punto ideal clásico y la opción más popular.</li>"
                  "<li><b>¿Quieres luz sin el precio del balcón?</b> Una vista al mar es el punto medio.</li>"
                  "<li><b>¿Celebras, o quieres espacio y beneficios?</b> Una suite cumple, sobre todo para familias o un viaje especial.</li>"
                  "</ul>"
                  "<p>¿Te enfocas en el presupuesto? Ve " + link("/es/guides/how-to-find-affordable-cruise/", "cómo encontrar un crucero accesible") +
                  "; la elección de camarote es una de las mayores palancas.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("Is a balcony cabin worth it on a cruise?", "For many people, yes, a balcony is the popular sweet spot, giving you private outdoor space and a view for a moderate step up from an oceanview. If you will barely be in the room, an interior saves more; on scenic itineraries like Alaska, a balcony shines."),
            ("What is the most affordable cruise cabin?", "An interior stateroom, with no window, is the most budget-friendly. Since you spend little waking time in the cabin, it is the choice that stretches the trip budget the furthest."),
            ("What is a guarantee cabin?", "You choose the cabin category and the cruise line assigns your exact room later, often at a friendlier fare in exchange for less control over the location. Good for flexible travellers, not ideal if a specific spot matters."),
            ("Which deck is best for a cruise cabin?", "Midship cabins feel the steadiest and are central for getting around, ideal if you are prone to seasickness. Higher decks are handy for pools; lower decks feel the least motion. Avoid rooms directly above or below busy venues."),
            ("How do I avoid a noisy cabin?", "Check the deck plan and steer clear of cabins directly above or below theatres, nightclubs and the pool deck, and rooms right beside the lifts. Midship, mid-deck cabins between other cabins are usually the quietest."),
        ],
        "es": [
            ("¿Vale la pena un camarote con balcón?", "Para muchos, sí, un balcón es el punto ideal popular, con espacio privado al aire libre y vista por un paso moderado sobre la vista al mar. Si casi no estarás en la habitación, un interior ahorra más; en itinerarios escénicos como Alaska, un balcón brilla."),
            ("¿Cuál es el camarote más económico?", "Un camarote interior, sin ventana, es el más económico. Como pasas poco tiempo despierto en el camarote, es la opción que más estira el presupuesto del viaje."),
            ("¿Qué es un camarote garantizado?", "Eliges la categoría y la línea asigna tu habitación exacta después, a menudo con una tarifa más amable a cambio de menos control sobre la ubicación. Bien para viajeros flexibles, no ideal si un lugar específico importa."),
            ("¿Qué cubierta es mejor para el camarote?", "Los camarotes del centro sienten el menor movimiento y son centrales para moverte, ideales si te mareas. Las cubiertas altas están cerca de las piscinas; las bajas sienten menos movimiento. Evita habitaciones justo encima o debajo de lugares concurridos."),
            ("¿Cómo evito un camarote ruidoso?", "Revisa el plano y evita camarotes justo encima o debajo de teatros, discotecas y la cubierta de piscina, y habitaciones junto a los ascensores. Los camarotes del centro, en cubierta media y entre otros camarotes, suelen ser los más tranquilos."),
        ],
    },
    "related": {
        "en": [
            ("💰", "How to find an affordable cruise", "/en/guides/how-to-find-affordable-cruise/", "Cabin choice is one of the biggest budget levers."),
            ("🚢", "Big ship vs small ship", "/en/guides/big-ship-vs-small-ship/", "The ship you pick shapes the cabins on offer."),
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "Everything else for a smooth first sailing."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "We'll find the right cabin on the right ship for you."),
        ],
        "es": [
            ("💰", "Cómo encontrar un crucero accesible", "/es/guides/how-to-find-affordable-cruise/", "La elección de camarote es una de las mayores palancas de presupuesto."),
            ("🚢", "Barco grande vs pequeño", "/es/guides/big-ship-vs-small-ship/", "El barco que eliges moldea los camarotes disponibles."),
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "Todo lo demás para un primer crucero sin problemas."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Encontramos el camarote correcto en el barco correcto para ti."),
        ],
    },
})
