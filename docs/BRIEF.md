# CruiseLine Advisors — Complete Build Brief

Paste this entire file to Claude Code as the project brief. Read it fully before writing code.

---

# 1. What this business is

A **lead-generation referral website** for cruise travel, operated by a Florida LLC that has
been in the travel industry since 2015.

**The model:** the site publishes genuinely useful, independently verified cruise information.
Visitors call a phone number. Calls are routed to licensed independent partner travel agencies,
which quote, book and take payment. The business earns a **referral fee**.

**The business does NOT:** sell travel, book travel, take payment for travel, hold inventory,
set prices, or hold cruise line appointments.

**Traffic:** ~100% paid search, overwhelmingly mobile, targeting cruise-line brand keywords.
The primary conversion metric is **inbound phone calls**.

---

# 2. THE SEVEN HARD RULES

These are build-breaking. Enforce them in code, not just in review.

1. **Never render a fare, price, rate, discount, saving, or "from $X" anywhere on the site.**
   Build a guard that scans generated page `<main>` content for `$`, `USD`, `save `, `discount`,
   `% off`, `cheapest`, `lowest price` and **exits non-zero**, failing the build.
   *Exception:* published **fees** (e.g. daily gratuity) are allowed — a disclosed service charge
   is not a fare — but must always render with a source link and a verified date.

2. **Never imply affiliation with a cruise line.** Every page carries a trademark disclaimer
   naming the specific line: *"Not affiliated with, sponsored by, endorsed by, authorised by,
   or an agent of [Line]. This is not an official site of [Line]."*

3. **Never invent a fact.** Unverified fields render as a visible *"Not yet verified"* gap.
   A gap is acceptable; a guess is not. **Do not remove these gaps, fill them with plausible
   defaults, or hide them behind an em dash.** They are a trust feature and a competitive
   advantage — almost no competitor page has anything comparable.

4. **Never copy prose from a cruise line site.** Facts (numbers, dates, capacities, yes/no)
   are extractable and not copyrightable. Sentences are. All descriptive copy is original.

5. **Never fabricate people, teams, credentials, or sales figures.** No alias advisor names,
   no invented extensions, no "sold 400 cruises". The advisors work for *partner agencies*,
   not this company. Describe the **network and its standards** instead.

6. **Never claim 24/7 or response times you cannot honour.** Publish real coverage hours
   (currently 8am–11pm ET daily). If partners genuinely staff 24/7, then and only then say so.

7. **Never state a fact as current if it is past its refresh window.** The build must flag
   these; fix or remove before publishing.

> These exist because the operator runs paid search on brand keywords. The exposure is FTC
> deception, state seller-of-travel law, TCPA, and trademark. Getting these wrong risks the
> Google Ads account and the entity itself.

---

# 3. Architecture

```
data/*.json          ← SINGLE SOURCE OF TRUTH (facts + sources + verified dates)
      │
      ▼
build_*.py           ← generators
      │
      ▼
site/**/*.html       ← 100% generated static output. NEVER hand-edited.
```

**If a page is wrong, the fix goes in the JSON or the generator — never in the HTML.**

Run order: `build_deep.py` → `build_site.py` → `build_nav.py` → `postprocess.py` → guards.
Wire this into a single `make build` / `npm run build`.

## Existing files to read first

| File | Purpose |
|---|---|
| `data/cruise-lines.json` | 8 launch lines: company, fleet, inclusions, cabins, family, accessibility, itineraries, policies, editorial, FAQs. Every factual field has `source` + `verified`. |
| `data/ports.json` | 37 home ports across the Americas + 17 regions; which regions are reachable from each port and which lines sail there. |
| `data/directory.json` | 36 cruise lines boardable from the Americas, categorised, with `status` (several are `VERIFY`). |
| `data/EXTRACTION-PLAYBOOK.md` | How to source and verify facts. Read before touching data. |
| `build_deep.py` | Deep cruise-line pages. Contains the `BANNED` price guard and staleness report. |
| `build_site.py` | Home, hubs, destinations, guides, legal, updates. |
| `build_nav.py` | Home-port navigator + directory. |
| `postprocess.py` | Injects breadcrumbs, back control, back-to-top into every page. |

---

# 4. Geographic scope

**In scope:** every cruise line boardable from the **United States, Canada, Mexico, the Caribbean,
and Central/South America** (including Antarctica from Ushuaia and Galápagos from Ecuador).

**Out of scope for now:** lines sailing only Europe/Asia/Oceania with no Americas departure.
A directory full of ships the visitor cannot reach is not useful.

## Priority order

