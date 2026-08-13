# -*- coding: utf-8 -*-
"""Rich guides cluster: dest. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("how-to-choose-a-destination", {
    "cat": "dest",
    "hero": "how-to-choose-a-destination.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "How to choose a cruise destination",
        "es": "Cómo elegir un destino de crucero",
    },
    "dek": {
        "en": "Where you sail shapes everything: the weather, the pace, the type of day in port, even "
              "which ship you end up on. Here is a simple way to pick the region that fits your trip, "
              "and the one detail that matters more than any other.",
        "es": "A dónde navegas moldea todo: el clima, el ritmo, el tipo de día en puerto, incluso en "
              "qué barco terminas. Aquí tienes una forma simple de elegir la región que encaja con tu "
              "viaje, y el detalle que importa más que cualquier otro.",
    },
    "takeaways": {
        "en": [
            "Season beats almost everything: every region has a window when the weather and scenery are at their best.",
            "Match the type of trip you want, beach and sun, dramatic scenery, culture and history, or a bucket-list transit.",
            "Think about how you get to the ship: sailing from a port you can drive to can make the whole trip simpler and better value.",
            "Beach regions (Caribbean, Bahamas, Mexico) are easy year-round-ish; scenery regions (Alaska, Northern Europe) have short, specific seasons.",
            "Not sure? Start from your dates and let the season point you to the region that is actually in its prime.",
        ],
        "es": [
            "La temporada le gana a casi todo: cada región tiene una ventana en que el clima y el paisaje están en su mejor momento.",
            "Ajusta el tipo de viaje que quieres: playa y sol, paisaje impresionante, cultura e historia, o un tránsito de lista de deseos.",
            "Piensa en cómo llegas al barco: zarpar desde un puerto al que puedas llegar en auto puede hacer todo más simple y de mejor valor.",
            "Las regiones de playa (Caribe, Bahamas, México) son fáciles casi todo el año; las de paisaje (Alaska, Norte de Europa) tienen temporadas cortas y específicas.",
            "¿No sabes? Empieza por tus fechas y deja que la temporada te señale la región que está en su mejor momento.",
        ],
    },
    "sections": [
        {
            "id": "season-first",
            "h2": {"en": "Start with the season", "es": "Empieza por la temporada"},
            "html": {
                "en": "<p>The most common mistake is picking a place and forcing your dates to fit. Flip it. Every "
                      "cruise region runs on a season, and sailing in the right window means better weather, calmer "
                      "seas and the scenery you came for.</p>"
                      + tip("Alaska only really sails May to September. The Caribbean is warm most of the year but "
                            "overlaps Atlantic hurricane season in late summer and autumn. Northern Europe shines in "
                            "the long-daylight summer. Get the season right and half the decision is made.")
                      + "<p>Our " + link("/en/destinations/", "destinations") + " section lays out the best time to "
                      "sail for each region, with the home ports and the ships that go.</p>",
                "es": "<p>El error más común es elegir un lugar y forzar las fechas a encajar. Dale la vuelta. Cada "
                      "región de crucero tiene su temporada, y navegar en la ventana correcta significa mejor clima, "
                      "mares más tranquilos y el paisaje por el que fuiste.</p>"
                      + tip("Alaska realmente solo navega de mayo a septiembre. El Caribe es cálido casi todo el año "
                            "pero coincide con la temporada de huracanes del Atlántico a fin de verano y otoño. El "
                            "Norte de Europa brilla en el verano de días largos. Acierta la temporada y media decisión "
                            "está tomada.")
                      + "<p>Nuestra sección de " + link("/es/destinations/", "destinos") + " muestra la mejor época "
                      "para navegar en cada región, con los puertos base y los barcos que van.</p>",
            },
        },
        {
            "id": "type-of-trip",
            "h2": {"en": "Match the type of trip you want", "es": "Ajusta el tipo de viaje que quieres"},
            "html": {
                "en": vcards([
                    ("🏝️", "Beach & sun", "The Caribbean, Bahamas and Mexican Riviera: warm water, easy port days, private islands. Great for first-timers and families."),
                    ("🏔️", "Dramatic scenery", "Alaska and the Norwegian fjords: glaciers, mountains and wildlife. Expect more sea-viewing and a shorter season."),
                    ("🏛️", "Culture & history", "The Mediterranean and Northern Europe: ancient cities, art and grand capitals, port-intensive and full of days off the ship."),
                    ("🛳️", "Bucket-list transits", "The Panama Canal or a transatlantic crossing: the voyage itself is the destination, with lots of sea days."),
                ]),
                "es": vcards([
                    ("🏝️", "Playa y sol", "El Caribe, Bahamas y la Riviera Mexicana: agua cálida, días de puerto fáciles, islas privadas. Ideal para primerizos y familias."),
                    ("🏔️", "Paisaje impresionante", "Alaska y los fiordos noruegos: glaciares, montañas y fauna. Espera más contemplación desde el barco y una temporada más corta."),
                    ("🏛️", "Cultura e historia", "El Mediterráneo y el Norte de Europa: ciudades antiguas, arte y grandes capitales, con muchos puertos y días fuera del barco."),
                    ("🛳️", "Tránsitos de lista de deseos", "El Canal de Panamá o un cruce transatlántico: el viaje en sí es el destino, con muchos días de mar."),
                ]),
            },
        },
        {
            "id": "getting-there",
            "h2": {"en": "Factor in how you get to the ship", "es": "Considera cómo llegas al barco"},
            "html": {
                "en": "<p>A destination is only as easy as getting to its departure port. Two travellers eyeing the "
                      "same warm beaches might have very different trips depending on where they sail from.</p>"
                      "<ul>"
                      "<li><b>Drive-to ports</b> (for many US travellers, Florida, Texas or the Northeast) can remove "
                      "the cost and hassle of flights entirely.</li>"
                      "<li><b>Fly-to and one-way itineraries</b> (Alaska Gulf cruises, most of Europe) need more "
                      "planning and add airfare, but open up bucket-list regions.</li>"
                      "</ul>"
                      "<p>If keeping it simple and good value matters, start from the ports near you and see where they "
                      "sail. If the region is the dream, we help you plan the rest.</p>",
                "es": "<p>Un destino es tan fácil como llegar a su puerto de salida. Dos viajeros que miran las mismas "
                      "playas cálidas pueden tener viajes muy distintos según desde dónde zarpen.</p>"
                      "<ul>"
                      "<li>Los <b>puertos a los que llegas en auto</b> (para muchos viajeros de EE.UU., Florida, Texas "
                      "o el noreste) pueden eliminar por completo el costo y la molestia de los vuelos.</li>"
                      "<li>Los <b>itinerarios a los que vuelas o de una vía</b> (cruceros por el Golfo de Alaska, casi "
                      "toda Europa) requieren más planificación y añaden vuelos, pero abren regiones de lista de "
                      "deseos.</li>"
                      "</ul>"
                      "<p>Si mantenerlo simple y con buen valor importa, empieza por los puertos cerca de ti y mira a "
                      "dónde navegan. Si la región es el sueño, te ayudamos a planear el resto.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>Choose the season first, match the region to the type of trip you want, and factor in how "
                      "you will reach the ship. Do that and you end up in the right place at the right time, which "
                      "matters far more than which specific island you visit.</p>"
                      "<p>Browse the " + link("/en/destinations/", "destination guides") + " to see each region's best "
                      "season, home ports and ships, then tell us your dates and a specialist matches you to the "
                      "sailing that fits.</p>",
                "es": "<p>Elige la temporada primero, ajusta la región al tipo de viaje que quieres, y considera cómo "
                      "llegarás al barco. Haz eso y terminarás en el lugar correcto en el momento correcto, lo que "
                      "importa mucho más que qué isla específica visitas.</p>"
                      "<p>Explora las " + link("/es/destinations/", "guías de destinos") + " para ver la mejor "
                      "temporada, los puertos base y los barcos de cada región, luego dinos tus fechas y un "
                      "especialista te empareja con el crucero que encaja.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("How do I choose a cruise destination?", "Start with the season, every region has a window when it is at its best, then match the region to the type of trip you want (beach, scenery, culture or a bucket-list transit), and factor in how easily you can reach the departure port."),
            ("What is the best cruise destination for first-timers?", "Warm, easy beach regions like the Caribbean and Bahamas are ideal for a first cruise: reliable weather, short flights or a drive to the port, and relaxed port days. They are also great value and very family-friendly."),
            ("When is the best time to cruise Alaska?", "Alaska sails roughly May to September only, with the peak summer months offering the warmest, driest weather and the most wildlife. Outside that window the ships are simply not there."),
            ("Is the Caribbean good to cruise year-round?", "Largely yes, it is warm most of the year, but late summer and autumn overlap Atlantic hurricane season, when sailings still operate and reroute but travel insurance matters more. See the Caribbean destination guide for the month-by-month picture."),
            ("Does it matter which port I sail from?", "Yes. Sailing from a port you can drive to can remove airfare and hassle entirely, while some regions only run from fly-to or one-way ports. Where you leave from can shape the value and simplicity of the whole trip."),
        ],
        "es": [
            ("¿Cómo elijo un destino de crucero?", "Empieza por la temporada, cada región tiene una ventana en que está en su mejor momento, luego ajusta la región al tipo de viaje que quieres (playa, paisaje, cultura o un tránsito de lista de deseos), y considera qué tan fácil llegas al puerto de salida."),
            ("¿Cuál es el mejor destino para primerizos?", "Las regiones de playa cálidas y fáciles como el Caribe y Bahamas son ideales para un primer crucero: clima confiable, vuelos cortos o llegar en auto al puerto, y días de puerto relajados. También son de buen valor y muy familiares."),
            ("¿Cuándo es la mejor época para navegar a Alaska?", "Alaska navega aproximadamente solo de mayo a septiembre, con los meses de verano ofreciendo el clima más cálido y seco y la mayor fauna. Fuera de esa ventana los barcos simplemente no están ahí."),
            ("¿El Caribe es bueno para navegar todo el año?", "En gran medida sí, es cálido casi todo el año, pero el fin de verano y el otoño coinciden con la temporada de huracanes del Atlántico, cuando los cruceros operan y se redirigen pero el seguro importa más. Ve la guía del Caribe para el detalle mes a mes."),
            ("¿Importa desde qué puerto zarpo?", "Sí. Zarpar desde un puerto al que llegas en auto puede eliminar vuelos y molestias, mientras que algunas regiones solo salen de puertos a los que vuelas o de una vía. Desde dónde sales puede moldear el valor y la simplicidad de todo el viaje."),
        ],
    },
    "related": {
        "en": [
            ("🗺️", "Cruise destinations", "/en/destinations/", "Every region's best season, home ports and the ships that sail there."),
            ("🗓️", "When to cruise", "/en/guides/when-to-cruise/", "Season by season, region by region."),
            ("🚢", "How to choose a cruise line", "/en/guides/how-to-choose-a-cruise-line/", "Once you have a region, pick the line that fits."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your dates; we'll match the region and sailing."),
        ],
        "es": [
            ("🗺️", "Destinos de crucero", "/es/destinations/", "La mejor temporada, puertos base y barcos de cada región."),
            ("🗓️", "Cuándo hacer un crucero", "/es/guides/when-to-cruise/", "Temporada por temporada, región por región."),
            ("🚢", "Cómo elegir una línea de crucero", "/es/guides/how-to-choose-a-cruise-line/", "Cuando tengas la región, elige la línea que encaja."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos tus fechas; emparejamos la región y el crucero."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("when-to-cruise", {
    "cat": "dest", "hero": "when-to-cruise.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "When to cruise: the best time to sail, by region", "es": "Cuándo hacer un crucero: la mejor época, por región"},
    "dek": {
        "en": "The week you sail shapes your trip more than almost anything else: the weather, the "
              "scenery, the crowds. Here is how each cruise region runs on a season, and how to time "
              "your trip so everything lines up.",
        "es": "La semana en que navegas moldea tu viaje más que casi cualquier otra cosa: el clima, el "
              "paisaje, la gente. Aquí verás cómo cada región tiene su temporada, y cómo programar tu "
              "viaje para que todo encaje.",
    },
    "takeaways": {
        "en": [
            "Every region has a season: sail in its window and you get the best weather, calmest seas and the scenery you came for.",
            "Alaska is a short May to September window; the Caribbean is warm most of the year but overlaps hurricane season in late summer and autumn.",
            "Shoulder seasons (just before and after peak) bring thinner crowds and better value.",
            "School holidays are the busiest and priciest weeks; a week either side is often far better.",
            "Start from your dates and let the season point you to the region that is in its prime.",
        ],
        "es": [
            "Cada región tiene su temporada: navega en su ventana y tendrás el mejor clima, mares más tranquilos y el paisaje por el que fuiste.",
            "Alaska es una ventana corta de mayo a septiembre; el Caribe es cálido casi todo el año pero coincide con la temporada de huracanes a fin de verano y otoño.",
            "Las temporadas media (justo antes y después del pico) traen menos gente y mejor valor.",
            "Las vacaciones escolares son las semanas más ocupadas y caras; una semana antes o después suele ser mucho mejor.",
            "Empieza por tus fechas y deja que la temporada te señale la región en su mejor momento.",
        ],
    },
    "sections": [
        {"id": "season-rules", "h2": {"en": "Why season beats everything", "es": "Por qué la temporada le gana a todo"},
         "html": {
            "en": "<p>The same destination can be wonderful or washed-out depending only on the month. Sailing in a "
                  "region's season means warmer, drier weather, calmer seas and the experiences you pictured, whether "
                  "that is a glacier calving in Alaska or a beach day in the Caribbean.</p>"
                  + tip("If your dates are flexible, decide the season first and let it choose the region. If your "
                        "dates are fixed, let them point you to whichever region is at its best that week."),
            "es": "<p>El mismo destino puede ser maravilloso o deslucido según solo el mes. Navegar en la temporada de "
                  "una región significa clima más cálido y seco, mares más tranquilos y las experiencias que "
                  "imaginaste, sea un glaciar desprendiéndose en Alaska o un día de playa en el Caribe.</p>"
                  + tip("Si tus fechas son flexibles, decide la temporada primero y deja que elija la región. Si tus "
                        "fechas son fijas, deja que te señalen qué región está en su mejor momento esa semana."),
         }},
        {"id": "by-region", "h2": {"en": "Best time to sail, region by region", "es": "Mejor época, región por región"},
         "html": {
            "en": vcards([
                ("🏔️", "Alaska", "May to September only, peak summer is warmest and best for wildlife."),
                ("🏝️", "Caribbean & Bahamas", "Warm year-round; drier and calmest in winter and spring. Late summer to autumn is Atlantic hurricane season."),
                ("🏛️", "Mediterranean", "April to October, spring and autumn are pleasant and less crowded than high summer."),
                ("🍁", "Canada & New England", "May to October, with September to October the classic fall-colour window."),
                ("🌵", "Mexican Riviera", "Best in the cooler, drier months from autumn to spring."),
                ("🏰", "Northern Europe", "May to August, for the long-daylight Nordic summer."),
            ]) + "<p>The " + link("/en/destinations/", "destinations") + " section has the month-by-month picture for "
            "each region, with the ships that sail it.</p>",
            "es": vcards([
                ("🏔️", "Alaska", "Solo de mayo a septiembre, el pico del verano es lo más cálido y mejor para la fauna."),
                ("🏝️", "Caribe y Bahamas", "Cálido todo el año; más seco y tranquilo en invierno y primavera. De fin de verano a otoño es temporada de huracanes."),
                ("🏛️", "Mediterráneo", "Abril a octubre, primavera y otoño son agradables y con menos gente que pleno verano."),
                ("🍁", "Canadá y Nueva Inglaterra", "Mayo a octubre, con septiembre-octubre la ventana clásica del follaje otoñal."),
                ("🌵", "Riviera Mexicana", "Mejor en los meses más frescos y secos, de otoño a primavera."),
                ("🏰", "Norte de Europa", "Mayo a agosto, por el verano nórdico de días largos."),
            ]) + "<p>La sección de " + link("/es/destinations/", "destinos") + " tiene el detalle mes a mes de cada "
            "región, con los barcos que la navegan.</p>",
         }},
        {"id": "crowds-value", "h2": {"en": "Crowds, value and shoulder season", "es": "Gente, valor y temporada media"},
         "html": {
            "en": "<p>Within a region's season, timing still matters. <b>School holidays</b>, summer, spring break and "
                  "the winter holidays, are the busiest and priciest. The <b>shoulder weeks</b> just before and after "
                  "peak bring thinner crowds, calmer ships and better value, often with weather that is nearly as "
                  "good.</p>"
                  + watch("In the Caribbean and Bahamas, late summer through autumn overlaps Atlantic hurricane season. Sailings still operate and reroute when needed, but travel insurance matters more in those months."),
            "es": "<p>Dentro de la temporada de una región, el momento aún importa. Las <b>vacaciones escolares</b>, "
                  "verano, Semana Santa y fiestas de invierno, son las más ocupadas y caras. Las <b>semanas de "
                  "temporada media</b> justo antes y después del pico traen menos gente, barcos más tranquilos y mejor "
                  "valor, a menudo con clima casi igual de bueno.</p>"
                  + watch("En el Caribe y Bahamas, de fin de verano a otoño coincide con la temporada de huracanes del Atlántico. Los cruceros operan y se redirigen cuando hace falta, pero el seguro de viaje importa más en esos meses."),
         }},
    ],
    "faqs": {
        "en": [
            ("When is the best time to cruise?", "It depends on the region, each has a season when the weather and scenery are at their best. Broadly: Alaska May to September, the Caribbean drier in winter and spring, the Mediterranean April to October. Shoulder weeks give the best mix of good weather and value."),
            ("When is the best time to cruise Alaska?", "May to September only, when the ships are there. Peak summer (June to August) is the warmest and driest and best for wildlife; the shoulder months can be quieter and better value."),
            ("Is it safe to cruise the Caribbean during hurricane season?", "Sailings operate through Atlantic hurricane season (roughly June to November) and reroute around storms when needed. It is generally fine, but travel insurance matters more, and itineraries can change at short notice."),
            ("When is the most affordable time to cruise?", "Outside school holidays, in a region's shoulder weeks, tends to offer the best value along with thinner crowds. Being flexible by a week or two makes the biggest difference; see our affordable-cruise guide."),
            ("How far ahead should I book a cruise?", "For the best cabin choice and dates, book several months to a year ahead, especially for peak weeks, Alaska and holiday sailings. A specialist can tell you whether booking early or late suits the sailing you want."),
        ],
        "es": [
            ("¿Cuándo es la mejor época para un crucero?", "Depende de la región, cada una tiene una temporada cuando el clima y el paisaje están en su mejor momento. En general: Alaska de mayo a septiembre, el Caribe más seco en invierno y primavera, el Mediterráneo de abril a octubre. Las semanas de temporada media dan la mejor mezcla de buen clima y valor."),
            ("¿Cuándo es la mejor época para Alaska?", "Solo de mayo a septiembre, cuando los barcos están ahí. El pico del verano (junio a agosto) es lo más cálido y seco y mejor para la fauna; los meses de temporada media pueden ser más tranquilos y de mejor valor."),
            ("¿Es seguro navegar el Caribe en temporada de huracanes?", "Los cruceros operan durante la temporada de huracanes del Atlántico (aproximadamente junio a noviembre) y se redirigen alrededor de las tormentas cuando hace falta. En general está bien, pero el seguro importa más, y los itinerarios pueden cambiar con poco aviso."),
            ("¿Cuándo es la época más económica para un crucero?", "Fuera de las vacaciones escolares, en las semanas de temporada media de una región, suele ofrecer el mejor valor junto con menos gente. Ser flexible una o dos semanas hace la mayor diferencia; ve nuestra guía de crucero accesible."),
            ("¿Con cuánta anticipación debo reservar?", "Para la mejor elección de camarote y fechas, reserva de varios meses a un año antes, sobre todo para semanas pico, Alaska y cruceros de fiestas. Un especialista puede decirte si reservar temprano o tarde conviene para el crucero que quieres."),
        ],
    },
    "related": {
        "en": [
            ("🗺️", "Cruise destinations", "/en/destinations/", "Every region's best season, ports and ships."),
            ("🗺️", "How to choose a destination", "/en/guides/how-to-choose-a-destination/", "Turn the right season into the right region."),
            ("💰", "How to find an affordable cruise", "/en/guides/how-to-find-affordable-cruise/", "Timing is the single biggest value lever."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your dates; we'll match the region in season."),
        ],
        "es": [
            ("🗺️", "Destinos de crucero", "/es/destinations/", "La mejor temporada, puertos y barcos de cada región."),
            ("🗺️", "Cómo elegir un destino", "/es/guides/how-to-choose-a-destination/", "Convierte la temporada correcta en la región correcta."),
            ("💰", "Cómo encontrar un crucero accesible", "/es/guides/how-to-find-affordable-cruise/", "El momento es la mayor palanca de valor."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos tus fechas; emparejamos la región en temporada."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("caribbean-vs-alaska-vs-med", {
    "cat": "dest",
    "hero": "caribbean-vs-alaska-vs-med.jpg",
    "published": "2026-08-13",
    "updated": "2026-08-13",
    "title": {
        "en": "Caribbean vs Alaska vs Mediterranean: how to decide",
        "es": "Caribe vs Alaska vs Mediterráneo: cómo decidir",
    },
    "dek": {
        "en": "These three account for most first cruises, and people usually pick by photograph. That is "
              "the wrong instrument. They differ in when you can go, how much you pack, what a day ashore "
              "asks of you, and how tiring the week is. Here is the honest comparison.",
        "es": "Estos tres concentran la mayoría de los primeros cruceros, y la gente suele elegir por una "
              "foto. Es el instrumento equivocado. Se diferencian en cuándo puedes ir, cuánto equipaje "
              "llevas, qué te exige un día en tierra y cuánto cansa la semana. Esta es la comparación honesta.",
    },
    "takeaways": {
        "en": [
            "Season decides more than preference. Alaska runs roughly May to September; the Mediterranean is best spring and autumn; the Caribbean sails year round.",
            "The Caribbean is the easiest first cruise: short flights from most of the US, warm water, and days you can spend doing nothing.",
            "Alaska is scenery-led. The ship is a moving viewing platform, and the best moments happen from the deck rather than ashore.",
            "The Mediterranean is a city-hopping holiday that happens to float. Expect long, hot days on your feet and a lot of history.",
            "Caribbean days ashore are optional. Mediterranean days ashore are the point, and skipping them wastes the trip.",
            "Pack differently: swimwear for one, layers and waterproofs for another, walking shoes and modest cover for churches in the third.",
        ],
        "es": [
            "La temporada decide más que la preferencia. Alaska va de mayo a septiembre; el Mediterráneo es mejor en primavera y otoño; el Caribe navega todo el año.",
            "El Caribe es el primer crucero más fácil: vuelos cortos desde casi todo EE.UU., agua cálida y días en los que puedes no hacer nada.",
            "Alaska va de paisaje. El barco es un mirador en movimiento y los mejores momentos ocurren desde la cubierta, no en tierra.",
            "El Mediterráneo es unas vacaciones de ciudades que además flotan. Días largos, calurosos y de mucho caminar entre historia.",
            "En el Caribe bajar a tierra es opcional. En el Mediterráneo es el objetivo, y saltárselo desaprovecha el viaje.",
            "Haz maletas distintas: bañador para uno, capas e impermeable para otro, calzado cómodo y ropa discreta para iglesias en el tercero.",
        ],
    },
    "sections": [
        {"id": "season", "h2": {"en": "Start with the calendar, not the map",
                                "es": "Empieza por el calendario, no por el mapa"},
         "html": {
            "en": "<p>Two of these three are seasonal, and that alone settles a lot of arguments.</p>"
                  + vcards([
                      ("🧊", "Alaska: May to September", "Outside that window the ships are not there. June and July give the longest daylight; May and September are quieter and often better value, with a slightly higher chance of grey days."),
                      ("🏛️", "Mediterranean: April to October", "July and August are hot and crowded in every port. Late spring and early autumn give you the same cities at a temperature you can actually walk around in."),
                      ("🌴", "Caribbean: year round", "Winter is peak season and peak price. Late summer into autumn is hurricane season, which is why fares drop, and why travel insurance stops being optional."),
                  ])
                  + "<p>If your leave is fixed to one week in July, you have effectively already chosen. If you "
                  "can move your dates, that flexibility is worth more than any other decision on this page. "
                  "Our " + link("/en/guides/when-to-cruise/", "when to cruise guide")
                  + " goes region by region.</p>",
            "es": "<p>Dos de los tres son estacionales, y eso solo ya zanja muchas discusiones.</p>"
                  + vcards([
                      ("🧊", "Alaska: de mayo a septiembre", "Fuera de esa ventana los barcos no están. Junio y julio dan más luz; mayo y septiembre son más tranquilos y suelen tener mejor precio, con algo más de probabilidad de días grises."),
                      ("🏛️", "Mediterráneo: de abril a octubre", "Julio y agosto son calurosos y llenos en todos los puertos. Finales de primavera y principios de otoño dan las mismas ciudades a una temperatura por la que se puede caminar."),
                      ("🌴", "Caribe: todo el año", "El invierno es temporada alta y precio alto. De finales de verano a otoño es temporada de huracanes, por eso bajan las tarifas y por eso el seguro deja de ser opcional."),
                  ])
                  + "<p>Si tus vacaciones son una semana fija de julio, ya has elegido de hecho. Si puedes mover "
                  "las fechas, esa flexibilidad vale más que cualquier otra decisión de esta guía. Nuestra "
                  + link("/es/guides/when-to-cruise/", "guía de cuándo navegar")
                  + " lo desglosa por región.</p>",
         }},
        {"id": "day-ashore", "h2": {"en": "What a day ashore actually asks of you",
                                    "es": "Qué te pide realmente un día en tierra"},
         "html": {
            "en": "<p>This is the difference people feel most and plan for least. All three put you in a "
                  "port; what happens next could not be less alike.</p>"
                  + vcards([
                      ("🏖️", "Caribbean: optional", "A beach, a rum punch, or the ship's pool while everyone else goes ashore. Nothing is missed if you stay on board, which is exactly why it suits a rest."),
                      ("🥾", "Alaska: outdoor and weather-led", "Whale watching, glaciers, trains, floatplanes. Excursions carry more of the value here than anywhere else, and rain does not cancel the day, it just changes the clothes."),
                      ("🏛️", "Mediterranean: dense and demanding", "Old towns, museums, ruins, and often a drive between the port and the city that matters. Full days on your feet in heat, and the trip is largely wasted if you skip them."),
                  ])
                  + tip("A blunt test for the Mediterranean: if the idea of walking a hot city for six hours, "
                        "then doing it again the next day in a different country, sounds tiring rather than "
                        "thrilling, the Caribbean will make you happier. There is no wrong answer, only a "
                        "wrong match."),
            "es": "<p>Esta es la diferencia que más se nota y menos se planifica. Los tres te dejan en un "
                  "puerto; lo que pasa después no puede ser más distinto.</p>"
                  + vcards([
                      ("🏖️", "Caribe: opcional", "Una playa, un ron con fruta, o la piscina del barco mientras el resto baja. No te pierdes nada si te quedas a bordo, y por eso funciona para descansar."),
                      ("🥾", "Alaska: al aire libre y según el clima", "Avistamiento de ballenas, glaciares, trenes, hidroaviones. Las excursiones aportan aquí más valor que en ningún otro sitio, y la lluvia no cancela el día, solo cambia la ropa."),
                      ("🏛️", "Mediterráneo: denso y exigente", "Cascos antiguos, museos, ruinas y a menudo un trayecto entre el puerto y la ciudad que importa. Días enteros de pie con calor, y el viaje se desaprovecha si te los saltas."),
                  ])
                  + tip("Una prueba directa para el Mediterráneo: si caminar seis horas por una ciudad "
                        "calurosa, y repetirlo al día siguiente en otro país, suena agotador más que "
                        "emocionante, el Caribe te hará más feliz. No hay respuesta incorrecta, solo mal encaje."),
         }},
        {"id": "ship-vs-place", "h2": {"en": "How much the ship matters",
                                       "es": "Cuánto importa el barco"},
         "html": {
            "en": "<p>The same ship delivers a different share of the holiday in each region, which changes "
                  "how much you should spend on it.</p>"
                  + vcards([
                      ("🛳️", "Caribbean: the ship is half the trip", "Sea days are frequent and the newest, biggest ships sail here. Waterslides and shows earn their keep. Paying up for a better ship makes obvious sense."),
                      ("🪟", "Alaska: the ship is a viewing platform", "You will spend hours watching the coast go past. Big open decks, forward-facing lounges and a balcony matter far more than waterparks."),
                      ("🛏️", "Mediterranean: the ship is a hotel", "You are ashore most days and asleep on board. A comfortable cabin and good dinners matter; the entertainment lineup barely gets used."),
                  ])
                  + "<p>That has a practical consequence for cabin choice. A balcony earns its money in Alaska, "
                  "where the view is the product, more than in the Mediterranean, where you are rarely in the "
                  "room in daylight. " + link("/en/guides/choosing-a-cabin/", "Choosing a cabin")
                  + " covers the trade-offs.</p>",
            "es": "<p>El mismo barco aporta una parte distinta del viaje en cada región, y eso cambia cuánto "
                  "conviene gastar en él.</p>"
                  + vcards([
                      ("🛳️", "Caribe: el barco es medio viaje", "Hay muchos días de mar y aquí navegan los barcos más nuevos y grandes. Los toboganes y los espectáculos se aprovechan. Pagar por un barco mejor tiene sentido claro."),
                      ("🪟", "Alaska: el barco es un mirador", "Pasarás horas viendo pasar la costa. Cubiertas abiertas, salones con vista a proa y un balcón importan mucho más que un parque acuático."),
                      ("🛏️", "Mediterráneo: el barco es un hotel", "Estás en tierra casi todos los días y a bordo durmiendo. Un camarote cómodo y buenas cenas importan; el entretenimiento apenas se usa."),
                  ])
                  + "<p>Esto tiene una consecuencia práctica para el camarote. Un balcón rinde en Alaska, donde "
                  "la vista es el producto, más que en el Mediterráneo, donde rara vez estás en la habitación "
                  "de día. " + link("/es/guides/choosing-a-cabin/", "Elegir camarote")
                  + " cubre los equilibrios.</p>",
         }},
        {"id": "cost-shape", "h2": {"en": "Where the money goes in each",
                                    "es": "A dónde va el dinero en cada uno"},
         "html": {
            "en": "<p>We do not publish fares here, but the shape of the spending is different in a way worth "
                  "knowing before you compare two quotes.</p>"
                  + vcards([
                      ("✈️", "Getting there", "The Caribbean is a short domestic hop for most of the US. Alaska usually means a flight to Seattle or Vancouver. The Mediterranean adds a transatlantic flight and often a hotel night either side."),
                      ("🎟️", "Excursions", "Alaska carries the heaviest excursion spend, because the things worth doing are organised and not walkable. Mediterranean ports often can be done independently. Caribbean beach days can cost nothing."),
                      ("🧾", "On board", "Similar across regions, but Caribbean sea days give you more hours in which to buy drinks and speciality dinners, which quietly raises the total."),
                  ])
                  + watch("<b>Compare total trips, not cruise fares.</b> A cheaper Mediterranean cruise plus "
                          "long-haul flights and two hotel nights can easily cost more than a pricier "
                          "Caribbean sailing you drive to. This is the single most common mistake in choosing "
                          "between regions, and it is also where bundling flights and hotel with the cruise "
                          "usually pays off."),
            "es": "<p>Aquí no publicamos tarifas, pero la forma del gasto cambia de un modo que conviene "
                  "conocer antes de comparar dos presupuestos.</p>"
                  + vcards([
                      ("✈️", "Llegar", "El Caribe es un vuelo nacional corto para casi todo EE.UU. Alaska suele implicar volar a Seattle o Vancouver. El Mediterráneo añade un vuelo transatlántico y a menudo una noche de hotel a cada lado."),
                      ("🎟️", "Excursiones", "Alaska concentra el mayor gasto en excursiones, porque lo que merece la pena está organizado y no se llega a pie. Los puertos mediterráneos a menudo se pueden hacer por libre. Un día de playa en el Caribe puede costar cero."),
                      ("🧾", "A bordo", "Parecido entre regiones, pero los días de mar del Caribe dan más horas para comprar bebidas y cenas de especialidad, lo que sube el total sin que lo notes."),
                  ])
                  + watch("<b>Compara viajes completos, no tarifas de crucero.</b> Un crucero mediterráneo más "
                          "barato con vuelos de larga distancia y dos noches de hotel puede costar más que uno "
                          "caribeño más caro al que llegas conduciendo. Es el error más común al elegir entre "
                          "regiones, y también donde agrupar vuelos y hotel con el crucero suele compensar."),
         }},
        {"id": "which-fits", "h2": {"en": "So which one", "es": "Entonces cuál"},
         "html": {
            "en": vcards([
                      ("🌴", "Choose the Caribbean if", "It is your first cruise, you are travelling with children, you want warmth and rest, your dates are inflexible, or you would rather drive to the port than fly."),
                      ("🧊", "Choose Alaska if", "Scenery and wildlife are the reason you are going, you do not mind cool and changeable weather, and you can travel between May and September."),
                      ("🏛️", "Choose the Mediterranean if", "You want cities and history more than beaches, you are happy on your feet all day, and you can add flights and a hotel night at each end."),
                  ])
                  + "<p>One more honest point. Most people who cruise more than once end up doing all three, "
                  "and the order matters less than the timing. If you are undecided and your dates are "
                  "flexible, the Caribbean is the low-risk starting point: shortest travel, lowest total cost, "
                  "and the easiest to enjoy even if cruising turns out not to be your thing.</p>",
            "es": vcards([
                      ("🌴", "Elige el Caribe si", "Es tu primer crucero, viajas con niños, quieres calor y descanso, tus fechas son rígidas, o prefieres conducir al puerto antes que volar."),
                      ("🧊", "Elige Alaska si", "El paisaje y la fauna son la razón del viaje, no te importa el clima fresco y cambiante, y puedes viajar entre mayo y septiembre."),
                      ("🏛️", "Elige el Mediterráneo si", "Quieres ciudades e historia más que playas, estás a gusto caminando todo el día, y puedes añadir vuelos y una noche de hotel a cada lado."),
                  ])
                  + "<p>Un apunte honesto más. Casi todos los que repiten crucero acaban haciendo los tres, y "
                  "el orden importa menos que el momento. Si dudas y tus fechas son flexibles, el Caribe es el "
                  "punto de partida de menor riesgo: menos viaje, menor coste total y el más fácil de "
                  "disfrutar aunque los cruceros resulten no ser lo tuyo.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("Which is better, a Caribbean or Alaska cruise?", "Neither is better; they answer different questions. The Caribbean is warm, year round, reachable by a short flight or a drive for much of the US, and the days ashore are optional. Alaska is scenery-led, runs only from roughly May to September, and the excursions carry more of the value. Pick the Caribbean for rest and the Alaska sailing for landscape."),
            ("Is a Mediterranean cruise good for a first cruise?", "It can be excellent, but it is the most demanding of the three. You are ashore most days, often walking a hot city for hours, and skipping ports wastes the trip. If your idea of a holiday is resting, a Caribbean sailing suits a first cruise better. If you want to see several countries in a week, the Mediterranean is hard to beat."),
            ("When is the best time to cruise Alaska?", "The season runs roughly May to September because the ships are not there outside it. June and July give the longest daylight and the warmest weather. May and September are quieter and often better value, with a slightly higher chance of grey or wet days."),
            ("Do I need a balcony in Alaska?", "It earns its money there more than in most regions, because the scenery is the product and a lot of it passes while you are in your cabin. In the Mediterranean, where you are ashore most daylight hours, the same money is often better spent elsewhere. Our cabin guide covers the trade-off."),
            ("Which cruise region works out least expensive overall?", "Compare the whole trip rather than the cruise fare. For most US travellers the Caribbean adds up to the least because flights are short or unnecessary and beach days can cost nothing. A cheaper Mediterranean fare can end up costing more once long-haul flights, hotel nights either side and excursions are counted."),
            ("Is hurricane season a reason to avoid the Caribbean?", "It is a reason to plan rather than to avoid. Roughly June to November brings a higher chance of storms, which is why fares are lower then. Ships routinely reroute around weather, so the usual outcome is a changed itinerary rather than a cancelled trip, and travel insurance matters more in that window."),
        ],
        "es": [
            ("¿Qué es mejor, un crucero por el Caribe o por Alaska?", "Ninguno es mejor; responden a preguntas distintas. El Caribe es cálido, de todo el año, accesible con un vuelo corto o en coche desde gran parte de EE.UU., y bajar a tierra es opcional. Alaska va de paisaje, solo navega de mayo a septiembre, y las excursiones aportan más valor. Elige el Caribe para descansar y Alaska por el paisaje."),
            ("¿Un crucero por el Mediterráneo es bueno como primer crucero?", "Puede ser excelente, pero es el más exigente de los tres. Estás en tierra casi todos los días, a menudo caminando por una ciudad calurosa durante horas, y saltarse puertos desaprovecha el viaje. Si tu idea de vacaciones es descansar, el Caribe encaja mejor como primer crucero."),
            ("¿Cuándo es la mejor época para navegar en Alaska?", "La temporada va de mayo a septiembre porque fuera de ahí los barcos no están. Junio y julio dan más luz y mejor temperatura. Mayo y septiembre son más tranquilos y suelen tener mejor precio, con algo más de probabilidad de días grises o de lluvia."),
            ("¿Necesito balcón en Alaska?", "Rinde allí más que en casi cualquier región, porque el paisaje es el producto y buena parte pasa mientras estás en el camarote. En el Mediterráneo, donde estás en tierra casi todas las horas de luz, ese dinero suele rendir más en otra cosa."),
            ("¿Qué región de crucero es más barata en total?", "Compara el viaje completo, no la tarifa del crucero. Para la mayoría de viajeros de EE.UU. el Caribe tiene el total más bajo porque los vuelos son cortos o innecesarios y un día de playa puede costar cero. Una tarifa mediterránea más barata puede salir más cara al sumar vuelos largos, noches de hotel y excursiones."),
            ("¿La temporada de huracanes es motivo para evitar el Caribe?", "Es motivo para planificar, no para evitarlo. De junio a noviembre aumenta la probabilidad de tormentas, y por eso las tarifas bajan. Los barcos desvían la ruta con normalidad, así que lo habitual es un itinerario cambiado y no un viaje cancelado, y el seguro importa más en esa ventana."),
        ],
    },
    "related": {
        "en": [
            ("🗺️", "How to choose a destination", "/en/guides/how-to-choose-a-destination/", "The wider version of this decision."),
            ("🗓️", "When to cruise", "/en/guides/when-to-cruise/", "Season by season, region by region."),
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "Where a balcony earns its money."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "Comparing total trips, not fares."),
        ],
        "es": [
            ("🗺️", "Cómo elegir un destino", "/es/guides/how-to-choose-a-destination/", "La versión amplia de esta decisión."),
            ("🗓️", "Cuándo hacer un crucero", "/es/guides/when-to-cruise/", "Temporada a temporada, región a región."),
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "Dónde rinde de verdad un balcón."),
            ("🧾", "Qué incluye la tarifa", "/es/guides/whats-included/", "Comparar viajes completos, no tarifas."),
        ],
    },
})
