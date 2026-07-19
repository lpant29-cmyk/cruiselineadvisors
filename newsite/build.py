# -*- coding: utf-8 -*-
"""Build orchestrator. Renders every page in every language into dist/, runs the seven-rules
banned-term guard on each <main>, and writes root redirect + 404 + sitemap.xml + robots.txt.

Output → newsite/dist/. The LIVE site/ folder is never touched. Run: python3 build.py"""
import os
import re
import shutil
import datetime
from config import LANGS, DEFAULT_LANG, SITE_URL, BRAND, COMPANY
from base import page
from i18n import T
import page_home
from pages import (p_lines_hub, p_line, p_compare, p_facts, p_dest_hub, p_region,
                   p_guides_hub, p_guide, p_updates, p_update_detail, GUIDES)
from updates import all_updates
from legal_pages import p_legal, LEGAL
from data import LINES, DESTINATIONS
from facts import coverage

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
TODAY = datetime.date.today().isoformat()
BANNED = ("$", "usd", "from $", "save ", "discount", "% off", "cheapest", "lowest price")

HOME_TITLE = {"en": "CruiseLine Advisors — Talk to a Licensed Cruise Specialist",
              "es": "CruiseLine Advisors — Habla con un especialista en cruceros"}


def _t(en, es, lang):
    return en if lang == "en" else es


def clean_urls(s):
    """Rewrite links/canonicals to clean directory URLs: /en/index.html -> /en/,
    /en/lines/carnival.html -> /en/lines/carnival/ . Pages are written as <path>/index.html."""
    s = re.sub(r'/(en|es)/index\.html', r'/\1/', s)
    s = re.sub(r'/(en|es)/([A-Za-z0-9/_%-]+?)\.html', r'/\1/\2/', s)
    return s


