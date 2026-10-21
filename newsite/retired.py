# -*- coding: utf-8 -*-
"""Stubs for pages that must stop making a claim, at URLs that keep being served.

Render publishes additively and never prunes, so a page we simply stop
generating is still served, byte for byte, forever. That is tolerable for a
page that is merely out of date. It is not tolerable for a page whose whole
claim has become false: /en/lines/costa/ships/costa-firenze/ says Costa Firenze
is a Costa ship, and Costa's own fleet page no longer lists her because she
sails for Carnival now. Deleting her from the roster removes the link and the
sitemap entry and leaves the wrong page answering the URL.

So the roster edit writes a replacement at the same URL: noindex, canonical to
wherever the truth now lives, and a sentence saying what changed, because
someone who followed a bookmark deserves an answer rather than a redirect they
cannot read. The /go/ layer solved the same problem the same way in
lp-system/templates/lp/_departed-redirect.html; this is that pattern for the
indexed site.

Each entry is (ship slug, line the page used to live under, where to send
people now, what changed). The reason text is shown to the visitor, so it says
what we verified, not what we did to the data.
"""

RETIRED_SHIPS = [
    {
        "slug": "costa-firenze", "from_line": "costa",
        "target": {"en": "/en/lines/carnival/ships/carnival-firenze/",
                   "es": "/es/lines/carnival/ships/carnival-firenze/"},
        "name": {"en": "Costa Firenze", "es": "Costa Firenze"},
        "why": {"en": "This ship sails for Carnival Cruise Line as Carnival Firenze. She is no longer "
                      "listed on Costa's own fleet page.",
                "es": "Este barco navega para Carnival Cruise Line como Carnival Firenze. Ya no "
                      "aparece en la página de flota de Costa."},
    },
    {
        "slug": "costa-venezia", "from_line": "costa",
        "target": {"en": "/en/lines/carnival/ships/carnival-venezia/",
                   "es": "/es/lines/carnival/ships/carnival-venezia/"},
        "name": {"en": "Costa Venezia", "es": "Costa Venezia"},
        "why": {"en": "This ship sails for Carnival Cruise Line as Carnival Venezia. She is no longer "
                      "listed on Costa's own fleet page.",
                "es": "Este barco navega para Carnival Cruise Line como Carnival Venezia. Ya no "
                      "aparece en la página de flota de Costa."},
    },
    {
        "slug": "costa-fortuna", "from_line": "costa",
        "target": {"en": "/en/lines/costa/", "es": "/es/lines/costa/"},
        "name": {"en": "Costa Fortuna", "es": "Costa Fortuna"},
        "why": {"en": "Costa no longer lists this ship on its fleet page, so we do not describe her as "
                      "a current Costa ship. The ships Costa does publish are on the Costa page.",
                "es": "Costa ya no incluye este barco en su página de flota, así que no lo "
                      "describimos como un barco actual de Costa. Los barcos que Costa sí publica "
                      "están en la página de Costa."},
    },
    {
        "slug": "norwegian-bella", "from_line": "norwegian",
        "target": {"en": "/en/lines/norwegian/", "es": "/es/lines/norwegian/"},
        "name": {"en": "Norwegian Bella", "es": "Norwegian Bella"},
        "why": {"en": "Norwegian lists this ship as a 2028 build. She is not sailing yet, so there is "
                      "nothing verified to publish about her. The ships sailing now are on the "
                      "Norwegian page.",
                "es": "Norwegian indica que este barco se construye para 2028. Todavía no navega, así "
                      "que no hay datos verificados que publicar. Los barcos que navegan ahora están "
                      "en la página de Norwegian."},
    },
]

_T = {
    "en": {"h": "This page has moved on", "cta": "See where she sails now",
           "call": "Call", "back": "Back to the fleet"},
    "es": {"h": "Esta página ha cambiado", "cta": "Ver dónde navega ahora",
           "call": "Llama", "back": "Volver a la flota"},
}


def stub_html(lang, entry, phone_tel, phone_display, site_url=""):
    t = _T[lang]
    target = entry["target"][lang]
    name = entry["name"][lang]
    why = entry["why"][lang]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{name}</title>
<link rel="canonical" href="{site_url}{target}">
<!-- GENERATED. This ship left this line's fleet, so the page that described her
     here is replaced rather than deleted: the host publishes additively and
     never prunes, and a deleted page keeps being served with its old claim. -->
<style>
:root{{--ink:#082C42;--bg:#fff;--brand:#0B6E8F;--muted:#4D6B7A}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--ink:#E8EEF4;--bg:#0C1D28;--muted:#9FC0CB}}}}
:root[data-theme="dark"]{{--ink:#E8EEF4;--bg:#0C1D28;--muted:#9FC0CB}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Arial,sans-serif;
  display:grid;place-items:center;min-height:100vh;padding:24px 16px}}
.w{{max-width:34rem;text-align:center}}
h1{{font-size:1.4rem;margin:0 0 .7rem;text-wrap:balance}}
p{{margin:0 0 1rem;color:var(--muted)}}
a.cta{{display:inline-block;background:var(--brand);color:#fff;text-decoration:none;
  font-weight:700;padding:.85rem 1.3rem;border-radius:.6rem;margin:.3rem}}
a.alt{{color:var(--brand);margin:.3rem;display:inline-block}}
</style>
</head>
<body>
<div class="w">
<h1>{t['h']}</h1>
<p><b>{name}</b>: {why}</p>
<p><a class="cta" href="{target}">{t['cta']}</a>
   <a class="alt" href="tel:{phone_tel}">{t['call']} {phone_display}</a></p>
</div>
</body>
</html>"""
