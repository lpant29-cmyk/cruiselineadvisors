# LP SYSTEM — AUTOMATION PLAN

**BUILT 2026-10-18.** Option 1 below (GitHub Actions) is live as
`.github/workflows/rates.yml`. Read that file and
`lp-system/scripts/auto_rates.py` first; everything from section 2 down is the
reasoning that produced them and is kept because the reasoning still applies.

What shipped, and the one thing that changed on the way:

- `lp-system/scripts/auto_rates.py` does the whole refresh with **no model in
  the loop**. Section 1 assumed the scheduler would need to run an agent and
  therefore an API key as a repo secret. It does not. Every number the manual
  runs produced came from two official `cruiseSearch` queries and a
  derivation; the only part that needed a model was the English prose, and
  that part is exactly where qa-auditor twice caught invented note history.
  So the script writes **no prose at all** and never touches `notes`, and
  there is **no API key secret**. The job runs on `GITHUB_TOKEN` alone.
- The gate is the two independently shaped queries: one by departure port,
  one per ship. A value publishes only where both return it to the cent.
  Anything else keeps its previous value **and its older `date_checked`
  stamp**, which means `PRICE_MAX_AGE_DAYS = 3` withholds that fare within
  three days on its own. A hold degrades to "Fare on request", never to a
  wrong number.
- Offers are still a human job. The script may only switch off a banner whose
  `end_date` has passed. It may not write offer copy, because offer copy is a
  claim in our own words and the one time a run imported a line's own `$299`
  figure, qa-auditor blocked the deploy.
- A row the queries no longer return is marked `frozen` in a new
  `auto_status` column, which `provenance_ok()` honours in both
  `generate.py` and `validate.py`. It is a column and not a note on purpose:
  writing "UNVERIFIED" into the append-only `notes` field would have blocked
  that row forever, including after its sailings came back.
- Notification is one GitHub issue, kept current, assigned to the operator.
  It comments (which is what reaches the phone) only when the set of problems
  changes, so a permanently volatile row does not mail every cycle. An
  optional `PUSH_WEBHOOK` secret adds a direct push if one is ever wanted.

Still a human decision every time, by design: retiring a row or a page,
pausing an ad group, and writing an offer.

---

Original note, kept for the record — operator decision 2026-07-30: *do not
build this yet. Launch the three pilot pages, create the ad campaigns, run
the account, and refresh prices daily. Revisit after 1-2 weeks of live data.*

---

## 1. How these agents actually work (the constraint everything follows from)

The agents in `.claude/agents/` are not services. Each is a role prompt
plus a tool allowlist that exists only while a Claude Code process runs.
Nothing wakes up on its own. Every agent action in the build sessions
happened because a session was open.

Consequence: **"laptop off, operator away" means the work must run somewhere
that is not the operator's laptop.** A launchd/cron job on the Mac only
fires while the Mac is awake, so it does not satisfy the requirement.

Hosting options, in the order they were judged:
1. **GitHub Actions** — best fit. Repo already on GitHub, Render already
   deploys from `main`, scheduler is free, and a run that commits + pushes
   triggers the existing deploy path. Needs an API key as a repo secret.
2. **Scheduled cloud agents (routines)** — runs in the cloud on a cron with
   no machine of ours involved. Confirm feature fit before committing.
3. **Small always-on VPS** — most control, ~$5-10/month, most maintenance.

## 2. The three layers, and where the human belongs

### Layer 1 — daily price refresh: FULLY AUTOMATIC
Low risk, high value, and far cheaper than the blueprint assumed: one
query to royalcaribbean.com/graph returns every sailing for a departure
port at once (all 16 Galveston itineraries, 210 sail dates, in a single
request). Daily = ~1 polite request per port per day, not hundreds. Even
at 12 ports x 10 lines that is ~120 requests/day spread over hours.

Run order (unchanged from Blueprint Part 5, cadence changed weekly -> daily):
pricing-scout Pass C -> validate.py -> gate -> commit + push -> Render deploys.
- ALL checks pass AND moves within tolerance (suggest +/-10%): auto-publish.
- ANY flag or larger move: publish clean rows only, hold flagged rows at
  their last verified value with the honest older stamp, push notification.
- Ad-copy sync: any price quoted in ad text is flagged in the same run
  (Google pricing-accuracy policy applies to the ad as well as the page).

### Layer 2 — new pages: AUTOMATIC BUILD, HUMAN RELEASE
A new page is a new ad destination attached to spend. The gates are good
(qa-auditor caught an invisible-above-the-fold disclosure and caught false
claims about Royal Caribbean during the build), but they are LLM-driven
and have also nearly filed a false blocker. Good enough to trust with
"build it and prove it passes"; not with "and start spending on it".

Pattern: research-registrar Pass A -> propose_pages.py -> structure-guard
registers -> page-builder builds -> tracking-guardian + qa-auditor gate ->
pages staged at status=review -> ONE notification with a preview link ->
operator replies to release. Once a page TYPE has proven itself live, that
type can be promoted to auto-release.

### Layer 3 — alerts: only what needs a human
Push (ntfy/email via `lp-system/scripts/notify.sh`) on:
- ads spending with ZERO conversions AND ZERO tracking events (means
  measurement broke, not that ads are bad; halts optimization decisions)
- a price moving beyond tolerance, or a source that changed shape
- a live page failing validation
- anything touching legal or compliance wording

## 3. The freshness fuse (matters more than the schedule)

Cron jobs fail silently. The protection is not "we refresh daily", it is
that a stale price cannot render.

**Rule to implement:** if a row's `date_checked` is older than N days
(suggest 3 for this inventory), `generate.py` refuses to render the number
and the page shows "Call for today's fare" instead. The generator already
enforces "no stamp, no price"; this extends it to "no FRESH stamp, no price".

Evidence this matters: i0005 balcony moved $566 -> $703.87 inside 24 hours;
i0008 August interior moved $590 -> $751 in a day. The 10-day validate
window is NOT tolerance on this inventory.

Failure mode becomes: automation dies -> pages degrade to call-only, not to
advertising a fare that is $140 wrong. Costs almost nothing because the
call is the conversion; the price is credibility, not a quote.

## 4. Honest limits

- **Ad spend is outside this loop.** No agent touches the Google Ads
  account; nothing can pause a campaign or cut a budget. If something
  breaks, pages degrade safely but ads keep spending until a human acts.
  This is exactly why the "spending with no events" alert is the most
  valuable one on the list.
- **Every run costs tokens.** A daily price run is small; a monthly
  page-expansion run with full gates is substantially larger.
- **`notify.sh` has no channel configured yet** (needs `NTFY_TOPIC` or
  `NOTIFY_EMAIL`), so today a held run cannot actually reach the operator.
- **`git push` is denied** in `.claude/settings.json` by design. Automation
  would push from the CI runner, not from a local agent session.

## 5. Build order when this resumes

1. Freshness fuse in `generate.py` (do this first; it is the safety net).
2. Tolerance rule + auto-publish gate in `validate.py` / manager runbook.
3. Notification channel configured and tested end to end.
4. Daily job on GitHub Actions (or routine), price refresh only.
5. Let it run two weeks. Confirm reliability before anything depends on it.
6. Only then, Layer 2 page expansion.

## 6. Open decision for the operator

**Do new pages go live automatically once they pass both gates, or wait for
a one-word approval?** The answer shapes Layer 2. Not needed until then.
