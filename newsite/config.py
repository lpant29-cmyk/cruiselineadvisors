# -*- coding: utf-8 -*-
"""
SINGLE SOURCE OF TRUTH for site-wide constants.
Change any of these in ONE place and it updates across every generated page.

Phone number lives here and ONLY here — swap PHONE_DISPLAY + PHONE_HREF once
when the real Render/tracking number is ready.
"""

# ── Contact (change in one place) ──────────────────────────────────────────
PHONE_DISPLAY = "+1 (888) 555-0142"   # TODO: replace with the real tracking number
PHONE_HREF    = "+18885550142"        # tel: form, digits only, leading +

# ── Brand / identity ───────────────────────────────────────────────────────
BRAND      = "CruiseLine Advisors"
SITE_URL   = "https://cruiselineadvisors.com"
SINCE_YEAR = 2015

# Legal entity (differs from the brand). NOTE: the LLC name contains "cheapest" — a banned
# marketing term — so build.py exempts this exact string from the guard (it's a proper noun).
COMPANY       = "BookMeCheapest LLC"
COMPANY_ADDR  = "6501 Arlington Expressway #2177, Jacksonville, FL 32211, United States"
PRIVACY_EMAIL = "privacy@cruiselineadvisors.com"  # TODO: confirm this inbox exists

# ── Coverage hours (NEVER "24/7" — Hard Rule 6) ────────────────────────────
HOURS = {
    "en": "8am–11pm ET, every day",
    "es": "8am–11pm ET, todos los días",
}

# ── Languages ──────────────────────────────────────────────────────────────
LANGS        = ["en", "es"]
DEFAULT_LANG = "en"

# Derived
IS_PLACEHOLDER_PHONE = (PHONE_HREF == "+18885550142")
