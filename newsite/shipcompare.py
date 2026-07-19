# -*- coding: utf-8 -*-
"""Ship-vs-ship comparison. Pick any two ships (grouped by line) and see their verified specs
side by side — class, year, guests, tonnage, features. Same card UI as the line compare tool
(A = teal, B = gold), mobile-first, guarded IIFE JS. Unverified specs show a 'Not yet verified'
gap. Data comes from ships.py (official-sourced). NO PRICES."""
import json
from config import PHONE_HREF
from data import LINES
from ships import all_ships, slugify, SHIPS
from badges import verified_stamp


def _latest_roster_date():
    ds = [b.get("verified") for b in SHIPS.values() if b.get("verified")]
    return max(ds) if ds else None

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}

_T = {
    "en": {"a": "Ship A", "b": "Ship B", "vs": "vs", "gap": "Not yet verified",
           "rows": [("class", "Ship class"), ("year", "Entered service"),
                    ("guests", "Guests"), ("tonnage", "Gross tonnage"), ("features", "On board")],
           "line": "Cruise line",
           "cta": "The right ship depends on your dates, party and budget. Call and we'll match you.",
           "call": "Find the right ship — call now",
           "flag": "specs verified from official cruise-line sources"},
    "es": {"a": "Barco A", "b": "Barco B", "vs": "vs", "gap": "No verificado aún",
           "rows": [("class", "Clase"), ("year", "En servicio desde"),
                    ("guests", "Huéspedes"), ("tonnage", "Tonelaje bruto"), ("features", "A bordo")],
           "line": "Línea",
           "cta": "El barco correcto depende de tus fechas, grupo y presupuesto. Llama y te emparejamos.",
           "call": "Encuentra el barco ideal — llama ahora",
           "flag": "datos verificados de sitios oficiales de las líneas"},
}


def _sid(line_slug, name):
    return f"{line_slug}::{slugify(name)}"


def _payload(lang):
    ships = []
    for line_slug, s in all_ships():
        exp = s.get("exp") or {}
        acts = exp.get("activities")
        ships.append({
            "id": _sid(line_slug, s["name"]),
            "line": _NAME.get(line_slug, line_slug),
            "name": s["name"],
            "class": s.get("class"),
            "year": s.get("year"),
            "guests": s.get("guests"),
            "tonnage": s.get("tonnage"),
            "features": [f for f in s.get("features", []) if f],
            "dine": len(exp.get("dining") or []),
            "acts": len(acts) if isinstance(acts, list) else 0,
        })
    ships.sort(key=lambda x: (x["line"], x["name"]))
    vd = ({"h": "Which should you pick?", "take": "Our take",
           "newer": "newer", "bigger": "bigger — more space & more to do",
           "moredine": "more dining choice",
           "consider": "Prefer a smaller, calmer, easier-to-navigate ship? Go with {x}.",
           "tie": "These two are closely matched — the right one really comes down to your dates, party and budget.",
           "close": "Either way, tell us your dates and party and we'll match the right ship — and the best rate our partners can offer."}
          if lang == "en" else
          {"h": "¿Cuál elegir?", "take": "Nuestra recomendación",
           "newer": "más nuevo", "bigger": "más grande — más espacio y más que hacer",
           "moredine": "más opciones de comida",
           "consider": "¿Prefieres un barco más pequeño, tranquilo y fácil de recorrer? Elige {x}.",
           "tie": "Están muy parejos — la elección depende de tus fechas, grupo y presupuesto.",
           "close": "En cualquier caso, dinos tus fechas y grupo y encontramos el barco ideal — y la mejor tarifa que nuestros socios pueden ofrecer."})
    return {"ships": ships, "gap": _T[lang]["gap"],
            "rows": [{"k": k, "label": lbl} for k, lbl in _T[lang]["rows"]],
            "lineLabel": _T[lang]["line"], "vd": vd}


def has_ship_compare():
    """True once at least two ships are loaded (else the tool is pointless)."""
    return sum(1 for _ in all_ships()) >= 2


