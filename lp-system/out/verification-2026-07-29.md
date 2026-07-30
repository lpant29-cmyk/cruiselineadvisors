# Verification record — 2026-07-29 (research-registrar)

Scope: Galveston slice priority checks requested by the operator after external
verification reports. All evidence below is from official sources on
lp-system/data/source_whitelist.txt (royalcaribbean.com, cbp.gov,
portofgalveston.com). Raw responses cached under
lp-system/out/cache/2026-07-29-registrar/.

## 1. Mariner 9/10-night from Galveston (reported package MA09W208) — NOT BOOKABLE

Claim under test (third-party, treated as a question only): an official RC
itinerary page exists for a 9-Night Western Caribbean from Galveston on Mariner
(MA09W208), and possibly a 10-night Mariner route through Oct 2026, implying our
enumeration missed them.

Queries run (POST https://www.royalcaribbean.com/graph, cruiseSearch, polite
sequential curl):

- filters "departurePort:GAL", pagination count 50
  (cache: graph-GAL-recheck.json). Result: total=16 groups, identical to the
  2026-07-29 enumeration i0003-i0018. Mariner appears ONLY as:
  - MA04GAL-597171001, 4N, 7 sailings 2026-08-13 .. 2026-10-26
  - MA05GAL-2956042404, 5N, 11 sailings 2026-08-03 .. 2026-10-17
  No Mariner 9N or 10N group from Galveston exists in bookable inventory.
- filters "ship:MA", pagination count 100 (cache: graph-ship-MA.json).
  Result: total=33 groups fleet-wide for Mariner. The only Galveston groups are
  the 4N and 5N above, ending 2026-10-26. From 2026-11 Mariner's bookable
  deployment shifts to New Orleans (MSY) and, for summer 2027, Europe
  (BCN/BLQ/LIS/ROM). Every Mariner 9-night in bookable inventory is either
  Europe (MA09M345-M349) or New Orleans (MA09W211, 2027-11-04); both 10-nights
  are Europe (MA10M412-M414 family from BCN/LIS). MA09W208 appears NOWHERE in
  bookable inventory.
- Direct probe of the reported package URL pattern:
  https://www.royalcaribbean.com/itinerary/9-night-western-caribbean-cruise-from-galveston-on-mariner-MA09W208?packageCode=MA09W208&country=USA
  returned HTTP 307 redirecting to https://www.royalcaribbean.com/cruises
  (the generic search page). RC's own site does not serve a live detail page
  for MA09W208; whatever page the external report saw, RC now redirects it to
  search. Consistent with a past deployment, not a bookable product.

VERDICT: no bookable future Mariner 9- or 10-night sailings from Galveston.
No rows added to 03_itineraries.csv / 04_itinerary_days.csv. The 9+ nights
filter band for the Galveston slice correctly contains exactly two products:

- i0016 Liberty 9N (LB09W212), single sailing 2027-08-12
- i0018 Symphony 10N one-way to Ft. Lauderdale (SY10R043), single sailing 2027-08-08

Any ad copy or page module claiming a Mariner 9/10-night from Galveston would
be unsupported by the operator's own site as of 2026-07-29.

## 2. Harmony of the Seas from Galveston — NO FUTURE GALVESTON SAILINGS

Queries run:

- filters "ship:HM", pagination count 100 (cache: graph-ship-HM.json).
  Result: total=23 bookable groups for Harmony, EVERY ONE departing PCN
  (Port Canaveral/Orlando), sail dates 2026-08-18 through 2028-04-15.
  Zero Galveston groups.
- Official ship page https://www.royalcaribbean.com/cruise-ships/harmony-of-the-seas
  (cache: ship-harmony.html, HTTP 200, server-rendered): the body copy states
  Harmony sails the Caribbean from Port Canaveral in Orlando, and the
  server-rendered sailing cards on the page are all Port Canaveral packages.
  Galveston appears only in the sitewide footer port-link list.
- Cross-check: the departurePort:GAL recheck above (16 groups) contains no
  Harmony group.

VERDICT: Harmony of the Seas has no bookable future sailings from Galveston;
its bookable deployment is Port Canaveral through at least April 2028. This is
the documented official evidence for keeping the p002--harmony ad group
("harmony of the seas galveston", ~480/mo) PAUSED at launch. The page/ad group
should intercept that search demand only with honest "Harmony no longer sails
from Galveston; here is what does" messaging if it is ever activated, and that
is a structure-guard/operator call, not a registrar one.

## 3. Enrichment provenance (same date)

- Currency, 05_ports_content.csv, verified from the Currency Accepted block on
  official royalcaribbean.com/cruise-to port pages (each row now carries its
  source URL and retrieved_date 2026-07-29):
  roatan HNL;USD - belize-city BZD (RC page notes most shops also take USD) -
  george-town KYD - falmouth JMD;USD - cozumel USD;MXN re-verified.
  GAP: costa-maya page returned HTTP 503 on two attempts; existing USD;MXN
  value kept from prior collection with an honest note, re-source when the
  page loads.
- Galveston pre-cruise module facts from
  https://www.portofgalveston.com/cruise-parking/explore-the-port/explore-galveston/
  (port authority site): Strand Historic District (National Historic Landmark,
  Victorian architecture), Texas Seaport Museum with the tall ship Elissa,
  Galveston Island Historic Pleasure Pier, East Beach, Galveston Island State
  Park (2,000+ acres), Moody Gardens (aquarium, Rainforest Pyramid). Written
  into a new trailing pre_cruise column in our own words. galveston.com (CVB)
  was NOT used: off-whitelist.
- FAQ q001 closed-loop documents confirmed on
  https://www.cbp.gov/travel/us-citizens/western-hemisphere-travel-initiative
  (page last modified 2026-06-17): US citizens on closed-loop cruises may enter
  the US with a birth certificate and government-issued photo ID; a passport
  may still be required by countries the ship visits; under-16s may travel on a
  birth certificate alone. Source URL recorded on the q001 row.
  GAP: travel.state.gov cruise-passengers page returned HTTP 403 (bot block)
  via two fetch methods; CBP alone is the recorded source.
