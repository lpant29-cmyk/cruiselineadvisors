# Campaign brief: first test launch (2026-08-05)

Scope: **only the three live pages.** No keyword in this brief points at a
page that does not exist. Everything else in the research stays parked
until its page is built.

Account: Ads `AW-18339104693` · GA4 `G-JTQWHFMTB8` · GTM `GTM-NM78WCVF`
Conversions and Google call forwarding are already configured.

---

## What can actually launch

| Page | Live URL | Campaign | Exact KWs | Volume |
|---|---|---|---|---|
| p002 finder | `/en/go/lines/royal-caribbean/from/galveston/` | RC-p002-BOOK | 9 | 17,230/mo |
| p008 ship | `/en/go/ships/mariner-of-the-seas/` | RC-p008-SHIP-TEST | 4 | 41,910/mo* |
| p007 itinerary | `/en/go/itineraries/5-night-...-mariner-of-the-seas/` | **none** | 0 | 70/mo |

\* high volume but low intent, see the warning on that campaign.

**p007 gets no campaign, deliberately.** The only keywords that match it
are 10 to 70 searches a month. It is a supporting page: people reach it by
clicking "View full itinerary" from the finder. Spending on it would buy
almost nothing. It still earns its keep by deepening the funnel.

---

# CAMPAIGN 1 — RC-p002-BOOK (the real test)

This is the one that matters. Tight theme, real inventory behind it,
16 bookable sailings on the page.

**Settings**
- Type: Search only. **Turn OFF** Display network and Search Partners.
- Final URL: `https://cruiselineadvisors.com/en/go/lines/royal-caribbean/from/galveston/`
- Budget: $30/day to start
- Bidding: **Maximize Conversions**. Move to tCPA only after 30+ conversions.
- Locations: **TX and OK** (drive market for Galveston), then LA. Target
  "people in or regularly in your targeted locations", not "interested in".
- Ad schedule: **8am to 11pm ET, every day.** Nobody answers outside that,
  and a missed call is a wasted click.
- Conversions: primary = calls 60s+ and lead_submit. tel_click is
  observational only, never a bidding signal.

**Ad groups and keywords** (all exact match, `[...]`)

`p002--core` — bid $0.80
```
[royal caribbean cruises from galveston]      9,900/mo
[royal caribbean galveston cruise port]       1,900/mo
[royal caribbean out of galveston]              880/mo
[royal caribbean galveston schedule]            480/mo
[royal caribbean cruise port in galveston texas] 260/mo
```

`p002--icon` — bid $0.70
```
[icon of the seas galveston]                  2,900/mo
```

`p002--symphony` — bid $0.90
```
[symphony of the seas galveston]                590/mo
```

`p002--2-4-night` — bid $0.70 · URL gets `?nights=4`
```
[royal caribbean 4 day cruise from galveston]   210/mo
```

`p002--liberty` — bid $0.70
```
[liberty of the seas galveston]                 110/mo
```

**DO NOT create these two ad groups yet:**
`p002--harmony` and `p002--allure`. Royal Caribbean's own data confirms
neither ship sails from Galveston (Harmony is at Port Canaveral through
2028). Bidding on them sends people to a page that cannot serve them.
Evidence: `lp-system/out/verification-2026-07-29.md`.

**Phrase-match discovery (optional, second week):** add
`"royal caribbean cruises from galveston"` in its own ad group at a lower
bid, purely to mine search terms. Do not add it on day one.

---

# CAMPAIGN 2 — RC-p008-SHIP-TEST (a genuine experiment)

**Read this before you launch it.** These keywords are parked in our own
research as BROAD-BRAND, meaning someone typing "mariner of the seas" is
usually looking at photos and deck plans, not booking. Our targeting policy
would normally exclude them.

They are worth testing anyway, for one reason: the page match is exact.
Keyword "mariner of the seas" to a page titled "Mariner of the Seas:
Cruises, Cabins and What's Onboard" at `/ships/mariner-of-the-seas/`. That
is a textbook Quality Score triangle, so clicks should be cheap.