def ship_compare_tool(lang, default_a=None, default_b=None):
    t = _T[lang]
    data = _payload(lang)
    ships = data["ships"]
    if len(ships) < 2:
        return ""
    ids = [s["id"] for s in ships]
    da = default_a if default_a in ids else ids[0]
    db = default_b if default_b in ids else next((i for i in ids if i != da), ids[0])

    # options grouped by line
    def opts(sel):
        html, cur = "", None
        for s in ships:
            if s["line"] != cur:
                if cur is not None:
                    html += "</optgroup>"
                html += f'<optgroup label="{s["line"]}">'
                cur = s["line"]
            html += f'<option value="{s["id"]}"{" selected" if s["id"]==sel else ""}>{s["name"]}</option>'
        if cur is not None:
            html += "</optgroup>"
        return html

    payload = json.dumps(data, ensure_ascii=False)
    return f"""<div class="cx" id="scmp">
  <div class="cx-top">
    <label class="cx-pick cx-pick-a"><span class="cx-tag">{t['a']}</span>
      <select class="cx-sel" id="scmpA" aria-label="{t['a']}">{opts(da)}</select></label>
    <span class="cx-vs">{t['vs']}</span>
    <label class="cx-pick cx-pick-b"><span class="cx-tag">{t['b']}</span>
      <select class="cx-sel" id="scmpB" aria-label="{t['b']}">{opts(db)}</select></label>
  </div>
  <div class="cx-flag">{verified_stamp(lang, _latest_roster_date())} <span class="cx-count">{t['flag']}</span></div>
  <div class="cx-cards" id="scmpBody"></div>
  <div class="cx-verdict" id="scmpVerdict"></div>
  <div class="cx-foot"><p>{t['cta']}</p>
    <a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall('ship-compare')"><span class="ic">☎</span>{t['call']}</a></div>
</div>
<script>(function(){{
  var D={payload};
  var A=document.getElementById('scmpA'),B=document.getElementById('scmpB'),body=document.getElementById('scmpBody');
  if(!A||!B||!body) return;
  var byId={{}}; D.ships.forEach(function(s){{byId[s.id]=s;}});
  function num(n){{return (n===null||n===undefined||n==='')?null:String(n).replace(/\\B(?=(\\d{{3}})+(?!\\d))/g,',');}}
  function fmt(s,k){{
    if(!s) return null;
    if(k==='features') return (s.features&&s.features.length)?s.features.join(' · '):null;
    if(k==='guests'||k==='tonnage') return num(s[k]);
    return (s[k]===null||s[k]===undefined||s[k]==='')?null:String(s[k]);
  }}
  function val(s,k){{var v=fmt(s,k); return v?v:'<span class="cmp-gap">'+D.gap+'</span>';}}
  function num2(n){{return num(n);}}
  function verdict(a,b){{
    var V=D.vd, vd=document.getElementById('scmpVerdict');
    if(!vd) return;
    if(!a||!b){{vd.innerHTML='';return;}}
    var ra=[],rb=[];
    if(a.year&&b.year){{ if(a.year>b.year)ra.push(V.newer+' ('+a.year+')'); else if(b.year>a.year)rb.push(V.newer+' ('+b.year+')'); }}
    if(a.guests&&b.guests){{ if(a.guests>b.guests)ra.push(V.bigger); else if(b.guests>a.guests)rb.push(V.bigger); }}
    if(a.dine&&b.dine){{ if(a.dine>b.dine)ra.push(V.moredine+' ('+a.dine+' vs '+b.dine+')'); else if(b.dine>a.dine)rb.push(V.moredine+' ('+b.dine+' vs '+a.dine+')'); }}
    var body;
    if(ra.length===0&&rb.length===0){{ body='<p>'+V.tie+'</p>'; }}
    else {{
      var win=ra.length>=rb.length?a:b, lose=win===a?b:a, wr=win===a?ra:rb;
      body='<p><span class="cx-vwin">'+V.take+': '+win.name+'</span> — '+wr.join(', ')+'. '+V.consider.replace('{{x}}',lose.name)+'</p>';
    }}
    vd.innerHTML='<div class="cx-vhead">★ '+V.h+'</div>'+body+'<p class="cx-vclose">'+V.close+'</p>';
  }}
  function render(){{
    var a=byId[A.value],b=byId[B.value],h='';
    // line row first
    h+=card(D.lineLabel,'',a?a.line:'',b?b.line:'');
    D.rows.forEach(function(r){{ h+=card(r.label,'',val(a,r.k),val(b,r.k)); }});
    body.innerHTML=h;
    verdict(a,b);
  }}
  function card(label,note,av,bv){{
    return '<div class="cx-card"><div class="cx-fact"><span>'+label+(note?'<small>'+note+'</small>':'')+'</span></div>'
      +'<div class="cx-vals">'
      +'<div class="cx-row cx-a"><span class="cx-line">'+(byId[A.value]?byId[A.value].name:'')+'</span><span class="cx-val">'+av+'</span></div>'
      +'<div class="cx-row cx-b"><span class="cx-line">'+(byId[B.value]?byId[B.value].name:'')+'</span><span class="cx-val">'+bv+'</span></div>'
      +'</div></div>';
  }}
  A.onchange=render; B.onchange=render; render();
}})();</script>"""
