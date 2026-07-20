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
