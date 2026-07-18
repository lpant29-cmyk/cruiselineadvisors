#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rich home page: animated ocean hero + intent selector + chaos section + quiz."""

HOME_CSS = """
/* animated ocean hero */
.ohero{position:relative;overflow:hidden;isolation:isolate;color:#EAF3F7;
  background:radial-gradient(120% 90% at 78% 8%,rgba(217,178,90,.26),transparent 58%),
  linear-gradient(178deg,#0E3A5C 0%,#08243B 62%,#05192B 100%);padding:30px 0 0}
.ohero .wrap2{position:relative;z-index:6;padding-bottom:150px}
.osun{position:absolute;top:22px;right:-30px;width:200px;height:200px;border-radius:50%;
  background:radial-gradient(circle,rgba(255,222,158,.5),rgba(217,178,90,.14) 45%,transparent 70%);
  z-index:1;animation:osun 8s ease-in-out infinite}
@keyframes osun{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.08);opacity:1}}
.oship{position:absolute;bottom:112px;left:50%;width:min(340px,74vw);transform:translateX(-50%);
  z-index:3;animation:osail 7.5s ease-in-out infinite}
@keyframes osail{0%,100%{transform:translateX(-50%) translateY(0) rotate(-.7deg)}
  50%{transform:translateX(-50%) translateY(-8px) rotate(.7deg)}}
.owaves{position:absolute;left:0;right:0;bottom:0;height:170px;z-index:4;pointer-events:none}
.owl{position:absolute;bottom:0;left:0;width:200%;height:100%}
.owl svg{width:50%;height:100%;float:left}
.ow1{animation:oroll 20s linear infinite;opacity:.9}
.ow2{animation:oroll 14s linear infinite reverse;opacity:.8;bottom:-14px}
.ow3{animation:oroll 10s linear infinite;bottom:-30px}
@keyframes oroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.ohero h1{color:#fff;font-size:clamp(1.9rem,7.4vw,2.7rem);margin-top:.8rem;max-width:16ch}
.ohero h1 em{font-style:italic;color:var(--brass)}
.ohero .osub{margin-top:.8rem;font-size:1rem;color:#A9C4D2;max-width:36ch}
.obadge{display:inline-flex;align-items:center;gap:.45em;background:rgba(217,178,90,.16);
  border:1px solid rgba(217,178,90,.38);color:var(--brass);padding:.4em .9em;border-radius:99px;
  font-size:.68rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase}

/* intent selector */
.intent{background:#fff;border:1px solid var(--line);border-radius:20px;padding:18px;
  max-width:560px;margin:-132px auto 0;position:relative;z-index:20;
  box-shadow:0 24px 60px rgba(8,36,59,.28),0 4px 12px rgba(8,36,59,.1)}
.intent__heading{font-family:'Inter',sans-serif;font-size:14px;font-weight:700;line-height:1.4;margin-bottom:12px}
.intent__grid{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.chip{display:flex;align-items:center;gap:.5em;min-height:44px;padding:10px 11px;background:var(--foam);
  border:1.5px solid var(--line);border-radius:12px;font-family:'Inter',sans-serif;font-size:13.5px;
  font-weight:700;color:var(--ink);text-align:left;cursor:pointer;
  transition:background .16s,border-color .16s,transform .12s,box-shadow .16s;-webkit-tap-highlight-color:transparent}
.chip__emoji{font-size:1.05rem;line-height:1;flex:none}
.chip__label{flex:1;min-width:0}
.chip:hover{border-color:#B9C9CE;background:#fff}
.chip:active{transform:scale(.97)}
.chip:focus-visible{outline:3px solid var(--ink2);outline-offset:2px}
.chip[aria-pressed="true"]{background:#fff;border-color:var(--brass);box-shadow:inset 0 0 0 2px rgba(217,178,90,.22)}
.intent__cta{display:flex;align-items:center;justify-content:center;gap:.4em;width:100%;margin-top:14px;
  background:linear-gradient(180deg,var(--brass),var(--brassd));color:var(--ink);font-weight:800;
  font-size:15px;line-height:1.25;text-align:center;text-decoration:none;padding:15px 12px;border-radius:12px;
  box-shadow:0 8px 20px rgba(184,147,61,.34);min-height:52px;word-break:break-word;transition:.14s}
.intent__cta:hover{filter:brightness(1.05)}
.intent__cta:active{transform:scale(.985)}
.intent__caption{font-size:11.5px;color:var(--muted);text-align:center;margin-top:9px;line-height:1.45}

/* chaos section */
.chaos2{background:#0B1A24;color:#DBE8EE;padding:44px 0}
.chaos2 h2{color:#fff}
.chaos2 .intro{color:#93AAB8}
.tabsim2{margin-top:24px;border-radius:14px;overflow:hidden;border:1px solid rgba(255,255,255,.14);background:#071219}
.tabbar2{display:flex;align-items:center;gap:6px;background:#13232E;padding:8px 10px;overflow:hidden}
.dot2{width:9px;height:9px;border-radius:50%;flex:none}
.tstrip{display:flex;gap:4px;margin-left:8px;overflow:hidden;flex:1}
.tb2{flex:none;background:#0C1B24;border:1px solid rgba(255,255,255,.09);border-radius:6px 6px 0 0;
  padding:.35em .7em;font-size:.66rem;color:#8EA7B5;white-space:nowrap;max-width:120px;overflow:hidden;text-overflow:ellipsis}
.tbmore2{flex:none;font-size:.66rem;color:var(--brass);font-weight:800;padding:.35em .5em;white-space:nowrap}
.qgrid2{padding:20px 16px 24px;display:grid;gap:10px}
.q2{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:13px 14px;
  animation:wob2 6s ease-in-out infinite}
.q2:nth-child(2n){animation-delay:-1.4s}.q2:nth-child(3n){animation-delay:-2.9s}
@keyframes wob2{0%,100%{transform:translateY(0) rotate(-.3deg)}50%{transform:translateY(-5px) rotate(.4deg)}}
.q2 b{display:block;color:#fff;font-size:.9rem;margin-bottom:.15rem}
.q2 span{font-size:.76rem;color:#7F99A8;font-style:italic}
.pivot2{text-align:center;padding:28px 16px 4px}
.pivot2 .arr{font-size:1.7rem;color:var(--brass)}
.pivot2 h3{color:#fff;font-size:clamp(1.3rem,4.4vw,1.8rem);margin-top:.4rem;max-width:22ch;margin-inline:auto}
.pivot2 h3 em{font-style:italic;color:#7FD4D0}
.pivot2 p{color:#93AAB8;font-size:.92rem;max-width:44ch;margin:.6rem auto 0}
.calm2{margin-top:22px;background:linear-gradient(150deg,#12506B,#0A2F42);
  border:1px solid rgba(127,212,208,.28);border-radius:16px;padding:22px}
.calmrow2{display:grid;gap:14px}
.cm2{display:flex;gap:.7em;align-items:flex-start}
.cm2 .ic2{flex:none;width:30px;height:30px;border-radius:9px;background:rgba(127,212,208,.16);
  display:flex;align-items:center;justify-content:center;font-size:.95rem}
.cm2 b{display:block;color:#fff;font-size:.9rem}
.cm2 span{font-size:.8rem;color:#A8C4D1}
.calmbtn{display:block;background:var(--brass);color:var(--ink);font-weight:800;text-decoration:none;
  padding:.9em;border-radius:12px;text-align:center;margin-top:18px;font-size:1rem}
.noob2{text-align:center;font-size:.74rem;color:#8FADBB;margin-top:.6rem}

/* quiz */
.quizsec{background:linear-gradient(150deg,#FFF6E8,#FFEEF0 46%,#E8F7F6);padding:44px 0}
.qcard{background:#fff;border-radius:20px;box-shadow:0 20px 50px rgba(8,36,59,.13);border:1px solid var(--line);
  max-width:600px;margin:22px auto 0;overflow:hidden}
.qhead2{background:linear-gradient(120deg,var(--ink2),var(--ink));color:#fff;padding:18px 20px;text-align:center}
.qhead2 h3{color:#fff;font-size:1.15rem}
.qhead2 p{color:#A9CBD8;font-size:.82rem;margin-top:.2rem}
.qbar2{height:5px;background:rgba(255,255,255,.18);border-radius:99px;margin-top:12px;overflow:hidden}
.qbar2 i{display:block;height:100%;background:linear-gradient(90deg,#FFC94D,#FF6F5E);width:33%;transition:width .45s}
.qbody2{padding:22px 20px 24px}
.qstep2{display:none}.qstep2.on{display:block}
.qq2{font-family:'Fraunces',serif;font-size:1.15rem;text-align:center;margin-bottom:14px}
.qopts2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.qopt2{background:var(--foam);border:2px solid var(--line);border-radius:14px;padding:14px 10px;cursor:pointer;
  text-align:center;font-family:inherit;font-size:.88rem;font-weight:700;color:var(--ink);
  display:flex;flex-direction:column;align-items:center;gap:.35em;transition:.16s}
.qopt2 .em2{font-size:1.6rem;line-height:1}
.qopt2 small{font-weight:500;font-size:.7rem;color:var(--muted);line-height:1.3}
.qopt2:hover{border-color:#2FC4BF;background:#fff;transform:translateY(-3px)}
.qback2{background:none;border:0;color:var(--muted);font-size:.8rem;margin:12px auto 0;cursor:pointer;
  font-family:inherit;text-decoration:underline;display:block}
.qres{text-align:center}
.qres .bdg{display:inline-block;background:linear-gradient(120deg,#FFC94D,#FF6F5E);color:#5A2A12;
  font-weight:800;font-size:.66rem;letter-spacing:.11em;text-transform:uppercase;padding:.42em 1em;border-radius:99px}
.qres h4{font-family:'Fraunces',serif;font-size:1.4rem;margin:.6rem 0 .35rem}
.qres p{font-size:.9rem;color:var(--muted);max-width:40ch;margin:0 auto}
.qtags{display:flex;flex-wrap:wrap;gap:7px;justify-content:center;margin:14px 0 4px}
.qtags span{background:var(--mist);border:1px solid var(--line);border-radius:99px;padding:.35em .85em;
  font-size:.78rem;font-weight:700}
.qcall{display:block;background:linear-gradient(180deg,var(--brass),var(--brassd));color:var(--ink);
  font-weight:800;text-decoration:none;padding:.9em;border-radius:12px;margin:16px auto 0;max-width:320px;text-align:center}
@media(min-width:700px){
  .qgrid2{grid-template-columns:repeat(3,1fr)}
  .calmrow2{grid-template-columns:repeat(3,1fr)}
}
@media(max-width:365px){
  .intent{padding:15px}.chip{font-size:12.5px;padding:9px 8px}.intent__cta{font-size:14px}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

SHIP_SVG = """<svg class="oship" viewBox="0 0 420 150" fill="none" aria-hidden="true">
<path d="M36 104h348c-10 22-30 32-58 32H92c-28 0-46-10-56-32z" fill="#04121E"/>
<path d="M36 104h348c-3 7-8 13-14 17H50c-6-4-11-10-14-17z" fill="#0E3A5C"/>
<rect x="62" y="80" width="296" height="24" rx="4" fill="#F4F8F9"/>
<rect x="86" y="60" width="248" height="21" rx="4" fill="#E4EDEF"/>
<rect x="118" y="42" width="184" height="19" rx="4" fill="#F4F8F9"/>
<rect x="152" y="27" width="112" height="16" rx="4" fill="#E4EDEF"/>
<path d="M196 27h34v-15c0-4-3-7-7-7h-20c-4 0-7 3-7 7z" fill="#0E3A5C"/>
<rect x="196" y="7" width="34" height="6" rx="3" fill="#D9B25A"/>
<g fill="#D9B25A" opacity=".9">
<rect x="74" y="88" width="9" height="7" rx="1.6"/><rect x="90" y="88" width="9" height="7" rx="1.6"/>
<rect x="106" y="88" width="9" height="7" rx="1.6"/><rect x="122" y="88" width="9" height="7" rx="1.6"/>
<rect x="138" y="88" width="9" height="7" rx="1.6"/><rect x="154" y="88" width="9" height="7" rx="1.6"/>
<rect x="170" y="88" width="9" height="7" rx="1.6"/><rect x="186" y="88" width="9" height="7" rx="1.6"/>
<rect x="202" y="88" width="9" height="7" rx="1.6"/><rect x="218" y="88" width="9" height="7" rx="1.6"/>
<rect x="234" y="88" width="9" height="7" rx="1.6"/><rect x="250" y="88" width="9" height="7" rx="1.6"/>
<rect x="266" y="88" width="9" height="7" rx="1.6"/><rect x="282" y="88" width="9" height="7" rx="1.6"/>
<rect x="298" y="88" width="9" height="7" rx="1.6"/><rect x="314" y="88" width="9" height="7" rx="1.6"/>
<rect x="330" y="88" width="9" height="7" rx="1.6"/>
<rect x="100" y="67" width="8" height="7" rx="1.6"/><rect x="116" y="67" width="8" height="7" rx="1.6"/>
<rect x="132" y="67" width="8" height="7" rx="1.6"/><rect x="148" y="67" width="8" height="7" rx="1.6"/>
<rect x="164" y="67" width="8" height="7" rx="1.6"/><rect x="180" y="67" width="8" height="7" rx="1.6"/>
<rect x="196" y="67" width="8" height="7" rx="1.6"/><rect x="212" y="67" width="8" height="7" rx="1.6"/>
<rect x="228" y="67" width="8" height="7" rx="1.6"/><rect x="244" y="67" width="8" height="7" rx="1.6"/>
<rect x="260" y="67" width="8" height="7" rx="1.6"/><rect x="276" y="67" width="8" height="7" rx="1.6"/>
<rect x="292" y="67" width="8" height="7" rx="1.6"/><rect x="308" y="67" width="8" height="7" rx="1.6"/>
<rect x="130" y="48" width="8" height="7" rx="1.6"/><rect x="146" y="48" width="8" height="7" rx="1.6"/>
<rect x="162" y="48" width="8" height="7" rx="1.6"/><rect x="178" y="48" width="8" height="7" rx="1.6"/>
<rect x="194" y="48" width="8" height="7" rx="1.6"/><rect x="210" y="48" width="8" height="7" rx="1.6"/>
<rect x="226" y="48" width="8" height="7" rx="1.6"/><rect x="242" y="48" width="8" height="7" rx="1.6"/>
<rect x="258" y="48" width="8" height="7" rx="1.6"/><rect x="274" y="48" width="8" height="7" rx="1.6"/>
</g></svg>"""

WAVES_SVG = """<div class="owaves" aria-hidden="true">
<div class="owl ow1">
<svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0 96c160-34 300 22 480 8s320-52 520-28 300 46 440 24v100H0z" fill="#0E3A5C"/></svg>
<svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0 96c160-34 300 22 480 8s320-52 520-28 300 46 440 24v100H0z" fill="#0E3A5C"/></svg></div>
<div class="owl ow2">
<svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0 118c200-28 340 16 540 6s330-40 520-20 260 34 380 22v74H0z" fill="#0A2C46"/></svg>
<svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0 118c200-28 340 16 540 6s330-40 520-20 260 34 380 22v74H0z" fill="#0A2C46"/></svg></div>
<div class="owl ow3">
<svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0 140c180-22 320 14 500 8s340-30 520-14 280 26 420 14v52H0z" fill="#05192B"/></svg>
<svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0 140c180-22 320 14 500 8s340-30 520-14 280 26 420 14v52H0z" fill="#05192B"/></svg></div>
</div>"""


def rich_hero(phone_display, phone_href):
    return f"""<section class="ohero">
