# -*- coding: utf-8 -*-
"""Rich, SEO-first cruise guides, the topical-authority layer.

Each guide is a hand-written research piece (no copied prose, no prices, Hard Rules), structured for
both Google and AI overviews: a clear H1 + dek, a "key takeaways" box (snippet/answer bait), scannable
H2 sections with their own anchors and a table of contents, an FAQ that emits FAQPage JSON-LD, Article
JSON-LD, and dense semantic interlinking to the tools, fact pages, line pages and sibling guides.

Content lives in RICH_GUIDES; render_rich_guide() returns the <main> inner HTML (p_guide adds the hero
and the call CTA). A guide whose slug isn't here falls back to the older paragraph guide.
"""
import json
import os
from config import SITE_URL, BRAND, PHONE_HREF, PHONE_DISPLAY

_GUIDES_IMG_DIR = os.path.join(os.path.dirname(__file__), "assets", "guides")


def guide_hero_img(slug, override=None):
    """Return the guide's hero image filename if it exists on disk, else None (gradient fallback)."""
    for name in ([override] if override else []) + [f"{slug}.jpg"]:
        if name and os.path.exists(os.path.join(_GUIDES_IMG_DIR, name)):
            return name
    return None


def link(href, text):
    """Inline interlink helper. Keeps content strings quote-safe (no embedded href="" quotes)."""
    return f'<a href="{href}">{text}</a>'


def vcards(items):
    """A visual card grid for scannable concept lists. items = [(emoji, label, note)...]."""
    cards = ""
    for emo, label, note in items:
        body = f'<div class="xr-b"><p class="xr-desc">{note}</p></div>' if note else ""
        cards += (f'<article class="xr-card gvc-card"><div class="xr-top">'
                  f'<span class="xr-emoji">{emo}</span><div class="xr-h"><h3>{label}</h3></div></div>{body}</article>')
    return f'<div class="xr-grid gvc-grid">{cards}</div>'


def photo_band(img, caption=""):
    """A full-width self-hosted photo band to break up a long guide (illustrative)."""
    cap = f'<figcaption class="gband-cap">{caption}</figcaption>' if caption else ""
    return (f'<figure class="gband"><img src="/guides/{img}" alt="{caption}" loading="lazy" decoding="async">{cap}</figure>')


# ── small content helpers used inside section HTML ────────────────────────────────────────────────
def tip(en_or_html):
    return f'<div class="gd-callout gd-tip"><span class="gd-cl-ic" aria-hidden="true">💡</span><div>{en_or_html}</div></div>'


def watch(html):
    return f'<div class="gd-callout gd-watch"><span class="gd-cl-ic" aria-hidden="true">⚠️</span><div>{html}</div></div>'


def define(term, html):
    return f'<div class="gd-callout gd-define"><span class="gd-cl-ic" aria-hidden="true">📖</span><div><b>{term}:</b> {html}</div></div>'


def _L(lang, en, es):
    return en if lang == "en" else es


# Registry of rich guides. See the flagship below for the shape.
RICH_GUIDES = {}


def register(slug, data):
    RICH_GUIDES[slug] = data


def has_rich_guide(slug):
    return slug in RICH_GUIDES


def _toc(lang, sections, faqs):
    items = [(f"#{s['id']}", s["h2"][lang]) for s in sections]
    if faqs:
        items.append(("#faq", _L(lang, "FAQ", "Preguntas frecuentes")))
    lbl = _L(lang, "On this page", "En esta página")
    links = "".join(f'<a class="ship-toc-a" href="{a}">{t}</a>' for a, t in items)
    return (f'<section class="section ship-toc-sec"><div class="wrap">'
            f'<nav class="ship-toc" aria-label="{lbl}"><span class="ship-toc-l">{lbl}</span>{links}</nav>'
            f'</div></section>')


def _takeaways(lang, items):
    lbl = _L(lang, "The short version", "En resumen")
    lis = "".join(f"<li>{x}</li>" for x in items)
    return (f'<section class="section"><div class="wrap"><div class="gd-takeaways">'
            f'<h2>{lbl}</h2><ul>{lis}</ul></div></div></section>')


def _sections(lang, sections):
    out = ""
    for i, s in enumerate(sections):
        cls = "cream" if i % 2 else ""
        out += (f'<section class="section {cls}" id="{s["id"]}"><div class="wrap gd-body">'
                f'<h2 class="rsec-h">{s["h2"][lang]}</h2>{s["html"][lang]}</div></section>')
    return out


def _faq(lang, faqs):
    if not faqs:
        return ""
    h = _L(lang, "Frequently asked questions", "Preguntas frecuentes")
    items = "".join(
        f'<details class="faq-item"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>'
        for q, a in faqs)
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    script = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'
    return (f'<section class="section" id="faq"><div class="wrap"><h2 class="rsec-h">{h}</h2>'
            f'<div class="faq-list">{items}</div>{script}</div></section>')


def _related(lang, related):
    """related = list of (emoji, title, href, blurb), semantic interlinks to guides/tools/pages."""
    if not related:
        return ""
    h = _L(lang, "Keep reading", "Sigue leyendo")
    cards = ""
    for emo, title, href, blurb in related:
        cards += (f'<a class="xr-card gd-rel" href="{href}"><div class="xr-top">'
                  f'<span class="xr-emoji">{emo}</span><div class="xr-h"><h3>{title}</h3></div></div>'
                  f'<div class="xr-b"><p class="xr-desc">{blurb}</p></div></a>')
    return (f'<section class="section cream"><div class="wrap"><h2 class="rsec-h">{h}</h2>'
            f'<div class="xr-grid">{cards}</div></div></section>')


def _article_ld(lang, slug, g):
    ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": g["title"][lang],
        "description": g["dek"][lang],
        "inLanguage": lang,
        "datePublished": g.get("published", g.get("updated")),
        "dateModified": g.get("updated"),
        "author": {"@type": "Organization", "name": BRAND, "url": SITE_URL},
        "publisher": {"@type": "Organization", "name": BRAND, "url": SITE_URL},
        "mainEntityOfPage": f"{SITE_URL}/{lang}/guides/{slug}/",
    }
    return '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'


def render_rich_guide(lang, slug):
    """Return the <main> inner HTML for a rich guide (p_guide wraps hero + CTA around this)."""
    g = RICH_GUIDES[slug]
    updated = _L(lang, "Reviewed", "Revisado") + " " + (g.get("updated") or "")
    meta = f'<p class="gd-meta">{updated} · {_L(lang, "Written by the CruiseLine Advisors team", "Escrito por el equipo de CruiseLine Advisors")}</p>'
    faqs = g.get("faqs", {}).get(lang) or []  # per-language list of (question, answer)
    return (_article_ld(lang, slug, g)
            + f'<section class="section gd-byline"><div class="wrap gd-body">{meta}</div></section>'
            + _takeaways(lang, g["takeaways"][lang])
            + _toc(lang, g["sections"], faqs)
            + _sections(lang, g["sections"])
            + _faq(lang, faqs)
            + _related(lang, g.get("related", {}).get(lang, [])))
