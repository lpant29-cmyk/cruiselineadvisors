# -*- coding: utf-8 -*-
"""
SINGLE SOURCE OF TRUTH for site-wide constants.
Change any of these in ONE place and it updates across every generated page.

Phone number lives here and ONLY here, swap PHONE_DISPLAY + PHONE_HREF once
when the real Render/tracking number is ready.
"""

# ── Contact (change in one place) ──────────────────────────────────────────
PHONE_DISPLAY = "+1-833-684-4250"     # real toll-free number (shown with a "Toll Free" label)
PHONE_HREF    = "+18336844250"        # tel: form, digits only, leading +

# ── Brand / identity ───────────────────────────────────────────────────────
BRAND      = "CruiseLine Advisors"
SITE_URL   = "https://cruiselineadvisors.com"
SINCE_YEAR = 2015

# Legal entity (differs from the brand). NOTE: the LLC name contains "cheapest", a banned
# marketing term, so build.py exempts this exact string from the guard (it's a proper noun).
COMPANY       = "BookMeCheapest LLC"
COMPANY_ADDR  = "6501 Arlington Expressway #2177, Jacksonville, FL 32211, United States"
PRIVACY_EMAIL = "privacy@cruiselineadvisors.com"  # TODO: confirm this inbox exists

# ── Operator credentials (2026-09-17) ───────────────────────────────────────
# These belong to the OPERATING ENTITY (COMPANY above), not to the CruiseLine
# Advisors referral service, and must be presented that way. Mirrored from the
# same company's bargainairticket.com, where they already run. Real, verifiable
# registrations, never decoration: if either lapses, remove it the same day.
# ASTA_MEMBER has no public member number, so we make no numeric claim.
ASTA_MEMBER     = True
ASTA_URL        = "https://www.asta.org/content/Membership/public-member-directory.aspx"
FSOT_REF        = "ST150081"          # Florida Seller of Travel, held by COMPANY
FSOT_URL        = "/docs/fl-seller-of-travel.pdf"

# Certified Bahamas Specialist, held by a principal of COMPANY (confirmed by the
# operator 2026-09-18). Scoped to the entity for the same reason as the two
# above: we have no in-house travel advisors, so this must never read as "our
# specialists". ONE diploma is on file, so the claim stays singular; if a second
# person certifies, that is when plural wording becomes supportable.
# The crest and the diploma link render ONLY when both files are actually
# present on disk. The sentence stands on its own without them.
BAHAMAS_SPECIALIST = True
BAHAMAS_CREST      = "/badges/bahamas-specialist.png"          # crest cropped from the diploma
BAHAMAS_DOC        = "/docs/bahamas-specialist-diploma.png"    # the full diploma, self-hosted

# ── Coverage hours (NEVER "24/7", Hard Rule 6) ────────────────────────────
HOURS = {
    "en": "8am-11pm ET, every day",
    "es": "8am-11pm ET, todos los días",
}

# ── Analytics & tag management ─────────────────────────────────────────────
# Paste the IDs from each Google/Microsoft property here (account: gocaribbea@gmail.com).
# Each snippet renders on EVERY page only when its ID is filled in; leave "" to disable.
# Recommended path: use GTM alone and add GA4 + Clarity as tags INSIDE GTM (then leave
# GA4_ID / CLARITY_ID blank here). Set them here only if you'd rather hard-code them.
GTM_ID     = "GTM-NM78WCVF"   # Google Tag Manager container (gocaribbea@gmail.com). GA4 is fired
                              # INSIDE this container, so GA4_ID stays blank to avoid double-counting.
GA4_ID     = ""               # INTENTIONALLY BLANK, GA4 is managed via GTM, never a separate gtag.js.
CLARITY_ID = "xpb1uyu7ta"     # Microsoft Clarity project (account: helpdesk@bargainairticket)
# Google Search Console: verify by DNS TXT or by the HTML-tag method, paste the token here
# and it renders a <meta name="google-site-verification"> on every page.
GSC_VERIFICATION = "riSdvugiyK2ysSxGBWNBloIRKzeSaYWfwZHUQgZF2d4"  # Search Console HTML-tag method; do NOT remove (Google re-checks)

# ── Languages ──────────────────────────────────────────────────────────────
LANGS        = ["en", "es"]
DEFAULT_LANG = "en"

# Derived
IS_PLACEHOLDER_PHONE = (PHONE_HREF == "+18885550142")
