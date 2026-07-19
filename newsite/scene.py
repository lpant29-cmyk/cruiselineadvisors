# -*- coding: utf-8 -*-
"""Decorative animated ocean scene + wave dividers. Pure inline SVG/CSS (no external assets).
All decorative, aria-hidden. Motion is transform/opacity only and freezes under
prefers-reduced-motion (see theme.py)."""

_SHIP = """
<svg class="ship-svg" viewBox="0 0 340 190" fill="none" aria-hidden="true">
  <!-- flag + mast -->
  <rect x="206" y="8" width="3" height="26" rx="1.5" fill="#082C42"/>
  <path d="M209 11l18 5-18 6z" fill="#FF6B5A"/>
  <!-- funnels -->
  <rect x="150" y="18" width="22" height="34" rx="7" fill="#FFB23E"/>
  <rect x="150" y="18" width="22" height="10" rx="5" fill="#F08A24"/>
  <rect x="180" y="24" width="18" height="28" rx="6" fill="#12919A"/>
  <!-- top deck -->
  <rect x="120" y="40" width="86" height="26" rx="7" fill="#FFFFFF"/>
  <!-- mid deck -->
  <rect x="92" y="62" width="150" height="30" rx="8" fill="#F4FAFB"/>
  <!-- main deck -->
  <rect x="66" y="86" width="204" height="34" rx="9" fill="#FFFFFF"/>
  <!-- windows -->
  <g fill="#8FD9F0">
    <rect x="132" y="48" width="8" height="10" rx="2"/><rect x="146" y="48" width="8" height="10" rx="2"/>
    <rect x="160" y="48" width="8" height="10" rx="2"/><rect x="174" y="48" width="8" height="10" rx="2"/>
    <rect x="104" y="70" width="9" height="12" rx="2"/><rect x="121" y="70" width="9" height="12" rx="2"/>
    <rect x="138" y="70" width="9" height="12" rx="2"/><rect x="155" y="70" width="9" height="12" rx="2"/>
    <rect x="172" y="70" width="9" height="12" rx="2"/><rect x="189" y="70" width="9" height="12" rx="2"/>
    <rect x="206" y="70" width="9" height="12" rx="2"/><rect x="223" y="70" width="9" height="12" rx="2"/>
  </g>
  <!-- hull -->
  <path d="M52 118h232l-18 40a20 20 0 0 1-18 11H88a20 20 0 0 1-18-11z" fill="#0A2C42"/>
  <rect x="52" y="112" width="232" height="12" rx="6" fill="#123C5A"/>
  <!-- portholes -->
  <g fill="#FFD98A">
    <circle cx="80" cy="135" r="5"/><circle cx="104" cy="135" r="5"/><circle cx="128" cy="135" r="5"/>
    <circle cx="152" cy="135" r="5"/><circle cx="176" cy="135" r="5"/><circle cx="200" cy="135" r="5"/>
    <circle cx="224" cy="135" r="5"/><circle cx="248" cy="135" r="5"/>
  </g>
  <!-- gold trim stripe -->
  <rect x="60" y="150" width="216" height="4" rx="2" fill="#FFB23E" opacity=".85"/>
</svg>"""

_ISLAND = """
<svg class="island-svg" viewBox="0 0 200 120" fill="none" aria-hidden="true">
  <ellipse cx="100" cy="104" rx="86" ry="16" fill="#0E7C86"/>
  <path d="M40 104q60-26 120 0z" fill="#F4D9A0"/>
  <g stroke="#0B5E52" stroke-width="4" stroke-linecap="round" fill="none">
    <path d="M78 96V64"/><path d="M122 96V60"/>
  </g>
  <g fill="#1FA47A">
    <path d="M78 62q-20-10-30-2 18-2 30 8zM78 62q20-12 32-4-20-2-32 10zM78 60q-4-18 6-26-2 16-6 26z"/>
    <path d="M122 58q-22-12-34-3 20-3 34 9zM122 58q22-13 35-4-22-3-35 9zM122 56q-4-20 7-28-3 17-7 28z"/>
  </g>
</svg>"""

_WAVE = ('<svg viewBox="0 0 1440 120" preserveAspectRatio="none">'
         '<path d="M0 46C180 8 360 8 540 42s360 66 540 30 300-58 360-40v92H0z"/></svg>')


def ocean_scene():
    clouds = "".join(f'<div class="cloud c{i}"></div>' for i in (1, 2, 3))
    waves = "".join(
        f'<div class="wl wl{i}">{_WAVE}{_WAVE}</div>' for i in (1, 2, 3))
    return f"""<div class="ocean" aria-hidden="true">
  <div class="sun"></div>
  <div class="clouds">{clouds}</div>
  <div class="island">{_ISLAND}</div>
  <div class="sea"></div>
  <div class="ship">{_SHIP}</div>
  <div class="waves">{waves}</div>
</div>"""


