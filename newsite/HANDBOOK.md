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

- **2026-07-28** — LP SYSTEM scaffolding (branch `lp-system`, Royal Caribbean scope, no pages built,
  live site untouched). Appended an "LP SYSTEM" section to root `CLAUDE.md` pointing at
  `lp-system/blueprint/`. Created six agents in `.claude/agents/` (manager, qa-auditor,
  pricing-scout, page-builder, photo-curator, research-registrar) alongside the existing
  keyword-scout + structure-guard. Created `lp-system/scripts/`: `collect.py` (three-pass model:
  Pass C price fetch with cache + candidate diffs, Pass A/B worklists), `validate.py` (price band
  $99–$25,000, ±25% swing vs git HEAD, stamp/staleness >10d, expired offers, ≥3-deals-per-page;
  writes `HOLD-{date}.md`, non-zero exit on flags), `generate.py` (bakes CSV data into both the
  call-gen RATES-DATA and finder PAGE-PARAMS template contracts; VERIFY-BEFORE-PUBLISH rows never
  render; preview output by default, `--deploy-dir` for real deploys), `propose_pages.py` (computes
  facet combos, ≥3-itinerary + next-6-months thresholds, identical-set dedupe, retire suggestions;
  never edits 09_pages.csv), `notify.sh` (ntfy/email run reports). All scripts smoke-tested against
  seed data: guards correctly refuse the seed/example rows. Pending same-commit-as-first-/go/-page:
  ADS-LP-BRIEF §6 footer/terms pricing-disclosure change. Next: keyword-scout run on
  `lp-system/data/kw_raw/` (10 Keyword Planner exports, UTF-16 TSV, exact volumes).

- **2026-07-29** — LP SYSTEM: provenance + Galveston data + tracking layer (branch `lp-system`,
  nothing deployed). (1) DATA PROVENANCE POLICY added to research-registrar, pricing-scout and
  qa-auditor; whitelist at `lp-system/data/source_whitelist.txt`; enforced in validate.py (off-whitelist
  or UNVERIFIED rows can never publish) and mirrored as a render gate in generate.py. Seed rows with
  source=public-site now correctly fail. (2) research-registrar Pass A/B (official-only): 16 live RC
  Galveston itineraries from royalcaribbean.com's own GraphQL endpoint; i0003/i0004 corrected (Icon
  is 2027-08+ at Galveston, not 2026), 14 new rows i0005-i0018, 3 ships added, 120 day-by-day rows,
  7 call-port stubs. Prices left for pricing-scout Pass C (launched, in progress). (3) TRACKING:
  /go/ pages were inheriting NO tags (LP templates bypass newsite/base.py). generate.py now injects
  the identical stack, IDs imported from newsite/config.py: GTM-NM78WCVF (head + noscript), Clarity
  xpb1uyu7ta direct, GA4/Ads via GTM as on the main site; dataLayer vars (page_type, page_id,
  lp_variant, lp_when, line, port, dest) pushed before GTM; events tel_click{page_id,position} and
  lead_submit{page_id,form_mode} with thank-you state. (4) tracking-guardian agent created,
  registered in manager's gate + Monday health check; its first audit found and page-builder fixed:
  finder cards missing from position map, finder template missing the callback form entirely.
  qa-auditor DoD extended with the tracking checklist. Access requests in lp-system/tracking-access.md.

