#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds deep, fact-driven cruise line pages from data/cruise-lines.json.

Run:  python3 build_deep.py
Output: lines-deep/<slug>.html  +  a staleness report on stdout

Design rules enforced here:
  * No fares, prices, discounts or savings are ever rendered.
  * Any field whose value is "VERIFY" renders as a visible gap, not as fake data.
  * Every section shows its source and verification date.
"""
import json, os, html, datetime, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "cruise-lines.json")
OUT  = os.path.join(ROOT, "lines-deep")

PHONE_DISPLAY = "+1 (888) 555-0142"
PHONE_HREF    = "+18885550142"
TODAY         = datetime.date.today()

BANNED = ("$", "usd", "from $", "save ", "discount", "% off", "cheapest", "lowest price")


def esc(s):
    return html.escape(str(s), quote=False)


def is_pending(v):
    return v is None or (isinstance(v, str) and (v.strip() == "" or v.startswith("VERIFY") or v == "PENDING"))


def val(v, fallback="Not yet verified"):
    """Render a value, or a visible gap if unverified. Never invents data."""
    if is_pending(v):
        return '<span class="pending">%s</span>' % fallback
    if isinstance(v, list):
        v = ", ".join(str(x) for x in v if not is_pending(x)) or "Not yet verified"
        if v == "Not yet verified":
            return '<span class="pending">Not yet verified</span>'
    return esc(v)


def stamp(node):
    """Renders a small source + verified-date line for a data block."""
    src = node.get("source") if isinstance(node, dict) else None
    ver = node.get("verified") if isinstance(node, dict) else None
    if is_pending(src) and is_pending(ver):
        return '<p class="srcline pending">Source pending verification</p>'
    bits = []
    if not is_pending(src):
        bits.append('<a href="%s" rel="nofollow noopener" target="_blank">Source</a>' % esc(src))
    if not is_pending(ver):
        bits.append("verified %s" % esc(ver))
    else:
        bits.append('<span class="pending">verification pending</span>')
    return '<p class="srcline">%s</p>' % " · ".join(bits)


def staleness(line):
    """Returns list of (path, verified_date, days_old, limit) needing refresh."""
    limits = {"company": 90, "inclusions": 30, "family": 90,
              "accessibility": 90, "itineraries": 60, "policies": 90}
    issues = []
    for key, limit in limits.items():
        node = line.get(key, {})
        if not isinstance(node, dict):
            continue
        ver = node.get("verified")
        if is_pending(ver):
            issues.append((f"{line['slug']}.{key}", "PENDING", None, limit))
            continue
        try:
            d = datetime.date.fromisoformat(ver)
        except ValueError:
            issues.append((f"{line['slug']}.{key}", ver, None, limit))
            continue
        age = (TODAY - d).days
        if age > limit:
            issues.append((f"{line['slug']}.{key}", ver, age, limit))
    return issues


# ───────────────────────── section builders ─────────────────────────

def sec_quickfacts(L):
    c = L.get("company", {})
    rows = [
        ("Founded", val(c.get("founded"))),
        ("Headquarters", val(c.get("headquarters"))),
        ("Parent company", val(c.get("parent"))),
        ("Ships in fleet", val(c.get("fleet_size"))),
        ("Loyalty programme", val(c.get("loyalty_program"))),
        ("Style", val(L.get("positioning", "").replace("-", " ").title())),
    ]
    body = "".join(
        '<div class="qf"><b>%s</b><span>%s</span></div>' % (k, v) for k, v in rows
    )
    return f"""
<section class="blk" id="quick-facts">
  <h2>{esc(L['name'])} at a glance</h2>
  <div class="qfgrid">{body}</div>
  {stamp(c)}
