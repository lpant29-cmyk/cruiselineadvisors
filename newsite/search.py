# -*- coding: utf-8 -*-
"""Site-wide search.

Builds a small client-side index over every page type — hubs, cruise lines, ships, cruise-fact
topics, destinations, guides and updates — from the SAME data modules the pages are generated from,
so the search can never drift from what's published. The index is embedded once per page as JSON and
matched by a self-contained IIFE with a null guard on line one (CLAUDE.md pitfall 1), so it can never
throw and kill other scripts. The Python matcher in tests/test_search.py mirrors the JS scoring
exactly, so a test failure means the two have drifted."""
import json

from data import LINES, DESTINATIONS
from facts import FACTS
from ships import all_ships, slugify
from pages import GUIDES
from updates import all_updates
from i18n import T
from metasearch import ship_regions, _REGIONS

# region id -> display name, so a ship's own (itinerary-derived) regions become search keywords —
# same source of truth the finder uses, so "alaska" surfaces the ships that actually sail it.
_REGION_NAME = {r["id"]: r["name"] for r in _REGIONS}

# type labels shown under each result
_TYPE = {
    "en": {"page": "Section", "line": "Cruise line", "ship": "Ship", "fact": "Cruise fact",
           "dest": "Destination", "guide": "Guide", "update": "Update"},
    "es": {"page": "Sección", "line": "Línea de crucero", "ship": "Barco", "fact": "Dato de crucero",
           "dest": "Destino", "guide": "Guía", "update": "Novedad"},
}

_UI = {
    "en": {"open": "Search", "ph": "Search ships, lines, destinations…", "no": "No matches — try a line, ship or destination name.",
           "hint": "Type to search the whole site"},
    "es": {"open": "Buscar", "ph": "Busca barcos, líneas, destinos…", "no": "Sin resultados — prueba con una línea, barco o destino.",
           "hint": "Escribe para buscar en todo el sitio"},
}


def _e(t, sub, u, kws, emo):
    """One index entry. `t` title, `sub` type label line, `u` url, `k` searchable keyword blob, `e` emoji."""
    return {"t": t, "s": sub, "u": u, "k": " ".join(x for x in kws if x).lower(), "e": emo}


def build_index(lang):
    ty = _TYPE[lang]
    idx = []

    # Hub / section pages
    hubs = [
        (T[lang]["nav_lines"], "cruise-lines", "🚢", ["cruise lines", "brands", "all lines"]),
        (T[lang]["nav_compare"], "compare", "🧭", ["find a cruise", "finder", "compare ships", "search cruises"]),
        (T[lang]["nav_facts"], "cruise-facts", "🧾", ["fees", "costs", "money", "fine print"]),
        (T[lang]["nav_dest"], "destinations", "🗺️", ["where to cruise", "regions", "itineraries"]),
        (T[lang]["nav_guides"], "guides", "📖", ["planning", "how to", "advice"]),
        (T[lang]["nav_updates"], "updates", "📰", ["news", "policy", "changes"]),
    ]
    for title, slug, emo, kws in hubs:
        idx.append(_e(title, ty["page"], f"/{lang}/{slug}/", [title] + kws, emo))

    # Cruise lines
    line_by_slug = {L["slug"]: L for L in LINES}
    for L in LINES:
        idx.append(_e(L["name"], ty["line"], f"/{lang}/lines/{L['slug']}/",
                      [L["name"], L["cat"][lang], L["tag"][lang], "cruise line"], L["emo"]))

    # Ships
    for line_slug, s in all_ships():
        L = line_by_slug.get(line_slug)
        lname = L["name"] if L else line_slug
        emo = L["emo"] if L else "🛳️"
        regs = [_REGION_NAME.get(r, "") for r in ship_regions(line_slug, s.get("exp") or {})]
        idx.append(_e(s["name"], f'{lname} · {ty["ship"]}',
                      f"/{lang}/lines/{line_slug}/ships/{slugify(s['name'])}/",
                      [s["name"], lname, s.get("cls") or "", "ship"] + regs, emo))

    # Cruise-fact topics
    for f in FACTS:
        idx.append(_e(f["label"][lang], ty["fact"], f"/{lang}/cruise-facts/",
                      [f["label"][lang], f["note"][lang], f["key"]], "🧾"))

    # Destinations
    for d in DESTINATIONS:
        idx.append(_e(d["name"][lang], ty["dest"], f"/{lang}/destinations/{d['slug']}/",
                      [d["name"]["en"], d["name"]["es"], "destination region"], d["emo"]))

    # Guides
    for g in GUIDES:
        idx.append(_e(g["t"][lang], ty["guide"], f"/{lang}/guides/{g['slug']}/",
                      [g["t"][lang], g["d"][lang], "guide"], g.get("emo", "📖")))

    # Updates
    for u in all_updates():
        idx.append(_e(u["title"][lang], ty["update"], f"/{lang}/updates/{u['slug']}/",
                      [u["title"][lang], "update news policy"], "📰"))

    return idx


def search_button(lang):
    """Icon button that lives in the header's right cluster and opens the search overlay."""
    return (f'<button type="button" class="sx-open" id="sxOpen" aria-label="{_UI[lang]["open"]}" '
            f'aria-expanded="false" aria-controls="sxPanel">'
            f'<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" '
            f'stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/>'
            f'<line x1="16.5" y1="16.5" x2="21" y2="21"/></svg></button>')


