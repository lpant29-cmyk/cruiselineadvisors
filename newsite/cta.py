# -*- coding: utf-8 -*-
"""Reusable call-to-action pieces. Phone always comes from config (one source)."""
from config import PHONE_DISPLAY, PHONE_HREF, HOURS
from i18n import T


def big_call(lang, placement="section"):
    t = T[lang]
    return (f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'{placement}\')">'
            f'<span class="ic" aria-hidden="true">☎</span>'
            f'<span>{t["cta_call"]} · {PHONE_DISPLAY}</span></a>')


def ask_advisor(lang, where="fact"):
    """The visible stand-in for a fact we have NOT verified.

    Replaces the old flat "Not yet verified" text on line and ship pages. It still
    refuses to print a value we have not read at a source (Hard Rule 3 is untouched),
    but the gap now goes somewhere: a licensed partner agency can answer it on the
    phone, and a call is the only thing this site exists to produce.

    What deliberately did NOT change: the internal accounting. verify.py and
    facts.coverage() still count this cell as unfilled, so softening the wording for
    the visitor cannot hide a gap from us. If that ever stops being true, this is the
    wrong helper and the honest text belongs back in.
    """
    label = "Ask an advisor" if lang == "en" else "Pregunta a un asesor"
    # trackCall is defined site-wide, but an undefined global here would throw inside an
    # onclick and, per the orphaned-reference pitfall, take the rest of the page with it.
    return (f'<a class="gap-ask" href="tel:{PHONE_HREF}" '
            f'onclick="try{{trackCall(\'gap-{where}\')}}catch(e){{}}">'
            f'<span class="ic" aria-hidden="true">☎</span>{label}</a>')


def sticky_callbar(lang):
    t = T[lang]
    return (f'<div class="callbar">'
            f'<div class="cbtxt"><b>{t["cta_call"]}, {PHONE_DISPLAY}</b>'
            f'<span>{t["free_to_call"]} · {HOURS[lang]}</span></div>'
            f'<a class="btn btn-call" href="tel:{PHONE_HREF}" onclick="trackCall(\'sticky\')">'
            f'<span class="ic" aria-hidden="true">☎</span></a></div>')