The risk is real: 33,100/mo of mostly idle curiosity will spend a daily
budget fast. Cap it hard and judge it on calls, not clicks.

**Settings:** same as Campaign 1, but **budget $10/day** and
**bid cap $0.40**.
Final URL: `https://cruiselineadvisors.com/en/go/ships/mariner-of-the-seas/`

`p008--ship-name` — exact match
```
[mariner of the seas ship]                   33,100/mo
[royal caribbean mariner of the seas]         6,600/mo
[mariner of the seas cruise ship]             1,900/mo
[royal caribbean cruise mariner of the seas]  1,300/mo
```

**Kill criterion, decide it now:** if this campaign spends $70 (one week)
with zero calls over 60 seconds, pause it. It will have told you that ship
browsers do not dial, which is worth $70 to learn and not worth $700.

**Critical negatives for this campaign** (ship names collide across lines):
```
-[seven seas mariner]  -regent  -"seven seas"  -deck plan  -deck plans
-webcam  -tracker  -position  -wiki  -refurbishment  -dry dock
```
"Seven Seas Mariner" is a Regent ship, a different cruise line entirely.
Without these you will pay for their traffic.

---

## Account-level negatives (apply to BOTH campaigns)

All 121 terms in `lp-system/data/rc_negatives.txt`. Add as a shared
negative list named "RC service desk + info". They block people looking for
Royal Caribbean's own customer service (check in, my booking, boarding
pass, Crown and Anchor), researchers (deck plans, menus, drink prices,
dress code), and the irrelevant (jobs, stock, lawsuits, Wikipedia).

Without this list, brand keywords bleed budget on people who will never
call.

---

## Ads to write (both campaigns)

Responsive search ads. Match the page, and keep every claim scoped the way
the pages do.

**Headlines** (mix, 8 to 12):
- Royal Caribbean From Galveston
- Galveston Sailings And Dates
- Talk To A Cruise Specialist
- Unadvertised Bundle Rates
- Call For Exclusive Rates
- 16 Sailings From Galveston
- Advisors 8am To 11pm ET
- Free To Call, No Obligation

**Descriptions:**
- One call compares every Royal Caribbean sailing from Galveston for your
  dates. Free, no pressure.
- Bundle cruise, flight and hotel by phone. Advisors answering now,
  8am to 11pm ET.

**Never write in ads:** "cheapest", "lowest price", "guaranteed",
"% off", or any specific dollar figure. Prices change daily and Google's
pricing-accuracy policy covers ad text as well as the page.

**Assets:** add the call asset (your forwarding number), sitelinks to the
ship page and itinerary page, and a callout set: "Free to call",
"No obligation", "Licensed partner agencies", "8am to 11pm ET".

---

## Bids: expect to raise them

The bids above are roughly 3x Planner's low-range estimate, which is a
realistic opening. Planner reports these terms at $0.15 to $0.45 low and
$1.15 to $2.32 high, competition Low to Medium. If impression share is
under 30% after three days, raise bids rather than budget: on 9 keywords
you want to win the auctions you enter, not enter more of them.

---

## First-week checklist

1. Day 1: confirm a real call fires the conversion. Ring the forwarding
   number yourself, stay on 60+ seconds, check it lands in Ads.
2. Day 2: search-terms report. Add negatives for anything irrelevant.
3. Day 3: check impression share, adjust bids not budget.
4. Daily: run `/rate-update` so the fares on the page stay current. A page
   whose prices went stale shows "Fare on request" instead, which converts
   worse.
5. End of week: if Campaign 2 has spent with no 60s calls, pause it.

## What this test is actually answering

Not "do these keywords get clicks" — they will. The questions are whether
Galveston brand-and-port searchers **call**, and whether ship-name browsers
**call**. Two different bets, deliberately separated so one answer cannot
hide inside the other.

The 616,570 searches a month sitting in the research and pointing at pages
that do not exist yet is the prize. This test tells you whether the model
works before you build 40 more pages chasing it.