def search_panel(lang):
    """The overlay: backdrop + input + results list + the embedded index + the matcher IIFE."""
    ui = _UI[lang]
    data = json.dumps(build_index(lang), ensure_ascii=False, separators=(",", ":"))
    return f"""<div class="sx-wrap" id="sxPanel" hidden>
  <div class="sx-back" id="sxBack"></div>
  <div class="sx-box" role="dialog" aria-modal="true" aria-label="{ui['open']}">
    <div class="sx-in">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
      <input type="search" id="sxq" class="sx-q" placeholder="{ui['ph']}" autocomplete="off" spellcheck="false" aria-label="{ui['ph']}" aria-controls="sxList" aria-expanded="false" role="combobox">
      <button type="button" class="sx-x" id="sxClose" aria-label="Close">&times;</button>
    </div>
    <ul class="sx-list" id="sxList" role="listbox"></ul>
    <p class="sx-hint" id="sxHint">{ui['hint']}</p>
  </div>
</div>
<script type="application/json" id="sxIdx">{data}</script>
<script>
(function(){{
  var panel=document.getElementById('sxPanel'); if(!panel) return;
  var open=document.getElementById('sxOpen'), close=document.getElementById('sxClose'),
      back=document.getElementById('sxBack'), q=document.getElementById('sxq'),
      list=document.getElementById('sxList'), hint=document.getElementById('sxHint'),
      raw=document.getElementById('sxIdx');
  var NO={json.dumps(ui['no'])};
  var IDX=[]; try{{ IDX=JSON.parse(raw.textContent)||[]; }}catch(e){{ return; }}
  for(var i=0;i<IDX.length;i++){{ IDX[i]._t=(IDX[i].t||'').toLowerCase(); }}
  var sel=-1, rows=[];
  function score(e,ql,toks){{
    var t=e._t, k=e.k||'';
    if(t===ql) return 1000;
    if(t.indexOf(ql)===0) return 600-t.length*0.1;
    var s=0, all=true;
    if(t.indexOf(ql)>=0) s+=200;
    for(var i=0;i<toks.length;i++){{ var tk=toks[i];
      if(t.indexOf(tk)>=0) s+=40; else if(k.indexOf(tk)>=0) s+=15; else all=false; }}
    if(!all) return 0;
    return s - t.length*0.1;
  }}
  function esc(x){{ return (x||'').replace(/[&<>\"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}}[c];}}); }}
  function run(){{
    var v=(q.value||'').trim().toLowerCase();
    list.innerHTML=''; rows=[]; sel=-1;
    q.setAttribute('aria-expanded', v?'true':'false');
    if(!v){{ hint.style.display='block'; return; }}
    hint.style.display='none';
    var toks=v.split(/\\s+/).filter(Boolean);
    var scored=[];
    for(var i=0;i<IDX.length;i++){{ var sc=score(IDX[i],v,toks); if(sc>0) scored.push([sc,IDX[i]]); }}
    scored.sort(function(a,b){{ return b[0]-a[0]; }});
    scored=scored.slice(0,8);
    if(!scored.length){{ list.innerHTML='<li class="sx-none">'+esc(NO)+'</li>'; return; }}
    for(var j=0;j<scored.length;j++){{ (function(e){{
      var li=document.createElement('li'); li.className='sx-row'; li.setAttribute('role','option');
      li.innerHTML='<a href="'+e.u+'"><span class="sx-emo" aria-hidden="true">'+esc(e.e)+'</span>'
        +'<span class="sx-tx"><span class="sx-t">'+esc(e.t)+'</span>'
        +'<span class="sx-s">'+esc(e.s)+'</span></span></a>';
      list.appendChild(li); rows.push(li);
    }})(scored[j][1]); }}
  }}
  function move(d){{ if(!rows.length) return; sel=(sel+d+rows.length)%rows.length;
    for(var i=0;i<rows.length;i++) rows[i].classList.toggle('on',i===sel);
    rows[sel].scrollIntoView({{block:'nearest'}}); }}
  function go(){{ var r=rows[sel<0?0:sel]; if(r){{ var a=r.querySelector('a'); if(a) location.href=a.getAttribute('href'); }} }}
  function show(){{ panel.hidden=false; document.body.style.overflow='hidden';
    open.setAttribute('aria-expanded','true'); setTimeout(function(){{q.focus();}},30); }}
  function hide(){{ panel.hidden=true; document.body.style.overflow=''; open.setAttribute('aria-expanded','false'); q.value=''; run(); }}
  open.addEventListener('click',show);
  if(close) close.addEventListener('click',hide);
  if(back) back.addEventListener('click',hide);
  q.addEventListener('input',run);
  q.addEventListener('keydown',function(ev){{
    if(ev.key==='ArrowDown'){{ev.preventDefault();move(1);}}
    else if(ev.key==='ArrowUp'){{ev.preventDefault();move(-1);}}
    else if(ev.key==='Enter'){{ev.preventDefault();go();}}
    else if(ev.key==='Escape'){{hide();}}
  }});
  document.addEventListener('keydown',function(ev){{
    if((ev.key==='/'||((ev.metaKey||ev.ctrlKey)&&ev.key==='k')) && panel.hidden){{
      var tag=(document.activeElement&&document.activeElement.tagName)||'';
      if(tag!=='INPUT'&&tag!=='TEXTAREA'){{ ev.preventDefault(); show(); }}
    }}
  }});
}})();
</script>"""
