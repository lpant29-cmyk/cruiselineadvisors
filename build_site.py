#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the full connected site + a single-file navigable preview."""
import json, os, re, datetime, html
from build_deep import CSS, build_page, esc, PHONE_DISPLAY, PHONE_HREF, nav_html
from home_rich import HOME_CSS, HOME_JS, rich_hero, chaos_section, quiz_section

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
TODAY = datetime.date.today()
data = json.load(open(os.path.join(ROOT, "data", "cruise-lines.json"), encoding="utf-8"))
LINES = data["lines"]

DESTS = [
 ("caribbean","Caribbean","🏝️","December – April","The most-sailed region in cruising, and the easiest to reach from US home ports.",
  [("Eastern","St. Thomas, St. Maarten, San Juan","Beaches, shopping, fewer sea days"),
   ("Western","Cozumel, Grand Cayman, Roatán","Reefs, ruins, diving and cave tubing"),
   ("Southern","Aruba, Curaçao, Barbados","Drier, longer sailings, fewer crowds")],
  "Hurricane season officially runs 1 June – 30 November, most active mid-August to mid-October.",
  ["Miami","Fort Lauderdale","Port Canaveral","Tampa","Galveston","New Orleans","San Juan"]),
 ("alaska","Alaska","🏔️","June – August","A short, sharply defined season with glaciers, whales and very long daylight.",
  [("Inside Passage","Round-trip Seattle or Vancouver","Sheltered water, no repositioning flights"),
   ("Gulf of Alaska","One-way Vancouver ↔ Seward/Whittier","Pairs with a Denali land tour"),
   ("Cruisetour","Sailing plus inland rail and coach","Reaches the interior national park")],
  "Season runs roughly late April to late September only. May and September are cheaper and quieter but cooler and wetter.",
  ["Seattle","Vancouver","Seward","Whittier"]),
 ("mediterranean","Mediterranean","🏛️","May–June, September–October","Port-intensive and history-dense — often a new city every morning.",
  [("Western","Barcelona, Rome, Florence, Riviera","Art, food, Roman history"),
   ("Eastern","Greece, Croatia, Turkey","Islands, ruins, sailing between them"),
   ("Adriatic","Venice, Split, Dubrovnik","Walled cities and short hops")],
  "Shoulder seasons are the sweet spot. July and August bring peak heat, peak crowds and peak pricing.",
  ["Barcelona","Civitavecchia (Rome)","Venice","Athens (Piraeus)"]),
 ("bahamas","Bahamas & Short Getaways","⛵","Year-round","The lowest-commitment way to try cruising — 2 to 5 nights from Florida.",
  [("Nassau","Capital, beaches, forts","Walkable from the terminal"),
   ("Freeport","Quieter, beach-focused","Often paired with Nassau"),
   ("Private islands","Line-owned beach destinations","Included on most short sailings")],
  "Operates year-round; winter is driest. Short itineraries can often be re-routed around weather more easily than long ones.",
  ["Miami","Fort Lauderdale","Port Canaveral","Palm Beach","Jacksonville"]),
 ("panama-canal","Panama Canal","🛳️","October – April","An engineering-marvel itinerary rather than a beach one.",
  [("Full transit","Ocean to ocean","Typically 14+ nights"),
   ("Partial transit","Enters Gatun Lake and returns","10–11 nights, sees the locks"),
   ("Repositioning","Seasonal fleet movement","Often the best per-night value")],
  "Aligned with the dry season, October through April. A forward-facing balcony pays off on transit day.",
  ["Fort Lauderdale","Miami","Los Angeles","San Diego"]),
 ("northern-europe","Northern Europe & Baltic","🌌","June – August","Norwegian fjords and Baltic capitals in a very tight season.",
  [("Norwegian fjords","Deep-water scenery, midnight sun","Best in high summer"),
   ("Baltic capitals","Copenhagen, Stockholm, Tallinn, Helsinki","City-focused, port-heavy"),
   ("Iceland & Arctic","Dramatic landscapes","Shortest season of all")],
  "Most ships reposition out by early September. Near-24-hour daylight above the Arctic Circle in June.",
  ["Southampton","Copenhagen","Amsterdam","Reykjavik"]),
]

