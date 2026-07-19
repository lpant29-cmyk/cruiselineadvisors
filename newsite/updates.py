# -*- coding: utf-8 -*-
"""Cruise policy/industry updates — SINGLE SOURCE for the Updates page AND the per-line update
cards. Tag each entry with the line slugs it affects (empty list = general/all lines). Posting an
entry here makes it appear on the Updates page and on each tagged line's page automatically.

Rule 3: only post what you can verify. Every entry should carry a real source URL and a real date."""
import datetime
from data import LINES

_NAME = {L["slug"]: L["name"] for L in LINES}
_EMO = {L["slug"]: L["emo"] for L in LINES}

# date = ISO. slug = the detail-page URL. lines = [] means general (shows everywhere).
# detail = the longer body for the update's own page. src = internal record only (never rendered).
UPDATES = [
    {"date": "2026-05-11", "slug": "msc-daily-service-charge-2026", "lines": ["msc"],
     "title": {"en": "MSC updated its daily service charge for new bookings",
               "es": "MSC actualizó su cargo por servicio diario para nuevas reservas"},
     "body": {"en": "For cruises booked from 11 May 2026 (US & Caribbean), MSC's daily hotel service charge changed.",
              "es": "Para cruceros reservados desde el 11 de mayo de 2026 (EE.UU. y Caribe), cambió el cargo por servicio diario de MSC."},
     "detail": {"en": "For MSC cruises booked from 11 May 2026 in the US and Caribbean region, the daily hotel service charge was updated. This charge is added automatically to your onboard account each night and is not part of the base fare. Bookings made before that date keep the earlier rate, and the amounts also vary by other regions. The current per-person amounts are on our MSC guide and comparison — and an advisor can confirm the exact charge for your specific sailing, region and cabin before you book.",
                "es": "Para los cruceros de MSC reservados desde el 11 de mayo de 2026 en EE.UU. y el Caribe, se actualizó el cargo por servicio diario. Este cargo se añade automáticamente a tu cuenta a bordo cada noche y no forma parte de la tarifa base. Las reservas anteriores mantienen la tarifa previa, y los montos también varían por región. Los montos actuales están en nuestra guía y comparación de MSC — y un asesor puede confirmar el cargo exacto para tu crucero, región y camarote antes de reservar."},
     "src": "https://www.msccruisesusa.com/manage-booking/before-you-go/service-charges"},
]

_BY_SLUG = {u["slug"]: u for u in UPDATES}


def get_update(slug):
    return _BY_SLUG.get(slug)


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
    read = "Read →" if lang == "en" else "Leer →"
    cards = ""
    for u in ups:
        tags = ""
        if show_line_tags:
            if u.get("lines"):
                tags = "".join(f'<span class="upd-tag">{_EMO[s]} {_NAME[s]}</span>' for s in u["lines"] if s in _NAME)
            else:
                tags = f'<span class="upd-tag">{"All lines" if lang=="en" else "Todas las líneas"}</span>'
        cards += (f'<a class="upd-card" href="/{lang}/updates/{u["slug"]}/">'
                  f'<div class="upd-top"><span class="upd-date">{_fmt(u["date"])}</span>{tags}</div>'
                  f'<h3 class="upd-title">{u["title"][lang]}</h3><p class="upd-body">{u["body"][lang]}</p>'
                  f'<span class="upd-read">{read}</span></a>')
    return f'<div class="updgrid">{cards}</div>'