**Phase 1 — the 8 launch lines (scaffolded; facts need verifying):**
Royal Caribbean · Carnival · Holland America · Celebrity · Princess · MSC · Cunard ·
Margaritaville at Sea

**Phase 2 — mainstream/premium:** Norwegian · Disney · Virgin Voyages · Oceania · Azamara ·
Viking Ocean · Costa

**Phase 3 — luxury:** Regent · Silversea · Seabourn · Explora · Ritz-Carlton Yacht · Windstar · Crystal

**Phase 4 — expedition & small ship:** Lindblad · HX/Hurtigruten · Quark · Ponant · Aurora ·
Atlas · UnCruise · Alaskan Dream · Ecoventura · Metropolitan Touring

**Phase 5 — river & US coastal:** American Cruise Lines · Viking Mississippi · Pearl Seas ·
American Queen (verify operating status first)

**Regions:** Caribbean (E/W/S) · Bahamas · Alaska · Mexican Riviera · Panama Canal ·
Canada & New England · Bermuda · Hawaii · Transatlantic · South America · Antarctica ·
Galápagos · Amazon · Mississippi · Great Lakes · Pacific Northwest

**Port pages:** one per major home port — dock vs tender, terminal location, walking distance to
town, parking, whether an excursion is genuinely needed, accessibility notes.

---

# 5. TASK 1 — Verification system (build first)

CLI managing the fact store lifecycle.

```
verify.py status              # staleness report, oldest first; EXIT NON-ZERO if anything stale
verify.py next                # the single most urgent record to verify
verify.py show <slug> <block> # current values + source URL
verify.py set  <slug> <block> # interactive: prompt each field, require a source URL, stamp today
verify.py audit               # every field still marked VERIFY
verify.py diff <slug> <block> # what changed at last verification
```

Requirements:

- Verification is **per field or per block**, never per page. Each stores `{value, source, verified}`.
- Refresh windows from `_schema.refresh_days`: `inclusions` **30d**, `itineraries` 60d,
  everything else 90d, climate/NOAA 365d.
- **`set` must refuse to save a value without a source URL.**
- Append-only changelog at `data/changelog.json`:
  `{timestamp, slug, block, field, old_value, new_value, source, operator}`.
  This is the audit trail if a fact is challenged, and it feeds Task 3.
- Validate the JSON against a schema (`jsonschema`) on every write so a malformed edit can't
  silently corrupt the store.
- `status` runs in CI.

## Human-readable verification stamp

Every section rendering facts shows a stamp such as:

> **Verified 14 March 2026** · checked against Royal Caribbean's official *What's Included* page ·
> next check due 13 April 2026

Design it as a small trust component, not fine print.

---

# 6. TASK 2 — Comparison tool (must be fun, not a spreadsheet)

Interactive comparison at `/compare`, generated from the fact store.

- Compare **2–4 lines** side by side; also **ship vs ship** within and across lines.
- Filters: style/positioning, region sailed, family suitability, accessible cabins, solo cabins,
  private destination, sailing length.
- Every cell shows its **verified date**. Unverified cells render as a visible pending state.
- **Like-for-like only.** If one line publishes "double occupancy" and another "maximum capacity",
  flag the mismatch in the UI rather than showing a misleading comparison.
- **The data layer must refuse price attributes.** Attributes carry `compare_safe: true|false`;
  anything false cannot render. Code-level block, not a convention.
- Mobile: stacked swipeable cards, not a squashed table. Desktop: real columns.
- Deep-linkable: `/compare?lines=carnival,princess`.
- Ends in a call CTA; fires `trackCall()`.

Make it feel like a tool: animated column reveals, tap-to-swap lines, a "surprise me" button,
and a sticky bar showing current selections.

---

# 7. TASK 3 — Updates / policy-change system

Dated, sourced log at `/updates`, plus per-line feeds.

- Entries in `data/updates.json`:
  `{date, scope: "line"|"industry"|"regulation", slug, title, summary, what_changed,
    what_it_means, source_url, source_label, verified_by}`
- `summary` and `what_it_means` are **original writing**. Never paste an announcement.
- Generate: main log (reverse chronological, filterable by scope and line) + an
  "Updates affecting this line" block injected into each line page.
- **When `verify.py` detects a changed value on a monitored field** (gratuity rate, inclusions,
  documentation policy), prompt to create a matching update entry. This link is what makes the
  system self-maintaining.
- Emit `/updates.xml` (RSS).

Monitor: cruise line newsrooms · NOAA/NHC · US State Dept · CBP · NPS Glacier Bay · port authorities.

---

# 8. TASK 4 — Home-port navigator (prototyped; productionise it)