- **2026-07-29 (later)** — LP SYSTEM: pilot p002 built + conversion architecture. Pricing-scout Pass C:
  all 16 Galveston rows priced from royalcaribbean.com's official endpoint (evidence in
  lp-system/out/candidates-2026-07-29.csv); i0003/i0004 +32%/+36% swings HELD for qa-auditor; real
  flash-sale offer o002 replaced the o001 example. Structure-guard cleared p002 (14 publishable,
  9 within 6 months) -> status building. Page-builder restyled the finder template to the site design
  system (Fraunces/Inter, navy #0A2540, teal/gold/coral tokens; DOM and tracking hooks untouched) and
  baked p002 to lp-system/out/preview/ (39KB). tracking-guardian audit #2 caught T6 (baked PAGE object
  missing lineLabel/portLabel, finder cards never rendered at runtime) -> fixed in generate.py.
  Operator conversion ruling implemented: exactly 3 conversions (calls-from-ads account-level;
  tel_click SECONDARY via GTM + Conversion Linker; website-calls 30s+ PRIMARY via _googWcmGet DNI
  CALLBACK with MutationObserver re-apply, never static swap) — module injected by generate.py,
  guardian spec extended incl. main-site inactive-call-conversion diagnostic note. Preview artifact
  published (private). Still blocking DoD: placeholder phone/form action/policy links, i0003 HOLD,
  qa-auditor APPROVE. Nothing committed or deployed.

- **2026-07-29 (evening)** — LP SYSTEM: itinerary architecture + completeness pass. Registrar verdicts
  (official evidence in lp-system/out/verification-2026-07-29.md): Mariner 9N MA09W208 NOT bookable
  (stale artifact, RC 307-redirects it; 9+ band = Liberty 9N + Symphony 10N only); Harmony has zero
  future Galveston sailings (all Port Canaveral thru 2028-04) -> p002--harmony AND p002--allure ad
  groups annotated PAUSE-AT-LAUNCH. Enrichment: port currencies from official pages, Galveston
  pre_cruise from portofgalveston.com, FAQ q001 verified vs cbp.gov. Photo-curator: 8 slots filled,
  licensed (Pexels/Unsplash, license evidence per row; 7 candidates rejected for real-ship livery).
  Itinerary detail pages ruled in: structure-guard rules added (>=1 row threshold, one-match keyword
  rule), pilot p007 registered (5N Mariner). Page-builder: finder completeness (assets via registry,
  route ribbons, day expanders + currency chips, ship module, pre-cruise tab, docs line, detailUrl
  CTA) + new itinerary-detail template + generator branch; p002 71KB / p007 36KB, jsdom-clean.
  Keyword-scout: 32 rows got ?nights= keyword-level final URLs; pause annotations; 2 single-match
  Symphony-7N keywords tagged FUTURE-ITIN-PAGE. validate.py HOLD file now append-only (re-runs were
  wiping qa arbitrations). Screenshots: lp-system/out/screenshots/ p002+p007 x desktop-1440/mobile-390.
  Pending: guardian audit #4, qa re-gate, operator inputs (tracking number, CRM endpoint, policy
  pages, §6a wording). Nothing committed or deployed.

- **2026-07-29 (re-gate)** — LP SYSTEM: guardian audit #4 TRACKING PASS on both pages (24/24 and
  21/21 jsdom checks; drift explained; .fares position ruling confirmed). qa-auditor re-gate:
  i0005 arbitrated CONFIRMED-AT-SOURCE (third independent fetch, 16/16 rows re-matched); both pages
  HOLD on operator inputs (tracking number, CRM endpoint, policy pages, §6a taxes ruling) + finds:
  i0009 Aug/Sep-2026 false interior-fare fallback (FIXED in generate.py: balcony-only months are
  dropped from interior display; template renders "Call for fare" on null), s001 Icon + 01_lines
  rows render while unsourced (registrar task queued), q001 Bahamas wording ruled accurate but
  generalization queued. Screenshots retaken post-fix: lp-system/out/screenshots/. Nothing committed
  or deployed; pages stay status=building pending operator inputs.