GUIDES = [
 ("first-time-cruisers","Your first cruise, explained","🧭",
  "Everything nobody tells you before your first sailing — boarding, sea days, dining, and what to actually pack.",
  [("Booking to boarding","Deposit, final payment, documents, online check-in and terminal arrival windows. Arriving at your assigned time genuinely matters at busy ports."),
   ("Your first day","Cabins aren't always ready at boarding. The buffet is open, the muster drill is mandatory, and your luggage may arrive hours after you do."),
   ("Sea days vs port days","Sea days are for the ship; port days are for the destination. A good itinerary balances both — too many ports back-to-back is exhausting."),
   ("Dining formats","Fixed seating, flexible dining, or a mix. Choose deliberately: fixed gives you the same table and waiter, flexible gives you freedom."),
   ("What to pack","Layers regardless of destination, a small day bag for port, any medication in hand luggage, and formal wear only if your line expects it.")]),
 ("choosing-a-cabin","Choosing a cabin without regret","🛏️",
  "Deck, position and category all change the experience — often more than the ship itself does.",
  [("The four categories","Interior, ocean view, balcony, suite. Interior is cheapest and surprisingly restful. Balcony is the upgrade most people say they'd repeat."),
   ("Position matters more than category","Mid-ship and lower decks feel steadiest in rough water. Cabins under the pool deck, buffet, theatre or nightclub can be genuinely noisy."),
   ("Obstructed views","Some balconies and windows are partially blocked by lifeboats or structure. They're cheaper for a reason — check the deck plan."),
   ("Connecting and family cabins","Limited in number and booked far ahead. If you need them, book earlier than you think."),
   ("Accessible cabins","Very limited, and they sell out long before general inventory. This is the strongest reason to book by phone rather than online.")]),
 ("whats-included","What's actually included","💳",
  "The gap between the fare and the final bill is where cruise budgets go wrong.",
  [("Usually included","Your cabin, main dining room, buffet, several casual venues, entertainment, pools and most facilities."),
   ("Usually extra","Gratuities, alcohol and speciality coffee, speciality restaurants, wi-fi, shore excursions, spa, casino and laundry."),
   ("Gratuities","Most lines add a daily service charge per guest automatically. It's a published fee, not a fare — check the current rate before you sail."),
   ("Drinks packages","Worth it only above a certain daily consumption, and usually must be bought for all adults in a cabin. Do the maths honestly."),
   ("The real comparison","Compare the all-in total between lines, not the headline fare. A higher fare that includes drinks and wi-fi can be the cheaper trip.")]),
 ("groups-and-families","Groups, families and celebrations","🎊",
  "Multiple cabins, multiple households and one itinerary — this is where phone booking earns its keep.",
  [("Kids club age bands","Bands decide whether siblings are together or split. Check them before choosing a ship — it's the most common family surprise."),
   ("Connecting cabins","Limited and early-booking. Adjacent isn't the same as connecting; be specific about which you need."),
   ("Linked dining","Groups can usually be seated together, but it must be arranged in advance rather than at the restaurant door."),
   ("Split payments","Several households paying separately for one booking is normal but not something booking websites handle well."),
   ("Group amenities","Blocks of cabins can unlock group handling and coordinated excursions. Worth asking about before booking individually.")]),
 ("accessibility","Accessible cruising","♿",
  "Cruising can be one of the most accessible ways to travel — with the right cabin and the right itinerary.",
  [("Accessible cabins","Limited per ship and sold well ahead of general inventory. Categories and features vary between lines."),
   ("Tender ports","Some ports require a small boat transfer from ship to shore, which can be difficult or impossible with a wheelchair or scooter. Check which ports tender."),
   ("Mobility equipment","Policies differ on scooters, oxygen, dialysis and refrigerated medication. Confirm before booking, not after."),
   ("Service animals","Accepted by most lines with documentation, but destination entry requirements vary by country."),
   ("Why phone matters here","None of this availability is visible on a booking website. A specialist can check it directly with the line.")]),
 ("when-to-cruise","Timing your cruise","📅",
  "Picking the right month usually matters more than picking the right ship.",
  [("Regions run on seasons","Alaska sails roughly May to September. Northern Europe closes by early autumn. The Caribbean runs year-round but varies enormously by month."),
   ("Hurricane season","Officially 1 June to 30 November in the Atlantic, most active mid-August to mid-October. Itineraries can be re-routed."),
   ("Shoulder seasons","May–June and September–October in Europe deliver comfortable weather without peak crowds."),
   ("School holidays","The busiest and most expensive weeks of the year on family-focused lines. Flexibility here changes everything."),
   ("Repositioning voyages","Spring and autumn fleet movements often deliver the lowest cost per night of any cruise product.")]),
]

