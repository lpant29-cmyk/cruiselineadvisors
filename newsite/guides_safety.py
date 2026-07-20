# -*- coding: utf-8 -*-
"""Rich guides cluster: safety. Hand-written, no prices, no em dashes."""
from guidepage import register, tip, watch, define, vcards, link


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("avoid-cruise-scams", {
    "cat": "safety",
    "hero": "cruise-planning.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "How to avoid cruise scams and robocalls",
        "es": "Cómo evitar estafas de crucero y llamadas automáticas",
    },
    "dek": {
        "en": "Cruising attracts scammers because the trips are a big, emotional purchase. Most cons "
              "follow the same handful of patterns. Learn the red flags and you can spot a fake offer "
              "in seconds and book with confidence instead of anxiety.",
        "es": "Los cruceros atraen estafadores porque son una compra grande y emocional. La mayoría de "
              "los engaños siguen los mismos patrones. Aprende las señales de alarma y podrás detectar "
              "una oferta falsa en segundos y reservar con confianza en lugar de ansiedad.",
    },
    "takeaways": {
        "en": [
            "Pressure is the tell: real cruise offers do not need a countdown timer, a 'today only' deadline or a threat that the price vanishes if you hang up.",
            "You never won a cruise you did not enter. Unsolicited 'you have been selected' calls, texts and emails are the classic hook.",
            "Never give card numbers, bank details or a deposit to an unsolicited caller, or pay by gift card, wire or crypto. Legitimate bookings do not work that way.",
            "Check who you are actually dealing with, a real, licensed seller of travel, before any money changes hands.",
            "On the do-not-call list and still getting cruise robocalls? That itself is a sign the caller is not legitimate.",
        ],
        "es": [
            "La presión es la señal: las ofertas reales no necesitan un cronómetro, un límite de 'solo hoy' ni la amenaza de que el precio desaparece si cuelgas.",
            "Nunca ganaste un crucero al que no te inscribiste. Las llamadas, mensajes y correos no solicitados de 'has sido seleccionado' son el gancho clásico.",
            "Nunca des números de tarjeta, datos bancarios ni un depósito a quien llama sin que lo pidieras, ni pagues con tarjetas de regalo, transferencia o cripto. Las reservas legítimas no funcionan así.",
            "Verifica con quién tratas de verdad, un vendedor de viajes real y con licencia, antes de que cambie de manos cualquier dinero.",
            "¿Estás en la lista de no llamar y aún recibes llamadas automáticas de cruceros? Eso ya es señal de que quien llama no es legítimo.",
        ],
    },
    "sections": [
        {
            "id": "how-they-work",
            "h2": {"en": "How cruise scams work", "es": "Cómo funcionan las estafas de crucero"},
            "html": {
                "en": "<p>Nearly every cruise scam runs the same play: manufacture excitement (you 'won' something "
                      "amazing), then manufacture urgency (you must act right now), so you hand over money or details "
                      "before you have time to think. The prize is bait; the goal is your card number or a deposit.</p>"
                      + define("Robocall",
                               "an automated, pre-recorded phone call, often 'about your cruise reservation' or a "
                               "'complimentary cruise'. If you did not book anything, there is no reservation.")
                      + "<p>Once you know the pattern, the specific script does not matter. Excitement plus urgency "
                      "plus a request for money or details equals a scam, every time.</p>",
                "es": "<p>Casi todas las estafas de crucero usan la misma jugada: fabrican emoción (has 'ganado' algo "
                      "increíble), luego fabrican urgencia (debes actuar ya), para que entregues dinero o datos antes "
                      "de tener tiempo de pensar. El premio es el cebo; el objetivo es tu número de tarjeta o un "
                      "depósito.</p>"
                      + define("Llamada automática (robocall)",
                               "una llamada automatizada y pregrabada, a menudo 'sobre tu reserva de crucero' o un "
                               "'crucero de cortesía'. Si no reservaste nada, no hay reserva.")
                      + "<p>Una vez que conoces el patrón, el guion específico da igual. Emoción más urgencia más una "
                      "petición de dinero o datos es igual a estafa, siempre.</p>",
            },
        },
        {
            "id": "red-flags",
            "h2": {"en": "The red flags to watch for", "es": "Las señales de alarma a vigilar"},
            "html": {
                "en": vcards([
                    ("⏰", "Manufactured urgency", "'Today only', a countdown timer, or 'the price disappears if you hang up'. Real offers give you time."),
                    ("🎉", "A prize you never entered", "'You have been selected for a free cruise.' You cannot win a draw you never entered."),
                    ("💳", "Odd payment methods", "Gift cards, wire transfers, crypto or a deposit demanded on the spot. Legitimate bookings never ask for these."),
                    ("🔒", "Details up front", "Asking for card, bank or passport details before you know who they are, or refusing to identify themselves."),
                    ("📞", "Unsolicited robocalls", "Automated calls about a reservation you never made, especially if you are on a do-not-call list."),
                    ("✉️", "Lookalike branding", "Emails or sites that mimic a cruise line's logo but use odd addresses, misspellings or off-brand domains."),
                ]),
                "es": vcards([
                    ("⏰", "Urgencia fabricada", "'Solo hoy', un cronómetro, o 'el precio desaparece si cuelgas'. Las ofertas reales te dan tiempo."),
                    ("🎉", "Un premio al que no entraste", "'Has sido seleccionado para un crucero gratis.' No puedes ganar un sorteo en el que nunca participaste."),
                    ("💳", "Métodos de pago raros", "Tarjetas de regalo, transferencias, cripto o un depósito exigido en el momento. Las reservas legítimas nunca piden esto."),
                    ("🔒", "Datos por adelantado", "Pedir tarjeta, banco o pasaporte antes de saber quiénes son, o negarse a identificarse."),
                    ("📞", "Llamadas automáticas no solicitadas", "Llamadas automatizadas sobre una reserva que nunca hiciste, sobre todo si estás en una lista de no llamar."),
                    ("✉️", "Marca imitada", "Correos o sitios que imitan el logo de una línea pero usan direcciones raras, errores o dominios sospechosos."),
                ]),
            },
        },
        {
            "id": "protect",
            "h2": {"en": "How to protect yourself", "es": "Cómo protegerte"},
            "html": {
                "en": "<p>The habits that keep you safe are simple:</p>"
                      "<ul>"
                      "<li><b>Slow down.</b> Any legitimate offer survives a night's sleep. Urgency is the scammer's only real weapon; remove it and the con falls apart.</li>"
                      "<li><b>Never pay an unsolicited caller.</b> Do not give card or bank details, and never pay by gift card, wire or crypto.</li>"
                      "<li><b>Verify independently.</b> Hang up and reach the company yourself through a number or website you looked up, not one the caller gave you.</li>"
                      "<li><b>Confirm they are a licensed seller of travel.</b> Real agencies are registered and will happily tell you who they are.</li>"
                      "<li><b>Hang up on robocalls.</b> Do not press buttons to 'opt out', that just confirms a live number.</li>"
                      "</ul>"
                      + tip("A trustworthy company is happy to answer questions, put things in writing and give you time. If someone gets pushy the moment you slow down, that is your answer."),
                "es": "<p>Los hábitos que te mantienen a salvo son simples:</p>"
                      "<ul>"
                      "<li><b>Ve más despacio.</b> Cualquier oferta legítima sobrevive a una noche de sueño. La urgencia es la única arma real del estafador; quítala y el engaño se cae.</li>"
                      "<li><b>Nunca pagues a quien llama sin que lo pidieras.</b> No des datos de tarjeta ni banco, y nunca pagues con tarjeta de regalo, transferencia o cripto.</li>"
                      "<li><b>Verifica por tu cuenta.</b> Cuelga y contacta a la empresa tú mismo con un número o sitio que hayas buscado, no uno que te dio quien llamó.</li>"
                      "<li><b>Confirma que sean un vendedor de viajes con licencia.</b> Las agencias reales están registradas y con gusto te dicen quiénes son.</li>"
                      "<li><b>Cuelga las llamadas automáticas.</b> No presiones botones para 'darte de baja', eso solo confirma un número activo.</li>"
                      "</ul>"
                      + tip("Una empresa confiable responde preguntas con gusto, pone las cosas por escrito y te da tiempo. Si alguien se pone insistente en cuanto vas más despacio, esa es tu respuesta."),
            },
        },
        {
            "id": "how-we-work",
            "h2": {"en": "How a trustworthy referral actually works", "es": "Cómo funciona una referencia confiable"},
            "html": {
                "en": "<p>For the record, here is how we operate, and what any honest service should look like. We "
                      "publish verified, source-checked facts, and we connect you by phone to a licensed, independent "
                      "partner travel agency that quotes and books your trip under its own terms. We never cold-call "
                      "you, never pressure you, and never take payment for travel ourselves.</p>"
                      "<p>You call us, on your terms, when you are ready. That is the opposite of how a scam works, "
                      "and it is a useful benchmark for judging anyone else who contacts you.</p>",
                "es": "<p>Para que conste, así operamos, y así debería verse cualquier servicio honesto. Publicamos "
                      "datos verificados y comprobados en la fuente, y te conectamos por teléfono con una agencia de "
                      "viajes asociada, independiente y con licencia, que cotiza y reserva tu viaje bajo sus propios "
                      "términos. Nunca te llamamos en frío, nunca te presionamos y nunca cobramos por el viaje.</p>"
                      "<p>Tú nos llamas, en tus términos, cuando estás listo. Eso es lo opuesto a cómo funciona una "
                      "estafa, y es un buen punto de referencia para juzgar a cualquiera que te contacte.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("How do I know if a cruise offer is a scam?", "Look for pressure and prizes: a 'today only' deadline, a countdown, a cruise you 'won' without entering, or a demand for card details or a deposit up front. Any of those, especially together, means walk away and verify independently."),
            ("Why am I getting cruise robocalls?", "Automated 'about your cruise reservation' or 'free cruise' calls are a common scam. If you did not book anything, there is no reservation. Do not press buttons to opt out (that confirms a live number); just hang up."),
            ("Is a 'free cruise' offer ever real?", "Genuine promotions exist, but an unsolicited 'you have been selected' call or email almost never is, especially if it wants payment, a deposit or personal details to 'claim' the prize. Treat it as a scam until proven otherwise."),
            ("What payment methods are a red flag?", "Gift cards, wire transfers and cryptocurrency are never how a legitimate cruise is booked. Neither is handing card or bank details to someone who called you unsolicited."),
            ("How can I check a company is legitimate?", "Confirm they are a registered, licensed seller of travel, reach them through a number or website you looked up yourself, and make sure they will identify themselves and put details in writing. Honest companies welcome the questions."),
        ],
        "es": [
            ("¿Cómo sé si una oferta de crucero es estafa?", "Busca presión y premios: un límite de 'solo hoy', un cronómetro, un crucero que 'ganaste' sin participar, o exigir datos de tarjeta o un depósito por adelantado. Cualquiera de esos, sobre todo juntos, significa retirarte y verificar por tu cuenta."),
            ("¿Por qué recibo llamadas automáticas de cruceros?", "Las llamadas automáticas 'sobre tu reserva de crucero' o de 'crucero gratis' son una estafa común. Si no reservaste nada, no hay reserva. No presiones botones para darte de baja (confirma un número activo); solo cuelga."),
            ("¿Alguna vez es real una oferta de 'crucero gratis'?", "Existen promociones genuinas, pero una llamada o correo no solicitado de 'has sido seleccionado' casi nunca lo es, sobre todo si pide pago, depósito o datos personales para 'reclamar' el premio. Trátalo como estafa hasta que se pruebe lo contrario."),
            ("¿Qué métodos de pago son señal de alarma?", "Tarjetas de regalo, transferencias y criptomonedas nunca son la forma de reservar un crucero legítimo. Tampoco lo es dar datos de tarjeta o banco a alguien que te llamó sin que lo pidieras."),
            ("¿Cómo verifico que una empresa es legítima?", "Confirma que sean un vendedor de viajes registrado y con licencia, contáctalos por un número o sitio que buscaste tú, y asegúrate de que se identifiquen y pongan los detalles por escrito. Las empresas honestas reciben bien las preguntas."),
        ],
    },
    "related": {
        "en": [
            ("🎣", "Is that 'free cruise' offer real?", "/en/guides/free-cruise-offer-red-flags/", "The specific red flags behind 'you have won a cruise' offers."),
            ("💰", "How to find an affordable cruise", "/en/guides/how-to-find-affordable-cruise/", "Real value comes from timing and cabin choice, not gimmicks."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "Know the real cost so no 'deal' can fool you."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Book on your terms, one call, no pressure, ever."),
        ],
        "es": [
            ("🎣", "¿Es real esa oferta de 'crucero gratis'?", "/es/guides/free-cruise-offer-red-flags/", "Las señales de alarma detrás de las ofertas de 'has ganado un crucero'."),
            ("💰", "Cómo encontrar un crucero accesible", "/es/guides/how-to-find-affordable-cruise/", "El valor real viene del momento y el camarote, no de trucos."),
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Conoce el costo real para que ninguna 'oferta' te engañe."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Reserva en tus términos, una llamada, sin presión, nunca."),
        ],
    },
})


