# -*- coding: utf-8 -*-
"""The interactive Cruise Finder ("navigator"), a 4-step where/when/who flow that
suggests a starting point and drives the call. A dolphin guide reacts to each choice.
Self-contained: bilingual data + guarded JS embedded here. Every path ends at the phone."""
import json
from config import PHONE_HREF
from data import LINES, DESTINATIONS
from scene import DOLPHIN_SVG

_LN = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}

# Which of the 8 launch lines commonly sail each region (general guidance; an advisor
# confirms actual deployment). Never presented as a guaranteed fact.
_MAP = {
    "caribbean": ["royal-caribbean", "carnival", "celebrity", "msc", "princess"],
    "bahamas": ["royal-caribbean", "carnival", "msc", "margaritaville-at-sea"],
    "alaska": ["princess", "holland-america", "royal-caribbean", "celebrity"],
    "mediterranean": ["msc", "celebrity", "princess", "cunard"],
    "mexican-riviera": ["princess", "royal-caribbean", "carnival"],
    "panama-canal": ["princess", "holland-america", "celebrity"],
    "northern-europe": ["princess", "holland-america", "cunard", "msc"],
    "hawaii": ["princess", "holland-america"],
}

_SEASONS = {
    "en": [("spring", "🌸", "Spring (Mar-May)"), ("summer", "☀️", "Summer (Jun-Aug)"),
           ("fall", "🍂", "Fall (Sep-Nov)"), ("winter", "❄️", "Winter (Dec-Feb)"),
           ("flex", "🗓️", "I'm flexible")],
    "es": [("spring", "🌸", "Primavera (Mar-May)"), ("summer", "☀️", "Verano (Jun-Ago)"),
           ("fall", "🍂", "Otoño (Sep-Nov)"), ("winter", "❄️", "Invierno (Dic-Feb)"),
           ("flex", "🗓️", "Soy flexible")],
}
_PARTIES = {
    "en": [("family", "👨‍👩‍👧", "Family with kids"), ("couple", "💑", "Couple"),
           ("group", "🎉", "Group / celebration"), ("solo", "🧳", "Solo or friends"),
           ("multigen", "👴", "Multi-generation")],
    "es": [("family", "👨‍👩‍👧", "Familia con niños"), ("couple", "💑", "Pareja"),
           ("group", "🎉", "Grupo / celebración"), ("solo", "🧳", "Solo o amigos"),
           ("multigen", "👴", "Multigeneracional")],
}

_TXT = {
    "en": {"kicker": "Cruise finder · 4 quick steps", "q1": "Where do you want to sail?",
           "q2": "When can you travel?", "q3": "Who's travelling?", "resultTitle": "Here's a great place to start",
           "back": "← Back", "restart": "Start over", "call": "Get your options, call now",
           "cap": "Free, no obligation, and we never take payment.",
           "linesLabel": "Lines that often sail here",
           "deployNote": "Deployments change by season, an advisor confirms which ships actually sail your dates.",
           "lead": "{region}, {when}, a great fit for {who}."},
    "es": {"kicker": "Buscador de cruceros · 4 pasos", "q1": "¿A dónde quieres navegar?",
           "q2": "¿Cuándo puedes viajar?", "q3": "¿Quién viaja?", "resultTitle": "Un excelente punto de partida",
           "back": "← Atrás", "restart": "Empezar de nuevo", "call": "Ver tus opciones, llama ahora",
           "cap": "Gratis, sin compromiso, y nunca cobramos por el viaje.",
           "linesLabel": "Líneas que suelen navegar aquí",
           "deployNote": "Los despliegues cambian por temporada, un asesor confirma qué barcos navegan en tus fechas.",
           "lead": "{region}, {when}, ideal para {who}."},
}


def _data(lang):
    regions = [{"id": d["slug"], "emo": d["emo"], "name": d["name"][lang]} for d in DESTINATIONS]
    seasons = [{"id": i, "emo": e, "name": n} for i, e, n in _SEASONS[lang]]
    parties = [{"id": i, "emo": e, "name": n} for i, e, n in _PARTIES[lang]]
    mp = {r: [{"slug": s, "name": _LN[s], "emo": _EMO[s], "href": f"/{lang}/lines/{s}.html"}
              for s in lines] for r, lines in _MAP.items()}
    t = dict(_TXT[lang])
    t["regions"] = regions
    t["seasons"] = seasons
    t["parties"] = parties
    t["map"] = mp
    t["phone"] = PHONE_HREF
    return t


