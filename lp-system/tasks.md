# LP System Task Board

Format: `- [ ] [owner] task` (added date, by agent). Owners pick up their
tasks top to bottom; mark `[x]` when done and note the date.

## Open tasks

- [x] [research-registrar] TARGETED COLLECTION for combo:royal-caribbean-galveston ONLY.
  Run Pass A (enumerate Royal Caribbean itineraries departing Galveston TX) and
  Pass B (verify ships, nights, destinations, sail months, source_url per row)
  for this slice only, appending new rows to lp-system/data/03_itineraries.csv
  with page_targets including combo:royal-caribbean-galveston. Current publishable
  count is 2 (i0003, i0004); category page threshold is >=3 rows with a sailing
  in the next 6 months, so collect at least 1 more verified itinerary (more if
  found - RC sails Galveston year-round with multiple ships). Do NOT touch other
  ports or lines in this run. (added 2026-07-29, by structure-guard)
  DONE 2026-07-29 (research-registrar): Pass A found 16 active Galveston
  itineraries via royalcaribbean.com's own cruise-search service (/graph on
  royalcaribbean.com, whitelisted domain). i0003/i0004 re-verified against live
  packages IC06W319/IC08W072: sail months corrected to 2027 (seeds had 2026),
  official itinerary URLs now in source; their seeded prices + month overrides
  are STALE, pricing-scout must refresh. 14 new rows i0005-i0018 added (Mariner,
  Liberty, Symphony, Icon), each with official royalcaribbean.com itinerary URL
  in source; prices/date_checked left empty for Pass C. Ships s016-s018 added
  (verified on official ship pages). 120 day-by-day rows added to
  04_itinerary_days.csv for all 16 itineraries (Pass B complete). 7 new call-port
  rows in 05_ports_content.csv (minimal blurbs, own words, flagged for later
  enrichment). Rows with a sailing in next 6 months: 8 (i0005-i0011, i0014);
  threshold met once Pass C prices them. UNVERIFIED gaps: quad_cabins (not in
  search data) and taxes_note left empty on all Galveston rows; dest=caribbean
  (i0018) has no 06_destinations_content row. Manager: run
  lp-system/scripts/propose_pages.py.

- [x] [pricing-scout] After the research-registrar task above completes, run
  Pass C (pricing/verification pass) for ONLY the newly added
  combo:royal-caribbean-galveston rows in lp-system/data/03_itineraries.csv.
  (added 2026-07-29, by structure-guard)
  DONE 2026-07-29 (pricing-scout): all 16 Galveston rows i0003-i0018 priced from
  royalcaribbean.com/graph cruiseSearch (official domain, departurePort:GAL; raw
  response cached at lp-system/out/cache/2026-07-29/graph-departurePort-GAL.json).
  Interior+balcony lead-ins, month overrides, taxes_note (taxes and fees included
  per source), date_checked=2026-07-29 written; evidence diff in
  lp-system/out/candidates-2026-07-29.csv (76 lines + 2 offer lines). 0 rows
  UNVERIFIED. Known gaps: i0009 Aug-2026 sailings show no interior fare (balcony
  only, override carries b only); i0003 interior +32% and i0004 interior +36% vs
  stale seeds (expected, seeds predated the 2027 re-date; validate flags them for
  qa-auditor). Offer o002 (Instant Savings Flash Sale, ends 2026-07-31) drafted
  from /cruise-deals; o001 example retired. collect.py direct page fetches all
  failed on local Python SSL trust store (CERTIFICATE_VERIFY_FAILED) - graph via
  curl used instead; worth fixing certifi before next weekly run.