DOLPHIN_SVG = ('<svg class="dsvg" viewBox="-8 0 148 100" fill="none" aria-hidden="true">'
  '<path d="M16 72C30 34 66 14 112 18l14-4c-5 8-11 12-18 14 9 1 17-1 23-7-3 14-15 20-31 19-13 14-45 24-84 22z" fill="#2C7A93"/>'
  '<path d="M30 74c26 0 50-9 61-23-5 12-16 18-30 19-11 12-40 20-63 20 12-3 23-8 32-16z" fill="#BFE9F0" opacity=".55"/>'
  '<path d="M58 24c8-15 20-18 30-14-8 4-13 11-15 22z" fill="#215E72"/>'
  '<path d="M74 48c-4 10-3 18 3 24-10-3-15-13-12-24z" fill="#215E72"/>'
  '<path d="M16 72c-9-2-16-8-19-16 10 1 17 6 23 14zM16 72c-8 5-17 7-24 4 7-6 16-8 24-8z" fill="#215E72"/>'
  '<circle cx="106" cy="30" r="2.6" fill="#0A2C42"/></svg>')


def hero_dolphin():
    """A dolphin leaping out of the hero waves (CSS loop)."""
    return f'<div class="dolphin-hero" aria-hidden="true">{DOLPHIN_SVG}</div>'


MINISHIP_SVG = ('<svg class="mship" viewBox="0 0 40 40" fill="none" aria-hidden="true">'
  '<path d="M6 24h28l-4 8a4 4 0 0 1-3.6 2.2H13.6A4 4 0 0 1 10 32z" fill="#0A2C42"/>'
  '<rect x="10" y="15" width="20" height="8" rx="2.5" fill="#fff"/>'
  '<rect x="14.5" y="9.5" width="11" height="6.5" rx="2" fill="#F1FAFB"/>'
  '<rect x="18.5" y="5" width="4" height="6" rx="1.6" fill="#FFB23E"/>'
  '<g fill="#8FD9F0"><rect x="12" y="17" width="3" height="4" rx="1"/><rect x="18.5" y="17" width="3" height="4" rx="1"/>'
  '<rect x="25" y="17" width="3" height="4" rx="1"/></g></svg>')


def scroll_companions():
    """As you scroll: a cruise ship sails down a spine (desktop), and a dolphin leaps
    across (mobile). One guarded scroll handler drives both; both freeze on reduced-motion."""
    return (
        '<div class="voyage" id="voyage" aria-hidden="true">'
        '<div class="voyage-line"><span class="voyage-fill" id="voyageFill"></span></div>'
        '<div class="voyage-ship" id="voyageShip">' + MINISHIP_SVG + '</div></div>'
        '<div class="dolphin-scroll" id="dolphin" aria-hidden="true">' + DOLPHIN_SVG + '</div>'
        '<script>(function(){'
        'var dol=document.getElementById("dolphin"),voy=document.getElementById("voyage"),'
        'fill=document.getElementById("voyageFill"),ship=document.getElementById("voyageShip");'
        'if(window.matchMedia&&matchMedia("(prefers-reduced-motion:reduce)").matches){'
        'if(dol)dol.style.display="none";if(voy)voy.style.display="none";return;}'
        'var vw=window.innerWidth,ticking=false;'
        'function u(){ticking=false;var de=document.documentElement,max=de.scrollHeight-window.innerHeight,'
        'p=max>0?window.scrollY/max:0;if(p<0)p=0;if(p>1)p=1;'
        'if(voy&&ship&&fill){var h=voy.clientHeight;fill.style.height=(p*100)+"%";'
        'ship.style.transform="translateY("+(p*(h-34))+"px)";}'
        'if(dol){var cyc=3,seg=p*cyc,x=seg%1,dir=(Math.floor(seg)%2===0)?1:-1,px=dir>0?x:1-x,arc=Math.sin(x*Math.PI);'
        'dol.style.transform="translate("+(px*(vw-90))+"px,"+(-arc*150)+"px) scaleX("+dir+") rotate("+(dir*(0.5-x)*44)+"deg)";}}'
        'function onS(){if(!ticking){ticking=true;requestAnimationFrame(u);}}'
        'window.addEventListener("scroll",onS,{passive:true});'
        'window.addEventListener("resize",function(){vw=window.innerWidth;u();});u();})();</script>')


def wave_divider(fill="white", prev="#12919A"):
    """A wave-shaped transition at the top of a section: the wave (filled `fill` = this
    section's colour) rises over the previous section's colour (`prev`)."""
    return (f'<div class="wdiv wdiv-{fill}" style="background:{prev}" aria-hidden="true">'
            '<svg viewBox="0 0 1440 90" preserveAspectRatio="none">'
            '<path d="M0 40C240 78 480 78 720 48S1200 6 1440 34V90H0z"/></svg></div>')
