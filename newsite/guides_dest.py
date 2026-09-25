# -*- coding: utf-8 -*-
"""Rich guides cluster: dest. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link, photo_band


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


# ══════════════════════════════════════════════════════════════════════════════════════════════════
# Credential + media snippets reused inside the Bahamas romance guide.
_BR_CRED = {
    "en": ('<div class="gd-callout gd-tip"><span class="gd-cl-ic" aria-hidden="true">🎓</span><div>'
           '<b>Certified for the Bahamas.</b> A principal of BookMeCheapest LLC, which operates CruiseLine '
           'Advisors, holds the official Islands of the Bahamas Specialist diploma. When you call, we connect you with '
           'licensed partner advisors who plan Bahamas honeymoons, weddings, proposals and romantic getaways.'
           '<span style="display:flex;gap:.7rem;align-items:center;margin-top:.6rem;flex-wrap:wrap">'
           '<a href="/docs/bahamas-specialist-diploma.png" target="_blank" rel="noopener" '
           'style="background:#fff;border-radius:10px;padding:.35rem .5rem;display:inline-flex">'
           '<img src="/badges/bahamas-specialist.png" alt="Certified Bahamas Specialist diploma" height="34" loading="lazy"></a>'
           '<span style="background:#fff;border-radius:10px;padding:.3rem .45rem;display:inline-flex">'
           '<img src="/badges/romance.png" alt="Bahamas Romance Specialist programme" height="46" loading="lazy"></span>'
           '</span></div></div>'),
    "es": ('<div class="gd-callout gd-tip"><span class="gd-cl-ic" aria-hidden="true">🎓</span><div>'
           '<b>Certificados para las Bahamas.</b> Un socio de BookMeCheapest LLC, que opera CruiseLine Advisors, '
           'posee el diploma oficial de Especialista de las Islas de las Bahamas. Cuando llamas, '
           'te conectamos con asesores asociados con licencia que planean lunas de miel, bodas, pedidas de mano '
           'y escapadas románticas en las Bahamas.'
           '<span style="display:flex;gap:.7rem;align-items:center;margin-top:.6rem;flex-wrap:wrap">'
           '<a href="/docs/bahamas-specialist-diploma.png" target="_blank" rel="noopener" '
           'style="background:#fff;border-radius:10px;padding:.35rem .5rem;display:inline-flex">'
           '<img src="/badges/bahamas-specialist.png" alt="Diploma de Especialista de las Bahamas" height="34" loading="lazy"></a>'
           '<span style="background:#fff;border-radius:10px;padding:.3rem .45rem;display:inline-flex">'
           '<img src="/badges/romance.png" alt="Programa de Especialista en Romance de las Bahamas" height="46" loading="lazy"></span>'
           '</span></div></div>'),
}

register("bahamas-romance-travel", {
    "cat": "dest", "hero": "bahamas-romance-travel.jpg", "published": "2026-09-19", "updated": "2026-09-19",
    "title": {"en": "Romance in the Bahamas: honeymoons, weddings and where to say I do",
              "es": "Romance en las Bahamas: lunas de miel, bodas y dónde decir sí"},
    "dek": {
        "en": "The Bahamas is billed as the world's leading wedding destination, and it is just as good for a "
              "honeymoon, a proposal or a quiet escape for two. With about 700 islands, pink-sand beaches and a "
              "wedding process that is refreshingly simple, it is one of the easiest places to turn a big "
              "moment into a great trip. Here is how to plan it.",
        "es": "Las Bahamas son consideradas el principal destino de bodas del mundo, y son igual de buenas para "
              "una luna de miel, una pedida de mano o una escapada tranquila para dos. Con unas 700 islas, "
              "playas de arena rosada y un proceso de boda sorprendentemente simple, es uno de los lugares más "
              "fáciles para convertir un gran momento en un gran viaje. Así se planea.",
    },
    "takeaways": {
        "en": [
            "The Bahamas is positioned as the world's leading wedding destination, with simple rules and hundreds of islands to choose from.",
            "Romance travel here is far more than honeymoons: proposals, vow renewals, mini-moons, babymoons, micro-weddings and private buyouts all fit.",
            "To marry, you must be in the Bahamas in person. You can apply the day after you arrive and marry the day after that.",
            "Cruisers can marry too: you need a short letter from the ship's purser confirming at least 24 hours in Bahamian waters.",
            "Each island has its own mood, from lively Nassau and Paradise Island to the pink sands of Harbour Island and the deep seclusion of the Out Islands.",
        ],
        "es": [
            "Las Bahamas se posicionan como el principal destino de bodas del mundo, con reglas simples y cientos de islas para elegir.",
            "El turismo romántico aquí es mucho más que lunas de miel: pedidas de mano, renovación de votos, mini-lunas, babymoons, microbodas y alquileres privados encajan todos.",
            "Para casarte debes estar en las Bahamas en persona. Puedes solicitar la licencia el día después de llegar y casarte al día siguiente.",
            "Los cruceristas también pueden casarse: necesitas una breve carta del comisario del barco que confirme al menos 24 horas en aguas bahameñas.",
            "Cada isla tiene su propio ánimo, desde la animada Nassau y Paradise Island hasta las arenas rosadas de Harbour Island y el profundo aislamiento de las Out Islands.",
        ],
    },
    "sections": [
        {"id": "why-bahamas", "h2": {"en": "Why couples choose the Bahamas", "es": "Por qué las parejas eligen las Bahamas"},
         "html": {
            "en": "<p>The Bahamas is not one island. It is a chain of about 700 islands and cays spread across "
                  "clear, shallow water, which is why it can feel like a busy resort one day and a private "
                  "sandbar the next. That range is the whole appeal for couples: you pick the mood, and the "
                  "islands deliver it.</p>"
                  "<p>It also has a serious romance reputation. The Bahamas is billed as the world's leading "
                  "wedding destination, and the Exumas were named among the most romantic islands in the world by "
                  "a major travel magazine. Couples tend to invest far more in a honeymoon than in an ordinary "
                  "trip, often several times as much, so it is worth getting the choice right the first time.</p>"
                  + _BR_CRED["en"],
            "es": "<p>Las Bahamas no son una sola isla. Son una cadena de unas 700 islas y cayos repartidos sobre "
                  "aguas claras y poco profundas, por eso pueden sentirse como un resort concurrido un día y un "
                  "banco de arena privado al siguiente. Ese rango es todo el atractivo para las parejas: tú eliges "
                  "el ánimo y las islas lo entregan.</p>"
                  "<p>También tiene una seria reputación romántica. Las Bahamas son consideradas el principal "
                  "destino de bodas del mundo, y una importante revista de viajes nombró a las Exumas entre las "
                  "islas más románticas del planeta. Las parejas suelen invertir mucho más en una luna de miel que "
                  "en un viaje normal, a menudo varias veces más, así que conviene acertar a la primera.</p>"
                  + _BR_CRED["es"],
         }},
        {"id": "more-than-honeymoon", "h2": {"en": "More than a honeymoon", "es": "Mucho más que una luna de miel"},
         "html": {
            "en": "<p>Romance travel has grown well beyond newlyweds. The Bahamas works for almost every version "
                  "of a couple's trip:</p>"
                  + vcards([
                      ("💍", "Proposals", "A private beach, a sunset sail or a quiet cove make the question easy to ask and hard to forget."),
                      ("🥂", "Mini-moons", "A short getaway right after the wedding when a long honeymoon has to wait."),
                      ("🤍", "Vow renewals", "A relaxed celebration of an anniversary, with no license needed."),
                      ("👶", "Babymoons", "A calm, comfortable escape before a baby arrives."),
                      ("🎉", "Micro-weddings", "A small ceremony with just your closest people, often at a single resort."),
                      ("🏝️", "Private buyouts", "A whole small resort or villa taken over for a wedding party or a family celebration."),
                  ])
                  + photo_band("bahamas-romance-travel/proposal-pier.jpg",
                               "A proposal at the water's edge.")
                  + "<p>Family-moons that bring the kids, adults-only trips, and multi-island honeymoons that pair "
                  "a lively island with a quiet one are all common. If you are weighing the couples-only angle, "
                  "our guide to " + link("/en/guides/couples-adults-only-cruising/", "couples and adults-only travel")
                  + " pairs well with this one.</p>",
            "es": "<p>El turismo romántico creció mucho más allá de los recién casados. Las Bahamas funcionan para "
                  "casi toda versión de un viaje en pareja:</p>"
                  + vcards([
                      ("💍", "Pedidas de mano", "Una playa privada, un velero al atardecer o una cala tranquila hacen la pregunta fácil de hacer y difícil de olvidar."),
                      ("🥂", "Mini-lunas", "Una escapada corta justo después de la boda cuando la luna de miel larga debe esperar."),
                      ("🤍", "Renovación de votos", "Una celebración relajada de un aniversario, sin licencia necesaria."),
                      ("👶", "Babymoons", "Una escapada tranquila y cómoda antes de que llegue el bebé."),
                      ("🎉", "Microbodas", "Una ceremonia pequeña con solo tus personas más cercanas, a menudo en un solo resort."),
                      ("🏝️", "Alquileres privados", "Un pequeño resort o villa entero reservado para una boda o una celebración familiar."),
                  ])
                  + photo_band("bahamas-romance-travel/proposal-pier.jpg",
                               "Una pedida de mano a la orilla del agua.")
                  + "<p>Los family-moons con los niños, los viajes solo para adultos y las lunas de miel de varias "
                  "islas que combinan una isla animada con una tranquila son todos comunes. Si estás sopesando el "
                  "enfoque solo para parejas, nuestra guía de " + link("/es/guides/couples-adults-only-cruising/", "viajes en pareja y solo para adultos")
                  + " combina bien con esta.</p>",
         }},
        {"id": "getting-married", "h2": {"en": "Getting married in the Bahamas: the simple version", "es": "Casarse en las Bahamas: la versión simple"},
         "html": {
            "en": "<p>One reason the Bahamas is so popular for weddings is that the process is short and clear. "
                  "The key rule: you must be in the Bahamas in person to apply. You can lodge the application the "
                  "day after you arrive and marry the day after that, so even a fairly short trip can include the "
                  "wedding itself.</p>"
                  "<p>Applications go through the Registrar General's Department in Nassau, or an Administrator's "
                  "Office in the Out Islands. You will generally need:</p>"
                  "<ul>"
                  "<li>Valid <b>passports</b>, <b>birth certificates</b> and <b>photo ID</b> for both partners.</li>"
                  "<li><b>Proof of arrival</b> in the Bahamas.</li>"
                  "<li><b>Two witnesses</b> aged 18 or over to sign, though the officiant can often supply them.</li>"
                  "</ul>"
                  "<p>There is no blood test. A marriage license carries a set government fee that includes one "
                  "certified copy of the certificate. Vow renewals do not need a license at all. Rules can change, "
                  "so confirm the current requirements with the Registrar General's Department before you travel.</p>"
                  + watch("<b>Marrying on a cruise?</b> You can, but there is one extra step: cruisers need a short "
                          "letter from the ship's purser confirming you have spent at least 24 hours in Bahamian "
                          "waters. Plan your sailing and your paperwork around that, and a call to a specialist "
                          "makes it simple.")
                  + photo_band("bahamas-romance-travel/wedding-cake.jpg",
                               "Rings, shells and flowers: the small details of a beach wedding.")
                  + "<p>For planning, couples can also build a free gift and RSVP page through the official "
                  "Islands of the Bahamas honeymoon registry, a handy way to organise guests and wishes in one place.</p>",
            "es": "<p>Una razón por la que las Bahamas son tan populares para bodas es que el proceso es corto y "
                  "claro. La regla clave: debes estar en las Bahamas en persona para solicitar. Puedes presentar la "
                  "solicitud el día después de llegar y casarte al día siguiente, así que incluso un viaje bastante "
                  "corto puede incluir la boda misma.</p>"
                  "<p>Las solicitudes se tramitan en el Registrar General's Department en Nassau, o en una Oficina "
                  "del Administrador en las Out Islands. Por lo general necesitarás:</p>"
                  "<ul>"
                  "<li><b>Pasaportes</b>, <b>actas de nacimiento</b> e <b>identificación con foto</b> válidos de ambos.</li>"
                  "<li><b>Prueba de llegada</b> a las Bahamas.</li>"
                  "<li><b>Dos testigos</b> de 18 años o más para firmar, aunque el oficiante suele poder aportarlos.</li>"
                  "</ul>"
                  "<p>No hay análisis de sangre. Una licencia de matrimonio tiene una tarifa gubernamental fija que "
                  "incluye una copia certificada del certificado. La renovación de votos no necesita licencia. Las "
                  "reglas pueden cambiar, así que confirma los requisitos actuales con el Registrar General's "
                  "Department antes de viajar.</p>"
                  + watch("<b>¿Casarte en un crucero?</b> Puedes, pero hay un paso extra: los cruceristas necesitan "
                          "una breve carta del comisario del barco que confirme que pasaron al menos 24 horas en "
                          "aguas bahameñas. Planea tu travesía y tus papeles en torno a eso, y una llamada a un "
                          "especialista lo hace simple.")
                  + photo_band("bahamas-romance-travel/wedding-cake.jpg",
                               "Anillos, conchas y flores: los pequeños detalles de una boda en la playa.")
                  + "<p>Para planear, las parejas también pueden crear una página gratuita de regalos y "
                  "confirmaciones a través del registro oficial de lunas de miel de las Islas de las Bahamas, una "
                  "forma práctica de organizar invitados y deseos en un solo lugar.</p>",
         }},
        {"id": "where-i-do", "h2": {"en": "Where to say 'I do'", "es": "Dónde decir 'sí, quiero'"},
         "html": {
            "en": "<p>Half the fun is the setting. The Bahamas offers a wide spread, from grand and historic to "
                  "barefoot and remote:</p>"
                  + vcards([
                      ("⛪", "Churches", "Many faiths are represented across the islands, including small historic chapels."),
                      ("🏛️", "The Cloisters", "A medieval French cloister reassembled stone by stone on Paradise Island, a striking garden ceremony spot."),
                      ("🌺", "Botanical gardens", "Lush garden settings in Nassau and Freeport."),
                      ("⛵", "On the water", "Catamaran and boat ceremonies out on the turquoise shallows."),
                      ("🐬", "Underwater", "For divers, a reef or dolphin-side ceremony is genuinely possible."),
                      ("🏝️", "A private sandbar", "A secluded strip of sand with nobody else in sight."),
                  ])
                  + photo_band("bahamas-romance-travel/garden-ceremony.jpg",
                               "A ceremony set up beside the water.")
                  + "<p>If you want local colour, some couples build the celebration around Junkanoo, the "
                  "islands' vibrant music-and-costume tradition, for a reception nobody forgets.</p>",
            "es": "<p>La mitad de la diversión es el escenario. Las Bahamas ofrecen una gran variedad, de lo "
                  "grandioso e histórico a lo descalzo y remoto:</p>"
                  + vcards([
                      ("⛪", "Iglesias", "Muchas religiones están representadas en las islas, incluidas pequeñas capillas históricas."),
                      ("🏛️", "Los Claustros", "Un claustro medieval francés reensamblado piedra por piedra en Paradise Island, un llamativo lugar para una ceremonia en jardín."),
                      ("🌺", "Jardines botánicos", "Escenarios de jardín exuberantes en Nassau y Freeport."),
                      ("⛵", "Sobre el agua", "Ceremonias en catamarán y barco sobre los bajos turquesa."),
                      ("🐬", "Bajo el agua", "Para buzos, una ceremonia en el arrecife o junto a delfines es realmente posible."),
                      ("🏝️", "Un banco de arena privado", "Una franja de arena apartada sin nadie más a la vista."),
                  ])
                  + photo_band("bahamas-romance-travel/garden-ceremony.jpg",
                               "Una ceremonia montada junto al mar.")
                  + "<p>Si quieres color local, algunas parejas arman la celebración en torno al Junkanoo, la "
                  "vibrante tradición de música y disfraces de las islas, para una recepción que nadie olvida.</p>",
         }},
        {"id": "islands", "h2": {"en": "Island by island: the romantic shortlist", "es": "Isla por isla: la lista romántica"},
         "html": {
            "en": "<p>These are the islands most couples start with, each with a different personality:</p>"
                  + vcards([
                      ("🎰", "Nassau & Paradise Island", "The lively heart: resorts, nightlife, the Atlantis aquarium and marine habitat, dolphin encounters and top spas. Easy to reach and full of energy."),
                      ("🌴", "Grand Bahama", "Lucayan National Park's cave system, the marinas and market at Port Lucaya, dolphin swims and a relaxed pace."),
                      ("⛵", "The Abacos", "Sailing country: calm water, pastel colonial towns and Hope Town's candy-striped lighthouse, a signature photo."),
                      ("🌊", "Andros", "The biggest and least developed island, edged by a huge barrier reef and dotted with blue holes. True off-the-beaten-path romance."),
                      ("🩷", "Eleuthera & Harbour Island", "Famous pink-sand beaches, the dramatic Glass Window Bridge and historic little chapels for weddings."),
                      ("🐷", "The Exumas", "Named among the world's most romantic islands: swimming pigs, the Thunderball Grotto and a protected land-and-sea park."),
                  ])
                  + photo_band("bahamas-romance-travel/harbour-island-bikes.jpg",
                               "On a small island, a bicycle is often the easiest way to get around.")
                  + "<p>Harbour Island's pink sand is one of the most photographed stretches in the country, and "
                  "the Abacos' lighthouse country is quietly one of the most romantic. Many couples pair two "
                  "islands: somewhere lively to celebrate, then somewhere quiet to unwind.</p>"
                  + photo_band("bahamas-romance-travel/lighthouse.jpg",
                               "A lighthouse on a tropical coast."),
            "es": "<p>Estas son las islas por las que empiezan la mayoría de las parejas, cada una con una "
                  "personalidad distinta:</p>"
                  + vcards([
                      ("🎰", "Nassau y Paradise Island", "El corazón animado: resorts, vida nocturna, el acuario y hábitat marino de Atlantis, encuentros con delfines y spas de primer nivel. Fácil de llegar y llena de energía."),
                      ("🌴", "Gran Bahama", "El sistema de cuevas del Parque Nacional Lucayan, las marinas y el mercado de Port Lucaya, nados con delfines y un ritmo relajado."),
                      ("⛵", "Los Abacos", "Tierra de vela: aguas tranquilas, pueblos coloniales en tonos pastel y el faro a rayas de Hope Town, una foto insignia."),
                      ("🌊", "Andros", "La isla más grande y menos desarrollada, bordeada por un enorme arrecife de barrera y salpicada de agujeros azules. Romance genuino fuera de lo común."),
                      ("🩷", "Eleuthera y Harbour Island", "Famosas playas de arena rosada, el espectacular Glass Window Bridge y pequeñas capillas históricas para bodas."),
                      ("🐷", "Las Exumas", "Nombradas entre las islas más románticas del mundo: cerdos nadadores, la gruta Thunderball y un parque protegido de tierra y mar."),
                  ])
                  + photo_band("bahamas-romance-travel/harbour-island-bikes.jpg",
                               "En una isla pequeña, la bicicleta suele ser la forma más fácil de moverse.")
                  + "<p>La arena rosada de Harbour Island es uno de los tramos más fotografiados del país, y la "
                  "tierra de faros de los Abacos es, en silencio, una de las más románticas. Muchas parejas "
                  "combinan dos islas: una animada para celebrar y otra tranquila para descansar.</p>"
                  + photo_band("bahamas-romance-travel/lighthouse.jpg",
                               "Un faro en una costa tropical."),
         }},
        {"id": "out-islands", "h2": {"en": "For total seclusion: the Out Islands", "es": "Para aislamiento total: las Out Islands"},
         "html": {
            "en": "<p>If the goal is privacy, the far-flung Out Islands deliver it. These are quiet, low-key and "
                  "sometimes very remote, reached by small plane or boat:</p>"
                  + vcards([
                      ("🕳️", "Long Island", "Scenic and narrow, home to one of the world's deepest blue holes, a bucket-list swim or dive."),
                      ("⛰️", "Cat Island", "Laid-back and untouched, crowned by a hand-built hilltop hermitage."),
                      ("🎣", "Bimini", "The closest islands to Florida, known for sport fishing and an easygoing waterfront."),
                      ("🚤", "Berry Islands", "Dozens of tiny islands and cays, private and focused on diving and fishing."),
                      ("⛵", "San Salvador & Crooked Island", "Columbus-landing history, quiet reefs and superb bonefishing."),
                      ("🤫", "Mayaguana & Inagua", "The most isolated and least developed, with very limited lodging, for couples who want to disappear."),
                  ])
                  + photo_band("bahamas-romance-travel/seaplane-sunset.jpg",
                               "A float plane at golden hour. Small aircraft link the quieter islands.")
                  + "<p>Andros has a romantic footnote worth sharing: the settlement of Love Hill, where locals "
                  "brew a tea from a plant known as the 'love vine'. It is exactly the kind of small story that "
                  "makes an Out Island trip feel like your own discovery.</p>",
            "es": "<p>Si la meta es la privacidad, las lejanas Out Islands la entregan. Son tranquilas, discretas y "
                  "a veces muy remotas, a las que se llega en avioneta o barco:</p>"
                  + vcards([
                      ("🕳️", "Long Island", "Escénica y angosta, hogar de uno de los agujeros azules más profundos del mundo, un nado o buceo de lista de deseos."),
                      ("⛰️", "Cat Island", "Relajada e intacta, coronada por una ermita construida a mano en la cima de un cerro."),
                      ("🎣", "Bimini", "Las islas más cercanas a Florida, conocidas por la pesca deportiva y un malecón tranquilo."),
                      ("🚤", "Berry Islands", "Decenas de islitas y cayos, privados y enfocados en el buceo y la pesca."),
                      ("⛵", "San Salvador y Crooked Island", "Historia del desembarco de Colón, arrecifes tranquilos y excelente pesca de bonefish."),
                      ("🤫", "Mayaguana e Inagua", "Las más aisladas y menos desarrolladas, con alojamiento muy limitado, para parejas que quieren desaparecer."),
                  ])
                  + photo_band("bahamas-romance-travel/seaplane-sunset.jpg",
                               "Un hidroavión al atardecer. Las avionetas conectan las islas más tranquilas.")
                  + "<p>Andros tiene una nota romántica que vale la pena contar: el poblado de Love Hill, donde los "
                  "locales preparan un té de una planta conocida como 'love vine'. Es justo el tipo de pequeña "
                  "historia que hace que un viaje a las Out Islands se sienta como tu propio descubrimiento.</p>",
         }},
        {"id": "planning", "h2": {"en": "Planning it (and arriving by cruise)", "es": "Cómo planearlo (y llegar en crucero)"},
         "html": {
            "en": "<p>Plenty of couples first meet the Bahamas from a cruise deck. Nassau, Freeport and the lines' "
                  "private islands are among the most visited stops in the region, which makes a cruise an easy, "
                  "low-commitment way to sample the islands before a longer romantic trip, or even to marry aboard "
                  "using the purser's-letter route above.</p>"
                  "<p>Whether you are cruising in or flying to a single island, the two decisions that shape the "
                  "trip are which island (or pair of islands) fits your mood, and the timing. Our guide to "
                  + link("/en/guides/when-to-cruise/", "when to cruise") + " helps with the season, our "
                  + link("/en/guides/bahamas-cruise-guide/", "Bahamas cruise guide") + " explains how the short "
                  "sailings actually work, and the "
                  + link("/en/destinations/bahamas/", "Bahamas destination guide") + " covers the ports and how to "
                  "reach them.</p>"
                  + photo_band("bahamas-romance-travel/beach-hammock.jpg",
                               "The reward: a quiet beach and nowhere to be.")
                  + _BR_CRED["en"],
            "es": "<p>Muchas parejas conocen las Bahamas por primera vez desde la cubierta de un crucero. Nassau, "
                  "Freeport y las islas privadas de las líneas están entre las paradas más visitadas de la región, "
                  "lo que hace del crucero una forma fácil y de bajo compromiso de probar las islas antes de un "
                  "viaje romántico más largo, o incluso de casarse a bordo usando la ruta de la carta del comisario "
                  "de arriba.</p>"
                  "<p>Ya sea que llegues en crucero o en avión a una sola isla, las dos decisiones que moldean el "
                  "viaje son qué isla (o par de islas) encaja con tu ánimo, y las fechas. Nuestra guía de "
                  + link("/es/guides/when-to-cruise/", "cuándo hacer un crucero") + " ayuda con la temporada, y la "
                  + link("/es/destinations/bahamas/", "guía de destino de las Bahamas") + " cubre los puertos y "
                  "cómo llegar.</p>"
                  + photo_band("bahamas-romance-travel/beach-hammock.jpg",
                               "La recompensa: una playa tranquila y ningún lugar al que ir.")
                  + _BR_CRED["es"],
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>The Bahamas earns its romance reputation. The wedding process is simple, the islands cover "
                  "every mood from party to total peace, and you can be as social or as hidden away as you like. "
                  "Decide what the trip is really about, celebrating, relaxing or a bit of both, pick the island "
                  "to match, and the rest falls into place.</p>"
                  "<p>When you want a certified Bahamas specialist to help choose the island, handle the timing and "
                  "connect you with a licensed advisor for the details, that is one call away, free, with no "
                  "obligation, and never a payment to us.</p>",
            "es": "<p>Las Bahamas se ganan su fama romántica. El proceso de boda es simple, las islas cubren todos "
                  "los ánimos, de la fiesta a la paz total, y puedes ser tan social o tan escondido como quieras. "
                  "Decide de qué se trata realmente el viaje, celebrar, descansar o un poco de ambos, elige la isla "
                  "que combine, y lo demás cae en su lugar.</p>"
                  "<p>Cuando quieras que un especialista certificado en las Bahamas te ayude a elegir la isla, "
                  "manejar las fechas y conectarte con un asesor con licencia para los detalles, eso está a una "
                  "llamada, gratis, sin compromiso, y nunca un pago para nosotros.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("Do you have to be in the Bahamas to get married there?", "Yes. Both partners must be physically present in the Bahamas to apply for the marriage license. You can apply the day after you arrive and marry the day after that, so a short trip can still include the ceremony. Confirm current rules with the Registrar General's Department before you travel."),
            ("What documents do you need to marry in the Bahamas?", "Generally valid passports, birth certificates and photo ID for both partners, plus proof of arrival in the Bahamas. Two witnesses aged 18 or over must sign, though the officiant can often provide them. There is no blood test required."),
            ("Can you get married on a Bahamas cruise?", "Yes. Cruisers need one extra document: a letter from the ship's purser confirming you have spent at least 24 hours in Bahamian waters. With that and the standard documents, the same license process applies. A specialist can help line up the timing."),
            ("Do vow renewals need a license in the Bahamas?", "No. Vow renewals do not require a marriage license, which makes them one of the simplest celebrations to arrange. You can hold one almost anywhere, from a beach to a garden to the deck of a boat."),
            ("Which Bahamas island is best for a honeymoon?", "It depends on your mood. Nassau and Paradise Island are lively and easy to reach; Harbour Island has the famous pink sand; the Exumas are prized for seclusion and were named among the world's most romantic islands; and the Out Islands offer near-total privacy. Many couples pair a lively island with a quiet one."),
            ("Is the Bahamas good for a destination wedding?", "Very. It is billed as the world's leading wedding destination, with a short and clear legal process, hundreds of islands and settings that run from historic churches to private sandbars. It is also easy to combine the wedding with the honeymoon in one trip."),
        ],
        "es": [
            ("¿Hay que estar en las Bahamas para casarse allí?", "Sí. Ambos deben estar físicamente en las Bahamas para solicitar la licencia de matrimonio. Puedes solicitarla el día después de llegar y casarte al día siguiente, así que un viaje corto puede incluir la ceremonia. Confirma las reglas actuales con el Registrar General's Department antes de viajar."),
            ("¿Qué documentos se necesitan para casarse en las Bahamas?", "Por lo general pasaportes, actas de nacimiento e identificación con foto válidos de ambos, más prueba de llegada a las Bahamas. Dos testigos de 18 años o más deben firmar, aunque el oficiante suele poder aportarlos. No se requiere análisis de sangre."),
            ("¿Se puede uno casar en un crucero por las Bahamas?", "Sí. Los cruceristas necesitan un documento extra: una carta del comisario del barco que confirme al menos 24 horas en aguas bahameñas. Con eso y los documentos habituales, aplica el mismo proceso de licencia. Un especialista puede ayudar a cuadrar las fechas."),
            ("¿La renovación de votos necesita licencia en las Bahamas?", "No. La renovación de votos no requiere licencia de matrimonio, lo que la hace una de las celebraciones más simples de organizar. Puedes hacerla casi en cualquier lugar, de una playa a un jardín o la cubierta de un barco."),
            ("¿Cuál isla de las Bahamas es mejor para una luna de miel?", "Depende de tu ánimo. Nassau y Paradise Island son animadas y fáciles de llegar; Harbour Island tiene la famosa arena rosada; las Exumas son apreciadas por el aislamiento y fueron nombradas entre las más románticas del mundo; y las Out Islands ofrecen privacidad casi total. Muchas parejas combinan una isla animada con una tranquila."),
            ("¿Las Bahamas son buenas para una boda de destino?", "Mucho. Son consideradas el principal destino de bodas del mundo, con un proceso legal corto y claro, cientos de islas y escenarios que van de iglesias históricas a bancos de arena privados. También es fácil combinar la boda con la luna de miel en un solo viaje."),
        ],
    },
    "related": {
        "en": [
            ("🏝️", "Bahamas destination guide", "/en/destinations/bahamas/", "Ports, how to reach the islands and what to do."),
            ("💞", "Couples & adults-only travel", "/en/guides/couples-adults-only-cruising/", "Planning a trip built around just the two of you."),
            ("🗺️", "How to choose a destination", "/en/guides/how-to-choose-a-destination/", "Match the place to the trip you want."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Talk through Bahamas dates and islands in one call."),
        ],
        "es": [
            ("🏝️", "Guía de destino de las Bahamas", "/es/destinations/bahamas/", "Puertos, cómo llegar a las islas y qué hacer."),
            ("💞", "Viajes en pareja y solo para adultos", "/es/guides/couples-adults-only-cruising/", "Planear un viaje pensado solo para ustedes dos."),
            ("🗺️", "Cómo elegir un destino", "/es/guides/how-to-choose-a-destination/", "Combina el lugar con el viaje que quieres."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Conversa fechas e islas de las Bahamas en una llamada."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("bahamas-cruise-guide", {
    "cat": "dest",
    "hero": "bahamas-cruise-guide.jpg",
    "published": "2026-09-25",
    "updated": "2026-09-25",
    "title": {
        "en": "Bahamas cruise guide: short trips, private islands and when to go",
        "es": "Guía de cruceros por las Bahamas: viajes cortos, islas privadas y cuándo ir",
    },
    "dek": {
        "en": "More first cruises start in the Bahamas than anywhere else, and the reason is simple "
              "geography: it sits a short hop off Florida, which makes a three or four night trip "
              "genuinely possible. That shapes everything about how these cruises feel, and it is worth "
              "understanding before you book one.",
        "es": "Más primeros cruceros empiezan en las Bahamas que en ningún otro sitio, y la razón es pura "
              "geografía: están a un salto de Florida, lo que hace posible un viaje de tres o cuatro "
              "noches. Eso condiciona todo el carácter de estos cruceros, y conviene entenderlo antes de reservar.",
    },
    "takeaways": {
        "en": [
            "The Bahamas is the short-cruise capital: three and four night sailings from Florida are the standard, which is why so many people start here.",
            "A private island day is often the highlight, and on a short itinerary it can be most of the point.",
            "Nassau is the busiest port in the region. How your day feels depends heavily on how many other ships are in that morning.",
            "It sails year round, which no other nearby region manages. Winter is peak, and hurricane season runs roughly June to November.",
            "Because the sailings are short, the ship matters more than the ports. You are rarely ashore for long.",
            "It is the easiest cruise to get to. For much of the eastern US you can drive to the port, which removes the biggest cost and the biggest risk.",
        ],
        "es": [
            "Las Bahamas son la capital del crucero corto: salidas de tres y cuatro noches desde Florida son lo habitual, y por eso tanta gente empieza aquí.",
            "El día en una isla privada suele ser lo mejor del viaje, y en un itinerario corto puede ser casi todo el sentido.",
            "Nassau es el puerto más concurrido de la región. Cómo te resulte el día depende mucho de cuántos barcos más lleguen esa mañana.",
            "Navega todo el año, algo que ninguna región cercana consigue. El invierno es temporada alta y la de huracanes va de junio a noviembre.",
            "Como las salidas son cortas, el barco importa más que los puertos. Pasas poco tiempo en tierra.",
            "Es el crucero más fácil de alcanzar. Desde buena parte del este de EE.UU. puedes conducir al puerto, lo que elimina el mayor gasto y el mayor riesgo.",
        ],
    },
    "sections": [
        {"id": "why-short", "h2": {"en": "Why almost every short cruise goes here",
                                   "es": "Por qué casi todos los cruceros cortos van aquí"},
         "html": {
            "en": "<p>The Bahamas begin about fifty miles off the Florida coast. That single fact explains "
                  "the whole market.</p>"
                  + vcards([
                      ("🗓️", "Three and four nights work", "A ship can leave Friday evening, call at two places and be back Monday morning. Almost nowhere else in cruising can do a real itinerary in a long weekend."),
                      ("🚗", "You can often drive to it", "Most sailings leave from Florida ports. For a lot of the eastern US that means no flights, which removes both the largest expense and the most common way a cruise goes wrong."),
                      ("🧪", "It is the natural first cruise", "Short, warm, close to home and cheap to reach. If cruising turns out not to suit you, you have lost a weekend rather than a fortnight."),
                  ])
                  + tip("If you are testing whether you like cruising at all, a three-night Bahamas sailing is "
                        "the lowest-risk way to find out. Just go in knowing it is a sampler. One short trip "
                        "will not tell you what a seven-night itinerary feels like, because the rhythm is "
                        "completely different.")
                  + photo_band("bahamas-cruise-guide/florida-departure.jpg",
                               "Most Bahamas sailings leave from a Florida port."),
            "es": "<p>Las Bahamas empiezan a unos ochenta kilómetros de la costa de Florida. Ese solo dato "
                  "explica todo el mercado.</p>"
                  + vcards([
                      ("🗓️", "Tres y cuatro noches funcionan", "Un barco puede salir el viernes por la tarde, hacer dos escalas y volver el lunes. Casi ningún otro destino permite un itinerario real en un fin de semana largo."),
                      ("🚗", "A menudo puedes ir en coche", "La mayoría de las salidas son desde puertos de Florida. Para buena parte del este de EE.UU. eso significa no volar, lo que elimina el mayor gasto y la causa más común de que un crucero salga mal."),
                      ("🧪", "Es el primer crucero natural", "Corto, cálido, cerca de casa y barato de alcanzar. Si los cruceros no te convencen, has perdido un fin de semana y no quince días."),
                  ])
                  + tip("Si quieres probar si te gustan los cruceros, una salida de tres noches a las Bahamas "
                        "es la forma de menor riesgo. Eso sí, ve sabiendo que es una muestra. Un viaje corto "
                        "no te dirá cómo se siente un itinerario de siete noches, porque el ritmo es distinto.")
                  + photo_band("bahamas-cruise-guide/florida-departure.jpg",
                               "La mayoría de las salidas a las Bahamas parten de un puerto de Florida."),
         }},
        {"id": "private-islands", "h2": {"en": "The private island day",
                                         "es": "El día en la isla privada"},
         "html": {
            "en": "<p>This is the part of Bahamas cruising that surprises people, and on a short sailing it "
                  "is frequently the best day of the trip.</p>"
                  + define("Private island",
                           "A stretch of Bahamian coast that a cruise line owns or leases and uses "
                           "exclusively for its own ships. Most of the major lines have one. Your ship "
                           "docks or tenders, the beach is set up for the day, and the food is usually "
                           "included in the same way it is on board.")
                  + vcards([
                      ("🏝️", "It is a beach day, run properly", "Loungers, shade, restrooms, lifeguards, included lunch. The predictability is the appeal: nothing to arrange and no way to get lost or be late."),
                      ("👨‍👩‍👧", "It suits families unusually well", "Shallow water, staff everywhere, and the ship is right there if a nap or a change of clothes is needed."),
                      ("💳", "The extras are where it costs", "The beach itself is included. Cabanas, waterparks, jet skis, speciality food and drinks are not, and on the more developed islands there are a lot of them."),
                      ("🌊", "Weather can cancel it", "Where ships tender rather than dock, rough water can mean the call is skipped entirely. It happens, and no itinerary is guaranteed."),
                  ])
                  + watch("<b>On a three-night sailing, check whether a private island day is actually on "
                          "your itinerary.</b> Two ships leaving the same port on the same weekend can have "
                          "quite different stops, and for many people this single day is the reason to pick "
                          "one over the other. It is worth asking about specifically.")
                  + photo_band("bahamas-cruise-guide/private-island-beach.jpg",
                               "A beach day set up in advance: loungers, shade and lunch included."),
            "es": "<p>Esta es la parte que sorprende a la gente, y en una salida corta suele ser el mejor día "
                  "del viaje.</p>"
                  + define("Isla privada",
                           "Un tramo de costa bahameña que una naviera posee o alquila y usa en exclusiva "
                           "para sus barcos. La mayoría de las grandes líneas tienen una. Tu barco atraca o "
                           "usa botes, la playa está preparada para el día y la comida suele estar incluida "
                           "igual que a bordo.")
                  + vcards([
                      ("🏝️", "Un día de playa bien organizado", "Hamacas, sombra, baños, socorristas, comida incluida. Lo previsible es el atractivo: nada que organizar y ninguna forma de perderse ni llegar tarde."),
                      ("👨‍👩‍👧", "Encaja muy bien con familias", "Agua poco profunda, personal por todas partes y el barco justo ahí si hace falta una siesta o ropa limpia."),
                      ("💳", "Los extras son lo que cuesta", "La playa está incluida. Las cabañas, los parques acuáticos, las motos de agua y la comida y bebida de especialidad no, y en las islas más desarrolladas hay muchos."),
                      ("🌊", "El clima puede cancelarlo", "Donde se llega en botes en vez de atracar, el mar movido puede hacer que se salte la escala. Pasa, y ningún itinerario está garantizado."),
                  ])
                  + watch("<b>En una salida de tres noches, comprueba si tu itinerario incluye día en isla "
                          "privada.</b> Dos barcos que salen del mismo puerto el mismo fin de semana pueden "
                          "tener escalas distintas, y para mucha gente ese día es la razón de elegir uno u "
                          "otro. Conviene preguntarlo expresamente.")
                  + photo_band("bahamas-cruise-guide/private-island-beach.jpg",
                               "Un día de playa preparado de antemano: hamacas, sombra y comida incluida."),
         }},
        {"id": "nassau", "h2": {"en": "Nassau, and why your day there varies so much",
                                "es": "Nassau, y por qué tu día allí varía tanto"},
         "html": {
            "en": "<p>Nassau is the capital and the region's busiest cruise port. Almost every Bahamas "
                  "itinerary calls there, which is precisely the thing to understand about it.</p>"
                  + vcards([
                      ("🚢", "Ship count changes everything", "The port can host several large ships at once. Arrive on a quiet morning and the town is pleasant; arrive alongside four others and every beach, taxi and attraction is absorbing thousands of extra people."),
                      ("🚶", "The terminal is walkable to town", "Unusually for a cruise port, you step off into the middle of things. That is convenient, and it also means the crowding is concentrated right where you land."),
                      ("🏖️", "The good beaches need a short trip", "The well-known stretches are a taxi or ferry ride away rather than at the dock. Budget the travel time, especially against an early all-aboard."),
                  ])
                  + tip("Ask which other ships are scheduled in port the same day. It is a question most "
                        "people never think to ask, and it predicts the character of your day in Nassau "
                        "better than any review will.")
                  + photo_band("bahamas-cruise-guide/nassau-harbour.jpg",
                               "Nassau, the busiest cruise port in the region."),
            "es": "<p>Nassau es la capital y el puerto de cruceros más concurrido de la región. Casi todos "
                  "los itinerarios paran allí, que es justo lo que hay que entender.</p>"
                  + vcards([
                      ("🚢", "El número de barcos lo cambia todo", "El puerto puede recibir varios barcos grandes a la vez. Si llegas una mañana tranquila la ciudad es agradable; si llegas junto a otros cuatro, cada playa, taxi y atracción absorbe miles de personas más."),
                      ("🚶", "La terminal está a pie del centro", "Algo poco habitual en un puerto de cruceros: bajas directamente al centro. Es cómodo, y también concentra la aglomeración justo donde desembarcas."),
                      ("🏖️", "Las buenas playas quedan a un trayecto", "Las más conocidas están a un taxi o ferry, no en el muelle. Cuenta el tiempo de ida y vuelta, sobre todo con una hora límite temprana."),
                  ])
                  + tip("Pregunta qué otros barcos coinciden ese día en puerto. Es una pregunta que casi "
                        "nadie hace, y predice el carácter de tu día en Nassau mejor que cualquier reseña.")
                  + photo_band("bahamas-cruise-guide/nassau-harbour.jpg",
                               "Nassau, el puerto de cruceros más concurrido de la región."),
         }},
        {"id": "when", "h2": {"en": "When to go", "es": "Cuándo ir"},
         "html": {
            "en": "<p>The Bahamas sails all year, which is rarer than it sounds and is a genuine advantage "
                  "if your dates are fixed.</p>"
                  + vcards([
                      ("❄️", "Winter into spring is peak", "Warm, dry, and the reason fares and crowds are at their highest. School holidays concentrate families into specific weeks."),
                      ("☀️", "Summer is hot and busy", "Hotter and more humid than the brochures suggest, and busy with families. The sea is at its warmest."),
                      ("🌀", "Hurricane season is roughly June to November", "Fares soften for a reason. Ships reroute around storms routinely, so the usual outcome is a changed itinerary rather than a cancelled trip, but this is the window where travel insurance stops being optional."),
                  ])
                  + "<p>Because the sailings are short, a weather disruption bites harder here than on a long "
                  "itinerary. Lose one call from a three-night cruise and you have lost a third of your "
                  "stops. Our " + link("/en/guides/when-to-cruise/", "when to cruise guide")
                  + " covers the seasonal picture across regions.</p>",
            "es": "<p>Las Bahamas navegan todo el año, algo menos común de lo que parece y una ventaja real "
                  "si tus fechas son fijas.</p>"
                  + vcards([
                      ("❄️", "De invierno a primavera es temporada alta", "Cálido, seco, y por eso las tarifas y la afluencia están en su punto más alto. Las vacaciones escolares concentran a las familias en semanas concretas."),
                      ("☀️", "El verano es caluroso y concurrido", "Más caluroso y húmedo de lo que sugieren los folletos, y lleno de familias. El mar está en su punto más cálido."),
                      ("🌀", "La temporada de huracanes va de junio a noviembre", "Las tarifas bajan por algo. Los barcos desvían la ruta con normalidad, así que lo habitual es un itinerario cambiado y no un viaje cancelado, pero es la ventana en la que el seguro deja de ser opcional."),
                  ])
                  + "<p>Como las salidas son cortas, una alteración por clima duele más aquí que en un "
                  "itinerario largo. Si pierdes una escala de un crucero de tres noches, has perdido un "
                  "tercio de tus paradas. Nuestra "
                  + link("/es/guides/when-to-cruise/", "guía de cuándo navegar")
                  + " cubre el panorama por regiones.</p>",
         }},
        {"id": "ship-matters", "h2": {"en": "On a short sailing, the ship is the destination",
                                      "es": "En una salida corta, el barco es el destino"},
         "html": {
            "en": "<p>This is the thing most first-timers get wrong. On a three or four night Bahamas cruise "
                  "you are ashore for parts of one or two days. The rest of the time you are on the ship.</p>"
                  + vcards([
                      ("🛳️", "Pick the ship, not the ports", "The itineraries are broadly similar. What differs is what you are sitting on, and on a short trip that is where nearly all your hours go."),
                      ("⏱️", "Embarkation and disembarkation eat into it", "The first afternoon and the last morning are largely logistics. A three-night cruise is really about two full days of holiday, which is worth knowing before you set expectations."),
                      ("🎉", "Short sailings have their own atmosphere", "Weekend trips draw a livelier, more party-leaning crowd than week-long itineraries. For some people that is the appeal and for others it is the thing to avoid, so it is worth asking about."),
                  ])
                  + "<p>If the ship is carrying the trip, it is worth understanding what varies between them. "
                  + link("/en/guides/big-ship-vs-small-ship/", "Big ship vs small ship")
                  + " and " + link("/en/guides/choosing-a-cabin/", "choosing a cabin")
                  + " both matter more on a short sailing than they would on a longer one.</p>"
                  + photo_band("bahamas-cruise-guide/ship-pool-deck.jpg",
                               "On a three-night sailing, this is where most of your hours go."),
            "es": "<p>Esto es lo que más malinterpretan los primerizos. En un crucero de tres o cuatro noches "
                  "por las Bahamas estás en tierra parte de uno o dos días. El resto del tiempo estás en el barco.</p>"
                  + vcards([
                      ("🛳️", "Elige el barco, no los puertos", "Los itinerarios son parecidos. Lo que cambia es aquello en lo que vas sentado, y en un viaje corto ahí se van casi todas tus horas."),
                      ("⏱️", "El embarque y el desembarque restan", "La primera tarde y la última mañana son sobre todo logística. Un crucero de tres noches son en realidad unos dos días completos de vacaciones."),
                      ("🎉", "Las salidas cortas tienen su propio ambiente", "Los viajes de fin de semana atraen a un público más animado y fiestero que los itinerarios de una semana. Para unos es el atractivo y para otros lo que evitar, así que conviene preguntar."),
                  ])
                  + "<p>Si el barco sostiene el viaje, conviene saber en qué se diferencian. "
                  + link("/es/guides/big-ship-vs-small-ship/", "Barco grande o pequeño")
                  + " y " + link("/es/guides/choosing-a-cabin/", "elegir camarote")
                  + " importan más en una salida corta que en una larga.</p>"
                  + photo_band("bahamas-cruise-guide/ship-pool-deck.jpg",
                               "En una salida de tres noches, aquí se van la mayoría de tus horas."),
         }},
    ],
    "faqs": {
        "en": [
            ("How long is a typical Bahamas cruise?", "Three and four nights are the standard, which is what makes the region distinctive: it is close enough to Florida that a real itinerary fits into a long weekend. Longer sailings exist and often combine the Bahamas with other Caribbean stops, but the short trip is the classic."),
            ("Are Bahamas cruises good for first-time cruisers?", "They are the most common way people start, and for good reason. They are short, warm, easy to reach without flying for much of the eastern US, and low commitment. The one thing to be clear about is that a short sailing is a sampler: the rhythm of a three-night trip is quite different from a week at sea."),
            ("What is a cruise line's private island?", "A stretch of Bahamian coast that a line owns or leases and uses only for its own ships. Most major lines have one. Your ship docks or tenders in, the beach is set up for the day and lunch is generally included the same way it is on board. Cabanas, watersports and speciality food and drink cost extra."),
            ("Do Bahamas cruises always stop in Nassau?", "Most do, since it is the capital and the region's busiest cruise port. How the day feels depends a great deal on how many other ships are scheduled the same morning, because the port can host several large ones at once. It is worth asking before you book."),
            ("When is the best time for a Bahamas cruise?", "The region sails year round, which is unusual. Winter into spring is the peak for warm dry weather, and also the busiest and priciest. Roughly June to November is hurricane season, when fares soften and travel insurance matters more. Ships routinely reroute around weather, so a changed itinerary is far more likely than a cancelled trip."),
            ("Can I cruise to the Bahamas without flying?", "Often yes, and it is one of the region's real advantages. Most sailings leave from Florida ports, so a large part of the eastern US can drive. That removes the biggest single cost for many families and the most common cause of missing a ship."),
        ],
        "es": [
            ("¿Cuánto dura un crucero típico por las Bahamas?", "Tres y cuatro noches es lo habitual, y eso distingue a la región: está tan cerca de Florida que cabe un itinerario real en un fin de semana largo. Hay salidas más largas que combinan las Bahamas con otras escalas del Caribe, pero el viaje corto es el clásico."),
            ("¿Son buenos para un primer crucero?", "Es la forma más común de empezar, y con razón. Son cortos, cálidos, fáciles de alcanzar sin volar desde buena parte del este de EE.UU. y de poco compromiso. Eso sí: una salida corta es una muestra, y el ritmo de tres noches es muy distinto al de una semana en el mar."),
            ("¿Qué es la isla privada de una naviera?", "Un tramo de costa bahameña que una línea posee o alquila y usa solo para sus barcos. La mayoría de las grandes tienen una. El barco atraca o llega en botes, la playa está preparada y la comida suele estar incluida como a bordo. Cabañas, deportes acuáticos y comida y bebida de especialidad se pagan aparte."),
            ("¿Todos los cruceros paran en Nassau?", "Casi todos, por ser la capital y el puerto más concurrido de la región. Cómo resulte el día depende mucho de cuántos barcos coincidan esa mañana, porque el puerto puede recibir varios grandes a la vez. Conviene preguntarlo antes de reservar."),
            ("¿Cuál es la mejor época?", "La región navega todo el año, algo poco común. De invierno a primavera es lo mejor por clima cálido y seco, y también lo más concurrido y caro. De junio a noviembre es temporada de huracanes: bajan las tarifas y el seguro importa más. Los barcos desvían la ruta con normalidad, así que un itinerario cambiado es mucho más probable que un viaje cancelado."),
            ("¿Puedo ir sin volar?", "A menudo sí, y es una de las ventajas reales de la región. La mayoría de las salidas son desde puertos de Florida, así que buena parte del este de EE.UU. puede conducir. Eso elimina el mayor gasto para muchas familias y la causa más común de perder el barco."),
        ],
    },
    "related": {
        "en": [
            ("💍", "Romance in the Bahamas", "/en/guides/bahamas-romance-travel/", "Honeymoons, weddings and quiet escapes."),
            ("🧭", "First-time cruisers", "/en/guides/first-time-cruisers/", "What nobody tells you before you sail."),
            ("⚓", "Port days vs sea days", "/en/guides/port-days-vs-sea-days/", "Why short sailings feel different."),
            ("🏝️", "Bahamas destination guide", "/en/destinations/bahamas/", "Ports, how to reach the islands and what to do."),
        ],
        "es": [
            ("💍", "Romance en las Bahamas", "/es/guides/bahamas-romance-travel/", "Lunas de miel, bodas y escapadas."),
            ("🧭", "Primer crucero", "/es/guides/first-time-cruisers/", "Lo que nadie te cuenta antes de zarpar."),
            ("⚓", "Puerto o navegación", "/es/guides/port-days-vs-sea-days/", "Por qué las salidas cortas se sienten distintas."),
            ("🏝️", "Guía de destino de las Bahamas", "/es/destinations/bahamas/", "Puertos, cómo llegar a las islas y qué hacer."),
        ],
    },
})