def finder_card(lang):
    """The finder card only (no section wrapper). The hero places it in a dock that is a
    static column on desktop and a slide-in drawer on mobile."""
    t = _TXT[lang]
    payload = json.dumps(_data(lang), ensure_ascii=False)
    return f"""<div class="finder" id="finder">
    <div class="finder-head">
      <div class="fd-dolphin" id="fdDolphin">{DOLPHIN_SVG}</div>
      <div class="fd-headtext">
        <span class="eyebrow">{t['kicker']}</span>
        <h2 id="fdTitle">{t['q1']}</h2>
      </div>
      <div class="fd-steps" id="fdSteps"><i class="on"></i><i></i><i></i><i></i></div>
    </div>
    <div class="finder-body" id="fdBody"></div>
    <noscript><p class="fd-cap">Enable JavaScript to use the finder, or just call, we'll walk you through it.</p></noscript>
  </div>
<script>
(function(){{
  var D={payload};
  var body=document.getElementById('fdBody'),title=document.getElementById('fdTitle'),
      steps=document.getElementById('fdSteps'),dolph=document.getElementById('fdDolphin');
  if(!body) return;
  var S={{region:null,when:null,who:null,step:0}};
  var STEPS=[{{q:D.q1,key:'region',opts:D.regions}},{{q:D.q2,key:'when',opts:D.seasons}},{{q:D.q3,key:'who',opts:D.parties}}];
  function leap(){{ if(!dolph) return; dolph.classList.remove('go'); void dolph.offsetWidth; dolph.classList.add('go'); }}
  function dots(){{ if(!steps) return; var n=steps.children,i; for(i=0;i<n.length;i++){{ n[i].className = i<=S.step?'on':''; }} }}
  function nameOf(list,id){{ for(var i=0;i<list.length;i++){{ if(String(list[i].id)===String(id)) return list[i].name; }} return ''; }}
  function render(){{
    if(S.step<3){{
      var st=STEPS[S.step]; title.textContent=st.q;
      var h='<div class="fd-opts">';
      st.opts.forEach(function(o){{ h+='<button type="button" class="fd-opt" data-v="'+o.id+'"><span class="fd-emo">'+o.emo+'</span><span>'+o.name+'</span></button>'; }});
      h+='</div>';
      if(S.step>0) h+='<div class="fd-navrow"><button type="button" class="fd-back">'+D.back+'</button></div>';
      body.innerHTML=h;
      body.querySelectorAll('.fd-opt').forEach(function(b){{ b.onclick=function(){{ S[st.key]=b.getAttribute('data-v'); S.step++; leap(); render(); }}; }});
      var bk=body.querySelector('.fd-back'); if(bk) bk.onclick=function(){{ S.step--; render(); }};
    }} else {{ result(); }}
    dots();
  }}
  function result(){{
    title.textContent=D.resultTitle; leap();
    var region=nameOf(D.regions,S.region),when=nameOf(D.seasons,S.when),who=nameOf(D.parties,S.who).toLowerCase();
    var lines=D.map[S.region]||[];
    var chips=lines.map(function(l){{ return '<a class="fd-chip" href="'+l.href+'">'+l.emo+' '+l.name+'</a>'; }}).join('');
    var lead=D.lead.replace('{{who}}',who).replace('{{region}}',region).replace('{{when}}',when);
    var h='<div class="fd-result"><p class="fd-lead">'+lead+'</p>'
      +'<div class="fd-block"><span class="fd-lbl">'+D.linesLabel+'</span><div class="fd-lines">'+chips+'</div>'
      +'<p class="fd-note">'+D.deployNote+'</p></div>'
      +'<a class="btn btn-call btn-block" href="tel:'+D.phone+'" onclick="trackCall(\\'navigator\\')"><span class="ic">☎</span>'+D.call+'</a>'
      +'<p class="fd-cap">'+D.cap+'</p>'
      +'<button type="button" class="fd-restart">'+D.restart+'</button></div>';
    body.innerHTML=h;
    var r=body.querySelector('.fd-restart'); if(r) r.onclick=function(){{ S={{region:null,when:null,who:null,step:0}}; render(); }};
    if(window.dataLayer) window.dataLayer.push({{event:'navigator_complete',region:S.region,when:S.when,who:S.who}});
  }}
  render();
}})();
</script>"""
