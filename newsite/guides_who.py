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


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("groups-and-families", {
    "cat": "who", "hero": "cruise-family.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "Cruising with groups & families: the complete guide", "es": "Cruceros con grupos y familias: la guía completa"},
    "dek": {
        "en": "A cruise is one of the easiest holidays for families and groups: everyone is together but "
              "free to do their own thing, and it is all pre-paid. Here is how to pick the right ship, "
              "link your cabins, sort dining and payments, and keep everyone happy.",
        "es": "Un crucero es una de las vacaciones más fáciles para familias y grupos: todos juntos pero "
              "libres de hacer lo suyo, y todo prepagado. Aquí te decimos cómo elegir el barco, conectar "
              "camarotes, organizar comidas y pagos, y tener a todos contentos.",
    },
    "takeaways": {
        "en": [
            "Big, activity-packed ships suit families and groups best: kids' clubs, family cabins and enough variety for every age.",
            "Ask about connecting or adjacent cabins early; they are limited and book up fast.",
            "Kids' clubs run by age band and are usually included by day; nurseries and late-night care can cost extra.",
            "Group dining can be arranged, one big table, a set time, so nobody eats alone.",
            "Payments can often be split across cabins, and a specialist coordinates the whole group in one call.",
        ],
        "es": [
            "Los barcos grandes y llenos de actividades convienen más a familias y grupos: clubes infantiles, camarotes familiares y variedad para cada edad.",
            "Pregunta pronto por camarotes conectados o contiguos; son limitados y se agotan rápido.",
            "Los clubes infantiles funcionan por bandas de edad y suelen estar incluidos de día; las guarderías y el cuidado nocturno pueden costar aparte.",
            "Se puede organizar comida en grupo, una mesa grande a una hora fija, para que nadie coma solo.",
            "Los pagos suelen poder dividirse entre camarotes, y un especialista coordina todo el grupo en una llamada.",
        ],
    },
    "sections": [
        {"id": "right-ship", "h2": {"en": "Picking the right ship", "es": "Elegir el barco correcto"},
         "html": {
            "en": "<p>For families and groups, a big, activity-packed ship usually wins. There is something for every "
                  "age all day, so a mixed group is never forced to do the same thing at the same time. Look for strong "
                  "kids' and teen clubs, family-sized cabins, and lots of included activity.</p>"
                  + tip("Not sure which line fits your crew? Read " + link("/en/guides/big-ship-vs-small-ship/", "big ship vs small ship") +
                        " and " + link("/en/guides/how-to-choose-a-cruise-line/", "how to choose a cruise line") + "."),
            "es": "<p>Para familias y grupos, un barco grande y lleno de actividades suele ganar. Hay algo para cada "
                  "edad todo el día, así que un grupo mixto nunca está obligado a hacer lo mismo al mismo tiempo. Busca "
                  "buenos clubes de niños y adolescentes, camarotes familiares y mucha actividad incluida.</p>"
                  + tip("¿No sabes qué línea encaja con tu grupo? Lee " + link("/es/guides/big-ship-vs-small-ship/", "barco grande vs pequeño") +
                        " y " + link("/es/guides/how-to-choose-a-cruise-line/", "cómo elegir una línea") + "."),
         }},
        {"id": "cabins", "h2": {"en": "Cabins: connecting, adjacent and family rooms", "es": "Camarotes: conectados, contiguos y familiares"},
         "html": {
            "en": vcards([
                ("🚪", "Connecting cabins", "Two rooms with an internal door, ideal for parents and kids. Limited in number, so book early."),
                ("↔️", "Adjacent cabins", "Rooms next door or across the hall keep the group close when connecting rooms are gone."),
                ("👨‍👩‍👧‍👦", "Family cabins & suites", "Larger rooms that sleep four or more, some with extra bathrooms or an in-room slide on newer ships."),
            ]) + "<p>Cabin location and configuration are exactly the phone-work a specialist handles, getting your rooms "
            "together before they sell out. Also read " + link("/en/guides/choosing-a-cabin/", "choosing a cabin") + ".</p>",
            "es": vcards([
                ("🚪", "Camarotes conectados", "Dos habitaciones con puerta interna, ideales para padres e hijos. Limitados, así que reserva pronto."),
                ("↔️", "Camarotes contiguos", "Habitaciones al lado o enfrente mantienen al grupo cerca cuando ya no hay conectados."),
                ("👨‍👩‍👧‍👦", "Camarotes familiares y suites", "Habitaciones más grandes para cuatro o más, algunas con baño extra o tobogán en barcos nuevos."),
            ]) + "<p>La ubicación y configuración de camarotes es justo el trabajo por teléfono que un especialista "
            "maneja, poniendo tus habitaciones juntas antes de que se agoten. También lee " + link("/es/guides/choosing-a-cabin/", "elegir camarote") + ".</p>",
         }},
        {"id": "kids-dining", "h2": {"en": "Kids' clubs and group dining", "es": "Clubes infantiles y comida en grupo"},
         "html": {
            "en": "<p><b>Kids' and teen clubs</b> are grouped by age and usually included during normal hours, giving "
                  "parents a break while children make friends. Infant nurseries and late-night care can carry an "
                  "hourly charge on some lines.</p>"
                  "<p><b>Group dining</b> is easy to arrange: ask for one large table at a set time so the whole party "
                  "eats together every evening. Specialty restaurants can host a group too, with notice.</p>",
            "es": "<p>Los <b>clubes de niños y adolescentes</b> se agrupan por edad y suelen estar incluidos en horario "
                  "normal, dando un respiro a los padres mientras los niños hacen amigos. Las guarderías para bebés y "
                  "el cuidado nocturno pueden tener un cargo por hora en algunas líneas.</p>"
                  "<p>La <b>comida en grupo</b> es fácil de organizar: pide una mesa grande a una hora fija para que "
                  "todo el grupo cene junto cada noche. Los restaurantes de especialidad también pueden recibir a un "
                  "grupo, con aviso.</p>",
         }},
        {"id": "payments", "h2": {"en": "Payments and coordination", "es": "Pagos y coordinación"},
         "html": {
            "en": "<p>The logistics are where a specialist earns their keep. Payments can often be <b>split across "
                  "cabins</b> so each family or couple settles their own, and one advisor can <b>coordinate the whole "
                  "group</b>, cabins together, dining booked, everyone on the same sailing, in a single call.</p>"
                  + tip("Organising a reunion, wedding group or multi-family trip? Tell us the group size and what "
                        "matters, and we handle the rest. That is exactly the kind of thing the phone call is for."),
            "es": "<p>La logística es donde un especialista demuestra su valor. Los pagos suelen poder <b>dividirse "
                  "entre camarotes</b> para que cada familia o pareja pague lo suyo, y un asesor puede <b>coordinar "
                  "todo el grupo</b>, camarotes juntos, comida reservada, todos en el mismo crucero, en una sola "
                  "llamada.</p>"
                  + tip("¿Organizas una reunión, grupo de boda o viaje de varias familias? Dinos el tamaño del grupo "
                        "y qué importa, y nosotros nos encargamos del resto. Para eso es la llamada."),
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>Pick a big, activity-rich ship, lock in connecting cabins early, use the kids' clubs, arrange "
                  "group dining, and split the payments. Everyone gets their own kind of holiday, together.</p>"
                  "<p>Group trips are fiddly to book alone and simple with help. Tell a specialist your group and dates, "
                  "and they line it all up, free, no obligation.</p>",
            "es": "<p>Elige un barco grande y lleno de actividades, asegura los camarotes conectados pronto, usa los "
                  "clubes infantiles, organiza la comida en grupo y divide los pagos. Cada uno tiene sus vacaciones, "
                  "juntos.</p>"
                  "<p>Los viajes en grupo son complicados de reservar solo y simples con ayuda. Dile a un especialista "
                  "tu grupo y fechas, y lo alinean todo, gratis y sin compromiso.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("What is the best cruise for families?", "A big, activity-packed contemporary ship with strong kids' and teen clubs, family cabins and lots of included activity. The right one depends on your children's ages and budget; compare the lines and what's included."),
            ("Can families get connecting cabins on a cruise?", "Yes, many ships have connecting cabins (two rooms with an internal door) and family-sized rooms, but they are limited and sell out early. Book ahead, and a specialist can secure rooms together for your group."),
            ("Are kids' clubs included on a cruise?", "Daytime, age-grouped youth programming is generally included. Infant nurseries and late-night care can carry an hourly charge on some lines. Minimum sailing ages and club age bands vary by line."),
            ("Can a group all eat together on a cruise?", "Yes. Ask for one large table at a set dining time so the whole party eats together each evening. Specialty restaurants can usually host a group with advance notice."),
            ("Can we split the payment across a group booking?", "Often yes, payments can be split across cabins so each family or couple settles their own. A specialist can coordinate the whole group, cabins, dining and payments, in one call."),
        ],
        "es": [
            ("¿Cuál es el mejor crucero para familias?", "Un barco informal grande y lleno de actividades, con buenos clubes de niños y adolescentes, camarotes familiares y mucha actividad incluida. El correcto depende de las edades de tus hijos y el presupuesto; compara las líneas y lo que incluyen."),
            ("¿Las familias pueden tener camarotes conectados?", "Sí, muchos barcos tienen camarotes conectados (dos habitaciones con puerta interna) y familiares, pero son limitados y se agotan pronto. Reserva con anticipación, y un especialista puede asegurar habitaciones juntas para tu grupo."),
            ("¿Los clubes infantiles están incluidos?", "La programación juvenil de día, por edades, suele estar incluida. Las guarderías para bebés y el cuidado nocturno pueden tener un cargo por hora en algunas líneas. Las edades mínimas y bandas de los clubes varían por línea."),
            ("¿Puede un grupo comer junto en un crucero?", "Sí. Pide una mesa grande a una hora fija para que todo el grupo cene junto cada noche. Los restaurantes de especialidad suelen poder recibir a un grupo con aviso previo."),
            ("¿Podemos dividir el pago en una reserva de grupo?", "A menudo sí, los pagos pueden dividirse entre camarotes para que cada familia o pareja pague lo suyo. Un especialista puede coordinar todo el grupo, camarotes, comida y pagos, en una llamada."),
        ],
    },
    "related": {
        "en": [
            ("🚢", "Big ship vs small ship", "/en/guides/big-ship-vs-small-ship/", "Why big ships usually win for families and groups."),
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "Connecting, adjacent and family cabin options."),
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "The big picture if this is the group's first cruise."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your group; we'll coordinate it all."),
        ],
        "es": [
            ("🚢", "Barco grande vs pequeño", "/es/guides/big-ship-vs-small-ship/", "Por qué los barcos grandes suelen ganar para familias y grupos."),
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "Opciones de camarotes conectados, contiguos y familiares."),
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "El panorama si es el primer crucero del grupo."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos tu grupo; lo coordinamos todo."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("accessibility", {
    "cat": "who", "hero": "accessibility.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "Accessible cruising: cabins, tendering & what to confirm", "es": "Cruceros accesibles: camarotes, transbordos y qué confirmar"},
    "dek": {
        "en": "Cruising can be one of the most accessible ways to travel: you unpack once and the ship "
              "comes with you. But accessibility varies by ship and port, so a little planning makes all "
              "the difference. Here is what to look for and what to confirm before you book.",
        "es": "Un crucero puede ser una de las formas más accesibles de viajar: desempacas una vez y el "
              "barco va contigo. Pero la accesibilidad varía por barco y puerto, así que un poco de "
              "planificación hace toda la diferencia. Esto es qué buscar y qué confirmar antes de reservar.",
    },
    "takeaways": {
        "en": [
            "Most modern ships have accessible staterooms with wider doors, roll-in showers and grab bars, but they are limited, so book early.",
            "Ships are largely step-free with elevators, but a few older areas and some tender ports can be harder to access.",
            "Tender ports (where you reach shore by small boat) are the main accessibility variable; some are not wheelchair-friendly.",
            "Tell the line about your needs in advance: mobility, dietary, medical equipment, oxygen, and service animals.",
            "Confirm the specifics for your exact ship and itinerary before you book; a specialist can check it for you.",
        ],
        "es": [
            "La mayoría de barcos modernos tienen camarotes accesibles con puertas más anchas, duchas sin escalón y barras de apoyo, pero son limitados, así que reserva pronto.",
            "Los barcos son en gran medida sin escalones y con ascensores, pero algunas áreas antiguas y ciertos puertos de fondeo pueden ser más difíciles de acceder.",
            "Los puertos de fondeo (donde llegas a tierra en bote pequeño) son la principal variable; algunos no son aptos para sillas de ruedas.",
            "Avisa a la línea de tus necesidades con anticipación: movilidad, dieta, equipo médico, oxígeno y animales de servicio.",
            "Confirma los detalles de tu barco e itinerario exactos antes de reservar; un especialista puede verificarlo por ti.",
        ],
    },
    "sections": [
        {"id": "cabins", "h2": {"en": "Accessible staterooms", "es": "Camarotes accesibles"},
         "html": {
            "en": "<p>Most modern ships offer <b>accessible staterooms</b> designed for wheelchair and mobility needs: "
                  "wider doorways, more turning space, roll-in showers, grab bars and lower fittings. They come in "
                  "several cabin categories, from interior to suite.</p>"
                  + watch("Accessible cabins are limited in number and in high demand, so they book up well ahead. If "
                          "you need one, reserve as early as you can, and confirm the exact features (roll-in shower vs "
                          "bath, door widths) for the specific ship."),
            "es": "<p>La mayoría de barcos modernos ofrecen <b>camarotes accesibles</b> diseñados para sillas de ruedas "
                  "y necesidades de movilidad: puertas más anchas, más espacio para girar, duchas sin escalón, barras "
                  "de apoyo y accesorios más bajos. Vienen en varias categorías, de interior a suite.</p>"
                  + watch("Los camarotes accesibles son limitados y muy demandados, así que se agotan con antelación. "
                          "Si necesitas uno, reserva lo antes posible, y confirma las características exactas (ducha sin "
                          "escalón vs bañera, ancho de puertas) del barco específico."),
         }},
        {"id": "getting-around", "h2": {"en": "Getting around the ship", "es": "Moverse por el barco"},
         "html": {
            "en": "<p>Modern ships are largely step-free, with elevators to every deck and accessible public spaces, "
                  "dining rooms, theatres and pools. Crew are generally well trained to assist. A few older ships or "
                  "specific areas can be trickier, which is worth checking for your vessel.</p>"
                  "<p>Bringing a mobility scooter or wheelchair? Confirm it fits through your cabin door and can be "
                  "stored in the room (corridors must stay clear), and let the line know in advance.</p>",
            "es": "<p>Los barcos modernos son en gran medida sin escalones, con ascensores a cada cubierta y espacios "
                  "públicos accesibles, comedores, teatros y piscinas. La tripulación suele estar bien entrenada para "
                  "ayudar. Algunos barcos viejos o áreas específicas pueden ser más complicados, lo que vale la pena "
                  "revisar para tu barco.</p>"
                  "<p>¿Llevas un scooter de movilidad o silla de ruedas? Confirma que pase por la puerta del camarote y "
                  "se pueda guardar en la habitación (los pasillos deben quedar libres), y avisa a la línea con "
                  "anticipación.</p>",
         }},
        {"id": "ports-tendering", "h2": {"en": "Ports and tendering", "es": "Puertos y transbordos"},
         "html": {
            "en": define("Tender port",
                         "a port where the ship anchors offshore and small boats (tenders) ferry guests to land, rather "
                         "than docking at a pier.")
                  + "<p>Tendering is the single biggest accessibility variable. At docked ports you roll straight off "
                  "the ship; at tender ports, boarding a small boat with a wheelchair or limited mobility can be "
                  "difficult or, in rough conditions, not possible. Some itineraries have more tender ports than "
                  "others.</p>"
                  + tip("If tendering is a concern, choose an itinerary with mostly docked ports. A specialist can flag "
                        "which stops on a given sailing are tender ports before you book."),
            "es": define("Puerto de fondeo (tender)",
                         "un puerto donde el barco ancla mar adentro y botes pequeños (tenders) llevan a los huéspedes a "
                         "tierra, en lugar de atracar en un muelle.")
                  + "<p>El transbordo es la mayor variable de accesibilidad. En puertos con muelle bajas directo del "
                  "barco; en puertos de fondeo, subir a un bote pequeño con silla de ruedas o movilidad limitada puede "
                  "ser difícil o, con mal tiempo, imposible. Algunos itinerarios tienen más puertos de fondeo que "
                  "otros.</p>"
                  + tip("Si el transbordo es una preocupación, elige un itinerario con puertos mayormente con muelle. "
                        "Un especialista puede señalar qué escalas de un crucero son de fondeo antes de reservar."),
         }},
        {"id": "confirm", "h2": {"en": "What to confirm before you book", "es": "Qué confirmar antes de reservar"},
         "html": {
            "en": "<ul>"
                  "<li><b>Cabin features</b> for the specific ship (roll-in shower, door widths, turning space).</li>"
                  "<li><b>Which ports are tender ports</b> on your itinerary.</li>"
                  "<li><b>Special needs</b> registered in advance: mobility equipment, oxygen, dietary requirements, service animals.</li>"
                  "<li><b>Embarkation assistance</b> and any medical facilities on board.</li>"
                  "</ul>"
                  "<p>Every major line offers accessible staterooms and step-free access, but the details vary by ship "
                  "and port. Confirming them for your exact sailing is precisely what a specialist does on the call.</p>",
            "es": "<ul>"
                  "<li><b>Características del camarote</b> del barco específico (ducha sin escalón, ancho de puertas, espacio para girar).</li>"
                  "<li><b>Qué puertos son de fondeo</b> en tu itinerario.</li>"
                  "<li><b>Necesidades especiales</b> registradas con anticipación: equipo de movilidad, oxígeno, dieta, animales de servicio.</li>"
                  "<li><b>Asistencia de embarque</b> y las instalaciones médicas a bordo.</li>"
                  "</ul>"
                  "<p>Cada línea principal ofrece camarotes accesibles y acceso sin escalones, pero los detalles varían "
                  "por barco y puerto. Confirmarlos para tu crucero exacto es justo lo que hace un especialista en la "
                  "llamada.</p>",
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>Cruising is genuinely accessible for many travellers: book an accessible cabin early, choose an "
                  "itinerary that avoids difficult tender ports if needed, and register your requirements in advance. "
                  "The ship does the rest.</p>"
                  "<p>Confirming the specifics is fiddly to do alone. Tell a specialist your needs and they will check "
                  "the exact ship and ports for you, free and with no obligation.</p>",
            "es": "<p>Un crucero es genuinamente accesible para muchos viajeros: reserva pronto un camarote accesible, "
                  "elige un itinerario que evite puertos de fondeo difíciles si hace falta, y registra tus necesidades "
                  "con anticipación. El barco hace el resto.</p>"
                  "<p>Confirmar los detalles es complicado de hacer solo. Dile a un especialista tus necesidades y "
                  "revisará el barco y los puertos exactos por ti, gratis y sin compromiso.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("Are cruise ships wheelchair accessible?", "Most modern ships are largely step-free with elevators to every deck, accessible staterooms and accessible public spaces. A few older ships or specific areas can be harder, so confirm the details for your exact vessel."),
            ("How do I get an accessible cabin on a cruise?", "Book as early as you can, accessible staterooms are limited and in high demand. Confirm the specific features (roll-in shower, door widths, turning space) for the ship, and register your needs with the line in advance."),
            ("What is tendering and why does it matter for accessibility?", "At a tender port the ship anchors offshore and small boats ferry guests to land. Boarding a tender with a wheelchair or limited mobility can be difficult or, in rough seas, not possible. Choosing an itinerary with mostly docked ports helps."),
            ("Can I bring a mobility scooter or oxygen on a cruise?", "Usually yes, with advance notice. Confirm the scooter fits through your cabin door and can be stored in the room, and register medical equipment like oxygen with the line before you sail."),
            ("Are service animals allowed on cruises?", "Generally yes, with documentation and advance notice, though rules and relief areas vary by line, and some ports of call have their own entry requirements. Confirm for your specific itinerary."),
        ],
        "es": [
            ("¿Los cruceros son accesibles para sillas de ruedas?", "La mayoría de barcos modernos son en gran medida sin escalones, con ascensores a cada cubierta, camarotes accesibles y espacios públicos accesibles. Algunos barcos viejos o áreas específicas pueden ser más difíciles, así que confirma los detalles de tu barco."),
            ("¿Cómo obtengo un camarote accesible?", "Reserva lo antes posible, los camarotes accesibles son limitados y muy demandados. Confirma las características específicas (ducha sin escalón, ancho de puertas, espacio para girar) del barco, y registra tus necesidades con la línea con anticipación."),
            ("¿Qué es el transbordo y por qué importa para la accesibilidad?", "En un puerto de fondeo el barco ancla mar adentro y botes pequeños llevan a los huéspedes a tierra. Subir a un tender con silla de ruedas o movilidad limitada puede ser difícil o, con mar agitado, imposible. Elegir un itinerario con puertos mayormente con muelle ayuda."),
            ("¿Puedo llevar scooter de movilidad u oxígeno?", "Normalmente sí, con aviso previo. Confirma que el scooter pase por la puerta del camarote y se pueda guardar en la habitación, y registra el equipo médico como el oxígeno con la línea antes de zarpar."),
            ("¿Se permiten animales de servicio en los cruceros?", "En general sí, con documentación y aviso previo, aunque las reglas y áreas de alivio varían por línea, y algunos puertos tienen sus propios requisitos de entrada. Confirma para tu itinerario específico."),
        ],
    },
    "related": {
        "en": [
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "Where accessible staterooms fit among the cabin types."),
            ("🗺️", "How to choose a destination", "/en/guides/how-to-choose-a-destination/", "Pick itineraries that avoid difficult tender ports."),
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "The big picture for a first accessible sailing."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your needs; we'll check the ship and ports."),
        ],
        "es": [
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "Dónde encajan los camarotes accesibles entre los tipos."),
            ("🗺️", "Cómo elegir un destino", "/es/guides/how-to-choose-a-destination/", "Elige itinerarios que eviten puertos de fondeo difíciles."),
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "El panorama para un primer crucero accesible."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos tus necesidades; revisamos el barco y los puertos."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("couples-adults-only-cruising", {
    "cat": "who",
    "hero": "couples-adults-only-cruising.jpg",
    "published": "2026-08-05",
    "updated": "2026-08-05",
    "title": {
        "en": "Cruising for couples: adults-only spaces and quieter ships",
        "es": "Cruceros en pareja: zonas solo para adultos y barcos más tranquilos",
    },
    "dek": {
        "en": "A cruise can be one of the easiest holidays two people ever take together: unpack once, "
              "wake up somewhere new, and nobody has to drive. Whether it feels romantic or feels like a "
              "school playground depends almost entirely on choices you make before you book. Here is what "
              "actually shapes a couples cruise.",
        "es": "Un crucero puede ser una de las vacaciones más fáciles para dos personas: deshaces la maleta "
              "una vez, despiertas en un lugar nuevo y nadie tiene que conducir. Que se sienta romántico o "
              "como un patio de colegio depende casi por completo de decisiones previas a la reserva. Esto "
              "es lo que de verdad define un crucero en pareja.",
    },
    "takeaways": {
        "en": [
            "When you sail matters more than which ship you pick. School holidays fill any ship with families; term time is a different holiday entirely.",
            "Most big ships have an adults-only area, usually a quieter pool and sun deck. It is the single feature that changes a couples cruise the most.",
            "Adults-only SHIPS exist too, where nobody under 18 sails at all, but they are a small part of the market and price accordingly.",
            "A balcony is worth more to two people than to four. Morning coffee looking at the sea is the whole argument.",
            "Speciality restaurants are where the quiet dinners are. The main dining room is sociable by design.",
            "Ask about what is included before you book: a couples cruise often ends up costing less than expected once bundled, and more than expected if you buy everything on board.",
        ],
        "es": [
            "Cuándo navegas importa más que qué barco eliges. Las vacaciones escolares llenan cualquier barco de familias; fuera de temporada es otro viaje.",
            "Casi todos los barcos grandes tienen una zona solo para adultos, normalmente una piscina y cubierta más tranquilas. Es lo que más cambia un crucero en pareja.",
            "También existen barcos solo para adultos, donde no viaja nadie menor de 18 años, pero son una parte pequeña del mercado y su precio lo refleja.",
            "Un balcón vale más para dos personas que para cuatro. El café de la mañana mirando al mar es todo el argumento.",
            "Los restaurantes de especialidad son donde están las cenas tranquilas. El comedor principal es sociable por diseño.",
            "Pregunta qué incluye la tarifa antes de reservar: un crucero en pareja suele costar menos de lo esperado si se agrupa, y más si compras todo a bordo.",
        ],
    },
    "sections": [
        {"id": "timing", "h2": {"en": "When you sail decides almost everything",
                                "es": "Cuándo navegas decide casi todo"},
         "html": {
            "en": "<p>People spend weeks choosing a ship and ten seconds choosing a week. That is backwards. "
                  "The same ship, same cabin, same route feels like two different holidays depending on the "
                  "calendar.</p>"
                  + vcards([
                      ("🏫", "School holidays", "Summer, Christmas, Easter and half terms fill every family-friendly ship. Pools are busy, the buffet is loud, and the good speciality tables book out early."),
                      ("🍂", "Term time", "Late January to early March, and September to mid-November, skew heavily adult. Quieter decks, easier bookings, and often the better value of the year."),
                      ("🌡️", "Shoulder season", "Spring and autumn give you gentler weather in the Caribbean and the Mediterranean, and a calmer crowd than peak summer."),
                  ])
                  + "<p>If your dates are flexible at all, this is the lever to pull first. It costs nothing "
                  "and changes more than any other decision on this page.</p>",
            "es": "<p>La gente dedica semanas a elegir barco y diez segundos a elegir la semana. Es al revés. "
                  "El mismo barco, el mismo camarote y la misma ruta se sienten como dos viajes distintos "
                  "según el calendario.</p>"
                  + vcards([
                      ("🏫", "Vacaciones escolares", "Verano, Navidad, Semana Santa y puentes llenan de familias cualquier barco. Piscinas concurridas, buffet ruidoso y las mejores mesas reservadas pronto."),
                      ("🍂", "Fuera de temporada", "De finales de enero a principios de marzo, y de septiembre a mediados de noviembre, el pasaje es mucho más adulto. Cubiertas tranquilas y a menudo la mejor relación calidad-precio del año."),
                      ("🌡️", "Temporada media", "Primavera y otoño dan mejor clima en el Caribe y el Mediterráneo, y menos gente que en pleno verano."),
                  ])
                  + "<p>Si tus fechas son algo flexibles, esta es la primera palanca. No cuesta nada y cambia "
                  "más que cualquier otra decisión de esta guía.</p>",
         }},
        {"id": "adults-only-areas", "h2": {"en": "Adults-only areas: the feature worth checking first",
                                           "es": "Zonas solo para adultos: lo primero que conviene mirar"},
         "html": {
            "en": "<p>Most large ships set aside a section of deck where under-18s are not allowed. Names vary "
                  "by line, but the idea is consistent: a quieter pool or hot tubs, padded loungers, a bar, "
                  "and sometimes a separate cafe.</p>"
                  + define("Adults-only area",
                           "a section of a mainstream ship reserved for guests 18 or older, typically a pool "
                           "deck or solarium. The rest of the ship stays open to all ages.")
                  + "<p>This matters more than it sounds. It means you can sail on a big, well-priced family "
                  "ship and still have somewhere calm to spend a sea day. Some lines charge a small fee for "
                  "the more elaborate versions; many include the basic one in your fare.</p>"
                  + tip("Two questions worth asking before you book: is the adults-only area covered or open "
                        "to the sun, and does it have its own bar and food service. An uncovered deck with no "
                        "service is a very different proposition on a hot Caribbean afternoon."),
            "es": "<p>Casi todos los barcos grandes reservan una zona de cubierta donde no se permiten menores "
                  "de 18. Los nombres varían por línea, pero la idea es la misma: piscina o jacuzzis más "
                  "tranquilos, tumbonas acolchadas, un bar y a veces una cafetería aparte.</p>"
                  + define("Zona solo para adultos",
                           "una sección de un barco convencional reservada a mayores de 18, normalmente una "
                           "cubierta de piscina o solárium. El resto del barco sigue abierto a todas las edades.")
                  + "<p>Importa más de lo que parece. Permite navegar en un barco familiar grande y bien de "
                  "precio y aun así tener un sitio tranquilo para un día en el mar. Algunas líneas cobran una "
                  "cuota pequeña por las versiones más elaboradas; muchas incluyen la básica en la tarifa.</p>"
                  + tip("Dos preguntas antes de reservar: si la zona está cubierta o al sol, y si tiene bar y "
                        "servicio de comida propios. Una cubierta descubierta y sin servicio es muy distinta "
                        "en una tarde calurosa del Caribe."),
         }},
        {"id": "adults-only-ships", "h2": {"en": "Adults-only ships, and who they suit",
                                           "es": "Barcos solo para adultos y a quién le encajan"},
         "html": {
            "en": "<p>A handful of lines sail ships where nobody under 18 is on board at all. It is a genuinely "
                  "different atmosphere: no kids clubs, no waterslides, no family cabins, and a passenger "
                  "profile that skews toward couples and friends travelling together.</p>"
                  + vcards([
                      ("🤫", "What you gain", "Consistent quiet, adult-paced entertainment, and dining rooms that stay calm at seven in the evening."),
                      ("💷", "What it costs", "These ships are smaller and carry fewer guests, so the fare per person is usually higher than a comparable mainstream sailing."),
                      ("🗓️", "Where they sail", "Deployment is narrower than the big lines, so your dates and destinations may be more limited."),
                  ])
                  + "<p>Worth knowing: you do not need an adults-only ship to get an adults-only holiday. A "
                  "mainstream ship in term time, with a balcony and a couple of speciality dinners booked, "
                  "gets most couples most of the way there for less money. We do not publish verified guides "
                  "for the adults-only lines yet, so we will not rank them here.</p>",
            "es": "<p>Unas pocas líneas operan barcos donde no viaja nadie menor de 18 años. El ambiente es "
                  "realmente distinto: sin clubes infantiles, sin toboganes, sin camarotes familiares, y con "
                  "un pasaje que tiende a parejas y grupos de amigos.</p>"
                  + vcards([
                      ("🤫", "Lo que ganas", "Tranquilidad constante, entretenimiento a ritmo adulto y comedores que siguen en calma a las siete de la tarde."),
                      ("💷", "Lo que cuesta", "Son barcos más pequeños con menos huéspedes, así que la tarifa por persona suele ser más alta que en una salida convencional comparable."),
                      ("🗓️", "Dónde navegan", "Su despliegue es más limitado que el de las grandes líneas, así que tus fechas y destinos pueden reducirse."),
                  ])
                  + "<p>Conviene saberlo: no necesitas un barco solo para adultos para tener unas vacaciones "
                  "de adultos. Un barco convencional fuera de temporada, con balcón y un par de cenas de "
                  "especialidad reservadas, lleva a la mayoría de las parejas casi al mismo sitio por menos "
                  "dinero. Todavía no publicamos guías verificadas de las líneas solo para adultos, así que "
                  "no las clasificamos aquí.</p>",
         }},
        {"id": "cabin", "h2": {"en": "The cabin question, for two", "es": "La cuestión del camarote, para dos"},
         "html": {
            "en": "<p>Cabin advice changes when there are only two of you. Space matters less; the view and the "
                  "privacy matter more.</p>"
                  + vcards([
                      ("🌅", "Balcony", "The strongest upgrade for a couple. Coffee at sea in the morning, a quiet place to read while the pool deck fills up, and somewhere to be alone together that is not a corridor."),
                      ("🪟", "Ocean view", "Natural light and a sense of where you are, without the balcony premium. A sensible middle if the fare gap is wide."),
                      ("🛏️", "Interior", "Genuinely fine for two people who plan to be out all day, and the money saved buys a lot of dinners ashore."),
                      ("🛎️", "Suite", "Worth it mainly for the extras attached: priority boarding, a quieter restaurant, sometimes a concierge. Ask what actually comes with it before paying for the square footage."),
                  ])
                  + "<p>Location deserves a thought too. Midship and lower decks feel the least motion, and a "
                  "cabin away from the pool deck and the theatre is measurably quieter at night. That is "
                  "covered properly in " + link("/en/guides/best-cabin-location/", "best cabin location") + ".</p>",
            "es": "<p>Los consejos sobre camarotes cambian cuando solo van dos. El espacio importa menos; la "
                  "vista y la privacidad importan más.</p>"
                  + vcards([
                      ("🌅", "Balcón", "La mejor mejora para una pareja. Café en el mar por la mañana, un sitio tranquilo para leer mientras se llena la piscina, y un lugar para estar a solas que no es un pasillo."),
                      ("🪟", "Vista al mar", "Luz natural y sentido de dónde estás, sin el sobreprecio del balcón. Un punto medio sensato si la diferencia de tarifa es grande."),
                      ("🛏️", "Interior", "Perfectamente válido para dos personas que piensan estar fuera todo el día, y lo ahorrado da para muchas cenas en tierra."),
                      ("🛎️", "Suite", "Vale la pena sobre todo por los extras asociados: embarque prioritario, un restaurante más tranquilo, a veces conserje. Pregunta qué incluye de verdad antes de pagar por los metros."),
                  ])
                  + "<p>La ubicación también merece un pensamiento. El centro del barco y las cubiertas bajas "
                  "sienten menos movimiento, y un camarote lejos de la piscina y del teatro es notablemente "
                  "más silencioso de noche. Lo cubrimos en "
                  + link("/es/guides/best-cabin-location/", "mejor ubicación del camarote") + ".</p>",
         }},
        {"id": "dining-evenings", "h2": {"en": "Dinner, and how to get a quiet one",
                                         "es": "La cena, y cómo conseguir una tranquila"},
         "html": {
            "en": "<p>The main dining room is designed to be sociable. On many ships that means shared tables "
                  "unless you ask otherwise, and a room that is lively rather than intimate.</p>"
                  + vcards([
                      ("🍽️", "Ask for a table for two", "Usually possible, but it is a request, not a guarantee, and it is far easier to arrange before you sail than on the first night."),
                      ("🥂", "Book a speciality restaurant", "Smaller rooms, quieter service, and the closest thing to a restaurant dinner ashore. These carry an extra charge and the good nights book out early."),
                      ("🌙", "Late seating", "If your line still runs fixed dining times, the later sitting is usually the calmer, more adult room."),
                      ("🎭", "Evening entertainment", "Theatre shows are the loud option; piano bars, jazz lounges and the observation lounges are where couples actually end up."),
                  ])
                  + watch("<b>Speciality dining and drinks packages are where a couples cruise gets expensive "
                          "quietly.</b> Two people, a package each, a few dinners out, and the total moves a "
                          "long way from the headline fare. Decide before you sail which of these you actually "
                          "want, rather than buying them one at a time on board."),
            "es": "<p>El comedor principal está diseñado para ser sociable. En muchos barcos eso significa mesas "
                  "compartidas salvo que pidas otra cosa, y una sala animada más que íntima.</p>"
                  + vcards([
                      ("🍽️", "Pide mesa para dos", "Suele ser posible, pero es una petición, no una garantía, y es mucho más fácil de organizar antes de zarpar que la primera noche."),
                      ("🥂", "Reserva un restaurante de especialidad", "Salas más pequeñas, servicio más tranquilo y lo más parecido a cenar en un restaurante en tierra. Tienen coste extra y las mejores noches se agotan pronto."),
                      ("🌙", "Segundo turno", "Si tu línea aún usa horarios fijos de cena, el turno tardío suele ser la sala más tranquila y adulta."),
                      ("🎭", "Espectáculos", "El teatro es la opción ruidosa; los piano bares, los salones de jazz y los miradores son donde acaban las parejas."),
                  ])
                  + watch("<b>Los restaurantes de especialidad y los paquetes de bebidas son donde un crucero "
                          "en pareja se encarece sin que lo notes.</b> Dos personas, un paquete cada uno, unas "
                          "cuantas cenas fuera, y el total se aleja mucho de la tarifa anunciada. Decide antes "
                          "de zarpar cuáles quieres de verdad, en vez de comprarlos uno a uno a bordo."),
         }},
        {"id": "occasions", "h2": {"en": "Honeymoons, anniversaries and birthdays",
                                   "es": "Lunas de miel, aniversarios y cumpleaños"},
         "html": {
            "en": "<p>Cruise lines are well set up for occasions, but almost none of it happens automatically. "
                  "Tell someone.</p>"
                  + "<p>Noted at booking, an occasion can bring a cabin decoration, a cake at dinner, or a note "
                  "from the captain. Some lines offer honeymoon or anniversary packages; what they contain "
                  "varies a great deal, so it is worth asking what is actually in one rather than assuming. "
                  "Onboard credit, if your booking comes with any, is often the more useful version of the "
                  "same idea, because you spend it on what you want.</p>"
                  + tip("Say it twice: once when you book, and once at guest services on embarkation day. "
                        "Requests made months earlier do not always survive the journey to the ship."),
            "es": "<p>Las líneas están bien preparadas para celebraciones, pero casi nada ocurre solo. "
                  "Díselo a alguien.</p>"
                  + "<p>Anotada al reservar, una ocasión puede traer decoración en el camarote, una tarta en la "
                  "cena o una nota del capitán. Algunas líneas ofrecen paquetes de luna de miel o aniversario; "
                  "su contenido varía mucho, así que conviene preguntar qué incluye en vez de suponerlo. El "
                  "crédito a bordo, si tu reserva lo incluye, suele ser la versión más útil de la misma idea, "
                  "porque lo gastas en lo que quieres.</p>"
                  + tip("Dilo dos veces: al reservar y otra vez en recepción el día de embarque. Las "
                        "peticiones hechas meses antes no siempre llegan al barco."),
         }},
    ],
    "faqs": {
        "en": [
            ("Which cruise is best for couples?", "The one sailing at the right time of year for you. Timing shapes the atmosphere more than the ship does: the same vessel in term time and in the school holidays are two different holidays. After that, look for an adults-only deck area, book a balcony if the fare gap is reasonable, and reserve a speciality dinner or two."),
            ("Are there adults-only cruise ships?", "Yes. A small number of lines sail ships where nobody under 18 is on board, with no kids clubs or waterslides and a passenger profile of couples and friends. They are smaller ships with narrower deployment and usually a higher fare per person, so they are a genuine option rather than an obvious default."),
            ("Do normal cruise ships have adults-only areas?", "Most large ships do, typically a quieter pool deck or solarium reserved for guests 18 or older, sometimes with its own bar. Names and layouts vary by line and by ship, and a few lines charge a small fee for the more elaborate versions, so it is worth confirming for the specific ship you are considering."),
            ("Is a balcony worth it for a couple?", "For two people it is the upgrade that changes the trip most. It gives you somewhere private to have coffee in the morning and to sit while the public decks are busy, which matters more when there are two of you than when a cabin is shared by four. If the fare gap is large, an ocean view is a sensible middle."),
            ("When is the quietest time to cruise as a couple?", "Outside school holidays. Late January to early March and September to mid-November are the most adult-skewed periods on most routes, and often the best value of the year. Avoid summer, Christmas, Easter and half terms if a calm ship matters to you."),
            ("How do we get a table for two at dinner?", "Ask when you book rather than on board. Main dining rooms often seat guests at shared tables by default, and a table for two is a request that is much easier to accommodate in advance. Speciality restaurants are the more reliable route to a quiet dinner, and the popular nights book out early."),
        ],
        "es": [
            ("¿Qué crucero es mejor para parejas?", "El que zarpa en la época del año adecuada para ti. El calendario define el ambiente más que el barco: el mismo buque fuera de temporada y en vacaciones escolares son dos viajes distintos. Después, busca una zona de cubierta solo para adultos, reserva balcón si la diferencia de tarifa es razonable, y aparta una o dos cenas de especialidad."),
            ("¿Existen barcos solo para adultos?", "Sí. Unas pocas líneas operan barcos donde no viaja nadie menor de 18 años, sin clubes infantiles ni toboganes y con un pasaje de parejas y amigos. Son barcos más pequeños, con despliegue más limitado y normalmente tarifa por persona más alta, así que son una opción real más que la elección obvia."),
            ("¿Los barcos normales tienen zonas solo para adultos?", "La mayoría de los grandes sí, normalmente una cubierta de piscina o solárium más tranquilos reservados a mayores de 18, a veces con bar propio. Los nombres y la distribución varían por línea y por barco, y algunas líneas cobran una cuota pequeña por las versiones más elaboradas, así que conviene confirmarlo para el barco concreto."),
            ("¿Vale la pena un balcón para una pareja?", "Para dos personas es la mejora que más cambia el viaje. Te da un sitio privado para tomar café por la mañana y para sentarte cuando las cubiertas están llenas, algo que pesa más entre dos que cuando el camarote lo comparten cuatro. Si la diferencia de tarifa es grande, la vista al mar es un punto medio sensato."),
            ("¿Cuál es la mejor época para navegar en pareja?", "Fuera de vacaciones escolares. De finales de enero a principios de marzo y de septiembre a mediados de noviembre el pasaje es más adulto en la mayoría de las rutas, y a menudo es la mejor relación calidad-precio del año. Evita verano, Navidad, Semana Santa y puentes si te importa un barco tranquilo."),
            ("¿Cómo conseguimos mesa para dos en la cena?", "Pídelo al reservar, no a bordo. Los comedores principales suelen sentar a los huéspedes en mesas compartidas por defecto, y una mesa para dos es una petición mucho más fácil de atender con antelación. Los restaurantes de especialidad son la vía más fiable para una cena tranquila, y las noches populares se agotan pronto."),
        ],
    },
    "related": {
        "en": [
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "Interior, ocean view, balcony or suite."),
            ("🧭", "Best cabin location", "/en/guides/best-cabin-location/", "Where on the ship your room should sit."),
            ("🗓️", "When to cruise", "/en/guides/when-to-cruise/", "Season by season, region by region."),
            ("🎚️", "Contemporary vs premium vs luxury", "/en/guides/contemporary-premium-luxury/", "Which tier suits the trip you want."),
        ],
        "es": [
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "Interior, vista al mar, balcón o suite."),
            ("🧭", "Mejor ubicación del camarote", "/es/guides/best-cabin-location/", "Dónde debe estar tu habitación en el barco."),
            ("🗓️", "Cuándo hacer un crucero", "/es/guides/when-to-cruise/", "Temporada a temporada, región a región."),
            ("🎚️", "Contemporánea vs premium vs lujo", "/es/guides/contemporary-premium-luxury/", "Qué nivel encaja con tu viaje."),
        ],
    },
})