- **2026-07-29 (master enrichment, phase 1)** — LP SYSTEM: ship-data unification + parity + assets.
  Ship dataset located: newsite/data/ships/royal-caribbean.json (30 ships, official fact sheets,
  exp{} with dining/activities/entertainment) becomes the SINGLE source for LP ship content (LP
  registry = view, join by ship_id; structure-guard SHIP PAGES rule added; p008 Mariner ship page
  registered). Registrar enriched Mariner exp from six loaded official pages: kids_bands (Adventure
  Ocean 3-11 + nursery + Teen Lounge), spa (Vitality), shopping, cabins categories + quad honesty
  gap; casino left null (not stated officially, not invented). s001/s002 verified+sourced;
  01_lines rci deposit/kids notes rebuilt from official FAQ pages with source columns; q001
  generalized to closed-loop wording; royalcaribbeanmedia.com whitelisted (first-party confirmed).
  Photo-curator: registry to 31 rows, 13 new files (7 section variants + 6 new subjects, Pexels
  license-verified, people-in-frame), trade_portal_upgrade column filled. Parity check vs the
  official 5N Mariner product page (SSR-verified): core content parity; theirs-only = transactional
  features by design; ours-richer = provenance stamps/FAQ/why-call/disclosures; one gap adopted
  (route schematic, building as our own SVG). validate.py: ship pages now >=1 threshold.
  In flight: page-builder ship template v2 + photo-story rework + rebakes; then gates + screenshots.

