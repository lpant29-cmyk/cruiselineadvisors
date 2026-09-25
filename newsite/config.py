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

# Royal Caribbean University "Master of Adventure", completed 2026-09-23 by a
# named individual. Sits in the PERSONAL TRAINING section, never the company
# credential section, and never without the non-affiliation line beside it.
# This one is more sensitive than the others: it carries a cruise line's own
# wordmark on a site that bids that line's brand keywords and states in its
# footer that it is not an agent of any cruise line. RCU is Royal Caribbean's
# training programme for travel professionals and completing it is a training
# achievement, NOT a partnership, appointment, endorsement or authorised-agent
# status. If the wording beside this badge ever drifts toward implying any of
# those, remove the badge rather than reword around it.
RCU_ACCOLADE = True
RCU_HOLDER   = "Lokesh Pant"
RCU_BADGE    = "/badges/rcu-master-of-adventure.png"
RCU_DOC      = "/docs/rcu-master-of-adventure-certificate.jpg"

# ── Specialist certifications, held by named INDIVIDUALS ────────────────────
# Rendered in the footer's personal-training slider, never the company block.
# Order matters: the first three are what shows before scrolling, so the
# cruise-relevant ones lead on a cruise site.
#   img  badge logo under assets/badges/ (None renders a text chip instead)
#   doc  the certificate itself under assets/docs/ (None = display-only, no link)
# A cert with no doc must never be made clickable to a DIFFERENT cert's
# document; offering the wrong thing as proof is worse than offering none.
#
# DELIBERATELY EXCLUDED: "Princess Hotels & Resorts Weddings Specialist".
# It is a hotel brand, but on a cruise site it sits beside our Princess
# Cruises line pages and would be read as a Princess Cruises credential,
# which we do not hold. It stays on bargainairticket where it is unambiguous.
SPECIALIST_CERTS = [
    {"key": "bahamas",  "img": "/badges/bahamas-specialist.png",
     "doc": "/docs/bahamas-specialist-diploma.png",
     "en": "Certified Bahamas Specialist", "es": "Especialista Certificado de las Bahamas"},
    {"key": "rcu",      "img": "/badges/rcu-master-of-adventure.png",
     "doc": "/docs/rcu-master-of-adventure-certificate.jpg",
     "en": "Royal Caribbean University Master of Adventure",
     "es": "Master of Adventure de Royal Caribbean University"},
    {"key": "romance",  "img": "/badges/romance.png", "doc": None,
     "en": "Bahamas Romance Specialist", "es": "Especialista en Romance de las Bahamas"},
    {"key": "iata",     "img": "/badges/iata-foundation.png",
     "doc": "/docs/iata-foundation-diploma.jpg",
     "en": "IATA Foundation in Travel and Tourism",
     "es": "IATA Foundation en Viajes y Turismo"},
    {"key": "domrep",   "img": "/badges/dominican-republic-specialist.png",
     "doc": "/docs/dominican-republic-specialist-certificate.pdf",
     "en": "Dominican Republic Specialist", "es": "Especialista de República Dominicana"},
    {"key": "xcaret",   "img": "/badges/xcaret-xpert.png",
     "doc": "/docs/xcaret-xpert-certificate.jpg",
     "en": "Xcaret Xpert", "es": "Xcaret Xpert"},
    {"key": "majestic", "img": None,
     "doc": "/docs/majestic-resorts-certificate.jpg",
     "en": "Majestic Resorts Specialist", "es": "Especialista de Majestic Resorts"},
]

# Bahamas Romance Specialist badge. Display-only logo in the footer credential
# row; renders ONLY when the image file is actually present on disk.
ROMANCE_SPECIALIST = True
ROMANCE_BADGE      = "/badges/romance.png"

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
