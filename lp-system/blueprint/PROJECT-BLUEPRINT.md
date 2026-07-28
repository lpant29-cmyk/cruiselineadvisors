# CRUISE ADS-LP PROJECT BLUEPRINT v1
### Page taxonomy · pricing sheet v2 · LP conversion anatomy · photo pipeline · weekly rate engine · Claude Code multi-agent build
For the cruiselineadvisors.com Claude Code project · July 28, 2026

---

# PART 1 — PAGE TAXONOMY (research findings)

## 1.1 What the OTA pattern actually is
Studying the reference OTA's LP system: every page type is the same
skeleton (query-mirroring hero → search/CTA → popular sailings with
per-person "from" prices → cross-links to related filtered views → FAQ),
and the real scale comes from COMBINATIONS (line×port, destination×port),
not from the four base categories. Their port page literally cross-links
"browse cruise lines FROM this port" — that combo layer is where
high-intent, low-competition keywords live. We replicate the taxonomy
logic with our own structure, copy, design, and call-first conversion.

## 1.2 Our full page catalog (call-generation focus, 10 lines)

TIER 1 — build first (highest call intent per page)
| Type | Pattern | Count | Example URL |
|---|---|---|---|
| Line | /en/go/lines/{line}/ | 10 | /en/go/lines/royal-caribbean/ |
| Port | /en/go/from/{port}/ | 12 | /en/go/from/galveston/ |
| Line×Port | /en/go/lines/{line}/from/{port}/ | ~45 real combos | /en/go/lines/carnival/from/galveston/ |
| Ship (flagships) | /en/go/ships/{ship}/ | ~25 | /en/go/ships/icon-of-the-seas/ |

TIER 2 — next wave
| Type | Pattern | Count | Example |
|---|---|---|---|
| Destination | /en/go/to/{dest}/ | 12 | /en/go/to/alaska/ |
| Line×Destination | /en/go/lines/{line}/to/{dest}/ | ~40 combos | /en/go/lines/princess/to/alaska/ |
| Audience | /en/go/{audience}-cruises/ | 8 | /en/go/family-cruises/ |
| Duration | /en/go/{n}-night-cruises/ (+port combos) | ~10 | /en/go/3-night-cruises-from-miami/ |

TIER 3 — long tail / seasonal
| Type | Pattern | Count | Example |
|---|---|---|---|
| Remaining ships | /en/go/ships/{ship}/ | ~100+ | fleet-wide |
| Deals/seasonal | /en/go/last-minute-cruises/, wave-season, holiday sailings | ~8 | rotating |
| ES mirrors of top performers | /es/go/... | as earned | |

## 1.3 The registries the research agent must fill (official sources only)
- SHIPS: full fleets of RCI (~28), Carnival (~27), Princess (~17),
  Celebrity (~17), Holland America (11), MSC (US-deployed subset ~10 of
  world fleet), Cunard (4), Margaritaville at Sea (current active fleet),
  Viking ocean (~12; river out of scope initially), Silversea (~12).
  Roughly 150 ships total; verify each fleet from the line's official
  fleet page, never from memory.
- PORTS: US primary 12 = Miami, Port Canaveral, Fort Lauderdale,
  Galveston, New York area (Manhattan/Brooklyn/Cape Liberty as one page),
  Seattle, Los Angeles (San Pedro), Long Beach, Tampa, New Orleans,
  Baltimore, San Juan. Secondary = Boston, Mobile, Jacksonville, San
  Diego, San Francisco, Norfolk, Vancouver. International later.
- LINE×PORT matrix: which of the 10 lines actually sail from each port
  (verify per line; ~45 true combos expected). No page for a combo that
  doesn't sail.
- DESTINATIONS: Caribbean (E/W/S), Bahamas, Alaska, Bermuda, Mexican
  Riviera, Hawaii, Mediterranean, Northern Europe, Canada & New England,
  Panama Canal, Transatlantic, World/Grand voyages.
- AUDIENCES: family, adults-only/couples, seniors, first-timers, luxury,
  groups, honeymoon, accessible.

# PART 2 — MASTER SHEET v2 (powers all LP pricing)

One Google Sheet, eight tabs. CSVs live in repo /data and sync to the
sheet; the sheet is the human interface, the CSVs are the build source.

| Tab | Key columns | Purpose |
|---|---|---|
| lines | line_id, name, slug, tier, priority | 10 rows, stable |
| ships | ship_id, line_id, name, slug, class, size, audience_fit, homeports (semicolon list), page_planned, asset_id | fleet registry (~150) |
| ports | port_id, name, slug, state, lines_serving (list), drive_market, priority, asset_id | port registry |
| destinations | dest_id, name, slug, season_months, lines_serving, asset_id | 12 rows |
| deals | deal_id, line_id, ship_slug, itinerary_name, region, port_slug, nights, sail_months, next_sail_date, from_price, currency, cabin_basis, date_checked, source, page_targets, featured | THE CORE. One row per itinerary×port×duration. Feeds every page via page_targets |
| offers | offer_id, line_id, offer_text, start_date, end_date, show_banner, banner_pages, date_checked | facts-only promos → auto-expiring ribbons |
| pages | page_id, page_type, slug, url, h1, deal_filter, keywords, tracking_number, status, priority | the site map; generate.py iterates this |
| assets | asset_id, subject_type (port/dest/ship-generic/theme), file, source (pexels/unsplash/ai/trade-portal), license_note, alt_text | photo registry |

