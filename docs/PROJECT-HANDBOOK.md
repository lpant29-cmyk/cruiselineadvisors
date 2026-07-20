# CruiseLine Advisors — Project Handbook (A–Z)

> The single place to understand this project end to end. If you're reading this a year from now
> and know nothing about it, start here. Last major update: 2026-07-20.

---

## 1. What this is (in one paragraph)

**CruiseLineAdvisors.com** is a bilingual (English/Spanish) **lead-generation referral website** for
cruise travel. It publishes *verified* cruise information. The **only** thing we want a visitor to do
is **call the phone number**. Calls route to licensed independent partner travel agencies who quote,
book and take payment. We earn a **referral fee**. We do **not** sell travel, book travel, take
payment, hold inventory, set prices, or hold cruise-line appointments. Traffic is ~100% paid search
(Google Ads) on cruise-line brand keywords, mostly mobile.

- **Live site:** https://cruiselineadvisors.com
- **Entity:** BookMeCheapest LLC (Florida), in travel since 2015.
- **Brand:** CruiseLine Advisors.
- **Accounts:** Google properties (Search Console, Tag Manager, Analytics/GA4) are under
  **gocaribbea@gmail.com**. **Microsoft Clarity** is under a *different* account:
  **helpdesk@bargainairticket** (bargainairticket.com). See §6 for details.

The authoritative product brief is `docs/BRIEF.md`. The build/agent rules live in `CLAUDE.md`.

---

## 2. The Seven Hard Rules (never break these)

These exist because we run paid search on brand keywords — breaking them risks FTC deception, state
seller-of-travel law, TCPA and trademark exposure, and the Google Ads account.

1. **No fares, prices, rates, discounts, savings, or "from $X" anywhere.** The build guard scans
   generated `<main>` content and fails the build on a hit. *Exception:* published fees (e.g. daily
   gratuities) are allowed, always with a source + verified date, wrapped so the guard ignores them.
2. **Never imply cruise-line affiliation.** Every page carries a disclaimer naming the specific line.
3. **Never invent a fact.** Unverified fields render as a visible "Not yet verified" gap — never a
   guess, default, or em dash.
4. **Never copy prose from a cruise-line site.** Facts are extractable; sentences are not. All
   descriptive copy is original.
5. **Never fabricate people, teams, credentials or sales figures.** Advisors work for partner
   agencies, not us.
6. **Never claim 24/7.** Real coverage hours are **8am–11pm ET, every day**.
7. **Never present a fact past its refresh window as current.** The build flags stale data.

---

## 3. Architecture

```
data/*.json + data/ships/*.json   →  SINGLE SOURCE OF TRUTH (facts + source URL + verified date)
        ↓
*.py generators (build.py orchestrates)
        ↓
newsite/dist/**/*.html            →  100% generated. NEVER hand-edit HTML.
        ↓  (copied to)
site/**                           →  what the live host serves
```

**If a page is wrong, fix the JSON or the generator — never the HTML.**

- Everything lives under `newsite/`. The generator writes to `newsite/dist/`.
- `site/` (repo root) is the deploy copy the host serves. It is a straight copy of `newsite/dist/`.
- Clean URLs: pages are emitted as `<path>/index.html` and served at `/<path>/`. Bilingual under
  `/en/…` and `/es/…`. The bare root `/` is a redirect page to `/en/`.

### Key data files (`newsite/data/`)
- `cruise-lines.json` — the 8 launch lines, per-field `{value, source, verified}`.
- `deployment.json` — 10 US/Canada cruise regions: id, name, season, months, home ports, lines.
  **This is the source of truth for destinations AND the finder's region/ship matching.**
- `ships/*.json` — one file per line; 131 ships with specs + an enriched `exp` block (overview,
  dining, activities, entertainment, kids_family, deploy_note = itinerary, neighbourhoods, …).
- `directory.json` — the wider list of lines boardable from the Americas.

### Important generator modules (`newsite/`)
- `build.py` — orchestrator. Emits every page, runs the banned-term guard, writes sitemap.xml +
  robots.txt, copies assets. Run it to rebuild the whole site.
- `base.py` — the page shell: `<head>` SEO, analytics snippets, inlined CSS, header, footer.
- `config.py` — **single source of truth for constants**: phone number, brand, analytics IDs,
  Search Console token, languages.
- `theme.py` — ALL CSS (inlined into every page).
- `header.py` / `footer.py` / `cta.py` — chrome. Header has nav + search + click-to-call.
- `pages.py` — most page builders (lines hub, line page, ship page, compare, facts, destinations,
  guides, updates).
