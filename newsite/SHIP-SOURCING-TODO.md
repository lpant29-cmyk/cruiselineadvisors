# Ship data — official-source checklist

Rule: **official cruise-line sites only** (no Wikipedia/third party). Anything not on an official
readable page renders as a "Not yet verified" gap until filled. Each ship page + fleet listing
carries a "Verified from official sources · checked <date>" stamp.

## ✅ Done — sourced from official sites (live)

### Celebrity Cruises — 15 ships (celebritycruises.com per-ship pages)
- Gross tonnage + guest capacity: **official, verified** for 14/15.
- **Still needed (official):**
  - `Celebrity Xcel` — gross tonnage + guest capacity (official page is marketing-only so far)
  - **Year entered service** for all ships except *Beyond* (2022) — Celebrity does not publish
    year on the ship pages. If you can get the official year per ship, paste it.

### Margaritaville at Sea — 2 ships (margaritavilleatsea.com)
- Years: **official** (Paradise 2022, Islander 2024).
- **Still needed (official):** gross tonnage, guest capacity, decks, ship class — for BOTH
  Paradise and Islander (none published anywhere on the official site).
- Beachcomber intentionally excluded (upcoming, PortMiami 2027 — not in service).

## ⏳ Pending — official spec pages are JavaScript-locked (session limit hit mid-run)

For these six, the official **fleet pages list the ships** (names, and some show class) but the
official **ship pages don't expose specs in readable HTML**. I will retry after the limit resets:
(a) confirm official rosters + class from the fleet pages, (b) hunt official press/media
**fact-sheet PDFs** for tonnage/guests/year. Whatever still isn't on an official readable page,
I'll list here for you to paste.

Per ship I need, **from the official site**: `class`, `year entered service`, `gross tonnage`,
`guest capacity`.

- **Royal Caribbean** (~28 ships) — official fleet list read; specs JS-locked
- **Holland America** (11 ships) — official roster + class read; "Ships at a Glance" PDF to try
- **Carnival** (~29 ships) — official fleet list read; specs JS-locked
- **Princess** (~17 ships) — official fleet page timed out; retry
- **Cunard** (4 ships: Queen Mary 2, Victoria, Elizabeth, Anne) — retry official "in numbers" pages
- **MSC** (~23 ships) — official US fleet page 403'd; retry msccruises.com / press area

## How to paste (any line)

Just send lines like:
```
Celebrity Xcel: GT 141,420, guests 3,260
Carnival Mardi Gras: Excel class, 2021, GT 180,800, guests 5,282
```
…and I'll drop them straight into `data/ships/<line>.json` with today's verified date.
