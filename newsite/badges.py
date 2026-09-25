# -*- coding: utf-8 -*-
"""The 'Verified from official source' stamp. Shown wherever verified facts/specs appear, 
line pages, the compare tools, and ship pages, with the date the data was last checked.
It only ever claims official-source verification; unverified fields still render as visible gaps."""
import datetime
import os

_LABEL = {
    "en": "Verified from official sources",
    "es": "Verificado de fuentes oficiales",
}
_CHECKED = {"en": "checked", "es": "revisado"}


def _fmt(date):
    if not date:
        return ""
    try:
        return datetime.date.fromisoformat(date).strftime("%b %d, %Y").replace(" 0", " ")
    except (ValueError, TypeError):
        return str(date)


def verified_stamp(lang, date=None):
    """A small rubber-stamp-style badge: shield check + 'Verified from official sources · checked <date>'.
    Used inline inside the compare tools where a full circular seal would not fit."""
    d = _fmt(date)
    datepart = f'<span class="vstamp-d">· {_CHECKED[lang]} {d}</span>' if d else ""
    return (f'<span class="vstamp" role="img" aria-label="{_LABEL[lang]}{(" - " + d) if d else ""}">'
            f'<svg class="vstamp-ic" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" '
            f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="12" cy="4" r="2"/><line x1="12" y1="6" x2="12" y2="21"/>'
            f'<line x1="8" y1="10" x2="16" y2="10"/><path d="M5 15a7 7 0 0 0 14 0"/></svg>'
            f'<span class="vstamp-t">{_LABEL[lang]}</span>{datepart}</span>')


# NOTE: the seal is OUR independent verification of data we read from the lines' official sites, 
# it must never read as an official cruise-line page/endorsement (Hard Rule 2). Keep wording clear.
_SEAL_TEXT = {
    "en": {"top": "INDEPENDENTLY VERIFIED", "bot": "CHECKED", "mid": "SOURCE"},
    "es": {"top": "VERIFICADO POR NOSOTROS", "bot": "REVISADO", "mid": "FUENTE"},
}
_seal_n = [0]


def verified_seal(lang, date=None):
    """A real circular rubber-stamp seal (SVG): double ring, curved 'OFFICIALLY VERIFIED' over the
    top, 'CHECKED <date>' under the bottom, a big check in the middle, flanking diamonds. Rotated and
    ink-toned so it reads like it was stamped onto the facts. Unique path ids per instance."""
    _seal_n[0] += 1
    u = _seal_n[0]
    t = _SEAL_TEXT[lang]
    d = _fmt(date).upper()
    bot = f'{t["bot"]} {d}' if d else t["bot"]
    aria = f'{t["top"]}, {t["bot"]} {d}' if d else t["top"]
    return (
        f'<span class="vseal" role="img" aria-label="{aria}">'
        f'<svg viewBox="0 0 200 200" width="122" height="122" aria-hidden="true">'
        f'<defs>'
        f'<path id="vs-t{u}" d="M 30 100 A 70 70 0 0 1 170 100"/>'
        f'<path id="vs-b{u}" d="M 33 103 A 67 67 0 0 0 167 103"/>'
        f'</defs>'
        f'<circle cx="100" cy="100" r="94" fill="none" stroke="currentColor" stroke-width="3.5"/>'
        f'<circle cx="100" cy="100" r="84" fill="none" stroke="currentColor" stroke-width="1.4"/>'
        f'<text class="vseal-arc"><textPath href="#vs-t{u}" startOffset="50%">{t["top"]}</textPath></text>'
        f'<text class="vseal-arc"><textPath href="#vs-b{u}" startOffset="50%">{bot}</textPath></text>'
        f'<text class="vseal-di" x="16" y="105">&#9670;</text>'
        f'<text class="vseal-di" x="184" y="105">&#9670;</text>'
        # centre: a cruise ship above an anchor
        f'<g fill="currentColor"><path d="M75 92 H125 L119 100 H81 Z"/>'
        f'<rect x="83" y="84" width="34" height="8" rx="1.5"/>'
        f'<rect x="89" y="78" width="22" height="6" rx="1.5"/>'
        f'<rect x="97.5" y="72" width="5.5" height="7" rx="1"/></g>'
        f'<g fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'
        f'<circle cx="100" cy="107" r="3"/><line x1="100" y1="110" x2="100" y2="126"/>'
        f'<line x1="91" y1="114" x2="109" y2="114"/>'
        f'<path d="M87 120 Q100 132 113 120 M87 120 L84 115 M113 120 L116 115"/></g>'
        f'</svg></span>')