- `linepage.py` / `experience.py` / `shipcompare.py` — rich line-page and ship-page sections.
- `metasearch.py` — the "Find a cruise" finder (client-side, region + party filtering/ranking).
- `search.py` — site-wide header search (client-side index over every page type).
- `destpage.py` — rich destination guides.
- `kids.py` — fleet-wide kids/teens/family club data, rendered as cards on every ship.
- `facts.py` — the 12 money/complex comparison facts, per line, verified.
- `badges.py` — the "Independently verified" seal.

### Build & deploy (the exact steps)
```bash
cd newsite
python3 build.py                 # regenerate dist/ (must end "✓ banned-term guard clean")
python3 tests/test_regions.py    # itinerary/region integrity
python3 tests/test_party.py      # finder "who's travelling" ranking
python3 tests/test_search.py     # site search
cd ..
rm -rf site && cp -r newsite/dist site
git add newsite site && git commit -m "…"
git push origin main             # the host auto-deploys `main` in ~1–3 minutes
```
**Never deploy without approval. Never push a build with banned-term hits or failing tests.**
The live host caches HTML at the edge (~5 min); hard-refresh (Cmd/Ctrl+Shift+R) to see changes.

---

## 4. What's built (feature inventory)

- **Cruise line pages** (8) — verified specs, the 12 money facts, cabins, families/kids,
  accessibility, a line-vs-line compare tool at the top, an "Independently verified" seal.
- **Ship pages** (131) — hero with seal, a ship-vs-ship compare tool at top, a **table of contents**,
  verified basics, rich experience sections (dining, things to do, entertainment, **kids & families**,
  districts, where & when it sails with scenery imagery), sister ships.
- **Ship directory** (`/ships/`) — every ship grouped by line; reachable from the "Cruise Lines"
  nav submenu (All cruise lines · Ship directory).
- **Find a cruise** finder (`/compare/`) — filter by region, home port, month, and "who's
  travelling"; results ranked and deep-linked; compare tray.
- **Site-wide search** — header 🔍 (or `/` / ⌘K): lines, ships, fact topics, destinations, guides,
  updates. Index built from the same data as the pages.
- **Destination guides** (`/destinations/<region>/`) — quick facts, what to expect, best-time month
  strip, home-port photo cards, typical ports of call, **ships that sail here** (grouped by line),
  which-line-fits, document practicalities, FAQ (with FAQPage structured data).
- **Cruise facts**, **guides**, **updates**, **legal** pages.

### Known honest gaps (intentional, not bugs)
- Real **call-tracking phone number** not set yet — placeholder `+1 (888) 555-0142` in
  `config.py` (`PHONE_DISPLAY` / `PHONE_HREF`). Swap in one place when ready.
- ~25 ships have no published itinerary captured, so they're excluded from the finder (accuracy
  over coverage); still reachable via line pages and search.
- Some Spanish deep-content and a few per-ship detail fields remain to be filled; they show as
  visible "Not yet verified" gaps, never guesses.

---

## 5. SEO — on-page status

On-page SEO is built into `base.py` and applies to **every** generated page:
- Unique `<title>` and `<meta name="description">` per page.
- `<link rel="canonical">` + `hreflang` alternates for en/es + `x-default`.
- `robots: index,follow,max-image-preview:large`.
- Open Graph + Twitter card tags, `og:image` (1200×630).
- JSON-LD: Organization site-wide; FAQPage on destination pages; breadcrumb-friendly URL structure.
- `sitemap.xml` and `robots.txt` are generated on every build (robots points to the sitemap).
- Mobile-first, fast (CSS inlined, fonts deferred), accessible (skip link, focus states).

**Submit `https://cruiselineadvisors.com/sitemap.xml` in Search Console after verification.**

---

## 6. Analytics & tag management — SETUP (account: gocaribbea@gmail.com)

All four tools are wired to be **config-driven**: paste an ID into `newsite/config.py`, rebuild,
and deploy — the snippet then renders on every page automatically. Nothing tracks until IDs are set.

### 6a. Google Search Console — DONE (verification method: HTML tag via Claude Code)
- **Property/URL:** https://cruiselineadvisors.com/
- **Verification method used:** **HTML meta tag injected into the site by Claude Code** —
  *NOT* the GoDaddy DNS/domain route.
- **Tag (kept permanently — Google re-checks it):**
  `<meta name="google-site-verification" content="riSdvugiyK2ysSxGBWNBloIRKzeSaYWfwZHUQgZF2d4">`
- **Where it lives:** `config.py → GSC_VERIFICATION`; rendered in `<head>` of every page **and** the
  root redirect page (`/`), which is the exact URL Google checks. Deployed 2026-07-20 (commit
  `bd09a67`).
