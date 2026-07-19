# -*- coding: utf-8 -*-
"""Homepage builder. Returns the <main> inner HTML for a given language."""
from config import PHONE_DISPLAY, PHONE_HREF, HOURS
from i18n import T
from cta import big_call
from data import LINES, CMP_FACTS, DESTINATIONS
from scene import ocean_scene, wave_divider, hero_dolphin, scroll_companions
from navigator import finder_card
from interactive import when_to_go, cabin_guide
from compare import compare_tool


def _hero(lang, t):
    benefits = "".join(
        f'<li><span class="ck">✓</span><span>{t[k]}</span></li>'
        for k in ("benefit_1", "benefit_2", "benefit_3"))
    chips = "".join(
        f'<span class="chip"><span class="ic">✓</span>{t[k]}</span>'
        for k in ("chip_independent", "chip_since", "chip_nopay"))
    return f"""<section class="hero">
  {ocean_scene()}
  {hero_dolphin()}
  <div class="wrap hero-grid">
    <div class="hero-content">
      <span class="badge"><span class="dot"></span>{t['hero_badge']}</span>
      <h1>{t['hero_h1a']} <em>{t['hero_h1b']}</em></h1>
      <p class="lead">{t['hero_sub']}</p>
      <div class="hero-cta">
        {big_call(lang, 'hero')}
        <label for="drawerCb" class="btn btn-ghost finder-open">🧭 {t['finder_open']}</label>
        <a class="btn btn-ghost hide-mobile" href="/{lang}/compare.html">{t['cta_compare']}</a>
      </div>
      <p class="hero-cap"><b>{t['free_to_call']}.</b> {HOURS[lang]}.</p>
      <div class="chips">{chips}</div>
      <ul class="benefits">{benefits}</ul>
    </div>
    <div class="finder-dock">
      <input type="checkbox" id="drawerCb" class="drawer-cb" aria-label="{t['finder_tab']}">
      <label for="drawerCb" class="drawer-tab"><span>🧭 {t['finder_tab']}</span></label>
      <label for="drawerCb" class="drawer-backdrop"></label>
      <div class="drawer-panel">
        <label for="drawerCb" class="drawer-close" aria-label="{t['finder_close']}">×</label>
        {finder_card(lang)}
      </div>
    </div>
  </div>
</section>"""


def _why(lang, t):
    cards = "".join(
        f"""<div class="card"><div class="ic-badge">{emo}</div>
        <h3>{t[tk]}</h3><p>{t[bk]}</p></div>"""
        for emo, tk, bk in [("💡", "why_1_t", "why_1_b"),
                            ("🧭", "why_2_t", "why_2_b"),
                            ("🤝", "why_3_t", "why_3_b")])
    return f"""<section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t['chip_independent']}</span><h2>{t['why_h2']}</h2></div>
  <div class="grid3">{cards}</div>
</div></section>"""


def _compare(lang, t):
    return f"""<section class="section foam" id="compare"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t['nav_facts']}</span><h2>{t['cmp_h2']}</h2><p>{t['cmp_sub']}</p></div>
  {compare_tool(lang)}
</div></section>"""


def _quiz(lang, t):
    return f"""<section class="section foam"><div class="wrap">
  <div class="quiz">
    <div><span class="eyebrow">{t['quiz_kicker']}</span>
      <h2>{t['quiz_h2']}</h2><p>{t['quiz_sub']}</p></div>
    <div><a class="btn btn-call btn-block" href="/{lang}/compare.html">{t['quiz_cta']}</a></div>
  </div>
</div></section>"""


ACCENTS = ["#FF6B5A", "#12919A", "#F0891F", "#6C5CE7", "#1FA47A", "#2E86DE", "#E0489B", "#0FA5B5"]


def _pcard(href, emo, name, cat, tag, read, i):
    ac = ACCENTS[i % len(ACCENTS)]
    return (f'<a class="pcard" style="--ac:{ac}" href="{href}">'
            f'<span class="pcard-emo">{emo}</span>'
            f'<span class="pcard-cat">{cat}</span>'
            f'<b>{name}</b><p>{tag}</p>'
            f'<span class="go">{read} →</span></a>')


def _lines(lang, t):
    cards = "".join(
        _pcard(f"/{lang}/lines/{L['slug']}.html", L['emo'], L['name'],
               L['cat'][lang], L['tag'][lang], t['read_guide'], i)
        for i, L in enumerate(LINES))
    return f"""<section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t['nav_lines']}</span><h2>{t['lines_h2']}</h2><p>{t['lines_sub']}</p></div>
  <div class="linegrid">{cards}</div>
  <p style="margin-top:20px"><a class="btn btn-ghost" href="/{lang}/cruise-lines.html">{t['lines_all']} →</a></p>
</div></section>"""


def _destinations(lang, t):
    cards = "".join(
        _pcard(f"/{lang}/destinations/{d['slug']}.html", d['emo'], d['name'][lang],
               f"{t['dest_best']}: {d['best'][lang]}", "", t['read_guide'], i)
        for i, d in enumerate(DESTINATIONS))
    return f"""<section class="section cream"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{t['nav_dest']}</span><h2>{t['dest_h2']}</h2><p>{t['dest_sub']}</p></div>
  <div class="linegrid">{cards}</div>
  <p style="margin-top:20px"><a class="btn btn-ghost" href="/{lang}/destinations.html">{t['dest_all']} →</a></p>
</div></section>"""


def _final(lang, t):
    return f"""<section class="section navy"><div class="wrap">
  <div class="finalcta"><span class="eyebrow" style="color:#7FD4D0">CruiseLine Advisors</span>
    <h2>{t['final_h2']}</h2><p>{t['final_sub']}</p>{big_call(lang, 'final')}</div>
</div></section>"""


def render(lang):
    t = T[lang]
    return (_hero(lang, t)
            + wave_divider("white", "var(--sea3)")
            + _why(lang, t)
            + when_to_go(lang)
            + cabin_guide(lang)
            + _compare(lang, t)
            + _lines(lang, t)
            + _destinations(lang, t)
            + wave_divider("sea", "var(--cream)")
            + _final(lang, t)
            + scroll_companions())