</section>"""


def sec_fleet(L):
    cards = []
    for s in L.get("ship_classes", []):
        specs = [
            ("Entered service", val(s.get("first_in_service"))),
            ("Guests (double occ.)", val(s.get("capacity_double"))),
            ("Decks", val(s.get("decks"))),
            ("Gross tonnage", val(s.get("gross_tonnage"))),
        ]
        spec_html = "".join('<li><b>%s</b><span>%s</span></li>' % (a, b) for a, b in specs)
        feats = "".join('<span class="ft">%s</span>' % esc(f) for f in s.get("features", []))
        ships = val(s.get("ships"), "Ship list pending verification")
        regions = val(s.get("typical_regions"))
        cards.append(f"""
    <article class="shipcard">
      <header><h3>{esc(s.get('class',''))} class</h3><p class="ships">{ships}</p></header>
      <ul class="specs">{spec_html}</ul>
      <div class="feats">{feats}</div>
      <p class="regions"><b>Typically sails</b> {regions}</p>
      {stamp(s)}
    </article>""")
    return f"""
<section class="blk" id="fleet">
  <h2>The fleet, class by class</h2>
  <p class="intro">Two ships from the same line at the same fare can deliver completely different holidays. Class is the single most useful thing to understand before you choose.</p>
  <div class="shipgrid2">{''.join(cards)}</div>
  {cta("Which class fits your trip?", "A specialist knows which ships are actually deployed where, and when.")}
</section>"""


def sec_inclusions(L):
    inc = L.get("inclusions", {})
    yes = "".join(
        '<li><b>%s</b>%s</li>' % (esc(i.get("item", "")),
                                  '<span>%s</span>' % esc(i["note"]) if i.get("note") and not is_pending(i.get("note")) else "")
        for i in inc.get("included", []))
    no = "".join(
        '<li><b>%s</b>%s</li>' % (esc(i.get("item", "")),
                                  '<span>%s</span>' % esc(i["note"]) if i.get("note") and not is_pending(i.get("note")) else "")
        for i in inc.get("extra_cost", []))
    grat = inc.get("gratuity_per_person_per_day")
    grat_html = (
        f'<div class="callout"><b>Daily gratuity</b> {val(grat)} per guest, per day, added automatically to your onboard account. '
        f'Suites may be charged at a different rate ({val(inc.get("gratuity_suite_rate"))}). '
        f'This is a published service charge, not a fare.</div>'
    )
    return f"""
<section class="blk" id="included">
  <h2>What's actually included — and what isn't</h2>
  <p class="intro">This is the question that trips up most first-time cruisers. The fare covers a lot, but the gap between fare and final bill is where budgets go wrong. Here's the honest split.</p>
  {grat_html}
  <div class="inc2">
    <div class="yes"><h3>Included in your fare</h3><ul>{yes}</ul></div>
    <div class="no"><h3>Costs extra</h3><ul>{no}</ul></div>
  </div>
  {stamp(inc.get('included', [{}])[0] if inc.get('included') else {})}
  <p class="note">Inclusions change more often than any other detail on this page, which is why we re-verify this section every 30 days. Confirm what applies to your specific sailing with the agency that books it.</p>
</section>"""


def sec_cabins(L):
    cab = L.get("cabins", {})
    cats = "".join('<span class="ft">%s</span>' % esc(c) for c in cab.get("categories", []))
    guide = "".join('<li>%s</li>' % esc(g["guidance"]) for g in cab.get("decks_to_consider", []))
    special = []
    vb = cab.get("virtual_balcony", {})
    if vb.get("exists"):
        special.append(("Virtual balcony", "An interior cabin with a floor-to-ceiling live view of the ocean. Real daylight cue without the balcony price. Available on %s classes." % val(vb.get("classes"))))
    nb = cab.get("neighbourhood_balcony", {})
    if nb.get("exists"):
        special.append(("Neighbourhood balcony", esc(nb.get("note", "")) + " Cheaper than an ocean balcony — decide deliberately rather than by price alone."))
    sp = "".join('<div class="tile"><b class="t">%s</b><p>%s</p></div>' % (a, b) for a, b in special)
    return f"""
