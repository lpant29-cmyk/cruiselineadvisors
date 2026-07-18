#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the home-port navigator (embedded in home page) and directory.html."""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PORTS = json.load(open(os.path.join(ROOT, "data", "ports.json"), encoding="utf-8"))
DIR   = json.load(open(os.path.join(ROOT, "data", "directory.json"), encoding="utf-8"))

PHONE_D = "+1 (888) 555-0142"
PHONE_H = "+18885550142"


NAV_CSS = """
/* ═══ HOME PORT NAVIGATOR ═══ */
.nvg{background:#fff;border:1px solid var(--line);border-radius:22px;overflow:hidden;
  box-shadow:0 28px 64px rgba(4,18,28,.34),0 4px 14px rgba(4,18,28,.12)}
.nvghead{background:linear-gradient(120deg,var(--ink2),var(--abyss));color:#fff;padding:16px 18px}
.nvghead .step{font-size:.62rem;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:var(--aqua)}
.nvghead h2{font-family:'Fraunces',serif;color:#fff;font-size:1.15rem;margin-top:.2rem;font-weight:600}
.nvgbar{height:4px;background:rgba(255,255,255,.16);border-radius:99px;margin-top:11px;overflow:hidden}
.nvgbar i{display:block;height:100%;background:linear-gradient(90deg,var(--aqua),var(--brass));width:25%;transition:width .4s}
.nvgbody{padding:16px 18px 18px}
.nvgq{font-size:.95rem;font-weight:700;margin-bottom:11px}
.nvgsub{font-size:.8rem;color:var(--muted);margin:-6px 0 11px}
.opts{display:grid;gap:8px;max-height:340px;overflow-y:auto;padding-right:2px}
.opts.two{grid-template-columns:1fr 1fr}
.opt{display:flex;align-items:center;gap:.55em;min-height:46px;padding:11px 12px;background:var(--foam);
  border:1.5px solid var(--line);border-radius:12px;font-size:13.5px;font-weight:700;color:var(--ink);
  text-align:left;cursor:pointer;transition:.15s;width:100%}
.opt:hover{border-color:var(--lagoon);background:#fff}
.opt:active{transform:scale(.98)}
.opt:focus-visible{outline:3px solid var(--lagoon);outline-offset:2px}
.opt[aria-pressed="true"]{background:#fff;border-color:var(--brass);box-shadow:inset 0 0 0 2px rgba(217,178,90,.24)}
.opt i{font-style:normal;font-size:1.05rem;flex:none}
.opt .txt{flex:1;min-width:0}
.opt .sm{display:block;font-weight:500;font-size:.72rem;color:var(--muted);line-height:1.3}
.grp{font-size:.62rem;font-weight:900;letter-spacing:.13em;text-transform:uppercase;color:var(--lagoon);
  margin:10px 0 4px;grid-column:1/-1}
.grp:first-child{margin-top:0}
.nvgnav{display:flex;gap:10px;align-items:center;margin-top:13px}
.nvgback{background:none;border:0;color:var(--muted);font-size:.82rem;text-decoration:underline;cursor:pointer}
.nvgnext{margin-left:auto;background:var(--ink);color:#fff;border:0;font-weight:800;font-size:.88rem;
  padding:.7em 1.3em;border-radius:99px;cursor:pointer}
.nvgnext:disabled{opacity:.35;cursor:not-allowed}

/* result */
.res{padding:2px 0}
.resbadge{display:inline-block;background:linear-gradient(120deg,var(--marigold),var(--coral));color:#5A2A12;
  font-weight:900;font-size:.62rem;letter-spacing:.13em;text-transform:uppercase;padding:.4em 1em;border-radius:99px}
.res h3{font-family:'Fraunces',serif;font-size:1.3rem;margin:.6rem 0 .3rem;font-weight:600}
.res .lead{font-size:.88rem;color:var(--muted);margin-bottom:12px}
.rescard{background:var(--foam);border:1px solid var(--line);border-radius:13px;padding:13px;margin-bottom:9px}
.rescard .lbl{font-size:.6rem;font-weight:900;letter-spacing:.11em;text-transform:uppercase;color:var(--lagoon)}
.rescard b.big{display:block;font-family:'Fraunces',serif;font-size:1.08rem;margin-top:.15rem;font-weight:600}
.rescard p{font-size:.83rem;color:var(--muted);margin-top:.3rem}
.reslines{display:flex;flex-wrap:wrap;gap:6px;margin-top:.55rem}
.reslines a,.reslines span{background:#fff;border:1px solid var(--line);border-radius:99px;padding:.32em .75em;
  font-size:.76rem;font-weight:700;text-decoration:none;color:var(--ink)}
.reslines a:hover{border-color:var(--brass)}
.reswarn{background:rgba(255,107,90,.09);border:1px solid rgba(255,107,90,.32);border-radius:12px;
  padding:11px 13px;margin-bottom:9px;font-size:.8rem;color:#9C3325;display:flex;gap:.5em}
.resgood{background:rgba(62,207,201,.1);border:1px solid rgba(62,207,201,.35);border-radius:12px;
  padding:11px 13px;margin-bottom:9px;font-size:.8rem;color:#0F5A63;display:flex;gap:.5em}
.restart{background:none;border:0;color:var(--lagoon);font-size:.82rem;text-decoration:underline;
  cursor:pointer;display:block;margin:10px auto 0}
@media(min-width:1000px){
  .nvghead{padding:20px 22px}
  .nvghead h2{font-size:1.3rem}
  .nvgbody{padding:20px 22px 22px}
  .opts{max-height:400px}
  .opt{font-size:14px;min-height:50px}
}
"""


