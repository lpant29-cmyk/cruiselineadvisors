# Campaign brief: first test launch (2026-08-05)

Scope: **only the three live pages.** Nothing here points at a page that
does not exist.

Account: Ads `AW-18339104693` · GA4 `G-JTQWHFMTB8` · GTM `GTM-NM78WCVF`
Conversions and Google call forwarding already configured.

---

## RULE: no cruise line trademarks in ad text

**Keywords may contain "Royal Caribbean", "Icon of the Seas" etc. Ad
headlines, descriptions, callouts and sitelink text may NOT.**

We are an independent referral service, not an authorised reseller, so
using the line's marks in ad copy invites a trademark complaint and
contradicts the disclosure on every page. Google permits trademarked terms
as keywords; it restricts them in ad text.

Write around it: "the biggest ships sailing from Galveston", "major cruise
lines", "your cruise". Never the brand or ship name.

---

## Message match: how the pages adapt

Each ad group passes a URL parameter and the page reshapes itself. This is
now real, not cosmetic: the headline **and the sailings shown** both change.

| Parameter | Headline becomes | Sailings shown |
|---|---|---|
| none | Royal Caribbean Cruises from Galveston | all 16 |
| `?v=icon` | Icon of the Seas Cruises from Galveston | 3 (Icon only) |
| `?v=symphony` | Symphony of the Seas Cruises from Galveston | 5 |
| `?v=liberty` | Liberty of the Seas Cruises from Galveston | 6 |
| `?v=mariner` | Mariner of the Seas Cruises from Galveston | 2 |
| `?nights=4` | unchanged | 5 short sailings |
| `?v=4night&nights=4` | 4-Night Royal Caribbean Cruises from Galveston | 5 |

A visible notice tells the visitor the list is narrowed, with a one-click
"See all 16 sailings" reset. Unknown values are ignored and the full page
renders, so a mistyped ad URL can never break anything.

The variant list is generated from the page's own inventory, so a headline
can only name a ship that genuinely sails from Galveston.

---

# CAMPAIGN 1 — RC-p002-BOOK

**Settings**
- Search only. **Off:** Display network, Search Partners.
- Budget $30/day · Maximize Conversions
- Locations: TX + OK, presence-based ("people in or regularly in"), not interest
- Ad schedule 8am–11pm ET daily
- Primary conversions: calls 60s+, lead_submit. Phone-click observational only.

### Ad group `p002--core` — bid $0.80
Final URL: `https://cruiselineadvisors.com/en/go/lines/royal-caribbean/from/galveston/`
```
[royal caribbean cruises from galveston]          9,900
[royal caribbean galveston cruise port]           1,900
[royal caribbean out of galveston]                  880
[royal caribbean galveston schedule]                480
[royal caribbean cruise port in galveston texas]    260
```

### Ad group `p002--icon` — bid $0.70
Final URL: `.../from/galveston/?v=icon`
```
[icon of the seas galveston]                      2,900
```

### Ad group `p002--symphony` — bid $0.90
Final URL: `.../from/galveston/?v=symphony`
```
[symphony of the seas galveston]                    590
```

### Ad group `p002--liberty` — bid $0.70
Final URL: `.../from/galveston/?v=liberty`
```
[liberty of the seas galveston]                     110
```

### Ad group `p002--4night` — bid $0.70
Final URL: `.../from/galveston/?v=4night&nights=4`
```
[royal caribbean 4 day cruise from galveston]       210
```

**Do not create harmony or allure ad groups.** Neither ship sails from
Galveston (verified at source, `lp-system/out/verification-2026-07-29.md`).

---

# CAMPAIGN 2 — RC-p008-SHIP-TEST

An explicit experiment. These ship-name terms are parked in our research as
broad-brand: most searchers want photos, not a booking. Worth testing only
because the page match is exact and clicks should be cheap.

**Budget $10/day · max CPC $0.40**
Final URL: `https://cruiselineadvisors.com/en/go/ships/mariner-of-the-seas/`

### Ad group `p008--ship-name`
```
[mariner of the seas ship]                       33,100
[royal caribbean mariner of the seas]             6,600
[mariner of the seas cruise ship]                 1,900
[royal caribbean cruise mariner of the seas]      1,300
```

**Campaign negatives** (Seven Seas Mariner is a different line entirely):
```
-[seven seas mariner]  -regent  -"seven seas"  -"deck plan"  -"deck plans"
-webcam  -tracker  -wiki  -"dry dock"  -refurbishment
```

**Kill criterion:** $70 spent with zero 60-second calls, pause it. That is
a cheap answer to a real question.

---

# CAMPAIGN 3 — none

The itinerary page gets no campaign. Its only matching keywords run 10 to
70 searches a month. It is a supporting page people reach by clicking
"View full itinerary" from the finder, and it deepens the funnel there.

---

## Ad copy (trademark-free)

**Headlines** — max 30 chars each, 8 to 12 per ad group:
```
Cruises From Galveston
Sailings From Galveston TX
Talk To A Cruise Advisor
Unadvertised Bundle Rates
Call For Exclusive Rates
16 Sailings From Galveston
Advisors 8am To 11pm ET
Free To Call, No Obligation
Bundle Cruise Flight Hotel
Ask About Onboard Credit
Licensed Travel Advisors
Your Dates Priced By Phone
```

For `p002--icon` / `--symphony` / `--liberty`, still no ship names. Use:
```
The Biggest Ships From Galveston
Newest Ships, Galveston Sailings
Ask Which Ship Fits You
```

**Descriptions** — max 90 chars:
```
One call compares every sailing from Galveston for your dates. Free, no pressure.
Bundle cruise, flight and hotel by phone. Advisors answering 8am to 11pm ET.
Unadvertised bundle rates and onboard credit on qualifying sailings. Call now.
Licensed advisors price your exact dates and cabins. No obligation.
```

**Never in ad text:** any cruise line or ship name · "cheapest" · "lowest
price" · "guaranteed" · "% off" · any dollar figure.

**Assets:** call asset (forwarding number) · callouts "Free to call",
"No obligation", "Licensed advisors", "8am to 11pm ET" · sitelinks to the
ship page and itinerary page, with trademark-free link text such as
"Ship guide" and "5-night itinerary".

---

## Account-level negatives

Add all 121 terms from `lp-system/data/rc_negatives.txt` as a shared list
named "RC service desk + info", applied to both campaigns. They block the
line's own customer-service seekers (check in, my booking, boarding pass),
researchers (deck plans, menus, drink prices) and the irrelevant (jobs,
stock, lawsuits).

---

## Bids

Planner reports these at $0.15–$0.45 low, $1.15–$2.32 high, competition Low
to Medium. The bids above are roughly 3x the low estimate. If impression
share is under 30% after three days, raise bids rather than budget: with
nine keywords you want to win the auctions you enter.

---

## First-week checklist

1. Day 1: call the forwarding number yourself, stay on 60+ seconds, confirm
   the conversion lands in Ads.
2. Day 1: click each ad group's URL and confirm the page narrows as the
   table above says.
3. Day 2: search-terms report, add negatives.
4. Day 3: impression share, adjust bids not budget.
5. Daily: run `/rate-update` so fares stay current. Stale fares render as
   "Fare on request" and convert worse.
6. End of week: apply Campaign 2's kill criterion honestly.

## What the test answers

Whether Galveston brand-and-port searchers **call**, and separately whether
ship-name browsers **call**. Two different bets, kept apart so one answer
cannot hide inside the other.

The 616,570 monthly searches still pointing at pages that do not exist are
the prize. This test says whether the model works before you build more.
