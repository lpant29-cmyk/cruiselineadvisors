# -*- coding: utf-8 -*-
"""Find-your-cruise metasearch (v2), the site's USP tool. Pick Destination + Departure port + When
+ Who's travelling; the tool ranks every ship (across all lines) that sails that region, matched to
travel style. Features: progressive "load more", refine filters + Show all, a compare tray (pick up
to 4 ships -> side-by-side facts), honest 0-results reasoning, and an agent-avatar "call a licensed
agent" CTA on every result. NO PRICES, we compare what you get, never fares. Region-level matching
(deployment.json); exact ship/date/port confirmed on the call."""
import json
import os
from config import PHONE_HREF, PHONE_DISPLAY
from data import LINES
from ships import all_ships, slugify
from linepage import line_data
from facts import LINE_FACTS

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}
_REGIONS = json.load(open(os.path.join(os.path.dirname(__file__), "data", "deployment.json"),
                          encoding="utf-8"))["regions"]

# A ship's finder regions must come from its OWN itinerary (exp.deploy_note), the same source the
# ship detail page shows, not from a line-level tag that over-matches every ship to every region the
# line sails anywhere. Keyword aliases map itinerary prose to region ids.
_REGION_ALIAS = {
    "alaska": ["alaska", "glacier", "inside passage"],
    "caribbean": ["caribbean", "west indies", "antilles", "cozumel", "eastern & western", "perfect day", "cococay", "coco cay"],
    "bahamas": ["bahama", "nassau"],
    "bermuda": ["bermuda"],
    "mexican-riviera": ["mexican riviera", "mexico", "cabo", "mazatlan", "vallarta", "ensenada", "baja"],
    "canada-new-england": ["canada", "new england", "quebec", "halifax", "maritime", "st. lawrence", "new-england"],
    "hawaii": ["hawaii", "honolulu", "maui"],
    "panama-canal": ["panama"],
    "pacific-coastal": ["pacific coast", "pacific coastal"],
    "transatlantic": ["transatlantic", "transatlántic", "atlantic crossing"],
}
_VALID_REGIONS = {r["id"] for r in _REGIONS}


def region_ids_for_note(note):
    """Region ids a ship actually sails, derived from its itinerary note (single source of truth)."""
    s = (note or "").lower()
    return [rid for rid, al in _REGION_ALIAS.items() if rid in _VALID_REGIONS and any(a in s for a in al)]


def ship_regions(line_slug, exp):
    """Finder regions for a ship, ALWAYS from its own itinerary (deploy_note), the same source the
    detail page shows. If the ship has an itinerary but it isn't one of our US/Canada regions (e.g.
    Mediterranean, Australia, Asia), it returns [] so the ship is not mis-matched; a ship with NO
    published itinerary also returns [] (excluded from the finder rather than guessed)."""
    return region_ids_for_note((exp or {}).get("deploy_note"))


# Some deploy_notes read like internal/scraped editorial notes; never show those to visitors.
_AWKWARD_NOTE = ("itinerary examples", "on the page", "deployment is seasonal", "at capture",
                 "ship page displayed", "editorial", "verify", "not confirmed", "see needs",
                 "pages read", "imagery near", "displayed")
_REG_BY_ID = {r["id"]: r for r in _REGIONS}


def note_is_clean(note):
    low = (note or "").lower()
    return bool(note) and not any(m in low for m in _AWKWARD_NOTE)


def route_display(line_slug, exp, lang="en"):
    """A clean, visitor-facing 'where it sails' string. Uses the deploy_note when it reads well,
    otherwise a tidy region summary derived from the itinerary, otherwise a call-to-confirm line."""
    note = (exp or {}).get("deploy_note")
    if note_is_clean(note):
        return note
    regs = ship_regions(line_slug, exp or {})
    names = [_REG_BY_ID[r]["name"] for r in regs if r in _REG_BY_ID]
    if names:
        return ("Seasonal: " if lang == "en" else "Por temporada: ") + ", ".join(names)
    return ("Sails seasonally; call for current itineraries." if lang == "en"
            else "Navega por temporada; llama por itinerarios actuales.")


_MONTHS = {"en": ["January", "February", "March", "April", "May", "June", "July", "August",
                  "September", "October", "November", "December"],
           "es": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                  "Septiembre", "Octubre", "Noviembre", "Diciembre"]}