Mapping rule: deals.page_targets holds every page key the deal serves,
e.g. `line:carnival;port:galveston;combo:carnival-galveston;dest:western-
caribbean;aud:family;dur:5-night`. pages.deal_filter matches one key.
One verified price feeds 5-6 pages. This is what makes weekly updates of
~120-150 deal rows power 100+ pages honestly.

Pricing scope rule: track lead-in fares at itinerary level (not per sail
date). Exact-date pricing is the phone call's job — that IS the funnel.

# PART 3 — LP CONVERSION ANATOMY (inspired, not copied)

One skeleton, four content modules. Every element exists to produce a
call or a form submit.

1. Disclosure ribbon (independent referral service, not the cruise line).
2. Slim header: logo + toll-free only. No nav. No exits.
3. HERO: H1 mirrors the ad query exactly; subline promises the call value
   ("one call compares every {X} sailing for your dates"); hours badge
   ("Advisors answering now · 8am–11pm ET").
4. CALL ZONE above the fold: big tap-to-call with tracking number + 3-field
   callback form (name, phone, best time) + TCPA consent line.
5. PRICE ANCHOR + DEAL CARDS (3-6 from sheet): itinerary, ship, nights,
   port, sail months, "Recently from $X" + date-checked stamp, CTA "Call
   for today's fare". Prices create credibility; the stamp creates the
   reason to call.
6. OFFER RIBBON (auto): active offers rows for this page — our wording,
   our design, auto-expires. Urgency without fabrication.
