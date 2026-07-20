# -*- coding: utf-8 -*-
"""Two interactive homepage sections that educate and drive calls:
  when_to_go(lang), tap a month, see which regions are in season (+ hurricane note).
  cabin_guide(lang), tap a cabin type, see what you get and what to watch for.
General cruise knowledge only (compliant, no invented line-specific facts). Guarded JS."""
import json
from config import PHONE_HREF
from data import DESTINATIONS

_NAME = {d["slug"]: d["name"] for d in DESTINATIONS}

# General seasonality (well-known, region-level, not line-specific). months are 1-12.
SEASONS = {
    "caribbean": {"months": [11, 12, 1, 2, 3, 4], "peak": {"en": "Dec-Mar", "es": "Dic-Mar"}, "warn": True},
    "bahamas": {"months": list(range(1, 13)), "peak": {"en": "Year-round", "es": "Todo el año"}, "warn": True},
    "alaska": {"months": [5, 6, 7, 8, 9], "peak": {"en": "Jun-Aug", "es": "Jun-Ago"}},
    "mediterranean": {"months": [4, 5, 6, 7, 8, 9, 10], "peak": {"en": "Jun-Aug", "es": "Jun-Ago"}},
    "mexican-riviera": {"months": [10, 11, 12, 1, 2, 3, 4], "peak": {"en": "Nov-Mar", "es": "Nov-Mar"}},
    "panama-canal": {"months": [10, 11, 12, 1, 2, 3, 4], "peak": {"en": "Dec-Mar", "es": "Dic-Mar"}},
    "northern-europe": {"months": [5, 6, 7, 8], "peak": {"en": "Jun-Aug", "es": "Jun-Ago"}},
    "hawaii": {"months": list(range(1, 13)), "peak": {"en": "Year-round", "es": "Todo el año"}},
}

MONTHS = {
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "es": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
}

CABINS = [
    {"id": "interior", "emo": "🛏️",
     "name": {"en": "Interior", "es": "Interior"},
     "get": {"en": "No window, the lowest-cost way to sail. Great if you're barely in the room.",
             "es": "Sin ventana, la forma más económica de navegar. Ideal si casi no estás en el camarote."},
     "watch": {"en": "No natural light, so mornings can feel dark. A few ships offer interior cabins with a live 'virtual balcony' screen, worth asking about.",
               "es": "Sin luz natural, las mañanas pueden sentirse oscuras. Algunos barcos ofrecen interiores con un 'balcón virtual' en pantalla, vale la pena preguntar."}},
    {"id": "ocean", "emo": "🪟",
     "name": {"en": "Ocean view", "es": "Vista al mar"},
     "get": {"en": "A window or porthole and natural light, usually for a modest step up from interior.",
             "es": "Una ventana o portilla y luz natural, normalmente por un pequeño aumento sobre el interior."},
     "watch": {"en": "On some decks the view is partly blocked by lifeboats, which cabins are obstructed isn't obvious online.",
               "es": "En algunas cubiertas la vista queda parcialmente bloqueada por botes salvavidas, cuáles camarotes están obstruidos no es obvio en línea."}},
    {"id": "balcony", "emo": "🌅",
     "name": {"en": "Balcony", "es": "Balcón"},
     "get": {"en": "Your own private outdoor space, the most popular upgrade, and the one most guests say they'd repeat.",
             "es": "Tu propio espacio exterior privado, la mejora más popular, y la que más huéspedes repetirían."},
     "watch": {"en": "Cabins directly under the pool deck or above a theatre can be noisy, and some balconies are partly obstructed. The exact cabin numbers to avoid aren't published.",
               "es": "Los camarotes justo debajo de la cubierta de piscina o encima de un teatro pueden ser ruidosos, y algunos balcones están parcialmente obstruidos. Los números exactos a evitar no se publican."}},
    {"id": "suite", "emo": "🛎️",
     "name": {"en": "Suite", "es": "Suite"},
     "get": {"en": "The most space, plus perks that can include priority boarding, a concierge and reserved areas.",
             "es": "El mayor espacio, más beneficios que pueden incluir embarque prioritario, conserje y áreas reservadas."},
     "watch": {"en": "Perks vary enormously by line and by suite tier, 'suite' means very different things on different ships. Confirm exactly what's included.",
               "es": "Los beneficios varían enormemente por línea y por nivel de suite, 'suite' significa cosas muy distintas en cada barco. Confirma exactamente qué incluye."}},
]

_T = {
    "en": {
        "when_kicker": "When to sail", "when_h2": "When can you actually go?",
        "when_sub": "Tap a month to see which regions are in season. Picking the right month often matters more than picking the ship.",
        "when_inseason": "In season", "when_peak": "peak", "when_none": "Few regions sail this month, an advisor can find one that fits.",
        "when_hurricane": "Atlantic hurricane season (Jun 1-Nov 30). Sailings still operate and reroute when needed, travel insurance matters more in these months.",
        "cab_kicker": "Choosing a cabin", "cab_h2": "Which cabin, really?",
        "cab_sub": "Same ship, same week, wildly different experiences. Tap a category to see what you get and what to watch for.",
        "cab_get": "What you get", "cab_watch": "Watch for",
        "cab_advisor": "The exact cabin numbers to avoid on each ship aren't published, that's exactly what an advisor knows.",
        "call": "Talk it through, call now",
    },
    "es": {
        "when_kicker": "Cuándo navegar", "when_h2": "¿Cuándo puedes ir realmente?",
        "when_sub": "Toca un mes para ver qué regiones están en temporada. Elegir el mes correcto suele importar más que elegir el barco.",
        "when_inseason": "En temporada", "when_peak": "pico", "when_none": "Pocas regiones navegan este mes, un asesor puede encontrar una que encaje.",
        "when_hurricane": "Temporada de huracanes del Atlántico (1 jun-30 nov). Los cruceros operan y se redirigen cuando es necesario, el seguro de viaje importa más en estos meses.",
        "cab_kicker": "Elegir camarote", "cab_h2": "¿Qué camarote, en realidad?",
        "cab_sub": "Mismo barco, misma semana, experiencias muy distintas. Toca una categoría para ver qué obtienes y qué vigilar.",
        "cab_get": "Qué obtienes", "cab_watch": "Vigila",
        "cab_advisor": "Los números exactos de camarotes a evitar en cada barco no se publican, eso es justo lo que sabe un asesor.",
        "call": "Conversémoslo, llama ahora",
    },
}