Four steps, then fact-based advice, then the call:

1. **Where will you board?** — 37 ports grouped by region. Driving beats flying; say so.
2. **Where do you want to sail?** — only regions genuinely reachable from that port.
3. **When?** — months out of season are visibly disabled, not hidden.
4. **Who's travelling?** — family / couple / group / solo / multi-gen / accessibility needs.

**Result** must give real advice: whether the month works; hurricane-season warning for the
Atlantic June–November; accessible-cabin scarcity warning; kids-club age-band note for families;
group coordination note; port characteristics; which lines sail that route, linking to guides.
Then the call CTA.

Move its data out of hardcoded JS and generate it from `ports.json` + `directory.json`.
Fire `dataLayer` events at every step — the cheapest ad-targeting insight available.

---

# 9. TASK 5 — Quote builder

Let a visitor assemble a shortlist from the comparison tool and generate a shareable summary.

- Captures: home port, region, month, party composition, shortlisted lines/ships, cabin preference.
- Outputs a clean, branded summary they can **download as PDF** or **share to WhatsApp**.
- **Contains no prices.** It is a *requirements brief*, not a quote — label it
  "Your cruise brief", never "Quote".
- Prominent CTA: "Call and read us your reference number — an advisor picks it up from there."
- Generate a short reference code and push it to `dataLayer` so inbound calls can be matched
  to the on-site session.

> Naming matters. A document titled "Quote" containing no prices confuses people; one that *did*
> contain prices would breach Rule 1. "Brief" solves both.

---

# 10. TASK 6 — Content depth standard

The current guides, destination and update pages are **too thin**. This is the biggest gap in
the project. Thin pages don't earn calls and don't rank.

**Standard:** ~2,000–3,000 words per destination/guide page, with tables, comparisons and
genuinely non-obvious detail. Test every page by asking: *"If I were planning this trip, would
this tell me something I couldn't easily find elsewhere?"* If no, it isn't finished.

## Destination page must include

- Routes and what each is actually like (not just port lists)
- **Month-by-month table:** avg high/low, rain days, sea temperature (NOAA), crowd level,
  daylight hours (critical for Alaska/Norway)
- Hurricane/monsoon/ice season with official dates and historical peak weeks
- **Port-by-port:** dock vs tender, walking distance to town, whether an excursion is genuinely
  needed or you can self-explore, accessibility notes, typical time in port
- Which home ports serve it and typical sailing lengths
- Which lines sail it and how they differ *on this route specifically*
- What to pack, what to book ahead, common mistakes
- Sources block with per-fact verification dates

## Guide page must include

Real decision frameworks, not platitudes. "Choosing a cabin" covers deck-by-deck noise sources,
identifying obstructed views on deck plans, connecting vs adjacent, why mid-ship lower decks are
steadiest, when a balcony is worth it by itinerary type, and accessible-cabin scarcity.

---

# 11. TASK 7 — Design system & UX requirements

## Tokens (do not redesign)

```
--abyss:#04121C  --ink:#08243B   --ink2:#0E3A5C  --deep:#123C5A
--lagoon:#1B7A8C --aqua:#3ECFC9  --foam:#F4F8F9  --mist:#E4EDEF
--line:#D5E0E3   --muted:#556B78 --brass:#D9B25A --brassd:#B8933D
--coral:#FF6B5A  --marigold:#FFB63D --plum:#6C5CE7 --paper:#FBFAF7
```

Fraunces (serif) for display headings only. Inter for all UI text and buttons.
Radius: 12px controls, 14–22px cards.

## Required on every page

- **Header:** logo + tagline left; phone number + hamburger right. Nav in a drawer.
- **Breadcrumb bar** under the header: `← Back` control + trail
  (`Home › Cruise lines › Royal Caribbean`), every ancestor clickable.
- **Back-to-top** button, appearing after ~500px scroll.
- **Phone number highly visible** — header, sticky mobile bar, and a CTA after every major section.
- **Sticky call bar** on mobile; a static banner on desktop.
- Mobile-first, verified at **360px**. Desktop must be a genuine desktop layout (multi-column,
  container ~1180px) — not a stretched phone column.
- Accessible: real `<button>` elements, `aria-pressed` where stateful, visible focus rings,
  keyboard operable, `prefers-reduced-motion` respected.

## Signature design element

The home page uses a **voyage spine**: a vertical dotted route down the page with numbered port
stops and a ship that sails along it as you scroll, each stop an interactive module. Keep this.
It is the memorable thing about the site and it is structurally honest — a cruise *is* a route
between stops.

---

# 12. TASK 8 — Documentation (`docs/`)

