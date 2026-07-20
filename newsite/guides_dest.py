# -*- coding: utf-8 -*-
"""Rich guides cluster: dest. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("how-to-choose-a-destination", {
    "cat": "dest",
    "hero": "cruise-port.jpg",
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
    "cat": "dest", "hero": "cruise-ship-sea.jpg", "published": "2026-07-20", "updated": "2026-07-20",
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