LEGAL = [
 ("terms","Terms of Use", [
  ("What this website is","CruiseLine Advisors is a marketing and referral service operated by [Your Company] LLC. We are not a cruise line, travel agency, tour operator or seller of travel. We do not sell, book, reserve, ticket or take payment for travel, and we do not set prices or hold inventory."),
  ("How referrals work","When you call us or submit a request, we may connect you with one of several independent, licensed third-party travel agencies. We may receive a marketing or referral fee for that connection. All quotes, bookings, payments, changes, cancellations and customer service are provided by that independent agency under its own terms and conditions."),
  ("No pricing on this site","This website does not advertise, display or guarantee any fare, rate, discount or saving. Any pricing you receive is quoted directly by an independent partner agency based on live availability at that time and is subject to change."),
  ("Editorial content","Destination guides, cruise line information and seasonal timing are general planning information compiled independently from published sources. They are not offers, recommendations or guarantees. Fleets, facilities, policies and entry requirements change frequently — always confirm details with the agency booking your trip and with official sources."),
  ("Trademarks","All cruise line names, ship names, logos and trademarks referenced on this site are the property of their respective owners and are used only descriptively to identify cruise lines our independent partner agencies are able to book. We are not affiliated with, sponsored by, endorsed by, authorised by, or an agent of any cruise line. This is not an official site of any cruise line."),
  ("Limitation of liability","We are not responsible for the products, services, pricing or conduct of any partner agency or cruise line. Your contract for travel is with the agency that books it."),
 ]),
 ("privacy","Privacy Policy", [
  ("What we collect","When you call us or submit a call-back request we collect information you provide, such as your name, telephone number, travel dates, destination interest and party size. We also collect standard technical data such as IP address, device type and pages visited."),
  ("Why we collect it","To connect you with an independent partner travel agency that can assist with your enquiry, and to measure and improve our advertising."),
  ("Sharing and sale of information","We share the information you provide with independent partner travel agencies so they can contact and assist you. Under certain state privacy laws, including California's, this constitutes a sale or share of personal information. You may opt out at any time using the Do Not Sell or Share My Personal Information link."),
  ("Your rights","Depending on your state you may have the right to know what personal information we hold, request deletion, request correction, and opt out of sale or sharing. Contact us using the details below to exercise these rights."),
  ("Retention","We retain enquiry records and consent records for as long as necessary to operate the service and to demonstrate compliance with telemarketing law."),
  ("Cookies and advertising","We use cookies and similar technologies for analytics and advertising measurement, including Google services. You can control cookies through your browser settings."),
 ]),
 ("consent","Calling & SMS Consent Terms", [
  ("What you are agreeing to","By providing your telephone number and checking the consent box, or by calling us, you agree that CruiseLine Advisors and its independent partner travel agencies may contact you at the number provided about your cruise enquiry."),
  ("Methods of contact","This may include contact by live agent, automatic telephone dialling system, prerecorded or artificial voice message, and SMS text message."),
  ("Consent is not a condition of purchase","You are never required to agree to be contacted in order to buy anything. Nothing on this site is conditioned on your consent."),
  ("Message frequency and rates","Message frequency varies based on your enquiry. Message and data rates may apply from your carrier."),
  ("How to opt out","Reply STOP to any text message to stop text messages. Ask any caller to place you on our internal do-not-call list. You may also contact us using the details below to revoke consent at any time, by any reasonable means."),
  ("Records","We retain a record of the consent language shown to you, the date and time you provided consent, and the page on which it was given."),
  ("Do-not-call","We scrub against the National Do Not Call Registry and maintain an internal do-not-call list. Requests to stop contact are honoured promptly."),
 ]),
 ("do-not-sell","Do Not Sell or Share My Personal Information", [
  ("Your right to opt out","Certain state privacy laws give you the right to opt out of the sale or sharing of your personal information. Because we share enquiry details with independent partner travel agencies so they can assist you, this activity may be treated as a sale or share under those laws."),
  ("How to opt out","Contact us using the details below with the subject line 'Do Not Sell or Share'. Include the phone number and name you provided so we can locate your record. We will process your request and confirm."),
  ("Authorised agents","You may designate an authorised agent to submit a request on your behalf. We may require verification of the agent's authority."),
  ("No discrimination","We will not deny you services, or provide a different level of service, because you exercised your privacy rights."),
  ("What opting out does not do","Opting out does not delete information already shared with a partner agency. To request deletion from that agency, contact them directly."),
 ]),
]