# ══════════════════════════════════════════════════════════════════════════════════════════════════
register("free-cruise-offer-red-flags", {
    "cat": "safety",
    "hero": "cruise-deck.jpg",
    "published": "2026-07-20",
    "updated": "2026-07-20",
    "title": {
        "en": "Is that 'free cruise' offer real? The red flags to know",
        "es": "¿Es real esa oferta de 'crucero gratis'? Las señales a conocer",
    },
    "dek": {
        "en": "A 'you have won a free cruise' call or email feels exciting for a reason: it is designed "
              "to. Here is how to tell a genuine promotion from the bait that is really after your card "
              "number, in about thirty seconds.",
        "es": "Una llamada o correo de 'has ganado un crucero gratis' emociona por una razón: está "
              "diseñado para eso. Aquí te decimos cómo distinguir una promoción genuina del cebo que "
              "en realidad busca tu número de tarjeta, en unos treinta segundos.",
    },
    "takeaways": {
        "en": [
            "You cannot win a draw you never entered. An unsolicited 'you have been selected' message is the number-one tell.",
            "If claiming the prize needs a payment, a deposit, 'taxes and fees' by gift card, or your card details, it is a scam.",
            "Real promotions come from a company you can identify and verify; scams hide behind spoofed numbers and lookalike branding.",
            "Urgency is the weapon: 'today only' and countdowns exist to stop you checking. A real offer survives a night's sleep.",
            "Even legitimate 'free cruise' promos usually have strings (deposits, deadlines, cabin restrictions); read them before you get excited.",
        ],
        "es": [
            "No puedes ganar un sorteo en el que nunca participaste. Un mensaje no solicitado de 'has sido seleccionado' es la señal número uno.",
            "Si reclamar el premio requiere un pago, un depósito, 'impuestos y tasas' por tarjeta de regalo o tus datos de tarjeta, es una estafa.",
            "Las promociones reales vienen de una empresa que puedes identificar y verificar; las estafas se esconden tras números falsificados y marcas imitadas.",
            "La urgencia es el arma: 'solo hoy' y los cronómetros existen para evitar que verifiques. Una oferta real sobrevive a una noche de sueño.",
            "Incluso las promos legítimas de 'crucero gratis' suelen tener condiciones (depósitos, plazos, restricciones de camarote); léelas antes de emocionarte.",
        ],
    },
    "sections": [
        {
            "id": "the-tell",
            "h2": {"en": "The one question that settles it", "es": "La única pregunta que lo resuelve"},
            "html": {
                "en": "<p>Before anything else, ask yourself: <b>did I enter this?</b> If a cruise arrives out of "
                      "nowhere, by call, text or email, and you never signed up for a draw, there is no prize. The "
                      "'win' exists only to get your attention and, a moment later, your details or a payment.</p>"
                      + tip("Genuine cruise promotions are things you opt into, a line's newsletter, a loyalty offer, "
                            "a booking with a real agency. They do not cold-call you to say you already won."),
                "es": "<p>Antes que nada, pregúntate: <b>¿yo participé en esto?</b> Si un crucero aparece de la nada, "
                      "por llamada, mensaje o correo, y nunca te inscribiste en un sorteo, no hay premio. El 'ganaste' "
                      "existe solo para captar tu atención y, un momento después, tus datos o un pago.</p>"
                      + tip("Las promociones genuinas son cosas a las que te inscribes: el boletín de una línea, una "
                            "oferta de fidelidad, una reserva con una agencia real. No te llaman en frío para decir "
                            "que ya ganaste."),
            },
        },
        {
            "id": "red-flags",
            "h2": {"en": "The red flags, at a glance", "es": "Las señales de alarma, de un vistazo"},
            "html": {
                "en": vcards([
                    ("🎟️", "A prize you never entered", "'You have been selected' for a draw you have no memory of joining."),
                    ("💳", "Pay to claim it", "'Just cover the taxes and fees' by gift card or card, or a refundable deposit to 'hold' it. Real prizes do not work this way."),
                    ("⏰", "Claim it now or lose it", "A countdown or 'today only' deadline that punishes you for checking."),
                    ("🕵️", "Vague or hidden identity", "They will not clearly say who they are, or the caller ID and email domain do not match the brand they claim."),
                    ("🔗", "Odd links and logos", "Lookalike cruise-line branding on a strange domain, misspellings, or links that do not go where they should."),
                ]),
                "es": vcards([
                    ("🎟️", "Un premio al que no entraste", "'Has sido seleccionado' para un sorteo que no recuerdas haber hecho."),
                    ("💳", "Paga para reclamarlo", "'Solo cubre los impuestos y tasas' por tarjeta de regalo o tarjeta, o un depósito 'reembolsable' para 'reservarlo'. Los premios reales no funcionan así."),
                    ("⏰", "Recláma­lo ya o lo pierdes", "Un cronómetro o límite de 'solo hoy' que te castiga por verificar."),
                    ("🕵️", "Identidad vaga u oculta", "No dicen con claridad quiénes son, o el identificador de llamada y el dominio del correo no coinciden con la marca que dicen ser."),
                    ("🔗", "Enlaces y logos raros", "Marca de línea imitada en un dominio extraño, errores de ortografía, o enlaces que no llevan a donde deberían."),
                ]),
            },
        },
        {
            "id": "what-to-do",
            "h2": {"en": "What to do when one lands", "es": "Qué hacer cuando llega una"},
            "html": {
                "en": "<p>Stay calm and do three things:</p>"
                      "<ul>"
                      "<li><b>Do not pay or share anything.</b> No card, no bank details, no 'taxes' by gift card, no deposit to a caller you did not contact.</li>"
                      "<li><b>Slow it down.</b> Tell them you will call back, then hang up. Real offers survive the wait; scams evaporate.</li>"
                      "<li><b>Verify independently.</b> If you are genuinely curious, look up the company yourself and ask them to confirm it in writing. A real business is glad to.</li>"
                      "</ul>"
                      + watch("Never press a number to 'speak to an agent' or 'opt out' of a robocall. It only confirms your line is live and invites more calls.")
                      ,
                "es": "<p>Mantén la calma y haz tres cosas:</p>"
                      "<ul>"
                      "<li><b>No pagues ni compartas nada.</b> Ni tarjeta, ni datos bancarios, ni 'impuestos' por tarjeta de regalo, ni un depósito a quien no contactaste.</li>"
                      "<li><b>Ve más despacio.</b> Diles que devolverás la llamada y cuelga. Las ofertas reales sobreviven la espera; las estafas se evaporan.</li>"
                      "<li><b>Verifica por tu cuenta.</b> Si de verdad te interesa, busca la empresa tú mismo y pide que lo confirmen por escrito. Un negocio real lo hace con gusto.</li>"
                      "</ul>"
                      + watch("Nunca presiones un número para 'hablar con un agente' o 'darte de baja' de una llamada automática. Solo confirma que tu línea está activa e invita más llamadas.")
                      ,
            },
        },
        {
            "id": "bottom-line",
            "h2": {"en": "The bottom line", "es": "En conclusión"},
            "html": {
                "en": "<p>Real value in cruising is never a surprise prize. It comes from picking the right week, the "
                      "right cabin and the right itinerary, and from booking with people you chose to contact. If an "
                      "offer arrives uninvited and wants money or details to 'claim' it, that is your answer.</p>"
                      "<p>Want a genuinely good cruise for your budget, with no gimmicks? Read "
                      + link("/en/guides/how-to-find-affordable-cruise/", "how to find an affordable cruise") +
                      ", then call us on your terms when you are ready.</p>",
                "es": "<p>El valor real en los cruceros nunca es un premio sorpresa. Viene de elegir la semana, el "
                      "camarote y el itinerario correctos, y de reservar con gente que tú elegiste contactar. Si una "
                      "oferta llega sin invitación y quiere dinero o datos para 'reclamarla', esa es tu respuesta.</p>"
                      "<p>¿Quieres un buen crucero para tu presupuesto, sin trucos? Lee "
                      + link("/es/guides/how-to-find-affordable-cruise/", "cómo encontrar un crucero accesible") +
                      ", y luego llámanos en tus términos cuando estés listo.</p>",
            },
        },
    ],
    "faqs": {
        "en": [
            ("Are free cruise offers real?", "Genuine promotions exist, but an unsolicited 'you have won a cruise' call or email almost never is, especially if claiming it needs a payment, deposit or your card details. Treat any prize you did not enter as a scam until you can verify it independently."),
            ("Why do they ask for 'taxes and fees' on a free cruise?", "It is a classic scam mechanic: the 'prize' is free, but you must pay taxes and fees, often by gift card, up front. Legitimate prizes never require payment by gift card, wire or crypto to release them."),
            ("How do I claim a legitimate cruise promotion safely?", "Only through a company you can identify and verify, contacted via a number or website you looked up yourself. Ask for the terms in writing, and never hand over payment or personal details to someone who reached out to you unsolicited."),
            ("A caller says it is about my cruise reservation, but I did not book. What is it?", "A scam. If you never booked, there is no reservation. Do not press any buttons or share details; just hang up."),
            ("Do real 'free' cruise promos have catches?", "Usually yes, deposits, deadlines, cabin or date restrictions, or add-on costs. That does not make them scams, but you should read the fine print before you get excited or hand over anything."),
        ],
        "es": [
            ("¿Son reales las ofertas de crucero gratis?", "Existen promociones genuinas, pero una llamada o correo no solicitado de 'has ganado un crucero' casi nunca lo es, sobre todo si reclamarlo requiere un pago, depósito o tus datos de tarjeta. Trata cualquier premio en el que no participaste como estafa hasta verificarlo por tu cuenta."),
            ("¿Por qué piden 'impuestos y tasas' por un crucero gratis?", "Es un mecanismo clásico de estafa: el 'premio' es gratis, pero debes pagar impuestos y tasas, a menudo por tarjeta de regalo, por adelantado. Los premios legítimos nunca requieren pago por tarjeta de regalo, transferencia o cripto para liberarlos."),
            ("¿Cómo reclamo una promoción de crucero legítima de forma segura?", "Solo a través de una empresa que puedas identificar y verificar, contactada por un número o sitio que buscaste tú. Pide los términos por escrito, y nunca entregues pago ni datos personales a quien te contactó sin que lo pidieras."),
            ("Alguien dice que llama por mi reserva de crucero, pero no reservé. ¿Qué es?", "Una estafa. Si nunca reservaste, no hay reserva. No presiones botones ni compartas datos; solo cuelga."),
            ("¿Las promos de crucero 'gratis' reales tienen condiciones?", "Normalmente sí: depósitos, plazos, restricciones de camarote o fecha, o costos adicionales. Eso no las hace estafas, pero debes leer la letra pequeña antes de emocionarte o entregar nada."),
        ],
    },
    "related": {
        "en": [
            ("🛡️", "How to avoid cruise scams & robocalls", "/en/guides/avoid-cruise-scams/", "The full playbook for spotting and shutting down cruise cons."),
            ("💰", "How to find an affordable cruise", "/en/guides/how-to-find-affordable-cruise/", "Real value, the honest way, no prize needed."),
            ("🧾", "What's included in a cruise fare", "/en/guides/whats-included/", "Know the real cost so no 'free' offer can fool you."),
            ("🧭", "Find a cruise that fits", "/en/compare/", "Book on your terms; we never cold-call or pressure."),
        ],
        "es": [
            ("🛡️", "Cómo evitar estafas y llamadas automáticas", "/es/guides/avoid-cruise-scams/", "El manual completo para detectar y frenar los engaños de crucero."),
            ("💰", "Cómo encontrar un crucero accesible", "/es/guides/how-to-find-affordable-cruise/", "Valor real, de forma honesta, sin premios."),
            ("🧾", "Qué incluye la tarifa de un crucero", "/es/guides/whats-included/", "Conoce el costo real para que ninguna oferta 'gratis' te engañe."),
            ("🧭", "Encuentra un crucero que encaje", "/es/compare/", "Reserva en tus términos; nunca llamamos en frío ni presionamos."),
        ],
    },
})