# ── Operator credential badges (2026-09-17) ────────────────────────────────
# ASTA membership and the Florida Seller of Travel registration are held by the
# OPERATING ENTITY (BookMeCheapest LLC), not by the CruiseLine Advisors referral
# service. The wording below is deliberate: it says "Operated by ... " so the
# credential attaches to the company, and never implies that this site sells,
# books or takes payment for cruise travel. Both badges link out to the issuer's
# own public lookup so a visitor can check them rather than take our word.
#
# Hard Rule 5 applies: these are real registrations, never decoration. If either
# lapses, remove it the same day. We show no ASTA member number because ASTA
# publishes none for this member; we do not invent one.
_TRUST = {
    "en": {"op": "Operated by", "asta": "Proud ASTA member",
           "asta_alt": "ASTA member, American Society of Travel Advisors",
           "romance_alt": "Bahamas Romance Specialist certification",
           "fsot": "FL Seller of Travel Ref.",
           "verify": "verify", "prev": "Previous certifications", "next": "More certifications"},
    "es": {"op": "Operado por", "asta": "Miembro orgulloso de ASTA",
           "asta_alt": "Miembro de ASTA, American Society of Travel Advisors",
           "romance_alt": "Certificación de Especialista en Romance de las Bahamas",
           "fsot": "Vendedor de Viajes de Florida Ref.",
           "verify": "verificar", "prev": "Certificaciones anteriores", "next": "Más certificaciones"},
}

# Entity-scoped, deliberately singular, and deliberately NOT "our specialists":
# advisors work for the independent partner agencies, not for us (Hard Rule 5).
_SECTIONS = {
    "en": {"company": "Company credentials", "personal": "Training and certifications"},
    "es": {"company": "Credenciales de la empresa", "personal": "Formación y certificaciones"},
}

# The non-affiliation line. This is the sentence that makes it safe to show a
# cruise line's own training mark on a site that bids that line's brand terms.
# It must sit in the SAME block as the badges, not in the footer small print.
_PERSONAL_NOTE = {
    "en": ("Training completed by individuals at {co}, the team that researches and publishes "
           "this site. Calls are answered by independent licensed travel agencies who hold "
           "their own credentials, not by the people named here. These are professional "
           "development courses run by tourist boards and cruise lines for travel "
           "professionals. Completing one is a training achievement, not a partnership, "
           "appointment or endorsement. We are not affiliated with, authorised by, or an "
           "agent of any cruise line or tourist board."),
    "es": ("Formación completada por personas de {co}, el equipo que investiga y publica este "
           "sitio. Las llamadas las atienden agencias de viajes independientes con licencia, "
           "que tienen sus propias credenciales, no las personas nombradas aquí. Son cursos de "
           "desarrollo profesional que las oficinas de turismo y las líneas de crucero ofrecen "
           "a profesionales del sector. Completar uno es un logro formativo, no una asociación, "
           "nombramiento ni respaldo. No estamos afiliados, autorizados por, ni somos agentes "
           "de ninguna línea de crucero ni oficina de turismo."),
}

_RCU = {
    "en": ("{who} has completed Royal Caribbean University's Master of Adventure certification.",
           "Royal Caribbean University Master of Adventure certificate"),
    "es": ("{who} ha completado la certificación Master of Adventure de Royal Caribbean University.",
           "Certificado Master of Adventure de Royal Caribbean University"),
}

_BAHAMAS = {
    "en": ("A principal of {co} holds the Certified Bahamas Specialist diploma from "
           "The Islands of The Bahamas.", "Certified Bahamas Specialist diploma"),
    "es": ("Un socio de {co} posee el diploma de Certified Bahamas Specialist de "
           "The Islands of The Bahamas.", "Diploma de Certified Bahamas Specialist"),
}


def _asset_exists(webpath):
    """True if a /-rooted asset URL maps to a real file under assets/.
    Lets a credential degrade to text-only instead of shipping a broken image
    or a link to a document we are not actually hosting."""
    if not webpath:
        return False
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.isfile(os.path.join(here, "assets", webpath.lstrip("/")))


