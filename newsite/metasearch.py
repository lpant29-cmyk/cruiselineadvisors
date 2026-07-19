# -*- coding: utf-8 -*-
"""Find-your-cruise metasearch — the site's USP tool. The user picks Destination + Departure port +
When + Who's travelling; the tool ranks the ships (across every published line) that sail that
region, matched to their style, and routes every result to a call for the exact sailing + best rate.
NO PRICES — we compare what you get, never fares. Region-level matching (deployment.json); the
precise ship/date/port is confirmed on the call. Guarded IIFE JS, self-contained payload."""
import json
import os
from config import PHONE_HREF, PHONE_DISPLAY
from data import LINES
from ships import all_ships, slugify
from linepage import line_data

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}
_REGIONS = json.load(open(os.path.join(os.path.dirname(__file__), "data", "deployment.json"),
                          encoding="utf-8"))["regions"]

_MONTHS = {"en": ["January", "February", "March", "April", "May", "June", "July", "August",
                  "September", "October", "November", "December"],
           "es": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                  "Septiembre", "Octubre", "Noviembre", "Diciembre"]}

_T = {
    "en": {"dest": "Where do you want to sail?", "port": "Sail from", "when": "When",
           "who": "Who's travelling?", "any": "Any", "anyport": "Any US/Canada port",
           "search": "Find my cruise", "results": "ships match", "reco": "Top match",
           "guests": "guests", "eat": "places to eat", "sails": "Sails",
           "view": "View ship", "call": "Call to book", "book": "Book this",
           "off": "is off-season for", "sweet": "is the sweet spot — ask us about the best time.",
           "none": "No ship in our published lines matches yet — but our specialists cover more. Call and we'll find it.",
           "cta": "Found one you like? Rates change daily by ship, date and cabin — one call gets you the real number and the best our partners can offer.",
           "filt": "Refine:", "family": "Great for families", "couples": "Couples & adults",
           "newest": "Newest ships", "biggest": "Biggest ships",
           "parties": [("any", "Just exploring"), ("family", "Family"), ("couple", "Couple"),
                       ("friends", "Friends"), ("solo", "Solo")],
           "lead": "Skip scrolling hundreds of pages. Tell us where and when — we'll line up the ships that fit and one call books the right one."},
    "es": {"dest": "¿A dónde quieres navegar?", "port": "Zarpar desde", "when": "Cuándo",
           "who": "¿Quién viaja?", "any": "Cualquiera", "anyport": "Cualquier puerto de EE.UU./Canadá",
           "search": "Encontrar mi crucero", "results": "barcos coinciden", "reco": "Mejor opción",
           "guests": "huéspedes", "eat": "lugares para comer", "sails": "Navega",
           "view": "Ver barco", "call": "Llama para reservar", "book": "Reservar",
           "off": "está fuera de temporada para", "sweet": "es la mejor época — pregúntanos.",
           "none": "Ningún barco de nuestras líneas coincide aún — pero nuestros especialistas cubren más. Llama y lo encontramos.",
           "cta": "¿Encontraste uno? Las tarifas cambian a diario — una llamada te da el número real y la mejor tarifa de nuestros socios.",
           "filt": "Refinar:", "family": "Ideal para familias", "couples": "Parejas y adultos",
           "newest": "Barcos más nuevos", "biggest": "Barcos más grandes",
           "parties": [("any", "Solo explorando"), ("family", "Familia"), ("couple", "Pareja"),
                       ("friends", "Amigos"), ("solo", "Solo")],
           "lead": "Sin revisar cientos de páginas. Dinos dónde y cuándo — alineamos los barcos que encajan y una llamada reserva el correcto."},
}


def _who_short(who, n=150):
    if not who:
        return ""
    who = who.strip()
    return who if len(who) <= n else who[:n].rsplit(" ", 1)[0] + "…"


def _flags(who, positioning):
    s = f"{who or ''} {positioning or ''}".lower()
    return {
        "fam": any(k in s for k in ("famil", "kid", "multi-gen", "children", "water")),
        "cpl": any(k in s for k in ("couple", "adult", "romantic", "honeymoon", "refined")),
        "lux": any(k in s for k in ("luxur", "premium", "grill", "suite", "elegan", "yacht club", "tradition")),
        "val": any(k in s for k in ("value", "budget", "casual", "fun", "easygoing", "first-time")),
    }


