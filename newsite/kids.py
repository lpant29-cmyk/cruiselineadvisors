# -*- coding: utf-8 -*-
"""Fleet-wide kids / teens / family programs, per line.

Cruise-line youth clubs are FLEET-WIDE brands, Carnival's Camp Ocean, Royal Caribbean's Adventure
Ocean, MSC's Doremiland, etc. run on every ship in the line, so we describe each line's program once
here and render it as rich cards on every ship page. This is the same age-band data our per-ship
enrichment read from the lines' official youth-program pages; ship-specific extras (e.g. an Ultimate
Family Suite, a named aquapark) stay on the individual ship in exp.kids_family. No prices. Original
copy, facts (club names, age bands) only, described in our own words.

KIDS_PROGRAMS[line_slug] = {"source": url, "verified": "YYYY-MM-DD",
    "cards": [{"name","ages","emo","desc":{"en","es"}}...]}
"""

KIDS_PROGRAMS = {
    "carnival": {
        "source": "https://www.carnival.com/onboard/camp-ocean",
        "verified": "2026-07-20",
        "cards": [
            {"name": "Camp Ocean", "ages": "2-11", "emo": "🐠",
             "desc": {"en": "Ocean-themed clubs split by age, Penguins (2-5), Sharks (6-8) and Stingrays (9-11), with games, crafts and marine-science play.",
                      "es": "Clubes con temática marina divididos por edad, Penguins (2-5), Sharks (6-8) y Stingrays (9-11), con juegos, manualidades y ciencia marina."}},
            {"name": "Circle “C”", "ages": "12-14", "emo": "🎮",
             "desc": {"en": "A tweens-only space with its own games, music and social events.",
                      "es": "Un espacio solo para preadolescentes con juegos, música y eventos sociales."}},
            {"name": "Club O2", "ages": "15-17", "emo": "🎧",
             "desc": {"en": "A teens-only hangout for older kids to meet up away from the younger crowd.",
                      "es": "Un lugar solo para adolescentes donde los mayores se reúnen lejos de los pequeños."}},
            {"name": "Night Owls", "ages": "late-night", "emo": "🌙",
             "desc": {"en": "Late-night supervised care so parents can enjoy the evening.",
                      "es": "Cuidado supervisado nocturno para que los padres disfruten la noche."}},
        ],
    },
    "royal-caribbean": {
        "source": "https://www.royalcaribbean.com/cruise-activities/adventure-ocean",
        "verified": "2026-07-20",
        "cards": [
            {"name": "Adventure Ocean", "ages": "3-12", "emo": "🚀",
             "desc": {"en": "Royal Caribbean's supervised youth program, grouped by age with games, science and imaginative play.",
                      "es": "El programa juvenil supervisado de Royal Caribbean, por grupos de edad con juegos, ciencia y juego imaginativo."}},
            {"name": "Teen programming", "ages": "13-17", "emo": "🎧",
             "desc": {"en": "Teen-only lounges and events so older kids have their own scene on board.",
                      "es": "Salones y eventos solo para adolescentes, para que los mayores tengan su propio ambiente."}},
        ],
    },
    "msc": {
        "source": "https://www.msccruises.com/en-gl/discover-msc/kids-cruise.aspx",
        "verified": "2026-07-20",
        "cards": [
            {"name": "Baby Club Chicco", "ages": "0-3", "emo": "🍼",
             "desc": {"en": "A club for babies and toddlers, designed together with Chicco.",
                      "es": "Un club para bebés y niños pequeños, diseñado junto con Chicco."}},
            {"name": "Mini Club", "ages": "3-6", "emo": "🧸",
             "desc": {"en": "Play and hands-on activities for young children.",
                      "es": "Juego y actividades para niños pequeños."}},
            {"name": "Juniors Club", "ages": "7-11", "emo": "🧱",
             "desc": {"en": "A school-age club with LEGO play, games and activities.",
                      "es": "Un club para edad escolar con juego LEGO, juegos y actividades."}},
            {"name": "Young & Teens Clubs", "ages": "12-17", "emo": "🎮",
             "desc": {"en": "Tween and teen clubs with gaming, music and social events.",
                      "es": "Clubes para preadolescentes y adolescentes con videojuegos, música y eventos."}},
        ],
    },
    "princess": {
        "source": "https://www.princess.com/en-us/ships-and-experience/things-to-do/youth-programs",
        "verified": "2026-07-20",
        "cards": [
            {"name": "Just For Kids", "ages": "3-7", "emo": "🌳",
             "desc": {"en": "A themed play world for the youngest cruisers with supervised activities.",
                      "es": "Un mundo de juego temático para los más pequeños con actividades supervisadas."}},
            {"name": "Just For Kids", "ages": "8-12", "emo": "🎨",
             "desc": {"en": "An activity center for school-age kids with crafts, games and events.",
                      "es": "Un centro de actividades para niños en edad escolar con manualidades, juegos y eventos."}},
            {"name": "Just For Teens", "ages": "13-17", "emo": "🎧",
             "desc": {"en": "A teen lounge with gaming, music and space to hang out.",
                      "es": "Un salón para adolescentes con videojuegos, música y espacio para reunirse."}},
        ],
    },
    "holland-america": {
        "source": "https://www.hollandamerica.com/en/us/onboard-experience/families",
        "verified": "2026-07-20",
        "cards": [
            {"name": "Club HAL", "ages": "3-12", "emo": "⚓",
             "desc": {"en": "Age-tiered supervised activities for kids; offered on select sailings.",
                      "es": "Actividades supervisadas por edad para niños; en salidas seleccionadas."}},
            {"name": "Club HAL Teens", "ages": "13-17", "emo": "🎮",
             "desc": {"en": "A separate space and program for teens.",
                      "es": "Un espacio y programa aparte para adolescentes."}},
        ],
    },
    "celebrity": {
        "source": "https://www.celebritycruises.com/things-to-do-onboard/camp-at-sea",
        "verified": "2026-07-20",
        "cards": [
            {"name": "Camp at Sea", "ages": "3-17", "emo": "🎨",
             "desc": {"en": "Celebrity's youth program with age-grouped arts, science, crafts and family activities.",
                      "es": "El programa juvenil de Celebrity con arte, ciencia, manualidades y actividades por grupos de edad."}},
        ],
    },
}


def line_program(line_slug):
    return KIDS_PROGRAMS.get(line_slug)
