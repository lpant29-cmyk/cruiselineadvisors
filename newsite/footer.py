# -*- coding: utf-8 -*-
"""Site footer, one file. Link columns + the compliance disclaimers (bilingual).
The disclaimers are legally load-bearing; edit with care."""
from config import (PHONE_DISPLAY, PHONE_HREF, HOURS, BRAND, COMPANY,
                    ASTA_MEMBER, ASTA_URL, FSOT_REF, FSOT_URL,
                    TRUE_ACCREDITED, TRUE_CODE, TRUE_URL,
                    BAHAMAS_SPECIALIST, BAHAMAS_CREST, BAHAMAS_DOC,
                    RCU_ACCOLADE, RCU_DOC, RCU_HOLDER,
                    CARNIVAL_LE, CARNIVAL_LE_DOC, CARNIVAL_LE_HOLDER,
                    ROMANCE_SPECIALIST, ROMANCE_BADGE)
from i18n import T
from badges import verified_seal, trust_badges
from facts import latest_verified_all
from legal_partial import legal_blocks_html, legal_links_html, LEGAL
import datetime
import re

YEAR = datetime.date.today().year

_SEAL_CAP = {
    "en": "All facts &amp; ship data verified from official cruise-line sites",
    "es": "Todos los datos verificados de sitios oficiales de las líneas",
}




_CRED_BAND = {
    "en": {"eyebrow": "Credentials you can check",
           "h": "Licensed, ASTA member and Bahamas-certified",
           "sub": "You are in good hands. We hold recognised travel-industry credentials and the official "
                  "Islands of the Bahamas certifications. Tap a badge to verify it."},
    "es": {"eyebrow": "Credenciales que puedes verificar",
           "h": "Con licencia, miembro de ASTA y certificados en las Bahamas",
           "sub": "Estás en buenas manos. Tenemos credenciales reconocidas del sector de viajes y las "
                  "certificaciones oficiales de las Islas de las Bahamas. Toca un distintivo para verificarlo."},
}



# A cruise line's own training credential belongs on that line's pages and
# nowhere else (operator ruling 2026-10-21). Naming Royal Caribbean University
# on a Carnival ad page reads as a connection to the wrong line, on the exact
# keywords where being misread is most expensive, and it tells a Carnival
# visitor about a competitor's course. The company credentials below it (ASTA,
# the Florida licence, the Bahamas diploma) describe us and show everywhere.
_LINE_TRAINING = {"royal-caribbean": "rcu", "carnival": "carnival"}


def line_of_path(page_path):
    """The cruise line a main-site page is about, from its own path.

    /en/lines/carnival/ and /en/lines/carnival/ships/carnival-jubilee/ are both
    Carnival; a guide, a destination or the homepage is no line at all. Reading
    it from the path means every page gets this right without a single call
    site having to pass it, which is why there is no page type that can forget.
    """
    m = re.match(r"lines/([a-z0-9-]+?)(?:\.html|/|$)", str(page_path or ""))
    return m.group(1) if m else None


def credentials_band(lang, section_class="section", line_slug=None, compact=False):
    """Full-width credential band shown on every page (before the footer). Covers all trust and
    specialist badges at a readable size; specialist badges link to the self-hosted diploma.

    section_class is the HOST surface's section-padding class, the one thing
    about this component that is not self-contained: the main site pads
    sections with .section, the /go/ pages with .blk. Everything else comes
    from .credband rules in cred_css.py, so the band is identical on both.

    line_slug decides which cruise line training shows: that line's, or none.

    compact is the band that sits directly under the hero (operator ruling
    2026-10-26), and it carries the COMPANY registrations only: ASTA, the
    Florida Seller of Travel licence and the TRUE accreditation. Three reasons
    it is not simply the whole band repeated. The full band is 980px tall on a
    375px screen, which is more than a screenful of push-down on a site whose
    only job is a phone call. The personal block's non-affiliation disclaimer
    is not optional, so its badges cannot travel without 243px of note. And a
    legal disclaimer printed twice on one page is noise, not extra protection.
    The full band, with every badge and every note, is unchanged below.
    """
    c = _CRED_BAND[lang]
    training = _LINE_TRAINING.get(line_slug or "")
    trust = trust_badges(lang, COMPANY, ASTA_URL, FSOT_REF, FSOT_URL, show_asta=ASTA_MEMBER,
                         true_accredited=TRUE_ACCREDITED, true_code=TRUE_CODE, true_url=TRUE_URL,
                         bahamas=BAHAMAS_SPECIALIST, bahamas_crest=BAHAMAS_CREST,
                         bahamas_doc=BAHAMAS_DOC, romance=ROMANCE_SPECIALIST,
                         romance_img=ROMANCE_BADGE,
                         rcu=RCU_ACCOLADE and training == "rcu",
                         rcu_doc=RCU_DOC, rcu_holder=RCU_HOLDER,
                         carnival=CARNIVAL_LE and training == "carnival",
                         carnival_doc=CARNIVAL_LE_DOC,
                         carnival_holder=CARNIVAL_LE_HOLDER,
                         company_only=compact)
    if not trust:
        return ""
    if compact:
        # Eyebrow and badges only. The compact band carried an <h2> of its own
        # and the operator cut it (2026-10-26): the eyebrow already labels the
        # strip, and a second headline this close to the hero competes with the
        # page's real one. The full band below keeps its heading.
        return (f'<section class="{section_class} credband credband-top"><div class="wrap">'
                f'<div class="credband-head"><span class="eyebrow">{c["eyebrow"]}</span>'
                f'</div>{trust}</div></section>')
    return (f'<section class="{section_class} credband"><div class="wrap">'
            f'<div class="credband-head"><span class="eyebrow">{c["eyebrow"]}</span>'
            f'<h2>{c["h"]}</h2><p>{c["sub"]}</p></div>{trust}</div></section>')


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
