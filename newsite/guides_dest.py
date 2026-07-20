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
