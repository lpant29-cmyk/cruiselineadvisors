# -*- coding: utf-8 -*-
"""Cruise policy/industry updates — SINGLE SOURCE for the Updates page AND the per-line update
cards. Tag each entry with the line slugs it affects (empty list = general/all lines). Posting an
entry here makes it appear on the Updates page and on each tagged line's page automatically.

Rule 3: only post what you can verify. Every entry should carry a real source URL and a real date."""
import datetime
from data import LINES

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}

# date = ISO. lines = [] means general (shows on every line page + updates page).
UPDATES = [
    {"date": "2026-05-11", "lines": ["msc"],
     "title": {"en": "MSC updated its daily service charge for new bookings",
               "es": "MSC actualizó su cargo por servicio diario para nuevas reservas"},
     "body": {"en": "For cruises booked from 11 May 2026 (US & Caribbean), MSC's daily hotel service charge changed. See the current amount on the MSC guide.",
              "es": "Para cruceros reservados desde el 11 de mayo de 2026 (EE.UU. y Caribe), cambió el cargo por servicio diario de MSC. Consulta el monto actual en la guía de MSC."},
     "src": "https://www.msccruisesusa.com/manage-booking/before-you-go/service-charges"},
]


def updates_for(slug):
    """Updates tagged with this line, plus general (untagged) updates — newest first."""
    ups = [u for u in UPDATES if not u.get("lines") or slug in u["lines"]]
    return sorted(ups, key=lambda u: u["date"], reverse=True)


def all_updates():
    return sorted(UPDATES, key=lambda u: u["date"], reverse=True)


def _fmt(d):
    try:
        return datetime.date.fromisoformat(d).strftime("%b %-d, %Y")
    except Exception:
        return d


def update_cards(lang, ups, show_line_tags=True):
    """Render a grid of update cards. `ups` is a list of update dicts."""
    if not ups:
        empty = ("No updates right now. Call and we'll confirm the latest policy from the source."
                 if lang == "en" else
                 "No hay novedades ahora. Llama y confirmamos la última política desde la fuente.")
        return f'<p class="upd-empty">{empty}</p>'
    cards = ""
    for u in ups:
        tags = ""
        if show_line_tags:
            if u.get("lines"):
                tags = "".join(f'<span class="upd-tag">{_EMO[s]} {_NAME[s]}</span>' for s in u["lines"] if s in _NAME)
            else:
                tags = f'<span class="upd-tag">{"All lines" if lang=="en" else "Todas las líneas"}</span>'
        cards += (f'<article class="upd-card"><div class="upd-top"><span class="upd-date">{_fmt(u["date"])}</span>{tags}</div>'
                  f'<h3 class="upd-title">{u["title"][lang]}</h3><p class="upd-body">{u["body"][lang]}</p></article>')
    return f'<div class="updgrid">{cards}</div>'