def when_to_go(lang):
    t = _T[lang]
    data = {"seasons": {s: {"months": v["months"], "peak": v["peak"][lang], "warn": bool(v.get("warn"))}
                        for s, v in SEASONS.items()},
            "names": {s: n[lang] for s, n in _NAME.items()},
            "months": MONTHS[lang], "inseason": t["when_inseason"], "peak": t["when_peak"],
            "none": t["when_none"], "hurricane": t["when_hurricane"]}
    payload = json.dumps(data, ensure_ascii=False)
    btns = "".join(f'<button type="button" class="whn-m" data-m="{i}">{MONTHS[lang][i]}</button>' for i in range(12))
    return f"""<section class="section foam" id="when"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t['when_kicker']}</span><h2>{t['when_h2']}</h2><p>{t['when_sub']}</p></div>
  <div class="whn"><div class="whn-months" id="whnMonths">{btns}</div>
    <div class="whn-panel" id="whnPanel"></div></div>
  <div class="whn-cta"><a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('when')"><span class="ic">☎</span>{t['call']}</a></div>
</div>
<script>(function(){{
  var D={payload};var months=document.getElementById('whnMonths'),panel=document.getElementById('whnPanel');
  if(!months||!panel)return;var cur=0;try{{cur=new Date().getMonth();}}catch(e){{}}
  function sel(m){{
    [].forEach.call(months.children,function(b,i){{b.className='whn-m'+(i===m?' on':'');}});
    var regions=[];for(var s in D.seasons){{if(D.seasons[s].months.indexOf(m+1)>-1)regions.push(s);}}
    var warn=regions.some(function(s){{return D.seasons[s].warn;}})&&m>=5&&m<=10;
    var h='';
    if(regions.length){{h+='<p class="whn-lbl">'+D.inseason+', '+D.months[m]+'</p><div class="whn-regions">';
      regions.forEach(function(s){{h+='<span class="whn-chip">'+D.names[s]+' <i>'+D.peak+' '+D.seasons[s].peak+'</i></span>';}});
      h+='</div>';}}else{{h+='<p class="whn-lbl">'+D.none+'</p>';}}
    if(warn)h+='<div class="whn-warn">⚠ '+D.hurricane+'</div>';
    panel.innerHTML=h;
  }}
  [].forEach.call(months.children,function(b){{b.onclick=function(){{sel(+b.getAttribute('data-m'));}};}});
  sel(cur);
}})();</script>
</section>"""


def cabin_guide(lang):
    t = _T[lang]
    data = {"cabins": [{"id": c["id"], "emo": c["emo"], "name": c["name"][lang],
                        "get": c["get"][lang], "watch": c["watch"][lang]} for c in CABINS],
            "getL": t["cab_get"], "watchL": t["cab_watch"], "advisor": t["cab_advisor"]}
    payload = json.dumps(data, ensure_ascii=False)
    tabs = "".join(f'<button type="button" class="cab-tab" data-c="{c["id"]}"><span class="cab-emo">{c["emo"]}</span>{c["name"][lang]}</button>' for c in CABINS)
    return f"""<section class="section" id="cabins"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t['cab_kicker']}</span><h2>{t['cab_h2']}</h2><p>{t['cab_sub']}</p></div>
  <div class="cab"><div class="cab-tabs" id="cabTabs">{tabs}</div>
    <div class="cab-panel" id="cabPanel"></div></div>
  <div class="whn-cta"><a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('cabins')"><span class="ic">☎</span>{t['call']}</a></div>
</div>
<script>(function(){{
  var D={payload};var tabs=document.getElementById('cabTabs'),panel=document.getElementById('cabPanel');
  if(!tabs||!panel)return;
  function sel(id){{
    var c=null;D.cabins.forEach(function(x){{if(x.id===id)c=x;}});if(!c)return;
    [].forEach.call(tabs.children,function(b){{b.className='cab-tab'+(b.getAttribute('data-c')===id?' on':'');}});
    panel.innerHTML='<div class="cab-body"><div class="cab-col"><span class="cab-lbl good">'+D.getL+'</span><p>'+c.get+'</p></div>'
      +'<div class="cab-col"><span class="cab-lbl warn">'+D.watchL+'</span><p>'+c.watch+'</p></div></div>'
      +'<p class="cab-advisor">💡 '+D.advisor+'</p>';
  }}
  [].forEach.call(tabs.children,function(b){{b.onclick=function(){{sel(b.getAttribute('data-c'));}};}});
  sel('balcony');
}})();</script>
</section>"""