<div class="osun" aria-hidden="true"></div>
{SHIP_SVG}
{WAVES_SVG}
<div class="wrap2">
<span class="obadge">☎ Phone-first cruise planning</span>
<h1>Your cruise, <em>sorted in one call.</em></h1>
<p class="osub">Independent guides to every major line — then a licensed specialist takes it from there.</p>
</div></section>

<section class="intent" aria-labelledby="intent-heading">
<h2 class="intent__heading" id="intent-heading">Where do you want to sail? Tell us and we'll take it from there.</h2>
<div class="intent__grid" role="group" aria-labelledby="intent-heading" id="chipGrid">
<button type="button" class="chip" aria-pressed="false" data-value="Caribbean"><span class="chip__emoji" aria-hidden="true">🏝️</span><span class="chip__label">Caribbean</span></button>
<button type="button" class="chip" aria-pressed="false" data-value="Alaska"><span class="chip__emoji" aria-hidden="true">🏔️</span><span class="chip__label">Alaska</span></button>
<button type="button" class="chip" aria-pressed="false" data-value="Mediterranean"><span class="chip__emoji" aria-hidden="true">🏛️</span><span class="chip__label">Mediterranean</span></button>
<button type="button" class="chip" aria-pressed="false" data-value="Bahamas"><span class="chip__emoji" aria-hidden="true">⛵</span><span class="chip__label">Bahamas</span></button>
<button type="button" class="chip" aria-pressed="false" data-value="Honeymoon"><span class="chip__emoji" aria-hidden="true">💑</span><span class="chip__label">Honeymoon</span></button>
<button type="button" class="chip" aria-pressed="false" data-value="Family"><span class="chip__emoji" aria-hidden="true">👨‍👩‍👧</span><span class="chip__label">Family</span></button>
</div>
<a href="tel:{phone_href}" class="intent__cta" id="callCta" onclick="trackCall('intent')">
<span aria-hidden="true">☎</span><span id="ctaLabel">Get today's prices — call now</span></a>
<p class="intent__caption">Live pricing changes daily. An advisor gives you the real number in minutes.</p>
</section>"""


def chaos_section(phone_display, phone_href):
    QS = [("\"Which cabin do I actually book?\"","Same price, same deck — one is under the nightclub."),
          ("\"Is this a good deal or not?\"","No baseline to compare against, and the number keeps moving."),
          ("\"What's actually included?\"","Gratuities, wi-fi, drinks, excursions — or not."),
          ("\"Which month should we go?\"","Cheaper in September. Nobody says why."),
          ("\"Will the kids be bored?\"","Three age groups, one ship, and Grandma's coming too."),
          ("\"Can we get cabins together?\"","Four families, four cards, one site that won't allow it.")]
    qs = "".join(f'<div class="q2"><b>{a}</b><span>{b}</span></div>' for a,b in QS)
    return f"""<section class="chaos2"><div class="wrap2">