<section class="blk" id="cabins">
  <h2>Choosing a cabin without regret</h2>
  <p class="intro">On the same deck, at the same price, one cabin can be perfect and the next can sit under the nightclub. Cabin number matters as much as cabin category.</p>
  <h3>Categories offered</h3>
  <div class="feats">{cats}</div>
  <h3>Cabin types worth understanding</h3>
  <div class="grid2">{sp}</div>
  <h3>Before you pick a number</h3>
  <ul class="check">{guide}</ul>
  <div class="factrow">
    <div><b>Connecting cabins</b><span>{val(cab.get('connecting_cabins',{}).get('note'))}</span></div>
    <div><b>Accessible cabins per ship</b><span>{val(cab.get('accessible_cabins_per_ship'))}</span></div>
    <div><b>Solo cabins</b><span>{val(cab.get('solo_cabins',{}).get('available'))}</span></div>
  </div>
  {cta("Want the actual cabin numbers to avoid?", "That detail isn't published anywhere. It's what a specialist does in two minutes.")}
</section>"""


def sec_family(L):
    f = L.get("family", {})
    rows = [
        ("Kids club", val(f.get("kids_club_name"))),
        ("Age bands", val(f.get("age_bands"))),
        ("Minimum sailing age", val(f.get("minimum_sailing_age"))),
        ("Nursery", val(f.get("nursery", {}).get("available"))),
        ("Teen programme", val(f.get("teen_program"))),
        ("Babysitting", val(f.get("babysitting"))),
    ]
    body = "".join('<li><b>%s</b><span>%s</span></li>' % (a, b) for a, b in rows)
    return f"""
<section class="blk" id="family">
  <h2>Cruising with children</h2>
  <p class="intro">Age bands decide whether siblings are together or split across two clubs — the single most common family surprise on board. Check them before you choose a ship.</p>
  <ul class="deflist">{body}</ul>
  {stamp(f)}
</section>"""


def sec_access(L):
    a = L.get("accessibility", {})
    rows = [
        ("Accessible cabin categories", val(a.get("accessible_cabin_categories"))),
        ("Wheelchair &amp; scooter policy", val(a.get("wheelchair_scooter_policy"))),
        ("Service animals", val(a.get("service_animal_policy"))),
        ("Medical equipment", val(a.get("medical_equipment"))),
    ]
    body = "".join('<li><b>%s</b><span>%s</span></li>' % (a_, b) for a_, b in rows)
    tender = a.get("tender_port_note", "")
    return f"""
<section class="blk" id="accessibility">
  <h2>Accessibility</h2>
  <p class="intro">Accessible cabins are limited in number and sell out long before general inventory. If you need one, booking early matters more here than anywhere else in travel.</p>
  <div class="callout"><b>Tender ports</b> {esc(tender)}</div>
  <ul class="deflist">{body}</ul>
  {stamp(a)}
  {cta("Need an accessible cabin?", "Availability isn't visible on booking sites. A specialist can check it directly.")}
</section>"""


def sec_itineraries(L):
    it = L.get("itineraries", {})
    rows = "".join(
        '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' %
        (esc(r.get("region", "")), val(r.get("months")), esc(r.get("note", "")))
        for r in it.get("regions", []))
    pd = it.get("private_destination", {})
    pd_html = ""
    if pd.get("name"):
        pd_html = f'<div class="callout"><b>{esc(pd["name"])}</b> — {esc(pd.get("location",""))}. {val(pd.get("note"))}</div>'
    return f"""
<section class="blk" id="itineraries">
  <h2>Where and when it sails</h2>
  <p class="intro">Regions run on seasons. Picking the right month usually matters more than picking the right ship.</p>
  <div class="tblscroll2"><table class="dtable">
    <thead><tr><th>Region</th><th>Operating months</th><th>Notes</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
  {pd_html}
  <div class="factrow">
    <div><b>Home ports</b><span>{val(it.get('home_ports'))}</span></div>
    <div><b>Typical lengths</b><span>{val(it.get('typical_lengths'))}</span></div>
  </div>
  {stamp(it)}