_T = {
    "en": {"dest": "Where do you want to sail?", "port": "Sail from", "when": "When",
           "who": "Who's travelling?", "any": "Any", "anyport": "Any US/Canada port",
           "search": "Find my cruise", "match": "ships match your search", "reco": "Top match",
           "guests": "guests", "eat": "dining", "do": "things to do", "sails": "Sails",
           "view": "Ship details", "book": "Call a licensed agent", "agentsub": "Free · 8am-11pm ET",
           "loadmore": "Load more ships", "showing": "Showing", "of": "of",
           "off": "is off-season for", "sweet": "is the sweet spot, ask us about the best time.",
           "compare": "Compare", "compared": "Comparing", "added": "Added",
           "traysel": "selected", "traycmp": "Compare these", "trayclr": "Clear", "close": "Close",
           "cmptitle": "Which ship wins for you?",
           "none0": "No ship matches every filter you picked.",
           "trythis": "Try removing", "unlocks": ", that alone brings back",
           "orcall": "Or just call, our specialists cover even more ships and sailings.",
           "cta": "Rates change daily by ship, date and cabin. One call gets you the real number and the best our partners can offer.",
           "call": "Call now", "filt": "Refine:", "showall": "Show all",
           "accnote": "Every line here offers accessible staterooms, step-free access and cabin type vary by ship and port, so call and we'll confirm exactly what works for you.",
           "parties": [("any", "Just exploring"), ("family", "Family"), ("couple", "Couple"),
                       ("friends", "Friends"), ("solo", "Solo")],
           "filters": [("family", "Kids & families"), ("couple", "Couples & adults"),
                       ("luxury", "Luxury / premium"), ("value", "Great value"),
                       ("newest", "Newest ships"), ("biggest", "Biggest ships"),
                       ("todo", "Most to do"), ("accessible", "Accessible cabins")],
           "rows": [("who", "Best for"), ("route", "Where it sails"), ("cls", "Ship class"),
                    ("year", "Entered service"), ("guests", "Guests"), ("dine", "Dining venues"),
                    ("acts", "Things to do"), ("kids", "Kids & families"), ("grat", "Daily gratuities"),
                    ("incl", "What's included"), ("drink", "Drink-package rule"),
                    ("cancel", "Cancellation")]},
    "es": {"dest": "¿A dónde quieres navegar?", "port": "Zarpar desde", "when": "Cuándo",
           "who": "¿Quién viaja?", "any": "Cualquiera", "anyport": "Cualquier puerto EE.UU./Canadá",
           "search": "Encontrar mi crucero", "match": "barcos coinciden", "reco": "Mejor opción",
           "guests": "huéspedes", "eat": "restaurantes", "do": "actividades", "sails": "Navega",
           "view": "Ver barco", "book": "Llama a un agente con licencia", "agentsub": "Gratis · 8am-11pm ET",
           "loadmore": "Ver más barcos", "showing": "Mostrando", "of": "de",
           "off": "está fuera de temporada para", "sweet": "es la mejor época, pregúntanos.",
           "compare": "Comparar", "compared": "Comparando", "added": "Añadido",
           "traysel": "seleccionados", "traycmp": "Comparar estos", "trayclr": "Limpiar", "close": "Cerrar",
           "cmptitle": "¿Qué barco gana para ti?",
           "none0": "Ningún barco coincide con todos tus filtros.",
           "trythis": "Prueba quitar", "unlocks": ", eso solo devuelve",
           "orcall": "O llama, nuestros especialistas cubren aún más barcos y salidas.",
           "cta": "Las tarifas cambian a diario. Una llamada te da el número real y la mejor tarifa de nuestros socios.",
           "call": "Llama ahora", "filt": "Refinar:", "showall": "Ver todos",
           "accnote": "Todas estas líneas ofrecen camarotes accesibles, el acceso sin escalones y el tipo de camarote varían por barco y puerto; llama y confirmamos lo que funciona para ti.",
           "parties": [("any", "Solo explorando"), ("family", "Familia"), ("couple", "Pareja"),
                       ("friends", "Amigos"), ("solo", "Solo")],
           "filters": [("family", "Niños y familias"), ("couple", "Parejas y adultos"),
                       ("luxury", "Lujo / premium"), ("value", "Buen valor"),
                       ("newest", "Más nuevos"), ("biggest", "Más grandes"),
                       ("todo", "Más que hacer"), ("accessible", "Camarotes accesibles")],
           "rows": [("who", "Ideal para"), ("route", "Dónde navega"), ("cls", "Clase"),
                    ("year", "En servicio"), ("guests", "Huéspedes"), ("dine", "Restaurantes"),
                    ("kids", "Niños y familias"),
                    ("acts", "Actividades"), ("grat", "Propinas diarias"),
                    ("incl", "Qué se incluye"), ("drink", "Regla de bebidas"),
                    ("cancel", "Cancelación")]},
}


