# START HERE - Cruise Ads-LP System (Royal Caribbean first)
Unzip this into the ROOT of your project folder. Only TWO things land there:
.claude/ (agents + commands, required at root) and lp-system/ (everything
else: blueprint, data, templates, and later scripts + logs). Your existing
data/ folder and site code are untouched. Then follow the steps.

## What just landed where
- lp-system/blueprint/        - the four planning docs (read order: PROJECT-BLUEPRINT,
                      ADS-LP-BRIEF, SCALING-PLAYBOOK, MASTER_PLAN)
- lp-system/data/             - sheet v3: 11 CSVs (lines, ships, itineraries,
                      itinerary_days, ports_content, destinations_content,
                      offers, faqs, pages, assets, geo_map) + rc_seed_keywords
- lp-system/data/kw_raw/      - EMPTY. Drop your Keyword Planner CSV exports here.
- .claude/agents/   - keyword-scout.md, structure-guard.md (more agents get
                      created by the kickoff below)
- .claude/commands/ - need-page.md (the /need-page command)
- lp-system/templates/lp/     - finder template (canonical) + 4 call-gen templates

## Step 1 - YOU (30 min, only step needing your hands)
Google Ads > Tools > Keyword Planner > Discover new keywords.
Paste seeds from lp-system/data/rc_seed_keywords.csv in batches by category
(max 10 seeds per run, ~7 runs). Location: United States. Language:
English. Download each run as CSV. Put all CSVs into lp-system/data/kw_raw/.

## Step 2 - kickoff prompt (paste into Claude Code in this folder)
"Read lp-system/blueprint/PROJECT-BLUEPRINT.md, lp-system/blueprint/SCALING-PLAYBOOK.md and
lp-system/blueprint/ADS-LP-BRIEF.md. Scope everything to Royal Caribbean only for
now. Create the remaining agents per Blueprint Part 6 (manager,
qa-auditor, pricing-scout, page-builder, photo-curator,
research-registrar) alongside the existing keyword-scout and
structure-guard. Create lp-system/scripts/collect.py, validate.py, generate.py,
propose_pages.py, notify.sh per Blueprint Part 5 and Playbook sections
2-3, using the lp-system/data/ CSVs as the schema. Then run keyword-scout on
lp-system/data/kw_raw. Stop and show me the keyword report."

## Step 3 - after the keyword report
Feed the report's top page needs to structure-guard:
  /need-page <highest scoring keyword>
Let it trigger targeted RC data collection (Pass A/B/C, Galveston and
Cape Liberty first), build the pilot page from lp-system/templates/lp/, pass
qa-auditor, and show you the result. Review the pilot before scaling.

## Step 4 - weekly autonomy (after one supervised run)
Schedule: cron/launchd Monday 06:00 runs `claude -p "/rate-update"`.
Manager runs the pipeline, qa-auditor gates publishing, notify.sh sends
you the report. Flagged prices HOLD at last verified value; clean rows
deploy themselves.

## House rules already baked in
- Prices always date-stamped; VERIFY-BEFORE-PUBLISH rows never deploy.
- /go/ pages are noindex; footer pricing disclosure ships with page 1
  (ADS-LP-BRIEF section 6 has the exact wording).
- All page copy original, written from the data registries; brand names
  in plain text only; disclosure ribbon on every page.
