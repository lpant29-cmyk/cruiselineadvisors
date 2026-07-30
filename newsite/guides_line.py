# -*- coding: utf-8 -*-
"""Rich guides cluster: line. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("how-to-choose-a-cruise-line", {
    "cat": "line",
    "hero": "how-to-choose-a-cruise-line.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "How to choose a cruise line that actually fits you",
        "es": "Cómo elegir una línea de crucero que de verdad encaje contigo",
    },
    "dek": {
        "en": "The ships all look similar from the outside, but the experience on board varies a lot "
              "from one line to the next. Match the line to how you actually like to travel and the "
              "whole trip gets better. Here is how to narrow it down fast.",
        "es": "Los barcos se parecen por fuera, pero la experiencia a bordo varía mucho de una línea a "
              "otra. Ajusta la línea a cómo te gusta viajar de verdad y todo el viaje mejora. Aquí te "
              "decimos cómo reducir las opciones rápido.",
    },
    "takeaways": {
        "en": [
            "Start with the vibe, not the ship: big and lively, relaxed and refined, family-packed, or classic and formal.",
            "Contemporary/casual lines suit families and first-timers; premium lines lean calmer and more adult; higher-end lines fold more into the fare.",
            "Who you travel with matters as much as the destination: kids, couples, solo or a big group each point to different lines.",
            "The details that decide it are the money-and-fine-print facts, gratuities, what's included, drink rules, which is where our compare tool comes in.",
            "There is rarely one 'best' line, only the best fit for your party, your budget and your itinerary.",
        ],
        "es": [
            "Empieza por el ambiente, no por el barco: grande y animado, relajado y refinado, lleno de familias, o clásico y formal.",
            "Las líneas informales convienen a familias y primerizos; las premium son más tranquilas y adultas; las de gama alta incluyen más en la tarifa.",
            "Con quién viajas importa tanto como el destino: niños, parejas, solos o un grupo grande apuntan a líneas distintas.",
            "Los detalles que lo deciden son los datos de dinero y letra pequeña: propinas, qué se incluye, reglas de bebidas, ahí entra nuestra herramienta de comparación.",
            "Rara vez hay una sola 'mejor' línea, solo la que mejor encaja con tu grupo, tu presupuesto y tu itinerario.",
        ],
    },
    "sections": [
        {
            "id": "start-with-vibe",
            "h2": {"en": "Start with the vibe you want", "es": "Empieza por el ambiente que quieres"},
            "html": {
                "en": "<p>The biggest difference between lines is not the hardware, it is the feel on board. Picture "
                      "your ideal sea day and you will already be narrowing the field:</p>"
                      + vcards([
                          ("🎢", "Big & lively", "Waterslides, shows, a dozen places to eat, buzz everywhere. Great for families and first-timers who want lots to do."),
                          ("🥂", "Relaxed & refined", "Calmer spaces, an adult-leaning crowd, a slower pace. Great for couples and anyone who wants to unwind."),
                          ("👨‍👩‍👧", "Family-packed", "Kids' clubs, family cabins and non-stop activities aimed squarely at younger travellers."),
                          ("🎩", "Classic & formal", "Ocean-liner tradition, dressier evenings and a timeless feel."),
                      ]),
                "es": "<p>La mayor diferencia entre líneas no es el hardware, es la sensación a bordo. Imagina tu día "
                      "de mar ideal y ya estarás reduciendo el campo:</p>"
                      + vcards([
                          ("🎢", "Grande y animado", "Toboganes, espectáculos, una docena de sitios para comer, energía por todas partes. Ideal para familias y primerizos que quieren mucho que hacer."),
                          ("🥂", "Relajado y refinado", "Espacios más tranquilos, público más adulto, ritmo pausado. Ideal para parejas y quien quiere desconectar."),
                          ("👨‍👩‍👧", "Lleno de familias", "Clubes infantiles, camarotes familiares y actividades sin parar pensadas para los más jóvenes."),
                          ("🎩", "Clásico y formal", "Tradición de transatlántico, noches más elegantes y un aire atemporal."),
                      ]),
            },
        },
        {
            "id": "who-with",
            "h2": {"en": "Factor in who you're travelling with", "es": "Considera con quién viajas"},
            "html": {
                "en": "<p>The right line for a young family is rarely the right line for a couple's anniversary. Let "
                      "your party guide you:</p>"
                      "<ul>"
                      "<li><b>Families with kids:</b> look for strong kids' clubs, family cabins and lots of included activity.</li>"
                      "<li><b>Couples:</b> adult-leaning, premium lines with quieter spaces and good dining tend to win.</li>"
                      "<li><b>Solo travellers:</b> a handful of lines offer dedicated studio cabins and solo lounges; see our "
                      + link("/en/guides/solo-cruising/", "solo cruising guide") + ".</li>"
                      "<li><b>Groups:</b> big, activity-packed ships give everyone something to do without forcing you all together.</li>"
                      "</ul>"
                      "<p>You can also tell us your party and let the " + link("/en/compare/", "cruise finder") +
                      " surface the ships that fit.</p>",
                "es": "<p>La línea correcta para una familia joven rara vez es la correcta para un aniversario de "
                      "pareja. Deja que tu grupo te guíe:</p>"
                      "<ul>"
                      "<li><b>Familias con niños:</b> busca buenos clubes infantiles, camarotes familiares y mucha actividad incluida.</li>"
                      "<li><b>Parejas:</b> las líneas premium y más adultas, con espacios tranquilos y buena gastronomía, suelen ganar.</li>"
                      "<li><b>Viajeros solos:</b> algunas líneas ofrecen camarotes estudio y salones para solos; ve nuestra "
                      + link("/es/guides/solo-cruising/", "guía de cruceros para solos") + ".</li>"
                      "<li><b>Grupos:</b> los barcos grandes y llenos de actividades dan a cada uno algo que hacer sin obligarlos a estar siempre juntos.</li>"
                      "</ul>"
                      "<p>También puedes decirnos tu grupo y dejar que el " + link("/es/compare/", "buscador de cruceros") +
                      " muestre los barcos que encajan.</p>",
            },
        },
        {
            "id": "compare-facts",
            "h2": {"en": "Then compare the details that cost money", "es": "Luego compara los detalles que cuestan dinero"},
            "html": {
                "en": "<p>Once you have two or three lines in mind, the tie-breaker is the fine print, the stuff that "
                      "quietly shapes your final bill and your day-to-day experience:</p>"
                      "<ul>"
                      "<li>How much are the daily gratuities, and are they included?</li>"
                      "<li>What is in the fare versus sold as an extra?</li>"
                      "<li>What is the drink-package rule, and the cancellation timeline?</li>"
                      "</ul>"
                      "<p>This is exactly what our tools are built for. Every " + link("/en/cruise-lines/", "cruise line") +
                      " page has a compare tool at the top, and the " + link("/en/cruise-facts/", "cruise facts") +
                      " page lines up the verified money facts side by side.</p>",
                "es": "<p>Cuando tengas dos o tres líneas en mente, el desempate es la letra pequeña, lo que moldea en "
                      "silencio tu factura final y tu experiencia diaria:</p>"
                      "<ul>"
                      "<li>¿Cuánto son las propinas diarias, y están incluidas?</li>"
                      "<li>¿Qué está en la tarifa y qué se vende como extra?</li>"
                      "<li>¿Cuál es la regla del paquete de bebidas, y el calendario de cancelación?</li>"
                      "</ul>"
                      "<p>Para esto están hechas nuestras herramientas. Cada página de " + link("/es/cruise-lines/", "línea de crucero") +
                      " tiene un comparador arriba, y la página de " + link("/es/cruise-facts/", "datos de crucero") +
                      " alinea los datos de dinero verificados lado a lado.</p>",
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>Pick the vibe, factor in your party, then compare the fine print. Do it in that order and "
                      "the right line usually becomes obvious, without hours of open tabs.</p>"
                      "<p>Still torn between two? That is the perfect thing to settle in one call. Tell a specialist "
                      "what matters most and they will point you to the line, and the ship, that fits. Browse the "
                      + link("/en/cruise-lines/", "cruise line guides") + " to get started.</p>",
                "es": "<p>Elige el ambiente, considera tu grupo, luego compara la letra pequeña. Hazlo en ese orden y "
                      "la línea correcta suele volverse obvia, sin horas de pestañas abiertas.</p>"
                      "<p>¿Sigues entre dos? Eso se resuelve perfecto en una llamada. Dile a un especialista qué es lo "
                      "más importante y te señalará la línea, y el barco, que encaja. Explora las "
                      + link("/es/cruise-lines/", "guías de líneas de crucero") + " para empezar.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("Which cruise line is best?", "There is rarely a single best line, only the best fit for your party, budget and itinerary. Start with the vibe you want (lively, relaxed, family or classic), factor in who is travelling, then compare the money facts between your shortlist."),
            ("What is the best cruise line for families?", "Big, activity-packed contemporary lines with strong kids' clubs and family cabins tend to suit families best. The right one still depends on your children's ages and your budget; compare the lines and what's included."),
            ("What is the best cruise line for couples?", "Premium, adult-leaning lines with calmer spaces and good dining are popular with couples. If you want a quieter, more refined feel, lean that way; if you love buzz and variety, a big-ship line can work too."),
            ("What is the difference between contemporary, premium and luxury lines?", "Broadly, contemporary/casual lines keep the base fare approachable and sell extras a la carte; premium lines fold in a bit more and feel calmer; higher-end lines include more still. Compare the inclusions, not the label."),
            ("How do I compare cruise lines?", "Look at the vibe and who each line suits, then compare the fine print, gratuities, what's included, drink rules and cancellation. Every line page on our site has a compare tool, and the cruise facts page lines the verified figures up side by side."),
        ],
        "es": [
            ("¿Cuál es la mejor línea de crucero?", "Rara vez hay una sola mejor línea, solo la que mejor encaja con tu grupo, presupuesto e itinerario. Empieza por el ambiente que quieres (animado, relajado, familiar o clásico), considera con quién viajas, y luego compara los datos de dinero entre tus finalistas."),
            ("¿Cuál es la mejor línea para familias?", "Las líneas informales grandes y llenas de actividades, con buenos clubes infantiles y camarotes familiares, suelen convenir más a las familias. La correcta depende de las edades de tus hijos y tu presupuesto; compara las líneas y lo que incluyen."),
            ("¿Cuál es la mejor línea para parejas?", "Las líneas premium y más adultas, con espacios tranquilos y buena gastronomía, son populares entre parejas. Si quieres un ambiente más tranquilo y refinado, inclínate por ahí; si te encanta la energía y la variedad, una línea de barcos grandes también funciona."),
            ("¿Cuál es la diferencia entre líneas informales, premium y de lujo?", "En general, las informales mantienen la tarifa base accesible y venden extras a la carta; las premium incluyen un poco más y se sienten más tranquilas; las de gama alta incluyen aún más. Compara lo incluido, no la etiqueta."),
            ("¿Cómo comparo líneas de crucero?", "Mira el ambiente y para quién es cada línea, luego compara la letra pequeña: propinas, qué se incluye, reglas de bebidas y cancelación. Cada página de línea en nuestro sitio tiene un comparador, y la página de datos de crucero alinea las cifras verificadas lado a lado."),
        ],
    },
    "related": {
        "en": [
            ("🚢", "Compare cruise lines", "/en/cruise-lines/", "In-depth, verified guides to every major line."),
            ("💸", "The cruise facts that cost you money", "/en/cruise-facts/", "The money-and-fine-print facts that break a tie."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your party; we'll match the line and ship."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "Compare lines on what the fare actually covers."),
        ],
        "es": [
            ("🚢", "Comparar líneas de crucero", "/es/cruise-lines/", "Guías detalladas y verificadas de cada línea principal."),
            ("💸", "Datos de crucero que cuestan dinero", "/es/cruise-facts/", "Los datos de dinero y letra pequeña que rompen el empate."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos tu grupo; emparejamos la línea y el barco."),
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Compara líneas en lo que la tarifa realmente cubre."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("big-ship-vs-small-ship", {
    "cat": "line", "hero": "cruise-ship-sea.jpg", "published": "2026-07-20", "updated": "2026-07-20",
    "title": {"en": "Big ship vs small ship: which cruise suits you", "es": "Barco grande vs pequeño: qué crucero te conviene"},
    "dek": {
        "en": "One of the biggest choices in cruising is not the destination, it is the size of the "
              "ship. A floating resort and an intimate vessel are almost different holidays. Here is how "
              "to tell which one you will love.",
        "es": "Una de las mayores decisiones en los cruceros no es el destino, es el tamaño del barco. "
              "Un resort flotante y un barco íntimo son casi vacaciones distintas. Aquí te decimos cuál "
              "te encantará.",
    },
    "takeaways": {
        "en": [
            "Big ships are floating resorts: waterslides, shows, many restaurants and non-stop activity, great for families and first-timers.",
            "Smaller ships are calmer and more intimate, with fewer crowds, a more relaxed pace and easier access to smaller ports.",
            "Big ships can feel busy and take longer to get on and off; small ships trade some amenities for atmosphere.",
            "Where you want to go matters: some ports and scenic areas only smaller ships can reach.",
            "Neither is better, only better for you, your party and the kind of days you want.",
        ],
        "es": [
            "Los barcos grandes son resorts flotantes: toboganes, espectáculos, muchos restaurantes y actividad sin parar, ideales para familias y primerizos.",
            "Los barcos pequeños son más tranquilos e íntimos, con menos gente, un ritmo más relajado y mejor acceso a puertos pequeños.",
            "Los grandes pueden sentirse concurridos y tardar más para embarcar y desembarcar; los pequeños cambian algunas comodidades por ambiente.",
            "A dónde quieres ir importa: algunos puertos y zonas escénicas solo los barcos más pequeños pueden alcanzar.",
            "Ninguno es mejor, solo mejor para ti, tu grupo y el tipo de días que quieres.",
        ],
    },
    "sections": [
        {"id": "big", "h2": {"en": "Big ships: the floating resort", "es": "Barcos grandes: el resort flotante"},
         "html": {
            "en": "<p>The newest mega-ships carry thousands of guests and pack in more to do than you could finish in "
                  "a week: waterparks, zip lines, Broadway-style shows, a dozen restaurants and bars, sprawling kids' "
                  "clubs.</p>"
                  + vcards([
                      ("🎢", "Endless activity", "Something for every age and mood, all day, so nobody is ever bored."),
                      ("👨‍👩‍👧", "Great for families & groups", "Kids' clubs, family cabins and enough variety to keep a mixed group happy."),
                      ("🍽️", "Choice everywhere", "Many dining venues and entertainment options included in the fare."),
                  ])
                  + "<p>The trade-off: more guests means more buzz, busier pools and lines, and longer to board or get "
                  "off in port. If you love energy and choice, that is a feature, not a flaw.</p>",
            "es": "<p>Los mega-barcos más nuevos llevan miles de huéspedes y reúnen más que hacer de lo que podrías "
                  "terminar en una semana: parques acuáticos, tirolesas, espectáculos estilo Broadway, una docena de "
                  "restaurantes y bares, enormes clubes infantiles.</p>"
                  + vcards([
                      ("🎢", "Actividad sin fin", "Algo para cada edad y ánimo, todo el día, así nadie se aburre."),
                      ("👨‍👩‍👧", "Ideal para familias y grupos", "Clubes infantiles, camarotes familiares y suficiente variedad para un grupo mixto."),
                      ("🍽️", "Opciones por todas partes", "Muchos restaurantes y opciones de entretenimiento incluidos en la tarifa."),
                  ])
                  + "<p>El equilibrio: más huéspedes significa más energía, piscinas y filas más concurridas, y más "
                  "tiempo para embarcar o bajar en puerto. Si amas la energía y la variedad, eso es una ventaja.</p>",
         }},
        {"id": "small", "h2": {"en": "Smaller ships: intimate and relaxed", "es": "Barcos pequeños: íntimos y relajados"},
         "html": {
            "en": "<p>Smaller and mid-size ships trade some of the bells and whistles for a calmer, more personal feel. "
                  "Fewer guests means shorter lines, quieter decks and crew who get to know you.</p>"
                  + vcards([
                      ("🧘", "A calmer pace", "Less crowding, more room to unwind, and an adult-leaning atmosphere on many."),
                      ("⚓", "Reaches more ports", "Smaller ships can dock at smaller, less-touristed harbours the big ships cannot."),
                      ("🤝", "A personal feel", "Crew recognise you, and the whole experience feels more intimate."),
                  ])
                  + "<p>The trade-off: fewer onboard attractions and dining venues. If your idea of a great day is a "
                  "quiet deck and a characterful port rather than a waterslide, this is your ship.</p>",
            "es": "<p>Los barcos pequeños y medianos cambian algunas atracciones por una sensación más tranquila y "
                  "personal. Menos huéspedes significa filas más cortas, cubiertas más tranquilas y una tripulación que "
                  "te conoce.</p>"
                  + vcards([
                      ("🧘", "Un ritmo más tranquilo", "Menos gente, más espacio para relajarte, y un ambiente más adulto en muchos."),
                      ("⚓", "Alcanza más puertos", "Los barcos pequeños pueden atracar en puertos más pequeños y menos turísticos que los grandes no pueden."),
                      ("🤝", "Una sensación personal", "La tripulación te reconoce, y toda la experiencia se siente más íntima."),
                  ])
                  + "<p>El equilibrio: menos atracciones y restaurantes a bordo. Si tu idea de un gran día es una "
                  "cubierta tranquila y un puerto con carácter en lugar de un tobogán, este es tu barco.</p>",
         }},
        {"id": "how-to-decide", "h2": {"en": "How to decide", "es": "Cómo decidir"},
         "html": {
            "en": "<p>Answer three questions and the choice usually makes itself:</p>"
                  "<ul>"
                  "<li><b>Who is travelling?</b> Kids and mixed groups usually love a big ship; couples chasing calm often prefer smaller.</li>"
                  "<li><b>What is a perfect day?</b> Non-stop activity and variety, or space, quiet and character.</li>"
                  "<li><b>Where do you want to go?</b> If your dream ports are small or off the beaten path, a smaller ship may be the only way in.</li>"
                  "</ul>"
                  "<p>Still weighing it up? That is a two-minute conversation. Tell a specialist your party and your "
                  "ideal day, and read " + link("/en/guides/how-to-choose-a-cruise-line/", "how to choose a cruise line") +
                  " for the next layer of the decision.</p>",
            "es": "<p>Responde tres preguntas y la elección suele hacerse sola:</p>"
                  "<ul>"
                  "<li><b>¿Quién viaja?</b> Los niños y grupos mixtos suelen amar un barco grande; las parejas que buscan calma prefieren uno más pequeño.</li>"
                  "<li><b>¿Cómo es un día perfecto?</b> Actividad y variedad sin parar, o espacio, tranquilidad y carácter.</li>"
                  "<li><b>¿A dónde quieres ir?</b> Si tus puertos soñados son pequeños o fuera de lo común, un barco más pequeño puede ser la única forma de llegar.</li>"
                  "</ul>"
                  "<p>¿Aún lo evalúas? Es una conversación de dos minutos. Dile a un especialista tu grupo y tu día "
                  "ideal, y lee " + link("/es/guides/how-to-choose-a-cruise-line/", "cómo elegir una línea de crucero") +
                  " para la siguiente capa de la decisión.</p>",
         }},
        {"id": "bottom-line", "h2": {"en": "The bottom line", "es": "En conclusión"},
         "html": {
            "en": "<p>Big ships are all-in resorts bursting with activity; smaller ships are calmer, more personal and "
                  "reach places the giants cannot. Match the size to your party, your ideal day and your dream ports, "
                  "and you will love the ship you are on.</p>"
                  "<p>Want us to point you to the right ships either way? Tell the " + link("/en/compare/", "cruise finder") +
                  " what you are after, or just call.</p>",
            "es": "<p>Los barcos grandes son resorts completos llenos de actividad; los pequeños son más tranquilos, "
                  "personales y llegan a lugares que los gigantes no. Ajusta el tamaño a tu grupo, tu día ideal y tus "
                  "puertos soñados, y amarás el barco en el que estés.</p>"
                  "<p>¿Quieres que te señalemos los barcos correctos en cualquier caso? Dile al "
                  + link("/es/compare/", "buscador de cruceros") + " qué buscas, o simplemente llama.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("Is a big or small cruise ship better?", "Neither is better overall, only better for you. Big ships are floating resorts packed with activity, ideal for families and first-timers; smaller ships are calmer, more intimate and reach more ports. Match the size to your party and the days you want."),
            ("Are big cruise ships good for families?", "Yes. Mega-ships have the most kids' clubs, family cabins, waterslides and non-stop activity, which suits families and mixed groups very well. The trade-off is more crowds and longer boarding."),
            ("Why choose a smaller cruise ship?", "For a calmer, more personal experience: fewer crowds, a relaxed pace, an adult-leaning feel on many, and access to smaller ports the big ships cannot reach. You give up some onboard attractions in return."),
            ("Do smaller ships visit different ports?", "Often yes. Smaller ships can dock at smaller, less-touristed harbours and scenic areas that mega-ships are too large to enter, which can open up a very different itinerary."),
            ("How do I choose between a big and small ship?", "Ask who is travelling, what your perfect day looks like, and where you want to go. Kids and activity-lovers lean big; couples wanting calm and off-the-beaten-path ports lean small. A specialist can match you to the right ship."),
        ],
        "es": [
            ("¿Es mejor un barco grande o pequeño?", "Ninguno es mejor en general, solo mejor para ti. Los grandes son resorts flotantes llenos de actividad, ideales para familias y primerizos; los pequeños son más tranquilos, íntimos y alcanzan más puertos. Ajusta el tamaño a tu grupo y los días que quieres."),
            ("¿Los barcos grandes son buenos para familias?", "Sí. Los mega-barcos tienen los mayores clubes infantiles, camarotes familiares, toboganes y actividad sin parar, lo que conviene muy bien a familias y grupos mixtos. El equilibrio es más gente y embarque más largo."),
            ("¿Por qué elegir un barco más pequeño?", "Por una experiencia más tranquila y personal: menos gente, ritmo relajado, un ambiente más adulto en muchos, y acceso a puertos pequeños que los grandes no alcanzan. A cambio renuncias a algunas atracciones a bordo."),
            ("¿Los barcos pequeños visitan puertos distintos?", "A menudo sí. Los barcos pequeños pueden atracar en puertos más pequeños y menos turísticos y zonas escénicas donde los mega-barcos son demasiado grandes para entrar, lo que abre un itinerario muy distinto."),
            ("¿Cómo elijo entre un barco grande y uno pequeño?", "Pregúntate quién viaja, cómo es tu día perfecto y a dónde quieres ir. Los niños y amantes de la actividad se inclinan por lo grande; las parejas que quieren calma y puertos fuera de lo común, por lo pequeño. Un especialista puede emparejarte con el barco correcto."),
        ],
    },
    "related": {
        "en": [
            ("🚢", "How to choose a cruise line", "/en/guides/how-to-choose-a-cruise-line/", "The next layer: match the line to how you travel."),
            ("🛏️", "Choosing a cabin", "/en/guides/choosing-a-cabin/", "Once you have a ship, pick the right room on it."),
            ("🗺️", "How to choose a destination", "/en/guides/how-to-choose-a-destination/", "Where you sail can decide the ship size for you."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Tell us your ideal day; we'll match the ship."),
        ],
        "es": [
            ("🚢", "Cómo elegir una línea de crucero", "/es/guides/how-to-choose-a-cruise-line/", "La siguiente capa: ajusta la línea a cómo viajas."),
            ("🛏️", "Elegir camarote", "/es/guides/choosing-a-cabin/", "Cuando tengas barco, elige la habitación correcta."),
            ("🗺️", "Cómo elegir un destino", "/es/guides/how-to-choose-a-destination/", "A dónde navegas puede decidir el tamaño del barco."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Dinos tu día ideal; emparejamos el barco."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("contemporary-premium-luxury", {
    "cat": "line",
    "hero": "contemporary-premium-luxury.jpg",
    "published": "2026-07-30",
    "updated": "2026-07-30",
    "title": {
        "en": "Contemporary vs premium vs luxury cruise lines",
        "es": "Líneas de crucero: contemporánea vs premium vs lujo",
    },
    "dek": {
        "en": "Cruise lines get sorted into three tiers, and the labels get thrown around as if everyone "
              "agrees what they mean. They are useful shorthand, but they describe a style of holiday and "
              "what the fare covers, not a quality ranking. Here is what each tier actually feels like on "
              "board, and how to tell which one suits the trip you want.",
        "es": "Las líneas de crucero se agrupan en tres niveles, y las etiquetas se usan como si todos "
              "coincidieran en su significado. Son un atajo útil, pero describen un estilo de viaje y qué "
              "cubre la tarifa, no una escala de calidad. Aquí verás cómo se siente cada nivel a bordo y "
              "cómo saber cuál encaja con el viaje que quieres.",
    },
    "takeaways": {
        "en": [
            "The tiers describe style and what is bundled into the fare, not how good a line is. A great contemporary cruise beats a poorly matched luxury one.",
            "Contemporary lines carry the most guests, pack in the most to do, and keep the base fare low by charging separately for extras.",
            "Premium lines run somewhat smaller ships at a calmer pace, with more included and more space per guest.",
            "Luxury lines are small, mostly all-inclusive, and priced accordingly; the fare covers what other tiers bill for.",
            "The tiers blur in practice. Suites on a contemporary ship include perks that feel premium, and every line runs both busy and quiet sailings.",
            "Pick the tier by the day you want, not by prestige. Who is travelling and what you want to do decides it.",
        ],
        "es": [
            "Los niveles describen el estilo y qué incluye la tarifa, no qué tan buena es una línea. Un buen crucero contemporáneo supera a uno de lujo mal elegido.",
            "Las líneas contemporáneas llevan más huéspedes, ofrecen más actividades y mantienen baja la tarifa base cobrando aparte los extras.",
            "Las líneas premium operan barcos algo más pequeños a un ritmo más tranquilo, con más incluido y más espacio por huésped.",
            "Las líneas de lujo son pequeñas, casi todo incluido, y su precio lo refleja: la tarifa cubre lo que otros niveles facturan aparte.",
            "Los niveles se difuminan en la práctica. Las suites de un barco contemporáneo incluyen ventajas que se sienten premium, y toda línea tiene salidas concurridas y tranquilas.",
            "Elige el nivel por el día que quieres, no por prestigio. Quién viaja y qué quieres hacer lo decide.",
        ],
    },
    "sections": [
        {"id": "what-the-tiers-are", "h2": {"en": "What the three tiers actually describe",
                                            "es": "Qué describen realmente los tres niveles"},
         "html": {
            "en": "<p>Walk into any cruise conversation and you will hear lines sorted into contemporary, premium "
                  "and luxury. It is industry shorthand rather than an official standard, so the edges are fuzzy "
                  "and lines move over time. What the tiers really track is two things: <b>how much is bundled "
                  "into your fare</b>, and <b>how many people you share the ship with.</b></p>"
                  + define("Cruise line tier",
                           "an informal grouping of cruise lines by style, ship size and how much the fare "
                           "includes. It is a description of the holiday, not a rating of the company.")
                  + "<p>That distinction matters, because the labels sound like a quality ladder and they are not. "
                  "A family who wants waterslides, a rock wall and a late-night comedy show will have a far better "
                  "week on a contemporary ship than on a hushed luxury one, whatever the fare says. The right "
                  "question is never which tier is best. It is which tier matches the trip you actually want.</p>",
            "es": "<p>En cualquier conversación sobre cruceros escucharás que las líneas se agrupan en "
                  "contemporánea, premium y lujo. Es una jerga del sector, no un estándar oficial, así que los "
                  "límites son difusos y las líneas cambian con el tiempo. Lo que los niveles realmente reflejan "
                  "son dos cosas: <b>cuánto incluye tu tarifa</b> y <b>con cuánta gente compartes el barco.</b></p>"
                  + define("Nivel de línea de crucero",
                           "una agrupación informal de líneas según estilo, tamaño del barco y cuánto incluye la "
                           "tarifa. Describe el viaje, no califica a la empresa.")
                  + "<p>Esa diferencia importa, porque las etiquetas suenan a escalera de calidad y no lo son. Una "
                  "familia que quiere toboganes, muro de escalada y comedia nocturna la pasará mucho mejor en un "
                  "barco contemporáneo que en uno de lujo silencioso, diga lo que diga la tarifa. La pregunta "
                  "correcta nunca es qué nivel es mejor, sino cuál encaja con el viaje que quieres.</p>",
         }},
        {"id": "contemporary", "h2": {"en": "Contemporary: the big, busy, do-everything ships",
                                      "es": "Contemporánea: los barcos grandes, animados y con todo"},
         "html": {
            "en": "<p>This is the tier most first-time cruisers meet, and the one that carries the most passengers "
                  "worldwide. The ships are large to very large, the atmosphere is lively, and the whole model is "
                  "built on keeping the entry fare accessible while offering a great deal to do.</p>"
                  + vcards([
                      ("🎢", "The ship is the attraction", "Waterslides, pools, live shows, sports decks, kids clubs and a long list of dining rooms. On the newest ships the vessel itself is as much the destination as the ports."),
                      ("👨‍👩‍👧‍👦", "Built for families and groups", "Kids programming by age band, connecting cabins, and enough going on that different ages can split up and meet for dinner."),
                      ("🧾", "Low base fare, more extras", "Your fare covers the room, main dining and most entertainment. Specialty restaurants, drinks packages, Wi-Fi and shore excursions are billed separately."),
                      ("🔊", "Livelier by design", "More guests means more energy, busier pool decks and queues at peak times. That is the trade for the variety and the price point."),
                  ])
                  + "<p>Among the lines we cover, "
                  + link("/en/lines/royal-caribbean/", "Royal Caribbean")
                  + " and " + link("/en/lines/carnival/", "Carnival")
                  + " sit squarely here, and "
                  + link("/en/lines/msc/", "MSC")
                  + " brings a European accent to the same big-ship idea. "
                  + link("/en/lines/margaritaville-at-sea/", "Margaritaville at Sea")
                  + " works the short-getaway end of it.</p>"
                  + tip("If you are weighing this tier, read "
                        + link("/en/guides/whats-included/", "what's included in a cruise fare")
                        + " first. The gap between the headline fare and your final bill is widest here, and it is "
                          "entirely manageable once you know which extras you actually want."),
            "es": "<p>Es el nivel que conoce la mayoría de quienes viajan por primera vez, y el que transporta más "
                  "pasajeros en el mundo. Los barcos son grandes o muy grandes, el ambiente es animado, y todo el "
                  "modelo se basa en mantener accesible la tarifa de entrada ofreciendo muchísimo que hacer.</p>"
                  + vcards([
                      ("🎢", "El barco es la atracción", "Toboganes, piscinas, espectáculos, cubiertas deportivas, clubes infantiles y una larga lista de restaurantes. En los barcos más nuevos, el barco es tanto destino como los puertos."),
                      ("👨‍👩‍👧‍👦", "Pensado para familias y grupos", "Programas infantiles por edades, camarotes comunicados y suficiente actividad para que cada edad se separe y se reúna a cenar."),
                      ("🧾", "Tarifa base baja, más extras", "Tu tarifa cubre la habitación, el comedor principal y casi todo el entretenimiento. Restaurantes de especialidad, paquetes de bebidas, Wi-Fi y excursiones se cobran aparte."),
                      ("🔊", "Más animado por diseño", "Más huéspedes significa más energía, cubiertas de piscina concurridas y filas en horas punta. Ese es el intercambio por la variedad y el precio."),
                  ])
                  + "<p>Entre las líneas que cubrimos, "
                  + link("/es/lines/royal-caribbean/", "Royal Caribbean")
                  + " y " + link("/es/lines/carnival/", "Carnival")
                  + " están claramente aquí, y "
                  + link("/es/lines/msc/", "MSC")
                  + " aporta un acento europeo a la misma idea de barco grande. "
                  + link("/es/lines/margaritaville-at-sea/", "Margaritaville at Sea")
                  + " trabaja el extremo de las escapadas cortas.</p>"
                  + tip("Si consideras este nivel, lee primero "
                        + link("/es/guides/whats-included/", "qué incluye la tarifa de un crucero")
                        + ". Aquí es donde más se separa la tarifa anunciada de tu cuenta final, y se maneja bien "
                          "en cuanto sabes qué extras quieres de verdad."),
         }},
        {"id": "premium", "h2": {"en": "Premium: calmer ships, more included",
                                 "es": "Premium: barcos más tranquilos, más incluido"},
         "html": {
            "en": "<p>Premium is the middle ground, and for a lot of travellers it is the sweet spot. The ships are "
                  "usually smaller than the contemporary giants, carry fewer guests, and give each of them more "
                  "room. The pace slows down. The entertainment leans toward music, enrichment and good food "
                  "rather than waterslides.</p>"
                  + vcards([
                      ("🌊", "More space per guest", "Fewer people on a similar hull means quieter decks, easier seating and shorter queues, which is what most people actually notice day to day."),
                      ("🍽️", "Food and service move up", "More attention on the dining rooms, more staff per guest, and a service style that gets to know you over the week."),
                      ("🎻", "A gentler evening", "Live music, theatre, talks and enrichment sessions rather than headline production spectacle. Quieter, not duller."),
                      ("🗺️", "More time in port", "Premium itineraries often stay later or overnight, which suits travellers who cruise mainly for the destinations."),
                  ])
                  + "<p>Of the lines we cover, "
                  + link("/en/lines/princess/", "Princess")
                  + ", " + link("/en/lines/celebrity/", "Celebrity")
                  + " and " + link("/en/lines/holland-america/", "Holland America")
                  + " sit in this space, each with its own character. "
                  + link("/en/lines/cunard/", "Cunard")
                  + " is its own case: a traditional ocean liner experience with formal evenings that does not map "
                    "neatly onto any tier.</p>"
                  + watch("<b>Premium does not mean everything is included.</b> More is bundled than on a "
                          "contemporary ship, but the specific list varies by line and by the fare you book. "
                          "Always check what your particular fare covers rather than assuming the tier decides it."),
            "es": "<p>Premium es el punto medio, y para muchos viajeros es el equilibrio ideal. Los barcos suelen "
                  "ser más pequeños que los gigantes contemporáneos, llevan menos huéspedes y dan más espacio a "
                  "cada uno. El ritmo baja. El entretenimiento se inclina a la música, el aprendizaje y la buena "
                  "comida más que a los toboganes.</p>"
                  + vcards([
                      ("🌊", "Más espacio por huésped", "Menos gente en un casco similar significa cubiertas más tranquilas, sitio para sentarse y menos filas, que es lo que más se nota a diario."),
                      ("🍽️", "Comida y servicio suben", "Más atención en los comedores, más personal por huésped y un servicio que llega a conocerte durante la semana."),
                      ("🎻", "Una noche más suave", "Música en vivo, teatro, charlas y sesiones de aprendizaje más que grandes espectáculos de producción. Más tranquilo, no más aburrido."),
                      ("🗺️", "Más tiempo en puerto", "Los itinerarios premium suelen quedarse hasta tarde o pernoctar, ideal para quien viaja sobre todo por los destinos."),
                  ])
                  + "<p>De las líneas que cubrimos, "
                  + link("/es/lines/princess/", "Princess")
                  + ", " + link("/es/lines/celebrity/", "Celebrity")
                  + " y " + link("/es/lines/holland-america/", "Holland America")
                  + " están en este espacio, cada una con su carácter. "
                  + link("/es/lines/cunard/", "Cunard")
                  + " es un caso aparte: una experiencia tradicional de transatlántico con noches formales que no "
                    "encaja del todo en ningún nivel.</p>"
                  + watch("<b>Premium no significa que todo esté incluido.</b> Se agrupa más que en un barco "
                          "contemporáneo, pero la lista concreta varía según la línea y la tarifa que reserves. "
                          "Revisa siempre qué cubre tu tarifa en lugar de suponer que lo decide el nivel."),
         }},
        {"id": "luxury", "h2": {"en": "Luxury: small ships, nearly everything bundled",
                                "es": "Lujo: barcos pequeños, casi todo incluido"},
         "html": {
            "en": "<p>Luxury lines run the smallest ships of the three tiers, often carrying a few hundred guests "
                  "rather than a few thousand. The defining feature is not decor, it is the <b>all-inclusive "
                  "model</b>: most of what other tiers add to your onboard account is simply part of the fare.</p>"
                  + vcards([
                      ("🥂", "Mostly all-inclusive", "Dining, drinks, gratuities and often Wi-Fi are typically bundled. What exactly is covered varies by line, and some include shore excursions or flights too."),
                      ("👥", "Few guests, high staffing", "Small ships with a high ratio of crew to guests, which is where the personal service comes from."),
                      ("⚓", "Smaller ports", "Compact ships reach harbours the big ships cannot enter, so itineraries often look quite different."),
                      ("🤫", "Quiet by nature", "No waterslides, no big production spectacle. The draw is space, service and the destinations."),
                  ])
                  + "<p>We do not currently publish verified guides for luxury lines, so we will not pretend to "
                  "rank them here. What we can tell you is how to compare a luxury fare honestly against a premium "
                  "or contemporary one: add up what you would realistically spend on board in the other tier, then "
                  "compare the totals rather than the headline fares. That is the only comparison that means "
                  "anything.</p>",
            "es": "<p>Las líneas de lujo operan los barcos más pequeños de los tres niveles, a menudo con unos "
                  "cientos de huéspedes en lugar de miles. Su rasgo definitorio no es la decoración, es el "
                  "<b>modelo todo incluido</b>: gran parte de lo que otros niveles cargan a tu cuenta a bordo "
                  "simplemente forma parte de la tarifa.</p>"
                  + vcards([
                      ("🥂", "Casi todo incluido", "Comidas, bebidas, propinas y a menudo Wi-Fi suelen ir incluidos. Lo que cubre exactamente varía por línea, y algunas incluyen excursiones o vuelos."),
                      ("👥", "Pocos huéspedes, mucho personal", "Barcos pequeños con una alta proporción de tripulación por huésped, de donde viene el servicio personal."),
                      ("⚓", "Puertos más pequeños", "Los barcos compactos llegan a puertos donde los grandes no entran, así que los itinerarios suelen ser muy distintos."),
                      ("🤫", "Tranquilo por naturaleza", "Sin toboganes ni grandes espectáculos. El atractivo es el espacio, el servicio y los destinos."),
                  ])
                  + "<p>Por ahora no publicamos guías verificadas de líneas de lujo, así que no vamos a fingir que "
                  "las clasificamos aquí. Lo que sí podemos decirte es cómo comparar con honestidad una tarifa de "
                  "lujo frente a una premium o contemporánea: suma lo que gastarías de verdad a bordo en el otro "
                  "nivel y compara los totales, no las tarifas anunciadas. Es la única comparación que significa "
                  "algo.</p>",
         }},
        {"id": "where-tiers-blur", "h2": {"en": "Where the tiers blur", "es": "Dónde se difuminan los niveles"},
         "html": {
            "en": "<p>Treat the labels as a starting point, not a verdict. Several things cut across them:</p>"
                  + vcards([
                      ("🏨", "Suites change everything", "Book a suite on a contemporary ship and you often get a private restaurant, a dedicated lounge and priority everything. That day feels premium even though the ship is not."),
                      ("📅", "The sailing matters as much as the line", "The same ship in school holidays and in late autumn is two different holidays. Timing shifts the atmosphere more than the tier does."),
                      ("🚢", "Fleets are not uniform", "A line's newest ship and its oldest can feel a generation apart. Pick the ship, not just the brand."),
                      ("💼", "Fare types differ within a line", "One line can sell a bare fare and an inclusive one on the same sailing. What is bundled depends on which you book."),
                  ])
                  + "<p>This is exactly why " + link("/en/guides/big-ship-vs-small-ship/", "ship size")
                  + " and " + link("/en/guides/how-to-choose-a-cruise-line/", "how you match a line to how you travel")
                  + " are usually more useful questions than which tier a brand belongs to.</p>",
            "es": "<p>Toma las etiquetas como punto de partida, no como veredicto. Varias cosas las atraviesan:</p>"
                  + vcards([
                      ("🏨", "Las suites lo cambian todo", "Reserva una suite en un barco contemporáneo y sueles obtener restaurante privado, salón exclusivo y prioridad en todo. Ese día se siente premium aunque el barco no lo sea."),
                      ("📅", "La salida importa tanto como la línea", "El mismo barco en vacaciones escolares y en otoño son dos viajes distintos. La fecha cambia el ambiente más que el nivel."),
                      ("🚢", "Las flotas no son uniformes", "El barco más nuevo de una línea y el más antiguo pueden sentirse de generaciones distintas. Elige el barco, no solo la marca."),
                      ("💼", "Las tarifas difieren dentro de una línea", "Una misma línea puede vender una tarifa básica y otra inclusiva en la misma salida. Lo incluido depende de cuál reserves."),
                  ])
                  + "<p>Por eso " + link("/es/guides/big-ship-vs-small-ship/", "el tamaño del barco")
                  + " y " + link("/es/guides/how-to-choose-a-cruise-line/", "cómo ajustar la línea a tu forma de viajar")
                  + " suelen ser preguntas más útiles que a qué nivel pertenece una marca.</p>",
         }},
        {"id": "which-fits", "h2": {"en": "Which tier fits you", "es": "Qué nivel encaja contigo"},
         "html": {
            "en": "<p>Skip the labels and answer three questions honestly.</p>"
                  + vcards([
                      ("🎯", "Who is travelling?", "Kids or teens in the group pushes you toward contemporary, where the programming and the space for different ages exist. Adults travelling together have the full range open."),
                      ("🌅", "What is your ideal day at sea?", "A packed day with something on every deck is contemporary. A book, a long lunch and a talk in the afternoon is premium or luxury."),
                      ("💳", "How do you want to pay?", "Prefer a low fare and control over your extras, or a higher fare with almost nothing added later? That single preference separates the tiers more cleanly than anything else."),
                  ])
                  + "<p>If your answers pull in different directions, that is normal and it is worth a conversation "
                  "rather than a guess. Ships within a single line vary enough that the right one often sits "
                  "somewhere other than where the label points.</p>",
            "es": "<p>Olvida las etiquetas y responde tres preguntas con honestidad.</p>"
                  + vcards([
                      ("🎯", "¿Quién viaja?", "Niños o adolescentes en el grupo te empujan a contemporánea, donde existen los programas y el espacio para distintas edades. Los adultos que viajan juntos tienen todo el abanico abierto."),
                      ("🌅", "¿Cuál es tu día ideal en el mar?", "Un día lleno con algo en cada cubierta es contemporánea. Un libro, una comida larga y una charla por la tarde es premium o lujo."),
                      ("💳", "¿Cómo quieres pagar?", "¿Prefieres tarifa baja y control sobre tus extras, o tarifa más alta y casi nada añadido después? Esa sola preferencia separa los niveles mejor que ninguna otra cosa."),
                  ])
                  + "<p>Si tus respuestas apuntan a lados distintos, es normal y merece una conversación en vez de "
                  "una suposición. Los barcos dentro de una misma línea varían lo suficiente como para que el "
                  "adecuado esté a menudo en otro sitio del que señala la etiqueta.</p>",
         }},
    ],
    "faqs": {
        "en": [
            ("What is the difference between contemporary, premium and luxury cruise lines?", "Contemporary lines run the largest ships with the most activities and the lowest base fares, charging separately for extras. Premium lines run somewhat smaller ships at a calmer pace with more included and more space per guest. Luxury lines run small ships where most things, typically dining, drinks and gratuities, are bundled into a higher fare. The tiers describe style and inclusions, not quality."),
            ("Is a luxury cruise line better than a contemporary one?", "Not inherently. They are built for different holidays. A family wanting waterslides, kids clubs and evening shows will enjoy a contemporary ship far more than a quiet luxury one, and a couple wanting space and a slow pace will feel the opposite. Better means better matched to you."),
            ("Which cruise lines are considered contemporary?", "Contemporary is the mass-market tier built around large ships and a low entry fare. Among the lines we cover, Royal Caribbean and Carnival are the clearest examples, with MSC bringing a European style to the same big-ship approach. Lines do shift over time, so treat any list as a guide rather than a fixed classification."),
            ("Are premium cruises all-inclusive?", "Usually not fully. Premium fares bundle more than contemporary ones, but the exact list varies by line and by the fare type you book, and drinks or specialty dining are often still extra. Check what your specific fare covers rather than relying on the tier."),
            ("Is a premium cruise worth the extra cost?", "It depends on what you would have spent anyway. If you would buy a drinks package, eat in specialty restaurants and want a quieter ship, the gap narrows quickly once you compare full totals rather than headline fares. If you are happy with the main dining room and the included entertainment, contemporary gives you more for less."),
            ("Do the tiers mean the same thing on every cruise line?", "No. They are informal industry shorthand, not a regulated standard, so lines position themselves differently and change over time. Two lines described as premium can feel quite different on board, which is why the ship and the sailing date matter as much as the label."),
        ],
        "es": [
            ("¿Cuál es la diferencia entre líneas contemporáneas, premium y de lujo?", "Las contemporáneas operan los barcos más grandes con más actividades y las tarifas base más bajas, cobrando aparte los extras. Las premium operan barcos algo más pequeños a un ritmo más tranquilo, con más incluido y más espacio por huésped. Las de lujo operan barcos pequeños donde casi todo, normalmente comidas, bebidas y propinas, va incluido en una tarifa más alta. Los niveles describen estilo e inclusiones, no calidad."),
            ("¿Una línea de lujo es mejor que una contemporánea?", "No por sí misma. Están hechas para viajes distintos. Una familia que quiere toboganes, clubes infantiles y espectáculos disfrutará mucho más un barco contemporáneo que uno de lujo silencioso, y una pareja que busca espacio y calma sentirá lo contrario. Mejor significa mejor ajustado a ti."),
            ("¿Qué líneas se consideran contemporáneas?", "Contemporánea es el nivel masivo construido en torno a barcos grandes y una tarifa de entrada baja. Entre las líneas que cubrimos, Royal Caribbean y Carnival son los ejemplos más claros, y MSC aporta un estilo europeo al mismo enfoque de barco grande. Las líneas cambian con el tiempo, así que toma cualquier lista como orientación y no como una clasificación fija."),
            ("¿Los cruceros premium son todo incluido?", "Normalmente no del todo. Las tarifas premium incluyen más que las contemporáneas, pero la lista exacta varía según la línea y el tipo de tarifa que reserves, y las bebidas o los restaurantes de especialidad suelen seguir siendo extra. Revisa qué cubre tu tarifa concreta en lugar de fiarte del nivel."),
            ("¿Vale la pena el coste extra de un crucero premium?", "Depende de lo que ibas a gastar de todos modos. Si comprarías un paquete de bebidas, cenarías en restaurantes de especialidad y quieres un barco más tranquilo, la diferencia se reduce rápido al comparar totales completos en vez de tarifas anunciadas. Si te basta el comedor principal y el entretenimiento incluido, la contemporánea te da más por menos."),
            ("¿Los niveles significan lo mismo en todas las líneas?", "No. Son jerga informal del sector, no un estándar regulado, así que cada línea se posiciona distinto y cambia con el tiempo. Dos líneas descritas como premium pueden sentirse muy diferentes a bordo, por eso el barco y la fecha importan tanto como la etiqueta."),
        ],
    },
    "related": {
        "en": [
            ("🚢", "How to choose a cruise line", "/en/guides/how-to-choose-a-cruise-line/", "Match a line to how you actually travel."),
            ("⚖️", "Big ship vs small ship", "/en/guides/big-ship-vs-small-ship/", "The size question that cuts across every tier."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "The difference between the fare and your final bill."),
            ("🔍", "Compare the lines side by side", "/en/compare/", "Put any two lines next to each other on the facts."),
        ],
        "es": [
            ("🚢", "Cómo elegir una línea de crucero", "/es/guides/how-to-choose-a-cruise-line/", "Ajusta la línea a tu forma real de viajar."),
            ("⚖️", "Barco grande vs barco pequeño", "/es/guides/big-ship-vs-small-ship/", "La pregunta de tamaño que atraviesa cada nivel."),
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "La diferencia entre la tarifa y tu cuenta final."),
            ("🔍", "Compara las líneas lado a lado", "/es/compare/", "Pon dos líneas cualquiera frente a frente con datos."),
        ],
    },
})
