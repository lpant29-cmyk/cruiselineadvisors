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
    """A small rubber-stamp-style seal: shield check + 'Verified from official sources · checked <date>'."""
    d = _fmt(date)
    datepart = f'<span class="vstamp-d">· {_CHECKED[lang]} {d}</span>' if d else ""
    return (f'<span class="vstamp" role="img" aria-label="{_LABEL[lang]}{(" - " + d) if d else ""}">'
            f'<svg class="vstamp-ic" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">'
            f'<path fill="currentColor" d="M12 1 3 5v6c0 5 3.8 9.4 9 11 5.2-1.6 9-6 9-11V5l-9-4z"/>'
            f'<path fill="#fff" d="m10.6 14.6-2.5-2.5 1.4-1.4 1.1 1.1 3.9-3.9 1.4 1.4z"/></svg>'
            f'<span class="vstamp-t">{_LABEL[lang]}</span>{datepart}</span>')
