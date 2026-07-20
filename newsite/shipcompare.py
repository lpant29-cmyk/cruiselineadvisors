# -*- coding: utf-8 -*-
"""Ship-vs-ship comparison. Pick any two ships (grouped by line) and see their verified specs
side by side — class, year, guests, tonnage, features. Same card UI as the line compare tool
(A = teal, B = gold), mobile-first, guarded IIFE JS. Unverified specs show a 'Not yet verified'
gap. Data comes from ships.py (official-sourced). NO PRICES."""
import json
from config import PHONE_HREF, PHONE_DISPLAY
from data import LINES
from ships import all_ships, slugify, SHIPS, kids_family_display, _kids_is_gap
from badges import verified_stamp
from facts import LINE_FACTS

# Decision rows, grouped. Line-policy rows pull from the verified 12-fact sheet (the confusing
# money stuff people actually agonise over); ship rows come from specs + enrichment.
_ROWS = {
    "en": [
        {"group": "On board this ship"},
        {"k": "who", "label": "Best for"}, {"k": "route", "label": "Where it sails"},
        {"k": "class", "label": "Ship class"}, {"k": "year", "label": "Entered service"},
        {"k": "guests", "label": "Guests"}, {"k": "tonnage", "label": "Gross tonnage"},
        {"k": "dine", "label": "Places to eat"}, {"k": "acts", "label": "Things to do"},
        {"k": "kids", "label": "Kids & families"},
        {"group": "Cost & the fine print (line policy)"},
        {"k": "gratuities", "label": "Daily gratuities"},
        {"k": "included", "label": "What's included vs extra"},
        {"k": "drink_pkg", "label": "Drink-package rule"},
        {"k": "wifi", "label": "Wi-Fi"},
        {"k": "deposit", "label": "Deposit & final payment"},
        {"k": "cancel", "label": "Cancellation & refunds"},
        {"k": "solo", "label": "Solo traveller supplement"},
    ],
    "es": [
        {"group": "A bordo de este barco"},
        {"k": "who", "label": "Ideal para"}, {"k": "route", "label": "Dónde navega"},
        {"k": "class", "label": "Clase"}, {"k": "year", "label": "En servicio desde"},
        {"k": "guests", "label": "Huéspedes"}, {"k": "tonnage", "label": "Tonelaje bruto"},
        {"k": "dine", "label": "Dónde comer"}, {"k": "acts", "label": "Qué hacer"},
        {"k": "kids", "label": "Niños y familias"},
        {"group": "Costo y la letra pequeña (política de la línea)"},
        {"k": "gratuities", "label": "Propinas diarias"},
        {"k": "included", "label": "Qué se incluye vs extra"},
        {"k": "drink_pkg", "label": "Regla del paquete de bebidas"},
        {"k": "wifi", "label": "Wi-Fi"},
        {"k": "deposit", "label": "Depósito y pago final"},
        {"k": "cancel", "label": "Cancelación y reembolsos"},
        {"k": "solo", "label": "Suplemento para viajero solo"},
    ],
}
_FACT_KEYS = ("gratuities", "included", "drink_pkg", "wifi", "deposit", "cancel", "solo")

def compare_band(lang, kick, headline, sub, tool_html):
    """Shared top-of-page compare band: headline + call on the left, a compare tool on the right
    (desktop 2-col); stacks on mobile. Reused by ship pages and line pages."""
    call = "Call now" if lang == "en" else "Llama ahora"
    return (f'<section class="cmphero"><div class="wrap"><div class="cmphero-grid">'
            f'<div class="cmphero-left"><span class="eyebrow">{kick}</span>'
            f'<h2>{headline}</h2><p class="cmphero-sub">{sub}</p>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'cmphero\')">'
            f'<span class="ic" aria-hidden="true">☎</span>{call} · {PHONE_DISPLAY}</a></div>'
            f'<div class="cmphero-right">{tool_html}</div>'
            f'</div></div></section>')


def compare_hero(lang, default_a=None, ship_name=None):
    """Ship-page compare band with a headline that names the current ship."""
    if not has_ship_compare():
        return ""
    kick = "Compare ships" if lang == "en" else "Comparar barcos"
    nm = ship_name or ("this ship" if lang == "en" else "este barco")
    if lang == "en":
        h = f"Compare {nm} with any other ship — and find the winner in seconds."
        sub = ("No more digging through hundreds of pages. Line it up against any ship, from any line, on "
               "what actually matters — size, dining, what's included and the fine print. Then one call gets "
               "you the best rate our partners can offer.")
    else:
        h = f"Compara {nm} con cualquier otro barco — y encuentra al ganador en segundos."
        sub = ("Sin revisar cientos de páginas. Compáralo con cualquier barco, de cualquier línea, en lo que "
               "importa — tamaño, restaurantes, qué se incluye y la letra pequeña. Luego una llamada te da la "
               "mejor tarifa que nuestros socios pueden ofrecer.")
    return compare_band(lang, kick, h, sub, ship_compare_tool(lang, default_a=default_a))