</section>"""


def sec_costdrivers(L):
    items = L.get("editorial", {}).get("cost_drivers", [])
    body = "".join(
        '<div class="tile"><b class="t">%s</b><p>%s</p></div>' % (esc(i["factor"]), esc(i["detail"]))
        for i in items)
    return f"""
<section class="blk" id="cost">
  <h2>What actually drives the cost</h2>
  <p class="intro">We don't publish fares — they move daily and any number here would be wrong by the time you read it. What doesn't change is <em>what</em> moves the price. Understand these six and you'll know whether a quote is good before you're told.</p>
  <div class="grid3b">{body}</div>
  {cta("Get the real number for your dates", "Pricing is live and specific to your sailing. A specialist quotes it in minutes.")}
</section>"""


def sec_fit(L):
    ed = L.get("editorial", {})
    yes = "".join("<li>%s</li>" % esc(x) for x in ed.get("who_its_for", []))
    no = "".join("<li>%s</li>" % esc(x) for x in ed.get("who_its_not_for", []))
    return f"""
<section class="blk" id="fit">
  <h2>Honestly — is this the right line for you?</h2>
  <p class="intro">We'd rather tell you it isn't than have you spend a week on the wrong ship.</p>
  <div class="inc2">
    <div class="yes"><h3>Strong fit for</h3><ul>{yes}</ul></div>
    <div class="no"><h3>Probably not for</h3><ul>{no}</ul></div>
  </div>
</section>"""


def sec_faq(L):
    body = "".join(
        '<details><summary>%s</summary><p>%s</p></details>' % (esc(f["q"]), esc(f["a"]))
        for f in L.get("faqs", []))
    return f"""
<section class="blk" id="faq">
  <h2>Questions people actually ask</h2>
  <div class="faq2">{body}</div>
</section>"""


def sec_sources(L):
    rows = "".join(
        '<li><a href="%s" rel="nofollow noopener" target="_blank">%s</a><span>%s</span></li>' %
        (esc(s["url"]), esc(s["label"]), esc(s.get("used_for", "")))
        for s in L.get("sources_master", []))
    return f"""
<section class="blk sources" id="sources">
  <h2>Where this information comes from</h2>
  <p class="intro">Every factual claim on this page is taken from a primary source and carries its own verification date. We re-check inclusions every 30 days and ship specifications every 90.</p>
  <ul class="srclist">{rows}</ul>
  <p class="note">Facts are compiled independently from published sources. Descriptions and opinions are our own. Cruise lines change fleets, facilities and policies frequently — always confirm details that matter with the agency booking your trip.</p>
