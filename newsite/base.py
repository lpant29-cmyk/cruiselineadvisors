# -*- coding: utf-8 -*-
"""The page shell — <head> SEO, fonts, inlined CSS, header, content, footer, sticky call.
Every page is composed through page(). Bilingual: emits canonical + hreflang alternates."""
import html, json
from config import PHONE_HREF, SITE_URL, BRAND, LANGS, DEFAULT_LANG, IS_PLACEHOLDER_PHONE, HOURS
from theme import CSS
from header import header
from footer import footer
from cta import sticky_callbar

FONT_URL = ("https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;"
            "0,9..144,600;1,9..144,600&family=Inter:wght@400;500;600;700;800;900&display=swap")


def esc(s):
    return html.escape(str(s), quote=True)


def _org_jsonld():
    org = {
        "@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE_URL,
        "description": ("Independent cruise information and referral service that connects travellers "
                        "with licensed cruise specialists at independent partner agencies. We are not a "
                        "cruise line or a travel agency."),
        "areaServed": {"@type": "Country", "name": "United States"},
        "knowsLanguage": ["en", "es"],
    }
    if not IS_PLACEHOLDER_PHONE:
        org["telephone"] = PHONE_HREF
        org["contactPoint"] = {
            "@type": "ContactPoint", "telephone": PHONE_HREF, "contactType": "reservations",
            "areaServed": "US", "availableLanguage": ["English", "Spanish"],
            "hoursAvailable": {"@type": "OpeningHoursSpecification",
                               "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                                             "Friday", "Saturday", "Sunday"],
                               "opens": "08:00", "closes": "23:00"}}
    return '<script type="application/ld+json">' + json.dumps(org, ensure_ascii=False) + '</script>'


def page(lang, page_path, title, desc, content, extra_jsonld=""):
    canonical = f"{SITE_URL}/{lang}/{page_path}"
    alternates = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{l}/{page_path}">' for l in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{DEFAULT_LANG}/{page_path}">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{alternates}
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0A2540">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:locale" content="{'en_US' if lang=='en' else 'es_ES'}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(BRAND)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE_URL}/og-image.png">
{_org_jsonld()}{extra_jsonld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONT_URL}">
<link rel="stylesheet" href="{FONT_URL}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{FONT_URL}"></noscript>
<style>{CSS}</style>
</head>
<body>
<a href="#main" class="skip">{'Skip to content' if lang=='en' else 'Saltar al contenido'}</a>
{header(lang, page_path)}
<main id="main">{content}</main>
{footer(lang)}
{sticky_callbar(lang)}
<button id="toTop" class="totop" aria-label="{'Back to top' if lang=='en' else 'Volver arriba'}">↑</button>
<script>
function trackCall(p){{window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'call_click',placement:p,lang:'{lang}'}});
if(typeof gtag==='function'){{gtag('event','call_click',{{placement:p}});}}return true;}}
(function(){{var b=document.getElementById('toTop');if(!b)return;
b.onclick=function(){{window.scrollTo({{top:0,behavior:'smooth'}});}};
addEventListener('scroll',function(){{b.classList.toggle('show',window.scrollY>600);}},{{passive:true}});}})();
</script>
</body></html>"""