# ─────────────────────────── shared chrome ───────────────────────────

def shell(title, desc, body, depth=0, extra_css=""):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}{extra_css}</style>
</head>
<body style="--l1:#0a2740;--l2:#123c5a;--laccent:#D9B25A">
<div class="disc">
  <b>We're an independent referral service — not a cruise line and not a travel agency.</b>
  We connect you with licensed cruise specialists at independent partner agencies and may be paid a referral fee.
</div>
{nav_html(up)}
{body}
<footer class="ftr">
  <div class="wrap2">
    <p class="built">Last built {TODAY.isoformat()}</p>
    <p><b>What we are:</b> a marketing and referral service. We are not a cruise line, travel agency, tour operator or seller of travel. We do not sell, book, ticket or take payment for travel. Calls may be connected to one of several independent, licensed third-party travel agencies, and we may receive a referral fee. All quotes, bookings and customer service are provided by that agency under its own terms.</p>
    <p><b>Trademarks:</b> All cruise line names, ship names and marks are the property of their respective owners, used descriptively only. We are not affiliated with, sponsored by, endorsed by or an agent of any cruise line.</p>
    <p><b>Pricing:</b> This site displays no fares, rates, discounts or savings.</p>
    <p><a href="{up}legal/terms.html">Terms</a> · <a href="{up}legal/privacy.html">Privacy</a> · <a href="{up}legal/consent.html">Calling &amp; SMS Consent</a> · <a href="{up}legal/do-not-sell.html">Do Not Sell or Share</a></p>
    <p>© {TODAY.year} [Your Company] LLC. Florida.</p>
  </div>
</footer>
<div class="stickybar">
  <div><b>Talk to a cruise specialist</b><span>Free · no obligation · EN/ES</span></div>
  <a href="tel:{PHONE_HREF}" onclick="trackCall('sticky')">☎ Call</a>
</div>
<script>
function trackCall(p){{window.dataLayer=window.dataLayer||[];
window.dataLayer.push({{event:'call_click',placement:p}});
if(typeof gtag==='function'){{gtag('event','call_click',{{placement:p}});}}return true;}}
</script>
</body></html>"""

def hero(badge, h1, sub, meta=""):
    return f"""<section class="dhero"><div class="wrap2">
<span class="dbadge">{badge}</span>
<h1>{esc(h1)}</h1>
<p class="dsub">{esc(sub)}</p>
{f'<p class="dmeta">{esc(meta)}</p>' if meta else ''}
<a href="tel:{PHONE_HREF}" class="dcall" onclick="trackCall('hero')">☎ {PHONE_DISPLAY}<small>Free · no obligation</small></a>
</div></section>"""

def cta_block(title, sub):
    return f"""<div class="inlinecta"><div><b>{esc(title)}</b><span>{esc(sub)}</span></div>
<a href="tel:{PHONE_HREF}" class="ictabtn" onclick="trackCall('inline')">☎ {PHONE_DISPLAY}</a></div>"""

# ─────────────────────────── page builders ───────────────────────────

def p_home():
    cards = "".join(f"""<a class="tile linkcard" href="lines-deep/{L['slug']}.html">
<b class="t">{L['theme']['emoji']} {esc(L['name'])}</b><p>{esc(L['one_line'])}</p>
<span class="go2">Read the guide →</span></a>""" for L in LINES)
    dcards = "".join(f"""<a class="tile linkcard" href="destinations/{s}.html">
<b class="t">{e} {esc(n)}</b><p>{esc(d)}</p><span class="go2">Best: {esc(best)} →</span></a>"""
        for s,n,e,best,d,_,_,_ in DESTS)
    gcards = "".join(f"""<a class="tile linkcard" href="guides/{s}.html">