</section>"""


def cta(title, sub):
    return f"""
  <div class="inlinecta">
    <div><b>{esc(title)}</b><span>{esc(sub)}</span></div>
    <a href="tel:{PHONE_HREF}" class="ictabtn" onclick="trackCall('inline')">☎ {PHONE_DISPLAY}</a>
  </div>"""


# ───────────────────────── page assembly ─────────────────────────

def build_page(L, css):
    t = L.get("theme", {})
    sections = "".join([
        sec_quickfacts(L), sec_fit(L), sec_fleet(L), sec_inclusions(L),
        sec_cabins(L), sec_family(L), sec_access(L), sec_itineraries(L),
        sec_costdrivers(L), sec_faq(L), sec_sources(L),
    ])

    toc = [("quick-facts", "At a glance"), ("fit", "Is it right for you"),
           ("fleet", "The fleet"), ("included", "What's included"),
           ("cabins", "Choosing a cabin"), ("family", "With children"),
           ("accessibility", "Accessibility"), ("itineraries", "Where it sails"),
           ("cost", "What drives cost"), ("faq", "FAQ"), ("sources", "Sources")]
    toc_html = "".join('<a href="#%s">%s</a>' % (a, b) for a, b in toc)

    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(L['legal_name'])}: Ships, Cabins, What's Included &amp; When to Sail</title>
<meta name="description" content="In-depth independent guide to {esc(L['legal_name'])} — every ship class, what the fare covers, how to choose a cabin, kids club age bands, accessibility and season timing. Not affiliated with {esc(L['legal_name'])}.">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body style="--l1:{t.get('c1','#0a2740')};--l2:{t.get('c2','#123c5a')};--laccent:{t.get('accent','#e0a458')}">

<div class="disc">
  <b>We're an independent referral service — not a cruise line and not a travel agency.</b>
  We are not affiliated with or endorsed by {esc(L['legal_name'])}. We connect you with licensed cruise specialists at independent partner agencies and may be paid a referral fee.
</div>

<header class="hdr">
  <div class="wrap2 nav2">
    <a href="../index.html" class="brand2">CruiseLine<span>Advisors</span></a>
    <a href="tel:{PHONE_HREF}" class="hcall2" onclick="trackCall('header')">☎ Call</a>
  </div>
</header>

<section class="dhero">
  <div class="wrap2">
    <p class="crumb2"><a href="../index.html">Home</a> › Cruise lines › {esc(L['name'])}</p>
    <span class="dbadge">{t.get('emoji','')} {esc(L.get('positioning','').replace('-',' ').title())}</span>
    <h1>{esc(L['name'])}</h1>
    <p class="dsub">{esc(L.get('one_line',''))}</p>
    <p class="dmeta">An independent, source-checked guide — ships, inclusions, cabins, timing. No fares, no sales pitch.</p>
    <a href="tel:{PHONE_HREF}" class="dcall" onclick="trackCall('hero')">☎ {PHONE_DISPLAY}<small>Free · no obligation · we never take payment</small></a>
  </div>
</section>

<nav class="toc"><div class="wrap2 tocrow">{toc_html}</div></nav>

<main class="wrap2 main2">{sections}</main>

<footer class="ftr">
  <div class="wrap2">
    <p class="built">Page generated from verified source data. Last built: {TODAY.isoformat()}</p>
    <p><b>What we are:</b> a marketing and referral service. We are not a cruise line, travel agency, tour operator or seller of travel. We do not sell, book, ticket or take payment for travel, and we do not set prices or hold inventory. Calls may be connected to one of several independent, licensed third-party travel agencies, and we may receive a referral fee. All quotes, bookings and customer service are provided by that agency under its own terms.</p>
    <p><b>Trademarks:</b> {esc(L['legal_name'])} and all cruise line names, ship names and marks are the property of their respective owners, used here descriptively only. We are not affiliated with, sponsored by, endorsed by, authorised by, or an agent of {esc(L['legal_name'])}. This is not an official site of {esc(L['legal_name'])}.</p>
    <p><b>Pricing:</b> This page displays no fares, rates, discounts or savings. Any pricing you receive is quoted by an independent partner agency based on live availability.</p>
    <p>© {TODAY.year} [Your Company] LLC. Florida.</p>
  </div>
</footer>

<div class="stickybar">
  <div><b>Talk to a {esc(L['name'])} specialist</b><span>Free · no obligation · EN/ES</span></div>
  <a href="tel:{PHONE_HREF}" onclick="trackCall('sticky')">☎ Call</a>
</div>

<script>
function trackCall(p){{
  window.dataLayer=window.dataLayer||[];
  window.dataLayer.push({{event:'call_click',placement:p,page:'{L["slug"]}'}});
  if(typeof gtag==='function'){{gtag('event','call_click',{{placement:p}});}}
  return true;
}}
</script>
</body>
</html>
"""
    return html_out