def trust_badges(lang, company, asta_url, fsot_ref, fsot_url, show_asta=True,
                 bahamas=False, bahamas_crest=None, bahamas_doc=None,
                 romance=False, romance_img=None,
                 rcu=False, rcu_badge=None, rcu_doc=None, rcu_holder=None, certs=None):
    """Two separate blocks, deliberately not one row (operator ruling 2026-09-25).

    COMPANY CREDENTIALS are registrations held by the operating entity: ASTA
    membership and the Florida Seller of Travel licence. They say something
    about the business.

    TRAINING AND CERTIFICATIONS are courses completed by named individuals.
    They say something about a person's product knowledge. Mixing the two
    implies the company is accredited by a cruise line or tourist board, which
    is exactly the affiliation our disclaimers deny. The non-affiliation note
    renders with the personal block and is not optional.
    """
    t, sec = _TRUST[lang], _SECTIONS[lang]

    # ── company credentials ────────────────────────────────────────────────
    company_items = []
    if show_asta:
        company_items.append(
            f'<a class="tb tb-asta" href="{asta_url}" target="_blank" rel="noopener nofollow" '
            f'title="{t["asta"]} ({t["verify"]})">'
            f'<img src="/badges/asta-member.png" alt="{t["asta_alt"]}" width="526" height="224" loading="lazy">'
            f'<span class="tb-cap">{t["asta"]}</span></a>')
    if fsot_ref:
        company_items.append(
            f'<a class="tb tb-fsot" href="{fsot_url}" target="_blank" rel="noopener nofollow" '
            f'title="{t["fsot"]} {fsot_ref} ({t["verify"]})">'
            f'<span class="tb-fsot-txt">{t["fsot"]} {fsot_ref}</span></a>')

    # ── personal training (scroller) ───────────────────────────────────────
    # Shows three at a time; the rest are reachable by swipe or the arrows.
    # A cert with no document renders as a non-clickable chip rather than
    # being pointed at some other cert's file.
    personal_items, lines = [], []
    if bahamas:
        lines.append(_BAHAMAS[lang][0].format(co=company))
    if rcu and rcu_holder:
        lines.append(_RCU[lang][0].format(who=rcu_holder))
    for c in (certs or []):
        label = c.get(lang) or c.get("en")
        img, doc = c.get("img"), c.get("doc")
        if img and _asset_exists(img):
            inner = (f'<img src="{img}" alt="{label}" loading="lazy">'
                     f'<span class="tb-cap">{label}</span>')
        else:
            inner = f'<span class="tb-chip">{label}</span>'
        cls = f'tb tb-cert tb-cert-{c.get("key","x")}'
        if doc and _asset_exists(doc):
            personal_items.append(f'<a class="{cls}" href="{doc}" target="_blank" rel="noopener" '
                                  f'title="{label} ({t["verify"]})">{inner}</a>')
        else:
            personal_items.append(f'<span class="{cls}" title="{label}">{inner}</span>')

    blocks = []
    if company_items:
        blocks.append(f'<div class="tb-group"><p class="tb-op">{sec["company"]}: '
                      f'<b>{company}</b></p><div class="tb-row">{"".join(company_items)}</div></div>')
    if personal_items:
        body = " ".join(lines)
        disclaimer = _PERSONAL_NOTE[lang].format(co=company)
        nav = (f'<button class="tb-nav tb-prev" type="button" aria-label="{t["prev"]}">‹</button>'
               f'<button class="tb-nav tb-next" type="button" aria-label="{t["next"]}">›</button>'
               ) if len(personal_items) > 3 else ""
        blocks.append(f'<div class="tb-group tb-group-personal"><p class="tb-op">{sec["personal"]}</p>'
                      f'<div class="tb-slider">{nav}'
                      f'<div class="tb-row tb-scroll">{"".join(personal_items)}</div></div>'
                      f'<p class="tb-note">{body}</p>'
                      f'<p class="tb-note tb-disclaim">{disclaimer}</p></div>')
    if not blocks:
        return ""
    # Arrows. Own IIFE with a null guard on line one, per the known pitfall:
    # a missing element must never take out later scripts on the page.
    js = ("<script>(function(){var s=document.querySelectorAll('.tb-slider');if(!s.length)return;"
          "s.forEach(function(sl){var r=sl.querySelector('.tb-scroll');if(!r)return;"
          "var p=sl.querySelector('.tb-prev'),n=sl.querySelector('.tb-next');"
          "function w(){var c=r.querySelector('.tb-cert');return c?c.offsetWidth+14:160;}"
          "function sync(){if(!p||!n)return;var m=r.scrollWidth-r.clientWidth-2;"
          "p.style.opacity=r.scrollLeft<=2?'.35':'1';n.style.opacity=r.scrollLeft>=m?'.35':'1';}"
          "if(p)p.addEventListener('click',function(){r.scrollBy({left:-w(),behavior:'smooth'});});"
          "if(n)n.addEventListener('click',function(){r.scrollBy({left:w(),behavior:'smooth'});});"
          "r.addEventListener('scroll',sync,{passive:true});"
          "window.addEventListener('resize',sync,{passive:true});sync();});})();</script>")
    return f'<div class="trustbadges">{"".join(blocks)}</div>{js}'