<b class="t">{e} {esc(t)}</b><p>{esc(d)}</p><span class="go2">Read →</span></a>"""
        for s,t,e,d,_ in GUIDES)

    body = rich_hero(PHONE_DISPLAY, PHONE_HREF)
    body += chaos_section(PHONE_DISPLAY, PHONE_HREF)
    body += f"""<main class="wrap2 main2">
<section class="blk"><h2>Cruise line guides</h2>
<p class="intro">Each line has a distinct personality. These guides cover ships class by class, what the fare actually includes, how to choose a cabin, and who each line genuinely suits — including who it doesn't.</p>
<div class="grid3b">{cards}</div></section></main>"""
    body += quiz_section(PHONE_DISPLAY, PHONE_HREF)
    body += f"""<main class="wrap2 main2">
<section class="blk"><h2>Destinations</h2>
<p class="intro">Regions run on seasons. Picking the right month usually matters more than picking the right ship.</p>
<div class="grid3b">{dcards}</div></section>
<section class="blk"><h2>Planning guides</h2>
<p class="intro">The practical questions — cabins, budgets, families, accessibility and timing.</p>
<div class="grid3b">{gcards}</div>
{cta_block("Ten minutes on the phone beats ten tabs open.","Tell a licensed specialist what you want from the trip. They'll do the comparing.")}
</section></main>
<script>{HOME_JS}</script>"""
    return shell("CruiseLine Advisors — Talk to a Licensed Cruise Specialist",
                 "Independent cruise guides and phone-first planning.", body, extra_css=HOME_CSS)

def p_lines_hub():
    cards = "".join(f"""<a class="tile linkcard" href="lines-deep/{L['slug']}.html">
<b class="t">{L['theme']['emoji']} {esc(L['name'])}</b><p>{esc(L['one_line'])}</p>
<span class="go2">Founded {L['company'].get('founded','—')} · Read the guide →</span></a>""" for L in LINES)
    body = hero("Cruise line guides", "Every major line, honestly compared",
        "Ships, inclusions, cabins, family facilities and seasons — with sources and verification dates.",
        "We cover who each line suits and who it doesn't. More lines are being added.")
    body += f"""<main class="wrap2 main2"><section class="blk">
<h2>Currently covered</h2><div class="grid3b">{cards}</div>
{cta_block("Not sure which line fits?","That's the exact question a specialist answers best.")}</section></main>"""
    return shell("Cruise Line Guides | CruiseLine Advisors", "Independent guides to every major cruise line.", body)

def p_dest_hub():
    cards = "".join(f"""<a class="tile linkcard" href="destinations/{s}.html">
<b class="t">{e} {esc(n)}</b><p>{esc(d)}</p><span class="go2">Best: {esc(best)} →</span></a>"""
        for s,n,e,best,d,_,_,_ in DESTS)
    body = hero("Destinations", "Where to sail, and when", "Season by season, region by region.",
        "Timing changes weather, wildlife, crowds and cost more than any other decision you make.")
    body += f"""<main class="wrap2 main2"><section class="blk">
<div class="grid3b">{cards}</div>
{cta_block("Have dates but no destination?","Give a specialist your window and they'll match it to regions actually in season.")}</section></main>"""
    return shell("Cruise Destinations | CruiseLine Advisors", "Cruise destination guides with season timing.", body)

def p_dest(s, n, e, best, d, routes, season_note, ports):
    rows = "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>" for a,b,c in routes)
    portlist = "".join(f'<span class="ft">{esc(p)}</span>' for p in ports)
    body = hero(f"{e} Destination guide", n, d, f"Best time to sail: {best}")
    body += f"""<main class="wrap2 main2">
