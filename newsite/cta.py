# -*- coding: utf-8 -*-
"""Reusable call-to-action pieces. Phone always comes from config (one source)."""
from config import PHONE_DISPLAY, PHONE_HREF, HOURS
from i18n import T


def big_call(lang, placement="section"):
    t = T[lang]
    return (f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'{placement}\')">'
            f'<span class="ic" aria-hidden="true">☎</span>'
            f'<span>{t["cta_call"]} · {PHONE_DISPLAY}</span></a>')


def sticky_callbar(lang):
    t = T[lang]
    return (f'<div class="callbar">'
            f'<div class="cbtxt"><b>{t["cta_call"]}, {PHONE_DISPLAY}</b>'
            f'<span>{t["free_to_call"]} · {HOURS[lang]}</span></div>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'sticky\')">'
            f'<span class="ic" aria-hidden="true">☎</span></a></div>')