def build_navigator():
    """Returns the navigator HTML block + its JS payload."""
    groups = {}
    for p in PORTS["ports"]:
        groups.setdefault(p["group"], []).append(p)

    order = ["Florida & Southeast", "Gulf Coast", "Northeast", "West Coast",
             "Canada", "Canada & Alaska", "Caribbean", "Mexico", "Latin America"]
    ordered = [(g, groups[g]) for g in order if g in groups]

    ports_js = json.dumps({p["id"]: {
        "n": p["name"], "s": p["state"], "r": p["regions"],
        "l": [x for x in p["lines"] if x != "VERIFY"], "note": p["note"]
    } for p in PORTS["ports"]}, ensure_ascii=False)

    regions_js = json.dumps(PORTS["regions"], ensure_ascii=False)
    groups_js = json.dumps([{"g": g, "p": [x["id"] for x in ps]} for g, ps in ordered], ensure_ascii=False)
    names_js = json.dumps({l["slug"]: {"n": l["name"], "e": l["emoji"], "c": l["covered"]}
                           for l in DIR["lines"]}, ensure_ascii=False)

    block = """
<div class="nvg" id="nvg">
  <div class="nvghead">
    <div class="step" id="nvgStep">Step 1 of 4</div>
    <h2 id="nvgTitle">Let's find your cruise</h2>
    <div class="nvgbar"><i id="nvgBar"></i></div>
  </div>
  <div class="nvgbody" id="nvgBody"></div>
</div>"""

    js = """
/* ═══ HOME PORT NAVIGATOR ═══ */
var NP=%s, NR=%s, NG=%s, NL=%s;
var NVG={port:null,region:null,month:null,party:null,step:1};
var MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];

function nvgRender(){
  var body=document.getElementById('nvgBody'),
      step=document.getElementById('nvgStep'),
      title=document.getElementById('nvgTitle'),
      bar=document.getElementById('nvgBar');
  var s=NVG.step;
  bar.style.width=(s>=5?100:s*25)+'%%';
  step.textContent = s>=5 ? 'Your result' : ('Step '+s+' of 4');

  if(s===1){
    title.textContent='Where will you board?';
    var h='<p class="nvgsub">Sailing from a port you can drive to removes airfares entirely — often the single biggest saving on a cruise.</p><div class="opts">';
    NG.forEach(function(g){
      h+='<div class="grp">'+g.g+'</div>';
      g.p.forEach(function(id){var p=NP[id];
        h+='<button class="opt" data-port="'+id+'"><i>⚓</i><span class="txt">'+p.n+
           '<span class="sm">'+p.s+'</span></span></button>';});
    });
    body.innerHTML=h+'</div>';
  }

  else if(s===2){
    var p=NP[NVG.port];
    title.textContent='Where do you want to sail?';
    var h='<p class="nvgsub">These are the regions you can actually reach from <b>'+p.n+'</b>. '+p.note+'</p><div class="opts">';
    p.r.forEach(function(rid){var r=NR[rid];if(!r)return;
      h+='<button class="opt" data-region="'+rid+'"><i>🧭</i><span class="txt">'+r.name+
         '<span class="sm">'+r.note+' · peak '+r.peak+'</span></span></button>';});
    body.innerHTML=h+'</div>'+navBtns(true,false);
  }

  else if(s===3){
    title.textContent='When can you travel?';
    var r=NR[NVG.region];
    var h='<p class="nvgsub">'+r.name+' operates in the highlighted months. Anything greyed out simply isn\\'t sailing then.</p><div class="opts two">';
    for(var i=0;i<12;i++){
      var on=r.months.indexOf(i+1)>-1;
      h+='<button class="opt" data-month="'+i+'"'+(on?'':' disabled style="opacity:.35"')+'>'+
         '<i>'+(on?'✅':'—')+'</i><span class="txt">'+MONTHS[i]+
         '<span class="sm">'+(on?'Sailing':'Out of season')+'</span></span></button>';
    }
    body.innerHTML=h+'</div>'+navBtns(true,false);
  }

  else if(s===4){
    title.textContent='Who\\'s travelling?';
    var opts=[['family','👨‍👩‍👧','Family with children','Kids club age bands matter most here'],
              ['couple','💑','Couple','Adult-leaning ships, quieter decks'],
              ['group','🎊','Group or celebration','Multiple cabins, linked dining'],
              ['solo','🧳','Solo or friends','Solo cabins and share options vary by line'],
              ['multigen','👴','Multi-generation','Everyone wants something different'],
              ['access','♿','Accessibility needs','Accessible cabins sell out earliest']];
    var h='<p class="nvgsub">This changes which ships genuinely work — more than the destination does.</p><div class="opts">';
    opts.forEach(function(o){
      h+='<button class="opt" data-party="'+o[0]+'"><i>'+o[1]+'</i><span class="txt">'+o[2]+
         '<span class="sm">'+o[3]+'</span></span></button>';});
    body.innerHTML=h+'</div>'+navBtns(true,false);
  }

  else { nvgResult(); }

  body.querySelectorAll('[data-port]').forEach(function(b){b.onclick=function(){
    NVG.port=b.getAttribute('data-port');NVG.step=2;nvgRender();push('nvg_port',{port:NVG.port});};});
  body.querySelectorAll('[data-region]').forEach(function(b){b.onclick=function(){
    NVG.region=b.getAttribute('data-region');NVG.step=3;nvgRender();push('nvg_region',{region:NVG.region});};});
  body.querySelectorAll('[data-month]').forEach(function(b){b.onclick=function(){
    if(b.disabled)return;NVG.month=+b.getAttribute('data-month');NVG.step=4;nvgRender();push('nvg_month',{month:NVG.month});};});
  body.querySelectorAll('[data-party]').forEach(function(b){b.onclick=function(){
    NVG.party=b.getAttribute('data-party');NVG.step=5;nvgRender();push('nvg_party',{party:NVG.party});};});
  var back=body.querySelector('.nvgback');
  if(back)back.onclick=function(){NVG.step=Math.max(1,NVG.step-1);nvgRender();};
  var re=body.querySelector('.restart');
  if(re)re.onclick=function(){NVG={port:null,region:null,month:null,party:null,step:1};nvgRender();};
}

function navBtns(back){return '<div class="nvgnav">'+(back?'<button class="nvgback">← Back</button>':'')+'</div>';}
function push(ev,o){o=o||{};o.event=ev;window.dataLayer=window.dataLayer||[];dataLayer.push(o);}

function nvgResult(){
  var p=NP[NVG.port],r=NR[NVG.region],m=NVG.month,body=document.getElementById('nvgBody');
  document.getElementById('nvgTitle').textContent='Here\\'s what fits';

  var inSeason=r.months.indexOf(m+1)>-1;
  var lines=p.l.filter(function(sl){return NL[sl];});

  var h='<div class="res"><span class="resbadge">Based on your answers</span>'+
    '<h3>'+r.name+' from '+p.n+'</h3>'+
    '<p class="lead">Sailing in '+MONTHS[m]+', for a '+partyLabel()+'.</p>';

  if(inSeason){
    h+='<div class="resgood"><b>✓</b><span><b>'+MONTHS[m]+' works.</b> '+r.name+
       ' is in season — peak demand runs '+r.peak+'.</span></div>';
  }else{
    h+='<div class="reswarn"><b>⚠</b><span><b>'+MONTHS[m]+' is outside the season.</b> '+r.name+
       ' typically sails '+monthRange(r.months)+'. A specialist can suggest an alternative region for your dates.</span></div>';
  }

  if(r.warn==='hurricane' && m>=5 && m<=10){
    h+='<div class="reswarn"><b>⚠</b><span><b>Hurricane season.</b> The Atlantic season runs 1 June – 30 November, '+
       'most active mid-August to mid-October. Sailings still operate and are re-routed when needed — but travel insurance matters more in these months.</span></div>';
  }
  if(NVG.party==='access'){
    h+='<div class="reswarn"><b>⚠</b><span><b>Book accessible cabins early.</b> They are limited per ship and sell out '+
       'long before general inventory. Some ports also require tendering, which can be difficult with a wheelchair or scooter.</span></div>';
  }
  if(NVG.party==='family'){
    h+='<div class="resgood"><b>✓</b><span><b>Check kids club age bands.</b> They decide whether siblings are together or split '+
       'across two clubs — the most common family surprise on board.</span></div>';
  }
  if(NVG.party==='group'){
    h+='<div class="resgood"><b>✓</b><span><b>Groups need arranging in advance.</b> Linked dining, adjacent cabins and split '+
       'payments across households are phone work, not website work.</span></div>';
  }

  h+='<div class="rescard"><span class="lbl">Your departure port</span><b class="big">'+p.n+'</b>'+
     '<p>'+p.note+'</p></div>';

  h+='<div class="rescard"><span class="lbl">Lines commonly sailing this route</span>'+
     '<div class="reslines">'+ (lines.length ? lines.map(function(sl){var L=NL[sl];
       return L.c ? '<a href="lines-deep/'+sl+'.html">'+L.e+' '+L.n+' →</a>'
                  : '<span>'+L.e+' '+L.n+'</span>';}).join('')
       : '<span>Verifying current deployment</span>') +
     '</div><p style="margin-top:.5rem">Deployments change seasonally — a specialist confirms which ships are actually sailing your dates.</p></div>';

  h+='<a href="tel:'+PHONE_H+'" class="bigcall" onclick="trackCall(\\'navigator\\')">'+
     '<span>☎</span><span>Get '+r.name.split(' ')[0]+' options — call now</span></a>'+
     '<p class="cap">Advisors answer quickly. Free, no obligation, and we never take payment for travel.</p>'+
     '<button class="restart">Start over</button></div>';

  body.innerHTML=h;
  var re=body.querySelector('.restart');
  if(re)re.onclick=function(){NVG={port:null,region:null,month:null,party:null,step:1};nvgRender();};
  push('nvg_complete',{port:NVG.port,region:NVG.region,month:NVG.month,party:NVG.party});
}

function partyLabel(){return {family:'family with children',couple:'couple',group:'group',
  solo:'solo or friends trip',multigen:'multi-generation group',access:'trip with accessibility needs'}[NVG.party]||'trip';}
function monthRange(ms){var n=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  if(ms.length>=12)return 'year-round';
  return n[ms[0]-1]+'–'+n[ms[ms.length-1]-1];}
var PHONE_H='%s';
nvgRender();
""" % (ports_js, regions_js, groups_js, names_js, PHONE_H)

    return block, js