- **Do NOT remove this token.** If it's ever removed, verification fails and the property drops.
- **Next steps for the operator:** in Search Console, click Verify; then submit the sitemap
  (`/sitemap.xml`); then use URL Inspection to request indexing of key pages.

### 6b. Google Tag Manager — LIVE
- **Container ID:** `GTM-NM78WCVF` (account gocaribbea@gmail.com). Set in `config.py → GTM_ID`.
- Renders the GTM script high in `<head>` and the `<noscript>` iframe immediately after `<body>` on
  every page. Deployed 2026-07-20 (commit `bd77979`), verified live.
- **GA4 is fired INSIDE this container** — there is deliberately **no** separate `gtag.js`/GA4
  snippet anywhere (`GA4_ID` is blank) so events are never double-counted. Do not add one.
- A custom event **`call_click`** is pushed to `dataLayer` whenever a phone link is tapped (with
  `placement` and `lang`). In GTM, make a Custom Event trigger on `call_click` → this is the
  **primary conversion (a lead)**. Send it to GA4 as a key event and import to Google Ads.

### 6c. Google Analytics 4 — via GTM (no separate snippet)
- GA4 is configured **entirely inside the GTM container** above. `config.py → GA4_ID` is
  intentionally left blank; the generator emits no `gtag/js` script. If GA4 ever needs to be
  hard-coded instead, put the `G-…` ID in `GA4_ID` — but then remove the GA4 tag from GTM first.
- In GA4, mark `call_click` as a **key event / conversion** and link GA4 to Google Ads.

### 6d. Microsoft Clarity — LIVE
- **Project ID:** `xpb1uyu7ta`. **Account: helpdesk@bargainairticket** (bargainairticket.com) —
  NOT the gocaribbea Google account. Set in `config.py → CLARITY_ID`.
- Renders in `<head>` on every page. Deployed 2026-07-20 (commit `bd77979`), verified live. Gives
  heatmaps + session recordings — useful for seeing why mobile visitors do/don't call.

### 6e. Google Ads (context)
- Traffic is ~100% paid search on brand keywords. The conversion to optimise is the **phone call**
  (`call_click`), imported from GA4 or tracked via GTM. Consider Google's call-tracking / call
  extensions once the real tracking number is live.

---

## 7. Conventions & pitfalls (for anyone editing)

- Verification is **per field**, never per page: every fact stores `{value, source, verified}`.
- Refresh windows: `inclusions` 30 days, `itineraries` 60, everything else 90, NOAA 365.
- One generator, never per-line template forks — fixes apply everywhere.
- Design tokens are fixed (see `docs/BRIEF.md §11`): Fraunces for display headings, Inter for UI.
- **JS pitfalls that have bitten us:** wrap every client script in its own IIFE with a null guard on
  line one (a reference to a removed element throws and kills every later script on the page);
  beware duplicate element IDs; the sticky header + breadcrumb bar own the top z-index band — use
  `scroll-margin-top` on anchors so they aren't hidden.
- Price-guard false positives: "discounts" legitimately appears in the footer disclaimer, so the
  guard scans only `<main>` and strips scripts + fee spans first.

---

## 8. Change log (high level)

- **2026-07-20:** Finder region-integrity fix (ships now matched to regions only from their own
  itinerary); "who's travelling" ranking made effective; site-wide search; ship directory + nav
  submenu; bigger verified seal; kids sections made rich fleet-wide + Anthem/Quantum sourced;
  per-ship table of contents; rich destination guides + 4 new region pages; Search Console
  verification live; GTM/GA4/Clarity wiring added (config-driven). Later same day: logo tagline
  ("Verified cruise facts. One call books it."); destination **photo heroes** (12 self-hosted
  region images — credits in `docs/hero-image-credits.json`, all Pexels License / commercial /
  no attribution); described ports-of-call cards; "Explore more destinations" cross-link grid.
- Earlier: initial bilingual rebuild — 8 lines, 131 ships, facts store, compare tools, finder,
  self-hosted port photos, verified seals.

---

## 9. Quick answers

- **How do I change the phone number?** `config.py → PHONE_DISPLAY` + `PHONE_HREF`, rebuild, deploy.
- **How do I add an analytics tool?** Paste its ID into `config.py`, rebuild, deploy.
- **A page shows wrong info?** Fix the JSON/data or the generator — never the HTML.
- **How do I see changes after deploy?** Hard-refresh; the edge cache is ~5 minutes.
- **Where's the sitemap?** `https://cruiselineadvisors.com/sitemap.xml` (regenerated every build).
