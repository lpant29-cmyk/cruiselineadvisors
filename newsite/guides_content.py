# -*- coding: utf-8 -*-
"""Hand-written content for the rich guides. Import this module to populate RICH_GUIDES.

Compliance: NO fares/prices/rates/discounts/savings, no "$", no copied prose. Original research copy
only. Interlinks are hard-coded per language (/en/… or /es/…)."""
from guidepage import register, tip, watch, define

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# FLAGSHIP — What's included in a cruise fare (cluster: cruise costs & money)
# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("whats-included", {
    "cat": "costs",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "What's included in a cruise fare — and what costs extra",
        "es": "Qué incluye la tarifa de un crucero — y qué cuesta aparte",
    },
    "dek": {
        "en": "A cruise fare can feel all-inclusive right up until the final statement. Here's exactly "
              "what your fare covers, what gets billed separately, and how to keep the extras in check "
              "— so you know the real cost of a sailing before you ever pick up the phone.",
        "es": "La tarifa de un crucero parece todo incluido… hasta que llega la cuenta final. Aquí "
              "verás exactamente qué cubre tu tarifa, qué se cobra aparte y cómo controlar los extras "
              "— para que sepas el costo real de un crucero antes de llamar.",
    },
    "takeaways": {
        "en": [
            "Your fare almost always covers your cabin, main dining, most casual and buffet food, daytime activities, kids' clubs and most entertainment.",
            "The usual extras are gratuities, alcoholic and specialty drinks, Wi-Fi, specialty restaurants, shore excursions, the spa and photos.",
            "Daily gratuities (a service charge) are added to your account automatically, per guest per day — the one 'extra' almost everyone ends up paying.",
            "Drink and Wi-Fi packages can be worth it, but most lines require every adult in the cabin to buy the same package — the rule that catches people out.",
            "What counts as 'included' shifts a lot by line: a premium fare may fold in more, a casual fare less. Read the inclusions, not the headline.",
        ],
        "es": [
            "Tu tarifa casi siempre cubre el camarote, el comedor principal, la mayoría de la comida informal y el bufé, las actividades de día, los clubes infantiles y casi todo el entretenimiento.",
            "Los extras habituales son las propinas, las bebidas alcohólicas y especiales, el Wi-Fi, los restaurantes de especialidad, las excursiones, el spa y las fotos.",
            "Las propinas diarias (un cargo por servicio) se añaden a tu cuenta automáticamente, por huésped y por día — el 'extra' que casi todos terminan pagando.",
            "Los paquetes de bebidas y Wi-Fi pueden valer la pena, pero la mayoría de las líneas exigen que todos los adultos del camarote compren el mismo paquete — la regla que sorprende a muchos.",
            "Lo que se considera 'incluido' cambia mucho según la línea: una tarifa premium puede incluir más y una informal menos. Lee lo que se incluye, no el titular.",
        ],
    },
    "sections": [
        {
            "id": "included",
            "h2": {"en": "What your cruise fare includes", "es": "Qué incluye tu tarifa de crucero"},
            "html": {
                "en": "<p>On nearly every major line, one fare covers the core of your trip. Think of it as your "
                      "room, your ride and your everyday food-and-fun — bundled together:</p>"
                      "<ul>"
                      "<li><b>Your cabin</b> — the stateroom you booked, housekeeping and, on most lines, room service (sometimes with a small delivery charge at night).</li>"
                      "<li><b>Main dining</b> — the main dining rooms, the buffet and most casual eateries, plus tea, drip coffee, iced tea, water and juice at meals.</li>"
                      "<li><b>Daytime activities</b> — pools, hot tubs, the gym, deck games, trivia, and most onboard entertainment and production shows.</li>"
                      "<li><b>Kids' and teen clubs</b> — supervised, age-grouped programming during normal hours.</li>"
                      "<li><b>Getting from port to port</b> — the sailing itself, and usually the government taxes and port fees folded into your fare.</li>"
                      "</ul>"
                      "<p>That's a real all-in base: you could board, never spend another cent, and still eat well, "
                      "be entertained and see every port. The extras below are optional — but a few of them are almost "
                      "universal, so it pays to know them going in. For the exact, per-line detail, we keep a verified "
                      'rundown on the <a href="/en/cruise-facts/">cruise facts that cost you money</a> page.</p>',
                "es": "<p>En casi todas las líneas principales, una sola tarifa cubre lo esencial del viaje. Piénsalo "
                      "como tu habitación, tu transporte y tu comida-y-diversión de cada día, todo junto:</p>"
                      "<ul>"
                      "<li><b>Tu camarote</b> — la habitación que reservaste, la limpieza y, en la mayoría de líneas, el servicio a la habitación (a veces con un pequeño cargo de entrega por la noche).</li>"
                      "<li><b>Comedor principal</b> — los comedores principales, el bufé y la mayoría de los sitios informales, además de té, café de filtro, agua y jugo en las comidas.</li>"
                      "<li><b>Actividades de día</b> — piscinas, jacuzzis, gimnasio, juegos en cubierta, trivias y casi todo el entretenimiento y los espectáculos.</li>"
                      "<li><b>Clubes de niños y adolescentes</b> — programación supervisada por edades en horario normal.</li>"
                      "<li><b>El traslado entre puertos</b> — la navegación en sí y, normalmente, los impuestos y tasas portuarias incluidos en tu tarifa.</li>"
                      "</ul>"
                      "<p>Es una base realmente completa: podrías embarcar, no gastar un centavo más, y aun así comer "
                      "bien, divertirte y ver cada puerto. Los extras de abajo son opcionales, pero algunos son casi "
                      'universales. Para el detalle exacto por línea, mantenemos un resumen verificado en la página de '
                      '<a href="/es/cruise-facts/">datos de crucero que cuestan dinero</a>.</p>',
            },
        },
        {
            "id": "extra",
            "h2": {"en": "What costs extra on a cruise", "es": "Qué cuesta aparte en un crucero"},
            "html": {
                "en": "<p>Here's where the final statement grows. None of these are hidden exactly — but they're easy "
                      "to underestimate when you add them across a week:</p>"
                      "<ul>"
                      "<li><b>Gratuities</b> — a daily service charge, added automatically (see below).</li>"
                      "<li><b>Alcohol &amp; specialty drinks</b> — cocktails, wine, beer, sodas, bottled water, energy drinks and barista coffee.</li>"
                      "<li><b>Wi-Fi</b> — sold as tiered internet packages on most lines.</li>"
                      "<li><b>Specialty restaurants</b> — steakhouses, sushi, chef's-table and other à la carte venues carry a cover charge.</li>"
                      "<li><b>Shore excursions</b> — line-run tours in port; you can also explore independently.</li>"
                      "<li><b>The spa &amp; salon</b>, <b>photos</b>, <b>the casino</b>, <b>laundry</b>, and premium activities (thermal suites, some fitness classes, upcharge attractions).</li>"
                      "</ul>"
                      + tip("A useful mental model: your fare buys the <i>ship experience</i>; the extras buy <i>indulgences and convenience</i>. Decide before you sail which indulgences matter to you, and the rest is easy to skip.")
                      ,
                "es": "<p>Aquí es donde crece la cuenta final. Ninguno está realmente oculto, pero es fácil "
                      "subestimarlos cuando se suman durante una semana:</p>"
                      "<ul>"
                      "<li><b>Propinas</b> — un cargo por servicio diario, añadido automáticamente (ver abajo).</li>"
                      "<li><b>Alcohol y bebidas especiales</b> — cócteles, vino, cerveza, refrescos, agua embotellada, bebidas energéticas y café de barista.</li>"
                      "<li><b>Wi-Fi</b> — se vende como paquetes de internet por niveles en la mayoría de las líneas.</li>"
                      "<li><b>Restaurantes de especialidad</b> — parrillas, sushi y otros lugares a la carta tienen un cargo de cubierto.</li>"
                      "<li><b>Excursiones</b> — tours de la línea en cada puerto; también puedes explorar por tu cuenta.</li>"
                      "<li><b>Spa y salón</b>, <b>fotos</b>, <b>casino</b>, <b>lavandería</b> y actividades premium (suites térmicas, algunas clases, atracciones con cargo).</li>"
                      "</ul>"
                      + tip("Un modelo útil: tu tarifa compra la <i>experiencia del barco</i>; los extras compran <i>lujos y comodidad</i>. Decide antes de zarpar qué lujos te importan y el resto es fácil de omitir."),
            },
        },
        {
            "id": "gratuities",
            "h2": {"en": "Gratuities: the automatic daily charge", "es": "Propinas: el cargo diario automático"},
            "html": {
                "en": "<p>This is the single most common surprise for first-time cruisers. Almost every line adds a "
                      "<b>daily gratuity</b> — sometimes called a service charge or crew appreciation — to your onboard "
                      "account, <b>per guest, per day</b>, for the whole sailing. It's shared among the dining and "
                      "housekeeping teams who look after you.</p>"
                      "<ul>"
                      "<li>It's added <b>automatically</b> — you don't opt in, and it applies to every guest in the cabin, including children on most lines.</li>"
                      "<li>Suites and higher cabin categories often carry a <b>higher</b> daily amount than standard staterooms.</li>"
                      "<li>You can usually <b>prepay</b> it when you book, which locks it in and keeps your onboard account smaller.</li>"
                      "</ul>"
                      + define("Closed-loop sailing", "a round-trip cruise that starts and ends at the same US port. It matters for documents, not gratuities — but you'll see the term a lot.")
                      + '<p>The exact daily amount is a published figure that changes from time to time, so we track the '
                      'current, source-checked number for each line on the '
                      '<a href="/en/cruise-facts/">cruise facts</a> page rather than quote it here. When you call, an '
                      'advisor confirms it for your specific ship and cabin.</p>',
                "es": "<p>Es la sorpresa más común para quienes navegan por primera vez. Casi todas las líneas añaden "
                      "una <b>propina diaria</b> — a veces llamada cargo por servicio o agradecimiento a la tripulación "
                      "— a tu cuenta a bordo, <b>por huésped y por día</b>, durante todo el crucero. Se reparte entre "
                      "los equipos de comedor y limpieza que te atienden.</p>"
                      "<ul>"
                      "<li>Se añade <b>automáticamente</b> — no te inscribes, y aplica a cada huésped del camarote, incluidos los niños en la mayoría de las líneas.</li>"
                      "<li>Las suites y categorías superiores suelen tener un monto diario <b>más alto</b> que los camarotes estándar.</li>"
                      "<li>Normalmente puedes <b>pagarla por adelantado</b> al reservar, lo que la fija y deja tu cuenta a bordo más pequeña.</li>"
                      "</ul>"
                      + define("Crucero de ida y vuelta (closed-loop)", "un crucero que empieza y termina en el mismo puerto de EE.UU. Importa para los documentos, no para las propinas — pero verás mucho el término.")
                      + '<p>El monto diario exacto es una cifra publicada que cambia de vez en cuando, así que llevamos '
                      'el número actual y verificado de cada línea en la página de '
                      '<a href="/es/cruise-facts/">datos de crucero</a> en lugar de citarlo aquí. Al llamar, un asesor '
                      'lo confirma para tu barco y camarote.</p>',
            },
        },
        {
            "id": "packages",
            "h2": {"en": "Drink & Wi-Fi packages — and the whole-cabin rule",
                   "es": "Paquetes de bebidas y Wi-Fi — y la regla de todo el camarote"},
            "html": {
                "en": "<p>If you'll drink more than a couple of coffees and cocktails a day, a package can make the "
                      "extras predictable instead of a running tab. But there's a catch that surprises a lot of "
                      "people:</p>"
                      + watch("On most major lines, if <b>one adult</b> in a stateroom buys the alcohol package, <b>every</b> adult of drinking age in that same cabin has to buy it too. It's designed to stop one person sharing a package for the whole room.")
                      + "<p>The same logic often applies to Wi-Fi (per-device or per-cabin tiers). Before you commit:</p>"
                      "<ul>"
                      "<li>Add up what you'd actually drink or stream in a day. Packages reward heavy use, not light use.</li>"
                      "<li>Check whether children or non-drinkers can take a cheaper zero-proof or soda package instead.</li>"
                      "<li>Ask whether the package covers specialty coffee, bottled water and mini-bar items, or just the basics.</li>"
                      "</ul>"
                      '<p>The precise package rules differ by line — we keep the current, verified version for each on '
                      'the <a href="/en/cruise-facts/">cruise facts</a> page, and an advisor can tell you whether a '
                      'package is worth it for how you actually travel.</p>',
                "es": "<p>Si vas a tomar más de un par de cafés y cócteles al día, un paquete puede hacer los extras "
                      "predecibles en lugar de una cuenta que crece. Pero hay un detalle que sorprende a muchos:</p>"
                      + watch("En la mayoría de las líneas, si <b>un adulto</b> del camarote compra el paquete de alcohol, <b>todos</b> los adultos en edad de beber de ese mismo camarote también deben comprarlo. Está diseñado para evitar que una persona comparta un paquete con toda la habitación.")
                      + "<p>La misma lógica suele aplicar al Wi-Fi (por dispositivo o por camarote). Antes de decidir:</p>"
                      "<ul>"
                      "<li>Suma lo que realmente beberías o transmitirías en un día. Los paquetes premian el uso alto, no el bajo.</li>"
                      "<li>Revisa si los niños o quienes no beben pueden tomar un paquete sin alcohol o de refrescos, más económico.</li>"
                      "<li>Pregunta si el paquete cubre café de especialidad, agua embotellada y minibar, o solo lo básico.</li>"
                      "</ul>"
                      '<p>Las reglas exactas varían por línea — llevamos la versión actual y verificada de cada una en '
                      'la página de <a href="/es/cruise-facts/">datos de crucero</a>, y un asesor puede decirte si un '
                      'paquete vale la pena para tu forma de viajar.</p>',
            },
        },
        {
            "id": "by-line",
            "h2": {"en": "How 'included' changes by cruise line", "es": "Cómo cambia lo 'incluido' según la línea"},
            "html": {
                "en": "<p>Two fares that look similar can include very different things. Broadly:</p>"
                      "<ul>"
                      "<li><b>Contemporary / casual lines</b> keep the base fare approachable and sell more of the extras à la carte — great value if you're disciplined about add-ons.</li>"
                      "<li><b>Premium lines</b> often fold a bit more into the fare and lean to a calmer, more adult feel.</li>"
                      "<li><b>Ocean-liner and higher-end fares</b> may include more still — but the right answer is always to compare the inclusions, not the label.</li>"
                      "</ul>"
                      '<p>That\'s exactly what our tools are for. Line up any two brands on the money-and-fine-print facts '
                      'with the tool on each <a href="/en/cruise-lines/">cruise line</a> page, or tell us how you travel '
                      'and we\'ll <a href="/en/compare/">match you to the ships that fit</a>. One call then gets you the '
                      "real number for your dates.</p>",
                "es": "<p>Dos tarifas que parecen iguales pueden incluir cosas muy distintas. En general:</p>"
                      "<ul>"
                      "<li><b>Líneas informales</b> mantienen la tarifa base accesible y venden más extras a la carta — muy buen valor si eres disciplinado con los adicionales.</li>"
                      "<li><b>Líneas premium</b> suelen incluir un poco más en la tarifa y tienen un ambiente más tranquilo y adulto.</li>"
                      "<li><b>Transatlánticos y tarifas de gama alta</b> pueden incluir aún más — pero lo correcto siempre es comparar lo incluido, no la etiqueta.</li>"
                      "</ul>"
                      '<p>Para eso son nuestras herramientas. Compara dos marcas en los datos de dinero y letra pequeña '
                      'con la herramienta en cada página de <a href="/es/cruise-lines/">línea de crucero</a>, o dinos '
                      'cómo viajas y te <a href="/es/compare/">emparejamos con los barcos que encajan</a>. Una llamada te '
                      "da el número real para tus fechas.</p>",
            },
        },
        {
            "id": "keep-in-check",
            "h2": {"en": "How to keep the extras in check", "es": "Cómo controlar los extras"},
            "html": {
                "en": "<p>You don't need to skip the fun — just plan the handful of things that add up:</p>"
                      "<ul>"
                      "<li><b>Prepay your gratuities</b> when you book, so the daily charge isn't a surprise on the statement.</li>"
                      "<li><b>Decide on packages before you sail</b>, not at the bar on day one. Match the package to your real habits, and remember the whole-cabin rule.</li>"
                      "<li><b>Plan port days early.</b> Line tours are convenient; independent options can cover the same sights for less effort on the wallet. Book the ones that book out fast.</li>"
                      "<li><b>Set an onboard budget</b> and check your account mid-cruise at guest services or on the app — no end-of-week shock.</li>"
                      "<li><b>Lean on what's already included</b> — the main dining room, the buffet, the shows and the pools are a full holiday on their own.</li>"
                      "</ul>"
                      + tip('A specialist does a lot of this <i>for</i> you — flagging which extras are worth prepaying, which to skip, and what your total is likely to look like — before you commit. That\'s the whole point of the call.'),
                "es": "<p>No tienes que renunciar a la diversión — solo planea lo poco que se acumula:</p>"
                      "<ul>"
                      "<li><b>Paga las propinas por adelantado</b> al reservar, para que el cargo diario no sorprenda en la cuenta.</li>"
                      "<li><b>Decide los paquetes antes de zarpar</b>, no en el bar el primer día. Ajusta el paquete a tus hábitos reales y recuerda la regla de todo el camarote.</li>"
                      "<li><b>Planea los días de puerto con tiempo.</b> Los tours de la línea son cómodos; las opciones independientes pueden cubrir lo mismo con menos costo. Reserva pronto los que se agotan.</li>"
                      "<li><b>Fija un presupuesto a bordo</b> y revisa tu cuenta a mitad del crucero en recepción o en la app — sin sustos al final.</li>"
                      "<li><b>Aprovecha lo que ya está incluido</b> — el comedor principal, el bufé, los espectáculos y las piscinas son unas vacaciones completas por sí solas.</li>"
                      "</ul>"
                      + tip('Un especialista hace mucho de esto <i>por ti</i> — te dice qué extras conviene pagar por adelantado, cuáles omitir y cómo se verá tu total — antes de comprometerte. Ese es el sentido de la llamada.'),
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>A cruise is one of the few holidays where the big-ticket items — your room, your food, your "
                      "entertainment and your transport between countries — are bundled into one fare. Know the handful "
                      "of near-universal extras (gratuities, drinks, Wi-Fi, specialty dining and excursions), decide "
                      "which ones matter to you, and there are almost no surprises left.</p>"
                      "<p>When you're ready to turn that into a real, all-in figure for specific dates and a specific "
                      "ship, that's what we're here for — one call, no obligation, and we never take payment for travel.</p>",
                "es": "<p>Un crucero es una de las pocas vacaciones donde lo caro — tu habitación, tu comida, tu "
                      "entretenimiento y tu transporte entre países — viene en una sola tarifa. Conoce el puñado de "
                      "extras casi universales (propinas, bebidas, Wi-Fi, restaurantes de especialidad y excursiones), "
                      "decide cuáles te importan, y casi no quedan sorpresas.</p>"
                      "<p>Cuando quieras convertir eso en una cifra real y completa para fechas y un barco concretos, "
                      "para eso estamos — una llamada, sin compromiso, y nunca cobramos por el viaje.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("Are drinks included on a cruise?", "Water, most non-specialty coffee and tea, and juice at breakfast are typically included. Sodas, alcohol, bottled water, energy drinks and barista coffee are usually extra unless you buy a drink package."),
            ("Is Wi-Fi free on a cruise?", "Rarely. Most lines sell tiered internet packages, and a few premium or higher-end fares include a basic tier. Check the line's current policy before you sail."),
            ("Are gratuities included in a cruise fare?", "Usually not. A daily service charge (gratuity) is added to your onboard account per guest, per day, unless your fare specifically includes it. You can often prepay it when you book."),
            ("Is food included on a cruise?", "Yes for the main dining rooms, the buffet and most casual venues. Specialty and à la carte restaurants carry an extra cover charge."),
            ("Do kids' clubs cost extra?", "Daytime, age-grouped youth programming is generally included. Late-night care and infant nurseries can carry an hourly charge on some lines."),
            ("What's the biggest extra cost on a cruise?", "For most guests it's the combination of daily gratuities, drinks and shore excursions — plan for those three and there are few surprises left."),
        ],
        "es": [
            ("¿Las bebidas están incluidas en un crucero?", "Agua, café y té básicos y jugo en el desayuno suelen estar incluidos. Refrescos, alcohol, agua embotellada, bebidas energéticas y café de barista normalmente son aparte, salvo que compres un paquete de bebidas."),
            ("¿El Wi-Fi es gratis en un crucero?", "Casi nunca. La mayoría de las líneas venden paquetes de internet por niveles, y algunas tarifas premium incluyen un nivel básico. Revisa la política actual antes de zarpar."),
            ("¿Las propinas están incluidas en la tarifa?", "Normalmente no. Se añade un cargo por servicio diario a tu cuenta, por huésped y por día, salvo que tu tarifa lo incluya. A menudo puedes pagarlo por adelantado al reservar."),
            ("¿La comida está incluida en un crucero?", "Sí en los comedores principales, el bufé y la mayoría de los sitios informales. Los restaurantes de especialidad y a la carta tienen un cargo de cubierto."),
            ("¿Los clubes infantiles cuestan aparte?", "La programación juvenil de día, por edades, suele estar incluida. El cuidado nocturno y las guarderías para bebés pueden tener un cargo por hora en algunas líneas."),
            ("¿Cuál es el mayor gasto adicional en un crucero?", "Para la mayoría es la combinación de propinas diarias, bebidas y excursiones — planea esos tres y quedan pocas sorpresas."),
        ],
    },
    "related": {
        "en": [
            ("💸", "The cruise facts that cost you money", "/en/cruise-facts/", "Gratuities, packages, cancellation and documents — the fine print, verified per line."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us where and when; we line up the ships and one call books it."),
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "Interior to suite — what you get, what to watch for, and the cabins to avoid."),
            ("🚢", "Compare cruise lines", "/en/cruise-lines/", "See how the major lines differ on what's included and who they suit."),
        ],
        "es": [
            ("💸", "Datos de crucero que cuestan dinero", "/es/cruise-facts/", "Propinas, paquetes, cancelación y documentos — la letra pequeña, verificada por línea."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos dónde y cuándo; alineamos los barcos y una llamada reserva."),
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "De interior a suite — qué obtienes, qué vigilar y qué camarotes evitar."),
            ("🚢", "Comparar líneas de crucero", "/es/cruise-lines/", "Cómo difieren las líneas en lo que incluyen y para quién son."),
        ],
    },
})