- **2026-07-29 (master enrichment, phase 2)** — LP SYSTEM: three-page build gated. Page-builder:
  ship-detail.html template v2 (15 sections, dataset-fed, casino honestly absent, cabin advice
  voice, inline call prompts), p007 photo-story (journey images, own-design SVG route schematic,
  ?when= incl. next-month), p002 ship tabs; ships-view loader joins newsite/data/ships/*.json by
  ship_id. Guardian audit #5: TRACKING PASS x3 (72 checks, ship dataLayer key accepted, byte-level
  drift proof); post-audit mobile full-bleed fix (.jday/.msec calc(50%-50vw), 20px overflow at 390
  eliminated) verified zero tracking drift. LIVE CONTAINER DISCOVERY (real-browser diagnostic):
  GTM-NM78WCVF already fires GA4 G-JTQWHFMTB8 + Ads AW-18339104693, and throws "gtag is not
  defined" (a container tag calls gtag() no page defines) — prime suspect for the main site's
  inactive website-call conversion; recorded in tracking-access.md. QA audit #6: p008 structure/
  provenance PASS (kids bands/spa/shopping/cabins verified at official sources; zero leakage);
  page weights pass; NEW finds: i0008 Aug fare moved at source ($590->$751, refresh dispatched),
  costa-maya row renders with empty source (503s; registrar retry dispatched). All three pages
  HOLD pending those two fixes + the four standing operator inputs. Screenshots (scroll-aware
  Playwright, all images decoded): lp-system/out/screenshots/ x6. Nothing committed or deployed.

- **2026-07-29 (master enrichment, CLOSED)** — LP SYSTEM: final gate green. i0008 re-fetched and
  arbitrated CONFIRMED-AT-SOURCE (Aug interior 590->751, cause: cheapest sailing dropped interior;
  three independent fetches agree). costa-maya resolved honestly: currency/highlights emptied,
  blurb trimmed to the one traceable fact, UNVERIFIED note; generator suppresses all content on
  UNVERIFIED rows. Final qa verdicts: p002, p007, p008 all APPROVE-PENDING-OPERATOR-INPUTS —
  blocked from live ONLY by: real tracking number, real callback endpoint, real legal pages +
  TCPA link, §6a taxes-wording ruling. .claude/settings.json created (scoped allowlist: lp-system
  + .claude edits, LP scripts, read-only shell, git add/commit/status/diff, WebFetch limited to
  the source whitelist + photo APIs; git push hard-denied). Fresh screenshots x6 in
  lp-system/out/screenshots/; live previews served locally. Nothing committed or deployed.

- **2026-07-29 (footer ruling)** — SHARED LEGAL PARTIAL: newsite/legal_partial.py is now the single
  source for the five legal blocks (what-we-are, trademarks, pricing, verification, photography) +
  the §6a fares paragraph + the legal-links list. newsite/footer.py and the LP generator both
  consume it; §6b pricing sentence sitewide ("fares shown anywhere on this site are indicative..."),
  §6c mirrored in the Terms clause (EN+ES), §6a appended only on fare-showing /go/ pages. LP footers
  compact (legal blocks + real /en/legal/ links + phone, no nav columns); TCPA fine print now links
  the consent page — clears the href="#" items from qa's T5 gate. Verified: blocks byte-identical
  across main-site footer and all three /go/ bakes; newsite build guard clean (380 pages, 96/96
  facts). One legal edit now updates every page on both surfaces. Next in flight: mobile UX redesign
  pass (sliders, bottom sheets, scroll-reveal) on all three /go/ templates.

- **2026-07-29 (mobile UX redesign, CLOSED)** — All three /go/ pages rebuilt for mobile per operator
  ruling: day-by-day = scroll-snap slider (85vw + peek, day dots, bottom-sheet disclosure, route
  schematic below); finder = compact rows + featured slider + deal sheets (route ribbon, month
  fares, both CTAs); ship-life = 43vw tile sliders opening fact sheets on p007/p008. Motion:
  IO scroll-reveals (once), 200ms sheets, CSS-only snap, full prefers-reduced-motion fallback
  (incl. 240ms timer for transition-free sheets). Four sheet-dismiss paths. Guardian audit #6:
  TRACKING PASS x3 (84 checks; .sheet-deal->deal-card ruled; sheet-day/life->'other';
  MutationObserver DNI re-swap in fresh sheet DOM proven; drift = exactly one POS line, then
  ZERO drift on the fix rebake, byte-for-byte). QA audit #7 found+we fixed: D1 legal links now
  clean directory URLs (targets verified on both deploy trees), D2 tile peek guaranteed (43vw,
  10.6px peek at 390 / holds 360-430). FINAL VERDICTS: p002/p007/p008 all
  APPROVE-PENDING-OPERATOR-INPUTS. Operator inputs now THREE: tracking number, callback endpoint,
  §6a taxes ruling. Review media: lp-system/out/screenshots/ = 6 PNGs + 3 mobile interaction
  recordings (scroll + swipe + sheet open). Weights 89.0/64.6/64.3 KB. Nothing committed/deployed.

- **2026-07-30 (mobile polish pass, CLOSED)** — External-audit fix list, all 10 items done + gated.
  Root cause of the phantom sheet found (off-state was translate-only with pointer-events auto;
  now visibility:hidden + pointer-events:none, verified computed-hidden at both viewports).
  Slim headers with phone icon-button ≤480 (incl. p002, accepted); hero fare nowrap; 2-screen top
  stack (one-line disclosure w/ no-JS-safe collapse, callback behind "Prefer we call you?");
  p002 true one-line rows + Show-all expander (stamp coverage = list-level + sheet, qa-accepted
  w/ condition N1: fail on mixed-date bakes); coral confined to sticky/hero/sheet CTAs (soft-gold
  offer ribbon, phoneband white-outline accepted); deposits as mini-tables (cell-checked vs
  01_lines); fare table 2-col + Interior/Balcony toggle + single deal-card CTA; route ribbon
  removed; kickers hidden. Guardian #7/#8: zero unexplained drift; found T-ARIA-DNI (aria-label
  kept base number after DNI swap = silent SR undercount of the primary conversion) -> fixed in
  applyAll, proven byte-exact, re-baselined; clean TRACKING PASS. QA audit #9 (HOLD-2026-07-30.md):
  APPROVE-PENDING-OPERATOR-INPUTS x3. Blockers: tracking phone, callback endpoint, §6a ruling +
  GTM setup at go-live. Six fresh screenshots; weights 94.6/72.3/70.3 KB. Nothing committed/deployed.

- **2026-07-30 (design batch + compliance fixes)** — Operator design changes: top disclosure BAR
  removed; main-site logo lockup (newsite/logo.py SVG) in the slim header, not linked; back-to-top
  + header Back button; ship-tab and finder-card imagery varied (LRU over licensed generic/port
  assets); ddpulse on day-by-day controls; phoneband H2 white (was invisible navy-on-navy);
  9 internal-sourcing strings rewritten to guest-facing copy. BUGFIXES: route ribbon overlapped on
  5+ port itineraries (chips shrank under flex nowrap) -> fixed-size ports/legs + horizontal scroll,
  label cap 78->120px, verified 0 overlap / 0 clipped across ALL 16 deal sheets; mobile day-by-day
  had disappeared entirely from p002 (rows lost the expander in the polish pass, sheet never gained
  it) -> full day list restored in the deal sheet, desktop parity verified.
  GATES: guardian audit #9 CLEAN PASS (141/141, zero drift, NAV_UI_JS proven tracking-inert) and it
  caught that the Back button's history.length>1 condition would render on a paid SERP click,
  putting a one-tap route back to the ad in the header -> restricted to same-origin referrer only,
  Chrome-verified absent on direct landing / present after internal nav. QA audit #10 filed THREE
  blockers, all now fixed: D-A the disclosure had ZERO unobstructed pixels above the fold (sticky
  bar covered it) -> moved into the hero above the H1, re-verified unobstructed at 360/390/430/1440;
  D-B the copy rewrite had turned honest gaps into FALSE claims about Royal Caribbean (qa proved
  deck plans and Casino Royale ARE published) -> all four sentences now assert only what WE have
  verified; D-C p008 2-vs-3 deal rows resolved as already-ruled (SHIP PAGES threshold is >=1;
  qa-auditor DoD reconciled). Also N-1/N-2/N-3/N-4/N-6. Weights ~100/75/73 KB. Operator inputs
  unchanged: tracking number, callback endpoint, §6a wording (+ deploy-day price refresh, N-7).

- **2026-07-30 (ALL THREE PAGES APPROVED)** — Final fixes: hero eyebrow chip was wrapping to 2 lines
  on phones (the "white stripe") and only repeated the H1 -> hidden <=600px, kept on desktop; p008
  sailing cards had day data baked but never rendered -> "Day by day" button opens the sheet with
  full days + currency chips + call CTA; QA found the compliance disclosure was CLIPPED by the
  sticky header on p007 at 360/375px (leaving text that no longer named Royal Caribbean) -> hero
  becomes height:auto/min-height:460px with content padding-top at <=420px, re-verified by QA at
  12 viewports (320-1440), 36/36 clean, clearance 25-246px. Dead .ind-note + .disclose CSS swept.
  QA VERDICTS: p002, p007, p008 all APPROVE. Blocked from live ONLY by the 3 operator inputs
  (tracking number, callback endpoint, §6a wording). Standing deploy-day gates: pricing refresh
  (i0005 balcony moved $566->$703.87 in 24h; the 10-day stamp window is NOT tolerance on this
  inventory), the container's "gtag is not defined" error resolved before spend, GTM setup, and a
  guardian NAV_UI_JS re-baseline at 6ec680ee. Two-screen budget margin narrowed ~150-210px by the
  taller hero (worst case p002@360 has 278px headroom) - QA recorded that the 12-viewport scanline
  check AND the budget must both be re-run after any future above-fold addition.
  Photo policy CHANGED (operator): real cruise-ship stock photography now permitted and preferred,
  choosing framings where ship names and funnel logos are not legible; alt text may never claim a
  specific ship without verification. Sourcing run in progress.

- **2026-07-30 (plan parked, launch scope set)** — Operator decision: do NOT build the automation
  yet. Scope = launch the 3 pilot pages, create the ad campaigns, run the account, refresh prices
  daily; revisit automation after 1-2 weeks of live data. Full architecture saved to
  lp-system/AUTOMATION-PLAN.md (agents are not services -> cloud runner needed; daily price refresh
  is 1 request/port/day because one graph query returns a whole port; the freshness fuse matters
  more than the cadence; ad spend is outside the loop). Real ship photography sourced and wired:
  6 slots (hero/at-sea/docked/balcony/interior/night), ~50 candidates rejected for legible
  branding; night shot left UNUSED as the only asset with any lettering; hero retains a small
  textless deck emblem (~7px on mobile), flagged to operator. Finder now shows 11 distinct images
  across 16 cards, zero adjacent repeats. NOTE: qa approved the pre-image-swap bakes; the asset
  swap wants a provenance spot-check to formally carry approval forward.
