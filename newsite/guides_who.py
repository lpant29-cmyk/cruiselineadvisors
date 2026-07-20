# -*- coding: utf-8 -*-
"""Rich guides cluster: who. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("solo-cruising", {
    "cat": "who",
    "hero": "cruise-balcony.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "Solo cruising & the single supplement, explained",
        "es": "Cruceros para solos y el suplemento individual, explicados",
    },
    "dek": {
        "en": "Cruising alone is one of the easiest ways to travel solo: safe, social if you want it, "
              "and everything is on one ship. The one thing to understand first is the single "
              "supplement, and how a growing number of ships now soften it.",
        "es": "Viajar solo en crucero es una de las formas más fáciles de hacerlo: seguro, social si "
              "quieres, y todo está en un barco. Lo primero a entender es el suplemento individual, y "
              "cómo cada vez más barcos lo suavizan.",
    },
    "takeaways": {
        "en": [
            "Cruise fares are usually priced per person based on two people sharing a cabin, so a solo traveller pays a 'single supplement' to cover the empty second berth.",
            "A growing number of ships offer dedicated solo studio cabins with no supplement, plus solo lounges and meet-ups.",
            "Solo cabins are limited and book up fast, so flexibility on ship and date helps a lot.",
            "Cruising solo is genuinely social if you want it: shared tables, solo mixers, group excursions, and easy if you do not.",
            "Which lines and ships have solo cabins is specific data; a specialist can point you straight to them.",
        ],
        "es": [
            "Las tarifas suelen fijarse por persona con base en dos personas compartiendo camarote, así que un viajero solo paga un 'suplemento individual' para cubrir la segunda cama vacía.",
            "Cada vez más barcos ofrecen camarotes estudio para solos sin suplemento, además de salones y encuentros para solos.",
            "Los camarotes para solos son limitados y se agotan rápido, así que la flexibilidad de barco y fecha ayuda mucho.",
            "Viajar solo en crucero es genuinamente social si quieres: mesas compartidas, encuentros para solos, excursiones en grupo, y fácil si prefieres estar solo.",
            "Qué líneas y barcos tienen camarotes para solos es un dato específico; un especialista puede llevarte directo a ellos.",
        ],
    },
    "sections": [
        {
            "id": "single-supplement",
            "h2": {"en": "The single supplement, in plain terms", "es": "El suplemento individual, en términos simples"},
            "html": {
                "en": define("Single supplement",
                             "an extra charge a solo traveller pays because cruise fares are usually quoted per person "
                             "assuming two people share the cabin. Sailing alone, you cover the 'missing' second person "
                             "so the line does not lose that berth's revenue.")
                      + "<p>It is not a penalty aimed at solo travellers so much as a side effect of how cabins are "
                      "priced. It varies by line, ship and sailing, and it is the single biggest factor in what a solo "
                      "cruise costs. The good news is there are real ways around it.</p>",
                "es": define("Suplemento individual",
                             "un cargo extra que paga un viajero solo porque las tarifas suelen cotizarse por persona "
                             "asumiendo que dos comparten el camarote. Al viajar solo, cubres a la segunda persona "
                             "'faltante' para que la línea no pierda los ingresos de esa cama.")
                      + "<p>No es tanto un castigo a los viajeros solos como un efecto secundario de cómo se fijan los "
                      "precios de los camarotes. Varía por línea, barco y crucero, y es el factor más grande en lo que "
                      "cuesta un crucero solo. La buena noticia es que hay formas reales de rodearlo.</p>",
            },
        },
        {
            "id": "studio-cabins",
            "h2": {"en": "Solo studio cabins and solo spaces", "es": "Camarotes estudio y espacios para solos"},
            "html": {
                "en": "<p>The best fix is a cabin designed for one. A growing number of ships include <b>solo studio "
                      "cabins</b>, real staterooms built for a single guest and priced without the supplement, often "
                      "clustered near a <b>solo lounge</b> with its own hosted get-togethers.</p>"
                      + vcards([
                          ("🛏️", "Studio cabins", "Purpose-built single rooms with no single supplement, so you pay one fair fare."),
                          ("🥂", "Solo lounges & mixers", "Dedicated spaces and hosted meet-ups make it easy to find company on day one."),
                          ("👥", "Group excursions & tables", "Shared dining tables and group tours mean you are only ever as social as you want to be."),
                      ])
                      + watch("Solo studios are limited in number and popular, so they sell out early. If one is your "
                              "goal, being flexible on ship and date, and booking ahead, makes all the difference."),
                "es": "<p>La mejor solución es un camarote diseñado para uno. Cada vez más barcos incluyen <b>camarotes "
                      "estudio para solos</b>, habitaciones reales para un solo huésped y con precio sin suplemento, a "
                      "menudo cerca de un <b>salón para solos</b> con sus propios encuentros organizados.</p>"
                      + vcards([
                          ("🛏️", "Camarotes estudio", "Habitaciones individuales hechas a propósito sin suplemento individual, así pagas una sola tarifa justa."),
                          ("🥂", "Salones y encuentros para solos", "Espacios dedicados y encuentros organizados facilitan encontrar compañía desde el primer día."),
                          ("👥", "Excursiones y mesas en grupo", "Las mesas compartidas y los tours en grupo hacen que seas tan social como quieras."),
                      ])
                      + watch("Los estudios para solos son limitados y populares, así que se agotan pronto. Si uno es "
                              "tu objetivo, ser flexible con barco y fecha, y reservar con anticipación, hace toda la "
                              "diferencia."),
            },
        },
        {
            "id": "is-it-social",
            "h2": {"en": "Is cruising alone lonely? (No, unless you want it)", "es": "¿Es solitario viajar solo? (No, salvo que quieras)"},
            "html": {
                "en": "<p>A ship is one of the friendliest places to travel solo. You are in a safe, self-contained "
                      "environment where meeting people is easy but never forced. Join a shared dinner table, drop into "
                      "a solo mixer, take a group shore excursion, or simply enjoy your own company on a quiet balcony. "
                      "The choice is yours, every single day.</p>",
                "es": "<p>Un barco es uno de los lugares más amigables para viajar solo. Estás en un entorno seguro y "
                      "autónomo donde conocer gente es fácil pero nunca obligatorio. Únete a una mesa compartida, pasa "
                      "por un encuentro para solos, toma una excursión en grupo, o simplemente disfruta de tu compañía "
                      "en un balcón tranquilo. La decisión es tuya, cada día.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>Solo cruising works beautifully once you understand the single supplement and how to sidestep "
                      "it, usually with a purpose-built studio cabin on a ship set up for solo travellers. Be flexible, "
                      "book ahead, and you get a safe, social trip on your own terms.</p>"
                      "<p>Want us to point you to the ships with solo cabins and solo lounges for your dates? Tell the "
                      + link("/en/compare/", "cruise finder") + " you are travelling solo, or just call and we will "
                      "line them up.</p>",
                "es": "<p>Los cruceros para solos funcionan de maravilla una vez que entiendes el suplemento individual "
                      "y cómo esquivarlo, normalmente con un camarote estudio en un barco preparado para viajeros solos. "
                      "Sé flexible, reserva con anticipación, y tendrás un viaje seguro y social en tus propios "
                      "términos.</p>"
                      "<p>¿Quieres que te señalemos los barcos con camarotes y salones para solos en tus fechas? Dile "
                      "al " + link("/es/compare/", "buscador de cruceros") + " que viajas solo, o simplemente llama y "
                      "los alineamos.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("What is a single supplement on a cruise?", "An extra charge a solo traveller pays because fares are usually quoted per person assuming two share the cabin. Sailing alone, you cover the empty second berth. It varies by line and sailing and is the biggest factor in a solo cruise's cost."),
            ("How do I avoid the single supplement?", "Book a dedicated solo studio cabin, which is priced for one guest with no supplement. These exist on a growing number of ships but are limited, so flexibility on ship and date, plus booking ahead, helps a lot."),
            ("Which cruise lines have solo cabins?", "Several lines now offer purpose-built studio cabins and solo lounges, and the list keeps growing. Which ships have them and when they sail your dates is exactly what a specialist can pin down for you."),
            ("Is cruising alone safe and social?", "Yes. A ship is a safe, self-contained environment, and it is easy to be as social as you like, shared tables, solo mixers and group excursions, or to keep to yourself. You choose each day."),
            ("Is solo cruising more expensive?", "It can be, because of the single supplement, but a solo studio cabin removes it, and being flexible on ship and date helps you find the best value. A specialist can find the options that work for a single traveller."),
        ],
        "es": [
            ("¿Qué es el suplemento individual en un crucero?", "Un cargo extra que paga un viajero solo porque las tarifas suelen cotizarse por persona asumiendo que dos comparten el camarote. Al viajar solo, cubres la segunda cama vacía. Varía por línea y crucero y es el factor más grande en el costo de un crucero solo."),
            ("¿Cómo evito el suplemento individual?", "Reserva un camarote estudio para solos, con precio para un huésped y sin suplemento. Existen en cada vez más barcos pero son limitados, así que la flexibilidad de barco y fecha, más reservar con anticipación, ayuda mucho."),
            ("¿Qué líneas tienen camarotes para solos?", "Varias líneas ofrecen ya camarotes estudio y salones para solos, y la lista sigue creciendo. Qué barcos los tienen y cuándo navegan en tus fechas es justo lo que un especialista puede precisar por ti."),
            ("¿Es seguro y social viajar solo en crucero?", "Sí. Un barco es un entorno seguro y autónomo, y es fácil ser tan social como quieras, mesas compartidas, encuentros para solos y excursiones en grupo, o mantenerte por tu cuenta. Tú eliges cada día."),
            ("¿Es más caro viajar solo en crucero?", "Puede serlo, por el suplemento individual, pero un camarote estudio para solos lo elimina, y ser flexible con barco y fecha ayuda a encontrar el mejor valor. Un especialista puede encontrar las opciones que funcionan para un viajero solo."),
        ],
    },
    "related": {
        "en": [
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell the finder you're solo and we'll surface the ships with studio cabins."),
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "How studio and interior cabins compare for a single traveller."),
            ("💰", "How to find an affordable cruise", "/en/guides/how-to-find-affordable-cruise/", "Extra tips for keeping a solo trip good value."),
            ("🚢", "How to choose a cruise line", "/en/guides/how-to-choose-a-cruise-line/", "Which lines are set up best for solo travellers."),
        ],
        "es": [
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dile al buscador que viajas solo y mostramos los barcos con camarotes estudio."),
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "Cómo se comparan los camarotes estudio e interiores para un viajero solo."),
            ("💰", "Cómo encontrar un crucero accesible", "/es/guides/how-to-find-affordable-cruise/", "Consejos extra para mantener un viaje solo con buen valor."),
            ("🚢", "Cómo elegir una línea de crucero", "/es/guides/how-to-choose-a-cruise-line/", "Qué líneas están mejor preparadas para viajeros solos."),
        ],
    },
})