<section class="blk"><h2>Routes and what they're like</h2>
<div class="tblscroll2"><table class="dtable"><thead><tr><th>Route</th><th>Typical ports</th><th>Character</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section class="blk"><h2>When to go</h2><div class="callout"><b>Season</b>{esc(season_note)}</div>
<p class="intro">Season data is verified against national meteorological and park sources. Monthly climate detail is being added — see the sources block on each page for what has been checked and when.</p></section>
<section class="blk"><h2>Common home ports</h2><div class="feats">{portlist}</div>
{cta_block(f"Planning {n}?","A specialist can match your dates to the right route and ship.")}</section>
<section class="blk sources"><h2>Sources</h2>
<ul class="srclist">
<li><a href="https://www.nhc.noaa.gov/climo/" rel="nofollow noopener" target="_blank">NOAA National Hurricane Center</a><span>Hurricane season dates and climatology</span></li>
<li><span class="pending">Monthly climate normals — verification pending</span></li>
<li><span class="pending">Port dock vs tender status — verification pending</span></li>
</ul>
<p class="note">Facts are compiled independently from primary sources. Conditions vary year to year — confirm details that matter with the agency booking your trip.</p></section></main>"""
    return shell(f"{n} Cruises — Best Time to Sail, Routes & Ports", d, body, depth=1)

def p_guides_hub():
    cards = "".join(f"""<a class="tile linkcard" href="guides/{s}.html">
<b class="t">{e} {esc(t)}</b><p>{esc(d)}</p><span class="go2">Read →</span></a>"""
        for s,t,e,d,_ in GUIDES)
    body = hero("Planning guides", "The practical questions", "Cabins, budgets, families, accessibility and timing.")
    body += f"""<main class="wrap2 main2"><section class="blk"><div class="grid3b">{cards}</div>
{cta_block("Still deciding?","A ten-minute call usually settles what an hour of reading can't.")}</section></main>"""
    return shell("Cruise Planning Guides | CruiseLine Advisors", "Practical cruise planning guides.", body)

def p_guide(s, t, e, d, sections):
    body = hero(f"{e} Guide", t, d)
    secs = "".join(f'<section class="blk"><h2>{esc(a)}</h2><p class="intro">{esc(b)}</p></section>'
                   for a,b in sections)
    body += f"""<main class="wrap2 main2">{secs}
<section class="blk">{cta_block("Questions this guide didn't answer?","That's exactly what the phone call is for. Free, no obligation.")}</section></main>"""
    return shell(f"{t} | CruiseLine Advisors", d, body, depth=1)

def p_legal(s, t, sections):
    secs = "".join(f'<section class="blk"><h2>{esc(a)}</h2><p class="intro">{esc(b)}</p></section>'
                   for a,b in sections)
    body = hero("Legal", t, "Last updated " + TODAY.isoformat())
    body += f"""<main class="wrap2 main2">{secs}
<section class="blk"><h2>Contact</h2><p class="intro">[Your Company] LLC, [Street Address], Florida. Telephone {PHONE_DISPLAY}. Email [privacy@yourdomain.com].</p></section></main>"""
    return shell(f"{t} | CruiseLine Advisors", t, body, depth=1)

def p_compare():
    rows = "".join(f"""<tr><td>{L['theme']['emoji']} {esc(L['name'])}</td>
<td>{L['company'].get('founded','—')}</td>
<td>{esc(L.get('positioning','').replace('-',' ').title())}</td>
<td><span class="pending">pending</span></td>
<td><span class="pending">pending</span></td>
<td><a href="lines-deep/{L['slug']}.html">Guide →</a></td></tr>""" for L in LINES)
    body = hero("Comparison", "Compare cruise lines on verified facts",
        "Same measure, same source, same verification standard across every line.",
        "We never compare on price. We compare on facts that don't move.")
    body += f"""<main class="wrap2 main2">
<section class="blk"><h2>Line comparison</h2>
<p class="intro">This table is generated from the fact store. Fields show as pending until verified against a primary source — we'd rather show a gap than a guess.</p>
<div class="tblscroll2"><table class="dtable"><thead><tr>
<th>Line</th><th>Founded</th><th>Style</th><th>Fleet</th><th>Daily gratuity</th><th></th>
</tr></thead><tbody>{rows}</tbody></table></div>
<div class="callout"><b>Why no prices</b>Fares change daily and vary by sailing, cabin and occupancy. Any number here would be wrong by the time you read it. We compare on stable facts instead — and a specialist quotes live pricing for your dates.</div>
{cta_block("Want these compared for your trip?","A specialist compares live availability across lines in minutes.")}</section>
<section class="blk"><h2>What we compare on</h2>
<ul class="check">
<li>Founding year, fleet size and parent company</li>
<li>Published daily gratuity — a fee, not a fare</li>
<li>Kids club age bands and minimum sailing age</li>
<li>Accessible cabin counts and categories</li>
<li>Solo cabin availability</li>
<li>Private destination and which itineraries include it</li>
<li>What the fare includes and what costs extra</li>
</ul>
<p class="note">Full interactive ship-by-ship comparison is in development. It will build from the same verified fact store as these pages, so a fact corrected once is corrected everywhere.</p></section></main>"""
    return shell("Compare Cruise Lines | CruiseLine Advisors", "Compare cruise lines on verified facts.", body)

def p_updates():
    body = hero("Updates", "Cruise policy & industry updates",
        "Changes to cruise line policies, documentation rules and regulations that affect passengers.",
        "Every entry is dated and sourced. We publish what changed, when, and what it means for you.")
    body += f"""<main class="wrap2 main2">