<div class="eyebrow" style="color:#7FD4D0">Sound familiar?</div>
<h2>Booking a cruise looks simple. Then you start comparing.</h2>
<p class="intro">Nine ships. Four cabin categories each. Three sailing months. Somewhere around tab seventeen, most people close the laptop and put it off another weekend.</p>
<div class="tabsim2">
<div class="tabbar2"><span class="dot2" style="background:#FF5F57"></span><span class="dot2" style="background:#FEBC2E"></span><span class="dot2" style="background:#28C840"></span>
<div class="tstrip"><span class="tb2">Compare balcony vs…</span><span class="tb2">Deck plans deck 8</span><span class="tb2">Is Glacier Bay incl…</span><span class="tb2">Hurricane season…</span><span class="tbmore2">+ 19 more</span></div></div>
<div class="qgrid2">{qs}</div></div>
<div class="pivot2"><div class="arr">↓</div>
<h3>Or — say it out loud once and <em>let someone else sort it.</em></h3>
<p>A licensed cruise specialist has answered all of those this week already. Ten minutes replaces a weekend of tabs.</p></div>
<div class="calm2"><div class="calmrow2">
<div class="cm2"><div class="ic2">🗣️</div><div><b>You describe the trip</b><span>Who's going, roughly when, what matters.</span></div></div>
<div class="cm2"><div class="ic2">🧭</div><div><b>They narrow it down</b><span>From nine options to the two that fit.</span></div></div>
<div class="cm2"><div class="ic2">✅</div><div><b>You decide — or don't</b><span>No pressure, no fee, no obligation.</span></div></div>
</div>
<a href="tel:{phone_href}" class="calmbtn" onclick="trackCall('chaos')">☎ {phone_display}</a>
<p class="noob2">Free call · no obligation · hang up any time · we never take payment</p>
</div></div></section>"""


def quiz_section(phone_display, phone_href):
    return f"""<section class="quizsec"><div class="wrap2">