def build_directory():
    cats = {c["id"]: c for c in DIR["categories"]}
    body = ""
    for c in DIR["categories"]:
        rows = [l for l in DIR["lines"] if l["cat"] == c["id"]]
        if not rows: continue
        cards = ""
        for l in rows:
            verify = "VERIFY" in l["status"]
            link = f'lines-deep/{l["slug"]}.html' if l["covered"] else ""
            tag = ('<span class="dtag done">In-depth guide →</span>' if l["covered"]
                   else '<span class="dtag soon">Guide in progress</span>')
            warn = ('<p class="dverify">⚠ Operating status being verified — confirm before relying on this entry.</p>'
                    if verify else "")
            regions = "".join(f'<span class="drg">{html.escape(r)}</span>' for r in l["regions"])
            open_t = f'<a class="dcard" href="{link}">' if l["covered"] else '<div class="dcard">'
            close_t = "</a>" if l["covered"] else "</div>"
            cards += f"""{open_t}
        <div class="dhead"><span class="demo">{l['emoji']}</span><b>{html.escape(l['name'])}</b></div>
        <p class="done1">{html.escape(l['one'])}</p>
        <div class="drgs">{regions}</div>{warn}{tag}{close_t}"""
        body += f"""
  <section class="dsec">
    <h2>{html.escape(c['name'])}</h2>
    <p class="dblurb">{html.escape(c['blurb'])}</p>
    <div class="dgrid">{cards}</div>
  </section>"""
    return body


