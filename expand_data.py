#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expands data/cruise-lines.json to the 8 launch lines.
Facts are VERIFY-flagged; editorial prose is original and final."""
import json, os, copy

ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(ROOT, "data", "cruise-lines.json")

data = json.load(open(PATH, encoding="utf-8"))
template = data["lines"][0]           # royal-caribbean is the shape reference

def V(): return "VERIFY"

def blank_class(name, year, feats, regions):
    return {"class": name, "ships": ["VERIFY"], "first_in_service": year,
            "capacity_double": V(), "decks": V(), "gross_tonnage": V(),
            "features": feats, "typical_regions": regions,
            "source": V(), "verified": "PENDING"}

def inc(item, note=""):
    return {"item": item, "note": note, "source": V(), "verified": "PENDING"}

BASE_EXTRA = [
    inc("Gratuities", "Auto-added daily per guest; VERIFY current amount"),
    inc("Alcohol, soda, speciality coffee", "Packages available"),
    inc("Speciality restaurants", "Cover charge or à la carte"),
    inc("Wi-fi", "Tiered packages"),
    inc("Shore excursions"),
    inc("Spa and salon"),
    inc("Casino and arcade"),
    inc("Laundry and pressing"),
]
BASE_INC = [
    inc("Main dining room", "Set or flexible seating"),
    inc("Buffet", "Open most of the day"),
    inc("Select casual venues", "VERIFY which are complimentary by class"),
    inc("Main theatre productions"),
    inc("Pools and sports decks"),
    inc("Fitness centre", "Classes may carry a fee"),
    inc("Kids club", "VERIFY age bands and hours"),
    inc("Water, drip coffee, tea, select juice", "VERIFY exact list"),
]

LINES = [
 {"slug":"carnival","name":"Carnival","legal":"Carnival Cruise Line",
  "theme":{"c1":"#8a1c2b","c2":"#c8362c","accent":"#ff8a5c","emoji":"🎉"},
  "pos":"fun-first-value","one":"Casual, high-energy sailings from more US home ports than any other line.",
  "founded":1972,"hq":"Miami, Florida","parent":"Carnival Corporation & plc",
  "loyalty":"VIFP Club","tiers":["Blue","Red","Gold","Platinum","Diamond"],
  "classes":[blank_class("Excel",2020,["roller coaster at sea","multiple dining zones","waterworks"],["Caribbean","Bahamas"]),
             blank_class("Vista",2016,["IMAX theatre","ropes course","waterworks"],["Caribbean","Mediterranean"]),
             blank_class("Dream",2009,["waterworks","large pool decks"],["Caribbean","Bahamas"]),
             blank_class("Conquest",2002,["classic layout","value deployment"],["Caribbean","Mexico"]),
             blank_class("Spirit",2001,["smaller footprint","unusual itineraries"],["Alaska","Hawaii","Panama Canal"])],
  "kids":"Camp Ocean",
  "for":["Budget-conscious families","First-time cruisers testing the format","Short 3–5 night getaways",
         "Travellers who can drive to a home port","Groups wanting a social atmosphere"],
  "not":["Travellers seeking a refined or quiet atmosphere","Those prioritising gourmet dining",
         "Cruisers who dislike party energy","Anyone wanting extensive enrichment programming"],
  "faqs":[("Is Carnival only for young party crowds?","Not uniformly. Short weekend sailings draw the liveliest crowds; longer itineraries and off-peak dates attract a broader mix including families and older travellers. Choosing the right sailing length matters more than choosing the right ship."),
          ("Why are so many people driving to their cruise?","Carnival sails from more US home ports than any other line, including several that competitors ignore. For a family of four, removing four airfares changes the entire budget — worth checking before you assume you need to fly."),
          ("What is a cove balcony?","A balcony set lower in the hull, closer to the waterline and more sheltered than a standard balcony. Only some ships have them. It's a distinctive option most booking sites won't explain to you.")],
  "cost":[("Home port choice","Driving instead of flying removes the largest single variable for most families. Compare drive-to ports before anything else."),
          ("Sailing length","Short 3–5 night sailings cost less overall but more per night. Seven nights is often better value per day."),
          ("Ship age","Newer classes command a premium over older tonnage sailing similar routes."),
          ("Cabin category","Interior to balcony is the biggest single step. Cove balconies sit in between on some ships."),
          ("School holiday timing","Holiday weeks are the busiest and most expensive of the year."),
          ("What you add on","Gratuities, drinks packages, speciality dining and excursions change the all-in total substantially.")]},

 {"slug":"holland-america","name":"Holland America","legal":"Holland America Line",
  "theme":{"c1":"#0b3d4f","c2":"#17708a","accent":"#6fd0d8","emoji":"🧊"},
  "pos":"classic-premium","one":"Mid-size ships, an unhurried pace, and decades of Alaska experience.",
  "founded":1873,"hq":"Seattle, Washington","parent":"Carnival Corporation & plc",
  "loyalty":"Mariner Society","tiers":["1-Star","2-Star","3-Star","4-Star","5-Star"],
  "classes":[blank_class("Pinnacle",2016,["music venue complex","expanded dining","largest suites"],["Alaska","Caribbean","Europe"]),
             blank_class("Signature",2008,["traditional design","modern amenities"],["Alaska","Caribbean"]),
             blank_class("Vista",2002,["smaller footprint","longer itineraries"],["Europe","World voyages"])],
  "kids":"Club HAL",
  "for":["Alaska and glacier-focused travellers","Couples and older cruisers","Music and culinary enthusiasts",
         "Longer voyages and world cruise segments","Travellers who want port depth over onboard spectacle"],
  "not":["Families needing extensive children's programming","Travellers wanting waterslides and thrill rides",
         "Those seeking nightlife-driven sailings","Budget-first shoppers"],
  "faqs":[("Is Holland America genuinely better for Alaska?","It is one of the longest-operating lines in the region with established glacier access and integrated land programmes. Whether it beats alternatives for your trip depends on your dates, budget and whether you want a land extension."),
          ("What is a cruisetour?","A one-way sailing combined with an inland land programme travelling by rail and coach toward the interior national park. More moving parts than a standard cruise, which is why most travellers arrange it by phone."),
          ("Is the average passenger older?","Generally yes, particularly on longer voyages and off-peak dates. Alaska summer sailings and holiday periods draw a broader mix.")],
  "cost":[("Alaska season timing","May and September sail for less than July but bring cooler, wetter weather and less wildlife activity."),
          ("Verandah vs interior","On scenic itineraries a verandah earns its cost far more than on a Caribbean sailing — you use it constantly."),
          ("Voyage length","Longer voyages frequently deliver the lowest cost per night in the fleet."),
          ("Cruisetour add-on","Land extensions add rail, hotels and transfers — a separate budget line from the sailing."),
          ("Ship class","The newest class carries a premium over older tonnage on similar routes."),
          ("What you add on","Gratuities, drinks, speciality dining and excursions change the total meaningfully.")]},

 {"slug":"celebrity","name":"Celebrity Cruises","legal":"Celebrity Cruises",
  "theme":{"c1":"#1a2b4a","c2":"#3d5a8a","accent":"#a89bd6","emoji":"🥂"},
  "pos":"premium-modern","one":"Design-led ships with a calmer, adult-leaning atmosphere and serious food.",
  "founded":1988,"hq":"Miami, Florida","parent":"Royal Caribbean Group",
  "loyalty":"Captain's Club","tiers":["Preview","Classic","Select","Elite","Elite Plus","Zenith"],
  "classes":[blank_class("Edge",2018,["infinite verandah","cantilevered deck platform","multiple main restaurants"],["Caribbean","Europe","Alaska"]),
             blank_class("Solstice",2008,["real grass lawn deck","glass-forward design"],["Caribbean","Alaska","Australia"]),
             blank_class("Millennium",2000,["smaller footprint","refurbished interiors"],["Europe","Asia","Caribbean"])],
  "kids":"Camp at Sea",
  "for":["Couples and adult groups","Food-focused travellers","Design and architecture enthusiasts",
         "Alaska, Europe and Caribbean in comfort","Cruisers upgrading from mainstream lines"],
  "not":["Families wanting large children's programmes","Travellers seeking waterparks and thrill attractions",
         "Strict budget shoppers","Those who prefer traditional formal ocean-liner style"],
  "faqs":[("What exactly is an infinite verandah?","A cabin design where the living space extends to the ship's edge with a retractable upper window, rather than a separate outdoor balcony. Some travellers prefer it; others miss a traditional open balcony. Understand which you're booking."),
          ("How is Celebrity different from mainstream lines?","Quieter atmosphere, stronger food and design, fewer large family attractions, and a higher fare that often includes more. Whether that trade is worth it depends on what you value on board."),
          ("Is suite class worth it?","Suite class functions almost as a separate product with its own restaurant, lounge and deck. It's a bigger step up than the equivalent on most lines.")],
  "cost":[("Promotional inclusions","Fares frequently bundle drinks, wi-fi and gratuities. The headline fare alone is a poor comparison tool — compare all-in."),
          ("Ship class","The newest class and the oldest are very different products at different price points."),
          ("Verandah type","Infinite verandah, traditional balcony and sunset verandah price differently."),
          ("Suite class","A separate tier with its own dining and spaces, priced accordingly."),
          ("Season","European shoulder months cost less than peak summer and are usually more pleasant."),
          ("What you add on","Speciality dining and excursions are the main variables once drinks are bundled.")]},

 {"slug":"princess","name":"Princess Cruises","legal":"Princess Cruises",
  "theme":{"c1":"#0a3550","c2":"#17679a","accent":"#5ec6e8","emoji":"🧭"},
  "pos":"premium-mainstream","one":"A balanced middle path with one of the widest itinerary maps at sea.",
  "founded":1965,"hq":"Santa Clarita, California","parent":"Carnival Corporation & plc",
  "loyalty":"Captain's Circle","tiers":["Gold","Ruby","Platinum","Elite"],
  "classes":[blank_class("Sphere",2023,["multi-deck glass atrium","expanded dining"],["Caribbean","Europe"]),
             blank_class("Royal",2013,["balanced layout","wide deployment"],["Alaska","Caribbean","Europe"]),
             blank_class("Grand",1998,["smaller footprint","distinctive itineraries"],["Japan","Australia","World"])],
  "kids":"Camp Discovery",
  "for":["Multi-generation groups needing common ground","Alaska travellers wanting a land extension",
         "Unusual destinations — Japan, Australia, world segments","Couples and older travellers",
         "Cruisers who value itinerary over onboard spectacle"],
  "not":["Travellers wanting waterparks and thrill attractions","Those seeking nightlife-driven sailings",
         "Budget-first shoppers","Anyone wanting a strictly adults-only atmosphere"],
  "faqs":[("Why do people choose Princess for Alaska?","The line pairs one-way sailings with rail-based land tours reaching the interior national park. Assembling that independently is difficult, which is why most travellers book it by phone."),
          ("Is Princess good for families?","It works well for multi-generation groups travelling together, but it isn't built around children the way family-focused lines are. If children are the primary consideration, other lines offer more."),
          ("What does the wearable device actually do?","Boarding, cabin access, onboard payments and locating your party. It's more useful with a large group — set it up before boarding rather than at the terminal.")],
  "cost":[("Cruisetour vs cruise only","Land extensions add rail, hotels and transfers as a separate budget line."),
          ("Region","Japan, Australia and world segments price very differently from Caribbean sailings."),
          ("Balcony value by itinerary","On Alaska and Norway a balcony is worth far more than on a Caribbean sailing."),
          ("Ship class","The fleet spans several generations with meaningfully different facilities."),
          ("Voyage length","Longer repositioning and world segments often carry the lowest per-night cost."),
          ("What you add on","Gratuities, drinks, speciality dining and excursions change the all-in total.")]},

 {"slug":"msc","name":"MSC Cruises","legal":"MSC Cruises",
  "theme":{"c1":"#0a2f5e","c2":"#1461a8","accent":"#f0b64f","emoji":"🍋"},
  "pos":"international-mainstream","one":"European-owned, international on board, and consistently competitive.",
  "founded":1989,"hq":"Geneva, Switzerland","parent":"MSC Group",
  "loyalty":"MSC Voyagers Club","tiers":["Classic","Silver","Gold","Diamond"],
  "classes":[blank_class("World",2022,["expanded dining districts","multi-deck entertainment"],["Caribbean","Mediterranean"]),
             blank_class("Meraviglia",2017,["covered indoor promenade","digital sky ceiling"],["Caribbean","Mediterranean"]),
             blank_class("Seaside",2017,["waterfront promenades","extensive outdoor deck"],["Caribbean"])],
  "kids":"MSC Kids Clubs",
  "for":["Value-focused travellers","Those who enjoy an international atmosphere","Mediterranean and European itineraries",
         "Yacht Club travellers wanting a boutique experience","Families comfortable in a multilingual environment"],
  "not":["Travellers wanting a strictly American onboard culture","Those expecting US-style service norms throughout",
         "Cruisers seeking extensive enrichment programming","Anyone who dislikes multilingual announcements"],
  "faqs":[("Will there be a language barrier?","Announcements are typically made in several languages and crew speak English, but the atmosphere is noticeably more international than US-based lines. Most travellers adapt quickly; a few find it disorienting."),
          ("What is the Yacht Club?","A gated suite area with private restaurant, lounge, pool and dedicated service — effectively a boutique ship inside the larger vessel. It's the line's standout offering and a different product entirely."),
          ("Is MSC cheaper for a reason?","Fares reflect scale and European cost structures. Service style differs from US norms rather than being simply lesser — worth setting expectations before you sail.")],
  "cost":[("Yacht Club vs standard","A genuinely different product — compare it against a premium line's balcony, not against an MSC balcony."),
          ("Drinks package tier","Inclusions differ more between tiers than on US lines. Read what each covers."),
          ("Region","European sailings feel more international than the line's Caribbean deployment and price differently."),
          ("Ship age","The fleet is modern; newer vessels are notably better equipped."),
          ("Season","Mediterranean shoulder months cost less and avoid August heat and crowds."),
          ("What you add on","Speciality dining, excursions and wi-fi are the main variables.")]},

 {"slug":"cunard","name":"Cunard","legal":"Cunard Line",
  "theme":{"c1":"#3a1518","c2":"#8a2a26","accent":"#e0a458","emoji":"🎩"},
  "pos":"classic-luxury","one":"The last line running genuine scheduled transatlantic crossings.",
  "founded":1840,"hq":"Southampton, United Kingdom","parent":"Carnival Corporation & plc",
  "loyalty":"Cunard World Club","tiers":["Silver","Gold","Platinum","Diamond"],
  "classes":[blank_class("Flagship liner",2004,["planetarium at sea","ballroom","deeper ocean-liner hull"],["Transatlantic","World voyages"]),
             blank_class("Queens class",2007,["traditional public rooms","ballroom","afternoon tea"],["Europe","Caribbean","World"])],
  "kids":"The Play Zone",
  "for":["Travellers seeking genuine transatlantic crossings","Lovers of formal dining and ballroom dancing",
         "Those who enjoy sea days over port days","Couples and solo travellers wanting classic service",
         "Anyone who dislikes waterslides and deck parties"],
  "not":["Families with young children","Travellers who dislike dress codes",
         "Those wanting maximum port time","Cruisers seeking casual, high-energy atmospheres"],
  "faqs":[("What is a transatlantic crossing actually like?","Roughly a week of open ocean between New York and Southampton with no port calls. Days are filled with lectures, dancing, dining and the sea. Travellers either find it deeply restorative or extremely long — there's little middle ground."),
          ("How formal is it really?","More formal than any other mainstream line. Gala evenings carry real expectations and most passengers observe them enthusiastically. If dressing for dinner sounds like a burden, another line suits you better."),
          ("Does cabin grade really affect dining?","Yes — your cabin grade determines your restaurant assignment, with suite guests in separate dining rooms. This makes cabin choice more consequential here than on any other line.")],
  "cost":[("Cabin grade determines dining","Grade sets your restaurant assignment, so the decision carries more weight than price alone suggests."),
          ("Crossing vs cruise","Scheduled crossings price differently from cruise itineraries and often include one-way air considerations."),
          ("Season","Summer crossings sail calmer seas; autumn and winter are rougher and priced accordingly."),
          ("Balcony value","Less useful on North Atlantic crossings where weather often keeps them closed."),
          ("Voyage length","World voyage segments vary enormously by length and region."),
          ("What you add on","Gratuities, drinks, speciality dining and excursions change the total.")]},

 {"slug":"margaritaville-at-sea","name":"Margaritaville at Sea","legal":"Margaritaville at Sea",
  "theme":{"c1":"#0a4a52","c2":"#12897f","accent":"#f5c74d","emoji":"🌴"},
  "pos":"island-casual-short","one":"Short, warm Bahamas getaways with almost no agenda.",
  "founded":2022,"hq":"Florida","parent":"VERIFY",
  "loyalty":"VERIFY","tiers":["VERIFY"],
  "classes":[blank_class("Getaway vessels",2022,["multiple bars","live music venues","casual dining","pool decks"],["Bahamas"])],
  "kids":"VERIFY",
  "for":["First-time cruisers testing the format","Long-weekend escapes from Florida",
         "Groups and celebrations on a budget","Travellers who want warmth without a long trip",
         "Anyone who values simplicity over ship facilities"],
  "not":["Travellers wanting extensive ship attractions","Those seeking long or exotic itineraries",
         "Cruisers expecting premium dining","Families needing large children's programmes"],
  "faqs":[("Is this a good first cruise?","For many travellers, yes. A short sailing is the cheapest, lowest-risk way to find out whether cruising suits you before committing to a week or more."),
          ("How does it compare to the big lines?","Smaller ships and far fewer onboard attractions, offset by lower cost, shorter commitment and a specific relaxed atmosphere. A different product rather than a lesser version of the same one."),
          ("Can I really do this as a weekend?","Departure and return timings make it genuinely feasible as a long weekend from many US cities. Worth confirming flight timings against the sailing schedule.")],
  "cost":[("Sailing length","Two to four nights keeps the total low but the per-night rate higher than a week-long sailing."),
          ("Season","Winter and spring bring the driest weather; late summer carries hurricane-season risk."),
          ("Cabin category","On sailings this short many travellers choose lower categories and live in the public spaces."),
          ("Getting to the port","Florida departure means drive-to for many travellers, removing airfare entirely."),
          ("Group bookings","Cabin blocks for celebrations are handled differently from individual bookings."),
          ("What you add on","Drinks, speciality dining, excursions and gratuities are the main variables.")]},
]

out = [template]   # keep royal-caribbean

for L in LINES:
    n = copy.deepcopy(template)
    n["slug"] = L["slug"]; n["name"] = L["name"]; n["legal_name"] = L["legal"]
    n["theme"] = L["theme"]; n["positioning"] = L["pos"]; n["one_line"] = L["one"]
    n["company"] = {"founded": L["founded"], "headquarters": L["hq"], "parent": L["parent"],
                    "loyalty_program": L["loyalty"], "loyalty_tiers": L["tiers"],
                    "fleet_size": V(), "source": V(), "verified": "PENDING"}
    n["ship_classes"] = L["classes"]
    n["inclusions"] = {"_refresh": "30 days", "included": copy.deepcopy(BASE_INC),
                       "extra_cost": copy.deepcopy(BASE_EXTRA),
                       "gratuity_per_person_per_day": V(), "gratuity_suite_rate": V(),
                       "room_service": {"available": True, "fee": V(), "source": V(), "verified": "PENDING"}}
    n["cabins"] = {"categories": ["VERIFY - list the line's own category names"],
                   "virtual_balcony": {"exists": False}, "neighbourhood_balcony": {"exists": False},
                   "connecting_cabins": {"available": True, "note": V(), "source": V(), "verified": "PENDING"},
                   "solo_cabins": {"available": V(), "source": V(), "verified": "PENDING"},
                   "accessible_cabins_per_ship": V(),
                   "suite_program": {"name": V(), "tiers": ["VERIFY"], "source": V(), "verified": "PENDING"},
                   "decks_to_consider": template["cabins"]["decks_to_consider"]}
    n["family"] = {"kids_club_name": L["kids"], "age_bands": V(), "minimum_sailing_age": V(),
                   "nursery": {"available": V(), "extra_cost": V(), "age_range": V(), "source": V(), "verified": "PENDING"},
                   "teen_program": V(), "babysitting": V(), "source": V(), "verified": "PENDING"}
    n["accessibility"] = {"accessible_cabin_categories": V(), "wheelchair_scooter_policy": V(),
                          "tender_port_note": template["accessibility"]["tender_port_note"],
                          "service_animal_policy": V(), "medical_equipment": V(),
                          "source": V(), "verified": "PENDING"}
    n["itineraries"] = {"home_ports": ["VERIFY"], "typical_lengths": ["VERIFY"],
                        "regions": [{"region": r, "months": V(), "note": ""} for r in
                                    sorted({x for c in L["classes"] for x in c["typical_regions"]})],
                        "private_destination": {"name": "", "location": "", "note": V()},
                        "source": V(), "verified": "PENDING"}
    n["policies"] = {k: V() for k in ["deposit_timing", "final_payment_days_before", "cancellation_schedule", "dress_code"]}
    n["policies"].update({"onboard_currency": "US dollar",
                          "documentation": template["policies"]["documentation"],
                          "source": V(), "verified": "PENDING"})
    n["editorial"] = {"_note": "Original prose. Safe to edit freely.",
                      "who_its_for": L["for"], "who_its_not_for": L["not"],
                      "cost_drivers": [{"factor": a, "detail": b} for a, b in L["cost"]]}
    n["faqs"] = [{"q": q, "a": a} for q, a in L["faqs"]]
    n["sources_master"] = [{"label": L["legal"] + " official site", "url": "VERIFY", "used_for": "Ship specs, inclusions, policies"}]
    n["last_built"] = None
    out.append(n)

data["lines"] = out
json.dump(data, open(PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("lines now:", len(data["lines"]))
for l in data["lines"]:
    print("  -", l["slug"])