- [x] [structure-guard] Re-check inventory for combo:royal-caribbean-galveston
  after both tasks above; if >=3 publishable rows with a sailing in the next
  6 months, clear BLOCKED-ON-INVENTORY on p002 and hand off to page-builder,
  then qa-auditor Definition of Done, before any status change toward live.
  (added 2026-07-29, by structure-guard)
  DONE 2026-07-29 (structure-guard): BLOCKED-ON-INVENTORY cleared. 14 of 16
  Galveston rows are publishable under the provenance policy (official
  royalcaribbean.com source, priced, date_checked=2026-07-29, not UNVERIFIED);
  i0003/i0004 excluded per HOLD-2026-07-29 price-evidence hold. 9 publishable
  rows have a sailing in the next 6 months: i0005-i0011, i0014, i0015 (one more
  than registrar's count - i0015 sails 2026-08/09). Threshold >=3 met with
  margin. p002 status set built-template -> building in 09_pages.csv.
  Page-builder and qa-auditor tasks queued below. NOT done by me: no new pages
  registered from pages_proposed.csv (operator review pending; overlap with
  keyword-scout NPQ noted in run report); p001 NOT retired despite
  pages_retire_suggestions.csv - it is a pilot registration awaiting its own
  collection slice (Cape Liberty task queued below).

- [x] [page-builder] BUILD p002 (combo:royal-caribbean-galveston), status now
  building. Template family: finder (finder-rci-from-galveston.html), bake via
  generate.py with the T1/T2/T4 fixes already in the generator.
  deal_filter=combo:royal-caribbean-galveston; render only publishable rows
  (i0005-i0018 minus any HOLD; i0003/i0004 stay out until their price hold in
  HOLD-2026-07-29.md is cleared with source evidence). Note i0006/i0007 carry
  sail_months=year-round; if the month filter derives from sail_months, derive
  months from month_price_overrides until the registrar task below lands, so
  no empty months render. Then hand to qa-auditor - no status change toward
  live without a QA pass. (added 2026-07-29, by structure-guard)
  DONE 2026-07-29 (page-builder): visual-integration pass on the finder
  template (site design system: navy #0A2540 / teal #12919A / gold
  #FFB23E-#F0891F / coral #FF6B5A, Fraunces display + Inter UI via the
  newsite/base.py font-loading pattern; CSS values and fonts only, DOM/ids/
  classes/section order untouched; em dashes removed from all copy).
  generate.py months_of() now derives year-round months from
  month_price_overrides (fallback: next 6 months), so i0006/i0007 render only
  priced months. Baked to lp-system/out/preview/en/go/lines/royal-caribbean/
  from/galveston/index.html (38KB): noindex OK, GTM x2 + Clarity OK, dataLayer
  p002 line/port OK, tel_click POS + lead_submit/.cb + form_mode OK, 6 deal
  cards all stamped 2026-07-29, offer o002 live. FLAG FOR QA-AUDITOR: i0003
  (featured=yes) DOES render at $1391 despite HOLD-2026-07-29 - generate.py
  has no hold gate (notes carry no UNVERIFIED flag); i0004 not rendered (price
  outside top 6). qa-auditor decides i0003's fate before any deploy. Known
  placeholder blockers remain per T5 gate: #CALLBACK_ACTION, href="#" policy
  links, placeholder tracking phone. NOT marked live; awaiting QA.

- [x] [qa-auditor] AUDIT rebaked p002 against the Definition of Done before
  any status=live: noindex present; independent-service disclosure ribbon
  naming Royal Caribbean; date stamps current (date_checked=2026-07-29);
  >=3 deal cards rendered from publishable rows only; phone number slots
  filled (no +18885550142 or other placeholders, incl. #CALLBACK_ACTION and
  href="#" policy links per T5 gate); page weight budget; tracking checklist
  per tracking-guardian T1-T4 (tel_click positions resolve to
  topbar/callzone/deal-card/phoneband/sticky on primary CTAs incl. .itin and
  .noresults; .cb form present so lead_submit binds; lead_submit carries
  form_mode). Also verify i0003/i0004 price flags from HOLD-2026-07-29.md are
  respected. (added 2026-07-29, by structure-guard)
  DONE 2026-07-29 (qa-auditor): VERDICT = HOLD, full detail in
  HOLD-2026-07-29.md. validate.py exits 1 (4 flags: i0003/i0004 price swings,
  i0001/p001 Cape Liberty seed items outside this slice). Provenance
  re-verification: fresh royalcaribbean.com/graph re-query (departurePort:GAL,
  16 groups) compared against applied values; i0003 (+32%) and i0004 (+36%)
  CONFIRMED-AT-SOURCE to the dollar incl. all monthly overrides (cause: seeds
  priced a 2026 deployment that actually starts 2027-08); arbitration recorded
  in the HOLD file. One NEW mismatch: i0005 price_balcony $598/2026-09:b649 vs
  fresh 565.94 (source price drop after the 11:33 fetch) -> i0005 HOLD, sample
  doubled to all 16 rows (15/16 clean). Offer o002 verified fresh at
  /cruise-deals (title, dates, all 3 perks verbatim); --fix-offers auto-expiry
  path confirmed. Page DoD: 11 checks PASS (noindex, ribbon, §6a text present,
  stamps, 6 cards, phone count, sticky bar, 40KB, no em dashes, no
  sitemap/inbound links, tracking per guardian audit #3 PASS accepted) but
  page CANNOT ship: placeholder phone 1-833-555-0100 everywhere,
  action="#CALLBACK_ACTION" discards leads, href="#" policy links + unlinked
  TCPA consent line, "IMG SLOT"/raw asset: strings render, i0003 rendered
  while under an open hold (generate.py lacks a hold gate), and footer §6a
  "exclude taxes" contradicts taxes-included fares. Operator must supply:
  real tracking number, callback endpoint, Terms/Privacy/Consent pages.
  p002 stays status=building; no move toward live.

- [x] [page-builder] TRACKING DEFECT T6 (URGENT, blocks QA pass on p002 and
  every finder-family bake; found in tracking-guardian audit #2, proven by
  executing the baked script). generate.py builds the finder PAGE object as
  `page_obj = {"type": kind, "filter": rest, "h1": page["h1"]}` (line 322)
  and replaces the template's PAGE const, but the template's runSearch card
  renderer (finder-rci-from-galveston.html line 486; baked p002 line 669)
  reads `PAGE.lineLabel` and `PAGE.portLabel.split(',')[0]`. portLabel is
  undefined, so `.split` throws `TypeError: Cannot read properties of
  undefined (reading 'split')` inside runSearch's map. Consequences on the
  real bake: (1) itinGrid stays EMPTY - zero deal cards, zero deal-card
  tel: links, so the page's primary conversion CTA does not exist and
  tel_click position=deal-card can never fire; (2) resultCount still says
  "6 itineraries" (set before the throw) next to an empty grid; (3) the
  inline `onsubmit="runSearch(); return false;"` throws before `return
  false`, so submitting the finder does a native GET reload. Fix in the
  generator only: add lineLabel and portLabel (from the registry/deal rows,
  e.g. line_label/port_label) to page_obj - and audit page_obj against every
  `PAGE.` reference in the template family. Then rebake and re-run
  tracking-guardian + qa-auditor. Note: the tracking scripts themselves are
  in separate <script> blocks and survive the crash (delegated listener +
  lead_submit binding verified alive); this is a render defect that kills
  the tracked element, not the tracker. (added 2026-07-29, by
  tracking-guardian)
  VERIFIED FIXED 2026-07-29 (tracking-guardian, audit #3): rebaked PAGE now
  carries lineLabel "Royal Caribbean" + portLabel "Galveston TX" from the
  registries, with a hard ValueError in generate.py if either is missing.
  Full jsdom execution of the baked page: 6 cards render with tel links,
  finder re-search re-renders cleanly, no TypeError. 18/18 tracking
  simulation checks passed (incl. new DNI module and post-swap tel_click
  positions). T6 closed.

- [x] [page-builder] BUILD p007 PILOT itinerary detail page (operator ruling
  2026-07-29, ITINERARY DETAIL PAGES). Create the itinerary-detail template
  family + the generate.py branch for page_type=itinerary, then bake p007:
  url /en/go/itineraries/5-night-western-caribbean-from-galveston-mariner-of-the-seas/,
  h1 "5-Night Western Caribbean Cruise from Galveston on Mariner of the Seas",
  deal_filter itin:5n-west-caribbean-mariner-galveston (single row i0005,
  s016 Mariner of the Seas; day-by-day rows exist in 04_itinerary_days.csv;
  ports Costa Maya, Cozumel; 11 sailings Aug-Oct 2026). Requirements:
  noindex, never in sitemaps or main-site nav; call CTA primary; add the
  secondary "View full itinerary" CTA on the matching p002 finder card
  linking here; carry the T1-T6 generator fixes (POS map, .cb callback form,
  lineLabel/portLabel in PAGE object, form_mode); taxes_note on i0005 is
  taxes-INCLUDED, so the §6a footer variant issue from the p002 audit (item
  6 in HOLD-2026-07-29.md) applies here too. GATES: qa-auditor Definition of
  Done AND tracking-guardian audit both required before any status change
  toward live; qa-auditor must also formally arbitrate the i0005
  price_balcony hold entry in HOLD-2026-07-29.md (pricing-scout refreshed it
  2026-07-29, two independent fetches agree at $566, awaiting
  CONFIRMED-AT-SOURCE). Known operator blockers shared with p002: real
  tracking number, callback endpoint, policy/consent pages.
  (added 2026-07-29, by structure-guard)
  DONE 2026-07-29 (page-builder), together with the p002 completeness pass:
  (A) generate.py now resolves ALL images through 10_assets.csv only
  (status sourced/live + file present, else labeled frame; dest=caribbean
  falls back to the generic ship-at-sea card, no alias row invented),
  copies referenced files to {out_root}/img/lp/ and emits root-relative
  src with width/height from a built-in WebP header reader; finder cards
  gained route ribbons + sea-day counts from 04_itinerary_days, a
  Day-by-day <details> expander (05 blurbs first-occurrence-only,
  currency chips, sea days framed from the ship's 02_ships highlights
  linking #ships), a 4-ship module (02_ships facts), the Galveston
  pre-cruise know-panel tab (05 pre_cruise), a Documents line from q001's
  answer anchoring #faq, a baked FAQ section (page facets, max 4, q003
  first, q001 included per operator ruling), and the "View full
  itinerary" secondary link baked only when 09_pages registers a
  buildable itinerary page (today only i0005 -> p007's URL).
  (B) new lp-system/templates/lp/itinerary-detail.html (site design
  system, ITINERARY PAGE DATA contract) + generate.py branch
  (TEMPLATE_BY_TYPE itinerary -> itinerary-detail.html; combo keeps the
  finder); full day-by-day, ship section (registry strings only, honest
  no-venue framing), included-vs-extras strictly from taxes_note /
  private_island / 01_lines deposit+kids notes, month fare table
  (interior+balcony incl. bare-token override parsing, every fare
  stamped, ?when= highlights the month), slim no-nav header, call zone,
  why-call, sticky bar; dataLayer line/port/dest for itinerary URLs now
  derived from the row's page_targets; POS map extended with
  ['.fares','deal-card'] (fare table = the page's deal module,
  tracking-guardian to confirm). Baked p002 (71,278 B, 16 cards, hero +
  card images resolve, o002 live, Sail-to = Western Caribbean +
  Caribbean) and p007 (36,491 B, 6 day rows, 3 fare rows, hero $398
  stamped) - both jsdom-executed clean, zero em dashes, zero IMG SLOT /
  asset: strings, noindex, GTM x2 + Clarity, tel_click/lead_submit/DNI.
  NOT fixed (known blockers): placeholder phone / #CALLBACK_ACTION /
  href="#" policy links (T5 gate), and the §6a taxes-wording decision -
  both templates keep the canonical "exclude taxes" footer pending the
  operator's arbitration while every rendered fare carries its registry
  taxes-included note. FLAGS: q001's question is Bahamas-worded but
  renders on these Western Caribbean pages per the operator's q001
  ruling (registrar should generalize the wording or add a WC docs FAQ);
  i0005 balcony HOLD still awaits qa arbitration; o002 not on p007
  (banner_pages carries no itin key; exact-match kept). NOT marked
  toward live; awaiting tracking-guardian + qa-auditor below.

- [x] [tracking-guardian] AUDIT the rebaked p002 and the new p007
  (lp-system/out/preview/.../galveston/index.html and
  .../5-night-western-caribbean-from-galveston-mariner-of-the-seas/index.html).
  New since audit #3: POS map gained ['.fares','deal-card'] for the
  itinerary page's fare table (confirm or escalate as a contract change);
  itinerary dataLayer line/port/dest now derived from the itinerary row's
  page_targets (p007 must show royal-caribbean/galveston/western-caribbean);
  finder cards re-render with images, day expanders and a detailUrl link
  (verify post-render tel_click positions still resolve, incl. fare-row
  tel links on p007); detail template has a slim no-nav header, so its
  header CTA falls to position 'other' like the finder nav CTA
  (documented catch-all per T3). (added 2026-07-29, by page-builder)
  DONE 2026-07-29 (tracking-guardian, audit #4): BOTH PAGES TRACKING PASS
  at build level, zero new defects filed. p002: 24/24 jsdom checks (16
  cards render with tel links, i0005 "View full itinerary" link + day
  expanders + know-tabs + FAQ do NOT swallow or emit tel_click, delegated
  listener survives all interactions, DNI re-swaps after finder re-render
  and on the .noresults path, positions
  topbar/callzone/deal-card/phoneband/sticky/nav-'other' all correct,
  lead_submit form_mode=placeholder + distinct thank-you). p007: 21/21
  jsdom checks (dataLayer line/port/dest from i0005 page_targets confirmed
  royal-caribbean/galveston/western-caribbean; ?v=/?when= flow to
  lp_variant/lp_when; ?when=2026-09 highlights its fare row and its tel
  link swaps; DNI covers all 9 tel links incl. 3 fare rows; both fallback
  scenarios keep the real number; ship .btn and slim-header .cta fall to
  documented 'other'). RULING: ['.fares','deal-card'] CONFIRMED sound, not
  a contract change - the fare table is the itinerary page's deal module,
  its row CTAs are the exact analog of finder-card CTAs, and no existing
  contract value is misassigned ('.fares' is inert on finder pages, no
  such element). Caution recorded: '.fares' is section-scoped, so any
  future non-row tel link inside that section would also report deal-card.
  Fingerprints: p002 baseline superseded (drift fully explained: head
  dataLayer +dest key, POS +'.fares'; injected DNI/tel_click/lead_submit
  blocks byte-identical to audit #3 wording and to p007 modulo page_id);
  new p002 0f0bca99..., new p007 baseline 3ae6d12f..., recipe now written
  into tracking-fingerprints.txt for reproducibility. Carried blockers
  unchanged (T5 gate: placeholder phone incl. p007 meta description,
  #CALLBACK_ACTION, href="#" policy links) - qa-auditor's gate, not new.
  PENDING-LIVE-VERIFICATION: GTM container triggers for
  tel_click/lead_submit (container listens for main-site call_click today),
  Clarity recording, Ads conversion actions - see tracking-access.md.

- [x] [qa-auditor] AUDIT p002 (rebaked, now 16 cards with registry images)
  and p007 (new itinerary-detail pilot) against the Definition of Done.
  Known-open items carried over, NOT fixed by page-builder: placeholder
  tracking phone, action="#CALLBACK_ACTION", href="#" policy links +
  unlinked TCPA consent line, §6a footer "exclude taxes" wording vs the
  taxes-included fares (operator arbitration pending; note every rendered
  fare now carries the row's taxes_note inline). Also formally arbitrate
  the i0005 price_balcony entry in HOLD-2026-07-29.md (pricing-scout
  refreshed to $566, two fetches agree) - p007 renders that row. New
  checks worth adding: images resolve from /img/lp/ (5 files copied to
  the preview tree), alt text matches 10_assets.csv, q001 renders with
  its Bahamas wording on Western Caribbean pages (operator-ruled; flag to
  registrar for generalization), Liberty's class_or_note renders verbatim
  incl. its "(class not stated on official page)" honesty note.
  (added 2026-07-29, by page-builder)
  DONE 2026-07-29 (qa-auditor, re-gate audit): VERDICT = HOLD on BOTH pages;
  full detail appended to HOLD-2026-07-29.md ("p002 + p007 re-gate audit").
  i0005 arbitrated CONFIRMED-AT-SOURCE (third independent graph fetch this
  audit matched 398/566 + all overrides to the cent; hold cleared) and all
  16 Galveston groups re-compared fresh: 16/16 match baked p002 to the
  dollar. Structure passes: noindex, ribbon, stamps 0 days old, 16 cards /
  3 fare rows, images all resolve from 10_assets.csv with license notes and
  registry-verbatim honest alts, day-by-day = 04 rows verbatim, pre_cruise
  = 05 column verbatim (portofgalveston.com), q001 = cbp.gov, s017 honesty
  note verbatim, zero em dashes / IMG SLOT / asset: strings, weights 71KB /
  36KB, tracking per guardian audit #4 PASS. HOLD blockers: carried T5 trio
  (placeholder phone incl. BOTH meta descriptions, #CALLBACK_ACTION,
  href="#" policy links + unlinked TCPA); §6a taxes wording still open
  (note: p002 has NO inline taxes note - its only taxes statement is the
  wrong footer line); NEW p002 render defect i0009 shows $649 interior for
  Aug 2026 where source has NO Aug interior fare (month-fallback in
  priceFor, generator fix needed); NEW provenance: s001 Icon is
  status=seeded/no source yet renders ship facts on p002 (registrar must
  verify); NEW provenance: 01_lines deposit_note/kids_policy render on
  p007 with no source column in the schema (registrar); validate.py still
  exits 1 (i0001/p001 Cape Liberty items + it re-flags already-arbitrated
  i0003/i0004 each run). Minor registrar notes: 05 galveston asset_id
  a-ga-01 vs registry a-gal-01; generalize q001 wording + page_targets.
  Both pages stay status=building.

- [ ] [research-registrar] TARGETED COLLECTION for the Cape Liberty slice
  (combo:royal-caribbean-cape-liberty / p001's itinerary) ONLY. Same
  official-only method as the Galveston run: Pass A enumerate Royal Caribbean
  itineraries departing Cape Liberty NJ via royalcaribbean.com (whitelisted),
  Pass B verify ships, nights, destinations, sail months, source_url per row;
  replace/verify seed row i0001 (currently source=seed-example-VERIFY-BEFORE-
  PUBLISH, 0 publishable rows for p001). Do NOT touch other ports or lines.
  p001 is NOT being retired - it is a pilot registration awaiting this slice;
  pricing-scout Pass C follows. (added 2026-07-29, by structure-guard)

- [ ] [research-registrar] DATA FIX i0006 (and check i0007, same pattern):
  sail_months=year-round but the first sailing is 2026-10-31, so month-filter
  UIs would show empty months (Aug/Sep 2026). Replace year-round with the
  explicit YYYY-MM list from the source data (pkg LB05W648 has 70 sailings
  2026-10 to 2028-04; LB04W201 39 sailings 2026-11 to 2028-04). Registrar
  edits itinerary rows, not structure-guard. (added 2026-07-29, by
  structure-guard, from pricing-scout's note)

- [x] [page-builder] TRACKING DEFECT T1 (blocks QA pass on p002 and every
  combo/itinerary page). In lp-system/scripts/generate.py tracking_events()
  (the POS array, ~line 231), the position map covers .scard/.pcard but not
  the finder template's result cards, which use class .itin
  (finder-rci-from-galveston.html line 452; baked p002 line 472). Result:
  the page's PRIMARY conversion CTA reports position "other" instead of
  "deal-card". Add ['.itin','deal-card'] to POS, and also map the
  .noresults call button (finder line 437) to 'deal-card' or 'callzone'.
  Fix in the generator only, then rebake. (added 2026-07-29, by tracking-guardian)
  DONE 2026-07-29 (page-builder): POS now maps '.itin' and '.noresults' to
  'deal-card'; list reordered card-level selectors first (most-specific-first).
  Generator-only fix; verified in a rebaked p002 test file. Live rebake happens
  when structure-guard clears BLOCKED-ON-INVENTORY.

- [x] [page-builder] TRACKING DEFECT T2 (blocks QA pass on p002 and every
  combo/itinerary page). The finder template
  (lp-system/templates/lp/finder-rci-from-galveston.html) contains NO
  callback form: there is no .cb block, so the injected lead_submit handler
  (tracking_events(), selector '.cb form') null-guards out and lead_submit
  can NEVER fire on combo/itinerary pages. Either (a) add the call-gen
  templates' .cb callback module (see call-gen-line-royal-caribbean.html
  lines 221-233) to the finder template, or (b) get explicit operator
  sign-off that finder pages are tel-only and record that in the pages
  registry notes so the missing event is documented, not silent.
  (added 2026-07-29, by tracking-guardian)
  DONE 2026-07-29 (page-builder): took option (a). Finder template now carries
  the full call zone per ADS-LP-BRIEF §4: .callzone card with tap-to-call plus
  the 3-field .cb callback form (cbname/cbphone/cbwhen, action #CALLBACK_ACTION,
  .fp TCPA line), same structure/classes as the call-gen templates. All .cb CSS
  incl. mobile stacking already existed in the finder stylesheet; only CSS change
  was .callzone margin-top -52px -> 26px because the finder card holds the
  hero-overlap slot. Finder/search UI untouched; lead_submit handler now binds
  on finder bakes (verified in rebaked p002 test file).

- [x] [page-builder] TRACKING DEFECT T3 (medium, both template families).
  Tel links outside the mapped sections report position "other", which is
  outside the tel_click position contract
  (topbar|callzone|deal-card|phoneband|sticky): the nav CTA (finder line
  239 / call-gen line 190) and the in-content section CTAs (finder line
  315 "Ask a Galveston specialist"; call-gen line 269). Extend the POS map
  in generate.py tracking_events() so every static tel link resolves to a
  contract value (suggest ['.nav','topbar'] and a mapping for the content
  .btn links; if a new value like 'content' is preferred, the operator must
  approve the contract change first). (added 2026-07-29, by tracking-guardian)
  DONE 2026-07-29 (page-builder), per operator guidance: 'other' is an
  acceptable catch-all under the contract, so no contract change and no
  .nav/content mapping was added (either would need operator approval of a
  new value or would mislabel nav as topbar). Verified post-T1 on both
  families: primary CTAs all resolve (topbar/callzone/deal-card incl. .itin
  and .noresults/phoneband/sticky). Known remaining fall-throughs to
  'other', accepted and documented: (1) nav .cta, (2) the one in-content
  .btn per page (finder "Ask a Galveston specialist" / call-gen "Which ship
  fits us? Ask").

- [x] [page-builder] TRACKING DEFECT T4 (low, measurement integrity
  hardening). In generate.py tracking_events(), the callback-form submit
  handler treats a non-http action as SUCCESS: with the placeholder
  action="#CALLBACK_ACTION" it shows the thank-you state and pushes
  lead_submit while the lead data is discarded. qa-auditor's placeholder
  gate stops this shipping, but the handler should fail closed anyway:
  if action does not start with http, show the call-us error path and do
  NOT push lead_submit. A lead_submit event must always mean a lead was
  actually transmitted. (added 2026-07-29, by tracking-guardian)
  DONE 2026-07-29 (page-builder), with an operator-directed variation on
  the fix: instead of suppressing the event, every lead_submit now carries
  form_mode ('live' when the http POST succeeded, 'placeholder' when the
  action is a placeholder). Placeholder submits still show the thank-you
  state but are fully distinguishable in GTM, so test traffic can never be
  counted as a real lead, and the placeholder case stays visible rather
  than silent. qa-auditor's placeholder gate remains the shipping block.
  If tracking-guardian still requires strict fail-closed, flag for the
  operator to arbitrate.

- [x] [page-builder] TRACKING NOTE T5 (consent link, coordinate with
  qa-auditor's placeholder check, do not double-fix). The TCPA fine print
  on call-gen forms says "See our Calling & SMS Consent policy" but is
  plain text with no link, and the footer's Terms / Privacy / Calling &
  SMS Consent links are href="#" on both templates (finder line ~357 baked;
  call-gen line 319). Before any page goes live the consent policy must be
  a real linked page and the fine print should link to it directly.
  (added 2026-07-29, by tracking-guardian)
  ACKNOWLEDGED 2026-07-29 (page-builder), no code change per guidance:
  this stays covered by qa-auditor's placeholder gate, which blocks any
  page carrying href="#" policy links (or the unlinked consent mention)
  from going live. Note: the new .cb block added to the finder template
  for T2 intentionally mirrors the call-gen fine print, so it is caught
  by the same gate until real policy URLs exist.

- [ ] [manager/operator] RECOMMENDATION: keep the p002--harmony ad group
  ("harmony of the seas galveston", ~480/mo) PAUSED at launch. Officially
  verified 2026-07-29 (research-registrar): royalcaribbean.com/graph
  cruiseSearch ship:HM returns 23 bookable groups, every one departing
  Port Canaveral (2026-08-18 through 2028-04-15), zero from Galveston; the
  official Harmony ship page's server-rendered copy and sailing cards also
  show Port Canaveral only. Evidence with query details:
  lp-system/out/verification-2026-07-29.md. Same file documents that the
  reported Mariner 9/10-night from Galveston (MA09W208) has NO bookable
  sailings (its URL 307-redirects to /cruises; fleet-wide ship:MA shows
  Mariner leaving Galveston after 2026-10-26 for New Orleans/Europe), so
  the Galveston 9+ nights band correctly holds only i0016 (Liberty 9N) and
  i0018 (Symphony 10N one-way). (added 2026-07-29, by research-registrar)

- [x] [page-builder] BUILD p008 PILOT ship page (operator ruling 2026-07-29,
  SHIP PAGES). Create the ship template v2 family + the generate.py branch for
  page_type=ship, then bake p008: url /en/go/ships/mariner-of-the-seas/,
  h1 "Mariner of the Seas: Cruises, Cabins and What's Onboard",
  deal_filter ship:mariner-of-the-seas, status=building, priority 1.
  IMPLEMENTATION DECISION (structure-guard, 2026-07-29): the ship-page
  branch matches itineraries by ship_ids (s016) with the deal_filter
  recorded as declared intent; do NOT rely solely on a ship: key in
  page_targets (both i0005 and i0008 happen to carry
  ship:mariner-of-the-seas today, but ship_id is the canonical join).
  Publishable priced inventory: i0005 (5N Western Caribbean, from $398
  interior) and i0008 (4N Western Caribbean, from $459 interior), both
  date_checked 2026-07-29; hero from-fare comes from the cheapest
  publishable row (i0005). Ship facts: canonical dataset is
  newsite/data/ships/royal-caribbean.json (ships array, "Mariner of the
  Seas" entry with spec_source royalcaribbeanmedia.com fact sheet) - the
  single source shared with the live site's ship guides; LP-specific
  fields stay in 02_ships.csv s016 (status=verified). Carry all T1-T6
  generator fixes (POS map, .cb callback form, lineLabel/portLabel,
  form_mode); noindex, never in sitemaps or main-site nav; call CTA
  primary. GATES apply: tracking-guardian audit AND qa-auditor Definition
  of Done before any status change toward live; known operator blockers
  shared with p002/p007 (real tracking number, callback endpoint,
  policy/consent pages, §6a taxes wording) remain. NOTE: no 12_keyword_map
  rows point at p008 yet - 13_rc_keywords has no mariner+galveston keyword
  with volume (structure-guard evaluation 2026-07-29); parked mariner
  keywords stay parked until re-evaluation. (added 2026-07-29, by
  structure-guard)
  DONE 2026-07-29 (page-builder), master-enrichment pass, all in one run:
  (1) NEW lp-system/templates/lp/ship-detail.html (ship template v2) +
  generate.py branch (SHIP_RE block, TEMPLATE_BY_TYPE ship ->
  ship-detail.html, deals_for_ship joins itineraries by ship_id per the
  structure-guard decision, ship provenance gate = verified 02 row with
  official source AND newsite-dataset entry). Section order per operator
  spec: hero / call zone / included-vs-extras / at-a-glance / dining /
  cabins-in-advice-voice / written decks orientation / bars / nightlife /
  casino / activities / kids & teens / spa+shopping / where-she-sails-now
  (live sheet cards + our own SVG route schematic + "View full itinerary"
  -> p007) / FAQ / final band / sticky; inline call prompts after
  included, cabins, kids, sailings. Honesty contracts: casino null ->
  one honest line (never "Casino Royale"), quad_note renders with the
  registrar-internal "Internal cross-check" sentence stripped
  (public_note()), thin sections render small or hide, cabin advice is a
  category-nature whitelist keyed by category name.
  (2) generate.py ships-view loader: load_ship_dataset() reads
  newsite/data/ships/*.json keyed by slugified name; one dataset, no
  facts duplicated into CSVs; 02_ships keeps LP-only fields.
  (3) p007 photo-story rework (itinerary-detail.html): full-width hero
  with overlaid title + call CTA; day-by-day is now a visual journey
  (per-day -section images from 10_assets, port assets cycle for repeat
  visits so day 1 = Pleasure Pier / day 6 = Galveston beach, sea days
  rotate deck-scene/sea-day/ship-at-sea, adjacent days always differ,
  hero eager + everything below lazy); route schematic SVG above the
  journey; ship section is now condensed dataset tabs (at-a-glance /
  dining / family=kids_bands / nightlife) with themed tab images
  (dining/waterslide/lounge); alternating image left/right on desktop,
  full-bleed on mobile; callrow prompt after the journey.
  (4) p002 ship module is now tabs (Icon/Mariner/Liberty/Symphony) with
  dataset at-a-glance chips (year/guests/tonnage), verified dining
  counts, family line; ships missing from the dataset render 02 facts
  only (null-guarded ds).
  (5) ?when= extension on itinerary pages: accepts YYYY-MM or
  next-month; acts ONLY when the resolved month is in the baked
  WHEN_LINES whitelist (highlight row + "Your month" badge + whitelisted
  fares subheading + guarded scroll); H1 static; unknown values silently
  ignored; lp_when still carries the raw param.
  (6) TRACKING NOTE for tracking-guardian: the head dataLayer push now
  carries a `ship` key on EVERY lp page ("" on non-ship pages; p008
  pushes line=royal-caribbean, port="", dest="", ship=mariner-of-the-seas
  because a ship page's intent spans ports). This is deliberate head
  drift vs the audit-#4 fingerprints; tracking_events() is byte-identical
  to before. Ship-page POS: sailing cards use .scard (deal-card);
  the 4 inline callrow prompts + hero CTA fall to documented 'other'.
  (7) Bakes verified (116/116 jsdom + static checks): p002 75,891 B /
  p007 48,862 B / p008 52,547 B, all <150KB; noindex, GTM x2 + Clarity,
  zero em dashes / IMG SLOT / asset: strings; every baked image ref
  resolves and is copied to preview img/lp/ (p007 has 11 registry refs,
  max 8 in DOM at once, all files <=140KB); kids_bands ages render on
  p008 and in p007's family tab; ?when=next-month resolves to 2026-08 and
  highlights; finder re-search still clean post-tab-rework; o002 live on
  p002; fare stamps everywhere a price renders.
  NOT done / carried: operator blockers UNCHANGED (placeholder tracking
  phone, #CALLBACK_ACTION, href="#" policy links + unlinked TCPA, §6a
  taxes wording arbitration); p008 has no offer (o002 banner_pages has no
  ship: key, exact-match kept); no keywords point at p008 (parked per
  structure-guard); statuses stay building pending the gates below. NOT
  marked live; awaiting tracking-guardian + qa-auditor.

- [x] [tracking-guardian] AUDIT rebaked p002 + p007 and NEW p008
  (lp-system/out/preview/en/go/ships/mariner-of-the-seas/index.html).
  New since audit #4: dataLayer `ship` var on every page (contract
  addition, see page-builder note above; p002/p007 push ship:"");
  p007 fares module now consumes WHEN_LINES + ?when=next-month; p007 day
  expander markup replaced by the photo-story journey (verify delegated
  tel_click survives, positions unchanged); p002 ship grid replaced by
  tabs (verify tab clicks emit no tel_click and the #ships anchor still
  lands); p008 POS expectations: .scard sailing cards -> deal-card,
  callrow/hero CTAs -> documented 'other'. Fingerprints in
  tracking-fingerprints.txt need re-baselining for the head drift.
  (added 2026-07-29, by page-builder)
  DONE 2026-07-29 (tracking-guardian, audit #5): ALL THREE PAGES TRACKING
  PASS at build level, 72/72 jsdom checks (p002 25/25, p007 25/25, p008
  22/22), zero new defects filed. Head drift PROVEN to be exactly the
  documented `ship` key: recomputing the v1 fingerprint recipe on the new
  bakes with only that key removed reproduces the audit-#4 baselines
  byte-for-byte; injected DNI/tel_click/lead_submit blocks byte-identical
  across all three pages modulo page_id. Re-baselined p002/p007 + new
  p008 baseline in tracking-fingerprints.txt. RULING: `ship` dataLayer
  key ACCEPTED as a contract addition ("" on non-ship pages); p008's
  empty port/dest ACCEPTED as coherent (ship intent spans ports) - GTM
  operator instructions must add a `ship` Data Layer Variable and no
  Ads/GA4 mapping may assume port is non-empty (noted in
  tracking-access.md). Interactive surfaces clean: p002 ship tabs, p007
  journey/ship tabs/?when=next-month (resolves 2026-08 today, raw value
  still flows to lp_when; non-whitelisted values silently inert), p008
  FAQ/anchors/View-full-itinerary emit zero stray tel_click and the
  delegated listener survives everything. p008 DNI covers all 12 tel
  links (10 static incl. 4 callrow prompts + both sailing cards), both
  fallback paths keep the real number. Positions: .scard->deal-card;
  p008 hero/nav/callrows documented 'other'. Carried blockers unchanged
  (T5 gate: placeholder phone incl. all three meta descriptions,
  #CALLBACK_ACTION, href="#" policy links) - qa-auditor's gate, not new.
  PENDING-LIVE-VERIFICATION list unchanged plus one addition: GTM `ship`
  Data Layer Variable does not exist in the container yet.
  ADDENDUM same day: the post-audit CSS-only rebake of p007/p008 (mobile
  full-bleed fix, files now 48,884/52,569 B) was fingerprint-replayed and
  MATCHES the audit-#5 baselines byte-for-byte - no re-audit needed, not
  drift. Coordinator's live-browser ledger (GA4 G-JTQWHFMTB8 + Ads
  AW-18339104693 fire from GTM-NM78WCVF; "gtag is not defined" pageerror
  from a container tag - prime suspect for the main site's inactive
  website-call conversion) recorded in tracking-access.md.

- [x] [qa-auditor] AUDIT p008 (new ship pilot) + rebaked p002/p007
  against the Definition of Done. Ship-page specifics worth checking:
  casino line renders the honest gap (never an invented venue), cabins
  note has no "Internal cross-check" leakage and no berth-count claims,
  kids_bands ages match the dataset sources, dining split counts match
  exp.dining extra flags, every fare carries its stamp (hero, 2 sailing
  cards), sailings note carries the taxes-included wording, route
  schematic is our own SVG (no copied map). Carried blockers unchanged
  (T5 trio + §6a arbitration). (added 2026-07-29, by page-builder)
  DONE 2026-07-29 (qa-auditor, audit #6): VERDICT = HOLD on all three;
  full detail in HOLD-2026-07-29.md ("Master-enrichment gate audit").
  p008 passes ALL DoD structure + provenance checks (every ship fact
  traces to the newsite dataset / LP CSVs; casino honest line only;
  quad_note internal sentence stripped; kids/spa/shopping/cabins facts
  re-opened AT their official source pages and confirmed; own-SVG route
  schematics; stamps everywhere; 52.6KB). p007 photo-story passes (11/11
  images sourced+licensed, alts verbatim, 04/05 fidelity exact, ?when=
  whitelist + static H1, fares match source to the dollar) EXCEPT the
  costa-maya 05 row renders currency/blurb with an EMPTY source (page
  503s, could not verify at source). p002 rebake: i0009 Aug-fallback
  defect confirmed FIXED; minor safe-side month-derivation note filed.
  NEW price hold: i0008 2026-08:i590 is stale (fresh source 750.64;
  sample doubled, ALL 16 groups re-compared, 15/16 clean). Image weights
  all within budget; p007's 11th image (62.6KB deck-scene-card) ACCEPTED
  with reasoning. Standing operator blockers unchanged. No page moves
  toward live.

- [x] [pricing-scout] REFRESH i0008 (MA04GAL-597171001): 2026-08 interior
  override stored i590, fresh source shows USD 750.64 (qa audit #6 fetch,
  cached at lp-system/out/cache/2026-07-29/graph-departurePort-GAL-qa-audit6.json;
  the 11:33 fetch showed 590.14, so the source moved after collection).
  Mirror 'HOLD:' into the i0008 notes field until refreshed (process note
  10), refresh the override from a fresh pull, then hand to page-builder
  to rebake p002 and p008, then qa arbitration. All other i0008 values
  (Sep/Oct, balcony, default $459) re-verified to the dollar.
  (added 2026-07-29, by qa-auditor)
  RESOLVED 2026-07-29: pricing-scout 18:18:01 refetch applied
  (2026-08:i751, all else unchanged); qa-auditor ARBITRATED
  CONFIRMED-AT-SOURCE (scout refetch matches qa's independent audit-6
  fetch to the cent; cause documented: 08-13 sailing dropped its interior
  fare). Rebaked p002 verified to carry 751. See "Audit #6 arbitrations"
  in HOLD-2026-07-29.md. Sequencing note: rebake preceded arbitration,
  accepted once because the baked value was qa-corroborated.

- [x] [research-registrar] SOURCE the costa-maya 05_ports_content row: its
  currency (USD;MXN) and blurb render on p007 with an empty source cell
  (official royalcaribbean.com/cruise-to/costa-maya-mexico returned 503 at
  collection AND at qa audit #6 re-try). Re-fetch when the page loads and
  record source + retrieved_date; until then page-builder should suppress
  the costa-maya currency chips on itinerary bakes (facts may not render
  unsourced). (added 2026-07-29, by qa-auditor)
  RESOLVED 2026-07-29: registrar emptied currency+highlights, trimmed the
  blurb to the one itinerary-page-traceable fact, set the whitelisted
  i0005 official itinerary URL as source with an honest UNVERIFIED note
  (5 further 503 retries logged). qa-auditor verified the rebakes: p007
  and p008 bake costa-maya with cur:[] and EMPTY blurb (generator
  suppresses all content on UNVERIFIED rows - stricter than required).
  Hold cleared. FOLLOW-UP still open: re-source from the official
  cruise-to page next weekly pass when it loads.

- [ ] [manager/operator] FINAL GATE STATE (qa-auditor audit #6 re-gate,
  2026-07-29): p002, p007 and p008 are each
  APPROVE-PENDING-OPERATOR-INPUTS. Every non-operator check passes; the
  ONLY items between these pages and live are: (1) real tracking phone
  (placeholder 1-833-555-0100 everywhere incl. all 3 meta descriptions),
  (2) real callback endpoint (#CALLBACK_ACTION), (3) real Terms/Privacy/
  Calling & SMS Consent pages + TCPA fine-print link, (4) the §6a
  taxes-included wording ruling. Full verdicts in HOLD-2026-07-29.md.
  Once supplied, pages need a rebake with the real values and a final
  tracking-guardian + qa placeholder-gate pass ONLY (no content re-audit
  needed if data is unchanged). (added 2026-07-29, by qa-auditor)

- [ ] [page-builder] MINOR (non-blocking, with the next generator pass):
  months_of()/override parsing drops the interior-DEFAULT month from a
  card's month list when that month carries a balcony-only override token
  (i0009 Sep 2026 interior $649 and i0004 Oct 2027 interior $1850 are
  real, source-verified fares but not filterable on p002). Safe-side
  omission, never a wrong price, but inventory is under-shown for those
  month filters. (added 2026-07-29, by qa-auditor)

- [x] [page-builder] MOBILE UX REDESIGN PASS (operator ruling 2026-07-29), all
  three /go/ templates, presentation-only (<=900px; desktop layouts untouched;
  zero content/data changes; template footers left as placeholders for the
  shared legal partial swap).
  DONE 2026-07-29 (page-builder). What shipped per template:
  (1) itinerary-detail.html: day-by-day is a horizontal swipe slider on
  mobile (same DOM as the desktop journey, CSS reflows .journey to a
  scroll-snap flex row, one ~85vw slide + peek; stories hidden on slides);
  numbered day dots above the slider (active dot tracks scroll via a
  rAF-throttled scroll listener; dot tap scrolls, honoring reduced motion);
  the own-SVG route schematic reflows BELOW the slider (flex order, source
  order unchanged for desktop); every slide gets a "Tap for the full day"
  control AND whole-slide tap opening a bottom sheet (day story, times,
  currency chips, sea-day seaLine with the #ship anchor that closes the
  sheet and navigates). Ship section on mobile: when SHIP.tabs is baked the
  tab UI is replaced by a 4-tile slider (At a glance / Dining / Kids &
  family / Nightlife) opening sheets with the SAME baked facts; ships
  without a dataset entry keep the honest single panel unchanged.
  (2) finder-rci-from-galveston.html: result cards become compact rows on
  mobile (96px thumb left; name/ship/nights/from-price right; months as ONE
  scrolling chip row, full set now baked with .xtra/.morechip so desktop
  still shows 4+more); ribbon/expander/per-card tel CTA hidden on mobile,
  row tap opens the deal bottom sheet (route ribbon, per-month from-fares
  each derived via priceFor, stamp line, call CTA primary + View-full-
  itinerary secondary when detailUrl is baked). Featured strip: featured=yes
  rows render as a top slider of tappable mini-cards (same sheet); today
  that is i0003 only. Stamps preserved everywhere a price shows (row stamp
  kept, second clause hidden via .stamp-x; sheet and featured slide carry
  their own stamp text).
  (3) ship-detail.html: new mobile-only #shiplife section after At-a-glance
  with a tile slider (Dining / Kids & teens / Nightlife / Spa & shopping /
  Activities, as available per baked consts); the stacked #dining #bars
  #shows #activities #kids #wellness sections are display:none at <=900px
  and their full content renders in the tiles' bottom sheets (nightlife
  sheet = bars + shows incl. the honest no-lineup line; kids sheet keeps
  the third/fourth-guest live-question prompt from the hidden callrow).
  #casino, #decks, #cabins, #glance, #sailings stay as-is on mobile.
  CONSISTENCY CHOICE (per spec item 3): BOTH itinerary and ship templates
  use the same tile-slider + bottom-sheet pattern for ship-life on mobile
  (replacing tabs on itinerary, replacing stacked sections on ship).
  Shared implementation: one bottom-sheet dialog per page (slide-up 200ms,
  backdrop tap + visible X + swipe-down on the grab bar + Escape; footer
  ALWAYS carries a call CTA; in-sheet #anchors close then navigate; no
  stopPropagation anywhere); scroll reveals (fade + 14px rise, 220ms, IO,
  once-per-element then unobserve, section-level targets, hidden/display:
  none sections skipped) gated on a .js-rv root class so reduced-motion,
  no-IO and no-JS paths all render fully visible; all sliders are CSS
  scroll-snap only (scroll-snap-type:x mandatory, overflow-x:auto inside
  the full-bleed calc(50% - 50vw) container, no libs); slider/tile images
  loading=lazy; reading-text floor 16px on mobile (.lead, .story->sheets,
  .wcard p, .faq p, .inccard/.cabcard p); coral stays CTA-only (disclosure
  controls are outline/teal).
  TRACKING (for tracking-guardian ruling): generate.py POS gained
  ['.sheet-deal','deal-card'] - the finder row/featured-slide sheet is the
  deal card's mobile expansion, its call CTA the same conversion element.
  Ship-life ('sheet-life') and day-detail ('sheet-day') sheets are
  deliberately UNMAPPED -> documented 'other' (contextual prompts, analog
  of the callrow prompts ruled 'other' in audit #5). One additive baked
  field: finder itin objects now carry featured:true/false from the
  registry featured column (presentation only). Head dataLayer and
  DNI/tel_click/lead_submit blocks otherwise unchanged except the POS
  array (fingerprints need re-baselining for that one line).
  VERIFIED: 92/92 jsdom checks (sheets open/close via all four dismissal
  paths incl. timer fallback under reduced motion; row/slide/tile taps
  emit ZERO tel_click; sheet-deal CTA -> deal-card, day/life sheet CTAs ->
  'other', fare-row and .scard tel -> deal-card unchanged; finder
  re-render keeps delegation; desktop clicks inert; no duplicate IDs) plus
  35/35 + 3/3 real-Chrome checks (document scrollWidth EXACTLY 390 at
  390px on all three pages, with sheet open too; sliders overflow only
  internally; dots track scroll and dot-tap scrolls; reduced-motion
  contexts render 0 hidden sections and no .js-rv; below-fold sections
  reveal on scroll; first visible call CTA at 103px; sticky bar present;
  desktop shows no mobile-only UI, p007 journey stays grid).
  Weights: p002 89,044 B / p007 64,612 B / p008 64,331 B (<150KB). Phone
  only via PHONE slots (7/9/11 tel links). Zero em dashes. Carried
  operator blockers unchanged (T5 trio + §6a wording). NOT marked live;
  tracking-guardian + qa-auditor gates next.

- [x] [tracking-guardian] AUDIT the mobile-UX rebakes of p002/p007/p008:
  POS drift is exactly +['.sheet-deal','deal-card'] (rule on it); confirm
  sheet-day/sheet-life fall-through to 'other' is acceptable under the
  documented catch-all; re-baseline fingerprints; verify sheet DOM (fresh
  innerHTML per open) stays covered by the DNI MutationObserver and the
  delegated tel_click listener (page-builder's jsdom run says yes; the
  sheet call CTA is JS-rendered AFTER _googWcmGet may have swapped, the
  observer re-applies). (added 2026-07-29, by page-builder)
  DONE 2026-07-29 (tracking-guardian, audit #6): ALL THREE PAGES TRACKING
  PASS at build level, 84/84 independent jsdom checks (p002 36/36, p007
  26/26, p008 22/22), zero new defects filed. RULING 1:
  ['.sheet-deal','deal-card'] CONFIRMED sound, not a contract change -
  sheetOpen() sets the dialog's className to 'sheet off <kind>' fresh on
  every open (no kind leakage), so only the finder deal sheet ever
  matches, and that sheet IS the .itin/.fslide deal card's mobile
  expansion (same conversion element). Selector is inert on p007/p008
  (no sheet-deal kind there). RULING 2: sheet-day/sheet-life fall-through
  to 'other' ACCEPTED under the documented catch-all - their CTAs are
  contextual prompts, exact analog of the callrow prompts ruled 'other'
  in audit #5. MUTATIONOBSERVER PROOF: with a simulated _googWcmGet swap
  applied BEFORE opening, every freshly-rendered sheet (deal, day, life
  x5 on p008) had BOTH its foot CTA tel: href and its displayed number
  text re-swapped within one MO tick; fallback (Google returns nothing)
  keeps the real number in fresh sheet DOM too. Also verified: row/slide/
  tile/dot taps emit ZERO tel_click; zero stopPropagation calls in all
  three pages, delegation survives full sheet open/close cycles (X,
  backdrop, Escape, timer fallback = reduced-motion path); finder
  re-render + re-swap + row-tap-sheets still clean; positions regression
  green (topbar/callzone/deal-card incl. .itin/.fares/.scard/phoneband/
  sticky); lead_submit unaffected (fires once, form_mode=placeholder,
  thank-you state); shared-footer legal partial: /en/legal/ + TCPA
  fine-print links intercept nothing (0 dataLayer events), footer tel
  link -> documented 'other'; fingerprint drift PROVEN exactly the one
  POS line by replay (minus that line = audit-#5 hashes byte-for-byte),
  all three re-baselined in tracking-fingerprints.txt. NOTE (not a
  defect): p007/p008 tile handlers lack the isMobile guard, but
  .tiles{display:none} at base (visible only inside the <=900px media
  query) makes desktop taps unreachable; p002's featWrap [hidden] is
  removed by JS on all viewports but .featwrap{display:none} base rule
  hides it on desktop and row/slide taps are isMobile-guarded.
  PENDING-LIVE-VERIFICATION unchanged (GTM triggers, Clarity, Ads
  conversion actions - see tracking-access.md; touch/swipe-down dismissal
  and scroll-snap physics need real-browser confirmation, page-builder's
  Chrome run covers layout). Carried operator blockers unchanged
  (placeholder phone, #CALLBACK_ACTION; policy links are now real
  /en/legal/ URLs - the pages themselves must still exist at deploy).
  qa-auditor: my scope covered tracking only; peeking-slide affordance,
  horizontal overflow, sheet dismissibility UX and reduced-motion visuals
  remain yours.
  ADDENDUM same day (tracking-guardian): the qa-audit-#7 defect rebake
  (D1 legal links -> clean /en/legal/terms/ etc. directory URLs from the
  shared partial; D2 tiles 46vw->43vw) was fingerprint-replayed on all
  three fresh bakes: v1 hashes MATCH the audit-#6 baselines
  byte-for-byte - ZERO drift, exactly as the coordinator predicted
  (body/CSS only). Full jsdom suites re-run clean on the rebakes (36/36
  + 26/26 + 22/22; the new legal URLs were clicked and intercept
  nothing). No re-baseline needed; audit-#6 baselines remain current.

- [x] [qa-auditor] AUDIT the mobile-UX rebakes of p002/p007/p008 against the
  DoD. Mobile-specific checks worth adding: every price surface still
  carries a stamp (compact rows keep "From-fare seen <date>"; deal sheet
  and featured slide carry their own stamp lines); hidden-on-mobile
  desktop sections (#dining/#bars/#shows/#activities/#kids/#wellness on
  p008, card ribbons/expanders on p002) re-render their facts verbatim in
  the bottom sheets (content parity, no invention - all sheet copy is
  template-voice + baked consts); disclosure ribbon/callzone/TCPA
  untouched; reduced-motion renders everything visible; no horizontal
  page overflow at 390. Carried operator blockers (T5 trio + §6a) are
  unchanged and still gate live. (added 2026-07-29, by page-builder)
  DONE 2026-07-29 (qa-auditor, mobile-redesign gate audit #7): VERDICT =
  HOLD on all three, full detail in HOLD-2026-07-29.md ("Mobile-redesign
  gate audit"). PASSES: sheets dismissible via all four paths + 240ms
  timer fallback (verified in baked JS, all three pages); reduced-motion
  fully honored (scroll-behavior:auto, sheet transitions:none, .js-rv
  gated behind a matchMedia return, dot-tap scrollIntoView behavior:auto
  when reduced); sliders scroll inside their own full-bleed containers
  (overflow-x:auto within margin:0 calc(50% - 50vw); scrollWidth exactly
  390 cited from page-builder's real-Chrome run + coordinator captures);
  day-slider peek 26.5px and featured-slider peek 77.2px at 390px (both
  pass); content parity EXACT (sheets and hidden desktop sections render
  from the SAME baked consts; p007 SHIP.tabs = p008 dataset verbatim
  incl. dining 1-inc/4-extra split, kids_bands, nightlife honest
  no-lineup line; casino honest line stays visible on mobile in #casino
  and is NOT a sheet/venue anywhere); stamps preserved (compact rows keep
  "From-fare seen July 29" with only the second clause hidden; deal sheet
  + featured slides carry own stamp lines); sheet month fares derive via
  priceFor over the audit-6-safe month lists (i0008 Aug=751, i0009 no
  Aug/Sep 2026); every sheet footer carries a call CTA; 16px reading
  floor present on all three; footers byte-identical to
  newsite/legal_partial.py output incl. §6a on all three; TCPA fine
  print now LINKS the consent page; zero em dashes / IMG SLOT /
  [AGENCY NAME]; weights 89.0/64.6/64.3 KB; tracking cited per guardian
  audit #6 PASS (84/84). NEW DEFECTS (page-builder, not operator):
  (D1, all three) legal links emit /en/legal/*.html but BOTH the live
  site/ and newsite/dist serve directory URLs (/en/legal/terms/ +
  index.html; newsite clean_urls() rewrites, LP generator does not) -
  all four policy links AND the TCPA consent link 404 as baked;
  (D2, p007+p008) ship-life tile peek NOT inevitable at 390px: 46vw
  tiles give 20+179.4+12+179.4=390.8px, so tile 2 clips only 0.8px and
  tile 3 is fully off-screen (at >=414px there is zero clip at all) -
  tiles 3-5 are undiscoverable, narrow tiles to ~42-44vw or add an
  affordance, then re-prove in real Chrome. T5 item 3 DOWNGRADED per
  operator ruling: policy pages exist in site/ and newsite/dist; only
  D1's URL shape stands between the links and working targets. MINOR
  (non-blocking): coral appears on two non-CTA accents on p002 (.anchors
  a.on underline, .ribbon .dot.e end-dot - the ribbon renders inside the
  deal sheet too); touch swipe-down + scroll-snap physics still need
  real-device confirmation (synthetic-event coverage only). validate.py
  exit 1 with the SAME 4 pre-existing flags (i0003/i0004 arbitrated
  re-flags + i0001/p001 Cape Liberty seeds); no facts changed this run
  (presentation-only rebake), so no new price sample was due - the
  audit-6 16/16 source comparison from earlier today stands.
  UPDATE same day (qa-auditor, D1/D2 fix re-check): both audit-#7
  defects verified FIXED in the 21:13 rebakes. D1: all legal hrefs now
  clean directory URLs on all three pages (incl. TCPA fine-print link
  /en/legal/consent/), zero .html refs remain, footer re-verified
  byte-identical to the updated newsite/legal_partial.py output, targets
  exist in BOTH site/en/legal/<page>/index.html and newsite/dist. D2:
  .tile 43vw in both templates; independent 390px math (tile 167.7px,
  tile 3 peek 10.6px) matches the real-Chrome measurements; peek also
  present at 360/414/430px. Regression battery clean (0 em dashes, 0
  href="#", noindex, §6a, stamps July 29, sticky); validate.py same 4
  pre-existing flags; guardian fingerprint replay pending, zero drift
  expected (approval void if drift exceeds the two documented changes).
  FINAL VERDICTS: p002 / p007 / p008 all
  APPROVE-PENDING-OPERATOR-INPUTS. Remaining operator items (3): real
  tracking phone, real callback endpoint, §6a taxes wording. Full detail
  in HOLD-2026-07-29.md ("Audit #7 D1/D2 fix re-check").

- [x] research-registrar: source s001 (Icon of the Seas) and s002 rows in 02_ships.csv from official
      RC ship pages (currently status=seeded, no source, yet Icon facts render in p002's ship module).
      Same pass: add trailing source columns to 01_lines.csv RC row (deposit_note/kids_policy render
      on p007) from official RC booking/kids pages; generalize 08_faqs q001 wording + page_targets
      beyond Bahamas (non-blocking, qa-approved as accurate for closed-loop WHTI). Queued 2026-07-29
      by coordinator after qa re-gate.
      DONE 2026-07-29 (research-registrar): s001/s002 set status=verified with official ship-page
      sources (icon-of-the-seas, utopia-of-the-seas pages loaded and read; unverifiable seed
      highlights like "largest ship at sea" replaced with page-stated facts; class cross-checked to
      the official fact sheets already verified in newsite/data/ships/royal-caribbean.json).
      01_lines gained trailing source_deposit/source_kids columns; rci row rewritten to match the
      loaded official FAQ pages (deposit-requirements: $100/$250/$450/$500 tiers, Bermuda $250,
      suites 10%; final-payment-schedule-policy: 75/90/120 days; children-teen-activities: Adventure
      Ocean ages 3-17) - unverified seed claims (kids-sail-free, refundable-vs-non-refundable
      pricing) dropped; other lines' source cells left empty. q001 generalized to closed-loop
      wording (Bahamas kept as an example in the answer), page_targets widened with
      dest:western-caribbean and all; cbp.gov source retained. Same run: royalcaribbeanmedia.com
      added to source_whitelist.txt after first-party confirmation (302 to royalcaribbeangroup.com,
      which serves its own media from that domain), and Mariner exp enriched in the newsite ships
      dataset (kids_bands, spa=Vitality Spa, shopping, cabins from the loaded rooms/things-to-do/
      family-guide pages; casino recorded as an explicit null honest gap - no casino stated on any
      loaded official Mariner page).

- [x] [page-builder] MOBILE POLISH PASS (operator fix list from external audit,
  2026-07-29), all three /go/ templates + generate.py. Per-item results:
  (1) SHEET OPEN-BY-DEFAULT FIXED: .sheet.off/.sheetback.off now carry
  visibility:hidden + pointer-events:none with transition:visibility 0s .2s
  (hides after the slide-out; base state 0s so open shows immediately);
  verified computed visibility:hidden on load at BOTH 390 and 1440 in real
  Chrome, and elementFromPoint at the bottom edge resolves to sticky-cta /
  page content, never the sheet or backdrop.
  (2) p007/p008 header: <=480px shows brand + a 42px circular navy-outline
  phone ICON button (tel: link, aria-label "Call <display number>", cta-t
  text hidden, one row, wrap nowrap + brand ellipsis); desktop/tablet keep
  the text CTA. ALSO APPLIED TO p002: with the real brand baked the finder
  header had the identical two-line collision (screenshot-verified), same
  fix class; flag if the operator wants it reverted there.
  (3) p008 (and p007, same element) hero fareline amount+unit
  white-space:nowrap; "$398 pp" measured single-line at 390.
  (4) TOP STACK: disclosure ribbon collapses on mobile to ONE ellipsized
  line "Independent referral service, not the cruise line" + chevron
  (button, aria-expanded, tap toggles the FULL ribbon text which always
  stays in the DOM; collapse is JS-gated via .disclose.js so no-JS renders
  the full text - legally load-bearing path preserved). Callback form on
  ALL three call zones collapses behind a "Prefer we call you?" navy
  outline button (mobile only, .cb.js:not(.open) hides form+h3; same ids;
  lead_submit binding proven alive after expand in jsdom, form_mode
  placeholder). Plus mobile-only compaction to hit the budget: one-line
  hours badge at <=480 (markup split, "8am-11pm ET, every day" ALWAYS
  renders; only the "Advisors answering now" prefix hides), hero 260px on
  p002, tighter callzone/section/intro paddings, offerbar flex-wrap (o002
  was rendering 283px tall in a squeezed column). First content on load at
  390: p002 1652px, p007 1278px, p008 1330px (budget 1688).
  (5) p002 list: featured slider capped at 4 slides; rows are TRUE
  one-liners (44px thumb, truncated name, "N nts" chip, from-price; months
  chips, per-row stamp, per-row call CTA and taphint all removed from the
  row - stamp + months live in the deal sheet, which keeps its own
  "From-fares seen <date>" line). First 6 rows render, then "Show all 16
  sailings" navy outline button (count dynamic from the live result list,
  re-renders on every search). Row tap still opens the deal sheet. STAMP
  NOTE FOR QA: the row from-price is covered by the list-level stamp in
  the results head ("... seen July 29", visible on mobile) plus the sheet
  stamp; no per-row stamp text remains on mobile rows (operator-directed).
  (6) COLOR DISCIPLINE both viewports: coral now ONLY sticky bar, hero CTA
  (p007/p008), sheet-footer CTAs. Navy outline: callzone bigcall, nav cta,
  card .go (.itin/.scard), callrows, know-panel + noresults buttons,
  ship-panel button, fare CTAs; phoneband bigcall is WHITE outline on the
  navy band (judgment call: navy-on-navy is invisible; still not coral).
  .fares .call is a teal text link. Offer ribbon restyled soft gold tint
  (#FFF7EC + gold border, navy text). Non-CTA coral accents removed too:
  finder ribbon end-dot and route-SVG end dots now navy, anchors underline
  teal. Real-Chrome coral count per 844px band at 390: p002 [1,1,...],
  p007/p008 [2,1,...] (hero+sticky on screen 1) - all <=2.
  (7) NUMBER-DENSE: new generate.py deposit_struct() mechanically splits
  the 01_lines deposit_note into tier rows + final-payment rows + leftover
  prose (clause-split on "; "/". "; regex over the registry's own wording,
  nothing invented; unmatched notes fall back to full prose). RC note
  yields a 4-row "Deposit per person" table (1-5/6-9/10-14/15+ nights) +
  3-row "Final payment due" table + Bermuda/suites prose, rendered as
  .minitbl 2-col tables on p007 AND p008 deposits cards, all viewports.
  Checked remaining blocks: kids policy (ages 3-17 / 6-36 months) renders
  as separate list items, not prose - left as-is (ages, not fares); flag
  to qa if they want it tabled too.
  (8) p007 fare table mobile: month + ONE fare column via an
  Interior/Balcony segmented control (navy outline active state), per-row
  CTA column hidden, single navy-outline call CTA below the table INSIDE
  section.fares - POS CONFIRMED: '.fares' ancestor resolves it to
  deal-card (jsdom-proven), fare-row links unchanged deal-card. Desktop
  keeps the 4-col table, no seg/no single CTA.
  (9) p007 static route ribbon strip (#heroRoute routeline) REMOVED on
  both viewports incl. its CSS and the now-unused routeOf(); day slider +
  own-SVG schematic remain the route representations.
  (10) .kicker hidden at <=900px on all three (exception: the featured
  strip keeps its "Featured sailings" label - it is that slider's only
  caption; flag if unwanted).
  EXTRA (defect found while verifying item 6): the hero-overlap cards
  clipped the hero CTA/tagline on BOTH viewports (pre-existing, made
  prominent now that the hero CTA is a flagship coral surface). Mobile:
  overlap removed (.finder.wrap / .callzone margin-top positive; budget
  re-verified after). Desktop: hero content bottom raised above the
  overlap zone (80/84px) - the ONE intentional desktop-visible layout
  change beyond the stated color/table items.
  VERIFIED: 175/175 jsdom checks (sheet computed-hidden on load both
  contexts; open/close via X/backdrop/Escape/swipe + 240ms reduced-motion
  timer path on all three; lead_submit fires once after expanding the
  collapsed form; positions topbar/callzone/deal-card(.itin,.scard,.fares,
  .sheet-deal,#fareRows,fare-cta)/phoneband/sticky + documented 'other'
  for nav/hero/callrow/life-sheet; show-all expands + emits nothing;
  re-search resets; no duplicate IDs; zero em dashes) + 55/55 real-Chrome
  checks at 390x844 and 1440x900 (scrollWidth exactly 390 incl. with the
  sheet open; first-content budget; coral bands; one-row header; one-line
  fare; collapsed disclosure/cb expand correctly; 6-rows+show-all; 2-col
  fare table + toggle; kickers hidden; desktop layout intact with all
  mobile-only UI display:none). Screenshots in scratchpad
  (polish2-*-390/1440-top.png).
  Weights: p002 94,581 B / p007 72,297 B / p008 70,318 B (<150KB). Phone
  via PHONE slots only (10/14/13 tel links, incl. footer partial).
  TRACKING NOTE (guardian): ZERO expected fingerprint drift - head
  dataLayer, DNI, tel_click (POS array md5-identical across all three
  bakes and unchanged vs audit #6) and lead_submit blocks untouched;
  changes are template CSS/markup/module-JS + one generator data field
  (BOOKING/INCLUDED.deposit is now {rows,pay,prose} instead of a string).
  New interactive elements (disclose-sum, cb-toggle, showall, fareSeg) are
  buttons, not tel links, no stopPropagation anywhere, delegation
  re-verified. One caveat: the header icon button's aria-label carries the
  baked display number as an ATTRIBUTE; the DNI text-walker swaps text
  nodes only, so after a Google swap the aria-label still announces the
  canonical number while the href/text are swapped - decide if acceptable.
  QA NOTES: mobile rows carry no per-row stamp (see item 5 note);
  phoneband white-outline + featured-label kicker exceptions are judgment
  calls; hours badge prefix hidden <=480 but coverage hours always
  visible; carried operator blockers UNCHANGED (placeholder tracking
  phone, #CALLBACK_ACTION, section-6a taxes wording arbitration). NOT
  marked live; tracking-guardian + qa-auditor gates run next.
  (added 2026-07-29, by page-builder)

- [x] [tracking-guardian] AUDIT the mobile-polish rebakes of p002/p007/p008:
  replay fingerprints (zero drift expected - injected blocks byte-identical,
  POS unchanged); verify the new buttons (discloseSum, cbToggle, .showall,
  fareSeg segments) emit no tel_click and do not break delegation; confirm
  fare-cta -> deal-card via '.fares'; rule on the aria-label DNI caveat
  above. (added 2026-07-29, by page-builder)
  DONE (2026-07-30, tracking-guardian, audit #7): PASS all three pages.
  (1) Fingerprint replay: ZERO drift - v1 hashes byte-match audit-#6
  baselines (p002 f882ddf8, p007 d607192b, p008 c5fa7945); extracted
  blocks diff-identical; POS md5 4147b726... identical across pages.
  (2) 95/95 independent jsdom checks (scratchpad audit7.js +
  audit7-p008-sheet.js): discloseSum/cbToggle/showall/fareSeg all emit
  ZERO dataLayer events; lead_submit fires exactly once after
  expand+submit (form_mode placeholder, ids unchanged, binding on load);
  fare-cta -> deal-card via '.fares' independently re-proven by click
  through the delegated listener (fare-row links too); full disclosure
  text in static DOM pre-expansion, hiding gated on JS-added .disclose.js
  class (no-JS renders it fully); sheet off-state (.off
  visibility:hidden + pointer-events:none) holds, sheet contains no tel
  links while closed, fresh sheet DOM gets DNI href+text re-swap via
  MutationObserver and sheet CTAs fire tel_click (p002 sheet-deal ->
  deal-card, p007 sheet-day / p008 sheet-life -> documented 'other');
  restyled navy-outline CTAs all still tel: anchors, 1 tel_click per
  click, full position maps: p002 topbar1/callzone1/deal-card16/
  phoneband1/sticky1/other3, p007 ...deal-card4/other5, p008
  ...deal-card2/other7. DNI empty-response fallback keeps the real
  number. (3) Header phone icon (nav .cta, icon-only <=480): IS a tel:
  link, DNI swaps its href, click -> tel_click position 'other'
  (documented: .nav is not in POS; adding ['.nav','topbar'] would be
  real drift - defer, GTM can segment on 'other' + page scroll depth if
  needed). (4) ARIA CAVEAT RULED A DEFECT -> task T-ARIA-DNI below.
  Fingerprint baselines unchanged; expect documented DNI-block drift at
  the audit after T-ARIA-DNI lands.

- [x] [page-builder] T-ARIA-DNI (defect, filed by tracking-guardian audit
  #7; severity: pre-live REQUIRED, does not block template work): the nav
  header cta carries aria-label="Call 1-833-555-0100" (one occurrence per
  page, verified only stale-aria element). The DNI text-walker swaps text
  nodes only, so after a Google number swap a screen-reader user is
  announced the BASE number while href/visible text carry the forwarding
  number: (a) an SR user who reads the number aloud and dials it manually
  bypasses the forwarding number -> untracked website call on the PRIMARY
  conversion, (b) announced number contradicts every visible number on
  the page. FIX in generate.py DNI module applyAll(): after the href
  loop, add an attribute pass, e.g.
  var els=document.querySelectorAll('[aria-label*="'+REAL_DISPLAY+'"]');
  for(...){els[i].setAttribute('aria-label',
    els[i].getAttribute('aria-label').split(REAL_DISPLAY).join(swapped.f));}
  Keep it inside applyAll so the MutationObserver re-apply covers
  re-rendered elements. NOTE: this changes the DNI block -> fingerprint
  WILL move; tracking-guardian will verify and re-baseline as documented
  drift. (added 2026-07-30, by tracking-guardian)
  CLOSED (2026-07-30, tracking-guardian, audit #8): fix verified on the
  rebakes of all three pages. Drift vs audit-#6/#7 baselines PROVEN to be
  exactly the 7-line aria pass in applyAll and nothing else (reduction
  replay: stripping only that pass reproduces all three prior baselines
  byte-for-byte; identical insertion on p002/p007/p008). Behavior 15/15
  (audit8-aria.js): stale-aria=0 / swapped-aria=1 after simulated swap,
  aria matches href number, MutationObserver re-applies aria+href+text to
  injected fresh DOM, non-number aria-labels untouched, empty-Google
  fallback keeps the base number everywhere. Audit-#7 suite regression:
  89/89 still-valid checks pass on the rebakes. Fingerprints RE-BASELINED
  (audit #8 lines in tracking-fingerprints.txt): p002 bec631ef, p007
  664f0270, p008 9a45c5e0. NOTE FOR QA-AUDITOR: T-ARIA-DNI is no longer a
  live-gate blocker; tracking gate is a clean PASS. Remaining live-gate
  blockers are the carried operator items only (placeholder tracking
  phone, #CALLBACK_ACTION, section-6a wording) + GTM-side setup per
  tracking-access.md (PENDING-LIVE-VERIFICATION).

- [x] [qa-auditor] AUDIT the mobile-polish rebakes against the DoD. New
  checks worth adding: sheet computed-hidden on load (both viewports);
  full disclosure text reachable on mobile (tap-to-expand + no-JS path);
  deposits mini-table values verbatim vs 01_lines deposit_note (4 tiers +
  3 final-payment rows + Bermuda/suites prose); p002 mobile row stamp
  coverage decision (list-level stamp + sheet stamp, no per-row stamp);
  fare table mobile shows exactly one fare column per toggle state, every
  visible fare still stamped; coral discipline both viewports; carried
  operator blockers unchanged. (added 2026-07-29, by page-builder)
  DONE (2026-07-30, qa-auditor, audit #9 = mobile-polish FINAL GATE; full
  evidence in HOLD-2026-07-30.md): VERDICT = APPROVE-PENDING-OPERATOR-
  INPUTS on p002, p007 AND p008. All six brief sections pass on the 00:23
  bakes (the exact files guardian re-baselined in audit #8): (1) sheet
  hidden on load PASS - .off carries visibility:hidden + pointer-events:
  none on sheet AND backdrop on all three, mechanism audited (base
  display:flex means .off, not [hidden], does the hiding; backdrop's
  hidden attr holds because no author display rule overrides it);
  coordinator computed-style captures cited. (2) 2-screens budget PASS -
  method sound (real Chrome 390x844, 1652/1278/1330 vs 1688), p008
  structurally corroborated (~527px fixed pre-content stack). (3) coral
  PASS - tokens consumed by .btn only; every .btn mapped to ancestors:
  coral survives only sticky/hero-CTA/sheet-foot; phoneband white-outline
  + gold offer tint ACCEPTED. (4) polish items PASS incl. p002 header-icon
  extension ACCEPTED, deposits tables cell-by-cell verbatim vs 01_lines
  (one accepted normalization: "due X days out" -> "X days before
  sailing"), fare table mode-i/-b shows exactly one stamped fare column
  per state, route ribbon gone, kickers hidden (featwrap exception
  accepted). STAMP-COVERAGE RULED: ACCEPTED - list-level "seen July 29"
  results-head line (visible on mobile, re-renders per search) + sheet
  sstamp + all 16 rows sharing date_checked 2026-07-29 satisfy the
  every-price-stamped rule; CONDITION filed as note N1: generate.py's
  single newest-date pricesCheckedOn const would overstate freshness on a
  future mixed-date bake - move to per-row stamps or fail on divergence.
  (5) standard sweep clean (zero em dashes/banned strings/inbound links;
  noindex; §6a present; phone >=5; <150KB); validate.py exit 1 with 6
  flags, ALL pre-existing or date-rollover artifacts of arbitrated rows
  (verbatim in HOLD file). (6) aria fix verified in all three baked DNI
  applyAll blocks; nav cta is the only phone-bearing aria-label; guardian
  audit #8 CLEAN PASS cited (drift = exactly the aria pass, re-baselined).
  Live remains blocked SOLELY by the three operator items: real tracking
  number, real callback endpoint, §6a taxes-wording ruling (+ GTM-side
  setup per tracking-access.md at go-live).

- [x] [tracking-guardian] AUDIT #9 (build-time) of the operator design batch
  + bugfix rebakes of p002 / p007 / p008 (files: lp-system/out/preview/en/go/
  lines/royal-caribbean/from/galveston/, .../itineraries/5-night-western-
  caribbean-from-galveston-mariner-of-the-seas/, .../ships/mariner-of-the-
  seas/, bakes of 2026-07-30 10:01-10:28). Coordinator-made changes recorded
  here for the record: (1) top disclosure bar REMOVED, compact .ind-note
  disclosure moved into the call zone, full legal blocks retained in footer,
  disclose collapse JS module deleted; (2) main-site logo lockup (inline SVG
  from newsite/logo.py) replaces the text brand in the slim header, with a
  BRAND_CSS head block, deliberately NOT a link; (3) NEW generator-injected
  NAV_UI_JS before </body>: back-to-top button (scroll-toggled, fixed, z-66)
  + conditional header Back button (history.back, referrer/history gated),
  both <button>; (4) p002 ship-tab + finder imagery, "Representative image"
  note, ddpulse CSS animation on day-by-day controls; (5) bugfixes - .ribbon
  horizontal scroll with fixed-size ports/legs, mobile deal sheet regained a
  full day-by-day list via new daysHTML()+dayLine(), .pname max-width
  78->120px; (6) phoneband h2 colour fix + 9 internal-language strings
  rewritten to guest-facing copy.
  VERDICT: CLEAN PASS on ALL THREE PAGES. Tracking gate = PASS.
  DRIFT: ZERO, exactly as predicted. v1 recipe (head dataLayer+GTM+Clarity
  line, GTM noscript iframe, injected DNI/tel_click/lead_submit block)
  replayed on the fresh bakes reproduces the audit-#8 baselines BYTE-FOR-
  BYTE: p002 bec631ef..., p007 664f0270..., p008 9a45c5e0... The extracted
  blocks are diff-IDENTICAL to the audit-#8 extractions (zero differing
  bytes), so this is not just a hash collision at the recipe level.
  BEHAVIOUR: 141/141 independent jsdom checks (scratchpad audit9.js) plus a
  15/15 regression of the audit-#8 aria suite. Specifically proven:
  - C1 disclosure removal is CLEAN: zero .disclose/#disclose elements, zero
    JS references to them (no orphaned querySelector/getElementById, so no
    null-guard failure and no TypeError that could kill later scripts - the
    known pitfall #1 in CLAUDE.md); .ind-note present in the call zone;
    footer still carries the full What-we-are / Trademarks / Pricing blocks
    and the /en/legal/consent/ link (2 consent links per page: form + footer).
  - C2 lockup is a <span>, not an <a>; no exit link added to a paid LP; the
    SVG is aria-hidden and carries no phone number, so it neither adds a
    tel_click surface nor interferes with the DNI aria pass.
  - C3 NAV_UI_JS is TRACKING-INERT and byte-identical on all three pages
    (sha256 1073db9f..., recorded as a supplemental fingerprint). The block
    contains no dataLayer / gtag / clarity / _googWcmGet / tel_click /
    lead_submit reference, no tel:, no createElement('a'), no href
    assignment. Runtime: backtop click emits ZERO dataLayer events (and
    still scrolls to top); scroll past 800px toggles .show with ZERO events;
    goback click emits ZERO events and calls history.back() exactly once.
    Neither control is matched by the delegated tel_click listener (both are
    <button>, neither is inside an a[href^="tel:"]). Inserting goback as
    firstChild of .nav .wrap breaks nothing: the brand lockup and the header
    tel CTA both survive, and the header CTA still fires exactly one
    tel_click (position 'other', the documented catch-all) in both the
    goback-present and goback-absent builds. Z-order verified from the baked
    CSS: backtop z-66 < sheetback z-80 < sheet z-81, so the button can never
    sit over an open sheet or its backdrop; it is also above the nav (z-60)
    but fixed bottom-right, and its bottom:88px clears the ~67px sticky-cta
    (z-70) so it does NOT cover the sticky call button (geometry check;
    PENDING-LIVE-VERIFICATION in a real browser at 360/390px).
  - C5b the sheet's new day list carries ZERO tel links on p002. Every
    anchor inside .sdays is an in-page #hash link (the at-sea "See the ship"
    link), and clicking one emits ZERO events. Sheet tracking is UNCHANGED:
    the sheet foot CTA is still DNI-swapped by the MutationObserver on fresh
    DOM and still maps to position deal-card via ['.sheet-deal','deal-card'].
    Ribbon still renders inside the sheet; .ribbon overflow-x:auto with
    flex:0 0 auto ports/legs and .pname max-width:120px confirmed in CSS.
  - DNI unchanged and healthy on all three: every tel: href swapped, all
    displayed text swapped, aria-label pass holds (0 stale / 1 swapped,
    matching the href number), MutationObserver re-applies href+text+aria to
    injected fresh DOM, and the empty-Google fallback keeps the real number
    in href+text+aria. The new backtop aria-label ("Back to top") and goback
    aria-label are correctly left untouched by the number pass.
  - lead_submit intact after the collapsed-form expand: cbToggle expands
    with ZERO events, submit fires exactly ONE lead_submit
    (form_mode:'placeholder') and renders the distinct thank-you state, on
    all three pages.
  - Positions unchanged: topbar/callzone/deal-card/phoneband/sticky all
    present on all three (p002 13 links, p007 13, p008 13; 'other' counts
    are the documented catch-alls: header CTA, footer tel, hero/nav/callrow
    prompts, day/life-sheet CTAs).
  - Container/consent/index checks: GTM-NM78WCVF (the live site's container,
    imported from newsite/config.py) + noscript iframe, Clarity xpb1uyu7ta
    loaded directly (site's method), noindex,nofollow present, consent link
    present and not conflicting with any tag.
  FINGERPRINTS: audit-#8 baselines REMAIN CURRENT (no re-baseline needed).
  NEW supplemental fingerprint added to tracking-fingerprints.txt covering
  the NAV_UI_JS block (invisible to the v1 recipe by design) plus a
  dataLayer-surface census invariant (6 script blocks / 3 dataLayer-touching
  / 3 push sites / exactly 2 event names) so a future silent measurement
  surface in a non-tracking block cannot slip past drift detection.
  OBSERVATION FOR THE OPERATOR (not a defect, no code filed): the header
  Back button renders when `document.referrer` is same-origin OR
  `history.length > 1`. On a paid click that lands from a Google SERP in the
  same tab, history.length is typically 2, so the button will render and
  history.back() will send the visitor back to the ad/SERP - an exit control
  in the header of a paid landing page, and one we have no measurement on
  (adding an event would be new measurement, which needs operator approval).
  jsdom cannot exercise history.length (always 1 there), so this is
  PENDING-LIVE-VERIFICATION. Recommend the operator either restrict the
  condition to the same-origin referrer clause only, or accept it knowingly.
  MINOR CLEANUP (cosmetic, non-blocking, not filed as a defect task): ~6
  dead .disclose / .disclose-sum CSS rules remain in the baked <style> now
  that the element and its JS are gone. Harmless; page-builder can drop them
  in the next generator touch. (added 2026-07-30, by tracking-guardian)

- [x] [qa-auditor] FINAL GATE (audit #10) on the operator design batch +
  bugfixes, all three /go/ pages (bakes of 2026-07-30 11:08 — note these are
  the rebakes made AFTER tracking-guardian audit #9, which covered the
  10:01-10:28 files).
  DONE 2026-07-30 (qa-auditor, audit #10): VERDICT = **HOLD on p002, p007 AND
  p008**. Full evidence in HOLD-2026-07-30.md ("Operator design batch +
  bugfix gate ... audit #10").
  THREE BLOCKERS:
  (D-A, all three) The `.ind-note` independent-service disclosure naming
  Royal Caribbean has **ZERO unobstructed visible pixels on initial load** at
  360/390/430 x 844 on every page (scanline elementFromPoint test in real
  Chromium; the opaque fixed `.sticky-cta` at z-70 starts at y=745/770).
  p002 390px: note 951-991. p007: 799-839. p008: 841-881. Also below the
  fold on desktop p002 at 1440x900. Above the fold instead: the RC brand
  eyebrow, an RC-branded H1, a phone number, and on p007/p008 a "$398 pp"
  fare with a coral call CTA. The removed top ribbon was the first element
  on the page; this is not an equivalent. Placement/wording/DOM are all
  correct, it is simply ~100-210px too low. Fix = raise it above the
  call-zone CTA stack and re-prove zero-scroll visibility at 360/390/430.
  (D-B, p008 rendering, p007 latent) The copy rewrite universalised
  source-scoped gaps into claims about Royal Caribbean's publishing
  practices, and TWO ARE FALSE at their own official whitelisted page. I
  opened https://www.royalcaribbean.com/cruise-ships/mariner-of-the-seas/deck-plans
  today (HTTP 200): it publishes Deck 02 through Deck 15 for this ship,
  refuting "Royal Caribbean publishes venue lists rather than a deck-by-deck
  map"; and it publishes "Casino Royale(SM)" as a Mariner venue with
  descriptive copy and imagery, refuting "Royal Caribbean does not publish
  casino details for Mariner of the Seas". Two more of the same shape are
  unsourced ("does not publish a fixed lineup" on p008; "does not itemize
  evening venues" latent on p007). Our own registry note is honestly scoped
  ("no casino venue is stated on any loaded official Mariner page ... left
  null rather than assumed") and does not support any of them. Fix
  direction: keep the guest-facing register but make the sentence about US,
  not about them, e.g. "We do not have a verified casino listing for this
  ship, so we do not guess. Ask on the call." Never state what a cruise line
  does or does not publish.
  (D-C, p008) Only 2 deal rows render (`.scard` x2; only i0005 and i0008
  carry ship_id s016). DoD requires >=3. Audits #6/#9 recorded this as
  passing; not carried forward. Needs more verified Mariner inventory
  (registrar) or an explicit recorded waiver of the threshold for ship-type
  pages (structure-guard/operator).
  PASSES: validate.py exit 1 with the SAME 6 pre-existing/rollover flags
  (verbatim in the HOLD file); no data CSV touched since 2026-07-29 18:22 so
  zero fact rows changed and no 10% sample was due. I re-ran the v1
  fingerprint recipe MYSELF on the 11:08 bakes because guardian audited the
  10:01-10:28 ones: hashes MATCH the audit-#8 baselines byte-for-byte
  (bec631ef / 664f0270 / 9a45c5e0) and the dataLayer-surface census holds
  (6 blocks / 3 dataLayer / 3 pushes / 2 event names) — the Back-button fix
  did not touch the tracking blocks. **NAV_UI_JS supplemental fingerprint
  MOVED 1073db9f -> 7918ce7a (identical on all three); tracking-guardian must
  re-baseline it.** Back button re-verified in real Chromium over HTTP:
  ABSENT on direct landing (history.length=2, the exact case the old
  condition failed), ABSENT with referer google.com, ABSENT on self-referrer
  and on a look-alike host, PRESENT only with a same-origin referrer, and a
  real p002->p007 click then Back returns to p002; brand lockup + header tel
  CTA survive, scrollWidth stays 390. RULING: the header exit control is
  ACCEPTABLE under this gate (cannot reach the SERP, is a <button> so no
  crawlable exit / no tel_click surface, and with zero main-site inbound
  links the destination is always another LP). Recommended one-line
  hardening: require the referrer path to start with /en/go/ as well.
  Also passing: logo lockup is a SPAN not an <a> (aria-hidden SVG + visible
  brand text, no new exit); 32/32 image refs resolve, all `status=sourced`
  with license notes and registry-VERBATIM alts, 8 distinct assets across 16
  finder cards with zero adjacent repeats, zero broken images; ddpulse is
  box-shadow-only, 3 iterations, reduced-motion guarded; ZERO `disclose`
  occurrences anywhere (no orphaned DOM ref, pitfall #1 clear); ribbon
  overflow-x:auto with `.pname` 120px and 0 overlaps / 0 clipped labels
  across all sheets; sheet day-by-day restored at EXACT parity with the
  desktop expander (7/6/6/5 rows, same strings); phoneband h2 white on navy;
  no dialog visible on load; 2-screens budget 1198/1046/1088 vs 1688; coral
  max 2 per band; scrollWidth exactly 390/1440; noindex; no sitemap; zero
  inbound /go/ links; footer legal blocks byte-identical to
  newsite/legal_partial.py incl. section 6a; TCPA links /en/legal/consent/;
  weights 100.5/75.1/72.6 KB; zero banned placeholder strings; every fare
  stamped "seen July 29" (1 day old).
  NON-BLOCKING, fix in the same rebake: N-1 drop "Official photography
  coming." (implies a cruise-line relationship); N-2 one em dash survives in
  the NAV_UI_JS comment (p002 L2446 / p007 L1047 / p008 L1107); N-3
  `.ind-note` contrast 4.33:1 vs WCAG AA 4.5:1 (and `.repnote` 2.90:1) —
  darken the compliance disclosure; N-4 back-to-top `bottom:88px` is clipped
  11px by the 99px sticky bar at 390px, raise to ~110px; N-5 the
  coordinator's "no internal-sourcing language" sweep claim is NOT accurate
  (three source-register strings still render; the "class not stated on
  official page" one is the audit-#6-approved honesty note and must be
  KEPT); N-6 extend the representative-image note to p008's generic hero and
  p007's ship tabs; N-8 o002 is `status=draft` and expires 2026-07-31
  (self-expiry verified); N-9 `gtag is not defined` pageerror fires on all
  three pages from the live GTM container — must be fixed before spend or a
  tel_click may never reach an Ads conversion; N-10 p002 shows the number as
  visible text only 4x at 390px (23 tel links).
  N-7 REQUIRED PRE-DEPLOY: I re-queried royalcaribbean.com/graph today and
  3/3 spot-checked rows moved within 24h — i0005 balcony $566 -> $703.87
  (+24%, renders on all three pages), i0009 i649/b806 -> 679.47/848.97,
  i0008 defaults still exact but its Aug/Sep overrides could not be verified
  at source (those sailings are gone from the package). Stamps are honest at
  1 day old, so nothing published is wrong today, but this inventory
  reprices overnight: a pricing-scout refresh is required ON THE DAY OF
  DEPLOY, immediately before the shipping bake.
  OPERATOR INPUTS (3 carried + 2 new): real tracking phone; real callback
  endpoint; section-6a taxes wording; NEW ruling on the p008 >=3-deal-rows
  threshold (D-C); NEW decision on the Back-button gate hardening. Plus
  GTM-side setup per tracking-access.md incl. the gtag container error.
  No page moves toward live.

- [ ] [page-builder] FIX D-A (BLOCKING, all three /go/ templates): the
  `.ind-note` independent-service disclosure must be visible above the fold
  without scrolling. Today it has ZERO unobstructed pixels at 360/390/430 x
  844 on all three pages (see HOLD-2026-07-30.md audit #10 for the
  per-viewport table and method). Move it above the call-zone CTA stack (or
  attach it to the hero eyebrow) and re-prove with a scanline
  elementFromPoint measurement at 360/390/430, accounting for the fixed
  99px sticky bar. Do NOT reintroduce the top ribbon (operator ruling
  2026-07-30) — the requirement is above-the-fold visibility, not a ribbon.
  While in there: N-3 darken `.ind-note` from #6B7C86 to at least 4.5:1 on
  white. (added 2026-07-30, by qa-auditor)

- [ ] [page-builder] FIX D-B (BLOCKING, ship + itinerary templates): remove
  every generator string that asserts what Royal Caribbean does or does not
  publish. Four strings: p008 `#decksTxt` ("publishes venue lists rather
  than a deck-by-deck map" — FALSE, their deck-plans page publishes Deck 02
  to Deck 15 for this ship), p008 `#casinoTxt` ("does not publish casino
  details for Mariner of the Seas" — FALSE, the same page publishes Casino
  Royale for Mariner with copy and imagery), p008 `#showsBody` ("does not
  publish a fixed lineup"), and the p007 night-tab fallback ("does not
  itemize evening venues for this ship"). Replace with self-scoped
  guest-facing wording that still discloses the gap and routes to the call,
  e.g. "We do not have a verified casino listing for this ship, so we do not
  guess. Ask on the call." Same run: N-1 drop "Official photography coming."
  from the repnote; N-2 remove the em dash from the NAV_UI_JS comment; N-4
  raise `.backtop` to ~bottom:110px; N-6 extend the representative-image
  note to p008's hero and p007's ship tabs. (added 2026-07-30, by qa-auditor)

- [ ] [tracking-guardian] RE-BASELINE the NAV_UI_JS supplemental fingerprint:
  it moved 1073db9f... -> 7918ce7a... in the 11:08 rebake (identical on all
  three pages) because the coordinator changed the Back-button gate to
  same-origin-referrer-only AFTER your audit #9. I verified the v1 tracking
  hashes still match the audit-#8 baselines byte-for-byte and that the block
  is still tracking-inert, and I ran the runtime gating matrix (see audit
  #10 in HOLD-2026-07-30.md), but the baseline line in
  tracking-fingerprints.txt is yours to update. Also please rule on N-9: the
  `gtag is not defined` pageerror from container GTM-NM78WCVF now reproduces
  on all three LP bakes. (added 2026-07-30, by qa-auditor)

- [ ] [structure-guard/operator] RULE ON D-C: p008 renders only 2 deal rows
  (i0005, i0008 — the only rows carrying ship_id s016) against a DoD
  threshold of >=3. Either queue research-registrar for further verified
  Mariner inventory (her Galveston deployment ends 2026-10-26, but a ship
  page is not port-scoped, so later New Orleans / Europe sailings count), or
  record an explicit written waiver of the >=3 threshold for ship-type
  pages. Until one exists p008 fails this DoD line. (added 2026-07-30, by
  qa-auditor)

- [ ] [pricing-scout] REQUIRED PRE-DEPLOY REFRESH (not due now, due on the
  day these pages ship): my audit-#10 re-query of royalcaribbean.com/graph
  (departurePort:GAL, 2026-07-30) shows this inventory repricing overnight —
  i0005 balcony $566 -> $703.87 (+24%; i0005 renders on p002, p007 AND
  p008), i0009 i649/b806 -> 679.47/848.97, and i0008's 2026-08/2026-09
  overriding sailings have left the package entirely (could not verify at
  source). Stamps are honest today at 1 day old, so no action is needed for
  a non-live preview, but do NOT treat the 10-day stamp window as tolerance
  here: refresh immediately before the bake that goes live. (added
  2026-07-30, by qa-auditor)

- [x] [qa-auditor] RE-GATE the audit-#10 fix rebakes (2026-07-30 12:40/12:43).
  DONE 2026-07-30 (qa-auditor, audit #10 fix re-gate; full evidence in
  HOLD-2026-07-30.md "Audit #10 fix re-gate"): **p002 and p008
  APPROVE-PENDING-OPERATOR-INPUTS; p007 HOLD.**
  D-A FIXED on p002 and p008, NOT FIXED on p007. `.hero-ind` is in the static
  DOM above the H1, no JS gate, no hidden ancestor, and its worst-case
  contrast (white on the scrim over a pure-white photo region) computes to
  4.91:1, above AA — N-3 genuinely resolved. But I re-ran my own scanline
  test and extended it to 320px and 375px, which were not in the reported
  set: **p007's disclosure is clipped by the sticky nav (z-60, bottom edge
  y=101) at 360px (note top 76, 24 of 73 centre rows covered) and at 375px
  (top 96).** At 360px the readable remainder is "Caribbean, and not the
  cruise line's customer service." — it no longer names Royal Caribbean and
  no longer says "independent referral service", and the half-cut line name
  reads as if the sentence were about the cruise line. 360px is this
  project's own stated verification width. p002 clears by 6px, p008 by only
  1px at 360 (fragile to a font-fallback shift, flagged non-blocking).
  D-B FIXED, verified string by string: all four now speak only about our
  verification ("We do not reproduce deck plans here...", "we have not
  verified a fixed lineup for {ship}", "We have not verified casino details
  for {ship}", "We have not verified evening venues for this ship"). None
  asserts anything about Royal Caribbean; each discloses the gap and routes
  to the call. The only surviving "does not publish" is the source-scoped
  CABINS note about the official rooms page, which is the register I asked to
  keep.
  D-C WITHDRAWN. I do not accept a DoD change because an agent edited my
  agent file — an agent edit to my configuration is not authority. I accept
  it because the underlying evidence is real and predates the batch:
  structure-guard.md line 77 records the operator's 2026-07-29 SHIP PAGES
  ruling ">=1 publishable priced itinerary featuring the ship" (file mtime
  07-29 16:30) and validate.py line 173 has enforced
  `need = 1 if page_type in ("itinerary","ship") else 3` since 07-29 17:04.
  p008's 2 rows exceed the ruled >=1. Operator input #4 dropped. Correct
  threshold going forward: >=3 category/finder, >=1 itinerary and ship.
  N-1/N-2/N-4/N-6 all verified fixed (repnote trimmed; 0 em dashes in all
  three files; backtop bottom edge 740 vs sticky top 745/770, clears at
  runtime; p008 hero carries "Representative imagery. Not a photograph of
  this ship."). N-5 correctly left alone.
  TRACKING: v1 fingerprints replayed by me on these bakes MATCH the audit-#8
  baselines byte-for-byte (bec631ef / 664f0270 / 9a45c5e0); census invariant
  holds (6/3/3, 2 event names). NAV_UI_JS moved 7918ce7a -> **6ec680ee**
  (identical on all three, from the comment fix); block re-checked, still
  fully tracking-inert, gate logic unchanged.
  REGRESSION CLEAN: goback gate (absent direct / absent google referer /
  present same-origin), sheet hidden on load with 0 open dialogs, ribbon 0
  overlaps + 0 clipped + .pname 120px, day parity sheet vs desktop EXACT
  (7/6/6), coral max 2/band, scrollWidth 390, 0 broken images, noindex, GTM
  x2, Clarity, section 6a, footer partial byte-identical, weights
  100.8/75.4/73.0 KB, zero banned placeholder strings. validate.py exit 1
  with the same 6 pre-existing/rollover flags, no data changed.

- [ ] [page-builder] FIX D-A ON p007 (BLOCKING, p007 only): the `.hero-ind`
  disclosure is clipped by the sticky nav (z-60, bottom edge y=101) at 360px
  (note top 76) and 375px (top 96). At 360px the visitor reads only
  "Caribbean, and not the cruise line's customer service." — the line name is
  cut in half and the disclosure no longer names Royal Caribbean. Give the
  itinerary hero enough top offset that `.hero-ind` always starts below the
  101px nav, then re-run the scanline elementFromPoint test at
  320/360/375/390/430 x 844 (not just 390/430 — that width set is what let
  this through). Same run: raise p008's 1px clearance at 360px (note top 102
  vs nav bottom 101) so it survives a font-fallback metric shift, and sweep
  the now-dead `.ind-note` CSS rule from all three `<style>` blocks.
  p002 and p008 are otherwise cleared. (added 2026-07-30, by qa-auditor)

- [ ] [tracking-guardian] RE-BASELINE NAV_UI_JS again: 7918ce7a -> 6ec680ee
  (identical on all three pages) from the audit-#10 comment fix. v1 tracking
  hashes still match the audit-#8 baselines byte-for-byte and I re-verified
  the block is tracking-inert with the same-origin gate unchanged, but the
  baseline line is yours. Supersedes the earlier re-baseline request.
  (added 2026-07-30, by qa-auditor)

- [x] [qa-auditor] RE-GATE the hero-height CSS fix (rebakes 2026-07-30 13:16).
  DONE 2026-07-30 (qa-auditor, final re-gate; full evidence in
  HOLD-2026-07-30.md "Hero-height CSS fix re-gate"): **ALL THREE PAGES
  APPROVE-PENDING-OPERATOR-INPUTS.**
  D-A FIXED on all three. I re-ran my own scanline elementFromPoint test at
  **12 viewports, not the 7 reported** (added 320x568, 344x882 Fold cover,
  360x640, 393x873 Pixel, 412x915, 1024x768): **36/36 PASS** — zero occluded
  points, zero occluded by the nav, full element height in the viewport, and
  the complete sentence (both "Independent referral service" and "Royal
  Caribbean") present in every case. Clearance below the nav bottom edge
  25px (p007 @430) to 246px (p002 @360), matching the reported range
  independently. p008's fragile 1px clearance at 360 is now 81px. Visual
  confirmation of the exact audit-#11 failure case at
  scratchpad/qa12-p007-360x844.png: the clipped fragment is gone.
  METHOD NOTE: my first pass reported 1 occluded point out of 165-365 in
  every single case. I probed instead of filing it — the sample was always
  `box.right-4` on the first/last scanline row against fractional box edges
  (e.g. top 176.484), returning the note's own parent DIV.wrap. Sub-pixel
  sampling artifact in my harness; NAV.nav / A.cta / SPAN.brand-txt (the
  elements behind the real audit-#11 failures) appear nowhere. With a 2px
  edge inset: 0/350 occluded everywhere.
  p002 and p008 RE-VERIFIED FROM SCRATCH, not carried forward on the earlier
  approval, because this CSS touched all three templates. The real risk was
  the taller hero eating the two-screens budget: re-measured at 1410/1348
  (p002 360/390), 1118/1056 (p007), 1140/1078 (p008) vs the 1688 budget —
  all pass, but the margin narrowed ~150-210px and the worst case (p002 @360)
  now has 278px of headroom. **Re-run the 12-viewport scanline check AND the
  budget after any future change that adds vertical space above the fold.**
  Also re-verified: sheet hidden on load with 0 dialogs, coral max 2/band,
  backtop clears the sticky bar, scrollWidth exactly 360/390, 0 broken
  images, 0 duplicate IDs, day-by-day parity sheet vs desktop EXACT
  (7/7,6/6,6/6), ribbon 0 overlaps / 0 clipped / .pname 120px, goback gate
  unchanged (absent direct, absent google referer, present same-origin),
  noindex / GTM x2 / Clarity / section 6a / 2 consent links / sticky bar,
  zero em dashes / href="#" / [AGENCY NAME] / IMG SLOT / +18885550142,
  footer byte-identical to newsite/legal_partial.py, weights 100.9/75.5/75.3
  KB, zero "Royal Caribbean does not publish/itemize" strings anywhere
  (D-B stays fixed), dead .ind-note CSS rule now gone from all three.
  TRACKING: v1 fingerprints replayed on the 13:16 bakes MATCH the audit-#8
  baselines byte-for-byte (bec631ef / 664f0270 / 9a45c5e0); NAV_UI_JS
  unchanged at 6ec680ee (CSS-only, as stated); census invariant holds.
  validate.py exit 1 with the same 6 pre-existing/rollover flags, no data
  changed. No page moves toward live: 3 operator inputs remain.

- [ ] [manager/operator] FINAL GATE STATE (qa-auditor final re-gate,
  2026-07-30): p002, p007 and p008 are each
  APPROVE-PENDING-OPERATOR-INPUTS. Every non-operator check passes on all
  three: DoD, provenance, imagery, honesty framing, mobile standing checks,
  tracking. The ONLY items between these pages and live are:
  (1) real tracking phone number (placeholder 1-833-555-0100 everywhere incl.
      all three meta descriptions and the DNI REAL_DISPLAY constant),
  (2) real callback endpoint (action="#CALLBACK_ACTION", x2 per page),
  (3) the section 6a taxes-included wording ruling.
  STANDING DEPLOY-DAY GATES (not operator decisions): pricing-scout refresh
  on the day of deploy (my 2026-07-30 source re-query showed i0005 balcony
  $566 -> $703.87 inside 24 hours; this inventory reprices overnight and the
  10-day stamp window is NOT tolerance here); resolve the `gtag is not
  defined` container error before spend or a tel_click may never reach an Ads
  conversion; GTM setup per tracking-access.md; tracking-guardian re-baseline
  of NAV_UI_JS at 6ec680ee. Once the three inputs are supplied, the pages
  need a rebake with the real values plus a tracking-guardian pass and a qa
  placeholder-gate pass ONLY — no content re-audit needed if data is
  unchanged. (added 2026-07-30, by qa-auditor)
