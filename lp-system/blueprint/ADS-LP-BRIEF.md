# ADS LP LAYER - BUILD BRIEF
### Noindexed, price-showing, call-conversion landing pages for paid traffic
For the cruiselineadvisors.com Claude Code project · July 28, 2026

---

## 1. Purpose and boundaries

A separate landing-page layer used ONLY as Google Ads destinations. These
pages show indicative pricing and convert to calls + inquiry forms. They are
noindexed and never linked from the main site, so the SEO/content site and
the ads funnel stay cleanly separated.

Business posture is unchanged: referral service, no booking, no payments.
Prices shown are observed lead-in fares, date-stamped, quotes and bookings
by licensed partner agencies.

## 2. URL scheme

All ad LPs live under /go/ with locale prefix, mirroring page types:

- /en/go/ships/icon-of-the-seas/
- /en/go/from/galveston/
- /en/go/lines/royal-caribbean/
- /en/go/family-cruises/
- /es/go/... (Spanish mirrors, phase 2)

Rules: lowercase-hyphen slugs, no dates in URLs, one LP = one ad group =
one search intent. Never canonicalize /go/ pages to main-site pages
(they serve different funnels); each /go/ page is its own destination.

## 3. Indexing and isolation

- <meta name="robots" content="noindex,nofollow"> on every /go/ page.
- Disallow: /en/go/ and /es/go/ in robots.txt is NOT enough on its own and
  actually blocks Google from seeing the noindex tag - use the meta tag,
  do not block /go/ in robots.txt.
- No links from main-site nav, sitemaps, or content pages into /go/.
- /go/ pages may link OUT to main-site guides only in the footer small
  print (trust), never in the body (exit paths kill conversion).

## 4. Page anatomy (all four types share this skeleton)

1. Disclosure ribbon (top, always visible): independent referral service,
   not the cruise line, not the cruise line's customer service.
2. Slim header: brand + toll-free number only. NO site navigation.
3. Hero: query-mirroring H1 + subline + hours badge ("Advisors answering
   now · 8am-11pm ET").
4. Call zone: large tap-to-call block (+1-833-684-4250 or campaign
   tracking number) + 3-field callback/inquiry form (name, phone, best
   time). Form posts to existing CRM endpoint; TCPA consent line links to
   /en/legal/consent/.
5. Deal cards (from master sheet): itinerary name, ship, nights, departure
   port, sail months, "Recently from $X" + date-checked stamp + "Call for
   today's fare" CTA. 3-6 cards per page.
6. One context module per page type (see section 5).
7. Offer ribbon slot: renders active offers rows (facts only, our own
   wording and design, auto-expires on end_date).
8. Why-call section (reuse existing site copy blocks: straight answers,
   specialist not script, no pressure).
9. Final call band + sticky mobile call bar (call + callback buttons).
10. Footer: compact legal (see section 6), FST/CST line NOT applicable
    (referral service - keep the existing "what we are" language instead).

Design: reuse the site's existing design system - theme #0A2540, existing
typography, existing components where possible. These must look and feel
like cruiselineadvisors.com, not a different brand.

## 5. Context module per page type

- SHIP LP: cabin categories mini-tabs + "which cabins we recommend" notes
  (reuse ship-directory data).
- PORT LP: getting there / parking basics / who sails from here (new
  content; verified-facts framing like the rest of the site).
- LINE LP: ship classes at a glance + the fine-print facts teaser (reuse
  cruise-facts data for that line).
- AUDIENCE LP: fit-by-ages or fit-by-style guidance (family: kids club age
  bands; couples: adults-only options).

## 6. Pricing display rules and REQUIRED legal updates

Because the main site currently states it displays no fares, shipping
prices on /go/ REQUIRES these changes in the same deploy:

a) /go/ page footer pricing language (every /go/ page):
   "Prices shown are per-person lead-in fares based on double occupancy,
   observed from publicly available sources on the date stamped with each
   offer. They exclude taxes, fees and port expenses, change frequently,
   and are not an offer to sell travel. All quotes, availability, bookings
   and payments are handled by independent licensed travel agencies. We do
   not sell, book or take payment for travel."

b) Sitewide footer edit: replace "This site displays no fares, rates,
   discounts or savings." with:
   "Pricing: fares shown anywhere on this site are indicative, observed
   from public sources on the date stamped, and are not an offer to sell
   travel; all quotes and bookings are provided by independent licensed
   agencies."

c) Terms page: mirror the same change in the pricing clause.

Operational rules:
- Every displayed price carries its date_checked stamp. No stamp, no price.
- Ad copy price claims must match the LP price and be updated in the same
  weekly run (Google pricing-accuracy policy).
- validate script flags: stamps older than 10 days, prices moved >25%
  since last run, offers past end_date still flagged show_banner=yes.

## 7. Data wiring (master sheet)

- deals tab drives the cards. page_targets column maps deals to LPs
  (ship:icon-of-the-seas;port:galveston;line:royal-caribbean;aud:family).
- from_price + date_checked are now PUBLIC on /go/ pages (decision made
  July 28, 2026). Keep internal-only columns (source, notes) out of the
  published CSV range.
- offers tab drives ribbons per banner_pages.
- Build-time generation preferred (generate.py renders static /go/ pages
  from sheet CSV at deploy) over client-side fetch: faster LPs = better
  Quality Score; weekly deploy cadence matches the rate-update run anyway.

## 8. Tracking

- Each campaign gets its own Google forwarding number or tracking number
  pool on its LP (PHONE_TEL / PHONE_DISPLAY variables per page).
- Conversion events: calls from ads (call reporting), 60s+ call duration
  as primary conversion, form submit -> thank-you page as secondary.
- GTM container already on site (GTM-NM78WCVF): add /go/ page-type and
  campaign dataLayer variables.

## 9. Build order

1. Footer/terms legal updates (section 6b, 6c) - same deploy as first LP.
2. /en/go/lines/royal-caribbean/ (first brand-keyword campaign target).
3. /en/go/from/galveston/ + /en/go/from/miami/ (port intent).
4. /en/go/ships/icon-of-the-seas/ (ship intent).
5. /en/go/family-cruises/ (audience).
6. generate.py + validate.py wired to the sheet; then scale pages from the
   pages tab registry.
7. /es/go/ mirrors for the top performers.

## 10. Definition of done per LP

- Renders from sheet data with correct deal_filter
- noindex meta present; absent from sitemap; zero inbound internal links
- Disclosure ribbon + pricing footer present
- Call + form conversions firing in test
- Mobile sticky bar functional; page weight under ~150KB excluding images
- Date stamps current at deploy
