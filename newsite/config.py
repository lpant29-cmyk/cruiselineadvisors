# -*- coding: utf-8 -*-
"""
SINGLE SOURCE OF TRUTH for site-wide constants.
Change any of these in ONE place and it updates across every generated page.

Phone number lives here and ONLY here, swap PHONE_DISPLAY + PHONE_HREF once
when the real Render/tracking number is ready.
"""

# ── Contact (change in one place) ──────────────────────────────────────────
PHONE_DISPLAY = "+1 (888) 555-0142"   # TODO: replace with the real tracking number
PHONE_HREF    = "+18885550142"        # tel: form, digits only, leading +

# ── Brand / identity ───────────────────────────────────────────────────────
BRAND      = "CruiseLine Advisors"
SITE_URL   = "https://cruiselineadvisors.com"
SINCE_YEAR = 2015

# Legal entity (differs from the brand). NOTE: the LLC name contains "cheapest", a banned
# marketing term, so build.py exempts this exact string from the guard (it's a proper noun).
COMPANY       = "BookMeCheapest LLC"
COMPANY_ADDR  = "6501 Arlington Expressway #2177, Jacksonville, FL 32211, United States"
PRIVACY_EMAIL = "privacy@cruiselineadvisors.com"  # TODO: confirm this inbox exists

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