def _who_short(who, n=150):
    if not who:
        return ""
    who = who.strip()
    return who if len(who) <= n else who[:n].rsplit(" ", 1)[0] + "…"


def _kids(kf, lang="en"):
    from ships import kids_family_display, _kids_is_gap
    if not kf:
        return None
    if isinstance(kf, list):
        n = [x.get("name") if isinstance(x, dict) else x for x in kf
             if (isinstance(x, dict) and x.get("name")) or isinstance(x, str)]
        return " · ".join(str(x) for x in n if x) or None
    if _kids_is_gap(kf):
        return kids_family_display(kf, lang, short=True)
    return kf if isinstance(kf, str) else None


def _flags(who, positioning):
    s = f"{who or ''} {positioning or ''}".lower()
    return {
        "fam": any(k in s for k in ("famil", "kid", "multi-gen", "children", "water")),
        "cpl": any(k in s for k in ("couple", "adult", "romantic", "honeymoon", "refined")),
        "lux": any(k in s for k in ("luxur", "premium", "grill", "elegan", "yacht club", "tradition", "refined")),
        "val": any(k in s for k in ("value", "budget", "casual", "fun", "easygoing", "first-time")),
    }


def _payload(lang):
    ships = []
    for line_slug, s in all_ships():
        exp = s.get("exp") or {}
        who = exp.get("who_for")
        pos = (line_data(line_slug).get("positioning") or "")
        regs = ship_regions(line_slug, exp)  # from the ship's own itinerary, not a line-level tag
        if not regs:
            continue
        fl = _flags(who, pos)
        lf = LINE_FACTS.get(line_slug, {})

        def fv(key):
            c = lf.get(key, {})
            v = c.get("v")
            if not v:
                return None
            return v.get(lang, v.get("en")) if isinstance(v, dict) else v

        acts = exp.get("activities")
        cabs = " ".join(str(x) for x in (line_data(line_slug).get("cabins", {}).get("categories") or [])).lower()
        solo = any(k in cabs for k in ("solo", "single", "studio"))
        ships.append({
            "id": f"{line_slug}::{s['name']}", "name": s["name"], "line": _NAME.get(line_slug, line_slug),
            "emo": _EMO.get(line_slug, "🚢"), "url": f"/{lang}/lines/{line_slug}/ships/{slugify(s['name'])}/",
            "guests": s.get("guests"), "year": s.get("year"), "cls": s.get("class"),
            "who": _who_short(who), "route": route_display(line_slug, exp, lang), "kids": _kids(exp.get("kids_family"), lang),
            "dine": len(exp.get("dining") or []), "acts": len(acts) if isinstance(acts, list) else 0,
            "regions": regs, "fam": fl["fam"], "cpl": fl["cpl"], "lux": fl["lux"], "val": fl["val"], "solo": solo,
            "grat": fv("gratuities"), "incl": fv("included"), "drink": fv("drink_pkg"), "cancel": fv("cancel"),
        })
    regions = [{"id": r["id"], "name": r["name"], "emoji": r["emoji"], "season": r["season"],
                "months": r["months"], "ports": r["ports"]} for r in _REGIONS]
    fits = ({"family": "Great for families", "couple": "Couples' choice", "solo": "Solo-friendly",
             "friends": "Good with friends"} if lang == "en" else
            {"family": "Ideal para familias", "couple": "Para parejas", "solo": "Para viajeros solos",
             "friends": "Genial con amigos"})
    return {"regions": regions, "ships": ships, "months": _MONTHS[lang], "t": _T[lang], "fits": fits,
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
    <label class="ms-field"><span>{t['dest']}</span><select id="msDest">{region_opts}</select></label>
    <label class="ms-field"><span>{t['port']}</span><select id="msPort"><option value="">{t['anyport']}</option></select></label>
    <label class="ms-field"><span>{t['when']}</span><select id="msMonth"><option value="">{t['any']}</option>{month_opts}</select></label>
    <label class="ms-field"><span>{t['who']}</span><select id="msWho">{party_opts}</select></label>
    <button class="btn btn-call ms-go" id="msGo" type="submit"><span class="ic">🔎</span>{t['search']}</button>
  </form>
  <div class="ms-note" id="msNote"></div>
  <div class="ms-filters" id="msFilters"></div>
  <div class="ms-count" id="msCount"></div>
  <div class="ms-results" id="msResults"></div>
  <div class="ms-more" id="msMore"></div>
  <div class="ms-foot" id="msFoot"></div>
  <div class="ms-tray" id="msTray"></div>
  <div class="ms-cmp" id="msCmp"></div>
</div>
<script>(function(){{
  var D={payload}, T=D.t;
  var byRegion={{}}; D.regions.forEach(function(r){{byRegion[r.id]=r;}});
  var byId={{}}; D.ships.forEach(function(s){{byId[s.id]=s;}});
  var $=function(id){{return document.getElementById(id);}};
  var dest=$('msDest'),port=$('msPort'),month=$('msMonth'),who=$('msWho');
  if(!dest) return;
  var active={{}}, shown=12, cmpSet=[];
  function num(n){{return (n===null||n===undefined)?null:String(n).replace(/\\B(?=(\\d{{3}})+(?!\\d))/g,',');}}
  function esc(s){{return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;');}}
  function fillPorts(){{
    var r=byRegion[dest.value]; port.innerHTML='<option value="">'+T.anyport+'</option>';
    if(r) r.ports.forEach(function(p){{var o=document.createElement('option');o.value=p;o.textContent=p;port.appendChild(o);}});
  }}
  function bscore(s){{ var sc=0;
    if(s.year)sc+=Math.max(0,(s.year-1995))/30; if(s.guests)sc+=Math.min(1,s.guests/6000)*0.6;
    if(s.dine)sc+=Math.min(1,s.dine/20)*0.4; return sc; }}
  // party is a PRIMARY sort key so the top results actually change with Who's travelling
  function pmatch(s,party){{
    if(party==='family')return s.fam?2:0;
    if(party==='couple')return (s.cpl&&!s.fam)?2:(s.cpl?1:0);
    if(party==='solo')return s.solo?2:(s.cpl?1:0);
    if(party==='friends')return (s.val||s.guests>=3800)?2:(s.guests>=3000?1:0);
    return 0;
  }}
  // "Just exploring" shows a spread ACROSS lines (variety), so its top row visibly differs from the
  // persona rankings, which cluster by fit and can otherwise repeat the same biggest family ships.
  function spread(arr){{
    var by={{}},order=[];
    arr.forEach(function(s){{ if(!by[s.line]){{by[s.line]=[];order.push(s.line);}} by[s.line].push(s); }});
    var out=[],added=true;
    while(added){{ added=false;
      for(var i=0;i<order.length;i++){{ var g=by[order[i]]; if(g.length){{ out.push(g.shift()); added=true; }} }} }}
    return out;
  }}
  var FILT={{family:function(s){{return s.fam;}},couple:function(s){{return s.cpl;}},
    luxury:function(s){{return s.lux;}},value:function(s){{return s.val;}},
    newest:function(s){{return s.year&&s.year>=2018;}},biggest:function(s){{return s.guests&&s.guests>=4000;}},
    todo:function(s){{return (s.acts>=6)||(s.dine>=12);}},accessible:function(s){{return true;}}}};
  function passAll(s,skip){{for(var k in active){{if(active[k]&&k!==skip&&!FILT[k](s))return false;}}return true;}}
  function base(){{var d=dest.value;return D.ships.filter(function(s){{return s.regions.indexOf(d)>=0;}});}}
  function inCmp(id){{return cmpSet.indexOf(id)>=0;}}

  function render(){{
    var r=byRegion[dest.value], party=who.value, mo=month.value?parseInt(month.value):0;
    var list=base(); list.forEach(function(s){{s._pm=pmatch(s,party);s._s=bscore(s);}});
    list.sort(function(a,b){{return (b._pm-a._pm)||(b._s-a._s);}});
    var matched=list.filter(function(s){{return passAll(s,null);}});
    if(party==='any') matched=spread(matched);  // variety for browsers; personas keep fit-ranking
    // note
    var note='';
    if(r){{ note='<b>'+r.emoji+' '+r.name+'</b>, '+r.season+'.';
      if(mo&&r.months.indexOf(mo)<0) note+=' <span class="ms-warn">'+D.months[mo-1]+' '+T.off+' '+r.name+'; '+r.season+' '+T.sweet+'</span>';
    }}
    if(active.accessible) note+='<span class="ms-accnote">♿ '+T.accnote+'</span>';
    $('msNote').innerHTML=note;
    // filters
    var chips=T.filters.map(function(c){{return '<button type="button" class="ms-chip'+(active[c[0]]?' on':'')+'" data-f="'+c[0]+'">'+c[1]+'</button>';}}).join('');
    var anyOn=Object.keys(active).some(function(k){{return active[k];}});
    $('msFilters').innerHTML='<span class="ms-flabel">'+T.filt+'</span>'+chips+(anyOn?'<button type="button" class="ms-chip ms-showall" id="msShowAll">✕ '+T.showall+'</button>':'');
    // count + results
    if(!matched.length){{
      $('msCount').innerHTML=''; $('msMore').innerHTML='';
      // 0-results reasoning: which single filter unlocks the most
      var best=null,bestN=0;
      Object.keys(active).forEach(function(k){{ if(!active[k])return;
        var n=list.filter(function(s){{return passAll(s,k);}}).length;
        if(n>bestN){{bestN=n;best=k;}} }});
      var bl=''; T.filters.forEach(function(c){{if(c[0]===best)bl=c[1];}});
      var msg='<div class="ms-none"><p><b>0</b>, '+T.none0+'</p>';
      if(best) msg+='<p>'+T.trythis+' <button type="button" class="ms-relax" data-f="'+best+'">'+bl+'</button> '+T.unlocks+' <b>'+bestN+'</b>.</p>';
      msg+='<p>'+T.orcall+'</p><a class="btn btn-call" href="tel:'+D.href+'" onclick="trackCall(\\'ms-zero\\')"><span class="ic">☎</span>'+T.call+' · '+D.phone+'</a></div>';
      $('msResults').innerHTML=msg; $('msFoot').innerHTML='';
      wire(); return;
    }}
    $('msCount').innerHTML='<b>'+matched.length+'</b> '+T.match+' &nbsp;·&nbsp; '+T.showing+' '+Math.min(shown,matched.length)+' '+T.of+' '+matched.length;
    var slice=matched.slice(0,shown);
    $('msResults').innerHTML='<div class="ms-grid">'+slice.map(function(s,i){{return card(s,i===0&&shown<=12,r);}}).join('')+'</div>';
    $('msMore').innerHTML=(shown<matched.length)?('<button type="button" class="btn ms-loadmore" id="msLoad">↓ '+T.loadmore+' ('+(matched.length-shown)+')</button>'):'';
    $('msFoot').innerHTML='<div class="nudge"><p>'+T.cta+'</p><a class="btn btn-call" href="tel:'+D.href+'" onclick="trackCall(\\'ms-foot\\')"><span class="ic">☎</span>'+T.call+' · '+D.phone+'</a></div>';
    tray(); wire();
  }}

  function card(s,top,r){{
    var meta=[]; if(s.guests)meta.push(num(s.guests)+' '+T.guests);
    if(s.dine)meta.push(s.dine+' '+T.eat); if(s.acts)meta.push(s.acts+' '+T.do);
    var sel=inCmp(s.id);
    return '<article class="ms-card'+(top?' top':'')+'">'
      +(top?'<span class="ms-badge">★ '+T.reco+'</span>':'')
      +'<div class="ms-card-h"><span class="ms-emo">'+s.emo+'</span><div><h3>'+esc(s.name)+'</h3><span class="ms-line">'+esc(s.line)+'</span></div>'
      +'<button type="button" class="ms-cmpbtn'+(sel?' on':'')+'" data-cmp="'+s.id+'">'+(sel?'✓ '+T.added:'+ '+T.compare)+'</button></div>'
      +'<div class="ms-tags">'+(s.cls?'<span class="ms-tag">'+esc(s.cls)+'</span>':'')
      +((who.value!=='any'&&pmatch(s,who.value)>0&&D.fits[who.value])?'<span class="ms-fit">✓ '+D.fits[who.value]+'</span>':'')+'</div>'
      +(s.who?'<p class="ms-who">'+esc(s.who)+'</p>':'')
      +'<div class="ms-meta">'+meta.join(' · ')+'</div>'
      +(r?'<div class="ms-sails">'+T.sails+' '+r.emoji+' '+r.name+(port.value?(' · '+esc(port.value)):'')+'</div>':'')
      +'<div class="ms-actions"><a class="ms-view" href="'+s.url+'">'+T.view+' →</a>'
      +'<a class="ms-bk" href="tel:'+D.href+'" onclick="trackCall(\\'ms-book\\')"><span class="ms-av">🧑‍✈️</span><span class="ms-bkt">'+T.book+'<small>'+T.agentsub+'</small></span></a></div>'
      +'</article>';
  }}
  function lang_class(s){{return '';}}

  function tray(){{
    var el=$('msTray');
    if(!cmpSet.length){{el.className='ms-tray';el.innerHTML='';return;}}
    el.className='ms-tray show';
    el.innerHTML='<span class="ms-traytxt"><b>'+cmpSet.length+'</b> '+T.traysel+'</span>'
      +'<button type="button" class="btn btn-call ms-traycmp" id="msTrayCmp"'+(cmpSet.length<2?' disabled':'')+'>'+T.traycmp+'</button>'
      +'<button type="button" class="ms-trayclr" id="msTrayClr">'+T.trayclr+'</button>';
  }}

  function openCmp(){{
    var el=$('msCmp'); var ships=cmpSet.map(function(id){{return byId[id];}});
    var head='<div class="ms-cmp-row ms-cmp-head"><div class="ms-cmp-lbl"></div>'+ships.map(function(s){{return '<div class="ms-cmp-col"><span class="ms-emo">'+s.emo+'</span><b>'+esc(s.name)+'</b><span class="ms-line">'+esc(s.line)+'</span></div>';}}).join('')+'</div>';
    var rows=T.rows.map(function(rw){{
      return '<div class="ms-cmp-row"><div class="ms-cmp-lbl">'+rw[1]+'</div>'+ships.map(function(s){{
        var v=s[rw[0]]; if(rw[0]==='guests')v=num(v); if(rw[0]==='dine'||rw[0]==='acts')v=v||null;
        return '<div class="ms-cmp-val">'+(v?esc(String(v)):'<span class="cmp-gap">, </span>')+'</div>';}}).join('')+'</div>';
    }}).join('');
    el.innerHTML='<div class="ms-cmp-inner"><div class="ms-cmp-top"><h3>'+T.cmptitle+'</h3><button type="button" class="ms-cmp-x" id="msCmpX">✕ '+T.close+'</button></div>'
      +'<div class="ms-cmp-scroll" style="--n:'+ships.length+'">'+head+rows+'</div>'
      +'<div class="nudge"><p>'+T.cta+'</p><a class="btn btn-call" href="tel:'+D.href+'" onclick="trackCall(\\'ms-cmp-call\\')"><span class="ic">☎</span>'+T.call+' · '+D.phone+'</a></div></div>';
    el.classList.add('show'); document.body.style.overflow='hidden';
    var x=document.getElementById('msCmpX'); if(x)x.onclick=closeCmp;
    el.onclick=function(e){{if(e.target===el)closeCmp();}};   // click backdrop to close
  }}
  function closeCmp(){{$('msCmp').classList.remove('show');document.body.style.overflow='';}}

  function wire(){{
    Array.prototype.forEach.call($('msFilters').querySelectorAll('.ms-chip'),function(b){{
      if(b.id==='msShowAll'){{b.onclick=function(){{active={{}};shown=12;render();}};return;}}
      b.onclick=function(){{active[b.dataset.f]=!active[b.dataset.f];shown=12;render();}};}});
    var relax=$('msResults').querySelector('.ms-relax'); if(relax)relax.onclick=function(){{active[relax.dataset.f]=false;render();}};
    var load=$('msLoad'); if(load)load.onclick=function(){{shown+=12;render();}};
    Array.prototype.forEach.call(document.querySelectorAll('.ms-cmpbtn'),function(b){{
      b.onclick=function(){{var id=b.dataset.cmp; var i=cmpSet.indexOf(id);
        if(i>=0)cmpSet.splice(i,1); else {{if(cmpSet.length>=4){{return;}} cmpSet.push(id);}} render();}};}});
    var tc=$('msTrayCmp'); if(tc)tc.onclick=openCmp;
    var tclr=$('msTrayClr'); if(tclr)tclr.onclick=function(){{cmpSet=[];render();}};
    var cx=$('msCmpX'); if(cx)cx.onclick=closeCmp;
  }}
  dest.onchange=function(){{fillPorts();shown=12;render();}};
  port.onchange=render; month.onchange=render; who.onchange=function(){{shown=12;render();}};
  $('msGo').onclick=function(){{shown=12;render();}};
  fillPorts(); render();
}})();</script>"""