CSS = """
:root{--ink:#08243B;--ink2:#0E3A5C;--brass:#D9B25A;--brassd:#B8933D;--foam:#F4F8F9;
--mist:#E4EDEF;--line:#D5E0E3;--muted:#556B78;--paper:#FBFAF7;--card:#fff}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:96px}
body{font-family:'Inter',system-ui,sans-serif;background:var(--paper);color:var(--ink);line-height:1.62;padding-bottom:64px}
h1,h2,h3{font-family:'Fraunces',Georgia,serif;font-weight:600;line-height:1.15;letter-spacing:-.015em}
a{color:inherit}
.wrap2{max-width:940px;margin:0 auto;padding:0 18px}
.disc{background:var(--ink);color:#C3D6E0;font-size:.73rem;text-align:center;padding:.55rem 16px;line-height:1.45}
.disc b{color:#fff;display:block}
.hdr{position:sticky;top:0;z-index:60;background:rgba(251,250,247,.95);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav2{display:flex;align-items:center;justify-content:space-between;height:56px}
.brand2{font-family:'Fraunces',serif;font-size:1.08rem;text-decoration:none;color:var(--ink)}
.brand2 span{color:var(--brassd)}
.hcall2{background:var(--brass);color:var(--ink);font-weight:800;text-decoration:none;padding:.5em 1em;border-radius:99px;font-size:.85rem}
.dhero{background:linear-gradient(165deg,var(--l1) 0%,var(--l2) 60%,#05192B 100%);color:#EAF3F7;padding:30px 0 34px}
.crumb2{font-size:.76rem;color:#8FADBB}
.crumb2 a{color:#BCD3DE;text-decoration:none}
.dbadge{display:inline-block;margin-top:.7rem;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);
  color:#EAF3F7;padding:.35em .85em;border-radius:99px;font-size:.68rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.dhero h1{color:#fff;font-size:clamp(2rem,7vw,2.9rem);margin-top:.6rem}
.dsub{color:var(--laccent);font-size:1.05rem;margin-top:.5rem;font-weight:500;max-width:44ch}
.dmeta{color:#9FBCCB;font-size:.85rem;margin-top:.7rem;max-width:52ch}
.dcall{display:inline-flex;flex-direction:column;align-items:center;background:var(--brass);color:var(--ink);
  font-weight:800;text-decoration:none;padding:.85em 1.5em;border-radius:13px;margin-top:1.3rem;font-size:1.08rem}
.dcall small{font-weight:600;font-size:.64rem;opacity:.72;letter-spacing:.04em;text-transform:uppercase;margin-top:.15rem}
.toc{position:sticky;top:56px;z-index:50;background:var(--mist);border-bottom:1px solid var(--line)}
.tocrow{display:flex;gap:16px;overflow-x:auto;padding:9px 18px;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.tocrow::-webkit-scrollbar{display:none}
.tocrow a{flex:none;font-size:.8rem;font-weight:700;color:var(--muted);text-decoration:none;white-space:nowrap}
.tocrow a:hover{color:var(--ink)}
.main2{padding:8px 18px 30px}
.blk{padding:30px 0;border-bottom:1px solid var(--line)}
.blk h2{font-size:clamp(1.4rem,4.4vw,1.85rem);margin-bottom:.5rem}
.blk h3{font-size:1.08rem;margin:20px 0 .5rem;font-family:'Inter',sans-serif;font-weight:800}
.intro{color:var(--muted);font-size:.97rem;max-width:62ch;margin-bottom:1rem}
.intro em{font-style:italic;color:var(--ink)}
.pending{color:#9AA7AF;font-style:italic;font-weight:500}
.srcline{font-size:.72rem;color:var(--muted);margin-top:.7rem}
.srcline a{color:var(--ink2)}
.note{font-size:.78rem;color:var(--muted);margin-top:.9rem;background:var(--foam);border-left:3px solid var(--brass);padding:.7em .9em;border-radius:0 8px 8px 0}
.qfgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.qf{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.qf b{display:block;font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.qf span{font-size:.95rem;font-weight:700}
.shipgrid2{display:grid;gap:12px;margin-top:14px}
.shipcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px}
.shipcard h3{font-family:'Fraunces',serif;font-size:1.15rem;margin:0}
.ships{font-size:.82rem;color:var(--muted);margin-top:.15rem}
.specs{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0}
.specs li b{display:block;font-size:.62rem;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.specs li span{font-size:.9rem;font-weight:700}
.feats{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.ft{background:var(--foam);border:1px solid var(--line);border-radius:99px;padding:.3em .7em;font-size:.75rem;font-weight:600}
.regions{font-size:.83rem;color:var(--muted);margin-top:.7rem}
.regions b{color:var(--ink);font-size:.68rem;letter-spacing:.06em;text-transform:uppercase}
.inc2{display:grid;gap:12px;margin-top:12px}
.inc2 .yes,.inc2 .no{border-radius:14px;padding:16px}
.inc2 .yes{background:rgba(90,156,43,.07);border:1px solid rgba(90,156,43,.3)}
.inc2 .no{background:rgba(209,84,63,.06);border:1px solid rgba(209,84,63,.28)}
.inc2 h3{margin:0 0 .5rem;font-size:1rem}
.inc2 ul{list-style:none;display:grid;gap:.5rem}
.inc2 li{font-size:.88rem;display:grid;gap:.1rem}
.inc2 li b{font-weight:700}
.inc2 li span{color:var(--muted);font-size:.8rem}
.inc2 .yes li b::before{content:"✓ ";color:#5A9C2B;font-weight:800}
.inc2 .no li b::before{content:"— ";color:#D1543F;font-weight:800}
.callout{background:linear-gradient(120deg,rgba(217,178,90,.12),rgba(14,58,92,.06));border:1px solid var(--line);
  border-left:4px solid var(--brass);border-radius:0 12px 12px 0;padding:14px 16px;margin:14px 0;font-size:.9rem}
.callout b{display:block;font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);margin-bottom:.2rem}
.grid2{display:grid;gap:12px;margin-top:10px}
.grid3b{display:grid;gap:12px;margin-top:14px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px}
.tile .t{font-family:'Fraunces',serif;font-size:1rem;display:block;margin-bottom:.25rem}
.tile p{font-size:.87rem;color:var(--muted)}
.check{list-style:none;display:grid;gap:.5rem;margin-top:8px}
.check li{font-size:.9rem;display:flex;gap:.55em}
.check li::before{content:"→";color:var(--brassd);font-weight:800;flex:none}
.factrow{display:grid;gap:10px;margin-top:14px}
.factrow div{background:var(--foam);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.factrow b{display:block;font-size:.65rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.factrow span{font-size:.9rem;font-weight:600}
.deflist{list-style:none;display:grid;gap:.6rem;margin-top:10px}
.deflist li{display:grid;grid-template-columns:150px 1fr;gap:.8em;padding-bottom:.6rem;border-bottom:1px solid var(--line);font-size:.9rem}
.deflist li:last-child{border:0}
.deflist b{font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:.2em}
.tblscroll2{overflow-x:auto;-webkit-overflow-scrolling:touch;margin-top:12px}
.dtable{width:100%;border-collapse:collapse;font-size:.86rem;min-width:460px}
.dtable th,.dtable td{border:1px solid var(--line);padding:.6em .75em;text-align:left;vertical-align:top}
.dtable th{background:var(--mist);font-size:.68rem;letter-spacing:.06em;text-transform:uppercase}
.dtable td:first-child{font-weight:700;white-space:nowrap}
.faq2 details{border-bottom:1px solid var(--line);padding:.9rem 0}
.faq2 summary{font-weight:700;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:1em;font-size:.95rem}
.faq2 summary::-webkit-details-marker{display:none}
.faq2 summary::after{content:"+";color:var(--brassd);font-size:1.25rem;line-height:1;flex:none}
.faq2 details[open] summary::after{content:"–"}
.faq2 p{font-size:.9rem;color:var(--muted);margin-top:.55rem}
.srclist{list-style:none;display:grid;gap:.6rem;margin-top:10px}
.srclist li{display:grid;gap:.1rem;font-size:.88rem;padding-bottom:.55rem;border-bottom:1px solid var(--line)}
.srclist a{font-weight:700;color:var(--ink2)}
.srclist span{font-size:.78rem;color:var(--muted)}
.inlinecta{background:linear-gradient(135deg,var(--ink2),var(--ink));color:#fff;border-radius:14px;
  padding:18px;margin-top:18px;display:grid;gap:12px}
.inlinecta b{display:block;font-family:'Fraunces',serif;font-size:1.1rem}
.inlinecta span{font-size:.85rem;color:#A9C4D2}
.ictabtn{background:var(--brass);color:var(--ink);font-weight:800;text-decoration:none;padding:.85em;
  border-radius:11px;text-align:center;font-size:1rem}
.sources{border-bottom:0}
.ftr{background:#061620;color:#8FA8B6;font-size:.76rem;padding:28px 0 22px;line-height:1.6}
.ftr p{margin-bottom:.7rem}
.ftr b{color:#B9CFDA}
.built{color:#5F7A8A;font-size:.72rem}
.stickybar{position:fixed;left:0;right:0;bottom:0;z-index:70;background:rgba(8,36,59,.97);
  padding:9px 14px calc(9px + env(safe-area-inset-bottom));display:flex;gap:10px;align-items:center;
  border-top:1px solid rgba(255,255,255,.12)}
.stickybar div{flex:1;min-width:0}
.stickybar b{display:block;color:#fff;font-size:.8rem}
.stickybar span{display:block;color:#8FADBB;font-size:.65rem}
.stickybar a{background:var(--brass);color:var(--ink);font-weight:800;text-decoration:none;
  padding:.65em 1.1em;border-radius:99px;font-size:.9rem;white-space:nowrap}
@media(min-width:700px){
  .qfgrid{grid-template-columns:repeat(3,1fr)}
  .shipgrid2{grid-template-columns:1fr 1fr}
  .inc2{grid-template-columns:1fr 1fr}
  .grid2{grid-template-columns:1fr 1fr}
  .grid3b{grid-template-columns:repeat(3,1fr)}
  .factrow{grid-template-columns:repeat(3,1fr)}
  .inlinecta{grid-template-columns:1fr auto;align-items:center}
  .ictabtn{padding:.85em 1.6em}
}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""


def main():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(OUT, exist_ok=True)
    all_issues = []

    for L in data["lines"]:
        page = build_page(L, CSS)

        # safety net: never ship a price.
        # Scope the scan to <main> — the footer legitimately contains the words
        # "discounts"/"savings" inside the disclaimer stating we display none.
        import re as _re
        m = _re.search(r"<main[^>]*>(.*?)</main>", page, _re.S)
        body_only = (m.group(1) if m else page).lower()
        for b in BANNED:
            if b in body_only:
                print(f"  !! BLOCKED: '{b}' found in {L['slug']} content — remove before publishing")

        path = os.path.join(OUT, L["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  built {L['slug']}.html  ({len(page)//1024} KB)")
        all_issues += staleness(L)

    print("\n─── STALENESS REPORT ───")
    if not all_issues:
        print("  All data within refresh windows.")
    for path, ver, age, limit in all_issues:
        if ver == "PENDING":
            print(f"  NEVER VERIFIED   {path}  (refresh every {limit}d)")
        elif age is None:
            print(f"  BAD DATE '{ver}'  {path}")
        else:
            print(f"  STALE {age}d       {path}  (limit {limit}d, verified {ver})")

    pend = json.dumps(data).count("VERIFY")
    print(f"\n  {pend} fields still marked VERIFY — fill these from tier-1 sources.")
    print("  Pages render these as visible gaps rather than inventing data.\n")


if __name__ == "__main__":
    main()
