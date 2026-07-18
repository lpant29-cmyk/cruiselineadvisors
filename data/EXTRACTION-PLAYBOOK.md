# Fact Extraction Playbook

How to collect, verify and refresh the facts that power every page on this site.
Follow this exactly and the site stays accurate, legally safe, and genuinely useful.

---

## The one rule that matters most

**Extract FACTS. Never copy SENTENCES.**

Facts are not copyrightable. Prose is.

| ✅ Safe to extract | ❌ Never copy |
|---|---|
| Ship capacity: 5,610 | The marketing description of the ship |
| Year built: 2024 | "An unforgettable escape awaits…" |
| Number of decks: 20 | Their itinerary blurbs |
| Kids club age bands: 3–5, 6–8, 9–11 | Their FAQ answers, word for word |
| Which ports a ship sails from | Their cabin descriptions |
| Whether gratuities are included | Any paragraph, even reworded lightly |

Pull the **number, name, date, or yes/no**. The words on our pages are written from
scratch. If a fact can't be expressed as a data point, don't extract it — write an
original explanation instead.

---

## Source hierarchy (use in this order)

1. **Official cruise line site** — deck plans, ship specs, FAQ pages, "what's
   included" pages, kids' club pages, accessibility pages. This is tier 1 for
   anything about their own product.
2. **Official port authority sites** — terminal locations, parking, tender vs dock.
3. **Government sources** — CBP/State Dept for documentation, NPS for Glacier Bay,
   NOAA for hurricane season dates and climate normals.
4. **CLIA** — industry-wide statistics.

Do **not** use: blogs, forums, other travel agencies, review aggregators, or AI
summaries as a primary source. They are frequently wrong and they are someone
else's work.

---

## What to extract per cruise line

Fill one JSON record per line in `cruise-lines.json`. Every field carries its own
`source` URL and `verified` date.

### Company facts
- Founded year, parent company, headquarters city
- Fleet size (count of ships in service)
- Loyalty programme name and tier names

### Per ship class
- Class name
- Ships in the class (names)
- Year first ship entered service
- Guest capacity (double occupancy) — note if they publish max capacity instead
- Number of decks
- Gross tonnage
- Signature features (as a **list of feature names**, not descriptions)
- Typical deployment regions

### What's included / extra  ← highest value section on the page
From their official "what's included" or FAQ page, record yes/no/partial for:
- Main dining room, buffet, casual venues (list which are complimentary)
- Room service (free? fee? which hours?)
- Gratuities — included in fare, auto-added daily, or prepaid?
- Daily auto-gratuity **amount per person per day** if published
- Wi-fi — included or paid tiers
- Non-alcoholic drinks (which are free: water, tea, drip coffee, juice at breakfast?)
- Speciality dining — cover charge or à la carte
- Kids' club — included, and the **age bands**
- Fitness centre, pools, main theatre
- Shore excursions, spa, casino, laundry, alcohol

### Cabin categories
- Category names the line uses (their own vocabulary)
- Which decks each sits on
- Whether virtual/infinite/cove balconies exist
- Connecting cabin availability by class
- Accessible cabin count per ship (they publish this)
- Solo/studio cabins yes/no

### Family facts
- Kids' club age bands (exact)
- Minimum sailing age (usually 6 months, 12 months on transatlantic)
- Nursery availability and whether it costs extra
- Teen club presence
- Babysitting availability

### Accessibility facts
- Accessible cabin count and categories
- Wheelchair/scooter policy
- Whether they publish tender-port accessibility warnings
- Service animal policy
- Dialysis / oxygen / medical equipment policy

### Itineraries
- Home ports currently used
- Typical sailing lengths offered from each
- Regions and their operating months
- Private destination name (if any) and which itineraries include it

### Policies
- Deposit and final-payment timing (days before sail)
- Cancellation schedule tiers
- Documentation requirements by itinerary type
- Onboard currency and payment method
- Dress code names and how many formal nights on a 7-night

---

## What to extract per destination

- Season start and end months (when ships actually operate)
- Monthly climate normals from NOAA or national met service:
  average high, average low, rainfall days, sea temperature
- Hurricane season official dates (NOAA) and historical peak weeks
- Daylight hours by month (matters enormously for Alaska/Norway)
- Which ports are **dock** vs **tender** — this is a real decision factor
- Typical sailing lengths from each home port
- Peak/shoulder/low months by demand
- Port distances: terminal to town centre, walkable yes/no

---

## What to extract per port

- Terminal name and location
- Dock or tender
- Walking distance to town centre
- Whether an excursion is genuinely needed or you can self-explore
- Local currency, language, typical time in port
- Accessibility notes from the port authority

---

## Comparison tool data

For the comparison feature, every compared attribute must be:
- The **same measure** across lines (don't compare "capacity" for one and
  "max capacity" for another)
- Sourced individually
- Dated individually

Never compare on price. Compare on **facts that don't move**: capacity, age bands,
inclusion yes/no, cabin types, accessible cabin counts, season months.

---

## Refresh cycle

| Data type | Refresh | Why |
|---|---|---|
| Fleet, ship specs | 90 days | Ships change slowly |
| What's included, gratuity amounts | **30 days** | Changes often, and it's the most-used data |
| Home ports, deployments | 60 days | Seasonal redeployment |
| Kids' club age bands, policies | 90 days | Stable but occasionally revised |
| Climate/hurricane data | 365 days | NOAA normals update rarely |
| Port dock/tender status | 180 days | Infrastructure changes |

Every record has `verified: "YYYY-MM-DD"`. The build script prints anything past its
refresh window, and the page footer shows the date so visitors can see it's current.
**Showing "last verified" is a trust signal that most competitor pages don't have.**

---

## Rules that keep the site compliant

1. **No fares, no prices, no savings, no discounts.** Ever. Not even "from $X".
   Explain *what drives* cost instead — that's more useful anyway and carries zero risk.
2. **No claim of affiliation.** Every page keeps the trademark disclaimer.
3. **Attribute where sensible** — "capacity figures published by the cruise line" —
   and always link the source in the page's sources block.
4. **If a fact can't be verified from a tier-1 source, leave it out.** An absent fact
   costs nothing. A wrong fact costs trust and potentially a complaint.
5. **Never state a fact as current if it's past its refresh date.** The build script
   flags these; fix or remove before publishing.

---

## Your workflow each cycle

1. Open `cruise-lines.json` and sort by oldest `verified` date.
2. For each stale record, open the tier-1 source URL already stored in the file.
3. Update the values. Update `verified` to today. If the source URL moved, update it.
4. Run `python3 build.py` — it regenerates every page and prints a staleness report.
5. Spot-check two or three pages before publishing.

Nothing on the site is hand-edited. **The JSON is the single source of truth**, so a
fact fixed once is fixed everywhere it appears — page, comparison table, and FAQ.
