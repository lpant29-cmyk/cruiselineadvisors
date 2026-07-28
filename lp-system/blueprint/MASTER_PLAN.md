# CRUISE SITE MASTER PLAN
### Data model · URL architecture · page generation · weekly rate workflow
Prepared July 28, 2026 · for Bookmecheapest LLC cruise lead-gen site

---

## 1. The master sheet (5 tabs)

Import the five CSVs into one Google Sheet, one tab each. This sheet is the
single source of truth for the entire site.

| Tab | File | What it holds | Who edits |
|---|---|---|---|
| cruise_lines | 01_cruise_lines.csv | The 10 lines, slugs, priority | Rarely edited |
| ships | 02_ships.csv | Fleet registry per line (seeded with 13; collection fills the rest) | Grows over time |
| deals | 03_deals.csv | THE CORE TAB. One row per itinerary x departure port x duration, with from_price + date_checked | Weekly |
| offers | 04_offers.csv | Active promotions per line, with end_date + show_banner | Weekly |
| pages | 05_pages.csv | Every page on the site: type, slug, URL, which deals it shows | When adding pages |

**Design decision that keeps this maintainable:** deals are tracked at the
itinerary level (with sail_months + next_sail_date), NOT one row per sail
date. Per-date tracking across 10 lines is thousands of rows nobody can
verify weekly; itinerary-level lead-in fares are what call-generation pages
need. The phone call is where exact dates get priced - that is the model.

**How pages know their deals:** the `page_targets` column on each deal
(e.g. `ship:icon-of-the-seas;port:miami;line:royal-caribbean;aud:family`)
maps one deal onto every page type it should appear on. One deal row can
feed four pages. The `deal_filter` column in the pages tab is the matching
key.

**Offers → banners:** any offers row with `show_banner=yes` and today
between start_date and end_date renders a limited-offer ribbon on the pages
listed in `banner_pages` - and disappears automatically after end_date.
Offer TEXT is rewritten in our own words (facts only: discount, audience,
deadline). We never copy cruise line banner images or creative.

## 2. URL architecture (our own theme)

All pages live under /cruises/ with intent-matching slugs:

- Ship pages:      /cruises/ships/icon-of-the-seas/
- Port pages:      /cruises/from/galveston/
- Line pages:      /cruises/royal-caribbean/
- Audience pages:  /cruises/family/

Rules: lowercase, hyphens, no dates in URLs (pages are evergreen; deals
inside them rotate), one page = one search intent = one ad group.

## 3. Page generation

The four templates already built (ship / port / line / audience, call-gen
versions) are upgraded to read the published sheet:

1. In Google Sheets: File → Share → Publish to web → CSV (per tab).
2. Each template fetches deals + offers CSVs on load, filters rows by its
   own `deal_filter`, renders deal cards, date stamps, and offer ribbons.
3. Adding a page = add a row to pages tab + copy a template file with the
   slug + deal_filter set. Claude Code automates this with one command.

Rollout phases (pages tab `priority` column):
- Phase 1 (launch): 4 built pages + Carnival line page + Miami port page.
- Phase 2: remaining 8 line pages, top 10 US ports (Port Canaveral, Ft
  Lauderdale, NYC/Cape Liberty, Seattle, LA/Long Beach, Tampa, Baltimore,
  New Orleans), top 15 ships.
- Phase 3: audience pages (couples/adults-only, seniors, first-timers,
  Alaska, group cruises) and long-tail ship pages.

## 4. Photos - the legal sourcing policy

- Destination/port/ocean imagery: free stock with commercial licenses
  (Pexels, Unsplash, Pixabay). Ports, beaches, Caribbean water, Alaska
  glaciers - abundant and safe. This covers most image slots.
- Generic cruise imagery (deck scenes, cabins, dining): stock first; AI
  generation acceptable for generic scenes, but never to depict a real,
  named ship (an AI "Icon of the Seas" that looks wrong is a
  misrepresentation risk, and logos/liveries are trademarks).
- Real ship photography: wait for cruise line TRADE PORTALS after agent
  status is active - official images licensed for agent marketing. The
  ships tab gets an `asset_url` column then, and templates auto-upgrade.
- Never: images lifted from cruise line consumer sites or other OTAs,
  cruise line logos beyond plain-text brand names, other agencies' photos.

## 5. Weekly rate workflow (the run-book)

Every Monday (or chosen day):
1. Open the collection session (Claude Code in terminal; Claude in Chrome
   for logged-in portals once MyAgentGenie is live).
2. For each deals row: check current lead-in fare at the source, update
   from_price + date_checked + next_sail_date if changed.
3. Check each line's promotions page / portal: update offers tab, expire
   ended offers, add new ones (rewritten in our words), set banner_pages.
4. Human review pass: any price that moved >25% gets manually re-verified
   (mis-scrapes are how wrong prices reach ads).
5. Approve → sheet is live → site reflects it immediately. Update any ad
   copy that quotes specific prices THE SAME DAY (Google pricing accuracy).
6. Log the run: date, rows changed, anomalies. Claude Code appends to
   lp-system/ratelog.md automatically.

Scale honestly: start by tracking the ~60-100 highest-intent deals rows
(featured itineraries per line/port), not every itinerary in existence.
Weekly verification capacity is the constraint; expand rows only as the
process proves stable. Low-frequency, human-approved collection; migrate
sources to agent portals as soon as access exists.

## 6. Claude Code project setup

```
cruise-site/
  CLAUDE.md              <- conventions + this plan's rules
  lp-system/data/                  <- the 5 CSVs (synced with Google Sheet)
  lp-system/templates/             <- the 4 call-gen templates
  pages/                 <- generated pages (deploy folder)
  lp-system/scripts/
    generate.py          <- pages.csv + templates -> pages/
    validate.py          <- price sanity checks, stale date_checked alerts
  lp-system/ratelog.md             <- weekly run log
```

Suggested slash commands to create in Claude Code:
- /new-page [type] [slug]   -> scaffolds a page from template + registry row
- /rate-update              -> walks the weekly run-book interactively
- /validate                 -> flags stale stamps (>10 days), price anomalies,
                               expired offers still marked show_banner=yes

## 7. Compliance rails (unchanged, now systematized)

- Independent-agency disclosure ribbon on every page (already in template).
- FST/CST footer line on every page (already in template).
- Every price shows its date_checked stamp; validate.py makes stale stamps
  impossible to miss.
- Original copy everywhere; brand names in plain text for identification.
- Brand-term ad campaigns only within vendor rules once host agreement is
  active.