def _payload(lang):
    ships = []
    for line_slug, s in all_ships():
        exp = s.get("exp") or {}
        who = exp.get("who_for")
        pos = (line_data(line_slug).get("positioning") or "")
        regs = [r["id"] for r in _REGIONS if line_slug in r["lines"]]
        if not regs:
            continue
        fl = _flags(who, pos)
        ships.append({
            "id": f"{line_slug}::{s['name']}", "name": s["name"], "line": _NAME.get(line_slug, line_slug),
            "emo": _EMO.get(line_slug, "🚢"), "url": f"/{lang}/lines/{line_slug}/ships/{slugify(s['name'])}/",
            "guests": s.get("guests"), "year": s.get("year"), "cls": s.get("class"),
            "who": _who_short(who), "dine": len(exp.get("dining") or []),
            "regions": regs, "fam": fl["fam"], "cpl": fl["cpl"], "lux": fl["lux"], "val": fl["val"],
        })
    regions = [{"id": r["id"], "name": r["name"], "emoji": r["emoji"], "season": r["season"],
                "months": r["months"], "ports": r["ports"]} for r in _REGIONS]
    return {"regions": regions, "ships": ships, "months": _MONTHS[lang], "t": _T[lang],
            "phone": PHONE_DISPLAY, "href": PHONE_HREF}