Write for someone who has never seen the project and may take it over tomorrow.

- `docs/00-START-HERE.md` — what the business is, how money is made, the seven hard rules,
  first-day checklist
- `docs/01-architecture.md` — data flow, why nothing is hand-edited, full directory map
- `docs/02-infrastructure.md` — domain registrar, DNS, hosting, SSL, CDN, deploy, rollback,
  which credentials exist and where they live (reference a password manager; never commit secrets)
- `docs/03-content-operations.md` — verification cycle, 30/60/90-day cadence, how to add a line,
  destination, port or guide
- `docs/04-compliance.md` — the seven rules in detail and why each exists; TCPA consent and
  record-keeping; privacy sale/share obligations; trademark/nominative-use boundaries; what to do
  if a cruise line complains. **State plainly this is operational guidance, not legal advice, and
  that a qualified attorney must review before launch and after any material change.**
- `docs/05-analytics-and-ads.md` — GA4 + Google Ads setup, the `trackCall` contract, `dataLayer`
  schema, call tracking, conversion definitions, what the landing page needs to survive Google
  policy review
- `docs/06-lead-buyers.md` — partner agency onboarding, required warranties, compliance addendum,
  diligence checks and cadence, grounds for termination
- `docs/07-runbook.md` — exact commands: build, deploy, verify, add a line, publish an update,
  rotate credentials, restore from backup
- `docs/08-roadmap.md` — remaining lines and regions in priority order

Plus a top-level `README.md` indexing all of it.

---

# 13. Analytics contract

```js
trackCall(placement)  // on every tel: link
dataLayer.push({event:'call_click', placement, interests, page})
```

Also emit: `nvg_port`, `nvg_region`, `nvg_month`, `nvg_party`, `nvg_complete`,
`compare_lines`, `directory_filter`, `month_select`, `cabin_explore`, `quote_generated`,
`exit_intent_shown`.

Google Ads conversion fires on `call_click`. Keep the conversion ID in config, not inline.

---

# 14. Build order

1. Verification system + schema validation + changelog
2. Content depth pass on the 8 launch lines + 6 destinations (**highest value**)
3. Comparison tool
4. Updates system
5. Home-port navigator productionised from JSON
6. Quote builder
7. Documentation
8. Phase 2–5 scale-out

---

# 15. Definition of done

- Build passes with **zero banned-term hits** (guard exits non-zero on failure)
- `verify.py status` runs in CI and fails on stale data
- Every rendered fact traces to a source URL and a verified date
- Mobile verified at 360px; desktop is a real desktop layout
- Accessibility: real buttons, focus rings, keyboard operable, reduced-motion respected
- Every page has header, breadcrumbs + back, back-to-top, visible phone, footer disclaimers
- Docs updated in the same commit as the code they describe

---

# 16. Pitfalls already hit — do not repeat these

These cost real time during prototyping.

1. **Orphaned DOM references kill the whole page.** A script referencing an element removed in a
   later edit threw a TypeError that silently killed every subsequent script — navigator, filters,
   back-to-top, all dead, with no visible error.
   → **Wrap every module in its own IIFE with a null guard on the first line.** One broken module
   must never take down the rest. Add a smoke test that loads each page and asserts zero console
   errors.

2. **Duplicate IDs across repeated components.** `getElementById` returns only the first match, so
   the hamburger/back-to-top on every page after the first did nothing.
   → Scope per component or use `querySelector` within a container. Never rely on global IDs for
   repeated components.

3. **Stacking order.** A card without `position`/`z-index` fell behind an absolutely positioned
   hero graphic; a sticky header (z-index 60) plus sticky breadcrumb bar (55) hid anything pulled
   up with a negative margin.
   → Define one explicit z-index scale and use `scroll-margin-top` on anchor targets.

4. **External CSS/JS paths break standalone file previews.** A shared `assets/style.css` is correct
   for production but renders unstyled when a file is opened directly.
   → Always review through a dev server.

5. **Price-guard false positives.** The word "discounts" appears legitimately in the footer
   disclaimer saying none are shown.
   → Scope the scan to `<main>`, not the whole document.

6. **Don't fork templates per line.** Every line page uses the same generator so a fix applies
   everywhere at once.

---

# 17. The one judgement call to preserve

The site's competitive advantage is that it **admits what it doesn't know**: visible
"Not yet verified" gaps, published verification dates, honest "probably not for you" sections,
and real coverage hours instead of a 24/7 claim.

Every instinct will say to tidy these away. Don't. A cruise buyer arriving from a brand keyword
has already read five sites that claim everything and prove nothing. Being the one that shows its
working is what earns the phone call.