def build():
    shutil.rmtree(DIST, ignore_errors=True)  # clean output so no stale files linger
    hits, written = [], []

    def write(rel, html):
        full = os.path.join(DIST, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(html)

    def guard(rel, html):
        m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S | re.I)
        if not m:
            return
        # Scripts carry the compare-tool data (may hold sanctioned fee amounts); <span class="fee">
        # wraps published fees (e.g. gratuities) — the allowed exception to Hard Rule 1. Strip both,
        # then scan the remaining visible prose strictly.
        main = re.sub(r"<script\b[^>]*>.*?</script>", "", m.group(1), flags=re.S | re.I)
        main = re.sub(r'<span class="fee">.*?</span>', "", main, flags=re.S | re.I)
        low = main.lower().replace(COMPANY.lower(), "")  # legal entity name is a proper noun
        for b in BANNED:
            if b in low:
                hits.append((b, rel))

    def emit(lang, path, title, desc, content):
        html = clean_urls(page(lang, path, title, desc, content))
        if path == "index.html":
            out, url = f"{lang}/index.html", f"{lang}/"
        else:
            out, url = f"{lang}/{path[:-5]}/index.html", f"{lang}/{path[:-5]}/"
        write(out, html)
        written.append(url)
        guard(out, html)

    for lang in LANGS:
        emit(lang, "index.html", HOME_TITLE[lang], T[lang]["hero_sub"], page_home.render(lang))

        emit(lang, "cruise-lines.html",
             _t("Cruise Line Guides — Every Major Line | CruiseLine Advisors",
                "Guías de líneas de crucero — cada línea principal | CruiseLine Advisors", lang),
             T[lang]["lines_sub"], p_lines_hub(lang))
        for L in LINES:
            emit(lang, f"lines/{L['slug']}.html",
                 _t(f"{L['name']} Cruises — Guide, Included, Cabins & Timing | CruiseLine Advisors",
                    f"{L['name']}: guía, qué se incluye, camarotes y temporada | CruiseLine Advisors", lang),
                 L["tag"][lang], p_line(lang, L["slug"]))

        emit(lang, "compare.html",
             _t("Compare Cruise Lines on What Matters | CruiseLine Advisors",
                "Compara líneas de crucero en lo que importa | CruiseLine Advisors", lang),
             T[lang]["cmp_sub"], p_compare(lang))
        emit(lang, "cruise-facts.html",
             _t("Cruise Facts That Cost You Money | CruiseLine Advisors",
                "Datos de crucero que cuestan dinero | CruiseLine Advisors", lang),
             _t("Gratuities, what's included, cancellation, documents — explained.",
                "Propinas, qué se incluye, cancelación, documentos — explicado.", lang), p_facts(lang))

        emit(lang, "destinations.html",
             _t("Cruise Destinations — Where & When to Sail | CruiseLine Advisors",
                "Destinos de crucero — a dónde y cuándo navegar | CruiseLine Advisors", lang),
             T[lang]["dest_sub"], p_dest_hub(lang))
        for d in DESTINATIONS:
            emit(lang, f"destinations/{d['slug']}.html",
                 _t(f"{d['name']['en']} Cruises — Best Time to Sail | CruiseLine Advisors",
                    f"Cruceros a {d['name']['es']} — mejor época | CruiseLine Advisors", lang),
                 _t(f"When to cruise {d['name']['en']} and what to expect.",
                    f"Cuándo navegar a {d['name']['es']} y qué esperar.", lang), p_region(lang, d["slug"]))

        emit(lang, "guides.html",
             _t("Cruise Planning Guides | CruiseLine Advisors",
                "Guías para planear tu crucero | CruiseLine Advisors", lang),
             _t("Cabins, budgets, families, accessibility and timing.",
                "Camarotes, presupuestos, familias, accesibilidad y temporada.", lang), p_guides_hub(lang))
        for g in GUIDES:
            emit(lang, f"guides/{g['slug']}.html",
                 f"{g['t'][lang]} | CruiseLine Advisors", g["d"][lang], p_guide(lang, g["slug"]))

        emit(lang, "updates.html",
             _t("Cruise Policy & Industry Updates | CruiseLine Advisors",
                "Novedades de políticas de cruceros | CruiseLine Advisors", lang),
             _t("Dated, sourced cruise policy updates.", "Novedades de políticas, fechadas y con fuente.", lang),
             p_updates(lang))
        for u in all_updates():
            emit(lang, f"updates/{u['slug']}.html", f"{u['title'][lang]} | CruiseLine Advisors",
                 u["body"][lang], p_update_detail(lang, u["slug"]))

        for k in LEGAL:
            emit(lang, f"legal/{k}.html", f"{LEGAL[k]['title'][lang]} | CruiseLine Advisors",
                 LEGAL[k]["title"][lang], p_legal(lang, k))

    # root → default language
    write("index.html", clean_urls(f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0; url=/{DEFAULT_LANG}/index.html">
<link rel="canonical" href="{SITE_URL}/{DEFAULT_LANG}/index.html"><title>{BRAND}</title></head>
<body><script>location.replace('/{DEFAULT_LANG}/index.html')</script>
<p>Redirecting to <a href="/{DEFAULT_LANG}/index.html">{BRAND}</a>…</p></body></html>"""))

    # 404
    nf = ('<section class="section navy phero"><div class="wrap">'
          '<h1>Page not found</h1><p class="phero-sub">That page has drifted off course. Let\'s get you back on deck.</p>'
          f'<a class="btn btn-call" href="/{DEFAULT_LANG}/index.html">← Back to home</a></div></section>')
    html404 = clean_urls(page(DEFAULT_LANG, "404.html", "Page not found | CruiseLine Advisors", "Page not found.", nf))
    html404 = html404.replace('content="index,follow', 'content="noindex,follow')
    write("404.html", html404)

    # sitemap + robots
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{p}" for p in written]
    body = "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    write("sitemap.xml",
          f'<?xml version="1.0" encoding="UTF-8"?>\n'
          f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    # static assets → dist root (favicon, icons, og-image, manifest)
    assets = os.path.join(ROOT, "assets")
    n_assets = 0
    if os.path.isdir(assets):
        for fn in os.listdir(assets):
            shutil.copy2(os.path.join(assets, fn), os.path.join(DIST, fn))
            n_assets += 1

    done, total = coverage()
    print(f"Built {len(written)} pages (+ root, 404, sitemap, robots) into dist/")
    print(f"  facts verified: {done}/{total}")
    if hits:
        print("  ⚠ BANNED-TERM HITS:", hits)
    else:
        print("  ✓ banned-term guard clean")


if __name__ == "__main__":
    build()