def _latest_roster_date():
    ds = [b.get("verified") for b in SHIPS.values() if b.get("verified")]
    return max(ds) if ds else None

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}

_T = {
    "en": {"a": "Ship A", "b": "Ship B", "vs": "vs", "gap": "Not yet verified",
           "rows": [("class", "Ship class"), ("year", "Entered service"),
                    ("guests", "Guests"), ("tonnage", "Gross tonnage"),
                    ("who", "Best for"), ("route", "Where it sails")],
           "line": "Cruise line",
           "cta": "The right ship depends on your dates, party and budget. Call and we'll match you.",
           "call": "Find the right ship — call now",
           "flag": "specs verified from official cruise-line sources"},
    "es": {"a": "Barco A", "b": "Barco B", "vs": "vs", "gap": "No verificado aún",
           "rows": [("class", "Clase"), ("year", "En servicio desde"),
                    ("guests", "Huéspedes"), ("tonnage", "Tonelaje bruto"),
                    ("who", "Ideal para"), ("route", "Dónde navega")],
           "line": "Línea",
           "cta": "El barco correcto depende de tus fechas, grupo y presupuesto. Llama y te emparejamos.",
           "call": "Encuentra el barco ideal — llama ahora",
           "flag": "datos verificados de sitios oficiales de las líneas"},
}


def _sid(line_slug, name):
    return f"{line_slug}::{slugify(name)}"


def _kids(kf, lang="en"):
    """Compact kids/family summary from a ship's enriched kids_family (string or list of {name,desc})."""
    if not kf:
        return None
    if isinstance(kf, list):
        n = [x.get("name") if isinstance(x, dict) else x for x in kf
             if (isinstance(x, dict) and x.get("name")) or isinstance(x, str)]
        return " · ".join(str(x) for x in n if x) or None
    if _kids_is_gap(kf):
        return kids_family_display(kf, lang, short=True)
    return kf if isinstance(kf, str) else None


def _payload(lang):
    ships = []
    for line_slug, s in all_ships():
        exp = s.get("exp") or {}
        acts = exp.get("activities")
        lf = LINE_FACTS.get(line_slug, {})

        def fv(key):
            c = lf.get(key, {})
            v = c.get("v")
            if not v:
                return None
            return v.get(lang, v.get("en")) if isinstance(v, dict) else v

        row = {
            "id": _sid(line_slug, s["name"]),
            "line": _NAME.get(line_slug, line_slug),
            "name": s["name"],
            "class": s.get("class"),
            "year": s.get("year"),
            "guests": s.get("guests"),
            "tonnage": s.get("tonnage"),
            "who": exp.get("who_for"),
            "route": exp.get("deploy_note"),
            "kids": _kids(exp.get("kids_family"), lang),
            "dine": len(exp.get("dining") or []),
            "acts": len(acts) if isinstance(acts, list) else 0,
        }
        for k in _FACT_KEYS:
            row[k] = fv(k)
        ships.append(row)
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
    return {"ships": ships, "gap": _T[lang]["gap"], "rows": _ROWS[lang],
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
    if(k==='guests'||k==='tonnage') return num(s[k]);
    if(k==='dine'||k==='acts') return s[k]>0?String(s[k]):null;
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
    h+=card(D.lineLabel,'',a?a.line:'',b?b.line:'');
    D.rows.forEach(function(r){{
      if(r.group){{ h+='<div class="cx-group">'+r.group+'</div>'; return; }}
      h+=card(r.label,'',val(a,r.k),val(b,r.k));
    }});
    body.innerHTML=h;
    var hs=body.querySelectorAll('.cx-head');
    for(var i=0;i<hs.length;i++){{ hs[i].onclick=function(){{
      var c=this.parentNode, was=c.classList.contains('open');
      var op=body.querySelectorAll('.cx-card.open');
      for(var j=0;j<op.length;j++) op[j].classList.remove('open');
      if(!was) c.classList.add('open');
    }}; }}
    var f=body.querySelector('.cx-card'); if(f) f.classList.add('open');
    verdict(a,b);
  }}
  function card(label,note,av,bv){{
    return '<div class="cx-card"><button type="button" class="cx-head"><span class="cx-fact"><span>'+label+(note?'<small>'+note+'</small>':'')+'</span></span><span class="cx-chev" aria-hidden="true">\\u25BE</span></button>'
      +'<div class="cx-vals">'
      +'<div class="cx-row cx-a"><span class="cx-line">'+(byId[A.value]?byId[A.value].name:'')+'</span><span class="cx-val">'+av+'</span></div>'
      +'<div class="cx-row cx-b"><span class="cx-line">'+(byId[B.value]?byId[B.value].name:'')+'</span><span class="cx-val">'+bv+'</span></div>'
      +'</div></div>';
  }}
  A.onchange=render; B.onchange=render; render();
}})();</script>"""
