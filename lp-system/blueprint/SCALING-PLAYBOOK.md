# SCALING PLAYBOOK — keyword groups, data collection, page generation
Addendum to PROJECT-BLUEPRINT.md · July 28, 2026

## 1. The core inversion
Keywords do not get their own data. ITINERARIES are collected once;
every keyword page is a saved filter over the itineraries tab:

| Keyword group | Facet filter | URL pattern |
|---|---|---|
| cruise deals from ft lauderdale | port=fort-lauderdale (sort: price asc) | /en/go/from/fort-lauderdale/ |
| bahamas cruises from galveston | dest=bahamas AND port=galveston | /en/go/to/bahamas/from/galveston/ |
| 3 day caribbean cruise | nights 2-4 AND dest in caribbean group | /en/go/2-4-night-caribbean-cruises/ |
| carnival cruises from galveston | line=carnival AND port=galveston | /en/go/lines/carnival/from/galveston/ |
| 7 day bahamas cruise royal caribbean | line=rci AND dest=bahamas AND nights=7 | itinerary page(s) or 3-facet page |
| cheap cruises from miami | port=miami (sort: price asc, H1 variant) | /en/go/from/miami/ (deals ad group) |

Rule: ONE page per facet combination. Multiple keywords share a page via
ad groups; minor H1 variants (deals/cheap/last-minute) come from a URL
param the template reads, not from duplicate pages.

## 2. Data collection is itinerary-first (three passes)

PASS A — ENUMERATE (per line, monthly, research-registrar agent):
For each of the 10 lines, list every active itinerary: name, ship(s),
departure port, nights, destination, sail months, and the itinerary's
public detail URL. Source: each line's public find-a-cruise/deployment
listings, walked port by port. Supervised Claude-in-Chrome session for
the first enumeration; thereafter it is diffing (new/retired itineraries
only). Expected scale: 10 lines x 40-80 active itineraries = roughly
400-800 rows. Each row stores its source_url — this is what makes
weekly pricing a direct fetch, not a repeated discovery crawl.

PASS B — ENRICH (once per itinerary, research-registrar):
From the itinerary's detail page: day-by-day rows (itinerary_days tab),
ports of call (creating any missing ports_content rows — written in OUR
words, never copied), private-island flag, quad availability. This data
changes rarely; refresh seasonally or when validate flags a mismatch.

PASS C — PRICE (weekly, pricing-scout):
For each itinerary row: fetch source_url (rate-limited, cached,
sequential), extract interior + balcony from-fares for upcoming months,
write month overrides + date_checked. Only this pass runs weekly.
Migrate source_url to host-portal equivalents as soon as agent access
exists — cleaner data and cleaner terms.

Volume discipline: weekly pass = one polite fetch per tracked itinerary
(hundreds of requests spread over hours, human-approved gate before
publish). Enumeration is monthly. This stays in the range of what a
diligent human staffer would do manually.

## 3. Page generation: combos are computed, never hand-listed

lp-system/scripts/propose_pages.py runs after every enumeration pass:
1. Compute all facet combos (line x port, dest x port, dur x dest,
   line x dest, line x port x nights, port-only, dest-only, dur-only).
2. Keep a combo only if: >=3 matching itineraries (>=1 for line x port x
   nights itinerary pages), at least one sailing in the next 6 months,
   and no thinner page already covers the identical itinerary set.
3. Output pages_proposed.csv with slug, url, h1, deal_filter, itinerary
   count. Human (or manager agent per rules) approves -> merged into
   pages tab -> generate.py builds them from the finder/itinerary
   templates.
Pages auto-retire the same way: a combo whose itinerary count drops
below threshold flips status=retire (page stays live with a call CTA and
"seasonal route" note for 30 days, then redirects to its parent facet).

Expected honest scale from 10 lines: ~10 line + ~12 port + ~45 line x
port + ~12 dest + ~60 dest x port + ~40 line x dest + ~30 duration
combos + itinerary pages for the top ~100 itineraries = roughly 300
pages in phase one, every one backed by >=3 real itineraries. Keyword
research then attaches ad groups to pages, not pages to keywords.

## 4. Keyword -> page mapping file
lp-system/data/12_keyword_map.csv: keyword_group, example_queries, page_id,
match_type_plan, h1_variant. This is the ads-side contract: every ad
group points at exactly one page; the weekly report cross-checks that
every page with an active ad group passed validation this week.

## 5. What to tell Claude Code (verbatim)
"Read lp-system/blueprint/SCALING-PLAYBOOK.md. Add propose_pages.py and
retire logic per section 3, add lp-system/data/12_keyword_map.csv, extend
collect.py to the three-pass model in section 2 with source_url per
itinerary row, and update the manager agent's runbook: Pass C weekly,
Pass A monthly first Monday, propose_pages after every Pass A. Then run
Pass A for Royal Caribbean from Galveston and Cape Liberty only, as the
pilot enumeration, and stop for review."
