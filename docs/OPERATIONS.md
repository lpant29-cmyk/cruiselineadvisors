# CruiseLine Advisors — Operations & Maintenance Runbook

> **Audience:** the developer/operator keeping the site accurate and compliant.
> **Not indexed / not public:** this file lives in the git repo under `docs/` only. It is **never
> copied into `newsite/dist/` or `site/`**, so it is never served by the website and never crawled
> or indexed by search engines. Keep it that way — operational notes stay in `docs/`, never in the
> generated site.
> Read alongside `docs/PROJECT-HANDBOOK.md` (the A–Z overview) and `CLAUDE.md` (the hard rules).
> Last updated: 2026-07-20.

---

## 0. Pending items (as of 2026-07-20)

| Item | Status | What's needed |
|---|---|---|
| **Real phone number** | ⏳ pending | Still the placeholder `+1 (888) 555-0142`. Give the developer the real call-tracking number → see §1. Nothing on the site converts correctly until this is set. |
| **Guides section** | ⏳ partial | 6 guides live; content plan to expand in §6. |
| **Updates cadence** | ⏳ ongoing | Publish updates as policies change → §4. The pipeline is built; it needs a steady stream of entries. |
| **Spanish deep content** | ⏳ partial | Some ES long-form fields still show as visible "Not yet verified" gaps (intentional, not bugs). |

---

## 1. Swapping in the real phone number (one place)

The number lives ONLY in `newsite/config.py`. When you have the real tracking number:

1. Edit `newsite/config.py`:
   - `PHONE_DISPLAY = "+1 (XXX) XXX-XXXX"`  (human-readable)
   - `PHONE_HREF    = "+1XXXXXXXXXX"`        (tel: form, digits only, leading +)
2. Rebuild + deploy (see PROJECT-HANDBOOK §3). Every call button, header, footer, sticky bar,
   `tel:` link, and the Organization JSON-LD `telephone` update automatically.
3. Verify: `grep -c "888) 555-0142" newsite/dist/en/index.html` should be `0`.
4. In GTM/GA4, confirm the `call_click` conversion still fires (the event is number-independent).

---

## 2. The 30-day fact re-check (the core maintenance job)

Everything factual on the site (the 12 money facts × 8 lines, plus ship rosters) carries a `verified`
date and a `source` URL. Re-verify on a 30-day cycle so nothing is ever presented past its window
(Hard Rule 7). There is a tool for this.

### 2a. Run the audit
```bash
cd newsite
python3 verify.py status      # summary + exits non-zero if anything is due (also run before deploy)
python3 verify.py report      # full per-line checklist: each fact, its source URL, days since verify
python3 verify.py report --window 30 > /tmp/recheck.txt   # force a 30-day threshold, save to a file
```
`report` prints, per line, every fact marked `[ok]`, `[DUE]`, or `[GAP]` with the exact source URL to
open. Work top to bottom.

### 2b. For each fact
1. Open the `source:` URL in the report.
2. Compare the published value to what we show (`newsite/facts.py → LINE_FACTS[<line>][<fact>]`).
3. **If it still matches:** update just the `verified` date to today in `facts.py`.
4. **If it changed:** update the `v` value (EN + ES), the `verified` date, and the `src` if the URL
   moved — then follow §4 (publish an Update, because a changed fact is news) and check whether any
   page copy or tool text needs to change (§4c).
5. **If the source page is gone / can't be read:** set `v` to `None` (renders as a visible "Not yet
   verified" gap — never guess) and note it to chase manually.

### 2c. Ship rosters, ports, deployment
- Ship rosters: `newsite/data/ships/*.json` — each file has a `verified` date; re-check new ships,
  retirements and capacity every 90 days (or when an alert fires).
- Regions / home ports / seasons: `newsite/data/deployment.json` — re-check itinerary seasons ~60 days.

### 2d. Finish
```bash
python3 verify.py status      # should now say "✓ all current — nothing due."
python3 build.py              # must end "✓ banned-term guard clean"
```
Then deploy (PROJECT-HANDBOOK §3). Done.