<div class="eyebrow">60-second cruise matcher</div>
<h2>Three taps. We'll point you in a direction.</h2>
<p class="intro">Not a quote, not a booking — a shortcut past the first hour of research.</p>
<div class="qcard">
<div class="qhead2"><h3 id="q-title">What kind of cruiser are you?</h3>
<p id="q-count">Question 1 of 3</p><div class="qbar2"><i id="q-prog"></i></div></div>
<div class="qbody2">
<div class="qstep2 on" id="qs1"><div class="qq2">Who's coming along?</div><div class="qopts2">
<button class="qopt2" onclick="pick(1,'family')"><span class="em2">👨‍👩‍👧</span><span>Family with kids</span><small>Ages all over the place</small></button>
<button class="qopt2" onclick="pick(1,'couple')"><span class="em2">💑</span><span>Just the two of us</span><small>Adults, quieter please</small></button>
<button class="qopt2" onclick="pick(1,'group')"><span class="em2">🎊</span><span>Big group</span><small>Reunion, birthday, wedding</small></button>
<button class="qopt2" onclick="pick(1,'solo')"><span class="em2">🧳</span><span>Solo or friends</span><small>Flexible and easygoing</small></button>
</div></div>
<div class="qstep2" id="qs2"><div class="qq2">What's the ideal day?</div><div class="qopts2">
<button class="qopt2" onclick="pick(2,'action')"><span class="em2">🎢</span><span>Nonstop action</span><small>Slides, shows, always something</small></button>
<button class="qopt2" onclick="pick(2,'scenery')"><span class="em2">🏔️</span><span>Scenery &amp; wildlife</span><small>Glaciers, fjords, whales</small></button>
<button class="qopt2" onclick="pick(2,'culture')"><span class="em2">🏛️</span><span>History &amp; ports</span><small>A new city every morning</small></button>
<button class="qopt2" onclick="pick(2,'relax')"><span class="em2">🍹</span><span>Do nothing, well</span><small>Beach, deck chair, repeat</small></button>
</div><button class="qback2" onclick="goStep(1)">← Back</button></div>
<div class="qstep2" id="qs3"><div class="qq2">How long can you get away?</div><div class="qopts2">
<button class="qopt2" onclick="pick(3,'short')"><span class="em2">⚡</span><span>A long weekend</span><small>2–5 nights</small></button>
<button class="qopt2" onclick="pick(3,'week')"><span class="em2">📅</span><span>About a week</span><small>7 nights</small></button>
<button class="qopt2" onclick="pick(3,'long')"><span class="em2">🌍</span><span>Two weeks or more</span><small>I've got time</small></button>
<button class="qopt2" onclick="pick(3,'flex')"><span class="em2">🤷</span><span>Totally flexible</span><small>Tell me what's best</small></button>
</div><button class="qback2" onclick="goStep(2)">← Back</button></div>
<div class="qstep2" id="qs4"><div class="qres">
<span class="bdg">Your starting point</span><h4 id="r-title">—</h4><p id="r-copy">—</p>
<div class="qtags" id="r-tags"></div>
<a href="tel:{phone_href}" class="qcall" onclick="trackCall('quiz')">☎ {phone_display}</a>
<p class="intent__caption">Free call · no obligation · a specialist confirms dates, ships and cabins in minutes.</p>
<button class="qback2" onclick="resetQuiz()">Start over</button>
</div></div>
</div></div>
<p class="note" style="max-width:60ch;margin:16px auto 0">This matcher is general guidance only — not a quote, offer, recommendation or booking. Availability is confirmed by the independent partner agency that books your trip.</p>
</div></section>"""


HOME_JS = """
/* intent selector */
(function(){
var g=document.getElementById('chipGrid'); if(!g) return;
var lbl=document.getElementById('ctaLabel'), sel=[];
var SHORT={'Caribbean':'Caribbean','Alaska':'Alaska','Mediterranean':'Med','Bahamas':'Bahamas','Honeymoon':'honeymoon','Family':'family'};
function upd(){lbl.textContent = sel.length===0 ? "Get today's prices — call now"
  : sel.length===1 ? 'Get '+SHORT[sel[0]]+' prices — call now' : 'Get your prices — call now';}
Array.prototype.forEach.call(g.querySelectorAll('.chip'),function(c){
  c.addEventListener('click',function(){
    var v=c.dataset.value, on=c.getAttribute('aria-pressed')!=='true';
    c.setAttribute('aria-pressed',String(on));
    var i=sel.indexOf(v); if(on&&i<0)sel.push(v); if(!on&&i>-1)sel.splice(i,1);
    upd();
    window.dataLayer=window.dataLayer||[];
    window.dataLayer.push({event:'cruise_intent_select',interest:v,selected:on,interests:sel.slice()});
  });
});
upd();
window.__intent=function(){return sel.slice()};
})();

