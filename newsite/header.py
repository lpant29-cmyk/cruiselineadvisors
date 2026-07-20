# -*- coding: utf-8 -*-
"""Site header — one file. Logo + dropdown-free primary nav + prominent click-to-call +
language switcher + mobile hamburger drawer. Pure CSS (no JS), so it can never throw."""
from config import PHONE_DISPLAY, PHONE_HREF
from i18n import T
from logo import lockup
from search import search_button, search_panel

# (string-key in i18n, page filename)
NAV = [
    ("nav_lines", "cruise-lines.html"),
    ("nav_compare", "compare.html"),
    ("nav_facts", "cruise-facts.html"),
    ("nav_dest", "destinations.html"),
    ("nav_guides", "guides.html"),
    ("nav_updates", "updates.html"),
]


def header(lang, page_path="index.html"):
    t = T[lang]
    other = "es" if lang == "en" else "en"
    nav_links = "".join(f'<li><a href="/{lang}/{href}">{t[key]}</a></li>' for key, href in NAV)
    return f"""<header class="hdr">
  <div class="wrap nav">
    {lockup(f'/{lang}/index.html')}
    <input type="checkbox" id="navcb" class="navcb" aria-label="{t['nav_menu']}">
    <nav class="mainnav" aria-label="Primary"><ul>{nav_links}</ul></nav>
    <div class="hdr-right">
      {search_button(lang)}
      <a class="lang" href="/{other}/{page_path}" hreflang="{other}"
         aria-label="{T[other]['lang_name']}">{t['lang_switch_code']}</a>
      <a class="call-btn" href="tel:{PHONE_HREF}" onclick="trackCall('header')">
        <span class="ic" aria-hidden="true">☎</span>
        <span class="tx"><small>{t['free_to_call']}</small><b>{PHONE_DISPLAY}</b></span>
      </a>
      <label for="navcb" class="burger" aria-label="{t['nav_menu']}"><span></span><span></span><span></span></label>
    </div>
  </div>
  {search_panel(lang)}
</header>"""
