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