7. CONTEXT MODULE (varies): ship→cabins+know-before-you-book; port→
   parking/terminals/who-sails-here; line→ship classes+fine-print facts
   teaser (reuse site's verified-facts data); audience→fit guidance;
   combo pages→port module + line facts strip.
8. WHY-CALL trio (reuse site voice): straight answers on the costly stuff /
   a specialist, not a script / free, no pressure, we never take payment.
9. FAQ (4 questions max, objection-killers: "is calling more expensive
   than booking online?" is question #1 on every page).
10. FINAL CALL BAND + mobile sticky bar (Call / Callback). 
Rules: page weight <150KB excl. images, LCP <2s, phone number appears
minimum 5 times, every price stamped, one page = one intent = one ad group.

# PART 4 — PHOTO PIPELINE

Sources, in order of preference per subject:
1. Ports/destinations/ocean/lifestyle: Pexels + Unsplash via their APIs
   (commercial use permitted; keep the existing footer courtesy credit).
   photo-curator agent searches, downloads, converts to WebP (1600px hero,
   800px card), writes assets rows with alt text + license_note.
2. Generic cruise scenes (deck, cabin, dining) where stock is thin: AI
   generation allowed with hard rules — never depict a real named ship,
   no line logos/liveries/funnels, label source=ai in assets tab.
3. Real ship photography: ONLY after agent status → cruise line trade
   portals (licensed for agent marketing). assets.source=trade-portal;
   templates automatically prefer trade-portal assets when present.
Never: images from cruise line consumer sites, other OTAs/agencies, or
logo usage beyond plain-text brand names.
File convention: /public/img/{subject_type}/{slug}-{variant}.webp; every
image referenced only through the assets registry (no hardcoded paths).

# PART 5 — WEEKLY PRICING ENGINE (runs even when you're away)

Principles: modest volume (~120-150 deal rows), weekly cadence, public
sources now → agent-portal sources when available, and a QA GATE decides
between auto-publish and hold-for-human. Autonomy comes from strict
validation, not from skipping it.

Pipeline stages (Monday 06:00 ET):
1. COLLECT — pricing-scout agent fetches each deal row's source (scripted
   HTTP fetches, rate-limited, cached, sequential; no login automation
   unattended). Extracts current lead-in fare + next sail date. Also
   checks each line's promotions page → drafts offers updates.
2. NORMALIZE — writes a candidate deals.csv + offers.csv diff.
3. VALIDATE (qa-auditor agent + validate.py):
   - price present, numeric, USD, within sanity band ($99–$25,000)
   - change vs last week within ±25% (else flag)
   - date_checked = today on every touched row
   - offers past end_date get show_banner=no automatically
   - every built page still has ≥3 live deal rows
   - stale check: any row untouched >10 days flagged
4. GATE — ALL checks pass → auto-commit, regenerate pages, deploy, log to
   lp-system/ratelog.md. ANY flag → publish only the clean rows, write HOLD-{date}.md
   listing flagged rows with evidence, notify you (email/ntfy push), leave
   flagged prices at last verified value with their honest older stamp.
   A stale-but-true stamp is safe; a wrong price in a Google ad is not.
5. REPORT — manager agent appends run summary: rows updated, flags, pages
   rebuilt, offers expired/added, next actions.
Ad-copy sync rule: any ad quoting a specific price is listed in
ads-price-map.csv; if that price changed, the run report's top line says
"UPDATE THESE ADS TODAY" with the list.

# PART 6 — CLAUDE CODE MULTI-AGENT BUILD

## 6.1 Repo layout
```
cruiselineadvisors/            (existing repo)
  CLAUDE.md                    <- add "ADS LP SYSTEM" section pointing to this blueprint
  lp-system/blueprint/PROJECT-BLUEPRINT.md   <- this file
  lp-system/data/*.csv                   <- the 8 tabs
  lp-system/templates/lp/*.html          <- the 4+combo skeletons
  pages generated to site build as /go/
  lp-system/scripts/collect.py  validate.py  generate.py  notify.sh
  .claude/agents/*.md          <- subagent definitions below
  .claude/commands/*.md        <- slash commands
  lp-system/ratelog.md  HOLD-*.md  ads-price-map.csv
```

## 6.2 The agents (.claude/agents/, YAML frontmatter + role prompt)
- **manager** — orchestrator. Owns the run order, invokes the others,
  enforces the gate, writes the run report, maintains the task board
  (tasks.md) with due dates and reminds/re-queues anything unfinished.
  Tools: read/write, bash. Never edits prices itself.
- **qa-auditor** — adversarial checker. Runs validate.py, re-verifies a
  random 10% sample of changed prices against source, audits new pages
  against the Definition of Done (noindex present, disclosure ribbon,
  stamps, tracking number, ≥3 deals), and must explicitly APPROVE before
  deploy. Instructed to fail loudly, never rubber-stamp.
- **pricing-scout** — runs collect.py, parses results, writes candidate
  CSV diffs with per-row evidence (source URL + retrieved value).
- **page-builder** — builds/edits LPs strictly from templates + pages.csv;
  runs generate.py; never invents content facts (pulls from registries).
- **photo-curator** — fills assets tab per Part 4 rules; checks licenses;
  writes alt text; optimizes files.
- **research-registrar** — one-time + monthly: fills/refreshes ships,
  ports, line×port matrix, destinations from official fleet/port pages,
  citing source URL per row.

## 6.3 Slash commands (.claude/commands/)
- /rate-update  → manager runs the full Part 5 pipeline
- /new-page {type} {slug}  → page-builder scaffolds + registers + QA audits
- /validate  → qa-auditor full site audit
- /fill-registry {tab}  → research-registrar populates a registry tab

## 6.4 Running it "even if I am not here" (macOS)
Claude Code doesn't self-start; the OS scheduler starts it headless:
1. Create the weekly job (cron):
   `0 6 * * 1  cd ~/cruiselineadvisors && claude -p "/rate-update" --output-format json >> logs/run-$(date +\%F).json 2>&1`
   (launchd plist is the more reliable Mac equivalent if the machine
   sleeps; or run it on a small always-on VPS / GitHub Actions runner.)
2. Permissions: pre-approve ONLY what the run needs in .claude/settings.json
   allowedTools (bash for the scripts, file edits in lp-system/data/ and pages/).
   Do not blanket-skip permissions; the allowlist IS the safety rail.
3. notify.sh sends the run report (and any HOLD file) to your email/ntfy
   so a flagged run reaches your phone; clean runs deploy themselves.
4. Monthly job: research-registrar refresh + link/photo audit.

## 6.5 What to paste into Claude Code to start (verbatim kickoff)
"Read lp-system/blueprint/PROJECT-BLUEPRINT.md. Create the .claude/agents and
.claude/commands files per Part 6, the lp-system/data/ CSVs per Part 2 (import the
existing cruise-master CSVs as the starting point), and lp-system/scripts/
collect.py, validate.py, generate.py, notify.sh per Part 5. Then run
/fill-registry ships and /fill-registry ports using official sources only,
then /new-page line royal-caribbean as the pilot LP including the sitewide
pricing-disclosure footer change from ADS-LP-BRIEF.md section 6. Stop for
my review after the pilot page."

## 6.6 Build order
1. Repo scaffolding + agents + scripts (day 1)
2. Registries filled + verified (ships, ports, line×port) (day 1-2)
3. Pilot: RC line LP + footer legal change → your review (day 2)
4. Tier 1 pages generated (line 10, port 12, ship 25, combos ~45) (week 1)
5. First supervised /rate-update run → then schedule the cron (week 1)
6. Tier 2 pages + ES mirrors of winners (week 2+)
7. Trade-portal photo upgrade + portal-sourced pricing when host access
   lands (post-OA activation)
