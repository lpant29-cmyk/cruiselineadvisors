# -*- coding: utf-8 -*-
"""Rich guides, cluster A: cruise costs & money. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link

# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("cruise-gratuities-explained", {
    "cat": "costs",
    "hero": "cruise-dining.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "Cruise gratuities & daily service charges, explained",
        "es": "Propinas de crucero y cargos por servicio diarios, explicados",
    },
    "dek": {
        "en": "Almost every cruise adds a daily gratuity to your account, and it surprises more "
              "first-timers than any other charge. Here is what it is, how it works, where the money "
              "goes, and how to plan for it, so nothing on your final statement is a shock.",
        "es": "Casi todos los cruceros añaden una propina diaria a tu cuenta, y sorprende a más "
              "primerizos que cualquier otro cargo. Esto es qué es, cómo funciona, a dónde va el dinero "
              "y cómo planearlo, para que nada en tu cuenta final te sorprenda.",
    },
    "takeaways": {
        "en": [
            "A daily gratuity (also called a service charge or crew appreciation) is added to your onboard account automatically, per guest, per day.",
            "It is shared among the dining, housekeeping and behind-the-scenes crew who look after you.",
            "Suites and higher cabin categories usually carry a higher daily amount than standard staterooms.",
            "You can prepay it when you book, which locks the amount and keeps your onboard account smaller.",
            "The exact daily figure changes over time and by line, so we keep the current verified number for each line on the cruise facts page.",
        ],
        "es": [
            "Una propina diaria (también llamada cargo por servicio o agradecimiento a la tripulación) se añade a tu cuenta a bordo automáticamente, por huésped y por día.",
            "Se reparte entre la tripulación de comedor, limpieza y de tras bambalinas que te atiende.",
            "Las suites y categorías superiores suelen tener un monto diario más alto que los camarotes estándar.",
            "Puedes pagarla por adelantado al reservar, lo que fija el monto y mantiene tu cuenta a bordo más pequeña.",
            "La cifra diaria exacta cambia con el tiempo y por línea, así que llevamos el número verificado de cada línea en la página de datos de crucero.",
        ],
    },
    "sections": [
        {
            "id": "what-are-they",
            "h2": {"en": "What a cruise gratuity actually is", "es": "Qué es realmente una propina de crucero"},
            "html": {
                "en": "<p>On a cruise, the tips that land staff would earn from you throughout the trip are pooled "
                      "into one <b>daily service charge</b>, added to your onboard account for every night you sail. "
                      "It is the cruise industry's standard way of handling gratuities, so you rarely hand cash to "
                      "individual crew for everyday service.</p>"
                      + define("Gratuity / service charge / crew appreciation",
                               "three names for the same thing: a set daily amount, per guest, that the line collects "
                               "on behalf of the crew who serve you.")
                      + "<p>Because it is automatic and per person, it adds up across a week in a way a lot of "
                      "first-time cruisers do not budget for. Knowing it is coming is half the battle.</p>",
                "es": "<p>En un crucero, las propinas que el personal ganaría de ti durante el viaje se juntan en un "
                      "solo <b>cargo por servicio diario</b>, añadido a tu cuenta por cada noche que navegas. Es la "
                      "forma estándar de la industria de manejar las propinas, así que rara vez das efectivo a la "
                      "tripulación por el servicio del día a día.</p>"
                      + define("Propina / cargo por servicio / agradecimiento a la tripulación",
                               "tres nombres para lo mismo: un monto diario fijo, por huésped, que la línea cobra en "
                               "nombre de la tripulación que te atiende.")
                      + "<p>Como es automático y por persona, se acumula durante una semana de una forma que muchos "
                      "primerizos no presupuestan. Saber que viene es la mitad de la batalla.</p>",
            },
        },
        {
            "id": "how-it-works",
            "h2": {"en": "How the daily charge works", "es": "Cómo funciona el cargo diario"},
            "html": {
                "en": vcards([
                    ("📅", "Per guest, per day", "Charged for every guest in the cabin, for every night of the sailing, including children on most lines."),
                    ("🏨", "Varies by cabin", "Suites and higher categories usually pay a higher daily amount than standard staterooms."),
                    ("🧾", "Added automatically", "It appears on your onboard account without you opting in; you settle the account at the end."),
                    ("💳", "Prepay option", "You can usually prepay at booking, which locks today's amount and keeps the onboard bill smaller."),
                ]) + "<p>The precise daily figure is a published number that lines adjust from time to time, and it "
                "differs from one line to the next. Rather than quote a figure that could go stale, we keep the "
                "current, source-checked amount for every line on the " + link("/en/cruise-facts/", "cruise facts") +
                " page.</p>",
                "es": vcards([
                    ("📅", "Por huésped, por día", "Se cobra por cada huésped del camarote, por cada noche del crucero, incluidos los niños en la mayoría de líneas."),
                    ("🏨", "Varía por camarote", "Las suites y categorías superiores suelen pagar un monto diario más alto que los camarotes estándar."),
                    ("🧾", "Añadido automáticamente", "Aparece en tu cuenta a bordo sin que te inscribas; liquidas la cuenta al final."),
                    ("💳", "Opción de prepago", "Normalmente puedes pagarla al reservar, lo que fija el monto de hoy y reduce la cuenta a bordo."),
                ]) + "<p>La cifra diaria exacta es un número publicado que las líneas ajustan de vez en cuando, y "
                "difiere de una línea a otra. En lugar de citar una cifra que podría quedar desactualizada, llevamos "
                "el monto actual y verificado de cada línea en la página de " + link("/es/cruise-facts/", "datos de crucero") +
                ".</p>",
            },
        },
        {
            "id": "where-it-goes",
            "h2": {"en": "Where the money goes", "es": "A dónde va el dinero"},
            "html": {
                "en": "<p>The daily charge is distributed across the crew who make your holiday run: your dining "
                      "room and buffet teams, your cabin steward, and the many behind-the-scenes staff you never see. "
                      "For crew members, it is a meaningful and expected part of their pay, which is why lines make it "
                      "the default rather than leaving it to chance.</p>",
                "es": "<p>El cargo diario se reparte entre la tripulación que hace funcionar tus vacaciones: los "
                      "equipos del comedor y el bufé, tu camarero de habitación y el mucho personal de tras bambalinas "
                      "que nunca ves. Para la tripulación es una parte importante y esperada de su salario, por eso las "
                      "líneas lo ponen por defecto en lugar de dejarlo al azar.</p>",
            },
        },
        {
            "id": "prepay-adjust",
            "h2": {"en": "Prepaying, and can you change it?", "es": "Prepago, ¿y puedes cambiarla?"},
            "html": {
                "en": "<p><b>Prepaying</b> is the simple win: pay the gratuities when you book or before you sail, "
                      "and they are locked at that amount, off your onboard account, and out of mind.</p>"
                      + watch("Adjusting or removing the daily gratuity is possible on some lines by visiting guest "
                              "services during the cruise, but policies vary, it is discouraged, and prepaid amounts "
                              "are handled differently. If you are considering it, confirm your line's current policy "
                              "first, and remember the crew are counting on it.")
                      + "<p>Some higher-end and premium fares <b>include</b> gratuities in the price, so there is "
                      "nothing added onboard at all. Whether yours does is exactly the kind of thing a specialist "
                      "confirms for your specific sailing when you call.</p>",
                "es": "<p><b>Prepagar</b> es la jugada sencilla: paga las propinas al reservar o antes de zarpar, y "
                      "quedan fijadas en ese monto, fuera de tu cuenta a bordo y de tu mente.</p>"
                      + watch("Ajustar o quitar la propina diaria es posible en algunas líneas visitando recepción "
                              "durante el crucero, pero las políticas varían, se desaconseja y los montos prepagados se "
                              "manejan distinto. Si lo consideras, confirma primero la política actual de tu línea, y "
                              "recuerda que la tripulación cuenta con ello.")
                      + "<p>Algunas tarifas premium y de gama alta <b>incluyen</b> las propinas en el precio, así que "
                      "no se añade nada a bordo. Si la tuya lo hace es justo el tipo de cosa que un especialista "
                      "confirma para tu crucero cuando llamas.</p>",
            },
        },
        {
            "id": "extra-tipping",
            "h2": {"en": "Automatic bar gratuities and extra tipping", "es": "Propinas de bar automáticas y propinas extra"},
            "html": {
                "en": "<p>The daily charge covers everyday service, but two things sit outside it:</p>"
                      "<ul>"
                      "<li><b>Bar and specialty purchases</b> usually have a gratuity added automatically at the "
                      "point of sale, so a drink or a specialty meal already includes the tip.</li>"
                      "<li><b>Extra cash tips</b> for standout service are entirely optional and always welcome, but "
                      "never expected on top of the daily charge.</li>"
                      "</ul>"
                      "<p>In other words: the daily gratuity handles the basics, and anything beyond it is your call.</p>",
                "es": "<p>El cargo diario cubre el servicio del día a día, pero dos cosas quedan fuera:</p>"
                      "<ul>"
                      "<li>Las <b>compras en bares y restaurantes de especialidad</b> normalmente llevan una propina "
                      "añadida automáticamente en el momento de pagar, así que una bebida o una comida ya incluye la "
                      "propina.</li>"
                      "<li>Las <b>propinas extra en efectivo</b> por un servicio excepcional son totalmente opcionales "
                      "y siempre bienvenidas, pero nunca esperadas sobre el cargo diario.</li>"
                      "</ul>"
                      "<p>En resumen: la propina diaria cubre lo básico, y cualquier cosa más allá es decisión tuya.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>Gratuities are the one near-universal extra on a cruise, so treat them as part of the "
                      "cost of the trip from the start. Prepay them if you like tidy accounting, know that suites pay "
                      "a little more, and check whether your fare already includes them.</p>"
                      "<p>Want the exact current amount for the line you are eyeing, and whether prepaying makes sense "
                      "for your sailing? One call sorts it, free and with no obligation. It also helps to read "
                      + link("/en/guides/whats-included/", "what is included in a cruise fare") + " next.</p>",
                "es": "<p>Las propinas son el extra casi universal de un crucero, así que trátalas como parte del "
                      "costo del viaje desde el principio. Págalas por adelantado si te gusta la contabilidad "
                      "ordenada, ten en cuenta que las suites pagan un poco más, y revisa si tu tarifa ya las "
                      "incluye.</p>"
                      "<p>¿Quieres el monto actual exacto de la línea que te interesa, y si prepagar tiene sentido "
                      "para tu crucero? Una llamada lo resuelve, gratis y sin compromiso. También ayuda leer "
                      + link("/es/guides/whats-included/", "qué incluye la tarifa de un crucero") + " a continuación.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("How much are cruise gratuities?", "They are a set daily amount per guest that varies by cruise line and cabin category, and lines adjust it over time. We keep the current, source-checked figure for each line on our cruise facts page; a specialist confirms it for your exact sailing when you call."),
            ("Are gratuities per person or per cabin?", "Per person, per day. The daily charge applies to each guest in the stateroom, including children on most lines, though some lines waive it for infants."),
            ("Can you remove or reduce cruise gratuities?", "On many lines you can ask to adjust them at guest services during the cruise, but policies vary, it is discouraged, and prepaid gratuities are handled differently. Confirm your line's current policy first."),
            ("Can you prepay gratuities?", "Usually yes, at booking or any time before you sail. Prepaying locks in the amount and keeps your onboard account smaller."),
            ("Do you still tip on top of the daily charge?", "You do not have to. Bar and specialty purchases already add a gratuity automatically, and extra cash for standout service is optional and never expected."),
            ("Are gratuities ever included in the fare?", "Yes. Some premium and higher-end fares include gratuities, so nothing is added onboard. Whether yours does depends on the line and fare type, which a specialist can confirm."),
        ],
        "es": [
            ("¿Cuánto son las propinas de crucero?", "Son un monto diario fijo por huésped que varía según la línea y la categoría del camarote, y las líneas lo ajustan con el tiempo. Llevamos la cifra actual y verificada de cada línea en nuestra página de datos de crucero; un especialista la confirma para tu crucero exacto cuando llamas."),
            ("¿Las propinas son por persona o por camarote?", "Por persona, por día. El cargo diario aplica a cada huésped del camarote, incluidos los niños en la mayoría de líneas, aunque algunas lo eximen para bebés."),
            ("¿Se pueden quitar o reducir las propinas?", "En muchas líneas puedes pedir ajustarlas en recepción durante el crucero, pero las políticas varían, se desaconseja y las propinas prepagadas se manejan distinto. Confirma primero la política actual de tu línea."),
            ("¿Se pueden pagar las propinas por adelantado?", "Normalmente sí, al reservar o en cualquier momento antes de zarpar. Prepagar fija el monto y mantiene tu cuenta a bordo más pequeña."),
            ("¿Se da propina extra además del cargo diario?", "No es obligatorio. Las compras en bares y restaurantes de especialidad ya añaden una propina automáticamente, y el efectivo extra por un servicio excepcional es opcional y nunca esperado."),
            ("¿Las propinas se incluyen alguna vez en la tarifa?", "Sí. Algunas tarifas premium y de gama alta incluyen las propinas, así que no se añade nada a bordo. Que la tuya lo haga depende de la línea y el tipo de tarifa, que un especialista puede confirmar."),
        ],
    },
    "related": {
        "en": [
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "The full split of what your fare covers and what costs extra."),
            ("💸", "The cruise facts that cost you money", "/en/cruise-facts/", "The current, verified gratuity figure for every line, plus packages and cancellation."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Line up the ships for your dates; one call books the right one."),
            ("🚢", "Compare cruise lines", "/en/cruise-lines/", "See how the lines differ on gratuities and what's included."),
        ],
        "es": [
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "El desglose completo de lo que cubre tu tarifa y lo que cuesta aparte."),
            ("💸", "Datos de crucero que cuestan dinero", "/es/cruise-facts/", "La cifra de propina actual y verificada de cada línea, además de paquetes y cancelación."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Alinea los barcos para tus fechas; una llamada reserva el correcto."),
            ("🚢", "Comparar líneas de crucero", "/es/cruise-lines/", "Cómo difieren las líneas en propinas y en lo que incluyen."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("how-to-find-affordable-cruise", {
    "cat": "costs",
    "hero": "cruise-planning.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "How to find an affordable cruise (without chasing fake deals)",
        "es": "Cómo encontrar un crucero accesible (sin caer en ofertas falsas)",
    },
    "dek": {
        "en": "Cruising can be one of the best-value holidays out there, if you know which levers "
              "actually move the number. Here are the real ones, from timing to cabin choice to the "
              "itineraries most people overlook, with none of the gimmicks.",
        "es": "Un crucero puede ser una de las vacaciones de mejor valor que existen, si sabes qué "
              "palancas mueven de verdad el precio. Aquí están las reales, del momento del año al tipo "
              "de camarote y los itinerarios que casi todos pasan por alto, sin trucos.",
    },
    "takeaways": {
        "en": [
            "Timing is the single biggest lever: shoulder seasons and the quieter weeks are far kinder to your budget than school holidays.",
            "The cabin type you pick moves the fare more than almost anything else; an interior or a guarantee cabin stretches the trip the furthest.",
            "Overlooked itineraries win: repositioning sailings, shorter cruises, and sailing from a port you can drive to instead of flying.",
            "Match the line to your budget; casual lines keep the base fare approachable and sell extras a la carte.",
            "The fastest way to overpay is ignoring the extras. Plan gratuities, drinks and excursions up front.",
        ],
        "es": [
            "El momento del año es la palanca más grande: las temporadas media y las semanas tranquilas son mucho más amables con tu presupuesto que las vacaciones escolares.",
            "El tipo de camarote que eliges mueve la tarifa más que casi cualquier otra cosa; un interior o un camarote garantizado rinde más el viaje.",
            "Los itinerarios olvidados ganan: cruceros de reposicionamiento, cruceros cortos y zarpar desde un puerto al que puedas llegar en auto en vez de volar.",
            "Ajusta la línea a tu presupuesto; las líneas informales mantienen la tarifa base accesible y venden extras a la carta.",
            "La forma más rápida de pagar de más es ignorar los extras. Planea propinas, bebidas y excursiones desde el principio.",
        ],
    },
    "sections": [
        {
            "id": "timing",
            "h2": {"en": "Timing is the biggest lever", "es": "El momento es la palanca más grande"},
            "html": {
                "en": "<p>The same cabin on the same ship can cost very different amounts depending only on the week "
                      "you sail. The pattern is simple: when demand is high, so is the fare.</p>"
                      + vcards([
                          ("🍂", "Sail in shoulder season", "The weeks just before and after peak (for many regions, spring and late autumn) bring calmer prices and thinner crowds."),
                          ("🎓", "Avoid school holidays", "Summer, spring break and the winter holidays are the busiest and priciest windows. A week either side is often far better value."),
                          ("🗓️", "Be flexible on dates", "If you can move your trip by a week or two, you give a specialist real room to find a better fare."),
                      ])
                      + "<p>If your dates are fixed to a holiday period, that is fine, just go in knowing it is the "
                      "least flexible way to book.</p>",
                "es": "<p>El mismo camarote en el mismo barco puede costar montos muy distintos solo según la semana "
                      "en que navegas. El patrón es simple: cuando la demanda es alta, la tarifa también.</p>"
                      + vcards([
                          ("🍂", "Navega en temporada media", "Las semanas justo antes y después del pico (para muchas regiones, primavera y fin de otoño) traen precios más tranquilos y menos gente."),
                          ("🎓", "Evita las vacaciones escolares", "El verano, la Semana Santa y las fiestas de invierno son las ventanas más ocupadas y caras. Una semana antes o después suele valer mucho más."),
                          ("🗓️", "Sé flexible con las fechas", "Si puedes mover el viaje una o dos semanas, le das a un especialista margen real para encontrar mejor tarifa."),
                      ])
                      + "<p>Si tus fechas están fijas a un periodo de vacaciones, está bien, solo ve sabiendo que es "
                      "la forma menos flexible de reservar.</p>",
            },
        },
        {
            "id": "cabin",
            "h2": {"en": "Pick the cabin type that fits the budget", "es": "Elige el tipo de camarote que encaje"},
            "html": {
                "en": "<p>After timing, your cabin choice moves the fare more than anything. You are on the same "
                      "ship, eating the same food and seeing the same ports no matter where you sleep, so if the "
                      "budget is the priority:</p>"
                      "<ul>"
                      "<li><b>An interior cabin</b> is the most budget-friendly room on the ship, and you spend little "
                      "waking time in it anyway.</li>"
                      "<li><b>A guarantee cabin</b> (where you pick the category and the line assigns the exact room) "
                      "often comes at a friendlier fare in exchange for less control over location.</li>"
                      "<li><b>Lower and mid decks</b> and rooms near the elevators tend to be gentler on the wallet than "
                      "prime locations.</li>"
                      "</ul>"
                      + tip("Not sure an interior is for you? Read " + link("/en/guides/choosing-a-cabin/", "choosing a cabin") +
                            " for the trade-offs between interior, oceanview, balcony and suite before you decide.")
                      ,
                "es": "<p>Después del momento, la elección de camarote mueve la tarifa más que nada. Estás en el mismo "
                      "barco, comes la misma comida y ves los mismos puertos sin importar dónde duermas, así que si el "
                      "presupuesto es la prioridad:</p>"
                      "<ul>"
                      "<li><b>Un camarote interior</b> es la habitación más económica del barco, y de todos modos pasas "
                      "poco tiempo despierto en ella.</li>"
                      "<li><b>Un camarote garantizado</b> (eliges la categoría y la línea asigna la habitación exacta) "
                      "suele tener una tarifa más amable a cambio de menos control sobre la ubicación.</li>"
                      "<li><b>Las cubiertas bajas y medias</b> y las habitaciones cerca de los ascensores suelen ser "
                      "más suaves para el bolsillo que las ubicaciones premium.</li>"
                      "</ul>"
                      + tip("¿No sabes si un interior es para ti? Lee " + link("/es/guides/choosing-a-cabin/", "elegir camarote") +
                            " para ver las diferencias entre interior, vista al mar, balcón y suite antes de decidir.")
                      ,
            },
        },
        {
            "id": "itineraries",
            "h2": {"en": "The itineraries most people overlook", "es": "Los itinerarios que casi todos pasan por alto"},
            "html": {
                "en": vcards([
                    ("🔁", "Repositioning cruises", "When ships move between seasons (say Alaska to Mexico), they run one-way sailings with lots of sea days at very approachable fares."),
                    ("⏱️", "Shorter sailings", "A 3 to 5 night cruise is an easy, lower-commitment way to try a line, and a gentler total than a long voyage."),
                    ("🚗", "Drive-to home ports", "Sailing from a port you can drive to instead of flying can save the whole cost of airfare for the family."),
                    ("🏝️", "Quieter weeks & routes", "Less-hyped itineraries and off-peak weeks compete harder for your booking."),
                ]) + "<p>These are exactly the kinds of options a specialist surfaces that a quick search usually will "
                "not, because they are matching your flexibility to what is actually open.</p>",
                "es": vcards([
                    ("🔁", "Cruceros de reposicionamiento", "Cuando los barcos cambian de temporada (por ejemplo de Alaska a México), hacen cruceros de una vía con muchos días de mar a tarifas muy accesibles."),
                    ("⏱️", "Cruceros cortos", "Un crucero de 3 a 5 noches es una forma fácil y de menor compromiso de probar una línea, y un total más suave que un viaje largo."),
                    ("🚗", "Puertos base a los que llegas en auto", "Zarpar desde un puerto al que puedas llegar en auto en vez de volar puede ahorrar todo el costo de los vuelos de la familia."),
                    ("🏝️", "Semanas y rutas más tranquilas", "Los itinerarios menos publicitados y las semanas de temporada baja compiten más por tu reserva."),
                ]) + "<p>Son justo el tipo de opciones que un especialista saca a la luz y que una búsqueda rápida "
                "normalmente no, porque están ajustando tu flexibilidad a lo que de verdad está disponible.</p>",
            },
        },
        {
            "id": "extras",
            "h2": {"en": "Keep the extras from eating the value", "es": "Que los extras no se coman el valor"},
            "html": {
                "en": "<p>A friendly base fare does not help if the onboard account balloons. The extras that quietly "
                      "add up are the same every time: gratuities, drinks, Wi-Fi, specialty dining and shore "
                      "excursions. Decide on each before you sail rather than in the moment.</p>"
                      "<p>Two guides make this easy: " + link("/en/guides/whats-included/", "what is included in a cruise fare") +
                      " and " + link("/en/guides/cruise-gratuities-explained/", "cruise gratuities explained") +
                      ". Between them you will know the real, all-in cost, not just the sticker.</p>",
                "es": "<p>Una tarifa base amable no ayuda si la cuenta a bordo se dispara. Los extras que se acumulan "
                      "en silencio son los mismos siempre: propinas, bebidas, Wi-Fi, restaurantes de especialidad y "
                      "excursiones. Decide cada uno antes de zarpar en lugar de en el momento.</p>"
                      "<p>Dos guías lo hacen fácil: " + link("/es/guides/whats-included/", "qué incluye la tarifa de un crucero") +
                      " y " + link("/es/guides/cruise-gratuities-explained/", "propinas de crucero explicadas") +
                      ". Entre las dos sabrás el costo real y completo, no solo el de la etiqueta.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>The best value comes from stacking small wins: a flexible week, the right cabin type, a "
                      "smarter itinerary, and a plan for the extras. You do not need a gimmick or a countdown timer.</p>"
                      "<p>When you are ready, a specialist does the hunting for you and quotes the best rate our "
                      "partners can offer for your dates. Free, no pressure, and we never take payment for travel. "
                      "Start by telling us how you like to travel with the " + link("/en/compare/", "cruise finder") + ".</p>",
                "es": "<p>El mejor valor viene de sumar pequeñas victorias: una semana flexible, el camarote correcto, "
                      "un itinerario más inteligente y un plan para los extras. No necesitas un truco ni un "
                      "cronómetro.</p>"
                      "<p>Cuando estés listo, un especialista hace la búsqueda por ti y cotiza la mejor tarifa que "
                      "nuestros socios pueden ofrecer para tus fechas. Gratis, sin presión, y nunca cobramos por el "
                      "viaje. Empieza contándonos cómo te gusta viajar con el " + link("/es/compare/", "buscador de cruceros") + ".</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("When is the most affordable time to cruise?", "The shoulder seasons, the quieter weeks just before and after a region's peak, are usually the best value, along with any week outside school holidays. Being flexible by a week or two makes the biggest difference."),
            ("Is it better to book a cruise early or last minute?", "Both can work. Booking early gives you the best cabin choice and time to pay it off; last-minute can suit a flexible traveller with no fixed dates. A specialist can tell you which is better for the sailing you want."),
            ("What is the most affordable cruise line?", "Casual, contemporary lines keep the base fare approachable and sell extras a la carte, which is great value if you are disciplined about add-ons. The right answer depends on how you travel; compare the lines and what is included."),
            ("How do I cruise on a budget?", "Sail in shoulder season, choose an interior or guarantee cabin, look at repositioning or shorter sailings, leave from a port you can drive to, and plan the extras (gratuities, drinks, excursions) up front."),
            ("Are those big cruise discounts real?", "Be careful. Real value comes from timing, cabin choice and itinerary, not from countdown timers or offers that pressure you. If something feels too good to be true, it usually is; see our guide on avoiding cruise scams."),
        ],
        "es": [
            ("¿Cuál es la época más accesible para navegar?", "Las temporadas media, las semanas tranquilas justo antes y después del pico de una región, suelen ser el mejor valor, junto con cualquier semana fuera de las vacaciones escolares. Ser flexible una o dos semanas hace la mayor diferencia."),
            ("¿Conviene reservar con anticipación o a último momento?", "Ambas pueden funcionar. Reservar temprano te da la mejor elección de camarote y tiempo para pagarlo; el último momento puede convenir a un viajero flexible sin fechas fijas. Un especialista puede decirte cuál conviene para el crucero que quieres."),
            ("¿Cuál es la línea de crucero más accesible?", "Las líneas informales mantienen la tarifa base accesible y venden extras a la carta, muy buen valor si eres disciplinado con los adicionales. La respuesta correcta depende de cómo viajas; compara las líneas y lo que incluyen."),
            ("¿Cómo hago un crucero con presupuesto limitado?", "Navega en temporada media, elige un camarote interior o garantizado, mira cruceros de reposicionamiento o cortos, sal desde un puerto al que llegues en auto, y planea los extras (propinas, bebidas, excursiones) desde el principio."),
            ("¿Son reales esas grandes ofertas de crucero?", "Ten cuidado. El valor real viene del momento, el camarote y el itinerario, no de cronómetros ni ofertas que te presionan. Si algo parece demasiado bueno para ser verdad, normalmente lo es; ve nuestra guía para evitar estafas de crucero."),
        ],
    },
    "related": {
        "en": [
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "Know the all-in cost before you book, not just the sticker."),
            ("🛡️", "How to avoid cruise scams", "/en/guides/avoid-cruise-scams/", "Spot the fake-deal red flags before they cost you."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your flexibility; we line up the best-value options."),
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "The cabin choice that stretches the budget furthest."),
        ],
        "es": [
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Conoce el costo completo antes de reservar, no solo la etiqueta."),
            ("🛡️", "Cómo evitar estafas de crucero", "/es/guides/avoid-cruise-scams/", "Detecta las señales de ofertas falsas antes de que te cuesten."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Cuéntanos tu flexibilidad; alineamos las opciones de mejor valor."),
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "La elección de camarote que más estira el presupuesto."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("cruise-deposit-payment-cancellation", {
    "cat": "costs",
    "hero": "cruise-ship-sea.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "Cruise deposits, final payment & cancellation, explained",
        "es": "Depósitos, pago final y cancelación de crucero, explicados",
    },
    "dek": {
        "en": "Booking a cruise runs on a timeline, a deposit to hold it, a final-payment date, and a "
              "cancellation window that tightens as you get closer to sailing. Understand it up front "
              "and you keep control of your money instead of losing it to a missed date.",
        "es": "Reservar un crucero sigue un calendario: un depósito para reservarlo, una fecha de pago "
              "final y una ventana de cancelación que se aprieta a medida que se acerca la salida. "
              "Entiéndelo desde el principio y mantienes el control de tu dinero en lugar de perderlo.",
    },
    "takeaways": {
        "en": [
            "A deposit holds your cabin at today's fare; you pay the balance later, by the final-payment date.",
            "Final payment is typically due a few months before sailing; miss it and the booking can be cancelled automatically.",
            "Cancellation penalties increase in steps as the sailing gets closer, from fully refundable early on to non-refundable near departure.",
            "Refundable and non-refundable fares/deposits behave differently; the non-refundable version usually looks friendlier up front but risks more if plans change.",
            "Travel insurance matters most in hurricane season and for non-refundable bookings.",
        ],
        "es": [
            "Un depósito reserva tu camarote a la tarifa de hoy; pagas el saldo después, en la fecha de pago final.",
            "El pago final suele vencer unos meses antes de zarpar; si lo pierdes, la reserva puede cancelarse automáticamente.",
            "Las penalidades de cancelación aumentan por tramos a medida que se acerca la salida, de totalmente reembolsable al principio a no reembolsable cerca de zarpar.",
            "Las tarifas y depósitos reembolsables y no reembolsables se comportan distinto; la versión no reembolsable suele verse más amable al inicio pero arriesga más si cambian los planes.",
            "El seguro de viaje importa más en temporada de huracanes y en reservas no reembolsables.",
        ],
    },
    "sections": [
        {
            "id": "deposit",
            "h2": {"en": "The deposit: holding your cabin", "es": "El depósito: reservar tu camarote"},
            "html": {
                "en": "<p>When you book, you usually pay a <b>deposit</b> rather than the whole fare. That locks in "
                      "your cabin and the fare at the time of booking, and you settle the rest later. Deposits vary by "
                      "line, cabin and sailing length, and some promotions run reduced or refundable deposits.</p>"
                      + tip("Booking early with a deposit is how you secure the cabin category and location you want "
                            "before they sell out, while spreading the cost over the months before you sail."),
                "es": "<p>Al reservar, normalmente pagas un <b>depósito</b> en lugar de toda la tarifa. Eso fija tu "
                      "camarote y la tarifa del momento de la reserva, y pagas el resto después. Los depósitos varían "
                      "por línea, camarote y duración, y algunas promociones ofrecen depósitos reducidos o "
                      "reembolsables.</p>"
                      + tip("Reservar temprano con un depósito es como aseguras la categoría y ubicación de camarote "
                            "que quieres antes de que se agoten, repartiendo el costo en los meses antes de zarpar."),
            },
        },
        {
            "id": "final-payment",
            "h2": {"en": "Final payment: the date you cannot miss", "es": "Pago final: la fecha que no puedes perder"},
            "html": {
                "en": "<p>The <b>final-payment date</b> is when the balance of your fare is due, typically a few "
                      "months before departure (the exact window varies by line and by how long the cruise is). This "
                      "is the single most important date in the whole process.</p>"
                      + watch("Miss the final-payment date and the line can cancel your booking automatically, and any "
                              "cancellation penalties that already apply can be charged. Put the date in your calendar "
                              "the day you book.")
                      + "<p>The precise final-payment window for each line is one of the facts we track; a specialist "
                      "flags your exact date when you book so it never sneaks up on you.</p>",
                "es": "<p>La <b>fecha de pago final</b> es cuando vence el saldo de tu tarifa, normalmente unos meses "
                      "antes de la salida (la ventana exacta varía por línea y por la duración del crucero). Es la "
                      "fecha más importante de todo el proceso.</p>"
                      + watch("Si pierdes la fecha de pago final, la línea puede cancelar tu reserva automáticamente, y "
                              "pueden cobrarse las penalidades de cancelación que ya apliquen. Pon la fecha en tu "
                              "calendario el día que reserves.")
                      + "<p>La ventana exacta de pago final de cada línea es uno de los datos que seguimos; un "
                      "especialista te marca tu fecha exacta al reservar para que nunca te sorprenda.</p>",
            },
        },
        {
            "id": "cancellation",
            "h2": {"en": "Cancellation: the window that tightens", "es": "Cancelación: la ventana que se aprieta"},
            "html": {
                "en": "<p>Cancellation works on a sliding scale. Far out from your sailing, you can usually cancel "
                      "for a full refund. As you approach departure, penalties step up in stages until, close to "
                      "sailing, the fare is fully non-refundable.</p>"
                      + vcards([
                          ("✅", "Early: fully refundable", "Cancel well before final payment and you typically get everything back (refundable deposits aside)."),
                          ("🟡", "Middle: partial penalty", "As the date nears, you forfeit a growing percentage of the fare in steps."),
                          ("🔴", "Late: non-refundable", "Close to departure the fare is usually lost entirely if you cancel."),
                      ])
                      + "<p>The exact penalty schedule differs by line and voyage length. We keep the current, verified "
                      "version for each line on the " + link("/en/cruise-facts/", "cruise facts") + " page.</p>",
                "es": "<p>La cancelación funciona en escala móvil. Lejos de tu salida, normalmente puedes cancelar con "
                      "reembolso total. Al acercarte a la fecha, las penalidades suben por etapas hasta que, cerca de "
                      "zarpar, la tarifa es totalmente no reembolsable.</p>"
                      + vcards([
                          ("✅", "Temprano: totalmente reembolsable", "Cancela mucho antes del pago final y normalmente recuperas todo (salvo depósitos no reembolsables)."),
                          ("🟡", "Medio: penalidad parcial", "Al acercarse la fecha, pierdes un porcentaje creciente de la tarifa por tramos."),
                          ("🔴", "Tarde: no reembolsable", "Cerca de la salida la tarifa normalmente se pierde por completo si cancelas."),
                      ])
                      + "<p>El calendario exacto de penalidades varía por línea y duración. Llevamos la versión actual "
                      "y verificada de cada línea en la página de " + link("/es/cruise-facts/", "datos de crucero") + ".</p>",
            },
        },
        {
            "id": "refundable-insurance",
            "h2": {"en": "Refundable vs non-refundable, and insurance", "es": "Reembolsable vs no reembolsable, y seguro"},
            "html": {
                "en": "<p>Many lines offer both a <b>refundable</b> and a <b>non-refundable</b> version of a fare or "
                      "deposit. The non-refundable option often looks friendlier at booking, but you forfeit more (or "
                      "pay a change fee) if plans shift. Which is right depends on how certain your dates are.</p>"
                      "<p>This is also where <b>travel insurance</b> earns its keep, especially for non-refundable "
                      "bookings and for sailings during Atlantic hurricane season, when the risk of disruption is "
                      "higher. A specialist can walk you through the trade-off for your trip.</p>",
                "es": "<p>Muchas líneas ofrecen una versión <b>reembolsable</b> y una <b>no reembolsable</b> de una "
                      "tarifa o depósito. La opción no reembolsable suele verse más amable al reservar, pero pierdes "
                      "más (o pagas un cargo por cambio) si los planes cambian. Cuál conviene depende de qué tan "
                      "seguras son tus fechas.</p>"
                      "<p>Aquí también el <b>seguro de viaje</b> demuestra su valor, sobre todo en reservas no "
                      "reembolsables y en cruceros durante la temporada de huracanes del Atlántico, cuando el riesgo "
                      "de interrupción es mayor. Un especialista puede explicarte el equilibrio para tu viaje.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>Three dates keep you in control: the deposit that holds your cabin, the final-payment date "
                      "you must not miss, and where you sit on the cancellation schedule. Get those straight and there "
                      "are no nasty surprises.</p>"
                      "<p>When you book through us, a specialist spells out all three for your exact sailing, plus "
                      "whether a refundable fare or travel insurance is worth it for you. It also helps to read "
                      + link("/en/guides/whats-included/", "what is included in a cruise fare") + " next.</p>",
                "es": "<p>Tres fechas te mantienen en control: el depósito que reserva tu camarote, la fecha de pago "
                      "final que no debes perder, y dónde estás en el calendario de cancelación. Ten eso claro y no "
                      "hay sorpresas desagradables.</p>"
                      "<p>Cuando reservas con nosotros, un especialista te detalla las tres para tu crucero exacto, "
                      "además de si una tarifa reembolsable o un seguro te conviene. También ayuda leer "
                      + link("/es/guides/whats-included/", "qué incluye la tarifa de un crucero") + " a continuación.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("How much is a cruise deposit?", "It varies by line, cabin category and how long the cruise is, and some promotions offer reduced or refundable deposits. A specialist confirms the deposit for your exact sailing when you book."),
            ("When is final payment due on a cruise?", "Typically a few months before departure, though the exact window depends on the line and the length of the cruise. Miss it and the booking can be cancelled automatically, so note the date the day you book."),
            ("What happens if I cancel my cruise?", "It depends on timing. Cancel well before final payment and you usually get a full refund; as departure nears, penalties step up until the fare is non-refundable. The exact schedule varies by line; we track the verified version for each."),
            ("What is the difference between refundable and non-refundable fares?", "A refundable fare or deposit lets you cancel and get money back (up to a point); a non-refundable one often looks friendlier at booking but forfeits more, or charges a change fee, if plans shift."),
            ("Do I need travel insurance for a cruise?", "It is optional but worth serious thought for non-refundable bookings and for sailings in hurricane season, when disruption is more likely. A specialist can walk you through whether it fits your trip."),
        ],
        "es": [
            ("¿Cuánto es el depósito de un crucero?", "Varía por línea, categoría de camarote y duración, y algunas promociones ofrecen depósitos reducidos o reembolsables. Un especialista confirma el depósito de tu crucero exacto al reservar."),
            ("¿Cuándo vence el pago final de un crucero?", "Normalmente unos meses antes de la salida, aunque la ventana exacta depende de la línea y la duración. Si lo pierdes, la reserva puede cancelarse automáticamente, así que anota la fecha el día que reserves."),
            ("¿Qué pasa si cancelo mi crucero?", "Depende del momento. Cancela mucho antes del pago final y normalmente recuperas todo; al acercarse la salida, las penalidades suben hasta que la tarifa es no reembolsable. El calendario exacto varía por línea; seguimos la versión verificada de cada una."),
            ("¿Cuál es la diferencia entre tarifas reembolsables y no reembolsables?", "Una tarifa o depósito reembolsable te deja cancelar y recuperar dinero (hasta cierto punto); una no reembolsable suele verse más amable al reservar pero pierde más, o cobra un cargo por cambio, si cambian los planes."),
            ("¿Necesito seguro de viaje para un crucero?", "Es opcional pero merece pensarse bien en reservas no reembolsables y en cruceros en temporada de huracanes, cuando la interrupción es más probable. Un especialista puede explicarte si conviene para tu viaje."),
        ],
    },
    "related": {
        "en": [
            ("💸", "The cruise facts that cost you money", "/en/cruise-facts/", "The verified cancellation and final-payment terms for every line."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "Know the all-in cost before you commit a deposit."),
            ("🛡️", "How to avoid cruise scams", "/en/guides/avoid-cruise-scams/", "Protect your deposit from pressure tactics and fake offers."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Line up your options; one call books the right one."),
        ],
        "es": [
            ("💸", "Datos de crucero que cuestan dinero", "/es/cruise-facts/", "Los términos verificados de cancelación y pago final de cada línea."),
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Conoce el costo completo antes de comprometer un depósito."),
            ("🛡️", "Cómo evitar estafas de crucero", "/es/guides/avoid-cruise-scams/", "Protege tu depósito de tácticas de presión y ofertas falsas."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Alinea tus opciones; una llamada reserva la correcta."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("drink-packages-worth-it", {
    "cat": "costs",
    "hero": "cruise-drinks.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "Cruise drink packages: are they worth it? (and the whole-cabin rule)",
        "es": "Paquetes de bebidas: ¿valen la pena? (y la regla de todo el camarote)",
    },
    "dek": {
        "en": "A drink package can turn a running bar tab into one predictable number, or it can be "
              "money you did not need to spend. Here is how to tell which, plus the whole-cabin rule "
              "that catches so many people off guard.",
        "es": "Un paquete de bebidas puede convertir una cuenta de bar que crece en un solo número "
              "predecible, o en dinero que no necesitabas gastar. Aquí te decimos cómo saberlo, además "
              "de la regla de todo el camarote que sorprende a tanta gente.",
    },
    "takeaways": {
        "en": [
            "A drink package makes sense if you will drink enough each day to pass its break-even point; light drinkers usually come out ahead paying as they go.",
            "The whole-cabin rule: on most lines, if one adult buys the alcohol package, every adult of drinking age in that cabin must buy it too.",
            "Non-drinkers and kids can often take a cheaper soda or zero-proof package instead.",
            "Read what the package actually covers, some exclude premium pours, bottled water, specialty coffee or mini-bar.",
            "Wi-Fi is usually sold the same way, in per-device or per-cabin tiers.",
        ],
        "es": [
            "Un paquete de bebidas tiene sentido si beberás lo suficiente cada día para pasar su punto de equilibrio; quien bebe poco suele salir mejor pagando sobre la marcha.",
            "La regla de todo el camarote: en la mayoría de líneas, si un adulto compra el paquete de alcohol, todos los adultos en edad de beber del camarote también deben comprarlo.",
            "Quienes no beben y los niños suelen poder tomar un paquete de refrescos o sin alcohol, más económico.",
            "Lee qué cubre realmente el paquete, algunos excluyen tragos premium, agua embotellada, café de especialidad o minibar.",
            "El Wi-Fi normalmente se vende igual, por niveles por dispositivo o por camarote.",
        ],
    },
    "sections": [
        {
            "id": "how-they-work",
            "h2": {"en": "How drink packages work", "es": "Cómo funcionan los paquetes de bebidas"},
            "html": {
                "en": "<p>A drink package is a flat, per-day price that covers drinks up to a certain value, for the "
                      "whole cruise. Lines offer tiers: a full alcohol package, a refreshment or soda package, and "
                      "sometimes a water or specialty-coffee package. You pay per day of the sailing, not per drink.</p>"
                      + define("Break-even point",
                               "the number of drinks per day at which the package costs the same as paying individually. "
                               "Below it you overpay for the package; above it the package wins."),
                "es": "<p>Un paquete de bebidas es un precio fijo por día que cubre bebidas hasta cierto valor, durante "
                      "todo el crucero. Las líneas ofrecen niveles: un paquete completo de alcohol, uno de refrescos, y "
                      "a veces uno de agua o café de especialidad. Pagas por día del crucero, no por bebida.</p>"
                      + define("Punto de equilibrio",
                               "el número de bebidas al día en que el paquete cuesta lo mismo que pagar individualmente. "
                               "Por debajo pagas de más por el paquete; por encima, el paquete gana."),
            },
        },
        {
            "id": "whole-cabin-rule",
            "h2": {"en": "The whole-cabin rule", "es": "La regla de todo el camarote"},
            "html": {
                "en": watch("On most major lines, if <b>one adult</b> in a stateroom buys the alcohol package, "
                            "<b>every</b> adult of legal drinking age in that same cabin has to buy it too. It exists to "
                            "stop one person sharing a package with the whole room.")
                      + "<p>This is the detail that most often turns a good-value package into an expensive one. If "
                      "only one of two adults in the cabin really drinks, buying the package for both can wipe out the "
                      "value. There are usually exceptions for children, for teens on a zero-proof package, and for "
                      "medical or pregnancy cases, so it is always worth asking.</p>",
                "es": watch("En la mayoría de las líneas, si <b>un adulto</b> del camarote compra el paquete de "
                            "alcohol, <b>todos</b> los adultos en edad legal de beber de ese mismo camarote también "
                            "deben comprarlo. Existe para evitar que una persona comparta un paquete con toda la "
                            "habitación.")
                      + "<p>Este es el detalle que más a menudo convierte un paquete de buen valor en uno caro. Si "
                      "solo uno de dos adultos del camarote bebe de verdad, comprar el paquete para ambos puede anular "
                      "el valor. Suele haber excepciones para niños, para adolescentes con un paquete sin alcohol y "
                      "para casos médicos o de embarazo, así que siempre vale la pena preguntar.</p>",
            },
        },
        {
            "id": "worth-it",
            "h2": {"en": "Is a package worth it for you?", "es": "¿Vale la pena un paquete para ti?"},
            "html": {
                "en": "<p>Do the honest maths for a single day, then multiply by how you really travel:</p>"
                      + vcards([
                          ("👍", "A package often wins if", "You enjoy several cocktails or glasses of wine a day, or you love specialty coffees and bottled drinks, every day of the cruise."),
                          ("👎", "Paying as you go often wins if", "You drink lightly, take some days off, or one adult in the cabin barely drinks (remember the whole-cabin rule)."),
                          ("🧒", "For non-drinkers & kids", "A soda or zero-proof package is far cheaper, and children usually cannot be on an alcohol package anyway."),
                      ])
                      + tip("Packages reward heavy, consistent use. If you are not sure you will drink enough every "
                            "day to clear the break-even point, you probably will not, and paying per drink keeps you "
                            "in control."),
                "es": "<p>Haz la cuenta honesta para un solo día, luego multiplica por cómo viajas de verdad:</p>"
                      + vcards([
                          ("👍", "Un paquete suele ganar si", "Disfrutas varios cócteles o copas de vino al día, o te encantan los cafés de especialidad y las bebidas embotelladas, todos los días del crucero."),
                          ("👎", "Pagar sobre la marcha suele ganar si", "Bebes poco, tomas algunos días de descanso, o un adulto del camarote casi no bebe (recuerda la regla de todo el camarote)."),
                          ("🧒", "Para quienes no beben y niños", "Un paquete de refrescos o sin alcohol es mucho más barato, y los niños normalmente no pueden estar en un paquete de alcohol."),
                      ])
                      + tip("Los paquetes premian el uso alto y constante. Si no estás seguro de que beberás lo "
                            "suficiente cada día para pasar el punto de equilibrio, probablemente no lo harás, y pagar "
                            "por bebida te mantiene en control."),
            },
        },
        {
            "id": "fine-print",
            "h2": {"en": "The fine print to check", "es": "La letra pequeña que revisar"},
            "html": {
                "en": "<p>Before you commit, confirm what the package really includes:</p>"
                      "<ul>"
                      "<li>Is there a per-drink value cap that excludes premium pours?</li>"
                      "<li>Does it cover bottled water, specialty coffee, fresh juice and the mini-bar, or just the basics?</li>"
                      "<li>Are gratuities on the package included, or added separately?</li>"
                      "<li>Does it work at every bar and venue, including the private island?</li>"
                      "</ul>"
                      "<p>The exact package rules differ by line and change over time, so we keep the current, verified "
                      "version for each on the " + link("/en/cruise-facts/", "cruise facts") + " page.</p>",
                "es": "<p>Antes de decidir, confirma qué incluye realmente el paquete:</p>"
                      "<ul>"
                      "<li>¿Hay un tope de valor por bebida que excluya los tragos premium?</li>"
                      "<li>¿Cubre agua embotellada, café de especialidad, jugo fresco y el minibar, o solo lo básico?</li>"
                      "<li>¿Las propinas del paquete están incluidas o se añaden aparte?</li>"
                      "<li>¿Funciona en todos los bares y lugares, incluida la isla privada?</li>"
                      "</ul>"
                      "<p>Las reglas exactas varían por línea y cambian con el tiempo, así que llevamos la versión "
                      "actual y verificada de cada una en la página de " + link("/es/cruise-facts/", "datos de crucero") + ".</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>A drink package is worth it when you will genuinely use it every day and both adults in "
                      "the cabin drink; otherwise, paying as you go usually keeps more in your pocket. Either way, the "
                      "whole-cabin rule is the thing to check first.</p>"
                      "<p>Tell a specialist how you actually drink and they will tell you, honestly, whether a package "
                      "pays off for your sailing. It also helps to read "
                      + link("/en/guides/whats-included/", "what is included in a cruise fare") + " next.</p>",
                "es": "<p>Un paquete de bebidas vale la pena cuando de verdad lo usarás todos los días y ambos adultos "
                      "del camarote beben; si no, pagar sobre la marcha suele dejarte más en el bolsillo. En cualquier "
                      "caso, la regla de todo el camarote es lo primero a revisar.</p>"
                      "<p>Cuéntale a un especialista cómo bebes de verdad y te dirá, con honestidad, si un paquete "
                      "conviene para tu crucero. También ayuda leer "
                      + link("/es/guides/whats-included/", "qué incluye la tarifa de un crucero") + " a continuación.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("Are cruise drink packages worth it?", "Yes if you will drink enough each day to clear the package's break-even point, and both adults in the cabin drink. Light or occasional drinkers usually pay less by ordering as they go."),
            ("Does everyone in the cabin have to buy the drink package?", "On most major lines, yes, for the alcohol package: if one adult buys it, every adult of drinking age in the same stateroom must buy it too. There are usually exceptions for children and medical cases."),
            ("Do kids need a drink package?", "No. Children cannot be on an alcohol package, and a cheaper soda or zero-proof package is optional. Water, milk and juice at meals are typically included in the fare anyway."),
            ("What does a cruise drink package include?", "It varies by line and tier, usually cocktails, beer, wine by the glass, sodas and often specialty coffee and bottled water, up to a per-drink value cap. Always check the exclusions before you buy."),
            ("Is Wi-Fi included, or a separate package?", "Usually separate. Most lines sell tiered internet packages, per device or per cabin, and a few premium fares include a basic tier. Check the current policy for your line."),
        ],
        "es": [
            ("¿Valen la pena los paquetes de bebidas?", "Sí, si beberás lo suficiente cada día para pasar el punto de equilibrio y ambos adultos del camarote beben. Quien bebe poco u ocasionalmente suele pagar menos ordenando sobre la marcha."),
            ("¿Todos en el camarote deben comprar el paquete de bebidas?", "En la mayoría de líneas, sí, para el paquete de alcohol: si un adulto lo compra, todos los adultos en edad de beber del mismo camarote también deben comprarlo. Suele haber excepciones para niños y casos médicos."),
            ("¿Los niños necesitan un paquete de bebidas?", "No. Los niños no pueden estar en un paquete de alcohol, y un paquete de refrescos o sin alcohol es opcional. Agua, leche y jugo en las comidas suelen estar incluidos en la tarifa."),
            ("¿Qué incluye un paquete de bebidas?", "Varía por línea y nivel, normalmente cócteles, cerveza, vino por copa, refrescos y a menudo café de especialidad y agua embotellada, hasta un tope de valor por bebida. Revisa siempre las exclusiones antes de comprar."),
            ("¿El Wi-Fi está incluido o es un paquete aparte?", "Normalmente aparte. La mayoría de líneas venden paquetes de internet por niveles, por dispositivo o por camarote, y algunas tarifas premium incluyen un nivel básico. Revisa la política actual de tu línea."),
        ],
    },
    "related": {
        "en": [
            ("💸", "The cruise facts that cost you money", "/en/cruise-facts/", "The verified drink-package rules for every line, plus gratuities and Wi-Fi."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "What your fare covers before you add any package."),
            ("💰", "How to find an affordable cruise", "/en/guides/how-to-find-affordable-cruise/", "Where a package fits into keeping the trip good value."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "One call and we'll tell you if a package pays off for you."),
        ],
        "es": [
            ("💸", "Datos de crucero que cuestan dinero", "/es/cruise-facts/", "Las reglas verificadas de paquetes de bebidas de cada línea, más propinas y Wi-Fi."),
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Qué cubre tu tarifa antes de añadir cualquier paquete."),
            ("💰", "Cómo encontrar un crucero accesible", "/es/guides/how-to-find-affordable-cruise/", "Dónde encaja un paquete para mantener el viaje con buen valor."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Una llamada y te decimos si un paquete conviene para ti."),
        ],
    },
})