/* quiz */
var QA={};
function goStep(n){for(var i=1;i<=4;i++){var e=document.getElementById('qs'+i);if(e)e.className='qstep2'+(i===n?' on':'');}
var p=document.getElementById('q-prog'); if(p)p.style.width=(n>=4?100:Math.round(n/3*100))+'%';
var c=document.getElementById('q-count'); if(c)c.textContent=n<4?('Question '+n+' of 3'):"Here's your match";}
function pick(s,v){QA['q'+s]=v; if(s<3)goStep(s+1); else showResult();
if(window.dataLayer)dataLayer.push({event:'quiz_step',step:s,value:v});}
function resetQuiz(){QA={};goStep(1);}
var RES={
action:['Big-ship, big-energy','Ships built like floating resorts — slides, shows and something happening every hour. The ship is the destination.',['Caribbean','Bahamas','7 nights','Family-friendly']],
scenery:['Wide windows and quiet decks','Mid-size ships with long port days and serious scenery. Timing matters more here than anywhere else.',['Alaska','Norway','June–August','Balcony worth it']],
culture:['A new city every morning','Port-intensive itineraries where the ship is the hotel and the map is the point.',['Mediterranean','Baltic','May–June','Sept–Oct']],
relax:['Beach days, minimal decisions','Shorter, warmer sailings with private island stops and very little on the schedule.',['Bahamas','Caribbean','3–5 nights','Private island']]};
function showResult(){var k=QA.q2||'relax',r=RES[k];
document.getElementById('r-title').textContent=r[0];
document.getElementById('r-copy').textContent=r[1];
var t=r[2].slice();
if(QA.q3==='short')t.push('Short getaway'); if(QA.q3==='long')t.push('Longer voyage');
if(QA.q1==='group')t.push('Group booking'); if(QA.q1==='family')t.push('Kids club');
document.getElementById('r-tags').innerHTML=t.map(function(x){return '<span>'+x+'</span>'}).join('');
goStep(4); if(window.dataLayer)dataLayer.push({event:'quiz_complete',result:k});}
"""