DIR_CSS = """
.dsec{padding:30px 0;border-bottom:1px solid var(--line)}
.dsec h2{font-size:clamp(1.4rem,4.6vw,1.9rem)}
.dblurb{color:var(--muted);font-size:.95rem;max-width:64ch;margin:.4rem 0 1rem}
.dgrid{display:grid;gap:12px}
.dcard{background:#fff;border:1px solid var(--line);border-radius:15px;padding:15px;
  text-decoration:none;display:block;transition:.18s}
a.dcard:hover{transform:translateY(-4px);box-shadow:0 14px 30px rgba(8,36,59,.14);border-color:var(--brass)}
.dhead{display:flex;align-items:center;gap:.5em}
.demo{font-size:1.3rem}
.dhead b{font-family:'Fraunces',serif;font-size:1.05rem;font-weight:600}
.done1{font-size:.85rem;color:var(--muted);margin-top:.4rem;line-height:1.5}
.drgs{display:flex;flex-wrap:wrap;gap:5px;margin-top:.6rem}
.drg{background:var(--foam);border:1px solid var(--line);border-radius:99px;padding:.22em .6em;
  font-size:.68rem;font-weight:700;color:var(--muted)}
.dtag{display:inline-block;margin-top:.7rem;font-size:.72rem;font-weight:900}
.dtag.done{color:var(--brassd)}
.dtag.soon{color:var(--muted);font-weight:700;font-style:italic}
.dverify{font-size:.72rem;color:#9C3325;background:rgba(255,107,90,.09);border-radius:8px;
  padding:.45em .6em;margin-top:.55rem}
@media(min-width:700px){.dgrid{grid-template-columns:1fr 1fr}}
@media(min-width:1000px){.dgrid{grid-template-columns:repeat(3,1fr)}}
"""

if __name__ == "__main__":
    b, j = build_navigator()
    print("navigator block:", len(b), "chars | js:", len(j))
    print("directory body:", len(build_directory()), "chars")
    print("ports:", len(PORTS["ports"]), "| lines:", len(DIR["lines"]))
