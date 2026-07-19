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
            f'<svg class="vstamp-ic" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">'
            f'<path fill="currentColor" d="M12 1 3 5v6c0 5 3.8 9.4 9 11 5.2-1.6 9-6 9-11V5l-9-4z"/>'
            f'<path fill="#fff" d="m10.6 14.6-2.5-2.5 1.4-1.4 1.1 1.1 3.9-3.9 1.4 1.4z"/></svg>'
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
        f'<path d="M 82 99 l 10 12 l 24 -29" fill="none" stroke="currentColor" stroke-width="7" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text class="vseal-mid" x="100" y="130">{t["mid"]}</text>'
        f'</svg></span>')
