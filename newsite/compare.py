# -*- coding: utf-8 -*-
"""Interactive comparison tool. Pick any two lines; each fact renders as a stacked CARD
(color-coded: Line A = teal, Line B = gold), readable on phones, no horizontal scroll.
Pulls from the verified data sheet (facts.py); unverified cells show a 'Not yet verified' gap
with a source link once sourced. Bilingual, guarded JS."""
import json
from config import PHONE_HREF
from data import LINES
from facts import FACTS, FACT_KEYS, LINE_FACTS, coverage, latest_verified_all
from badges import verified_stamp

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}

_T = {
    "en": {"a": "Line A", "b": "Line B", "vs": "vs", "gap": "Not yet verified",
           "cta": "These differences add up. Call and we'll sort them for your trip.",
           "call": "Get your options, call now", "flag": "facts verified from official sources"},
    "es": {"a": "Línea A", "b": "Línea B", "vs": "vs", "gap": "No verificado aún",
           "cta": "Estas diferencias suman. Llama y las resolvemos para tu viaje.",
           "call": "Ver tus opciones, llama ahora", "flag": "datos verificados de fuentes oficiales"},
}


def _payload(lang):
    vals = {}
    for slug in _NAME:
        vals[slug] = {}
        for k in FACT_KEYS:
            cell = LINE_FACTS[slug][k]
            v = cell["v"]
            vals[slug][k] = {"v": (v.get(lang, v.get("en")) if isinstance(v, dict) else v) if v else None}
    return {
        "facts": [{"key": f["key"], "label": f["label"][lang], "note": f["note"][lang],
                   "imp": bool(f.get("imp")), "fee": bool(f.get("fee"))} for f in FACTS],
        "names": _NAME, "vals": vals, "gap": _T[lang]["gap"],
    }


def line_compare_hero(lang, slug, line_name):
    """Top-of-line-page compare band with a headline naming the current line."""
    from shipcompare import compare_band
    kick = "Compare lines" if lang == "en" else "Comparar líneas"
    if lang == "en":
        h = f"Compare {line_name} with any other cruise line, and see who wins on what matters."
        sub = ("No more hopping between pages. Line them up on the money-and-complexity facts, gratuities, "
               "what's included, drink rules, cancellation, then one call gets you the best rate our partners "
               "can offer.")
    else:
        h = f"Compara {line_name} con cualquier otra línea, y ve quién gana en lo que importa."
        sub = ("Sin saltar entre páginas. Compáralas en los datos de dinero y complejidad, propinas, qué se "
               "incluye, reglas de bebidas, cancelación, luego una llamada te da la mejor tarifa que nuestros "
               "socios pueden ofrecer.")
    return compare_band(lang, kick, h, sub, compare_tool(lang, default_a=slug))


def compare_tool(lang, default_a="royal-caribbean", default_b="carnival"):
    t = _T[lang]
    done, total = coverage()
    payload = json.dumps(_payload(lang), ensure_ascii=False)
    opts_a = "".join(f'<option value="{s}"{" selected" if s==default_a else ""}>{_EMO[s]} {n}</option>' for s, n in _NAME.items())
    opts_b = "".join(f'<option value="{s}"{" selected" if s==default_b else ""}>{_EMO[s]} {n}</option>' for s, n in _NAME.items())
    return f"""<div class="cx" id="cmp">
  <div class="cx-top">
    <label class="cx-pick cx-pick-a"><span class="cx-tag">{t['a']}</span>
      <select class="cx-sel" id="cmpA" aria-label="{t['a']}">{opts_a}</select></label>
    <span class="cx-vs">{t['vs']}</span>
    <label class="cx-pick cx-pick-b"><span class="cx-tag">{t['b']}</span>
      <select class="cx-sel" id="cmpB" aria-label="{t['b']}">{opts_b}</select></label>
  </div>
  <div class="cx-flag">{verified_stamp(lang, latest_verified_all())} <span class="cx-count">{done}/{total} {t['flag']}</span></div>
  <div class="cx-cards" id="cmpBody"></div>
  <div class="cx-foot"><p>{t['cta']}</p>
    <a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('compare')"><span class="ic">☎</span>{t['call']}</a></div>
</div>
<script>(function(){{
  var D={payload};
  var A=document.getElementById('cmpA'),B=document.getElementById('cmpB'),body=document.getElementById('cmpBody');
  if(!A||!body) return;
  function nm(s){{return D.names[s]||s;}}
  function cell(slug,key){{var c=(D.vals[slug]||{{}})[key]||{{}};
    if(!c.v) return '<span class="cmp-gap">'+D.gap+'</span>';
    return c.v;}}
  function render(){{
    var a=A.value,b=B.value,na=nm(a),nb=nm(b),h='';
    D.facts.forEach(function(f){{
      h+='<div class="cx-card'+(f.imp?' imp':'')+'"><button type="button" class="cx-head"><span class="cx-fact">'+(f.imp?'<span class="cx-badge">💰</span>':'')+'<span>'+f.label+'<small>'+f.note+'</small></span></span><span class="cx-chev" aria-hidden="true">\\u25BE</span></button>'
        +'<div class="cx-vals">'
        +'<div class="cx-row cx-a"><span class="cx-line">'+na+'</span><span class="cx-val">'+cell(a,f.key)+'</span></div>'
        +'<div class="cx-row cx-b"><span class="cx-line">'+nb+'</span><span class="cx-val">'+cell(b,f.key)+'</span></div>'
        +'</div></div>';
    }});
    body.innerHTML=h;
    var hs=body.querySelectorAll('.cx-head');
    for(var i=0;i<hs.length;i++){{ hs[i].onclick=function(){{
      var c=this.parentNode, was=c.classList.contains('open');
      var op=body.querySelectorAll('.cx-card.open');
      for(var j=0;j<op.length;j++) op[j].classList.remove('open');
      if(!was) c.classList.add('open');
    }}; }}
    var fst=body.querySelector('.cx-card'); if(fst) fst.classList.add('open');
  }}
  A.onchange=render; B.onchange=render; render();
}})();</script>"""
