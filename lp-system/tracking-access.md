# Tracking Access Requests

Maintained by tracking-guardian. Nothing here is granted until the operator
says so and records it. I never create containers, properties, or conversion
actions myself; until access exists I output click-through instructions.

Last updated: 2026-07-30 (audit #9, operator design batch + bugfixes: NO
scope change - no new dataLayer keys, event names, position values, or POS
selectors; zero drift in the tracking blocks, audit-#8 baselines still
current. The batch's new NAV_UI_JS block, back-to-top + header Back button,
is tracking-INERT by design and needs NO GTM work. Audit #8, the aria-label
DNI fix, likewise needed no GTM change. Earlier ledger: audit #6 POS
selector ['.sheet-deal','deal-card']; audit #5 + coordinator's real-browser
diagnostics; no access granted since audit #1, all four requests still open)

OPERATOR CONFIRMATION NEEDED (threshold discrepancy, raised 2026-07-30):
the primary website-call conversion is recorded in two places with two
different call-length thresholds - "calls from website, 30s+" in the
conversion-architecture ruling and "calls 60s+" in the weekly plumbing
checklist below. The threshold lives in the Google Ads conversion action
settings, not on the page, so no page change is implied either way, but the
number must be settled BEFORE the conversion action is created, because
changing it later resets the conversion history. Guardian will not pick one.

## LIVE CONTAINER EVIDENCE (coordinator Playwright run, 2026-07-29)

First live observation of GTM-NM78WCVF's contents, from loading the p008
preview in a real browser. This SUPERSEDES the "presumed absent /
unverified" status on two items below:

- The container ALREADY FIRES a GA4 config tag: property **G-JTQWHFMTB8**
  (page_view observed on the LP preview).
- The container ALREADY FIRES a Google Ads tag: **AW-18339104693**
  (plus doubleclick ccm collect).
- PAGEERROR observed on the LP preview: **"gtag is not defined"** - some
  tag in the container calls gtag() directly. Neither the LPs nor the main
  site define gtag (intentionally no gtag.js; GA4 fires via GTM), so that
  tag crashes on every page. PRIME SUSPECT for the main site's inactive
  website-call conversion, matching the standing diagnostic note: if the
  website-call conversion snippet lives in that (likely Custom HTML) tag,
  it dies on the missing gtag stub before _googWcmGet is ever defined.
  OPERATOR DECISION NEEDED: locate the offending tag in GTM and either
  (a) convert it to a proper GTM tag template, or (b) have pages define a
  gtag stub. I do not edit pages or the container; recording only.
- Still UNVERIFIED (needs container read access): whether any trigger
  matches `tel_click`/`lead_submit`, and which trigger/settings the
  observed GA4 + Ads tags use.

Same ledger item: post-audit-#5 rebake of p007/p008 was a mobile
full-bleed CSS fix only; v1 fingerprint replay on the rebaked files
matches the audit-#5 baselines byte-for-byte (verified 2026-07-29, same
day, not deferred). No drift.

Note for GTM request #1 (scope grew again with audit #5): the head dataLayer
now also pushes `dest` (audit #4) and `ship` (audit #5) on every LP page, so
the click-through instructions must include Data Layer Variables for BOTH.
On ship pages (p008) `port` and `dest` are intentionally "" - a ship page's
intent spans ports - so no GA4/Ads mapping may assume `port` is non-empty;
segment by `page_type` + whichever facet is set.

Note for GTM request #1 (scope grew with the conversion-architecture ruling):
publish access is now also needed to (a) deploy the "Google Ads Calls from
Website Conversion" tag on /go/ pages - this tag is what defines
window._googWcmGet; the page's DNI callback polls for it up to 20s and falls
back to the real number until the tag exists (verified graceful) - and
(b) add the Conversion Linker tag on all pages. Until granted, both go in
the click-through instructions.

| # | System | Access needed | Why | Status |
|---|--------|---------------|-----|--------|
| 1 | Google Tag Manager, container GTM-NM78WCVF (account: gocaribbea@gmail.com) | Publish access | Create Data Layer Variables (page_id, page_type, lp_variant, lp_when, line, port, position), Custom Event triggers for `tel_click` and `lead_submit`, and map them to GA4 + Google Ads tags. The container's existing triggers listen for the main site's `call_click` event; LP pages emit `tel_click`/`lead_submit`, so today those events reach the dataLayer and STOP THERE. Until granted, I supply exact step-by-step GTM instructions for the operator. | REQUESTED, not granted |
| 2 | GA4 property **G-JTQWHFMTB8** (identified 2026-07-29 by live observation: it fires from GTM-NM78WCVF on LP preview pages; GA4_ID intentionally blank in newsite/config.py) | Viewer access | Verify `tel_click`/`lead_submit` events arrive in GA4 reports/DebugView after GTM wiring. | REQUESTED, not granted |
| 3 | Google Ads API (account behind tag **AW-18339104693**, identified 2026-07-29 by live observation) | Read access (shareable with campaign-manager's future token) | Verify conversion actions exist and record; detect the spent-but-zero-conversions-and-zero-events broken-measurement pattern. | REQUESTED, not granted |
| 4 | Microsoft Clarity, project xpb1uyu7ta (account: helpdesk@bargainairticket) | Project access | Confirm /go/ page sessions are actually recording (Clarity loads direct on-page, matching the main site's method, but recording is only provable in the dashboard). | REQUESTED, not granted |

## Cannot-verify-without-access (explicit)

- ~~Whether GTM-NM78WCVF contains a GA4 config tag and a Google Ads tag
  that fire on /go/ pages~~ RESOLVED 2026-07-29 by live observation: BOTH
  fire (GA4 G-JTQWHFMTB8 page_view + Ads AW-18339104693) - see LIVE
  CONTAINER EVIDENCE above. Their triggers/settings remain UNVERIFIED.
- Whether any trigger in the container matches `tel_click` or `lead_submit`:
  UNVERIFIED, and presumed ABSENT because the main site uses the event name
  `call_click` (newsite/base.py trackCall).
- Which container tag calls gtag() directly (source of the observed
  "gtag is not defined" pageerror): UNVERIFIED without container read
  access; behavior observed, cause not yet located.
- Whether Clarity records /go/ sessions: UNVERIFIED.
- Whether Google Ads conversion actions (calls 60s+ primary, lead_submit
  secondary, tel_click observational) exist: UNVERIFIED.