def metasearch_tool(lang):
    t = _T[lang]
    data = _payload(lang)
    payload = json.dumps(data, ensure_ascii=False)
    region_opts = "".join(f'<option value="{r["id"]}">{r["emoji"]} {r["name"]}</option>' for r in data["regions"])
    month_opts = "".join(f'<option value="{i+1}">{m}</option>' for i, m in enumerate(data["months"]))
    party_opts = "".join(f'<option value="{v}">{lbl}</option>' for v, lbl in t["parties"])
    return f"""<div class="ms" id="ms">
  <form class="ms-form" id="msForm" onsubmit="return false">
    <label class="ms-field"><span>{t['dest']}</span>
      <select id="msDest">{region_opts}</select></label>
    <label class="ms-field"><span>{t['port']}</span>
      <select id="msPort"><option value="">{t['anyport']}</option></select></label>
    <label class="ms-field"><span>{t['when']}</span>
      <select id="msMonth"><option value="">{t['any']}</option>{month_opts}</select></label>
    <label class="ms-field"><span>{t['who']}</span>
      <select id="msWho">{party_opts}</select></label>
    <button class="btn btn-call ms-go" id="msGo" type="submit"><span class="ic">🔎</span>{t['search']}</button>
  </form>
  <div class="ms-note" id="msNote"></div>
  <div class="ms-filters" id="msFilters"></div>
  <div class="ms-results" id="msResults"></div>
  <div class="ms-foot" id="msFoot"></div>
</div>
<script>(function(){{
  var D={payload}, T=D.t;
  var byRegion={{}}; D.regions.forEach(function(r){{byRegion[r.id]=r;}});
  var $=function(id){{return document.getElementById(id);}};
  var dest=$('msDest'),port=$('msPort'),month=$('msMonth'),who=$('msWho');
  if(!dest) return;
  var active={{}};  // filter chips
  function fillPorts(){{
    var r=byRegion[dest.value]; port.innerHTML='<option value="">'+T.anyport+'</option>';
    if(r) r.ports.forEach(function(p){{var o=document.createElement('option');o.value=p;o.textContent=p;port.appendChild(o);}});
  }}
  function num(n){{return (n===null||n===undefined)?null:String(n).replace(/\\B(?=(\\d{{3}})+(?!\\d))/g,',');}}
  function score(s,party){{
    var sc=0;
    if(party==='family'&&s.fam)sc+=3; if(party==='couple'&&s.cpl)sc+=3;
    if(party==='friends'&&(s.val||s.guests>3500))sc+=2; if(party==='solo'&&s.cpl)sc+=1;
    if(s.year)sc+=Math.max(0,(s.year-1995))/30;           // newer = better
    if(s.guests)sc+=Math.min(1,s.guests/6000)*0.6;         // more to do
    if(s.dine)sc+=Math.min(1,s.dine/20)*0.4;
    return sc;
  }}
  function passFilters(s){{
    if(active.family&&!s.fam)return false; if(active.couples&&!s.cpl)return false;
    if(active.newest&&!(s.year&&s.year>=2018))return false;
    if(active.biggest&&!(s.guests&&s.guests>=4000))return false;
    return true;
  }}
  var lastList=[];
  function render(){{
    var r=byRegion[dest.value], party=who.value, mo=month.value?parseInt(month.value):0;
    var list=D.ships.filter(function(s){{return s.regions.indexOf(dest.value)>=0;}});
    list.forEach(function(s){{s._s=score(s,party);}});
    list.sort(function(a,b){{return b._s-a._s;}});
    lastList=list;
    // season note
    var note='';
    if(r){{
      note='<b>'+r.emoji+' '+r.name+'</b> — '+r.season+'.';
      if(mo&&r.months.indexOf(mo)<0) note+=' <span class="ms-warn">'+D.months[mo-1]+' '+T.off+' '+r.name+'; '+r.season+' '+T.sweet+'</span>';
    }}
    $('msNote').innerHTML=note;
    // filters
    var chips=[['family',T.family],['couples',T.couples],['newest',T.newest],['biggest',T.biggest]];
    $('msFilters').innerHTML='<span class="ms-flabel">'+T.filt+'</span>'+chips.map(function(c){{
      return '<button type="button" class="ms-chip'+(active[c[0]]?' on':'')+'" data-f="'+c[0]+'">'+c[1]+'</button>';}}).join('');
    var shown=list.filter(passFilters);
    var portTxt=port.value?(' · '+port.value):'';
    var h='';
    if(!shown.length){{ h='<p class="ms-none">'+T.none+'</p>'; }}
    else {{
      h=shown.slice(0,12).map(function(s,i){{
        var meta=[];
        if(s.guests)meta.push(num(s.guests)+' '+T.guests);
        if(s.dine)meta.push(s.dine+' '+T.eat);
        return '<article class="ms-card'+(i===0?' top':'')+'">'
          +(i===0?'<span class="ms-badge">★ '+T.reco+'</span>':'')
          +'<div class="ms-card-h"><span class="ms-emo">'+s.emo+'</span><div><h3>'+s.name+'</h3><span class="ms-line">'+s.line+'</span></div></div>'
          +(s.who?'<p class="ms-who">'+s.who+'</p>':'')
          +'<div class="ms-meta">'+meta.join(' · ')+'</div>'
          +'<div class="ms-sails">'+T.sails+' '+r.emoji+' '+r.name+portTxt+'</div>'
          +'<div class="ms-actions"><a class="ms-view" href="'+s.url+'">'+T.view+' →</a>'
          +'<a class="btn btn-call ms-bk" href="tel:'+D.href+'" onclick="trackCall(\\'metasearch\\')"><span class="ic">☎</span>'+T.book+'</a></div>'
          +'</article>';
      }}).join('');
    }}
    $('msResults').innerHTML='<div class="ms-count">'+shown.length+' '+T.results+'</div><div class="ms-grid">'+h+'</div>';
    $('msFoot').innerHTML=shown.length?('<div class="nudge"><p>'+T.cta+'</p><a class="btn btn-call" href="tel:'+D.href+'" onclick="trackCall(\\'metasearch-foot\\')"><span class="ic">☎</span>'+T.call+' · '+D.phone+'</a></div>'):'';
    // wire chips
    Array.prototype.forEach.call($('msFilters').querySelectorAll('.ms-chip'),function(b){{
      b.onclick=function(){{active[b.dataset.f]=!active[b.dataset.f];render();}};}});
  }}
  dest.onchange=function(){{fillPorts();render();}};
  port.onchange=render; month.onchange=render; who.onchange=render;
  $('msGo').onclick=render;
  fillPorts(); render();
}})();</script>"""