<section class="blk"><h2>How this page works</h2>
<p class="intro">Cruise line policies change frequently — gratuity rates, drinks package terms, documentation requirements, health rules and cancellation schedules. When something changes that affects passengers, it's logged here with the date it changed and a link to the primary source.</p>
<div class="callout"><b>Verification standard</b>Every entry links to a primary source: the cruise line's own announcement, a government agency, or a port authority. We don't publish rumour or repost other sites' reporting.</div>
</section>
<section class="blk"><h2>Recent updates</h2>
<div class="callout"><b>No entries yet</b>This log begins when the fact store goes live. Each entry will show the date, the line or authority affected, what changed, and what it means in practice.</div>
<p class="intro">Planned categories: gratuity and service charge changes · drinks and wi-fi package terms · documentation and entry requirements · itinerary and deployment changes · accessibility policy changes · cancellation and refund policy changes.</p>
{cta_block("Policy question about your sailing?","A specialist can confirm what applies to your specific booking.")}</section>
<section class="blk sources"><h2>Sources we monitor</h2>
<ul class="srclist">
<li><a href="https://www.nhc.noaa.gov/" rel="nofollow noopener" target="_blank">NOAA National Hurricane Center</a><span>Season dates and storm advisories</span></li>
<li><a href="https://travel.state.gov/" rel="nofollow noopener" target="_blank">US Department of State</a><span>Passport and entry requirements</span></li>
<li><a href="https://www.cbp.gov/" rel="nofollow noopener" target="_blank">US Customs and Border Protection</a><span>Documentation for closed-loop sailings</span></li>
<li><a href="https://www.nps.gov/glba/" rel="nofollow noopener" target="_blank">NPS Glacier Bay</a><span>Alaska park access</span></li>
<li><span class="pending">Individual cruise line newsroom feeds — to be added</span></li>
</ul></section></main>"""
    return shell("Cruise Policy Updates | CruiseLine Advisors", "Dated, sourced log of cruise policy and regulation changes.", body)

EXTRA_CSS = """
.linkcard{text-decoration:none;display:block;transition:.2s}
.linkcard:hover{transform:translateY(-4px);box-shadow:0 14px 30px rgba(8,36,59,.14);border-color:var(--brass)}
.go2{display:block;margin-top:.6rem;font-size:.75rem;font-weight:800;color:var(--brassd)}
.ftr a{color:#B9CFDA}
"""

def main():
    os.makedirs(SITE, exist_ok=True)
    for d in ("lines-deep","destinations","guides","legal"):
        os.makedirs(os.path.join(SITE, d), exist_ok=True)

    def w(path, content):
        with open(os.path.join(SITE, path), "w", encoding="utf-8") as f:
            f.write(content.replace("<style>"+CSS, "<style>"+CSS+EXTRA_CSS))

    w("index.html", p_home())
    w("cruise-lines.html", p_lines_hub())
    w("destinations.html", p_dest_hub())
    w("guides.html", p_guides_hub())
    w("compare.html", p_compare())
    w("updates.html", p_updates())

    for L in LINES:
        w(f"lines-deep/{L['slug']}.html", build_page(L, CSS + EXTRA_CSS))
    for d in DESTS:
        w(f"destinations/{d[0]}.html", p_dest(*d))
    for g in GUIDES:
        w(f"guides/{g[0]}.html", p_guide(*g))
    for s,t,sec in LEGAL:
        w(f"legal/{s}.html", p_legal(s,t,sec))

    n = sum(len(files) for _,_,files in os.walk(SITE))
    print(f"built {n} pages into site/")

if __name__ == "__main__":
    main()
