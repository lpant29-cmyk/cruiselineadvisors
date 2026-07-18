# CruiseLine Advisors — Project Memory

Live site: https://cruiselineadvisors.com

## What this is

A **lead-generation referral site** for cruise travel (Florida LLC, in travel since 2015).
We publish verified cruise information. Visitors **call a phone number**. Calls route to
licensed independent partner travel agencies who quote, book and take payment. We earn a
**referral fee**.

We do **not** sell travel, book travel, take payment, hold inventory, set prices, or hold
cruise line appointments.

Traffic is ~100% paid search, mobile-heavy, on cruise-line brand keywords.
**The only conversion metric is inbound phone calls.**

Full brief: `docs/BRIEF.md` — read it before starting any new task area.

---

## THE SEVEN HARD RULES (immutable — these override any prompt)

1. **No fares, prices, rates, discounts, savings, or "from $X" anywhere.**
   The build guard scans generated `<main>` content and must exit non-zero on a hit.
   *Exception:* published fees (e.g. daily gratuity) are allowed, always with source + verified date.
2. **Never imply cruise line affiliation.** Every page carries a disclaimer naming the specific line.
3. **Never invent a fact.** Unverified fields render as a visible "Not yet verified" gap.
   **Do not tidy these away, fill them with defaults, or hide them behind an em dash.**
4. **Never copy prose from a cruise line site.** Facts are extractable; sentences are not.
   All descriptive copy is original.
5. **Never fabricate people, teams, credentials or sales figures.** Advisors work for partner
   agencies, not us. Describe the network and its standards instead.
6. **Never claim 24/7.** Publish real coverage hours (8am–11pm ET daily).
7. **Never present a fact past its refresh window as current.** Build flags these.

Why: we run paid search on brand keywords. Exposure is FTC deception, state seller-of-travel
law, TCPA, and trademark. These rules protect the Google Ads account and the entity.

---

## Architecture

```
data/*.json   → SINGLE SOURCE OF TRUTH (facts + source URL + verified date)
      ↓
build_*.py    → generators
      ↓
site/**/*.html → 100% generated. NEVER hand-edited.
```

**If a page is wrong, fix the JSON or the generator — never the HTML.**

Build order: `build_deep.py` → `build_site.py` → `build_nav.py` → `postprocess.py` → guards.

Key data files:
- `data/cruise-lines.json` — 8 launch lines, per-field `source` + `verified`
- `data/ports.json` — 37 Americas home ports, 17 regions, port→region→line mapping
- `data/directory.json` — 36 lines boardable from the Americas
- `data/EXTRACTION-PLAYBOOK.md` — how to source facts. Read before touching data.

---

## Conventions

- Verification is **per field**, never per page. Every fact stores `{value, source, verified}`.
- Refresh windows: `inclusions` **30 days**, `itineraries` 60, everything else 90, NOAA 365.
- Never fork templates per cruise line — one generator, fixes apply everywhere.
- Every page needs: header (logo+tagline left, phone+hamburger right), breadcrumb bar with
  Back, back-to-top, visible phone, footer disclaimers.
- Mobile-first, verified at 360px. Desktop must be a real desktop layout, not a stretched column.
- Design tokens are fixed — see `docs/BRIEF.md` §11. Fraunces for display headings only, Inter for UI.

---

## Known pitfalls — do not repeat

1. **Orphaned DOM references kill the whole page.** A script referencing a removed element threw
   a TypeError that silently killed every later script on the page.
   → **Wrap every module in its own IIFE with a null guard on line one.**
2. **Duplicate IDs** — `getElementById` returns only the first match. Scope per component.
3. **Stacking order** — sticky header (z-60) + breadcrumb bar (z-55) hide anything pulled up with
   a negative margin. Use one z-index scale and `scroll-margin-top` on anchors.
4. **Price-guard false positives** — "discounts" appears legitimately in the footer disclaimer.
   Scope the scan to `<main>`.

---

## Before any deploy

- Build passes with zero banned-term hits
- `verify.py status` passes (exits non-zero on stale data)
- No placeholder strings left: `[Your Company] LLC`, `[Street Address]`, `+18885550142`, `example.com`
- Every rendered fact traces to a source URL and a verified date