---

## 3. Calendar reminder — set it up once (Google Calendar)

So the 30-day job never slips:

1. Google Calendar → **Create → Event**.
2. Title: **"CruiseLineAdvisors — 30-day fact re-check"**.
3. Date: today. Time: a 1-hour block you'll actually use.
4. **Recurrence → Custom → Repeat every 1 month** (or "every 30 days"). *(Monthly is close enough and
   easier to read; if you want exactly 30 days, choose "every 30 days".)*
5. **Notification:** add **Email — 1 day before** and **Notification — at time of event**.
6. Paste this into the event **Description** (your runbook-in-a-reminder):
   ```
   cd newsite && python3 verify.py report --window 30
   Re-verify each DUE/GAP fact against its source URL. Update facts.py verified dates.
   If a value changed: update facts.py + publish an Update (docs/OPERATIONS.md §4).
   Finish: python3 verify.py status  → build.py  → deploy.
   ```
7. Save. You'll now get an email reminder every cycle with the exact steps.

*(Optional: also set the recurring reminder in whatever you check daily — phone reminders app, Todoist,
etc. The calendar event is the source of truth.)*

---

## 4. Publishing an Update (and propagating it)

The Updates pipeline is already automatic for placement; the fact change is the manual part.

### 4a. Add the update entry
Edit `newsite/updates.py → UPDATES` (newest first). One entry:
```python
{"date": "2026-08-15", "slug": "carnival-gratuity-2026", "lines": ["carnival"],
 "title": {"en": "...", "es": "..."},
 "body":  {"en": "one-line summary", "es": "..."},
 "detail":{"en": "the fuller, sourced explanation", "es": "..."}}
```
- `lines`: the slugs it affects (`["carnival"]`). **Empty `[]` = general → shows on every line page.**
- `slug`: becomes the detail URL `/updates/<slug>/`.

### 4b. What happens automatically
Rebuilding after adding the entry makes it appear, with **no other edits**:
- on the **Updates page** (`/updates/`), and
- in the **"Latest updates" section of each tagged line's page** (via `updates_for(slug)`), and
- as its own **detail page** `/updates/<slug>/`.
This is already wired — see `updates.py` docstring and `pages.py` (line-page updates section).

### 4c. If the update CHANGES A FACT — also do this (NOT automatic)
The compare tool, line pages and ship pages read facts from `newsite/facts.py` (single source of
truth). An Update entry is just news copy; it does **not** change the numbers shown. So when a policy
value actually changes:
1. Update the value in `facts.py → LINE_FACTS[<line>][<fact>]` (`v` EN+ES, `verified`, `src`).
   → This automatically updates the **compare tool, the line page facts, and any ship page** that
   shows that fact, everywhere, because they all read `facts.py`.
2. If the change affects *descriptive copy* (e.g. a guide paragraph, a page intro), update that
   generator/data too.
3. Rebuild → `verify.py status` → guard clean → deploy.

**Rule of thumb:** *Update entry = the announcement. `facts.py` edit = the actual number.* A fact
change needs both.

---

## 5. Monitoring — Google Alerts + Feedly (facts-only)

Goal: get a **weekly** heads-up ONLY about things that change a fact we publish — gratuities/service
charges, drink-package rules, Wi-Fi, deposit/final-payment, cancellation/refunds, kids age & clubs,
travel documents, loyalty tiers, onboard-credit terms, and fleet changes (new/retiring ships). Ignore
general cruise news, deals, and marketing.

### 5a. Google Alerts (google.com/alerts) — create these ~7 alerts
For **each**: set **How often = At most once a week**, **Sources = Automatic**, **Language = English**,
**Region = United States** (or Any), **How many = Only the best results**, deliver to your inbox.

