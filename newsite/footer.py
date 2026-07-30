# -*- coding: utf-8 -*-
"""Site footer, one file. Link columns + the compliance disclaimers (bilingual).
The disclaimers are legally load-bearing; edit with care."""
from config import PHONE_DISPLAY, PHONE_HREF, HOURS, BRAND, COMPANY
from i18n import T
from badges import verified_seal
from facts import latest_verified_all
from legal_partial import legal_blocks_html, legal_links_html, LEGAL
import datetime

YEAR = datetime.date.today().year

_SEAL_CAP = {
    "en": "All facts &amp; ship data verified from official cruise-line sites",
    "es": "Todos los datos verificados de sitios oficiales de las líneas",
}




def footer(lang):
    t = T[lang]
    disc = legal_blocks_html(lang)
    legal = legal_links_html(lang)
    return f"""<footer class="ftr">
  <div class="wrap">
    <div class="cols">
      <div class="foot-brand">
        <b style="color:#fff;font-family:'Fraunces',serif;font-size:1.2rem">CruiseLine<span style="color:#E0A84E">Advisors</span></b>
        <p>{t['foot_tag']} <b style="color:#C9DBE5">{t['foot_hours']}:</b> {HOURS[lang]}.</p>
        <p><a href="tel:{PHONE_HREF}" style="color:#E0A84E;font-weight:800;display:inline">☎ {PHONE_DISPLAY}</a></p>
        <div class="foot-seal">{verified_seal(lang, latest_verified_all())}<small>{_SEAL_CAP[lang]}</small></div>
      </div>
      <div>
        <h4>{t['foot_col_lines']}</h4>
        <a href="/{lang}/cruise-lines.html">{t['lines_all']}</a>
        <a href="/{lang}/lines/royal-caribbean.html">Royal Caribbean</a>
        <a href="/{lang}/lines/carnival.html">Carnival</a>
        <a href="/{lang}/lines/princess.html">Princess</a>
      </div>
      <div>
        <h4>{t['foot_col_res']}</h4>
        <a href="/{lang}/compare.html">{t['nav_compare']}</a>
        <a href="/{lang}/cruise-facts.html">{t['nav_facts']}</a>
        <a href="/{lang}/destinations.html">{t['nav_dest']}</a>
        <a href="/{lang}/guides.html">{t['nav_guides']}</a>
        <a href="/{lang}/updates.html">{t['nav_updates']}</a>
      </div>
      <div>
        <h4>{t['foot_col_legal']}</h4>
        {legal}
      </div>
      <div class="disc">
        {disc}
        <div class="legalrow">{legal}</div>
        <p style="margin-top:.6rem">© {YEAR} {COMPANY}. Florida, USA.</p>
      </div>
    </div>
  </div>
</footer>"""
