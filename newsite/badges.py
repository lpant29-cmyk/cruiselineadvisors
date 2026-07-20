# -*- coding: utf-8 -*-
"""The 'Verified from official source' stamp. Shown wherever verified facts/specs appear —
line pages, the compare tools, and ship pages — with the date the data was last checked.
It only ever claims official-source verification; unverified fields still render as visible gaps."""
import datetime

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


_SEAL_TEXT = {
    "en": {"top": "OFFICIALLY VERIFIED", "bot": "CHECKED", "mid": "SOURCE"},
    "es": {"top": "VERIFICADO OFICIAL", "bot": "REVISADO", "mid": "FUENTE"},
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
    aria = f'{t["top"]} — {t["bot"]} {d}' if d else t["top"]
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
