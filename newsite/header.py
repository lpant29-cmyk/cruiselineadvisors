# -*- coding: utf-8 -*-
"""Site header — one file. Logo + dropdown-free primary nav + prominent click-to-call +
language switcher + mobile hamburger drawer. Pure CSS (no JS), so it can never throw."""
from config import PHONE_DISPLAY, PHONE_HREF
from i18n import T
from logo import lockup
from search import search_button, search_panel
from data import LINES

# (string-key in i18n, page filename)
NAV = [
    ("nav_lines", "cruise-lines.html"),
    ("nav_compare", "compare.html"),
    ("nav_facts", "cruise-facts.html"),
    ("nav_dest", "destinations.html"),
    ("nav_guides", "guides.html"),
    ("nav_updates", "updates.html"),
]


def _lines_submenu(lang, t):
    """Dropdown under 'Cruise Lines': the hub, the full ship directory, then each line.
    Pure CSS (hover/focus-within on desktop, expanded in the mobile drawer) — no JS."""
    items = [
        f'<li><a href="/{lang}/cruise-lines/">{t["nav_all_lines"]}</a></li>',
        f'<li><a href="/{lang}/ships/"><span aria-hidden="true">🚢</span> {t["nav_ships_dir"]}</a></li>',
        '<li class="sub-sep" aria-hidden="true"></li>',
    ]
    items += [f'<li><a href="/{lang}/lines/{L["slug"]}/">{L["emo"]} {L["name"]}</a></li>' for L in LINES]
    return f'<ul class="sub">{"".join(items)}</ul>'


def header(lang, page_path="index.html"):
    t = T[lang]
    other = "es" if lang == "en" else "en"
    nav_links = ""
    for key, href in NAV:
        if key == "nav_lines":
            nav_links += (f'<li class="has-sub"><a href="/{lang}/{href}" aria-haspopup="true">'
                          f'{t[key]} <span class="sub-caret" aria-hidden="true">▾</span></a>'
                          f'{_lines_submenu(lang, t)}</li>')
        else:
            nav_links += f'<li><a href="/{lang}/{href}">{t[key]}</a></li>'
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