1. `cruise ("daily gratuity" OR "gratuities" OR "service charge" OR "crew appreciation") (increase OR change OR update OR raises)`
2. `cruise ("beverage package" OR "drink package" OR "Wi-Fi package" OR "internet package") (change OR policy OR rule OR price)`
3. `cruise ("cancellation policy" OR "final payment" OR "deposit" OR "refund policy") (change OR update)`
4. `cruise ("minimum age" OR "kids club" OR "youth program" OR "sailing age") (policy OR change)`
5. `cruise ("passport" OR "birth certificate" OR "closed-loop") (requirement OR rule OR change)`
6. `("Royal Caribbean" OR "Carnival" OR "Princess" OR "Celebrity Cruises" OR "Holland America" OR "MSC Cruises" OR "Cunard") ("new ship" OR "joins the fleet" OR "maiden voyage" OR "retires" OR "leaves the fleet")`
7. `("Royal Caribbean" OR "Carnival" OR "Princess" OR "Celebrity Cruises" OR "Holland America" OR "MSC Cruises") ("loyalty program" OR "onboard credit" OR "tier" OR "member benefit") change`

*Tip:* if any alert is too noisy, tighten it by adding a line name, or change "How many" to "Only the
best results". If it's too quiet, broaden the OR list. Review and prune every quarter.

### 5b. Feedly (feedly.com) — a focused folder + weekly digest
1. Create a folder/board named **"CLA — Fact Watch"**.
2. Add the **official cruise-line newsrooms** (primary, most trustworthy sources) — search each in
   Feedly by name and follow their press/news page, e.g.:
   - Royal Caribbean Press Center, Carnival newsroom, Princess news, Celebrity newsroom,
     Holland America news, MSC Cruises press, Cunard news.
3. Add **1–2 reputable trade sources** for policy coverage (e.g. Cruise Industry News, USA Today
   Cruises). Keep the list short — quality over volume.
4. **Filter to facts only:** on Feedly Pro use a **Mute/Priority filter** so only articles containing
   words like `gratuity, service charge, beverage package, cancellation, deposit, passport, minimum
   age, new ship, retire` surface. On the free tier, just skim the folder weekly for those words.
5. **Weekly digest:** Feedly → settings → enable the **weekly email newsletter** for that folder, or
   just open the folder once a week (pair it with the calendar reminder in §3).

### 5c. When an alert/feed fires
Open the source → confirm it's a real policy change to one of our 12 facts → do §4 (publish the
Update **and** edit `facts.py` if a value changed) → deploy. If it's not fact-affecting, ignore it.

---

## 6. Guides section — content plan

Live now (`newsite/pages.py → GUIDES`, bodies in `GUIDE_BODY`): First-time cruisers · Choosing a cabin ·
What's included · When to cruise · Groups & families · Accessibility.

Proposed additions (all compliant — general how-to, no prices, original copy):
- **Understanding gratuities & onboard charges** — ties directly to our #1 fact; strong internal link
  to the compare tool.
- **Drink & Wi-Fi packages explained** — the rule that surprises people (whole-cabin purchase).
- **Cancellation, deposits & travel insurance** — the money-at-risk timeline.
- **Cruise documents & ID** — passport vs birth certificate, closed-loop sailings.
- **Solo cruising** — single supplement and studio cabins (links to the finder's Solo persona).
- **Shore excursions: book with the line or independently** — decision guide.
Each new guide = one dict in `GUIDES` + its body in `GUIDE_BODY` (EN/ES). They auto-appear on the
Guides hub and get their own page. Prioritise the first three — they reinforce the fact pages and
push calls.

---

## 7. Pre-deploy checklist (every time)
- [ ] `python3 verify.py status` → "✓ all current" (or you intentionally accept the flagged gaps)
- [ ] `python3 build.py` → "✓ banned-term guard clean"
- [ ] `python3 tests/test_regions.py && python3 tests/test_party.py && python3 tests/test_search.py` → all PASS
- [ ] No placeholder strings left where a real value is due (phone, address, emails)
- [ ] `rm -rf site && cp -r newsite/dist site` → commit `newsite/` + `site/` → push `main`
