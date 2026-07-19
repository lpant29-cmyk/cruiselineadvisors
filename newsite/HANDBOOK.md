# CruiseLine Advisors — Internal Handbook

> **Private / noindex.** This file documents the NEW site in `newsite/`. It is never deployed
> (it lives outside `dist/`, so it is never served or indexed). Update the Changelog at the bottom
> on every deploy.

---

## 1. What this is

A bilingual (EN/ES) lead-generation cruise resource. **The only conversion metric is inbound phone
calls.** We publish genuinely useful, verified cruise information; visitors call a phone number;
calls route to licensed independent partner agencies who quote, book and take payment. We earn a
referral fee. **We do not sell travel, book, take payment, set prices, or hold cruise-line
appointments.** Traffic is ~100% paid search, mobile-heavy.

Live site: https://cruiselineadvisors.com

## 2. Why this rebuild exists (read `memory/hosting-and-lost-generators`)

The repo's OLD generators (`build_deep.py`, `build_site.py`, `home_rich.py` at repo root) are
**stale** — the deployed `site/*.html` was built by a newer generator version that was never
committed, and running the old ones **downgrades** the design. So we rebuilt fresh in `newsite/`
with a clean, drift-proof pipeline. **Do NOT run the old root generators and deploy their output.**

## 3. Architecture

```
newsite/
  config.py        SINGLE SOURCE: phone, brand, hours, SITE_URL, languages
  i18n.py          all EN/ES UI strings
  theme.py         the whole design system (one inlined stylesheet)
  logo.py          the SVG logo (one file)
  header.py        header / nav / language switch (one file)
  footer.py        footer + compliance disclaimers (one file)
  base.py          page shell: <head> SEO (canonical, hreflang, OG, Organization JSON-LD), fonts
  cta.py           call buttons + sticky mobile call bar
  scene.py         animated ocean, dolphins, wave dividers, scroll-ship
  navigator.py     interactive Cruise Finder (where→when→who→call)
  interactive.py   "when to go" + "which cabin" interactive sections
  compare.py       data-driven comparison tool
  facts.py         THE COMPARISON DATA SHEET (single source for the 12 money/complex facts)
  data.py          8 lines, 8 destinations
  pages.py         all content-page builders
  legal_pages.py   Terms / Privacy / Consent(TCPA) / Do Not Sell — bilingual
  build.py         orchestrator → dist/ + sitemap.xml + robots.txt + 404 + banned-term guard
  dist/            GENERATED OUTPUT (en/ + es/ + root redirect). Never hand-edit.
```

**Data → generator → HTML.** Fix content in the data/generator, never in `dist/`. `facts.py` powers
BOTH the comparison tool AND every line page, so verifying a fact once updates everywhere.

## 4. Build & deploy (Render)

- Build: `cd newsite && python3 build.py` → writes `newsite/dist/`. Pure Python stdlib, no deps.
- Hosting: **Render**, auto-deploys the GitHub repo `lpant29-cmyk/cruiselineadvisors` on push to
  `main`. Confirm in the Render dashboard whether it serves a committed folder or runs a build, and
  set the **publish directory to `newsite/dist`** (or run `python3 newsite/build.py` as the build
  command with publish `newsite/dist`) when we cut over.
- **Cutover plan (not done yet):** keep the live `site/` untouched until approved; then point Render
  at `newsite/dist` (or copy `dist/*` into the served folder) and push. Never blank the live site.
- Every deploy: build must print `✓ banned-term guard clean`; then add a Changelog entry below.

## 5. The seven hard rules (immutable)

1. No fares/prices/rates/discounts/savings/"from $X" anywhere. Build guard scans each `<main>` and
   fails on a hit. (Exception: published fees like daily gratuity, always with source + verified date.)
2. Never imply cruise-line affiliation. Every line page carries a disclaimer naming that line.
3. Never invent a fact. Unverified fields render a visible "Not yet verified" gap — do not fill or hide.
4. Never copy prose from a cruise-line site. Facts are extractable; sentences are original.
5. Never fabricate people, teams, credentials or figures.
6. Never claim 24/7. Real hours: 8am–11pm ET daily (in `config.HOURS`).
7. Never present a fact past its refresh window as current.

## 6. Facts verification (the 30-day cadence)

- The 12 facts × 8 lines live in `facts.py` → `LINE_FACTS[slug][key] = {v, src, verified}`.
- **Source the real value by actually reading the source page** (not a search snippet). Record the
  source URL and the ISO date verified. If a source page can't be read (JS app / login / blocked),
  **leave it None and ask the user to read it** — never guess.
- Refresh window: **30 days** for these facts (they change often). Re-verify from the same source and
  update `verified`. A future guard should flag any cell older than 30 days.
- `build.py` prints `facts verified: N/96` so coverage is always visible.

## 7. SEO / performance / accessibility

Per page: `<title>`, meta description, canonical, `hreflang` (en/es/x-default), Open Graph, Twitter,
Organization JSON-LD, `theme-color`. Site: `sitemap.xml`, `robots.txt`, `404.html`. CSS is inlined
(no render-blocking); fonts load async (preconnect + `media=print` swap + `<noscript>`). Skip link,
single `<main>`, keyboard-operable nav/finder, reduced-motion honored, mobile verified at 360–390px
with zero horizontal overflow. Run Lighthouse before cutover and record scores here.

## 8. Before any deploy — checklist

- [ ] `python3 build.py` prints guard clean
- [ ] No banned terms; every rendered fact traces to a source URL + verified date (or shows the gap)
- [ ] Placeholders replaced: real phone in `config.py`; `[Your Company] LLC`, `[Street Address]`,
      `[privacy@yourdomain.com]` in `footer.py` / `legal_pages.py`
- [ ] Mobile checked at 360px; language switch works EN↔ES on the page you changed
- [ ] Changelog entry added below

## 9. Known TODO before launch

- **Real tracking phone number** (currently placeholder `+1 (888) 555-0142`).
- **Facts sourcing**: 0/96 verified — do the sourcing pass; flag unreadable sources to the user.
- **Company legal details**: fill `[Your Company] LLC`, address, privacy email.
- **Spanish review**: legal/compliance ES copy should get a native-speaker review.
- **OG image**: add a shareable image + `og:image` (optional; not a Lighthouse factor).
- **Render cutover**: point publish dir at `newsite/dist`.

---

## Changelog

- **2026-07-18** — New site scaffolded in `newsite/`. Homepage (EN+ES) with animated ocean hero,
  interactive Cruise Finder (hero on desktop / right drawer on mobile), when-to-go + cabin interactive
  sections, data-driven comparison tool, playful cards, scroll-ship. All 33 page types × 2 languages
  built (66 pages) + root redirect + 404 + sitemap.xml + robots.txt. Banned-term guard clean. Facts
  0/96 verified (sourcing pending). NOT yet deployed — live `site/` untouched.
