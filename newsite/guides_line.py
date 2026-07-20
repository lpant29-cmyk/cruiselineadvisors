# -*- coding: utf-8 -*-
"""Rich guides cluster: line. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("how-to-choose-a-cruise-line", {
    "cat": "line",
    "hero": "cruise-ship-sea.jpg",
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
