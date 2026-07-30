---
description: Daily price refresh for the live /go/ pages, gated and ready to push
---

Run the daily rate update for the live ads-LP pages. Work through this in
order and stop if a step fails.

## 1. Refresh the fares (pricing-scout)

Invoke the **pricing-scout** agent for a full Pass C over every itinerary
that feeds a live page (currently the 16 Galveston rows, i0003-i0018 in
`lp-system/data/03_itineraries.csv`).

Its standing rules apply and matter here: official `royalcaribbean.com`
sources only, one polite `royalcaribbean.com/graph` cruiseSearch query per
departure port returns every sailing at once, per-row evidence with the
literal value seen, and **never a guess** — a fetch that fails leaves the
old value with its old stamp and an UNVERIFIED note.

Because these fares ship the same day, have it run a second confirmation
query and report any row where the two disagree.

Also check the line's official promotions page. If a promo is live, record
it in `lp-system/data/07_offers.csv` **in our own words, attributed and
dated** ("Royal Caribbean promotion, seen {date}: ..."), never as our own
savings claim. Expired offers get `show_banner=no`.

## 2. Validate

```
python3 lp-system/scripts/validate.py
```

Flags are expected when fares move more than 25% against the last commit.
That is not automatically a stop: if pricing-scout double-confirmed the
value at source, it is real and publishes. A flag means "prove it", not
"hide it". Anything that could not be confirmed keeps its old value.

A fare that returns different numbers on different fetches gets
`HOLD: fare unstable at source` in its notes — the sailing still publishes,
only the number is withheld.

## 3. Rebuild and check

```
bash lp-system/scripts/deploy.sh
```

This rebuilds the main site, copies it to `site/`, regenerates the three
`/go/` pages, and hard-fails on a placeholder phone, a placeholder form
action, a missing noindex, `/go/` in the sitemap or robots, or any inbound
link from the main site. Do not work around a FAIL line; fix the cause.

Note the "fares withheld" count it prints. One or two is normal. If every
fare is withheld, the refresh did not actually work — investigate rather
than shipping a page with no prices.

## 4. Commit

Commit with a short summary of what moved, for example:

```
Daily rates {date}: 8 rows updated, 1 withheld as unstable
```

## 5. Hand back

Do **not** push. Tell the operator the exact command:

```
git push origin main
```

and summarise in plain language: which fares moved and by how much, any
row now showing "Fare on request" and why, any promo added or expired, and
anything that needs a human decision.

## Context worth remembering

- The pages carry a **freshness fuse**: a fare older than 3 days stops
  printing automatically and shows "Fare on request" instead. So a missed
  day is safe, but several missed days means the pages quietly go
  call-only.
- This inventory has moved more than 20% inside 24 hours. Treat the
  10-day staleness window in validate.py as a backstop, not as tolerance.
- If any live ad quotes a specific price, it must be updated in the same
  run (Google's pricing-accuracy policy covers the ad as well as the page).
- Full automation of this loop is designed but deliberately not built yet:
  see `lp-system/AUTOMATION-PLAN.md`.
