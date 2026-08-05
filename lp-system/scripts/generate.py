#!/usr/bin/env python3
"""generate.py — renders /go/ landing pages from the lp-system data CSVs
(ADS-LP-BRIEF §7: build-time generation, no client-side data fetch).

The templates in lp-system/templates/lp/ are the functional/structural
spec. This generator bakes the page's real data into that skeleton at
build time:
  - replaces the generated-data block (RATES DATA for call-gen pages,
    PAGE PARAMS + DATA for finder pages, ITINERARY PAGE DATA for
    itinerary-detail pages) with rows from the registries filtered by
    the page's deal_filter,
  - resolves every image through 10_assets.csv ONLY (status sourced/live
    AND file present under lp-system/assets/, else the template keeps a
    labeled frame), copies referenced files to {out_root}/img/lp/... and
    emits root-relative src,
  - bakes day-by-day rows (04), port blurbs/currencies (05), ship facts
    (02), line booking notes (01) and page-facet FAQs (08),
  - stamps pricesCheckedOn from the newest date_checked actually shown,
  - swaps phone placeholders for the page's tracking slot,
  - injects the page's H1/title from 09_pages.csv,
  - guarantees the noindex meta.

Visual integration with the site design system (theme #0A2540, Fraunces/
Inter) is page-builder's job in the template files themselves; this script
is deliberately mechanical and adds no copy of its own.

Rows with VERIFY-BEFORE-PUBLISH sources never render. A page with fewer
than its minimum publishable deals (3; 1 for itinerary pages) is skipped
with an error so a thin LP can never ship silently.

Output: lp-system/out/preview/... by default. Pass --deploy-dir site to
write into the served tree (only on an approved deploy — the first such
run must ship together with the ADS-LP-BRIEF §6 footer disclosure change).

Usage:
  python3 lp-system/scripts/generate.py                # all buildable pages -> preview
  python3 lp-system/scripts/generate.py --page p002    # one page
  python3 lp-system/scripts/generate.py --deploy-dir site
"""

import argparse
import csv
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "lp-system" / "data"
TPL = ROOT / "lp-system" / "templates" / "lp"
ASSETS_DIR = ROOT / "lp-system" / "assets"

def _site_phone():
    """The phone number lives in newsite/config.py and ONLY there (same rule
    as the GTM/Clarity IDs). LP pages inherit it so the site and the ads
    layer can never drift. Per-campaign tracking numbers still override per
    page via 09_pages.csv tracking_number; env vars override for testing."""
    sys.path.insert(0, str(ROOT / "newsite"))
    try:
        import config as site_config
        return site_config.PHONE_HREF, site_config.PHONE_DISPLAY
    finally:
        sys.path.pop(0)


_SITE_TEL, _SITE_DISPLAY = _site_phone()
# Per-campaign tracking numbers are assigned per page (ADS-LP-BRIEF §8);
# qa-auditor's placeholder check still runs before any deploy.
PHONE_TEL = os.environ.get("LP_PHONE_TEL", _SITE_TEL)
PHONE_DISPLAY = os.environ.get("LP_PHONE_DISPLAY", _SITE_DISPLAY)
AGENCY_NAME = os.environ.get("LP_AGENCY_NAME", "CruiseLine Advisors")


def _legal_partial():
    """The shared legal-disclosure partial (newsite/legal_partial.py) — the
    operator's one-source-of-truth ruling: main site and /go/ pages render
    the SAME legal blocks; a legal edit there updates every page. LP pages
    add the 6a fares paragraph (fare-showing pages only)."""
    sys.path.insert(0, str(ROOT / "newsite"))
    try:
        import legal_partial
        import config as site_config
        return legal_partial, site_config
    finally:
        sys.path.pop(0)


def lp_footer_html(final_tel, final_display):
    """Compact LP footer: shared legal blocks (incl. 6a) + real legal links
    + phone. No nav columns (ADS-LP-BRIEF: no exits; footer small-print
    links to main-site legal pages are the permitted exception)."""
    lp, cfg = _legal_partial()
    year = dt.date.today().year
    blocks = lp.legal_blocks_html("en", include_fares_paragraph=True)
    links = lp.legal_links_html("en")
    return f"""<footer>
  <div class="wrap">
    <div class="legal">
      <p class="agency-line">{AGENCY_NAME}: independent cruise information &amp; referral service</p>
      {blocks}
      <div class="legalrow" style="display:flex;gap:14px;flex-wrap:wrap;margin:10px 0">{links}</div>
      <p><a href="tel:{final_tel}" style="font-weight:800">{final_display}</a> · 8am-11pm ET, every day</p>
      <p style="margin-top:.6rem">© {year} {cfg.COMPANY}. Florida, USA.</p>
    </div>
  </div>
</footer>"""


def lp_brand_html():
    """The MAIN SITE's logo lockup (newsite/logo.py, single source) for the
    LP slim header — mark + wordmark, deliberately NOT linked (no exits on
    /go/ pages). Operator ruling 2026-07-30."""
    sys.path.insert(0, str(ROOT / "newsite"))
    try:
        import logo
        return ('<span class="brand brand-lockup">' + logo.mark(30) +
                '<span class="brand-txt">CruiseLine<span>Advisors</span></span></span>')
    finally:
        sys.path.pop(0)


BRAND_CSS = ("<style>.brand-lockup{display:inline-flex;align-items:center;gap:9px}"
             ".brand-lockup .brand-txt{font-family:'Fraunces','Georgia',serif;font-weight:600;"
             "font-size:20px;letter-spacing:-.01em;color:var(--deep)}"
             ".brand-lockup .brand-txt span{color:#E0A84E}"
             # back-to-top + header back button (operator ruling 2026-07-30)
             ".backtop{position:fixed;right:14px;bottom:calc(104px + env(safe-area-inset-bottom));z-index:66;width:44px;height:44px;"
             "border-radius:50%;border:2px solid var(--deep);background:#fff;color:var(--deep);"
             "font-size:20px;font-weight:800;cursor:pointer;box-shadow:0 6px 18px rgba(10,37,64,.18);"
             "opacity:0;visibility:hidden;transition:opacity .2s,visibility 0s .2s}"
             ".backtop.show{opacity:1;visibility:visible;transition:opacity .2s,visibility 0s}"
             "@media(min-width:901px){.backtop{bottom:24px}}"
             ".goback{border:0;background:none;color:var(--sea-d);font:inherit;font-weight:700;"
             "font-size:14px;cursor:pointer;padding:6px 10px 6px 0;white-space:nowrap}"
             "@media(prefers-reduced-motion:reduce){.backtop{transition:none}}</style>")

NAV_UI_JS = """<script>
(function(){if(!document.body)return; /* back-to-top, appears after a scroll */
var b=document.createElement('button');b.className='backtop';b.type='button';
b.setAttribute('aria-label','Back to top');b.textContent='\\u2191';
document.body.appendChild(b);
var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
b.addEventListener('click',function(){window.scrollTo({top:0,behavior:rm?'auto':'smooth'});});
var t=false;
window.addEventListener('scroll',function(){if(t)return;t=true;requestAnimationFrame(function(){
  b.classList.toggle('show',window.scrollY>800);t=false;});},{passive:true});
})();
(function(){ /* header Back button , ONLY when the previous page is one of
   ours. history.length>1 would also be true for a paid click from a SERP,
   putting a one-tap route back to the ad in the header of a page
   we paid for (guardian audit #9). Same-origin referrer only. */
var wrap=document.querySelector('.nav .wrap');if(!wrap)return;
var ref=document.referrer||'';
var hasPrev=ref.indexOf(location.origin+'/')===0&&ref!==location.href;
if(!hasPrev)return;
var b=document.createElement('button');b.className='goback';b.type='button';
b.setAttribute('aria-label','Go back to the previous page');b.textContent='\\u2039 Back';
b.addEventListener('click',function(){history.back();});
wrap.insertBefore(b,wrap.firstChild);
})();
</script>"""


# Callback form endpoint: Apps Script web app appending to the sheet's
# cruise_leads tab. Public by design (it can only append to that tab).
CALLBACK_ACTION = os.environ.get("LP_CALLBACK_ACTION", "https://script.google.com/macros/s/AKfycbyK9a8Y6iWMEHOQb8FyVXAm4jEl6cFt8mVlJCp67leR-nPDG7SIbvEAJyJGwnOOasPg6g/exec")

CONSENT_SENTENCE = "See our Calling & SMS Consent policy."
# clean directory URL — the host serves /en/legal/<page>/index.html (qa D1)
CONSENT_LINKED = ('See our <a href="/en/legal/consent/">Calling &amp; SMS Consent</a> policy.')


def _site_tag_ids():
    """GTM container and Clarity project MUST match the live site's — import
    them from newsite/config.py (the site's single source) so they can never
    drift. GA4 and the Ads tag fire inside GTM on the main site, so loading
    the same container gives /go/ pages the identical stack."""
    sys.path.insert(0, str(ROOT / "newsite"))
    try:
        import config as site_config
        return site_config.GTM_ID, site_config.CLARITY_ID
    finally:
        sys.path.pop(0)

TEMPLATE_BY_TYPE = {
    "line": "call-gen-line-royal-caribbean.html",
    "port": "call-gen-port-galveston.html",
    # ship template v2 (operator ruling 2026-07-29, SHIP PAGES): full
    # master-enrichment page fed by the newsite ships dataset + the LP CSVs
    "ship": "ship-detail.html",
    "audience": "call-gen-audience-family.html",
    "combo": "finder-rci-from-galveston.html",
    "itinerary": "itinerary-detail.html",
}
BUILDABLE = {"approved", "building", "built", "built-template", "live", "pilot"}
VERIFY_MARK = "VERIFY-BEFORE-PUBLISH"
ASSET_OK = {"sourced", "live"}
# call-gen templates carry a RATES DATA block; the finder template carries a
# PAGE PARAMS + DATA block; itinerary-detail carries ITINERARY PAGE DATA
RATES_RE = re.compile(
    r"/\* ===== RATES DATA[^*]*\*/.*?/\* ===== END RATES DATA ===== \*/",
    re.S)
FINDER_RE = re.compile(
    r"/\* =+\n\s*PAGE PARAMS \+ DATA.*?/\* =+ END GENERATED DATA =+ \*/",
    re.S)
ITIN_RE = re.compile(
    r"/\* =+\n\s*ITINERARY PAGE DATA.*?/\* =+ END GENERATED DATA =+ \*/",
    re.S)
SHIP_RE = re.compile(
    r"/\* =+\n\s*SHIP PAGE DATA.*?/\* =+ END GENERATED DATA =+ \*/",
    re.S)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def targets_of(row):
    return {t.strip() for t in row.get("page_targets", "").split(";") if t.strip()}


def month_label(iso_date):
    return dt.date.fromisoformat(iso_date).strftime("%B %-d")


def load_whitelist():
    domains = []
    for line in (DATA / "source_whitelist.txt").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            domains.append(line.lower())
    return domains


# how many days a stamp stays printable. Past this the fare is withheld and
# the card shows a call prompt instead (the "freshness fuse"): if the daily
# refresh ever stops, pages degrade to call-only rather than advertising a
# stale number. This inventory has moved 20%+ inside 24h.
PRICE_MAX_AGE_DAYS = 3


def price_ok(row, today=None):
    """Is this row's fare safe to PRINT today? Separate from provenance:
    the sailing still publishes either way (operator ruling 2026-07-30),
    but an unstable, unstamped or stale fare renders as a call prompt."""
    if "HOLD:" in row.get("notes", "").upper():
        return False
    if not row.get("price_interior", "").strip():
        return False
    stamp = row.get("date_checked", "").strip()
    if not stamp:
        return False
    try:
        age = ((today or dt.date.today()) - dt.date.fromisoformat(stamp)).days
    except ValueError:
        return False
    return age <= PRICE_MAX_AGE_DAYS


def provenance_ok(row, whitelist):
    """CONTENT gate: is this itinerary real and officially sourced? Only rows
    from a whitelisted official URL and not flagged UNVERIFIED/
    VERIFY-BEFORE-PUBLISH publish at all. A price HOLD no longer blocks the
    row (see price_ok) - it withholds the fare, not the sailing."""
    if VERIFY_MARK in row.get("source", ""):
        return False
    if "UNVERIFIED" in row.get("notes", "").upper():
        return False
    src = row.get("source", "")
    if not src.startswith(("http://", "https://")):
        return False
    host = (urlparse(src).netloc or "").lower().split(":")[0]
    return any(host == d or host.endswith("." + d) for d in whitelist)


def ship_slug_map(deals, reg):
    """variant key -> ship_id, for the finder's ?v= ship focus. Built from the
    page's own sailings so a variant can only narrow to a ship that is here."""
    out = {}
    for r in deals:
        for sid in [x.strip() for x in r.get("ship_ids", "").split(";") if x.strip()]:
            srow = reg["ships_by_id"].get(sid)
            if not srow:
                continue
            slug = srow.get("slug", "")
            if slug:
                out[slug] = sid
                out[slug.replace("-of-the-seas", "")] = sid
    return out


def h1_variants(deals, reg, page):
    """Whitelisted H1 rewrites for ?v=. ONE VARIANT PER AD GROUP so every
    keyword lands on a heading that mirrors it (the quality-score triangle).
    Generated from this page's own inventory, so a heading can never claim a
    ship or a length the page cannot show. Unknown values are ignored."""
    port = deals[0]["port_label"].rsplit(" ", 1)[0] if deals else ""
    line = page.get("h1", "").split(" Cruises")[0] or "Royal Caribbean"
    out = {}

    # port/schedule phrasings, one per core keyword
    out["port"] = f"{line} {port} Cruise Port"
    out["outof"] = f"{line} Cruises Out of {port}"
    out["schedule"] = f"{line} {port} Cruise Schedule"
    out["porttx"] = f"{line} Cruise Port in {port}, Texas"

    # ship variants, only for ships with sailings here
    by_ship = {}
    for r in deals:
        for sid in [x.strip() for x in r.get("ship_ids", "").split(";") if x.strip()]:
            by_ship.setdefault(sid, []).append(r)
    for sid in by_ship:
        srow = reg["ships_by_id"].get(sid)
        if not srow:
            continue
        slug, name = srow.get("slug", ""), srow.get("ship_name", "")
        if not slug or not name:
            continue
        label = f"{name} Cruises from {port}"
        out[slug] = label
        out[slug.replace("-of-the-seas", "")] = label

    # duration variants, only for lengths that exist on this page
    for n in sorted({int(r["nights"]) for r in deals}):
        out[f"{n}night"] = f"{n}-Night {line} Cruises from {port}"
        out[f"{n}day"] = f"{n}-Day {line} Cruises from {port}"
    return out


def deals_for(page, itins, cap=6):
    """cap=6 for call-gen deal cards (ADS-LP-BRIEF: 3-6 cards); finder pages
    pass cap=None — the finder is a search UI over the FULL publishable
    inventory, and its Sail-to filter must reflect every real destination."""
    flt = page["deal_filter"].strip()
    whitelist = load_whitelist()
    # no stamp, no price, no render — provenance AND a stamped price required
    rows = [r for r in itins
            if flt in targets_of(r) and provenance_ok(r, whitelist)]
    # priced rows first (cheapest first); fare-withheld rows keep their place
    # in the list rather than disappearing from it
    rows.sort(key=lambda r: (r.get("featured") != "yes", not price_ok(r),
                             int(r["price_interior"] or 10 ** 6)))
    return rows[:cap] if cap else rows


def deals_for_ship(page, reg):
    """Ship pages join itineraries by ship_id (structure-guard implementation
    decision 2026-07-29): canonical mechanism is 02_ships membership in the
    row's ship_ids; the page's deal_filter (ship:<slug>) is declared intent
    only. Same provenance + stamped-price gates as deals_for; sorted by
    interior from-fare so the hero fare is the cheapest publishable row."""
    srow = reg["ships_by_slug"].get(page["slug"])
    if not srow:
        raise ValueError(f"{page['page_id']}: ship slug {page['slug']!r} not in 02_ships.csv")
    whitelist = load_whitelist()
    sid = srow["ship_id"]
    rows = [r for r in reg["itins"]
            if sid in [s.strip() for s in r.get("ship_ids", "").split(";")]
            and provenance_ok(r, whitelist)]
    rows.sort(key=lambda r: (not price_ok(r), int(r["price_interior"] or 10 ** 6)))
    return rows


def offers_for(page, offers, today):
    flt = page["deal_filter"].strip()
    live = []
    OFFER_PUBLISHABLE = {"", "approved", "live", "verified"}
    for o in offers:
        if o.get("show_banner") != "yes":
            continue
        # a row still marked draft/example must never render, whatever its
        # banner flag says (pricing-scout finding 2026-07-30)
        if o.get("status", "").strip().lower() not in OFFER_PUBLISHABLE:
            continue
        pages_ = {t.strip() for t in o.get("banner_pages", "").split(";")}
        if flt not in pages_:
            continue
        if not (o["start_date"] <= today.isoformat() <= o["end_date"]):
            continue
        live.append(o)
    return live


def ship_names(row, ships):
    ids = [s.strip() for s in row.get("ship_ids", "").split(";") if s.strip()]
    return "; ".join(ships.get(i, i) for i in ids) or row["line_id"].upper()


def months_of(row, today):
    """Sail months as YYYY-MM list. 'year-round' rows: prefer the months that
    actually carry a price in month_price_overrides (registrar task queued to
    replace 'year-round' with explicit lists; until then this stops months
    with no sailings/prices from rendering as filter options). Fall back to
    the next 6 months only when no overrides exist."""
    raw = row.get("sail_months", "").strip()
    if raw != "year-round":
        return [t.strip() for t in raw.split(";") if t.strip()]
    override_months = sorted({m.group(1) for m in
                              re.finditer(r"(\d{4}-\d{2}):", row.get("month_price_overrides", ""))})
    if override_months:
        return override_months
    out, y, m = [], today.year, today.month
    for _ in range(6):
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


def parse_overrides(row):
    """month_price_overrides -> {'YYYY-MM': {'i': int, 'b': int}}. Tokens are
    |-separated; a bare i/b token (e.g. 'b598') belongs to the last month
    seen ('2026-08:i448|b598|2026-10:i456|b794')."""
    out, cur = {}, None
    for tok in row.get("month_price_overrides", "").split("|"):
        tok = tok.strip()
        if not tok:
            continue
        m = re.match(r"(\d{4}-\d{2}):([ib])(\d+)$", tok)
        if m:
            cur = m.group(1)
            out.setdefault(cur, {})[m.group(2)] = int(m.group(3))
            continue
        m = re.match(r"([ib])(\d+)$", tok)
        if m and cur:
            out.setdefault(cur, {})[m.group(1)] = int(m.group(2))
    return out


def price_map(row):
    """{'default': interior, 'YYYY-MM': interior-override} for the finder's
    month-aware from-fare display."""
    prices = {"default": int(row["price_interior"])}
    for month, v in parse_overrides(row).items():
        if "i" in v:
            prices[month] = v["i"]
    return prices


def months_without_interior(row):
    """Months whose override carries a balcony fare but NO interior fare: the
    source offers no interior that month (e.g. sold out). The finder displays
    interior-only, so these months must never fall back to the default
    interior — that would render a fare that does not exist (qa-auditor
    re-gate find, i0009 Aug-2026)."""
    return {m for m, v in parse_overrides(row).items() if "b" in v and "i" not in v}


def facet_parts(deal_filter):
    """('combo', 'royal-caribbean-galveston') from 'combo:royal-caribbean-galveston'."""
    kind, _, rest = deal_filter.partition(":")
    return kind, rest


def url_facets(url):
    """line/port/dest parsed from the /go/ URL patterns for dataLayer vars."""
    line = re.search(r"/lines/([^/]+)/", url)
    port = re.search(r"/from/([^/]+)/", url)
    dest = re.search(r"/to/([^/]+)/", url)
    return (line.group(1) if line else "",
            port.group(1) if port else "",
            dest.group(1) if dest else "")


def facet_from_targets(targets, prefix):
    return next((t.split(":", 1)[1] for t in sorted(targets) if t.startswith(prefix)), "")


# ------------------------------------------------- ships dataset (newsite)

def slugify(name):
    """'Mariner of the Seas' -> 'mariner-of-the-seas'. The join key between
    the newsite ships dataset and 02_ships.csv slugs."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower())
    return s.strip("-")


def load_ship_dataset():
    """Single source of ship experience facts, shared with the live site:
    newsite/data/ships/*.json (per-line rosters with spec_source + exp).
    Keyed by slugified ship name; no facts are duplicated into the LP CSVs
    (02_ships keeps only the LP-specific fields)."""
    out = {}
    ships_dir = ROOT / "newsite" / "data" / "ships"
    if not ships_dir.is_dir():
        return out
    for path in sorted(ships_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for ship in data.get("ships", []):
            if ship.get("name"):
                out[slugify(ship["name"])] = ship
    return out


def venue_split(entertainment):
    """Mechanical bars-vs-shows split of exp.entertainment by the venue's own
    stated words (name/desc containing bar/lounge/pub). Nothing is invented:
    a ship with no show entries renders an honestly small nightlife note."""
    bars, shows = [], []
    for v in entertainment or []:
        blob = f"{v.get('name', '')} {v.get('desc', '')}".lower()
        (bars if re.search(r"\b(bar|lounge|pub)\b", blob) else shows).append(v)
    return bars, shows


def family_line(exp):
    """One family line from the dataset: kids_family verbatim when it is a
    string; when it is a venue list, the venue names joined (registry names
    only, no invented descriptions)."""
    fam = (exp or {}).get("kids_family")
    if isinstance(fam, str):
        return fam
    if isinstance(fam, list):
        names = [x.get("name") for x in fam if x.get("name")]
        if names:
            if len(names) > 1:
                return ("Family spaces on board include "
                        + ", ".join(names[:-1]) + " and " + names[-1] + ".")
            return f"Family spaces on board include {names[0]}."
    return ""


def public_note(text):
    """Strip registrar-internal provenance sentences (from 'Internal
    cross-check' on) out of a note before it renders as page copy. The
    public honest-gap wording stays verbatim."""
    return (text or "").split("Internal cross-check")[0].strip()


# ---------------------------------------------------------------- assets

def webp_size(path):
    """Minimal WebP dimension reader (VP8/VP8L/VP8X) so <img> can carry
    proportion-preserving width/height without an imaging dependency."""
    try:
        with open(path, "rb") as f:
            head = f.read(30)
        if head[:4] != b"RIFF" or head[8:12] != b"WEBP":
            return (None, None)
        fmt = head[12:16]
        if fmt == b"VP8X":
            return (int.from_bytes(head[24:27], "little") + 1,
                    int.from_bytes(head[27:30], "little") + 1)
        if fmt == b"VP8L":
            b = head[21:25]
            w = 1 + (((b[1] & 0x3F) << 8) | b[0])
            h = 1 + (((b[3] & 0x0F) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
            return (w, h)
        if fmt == b"VP8 ":
            return (int.from_bytes(head[26:28], "little") & 0x3FFF,
                    int.from_bytes(head[28:30], "little") & 0x3FFF)
    except OSError:
        pass
    return (None, None)


def _asset_rows(assets, subject_type, slug, variant):
    """All 10_assets.csv rows matching (type, slug, variant) whose file is
    present on disk, in registry order. Resolution is STRICT: status must be
    sourced/live and the file must exist under lp-system/assets/."""
    out = []
    for r in assets:
        if (r.get("status") in ASSET_OK
                and r.get("subject_type") == subject_type
                and r.get("subject_slug") == slug
                and r.get("file", "").startswith("img/")
                and r.get("file", "").endswith(f"-{variant}.webp")):
            path = ASSETS_DIR / r["file"]
            if path.is_file():
                out.append((r, path))
    return out


def _register_asset(row, path, used):
    rel = row["file"][len("img/"):]
    used[rel] = path
    w, h = webp_size(path)
    obj = {"src": f"/img/lp/{rel}", "alt": row.get("alt_text", "")}
    if w and h:
        obj["w"], obj["h"] = w, h
    return obj


def asset_obj(assets, subject_type, slug, variant, used):
    """Resolve an image STRICTLY through 10_assets.csv (first matching row).
    Anything unresolved returns None and the template keeps a labeled frame.
    Resolved files are registered in `used` for the copy step and the src
    emitted is root-relative (/img/lp/...)."""
    rows = _asset_rows(assets, subject_type, slug, variant)
    if not rows:
        return None
    return _register_asset(rows[0][0], rows[0][1], used)


def asset_pick(assets, subject_type, slug, variant, used, index):
    """Like asset_obj but cycles through ALL registry matches (index mod
    count) so repeated subjects (e.g. Galveston on embark day AND return
    day) can rotate between their registered photos."""
    rows = _asset_rows(assets, subject_type, slug, variant)
    if not rows:
        return None
    row, path = rows[index % len(rows)]
    return _register_asset(row, path, used)


# photo-story sea-day rotation: generic on-board subjects from the registry,
# cycled so adjacent sea days never repeat the same photo
SEA_DAY_SUBJECTS = [("ship-generic", "deck-scene"), ("ship-generic", "sea-day"),
                    ("ship-generic", "ship-at-sea")]


def journey_images(days, assets, used):
    """Attach a -section image to every day row for the photo-story layout.
    Port days use that port's section asset(s) (cycling when the port
    repeats); sea days rotate through the generic on-board subjects so
    adjacent days differ. Unresolvable days keep img=None (labeled frame)."""
    port_seen, sea_i, last_src = {}, 0, None
    out = []
    for d in days:
        img = None
        if d["p"] == "at-sea":
            for _ in range(len(SEA_DAY_SUBJECTS)):
                st, sl = SEA_DAY_SUBJECTS[sea_i % len(SEA_DAY_SUBJECTS)]
                sea_i += 1
                cand = asset_obj(assets, st, sl, "section", used)
                if cand and cand["src"] != last_src:
                    img = cand
                    break
        else:
            k = port_seen.get(d["p"], 0)
            port_seen[d["p"]] = k + 1
            img = asset_pick(assets, "port", d["p"], "section", used, k)
        last_src = img["src"] if img else last_src
        out.append({**d, "img": img})
    return out


def card_asset(assets, dest, used):
    """Deal/itinerary card image: the destination's card asset. Destinations
    without an asset row (photo-curator 2026-07-29: no 'caribbean' row, do
    NOT invent an alias row) fall back to the generic ship-at-sea card."""
    return (asset_obj(assets, "dest", dest, "card", used)
            or asset_obj(assets, "ship-generic", "ship-at-sea", "card", used))


def ship_card_img(assets, used, idx):
    """Sailing cards on a ship page: rotate the licensed real-ship photos so
    each card differs. ship-night is excluded on purpose, it is the one asset
    with any lettering in frame."""
    pool = ["ship-hero", "ship-bow", "ship-lowangle", "ship-aerial",
            "ship-sunset", "ship-at-sea", "ship-docked", "ship-balcony",
            "ship-decks", "ship-foredeck", "deck-scene", "sea-day"]
    for n in range(len(pool)):
        img = asset_obj(assets, "ship-generic", pool[(idx + n) % len(pool)], "card", used)
        if img:
            return img
    return None


def itinerary_card_img(assets, days, dest, used, idx, prev_src):
    """Finder-card imagery, varied AND relevant (operator ruling 2026-07-30):
    prefer the itinerary's own ports of call (cococay resolves to the
    generic-beach stand-in via its dest row), interleave the licensed
    generic ship shots on alternating cards, avoid repeating the previous
    card's image. Real named-ship photos remain trade-portal-only; every
    slot here carries the registry's honest alt text."""
    cands = []
    seen = set()
    for d in days:
        slug = d.get("p", "")
        if slug in ("at-sea", "") or slug in seen:
            continue
        seen.add(slug)
        img = (asset_obj(assets, "port", slug, "card", used)
               or asset_obj(assets, "dest", slug, "card", used))
        if img:
            cands.append(img)
    ships = [i for i in (asset_obj(assets, "ship-generic", s, "card", used)
                         for s in ("ship-hero", "ship-bow", "ship-lowangle",
                                   "ship-aerial", "ship-sunset", "ship-at-sea",
                                   "ship-docked", "ship-balcony", "ship-decks",
                                   "ship-foredeck", "deck-scene", "sea-day")) if i]
    fallback = card_asset(assets, dest, used)
    # least-recently-used pick over the row's RELEVANT pool (its own call
    # ports first, then the ship shots, then the dest fallback): spreads
    # the whole licensed set across the list while every port image stays
    # tied to an itinerary that actually calls there
    pool = cands + ships + ([fallback] if fallback else [])
    if not pool:
        return None
    counts = itinerary_card_img.counts
    best = min((img for img in pool if img["src"] != prev_src),
               key=lambda img: (counts.get(img["src"], 0), pool.index(img)),
               default=pool[0])
    counts[best["src"]] = counts.get(best["src"], 0) + 1
    return best


itinerary_card_img.counts = {}


# ------------------------------------------------------- registry shaping

_PORT_SUFFIXES = (" Mexico", " Honduras", " Bahamas", " Belize", " Grand Cayman",
                  " Jamaica", " Curacao", " Aruba", " TX", " FL", " NJ")


def short_port(label):
    """Mechanical short label for route chips (strip country/state suffix)."""
    if "CocoCay" in label:
        return "CocoCay"
    if label.startswith("Cape Liberty"):
        return "Cape Liberty"
    for suf in _PORT_SUFFIXES:
        if label.endswith(suf):
            return label[:-len(suf)]
    return label


def day_objs(itin_id, day_rows):
    """Baked day array from 04_itinerary_days: port slug + times + note.
    Labels/blurbs/currencies come from the PORTS lookup at render time."""
    ds = sorted((r for r in day_rows if r["itin_id"] == itin_id),
                key=lambda r: int(r["day_no"]))
    return [{"n": int(r["day_no"]), "p": r["port_slug"],
             "arr": r.get("arrive", "").strip(), "dep": r.get("depart", "").strip(),
             "note": r.get("note", "").strip()} for r in ds]


def port_info(slug, ports_by_slug):
    """PORTS lookup entry from 05_ports_content: full label, chip label,
    one-line blurb (first sentence, own words already in the registry) and
    currency chips. Rows flagged UNVERIFIED keep label only — the honest
    gap renders as no blurb and no currency chip."""
    row = ports_by_slug.get(slug)
    if not row:
        return {"label": slug.replace("-", " ").title(), "short": slug,
                "blurb": "", "story": "", "cur": []}
    label = row.get("port_label", slug)
    out = {"label": label, "short": short_port(label), "blurb": "", "story": "", "cur": []}
    if "UNVERIFIED" in row.get("notes", "").upper():
        return out
    blurb = row.get("blurb", "").strip()
    if blurb:
        first = blurb.split(". ")[0].rstrip(".") + "."
        out["blurb"] = first
        # photo-story caption: the registry blurb in full (already our own
        # words); the one-liner stays for chips/expanders
        out["story"] = blurb
    out["cur"] = [c.strip() for c in row.get("currency", "").split(";") if c.strip()]
    return out


def ship_obj(srow, ds=None):
    """Ship module entry from 02_ships — name, class_or_note verbatim
    (Rule 3: unverified gaps stay visible, never tidied), size tier,
    audience fit, highlights, family note, plus a sea-day line built only
    from the registry's own highlights (never invented venues). When the
    newsite ships dataset carries this ship, a `ds` summary is attached
    (specs, verified dining counts, family line) for the tabbed modules;
    templates null-guard `ds` for ships not yet in the dataset."""
    high = [h.strip() for h in srow.get("highlights", "").split(";") if h.strip()]
    if len(high) > 1:
        sea = ", ".join(high[:-1]) + " and " + high[-1]
    else:
        sea = high[0] if high else ""
    out = {
        "id": srow["ship_id"], "name": srow["ship_name"],
        "cls": srow.get("class_or_note", ""), "tier": srow.get("size_tier", ""),
        "fit": [f.strip() for f in srow.get("audience_fit", "").split(";") if f.strip()],
        "high": high, "family": srow.get("family_note", ""),
        "seaLine": (f"A full day on board. Ship time on {srow['ship_name']}: {sea}."
                    if sea else f"A full day on board {srow['ship_name']}."),
        "ds": None,
    }
    if ds:
        exp = ds.get("exp") or {}
        dining = exp.get("dining") or []
        out["ds"] = {
            "year": ds.get("year"), "guests": ds.get("guests"),
            "tonnage": ds.get("tonnage"),
            "dineInc": sum(1 for v in dining if not v.get("extra")),
            "dineExtra": sum(1 for v in dining if v.get("extra")),
            "famLine": family_line(exp),
        }
    return out


def ship_tabs(ds, assets, used):
    """Condensed ship tabs for the itinerary page (at-a-glance / dining /
    family / nightlife). Facts strictly from the newsite ships dataset;
    None when the ship is not in the dataset (template falls back to the
    single honest panel). Tab images resolve via 10_assets.csv per theme:
    dining -> dining, family -> waterslide, nightlife -> lounge-bar; the
    at-a-glance tab is a facts card and carries no photo."""
    if not ds:
        return None
    exp = ds.get("exp") or {}
    dining = exp.get("dining") or []
    bars, _shows = venue_split(exp.get("entertainment"))
    fam = exp.get("kids_bands") if isinstance(exp.get("kids_bands"), str) else ""
    fam = fam or family_line(exp)
    return {
        "glance": {"year": ds.get("year"), "guests": ds.get("guests"),
                   "tonnage": ds.get("tonnage"),
                   "features": ds.get("features") or [],
                   "overview": exp.get("overview", "")},
        "dining": {"inc": [v.get("name", "") for v in dining if not v.get("extra")],
                   "extra": [v.get("name", "") for v in dining if v.get("extra")],
                   "img": asset_obj(assets, "ship-generic", "dining", "section", used)},
        "family": {"text": fam,
                   "img": asset_obj(assets, "theme", "waterslide", "section", used)},
        "night": {"venues": [{"name": v.get("name", ""), "desc": v.get("desc", "")}
                             for v in bars],
                  "img": asset_obj(assets, "ship-generic", "lounge-bar", "section", used)},
    }


def when_lines(month_list):
    """?when= subheading WHITELIST: one baked phrase per month that actually
    has fare data. The runtime reads ?when= (YYYY-MM or next-month) and only
    ever uses a phrase from this dict; anything else is silently ignored."""
    out = {}
    for m in month_list:
        label = dt.date(int(m[:4]), int(m[5:7]), 1).strftime("%B %Y")
        out[m] = f"Sailing in {label}? Here is the fare picture."
    return out


def deposit_struct(note):
    """Mobile-polish item 7: deposit notes are number-dense, so the
    registry's own wording is mechanically split into 2-col table rows
    (sailing length | deposit; sailing length | final payment due) plus the
    prose clauses that carry no tier series. Nothing is invented: every cell
    is a substring of the registry note re-shaped, and notes that match no
    tier pattern return rows=[]/pay=[] with the full note as prose, which
    the templates render exactly as before."""
    note = (note or "").strip()
    rows, pay, prose = [], [], []
    if not note:
        return {"rows": rows, "pay": pay, "prose": ""}
    clauses = [c.strip() for c in re.split(r"(?:(?<=[a-z)])\. |; )", note) if c.strip()]
    for c in clauses:
        tier = re.findall(r"\$(\d+) pp on (\d+(?:-\d+|\+)) night", c)
        due = re.findall(r"(\d+) days(?: out)? \((\d+(?:-\d+|\+)) nights?\)", c)
        if tier:
            rows += [{"len": t[1] + " nights", "amt": "$" + t[0] + " pp"} for t in tier]
        elif due:
            pay += [{"len": d[1] + " nights", "due": d[0] + " days before sailing"}
                    for d in due]
        else:
            prose.append(c[0].upper() + c[1:] if c else c)
    prose_txt = ". ".join(p.rstrip(".") for p in prose)
    if prose_txt:
        prose_txt += "."
    return {"rows": rows, "pay": pay, "prose": prose_txt}


def pre_cruise_obj(port_row):
    """Pre-cruise module content: the registry's own pre_cruise prose plus
    the port's highlight list. None when the registry has nothing."""
    if not port_row:
        return None
    txt = port_row.get("pre_cruise", "").strip()
    if not txt:
        return None
    items = [h.strip() for h in port_row.get("highlights", "").split(";") if h.strip()]
    items = [i[0].upper() + i[1:] if i else i for i in items]
    return {"text": txt, "items": items}


def faqs_for(page, deals, faqs):
    """FAQ bake: rows from 08_faqs matching the page's facets (deal_filter
    plus every page_target on the rendered deal rows, plus 'all'). Max 4;
    'is calling more expensive' (q003) always first. q001 (travel documents,
    cbp.gov-sourced closed-loop answer) is included per the operator ruling
    2026-07-29 — it backs the know-panel Documents line and the itinerary
    page's travel-documents section."""
    facets = {"all", page["deal_filter"].strip()}
    for d in deals:
        facets |= targets_of(d)
    sel = [f for f in faqs if targets_of(f) & facets]
    if not any(f["faq_id"] == "q001" for f in sel):
        q1 = next((f for f in faqs if f["faq_id"] == "q001" and f.get("source")), None)
        if q1:
            sel.append(q1)
    sel.sort(key=lambda f: (f["faq_id"] != "q003", f["faq_id"]))
    return [{"q": f["question"], "a": f["answer"]} for f in sel[:4]]


def docs_summary(faqs):
    """One-line travel-documents summary for the know panel: first sentence
    of q001's registry answer (only when it carries a source)."""
    q1 = next((f for f in faqs if f["faq_id"] == "q001" and f.get("source")), None)
    if not q1:
        return ""
    return q1["answer"].split(". ")[0].rstrip(".") + "."


# ------------------------------------------------------------- tracking

def tracking_head(page, gtm_id, clarity_id, facets):
    """dataLayer vars first, then GTM, then Clarity — mirroring newsite/base.py.
    lp_variant/lp_when come from the URL at runtime (?v= / ?when=).
    facets = (line, port, dest, ship); itinerary URLs carry no
    /lines//from//to/ segments, so their facets are derived from the
    itinerary row's page_targets by the caller. `ship` is set ONLY on ship
    pages (from the page slug): a ship page's intent spans ports, so port
    and dest stay empty there rather than guessing a home port — documented
    for tracking-guardian."""
    line, port, dest, ship = facets
    page_vars = json.dumps({"page_type": "lp", "page_id": page["page_id"],
                            "line": line, "port": port, "dest": dest,
                            "ship": ship})
    out = ("<script>window.dataLayer=window.dataLayer||[];"
           "(function(){var q=new URLSearchParams(location.search),v=" + page_vars + ";"
           "v.lp_variant=q.get('v')||'';v.lp_when=q.get('when')||'';"
           "window.dataLayer.push(v);})();</script>")
    if gtm_id:
        out += ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
                "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
                "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
                "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;"
                "f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','" + gtm_id + "');</script>")
    if clarity_id:
        out += ("<script>(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[])"
                ".push(arguments)};t=l.createElement(r);t.async=1;"
                "t.src='https://www.clarity.ms/tag/'+i;y=l.getElementsByTagName(r)[0];"
                "y.parentNode.insertBefore(t,y);})(window,document,'clarity','script','" + clarity_id + "');</script>")
    return out


def tracking_noscript(gtm_id):
    if not gtm_id:
        return ""
    return (f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={gtm_id}"'
            ' height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>')


def tracking_events(page, final_tel, final_display):
    """Conversion-event wiring: tel_click on every tel: link with its section
    position, lead_submit on callback-form success with a thank-you state,
    plus Google website-call dynamic number insertion via the _googWcmGet
    CALLBACK method (numbers here are JS-rendered, so the static swap snippet
    cannot see them). The callback re-applies through a MutationObserver so
    re-rendered elements (finder searches, dynamic cards) stay swapped, and
    falls back gracefully to the real number when Google returns nothing.
    The 30s threshold lives in the Ads conversion action, not this page.
    POS note: '.fares' maps to 'deal-card' — the itinerary page's fare table
    is that page's deal module (same contract role as .itin/.scard cards).
    '.sheet-deal' (mobile UX pass) also maps to 'deal-card': the finder's
    row/featured-slide bottom sheet IS the deal card's mobile expansion and
    its call CTA is the same conversion element. Ship-life ('sheet-life')
    and day-detail ('sheet-day') sheets carry no mapping on purpose: their
    call CTAs are contextual prompts, the analog of the callrow prompts
    already documented as 'other'.
    IIFE + null guards per the project's known-pitfalls rules."""
    return """<script>
(function(){if(!document.body)return;
var REAL_DISPLAY=%s,swapped=null;
function telHref(n){var d=String(n).replace(/\\D/g,'');if(d.length===10)d='1'+d;return 'tel:+'+d;}
function applyAll(){
  if(!swapped)return;
  var links=document.querySelectorAll('a[href^="tel:"]');
  for(var i=0;i<links.length;i++){links[i].setAttribute('href',telHref(swapped.m));}
  var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT),n;
  while((n=w.nextNode())){if(n.nodeValue&&n.nodeValue.indexOf(REAL_DISPLAY)!==-1){n.nodeValue=n.nodeValue.split(REAL_DISPLAY).join(swapped.f);}}
  /* T-ARIA-DNI: accessible names must swap with the displayed number, or
     screen-reader users dial around Google forwarding (undercounts the
     primary call conversion). Runs inside applyAll so the MutationObserver
     covers re-rendered elements too. */
  var al=document.querySelectorAll('[aria-label]');
  for(var k=0;k<al.length;k++){var v=al[k].getAttribute('aria-label');
    if(v&&v.indexOf(REAL_DISPLAY)!==-1){al[k].setAttribute('aria-label',v.split(REAL_DISPLAY).join(swapped.f));}}
}
new MutationObserver(function(){if(swapped)applyAll();}).observe(document.body,{childList:true,subtree:true});
var tries=0;
(function poll(){
  if(window._googWcmGet){
    try{window._googWcmGet(function(formatted,mobile){
      if(!formatted)return;
      swapped={f:formatted,m:mobile||formatted};applyAll();
    },REAL_DISPLAY);}catch(e){}
  }else if(++tries<40){setTimeout(poll,500);}
})();
})();
(function(){if(!document.body)return;var PID=%s;
var POS=[['.scard','deal-card'],['.pcard','deal-card'],['.itin','deal-card'],['.noresults','deal-card'],['.fares','deal-card'],['.sheet-deal','deal-card'],['.topbar','topbar'],['.callzone','callzone'],['.phoneband','phoneband'],['.sticky-cta','sticky']];
document.addEventListener('click',function(e){
  var a=e.target&&e.target.closest?e.target.closest('a[href^="tel:"]'):null;if(!a)return;
  var pos='other';for(var i=0;i<POS.length;i++){if(a.closest(POS[i][0])){pos=POS[i][1];break;}}
  window.dataLayer=window.dataLayer||[];
  window.dataLayer.push({event:'tel_click',page_id:PID,position:pos});
});})();
(function(){var form=document.querySelector('.cb form');if(!form)return;var PID=%s;
function thanks(mode){
  form.innerHTML='<div class="cb-thanks"><h3>Thank you. We\\'ll call you shortly.</h3>'+
  '<p>An advisor will reach out at the time you chose. Advisors answer 8am-11pm ET, every day.</p></div>';
  window.dataLayer=window.dataLayer||[];
  window.dataLayer.push({event:'lead_submit',page_id:PID,form_mode:mode});
}
form.addEventListener('submit',function(e){
  e.preventDefault();
  var action=form.getAttribute('action')||'';
  if(action.indexOf('http')===0){
    /* URL-ENCODED, not FormData: Apps Script only populates e.parameter for
       application/x-www-form-urlencoded, so a multipart body would land as
       empty columns. Also a "simple" content type, so no CORS preflight. */
    var body=new URLSearchParams();
    var fd=new FormData(form);
    fd.forEach(function(v,k){body.append(k,v);});
    /* page context so each lead row shows which page and which ad variant
       produced it (the sheet has page_id/page_url/lp_variant/lp_when cols) */
    var q=new URLSearchParams(location.search);
    body.append('page_id',PID);
    body.append('page_url',location.href);
    body.append('lp_variant',q.get('v')||'');
    body.append('lp_when',q.get('when')||'');
    /* no-cors: Apps Script 302-redirects to googleusercontent, which the
       browser will not let us read cross-origin. The POST is still
       delivered; a resolved promise means it left the browser. We cannot
       read the script's JSON, so the email alert is the second signal. */
    fetch(action,{method:'POST',mode:'no-cors',body:body})
      .then(function(){thanks('live');})
      .catch(function(){alert('Sorry, that did not send. Please call us instead.');});
  }else{
    /* placeholder action (a bare '#' target): lead is NOT transmitted.
       Thank-you still shows, but form_mode:'placeholder' keeps the event
       distinguishable from real leads in GTM. qa-auditor's placeholder gate
       blocks this from shipping live. */
    thanks('placeholder');
  }
});})();
</script>""" % (json.dumps(final_display), json.dumps(page["page_id"]),
                json.dumps(page["page_id"]))


# ------------------------------------------------------------------ bake

def bake(page, reg, today, used):
    tpl_name = TEMPLATE_BY_TYPE.get(page["page_type"])
    if not tpl_name:
        raise ValueError(f"{page['page_id']}: no template for type {page['page_type']!r}")
    html = (TPL / tpl_name).read_text(encoding="utf-8")

    # finder/itinerary pages carry the full publishable inventory for their
    # filter; ship pages join by ship_id; call-gen pages show 3-6 curated cards
    is_finder = FINDER_RE.search(html) is not None
    is_itin = ITIN_RE.search(html) is not None
    is_ship = SHIP_RE.search(html) is not None
    if is_ship:
        deals = deals_for_ship(page, reg)
    else:
        deals = deals_for(page, reg["itins"], cap=None if (is_finder or is_itin) else 6)
    need = 1 if page["page_type"] in ("itinerary", "ship") else 3
    if len(deals) < need:
        raise ValueError(f"{page['page_id']}: only {len(deals)} publishable deals "
                         f"for filter {page['deal_filter']!r}, needs >={need}")

    priced = [r for r in deals if price_ok(r, today)]
    # the "seen" stamp describes the fares actually shown; if none print,
    # fall back to any stamp so the page still renders honestly
    newest = max((r["date_checked"] for r in priced),
                 default=max((r["date_checked"] for r in deals if r.get("date_checked")),
                             default=today.isoformat()))
    offer_objs = [{
        "text": o["offer_text"], "start": o["start_date"], "end": o["end_date"],
        "endLabel": dt.date.fromisoformat(o["end_date"]).strftime("%b %-d"),
    } for o in offers_for(page, reg["offers"], today)]

    # dataLayer facets: URL segments first; itinerary URLs carry none, so
    # derive from the itinerary row's registered page_targets (never guessed).
    # Ship pages set line + ship only: their intent spans ports/destinations
    # (deployments move), so port/dest stay honestly empty.
    line_slug, port_slug, dest_slug = url_facets(page["url"])
    ship_slug = ""
    if page["page_type"] == "itinerary" and deals:
        t0 = targets_of(deals[0])
        line_slug = line_slug or facet_from_targets(t0, "line:")
        port_slug = port_slug or facet_from_targets(t0, "port:")
        dest_slug = dest_slug or facet_from_targets(t0, "dest:")
    if page["page_type"] == "ship":
        ship_slug = page["slug"]
        srow0 = reg["ships_by_slug"].get(page["slug"], {})
        line_slug = reg["lines_by_id"].get(srow0.get("line_id", ""), {}).get("slug", "")
        port_slug, dest_slug = "", ""
    assets = reg["assets"]

    if RATES_RE.search(html):
        deal_objs = [{
            "name": r["name"],
            "meta": f"{ship_names(r, reg['ship_names'])} · {r['port_label']}",
            "nights": r["nights"],
            "months": r["sail_months"],
            "from": int(r["price_interior"]) if price_ok(r, today) else None,
            "stamp": r["date_checked"],
            "img": f"asset:{r.get('dest', 'theme')}",
        } for r in deals]
        block = (
            "/* ===== RATES DATA — GENERATED by generate.py, DO NOT HAND-EDIT ===== */\n"
            f"const DEALS = {json.dumps(deal_objs, indent=2)};\n"
            f"const OFFERS = {json.dumps(offer_objs, indent=2)};\n"
            "/* ===== END RATES DATA ===== */"
        )
        html = RATES_RE.sub(lambda _: block, html, count=1)
        html = re.sub(r'const pricesCheckedOn = "[^"]*";',
                      f'const pricesCheckedOn = "{month_label(newest)}";', html)
    elif is_finder:
        kind, rest = facet_parts(page["deal_filter"])
        itin_objs = []
        for r in deals:
            obj = {
                "id": r["itin_id"],
                "name": r["name"],
                "ship": ship_names(r, reg["ship_names"]),
                "shipId": r["ship_ids"].split(";")[0].strip(),
                "nights": int(r["nights"]),
                "dest": r["dest"],
                "destLabel": r["dest_label"],
                "months": [m for m in months_of(r, today)
                           if m not in months_without_interior(r)],
                # presentation flag for the mobile featured strip (registry
                # featured column; no content depends on it)
                "featured": r.get("featured", "").strip() == "yes",
                "prices": price_map(r) if price_ok(r, today) else {},
                "noPrice": not price_ok(r, today),
                "days": day_objs(r["itin_id"], reg["days"]),
            }
            obj["img"] = itinerary_card_img(
                assets, obj["days"], r["dest"], used, len(itin_objs),
                itin_objs[-1]["img"]["src"] if itin_objs and itin_objs[-1].get("img") else "")
            # secondary CTA: only itineraries with a registered buildable
            # itinerary page in 09_pages.csv get a detail link
            du = reg["detail_urls"].get(r["slug"])
            if du and du != page["url"]:
                obj["detailUrl"] = du
            itin_objs.append(obj)
        # PORTS lookup for route chips / day expanders (labels, one-line
        # blurbs and currency chips from 05_ports_content)
        port_slugs = {d["p"] for o in itin_objs for d in o["days"]} - {"at-sea"}
        ports_const = {s: port_info(s, reg["ports_by_slug"]) for s in sorted(port_slugs)}
        # ship module: every ship sailing on this page's itinerary set
        ship_ids, ship_list = [], []
        for o in itin_objs:
            if o["shipId"] and o["shipId"] not in ship_ids:
                ship_ids.append(o["shipId"])
        # rotate the licensed GENERIC ship imagery across tabs (real named-ship
        # photos are trade-portal-only; these slots carry trade_portal_upgrade
        # flags in the registry and swap to official photography later).
        # Registry alts never claim a specific ship (operator ruling 2026-07-30).
        ship_img_cycle = ["ship-hero", "ship-bow", "ship-lowangle", "ship-sunset",
                          "ship-aerial", "ship-decks"]
        for idx, sid in enumerate(ship_ids):
            srow = reg["ships_by_id"].get(sid)
            if srow:
                sobj = ship_obj(srow, reg["ship_exp"].get(srow.get("slug", "")))
                img = asset_obj(assets, "ship-generic",
                                ship_img_cycle[idx % len(ship_img_cycle)], "card", used)
                if img:
                    sobj["img"] = img
                ship_list.append(sobj)
        hero = asset_obj(assets, "port", port_slug, "hero", used)
        # know-panel slot reuses the port hero — no second Galveston asset
        # exists in the registry (kept honest, per photo-curator)
        know_img = hero
        port_row = reg["ports_by_slug"].get(port_slug)
        # the finder card renderer reads PAGE.lineLabel and PAGE.portLabel at
        # runtime (T6): labels come from the registries, never guessed
        page_obj = {
            "type": kind, "filter": rest, "h1": page["h1"],
            "line": line_slug, "port": port_slug,
            "lineLabel": reg["line_labels"].get(line_slug, ""),
            "portLabel": deals[0]["port_label"] if deals else "",
        }
        if not page_obj["lineLabel"] or not page_obj["portLabel"]:
            raise ValueError(f"{page['page_id']}: missing lineLabel/portLabel "
                             "for finder PAGE object")
        block = (
            "/* ============================================================\n"
            "   PAGE PARAMS + DATA - GENERATED by generate.py, DO NOT HAND-EDIT\n"
            "   ============================================================ */\n"
            f"const PAGE = {json.dumps(page_obj)};\n"
            f'const PHONE_TEL = "{PHONE_TEL}";\n'
            f'const PHONE_DISPLAY = "{PHONE_DISPLAY}";\n'
            f'const pricesCheckedOn = "{month_label(newest)}";\n'
            # True when the fare-printing rows do NOT share one date_checked:
            # a single list-level stamp would then overstate freshness, so the
            # template falls back to per-card stamps (qa condition N1).
            f"const STAMP_MIXED = {json.dumps(len({r['date_checked'] for r in priced}) > 1)};\n"
            # ?v= H1 variants, generated from the page's OWN inventory so a
            # variant can never claim a ship or length the page cannot serve.
            # Ad groups pass ?v=<ship-slug> or ?v=<n>night to mirror the query.
            f"const H1_VARIANTS = {json.dumps(h1_variants(deals, reg, page))};\n"
            # ?v=<ship> must narrow the list too, so the headline's promise and
            # the sailings shown agree. Maps variant key -> ship_id.
            f"const SHIP_SLUGS = {json.dumps(ship_slug_map(deals, reg))};\n"
            f'const H1_BASE = {json.dumps(page["h1"])};\n'
            f"const HERO = {json.dumps(hero)};\n"
            f"const KNOW_IMG = {json.dumps(know_img)};\n"
            f"const PRE_CRUISE = {json.dumps(pre_cruise_obj(port_row))};\n"
            f"const DOCS_SUMMARY = {json.dumps(docs_summary(reg['faqs']))};\n"
            f"const PORTS = {json.dumps(ports_const)};\n"
            f"const SHIPS = {json.dumps(ship_list, indent=1)};\n"
            f"const ITINERARIES = {json.dumps(itin_objs, indent=1)};\n"
            f"const FAQS = {json.dumps(faqs_for(page, deals, reg['faqs']), indent=1)};\n"
            f"const OFFERS = {json.dumps(offer_objs, indent=2)};\n"
            "/* ================== END GENERATED DATA ====================== */"
        )
        html = FINDER_RE.sub(lambda _: block, html, count=1)
    elif is_itin:
        r = deals[0]
        days = day_objs(r["itin_id"], reg["days"])
        if not days:
            raise ValueError(f"{page['page_id']}: no day rows in "
                             f"04_itinerary_days.csv for {r['itin_id']}")
        # photo-story layout: every day carries a registry -section image
        # (port days = that port's asset, sea days rotate generic subjects)
        days = journey_images(days, assets, used)
        port_slugs = {d["p"] for d in days} - {"at-sea"}
        ports_const = {s: port_info(s, reg["ports_by_slug"]) for s in sorted(port_slugs)}
        ship_id = r["ship_ids"].split(";")[0].strip()
        srow = reg["ships_by_id"].get(ship_id)
        if not srow:
            raise ValueError(f"{page['page_id']}: ship {ship_id} not in 02_ships.csv")
        ds = reg["ship_exp"].get(srow.get("slug", ""))
        ship = ship_obj(srow, ds)
        # generic registry image only (no line livery); alt stays honest
        ship["img"] = asset_obj(assets, "ship-generic", "deck-scene", "card", used)
        # condensed dataset tabs (at-a-glance / dining / family / nightlife)
        ship["tabs"] = ship_tabs(ds, assets, used)
        hero = (asset_obj(assets, "port", r["port_slug"], "hero", used)
                or asset_obj(assets, "ship-generic", "ship-at-sea", "hero", used))
        line_row = reg["lines_by_id"].get(r["line_id"], {})
        ov = parse_overrides(r)
        i_def = int(r["price_interior"])
        b_def = int(r["price_balcony"]) if r.get("price_balcony", "").strip() else None
        no_int = months_without_interior(r)
        month_list = months_of(r, today)
        months = [{"m": m,
                   "i": None if m in no_int else ov.get(m, {}).get("i", i_def),
                   "b": ov.get(m, {}).get("b", b_def)}
                  for m in month_list]
        page_obj = {
            "type": "itinerary", "id": page["page_id"], "h1": page["h1"],
            "name": r["name"], "nights": int(r["nights"]),
            "line": line_slug, "port": port_slug, "dest": dest_slug,
            "lineLabel": line_row.get("line_name", "") or reg["line_labels"].get(line_slug, ""),
            "portLabel": r["port_label"], "destLabel": r["dest_label"],
            "shipName": ship["name"], "oneWay": "one-way" in r.get("notes", "").lower(),
        }
        if not page_obj["lineLabel"] or not page_obj["portLabel"]:
            raise ValueError(f"{page['page_id']}: missing lineLabel/portLabel "
                             "for itinerary PAGE object")
        booking = {
            "taxes": r.get("taxes_note", ""),
            "privateIsland": r.get("private_island", "") == "yes",
            # structured tiers for the 2-col deposits mini table (item 7)
            "deposit": deposit_struct(line_row.get("deposit_note", "")),
            "kids": line_row.get("kids_policy", ""),
            "season": r.get("season_note", ""),
        }
        block = (
            "/* ============================================================\n"
            "   ITINERARY PAGE DATA - GENERATED by generate.py, DO NOT HAND-EDIT\n"
            "   ============================================================ */\n"
            f"const PAGE = {json.dumps(page_obj)};\n"
            f'const PHONE_TEL = "{PHONE_TEL}";\n'
            f'const PHONE_DISPLAY = "{PHONE_DISPLAY}";\n'
            f'const STAMP = "{r["date_checked"]}";\n'
            f'const pricesCheckedOn = "{month_label(newest)}";\n'
            f"const HERO = {json.dumps(hero)};\n"
            f"const SHIP = {json.dumps(ship, indent=1)};\n"
            f"const DAYS = {json.dumps(days)};\n"
            f"const PORTS = {json.dumps(ports_const)};\n"
            f"const MONTHS = {json.dumps(months)};\n"
            f"const WHEN_LINES = {json.dumps(when_lines(month_list))};\n"
            f"const BOOKING = {json.dumps(booking)};\n"
            f"const FAQS = {json.dumps(faqs_for(page, deals, reg['faqs']), indent=1)};\n"
            f"const OFFERS = {json.dumps(offer_objs, indent=2)};\n"
            "/* ================== END GENERATED DATA ====================== */"
        )
        html = ITIN_RE.sub(lambda _: block, html, count=1)
    elif is_ship:
        srow = reg["ships_by_slug"].get(page["slug"])
        # ship provenance gate: a verified 02_ships row with an official
        # source AND a newsite-dataset entry (the page renders dataset facts)
        if not srow or srow.get("status") != "verified" \
                or not srow.get("source", "").startswith("http"):
            raise ValueError(f"{page['page_id']}: ship row for {page['slug']!r} "
                             "is not verified with an official source")
        ds = reg["ship_exp"].get(page["slug"])
        if not ds:
            raise ValueError(f"{page['page_id']}: {page['slug']!r} not in the "
                             "newsite ships dataset")
        exp = ds.get("exp") or {}
        line_row = reg["lines_by_id"].get(srow["line_id"], {})
        dining = exp.get("dining") or []
        bars, shows = venue_split(exp.get("entertainment"))
        # fare basis: only when the note is uniform across this ship's
        # publishable rows (never a merged claim)
        taxes_notes = {r.get("taxes_note", "").strip() for r in deals}
        taxes = taxes_notes.pop() if len(taxes_notes) == 1 else ""
        kids_text = exp.get("kids_bands") if isinstance(exp.get("kids_bands"), str) else ""
        kids_text = kids_text or family_line(exp)
        cab = exp.get("cabins") or {}
        # casino contract: key absent -> section omitted entirely; key present
        # with null name -> the template renders ONE honest line (registrar
        # recorded the gap deliberately; never invent a venue name)
        casino = ({"name": (exp.get("casino") or {}).get("name"),
                   "desc": (exp.get("casino") or {}).get("desc")}
                  if "casino" in exp else None)
        sailings = []
        for r in deals:
            obj = {
                "id": r["itin_id"], "name": r["name"], "nights": int(r["nights"]),
                "portLabel": r["port_label"],
                "months": months_of(r, today),
                "from": int(r["price_interior"]) if price_ok(r, today) else None,
                "stamp": r["date_checked"],
                # a SHIP page's sailing cards show the ship, not a beach
                # (operator ruling 2026-07-30); rotate the real-ship pool
                "img": ship_card_img(assets, used, len(sailings)),
                "days": day_objs(r["itin_id"], reg["days"]),
                "oneWay": "one-way" in r.get("notes", "").lower(),
            }
            du = reg["detail_urls"].get(r["slug"])
            if du and du != page["url"]:
                obj["detailUrl"] = du
            sailings.append(obj)
        port_slugs = {d["p"] for s_ in sailings for d in s_["days"]} - {"at-sea"}
        ports_const = {s: port_info(s, reg["ports_by_slug"]) for s in sorted(port_slugs)}
        page_obj = {
            "type": "ship", "id": page["page_id"], "h1": page["h1"],
            "shipName": srow["ship_name"], "cls": srow.get("class_or_note", ""),
            "tier": srow.get("size_tier", ""),
            "line": line_slug, "ship": ship_slug,
            "lineLabel": line_row.get("line_name", ""),
        }
        if not page_obj["lineLabel"]:
            raise ValueError(f"{page['page_id']}: missing lineLabel for ship PAGE object")
        glance = {"cls": srow.get("class_or_note", ""), "year": ds.get("year"),
                  "tonnage": ds.get("tonnage"), "guests": ds.get("guests"),
                  "features": ds.get("features") or [],
                  "overview": exp.get("overview", ""),
                  "whoFor": exp.get("who_for", "")}
        included = {
            "taxes": taxes,
            # structured tiers for the 2-col deposits mini table (item 7)
            "deposit": deposit_struct(line_row.get("deposit_note", "")),
            "kids": line_row.get("kids_policy", ""),
            "incDining": [v.get("name", "") for v in dining if not v.get("extra")],
            "extraDining": [v.get("name", "") for v in dining if v.get("extra")],
        }
        cabins = {"categories": cab.get("categories") or [],
                  "note": public_note(cab.get("quad_note", ""))}
        # themed section images per the photo-story spec; at-a-glance and
        # thin sections carry no photo (they render honestly small)
        imgs = {
            "dining": asset_obj(assets, "ship-generic", "dining", "section", used),
            "bars": asset_obj(assets, "ship-generic", "lounge-bar", "section", used),
            "activities": (asset_obj(assets, "ship-generic", "ship-sports", "section", used)
                           or asset_obj(assets, "ship-generic", "deck-scene", "section", used)),
            "kids": (asset_obj(assets, "ship-generic", "ship-waterslide", "section", used)
                     or asset_obj(assets, "theme", "waterslide", "section", used)),
            "spa": (asset_obj(assets, "ship-generic", "ship-interior", "section", used)
                    or asset_obj(assets, "theme", "spa", "section", used)),
            "cabins": (asset_obj(assets, "ship-generic", "ship-balcony", "section", used)
                       or asset_obj(assets, "ship-generic", "sea-day", "section", used)),
        }
        hero = (asset_obj(assets, "ship-generic", "ship-hero", "hero", used)
            or asset_obj(assets, "ship-generic", "ship-at-sea", "hero", used))
        block = (
            "/* ============================================================\n"
            "   SHIP PAGE DATA - GENERATED by generate.py, DO NOT HAND-EDIT\n"
            "   ============================================================ */\n"
            f"const PAGE = {json.dumps(page_obj)};\n"
            f'const PHONE_TEL = "{PHONE_TEL}";\n'
            f'const PHONE_DISPLAY = "{PHONE_DISPLAY}";\n'
            f'const STAMP = "{newest}";\n'
            f'const pricesCheckedOn = "{month_label(newest)}";\n'
            f"const HERO = {json.dumps(hero)};\n"
            f"const GLANCE = {json.dumps(glance)};\n"
            f"const INCLUDED = {json.dumps(included)};\n"
            f"const DINING = {json.dumps(dining, indent=1)};\n"
            f"const CABINS = {json.dumps(cabins)};\n"
            f"const BARS = {json.dumps(bars, indent=1)};\n"
            f"const SHOWS = {json.dumps(shows, indent=1)};\n"
            f"const CASINO = {json.dumps(casino)};\n"
            f"const ACTIVITIES = {json.dumps(exp.get('activities') or [], indent=1)};\n"
            f"const KIDS = {json.dumps(kids_text)};\n"
            f"const SPA = {json.dumps(exp.get('spa') or None)};\n"
            f"const SHOPPING = {json.dumps(exp.get('shopping') or None)};\n"
            f"const IMGS = {json.dumps(imgs)};\n"
            f"const SAILINGS = {json.dumps(sailings, indent=1)};\n"
            f"const PORTS = {json.dumps(ports_const)};\n"
            f"const FAQS = {json.dumps(faqs_for(page, deals, reg['faqs']), indent=1)};\n"
            f"const OFFERS = {json.dumps(offer_objs, indent=2)};\n"
            "/* ================== END GENERATED DATA ====================== */"
        )
        html = SHIP_RE.sub(lambda _: block, html, count=1)
    else:
        raise ValueError(f"{tpl_name}: no recognized generated-data block")

    # phone + brand slots; the final numbers are the DNI module's canonical
    # format (one source of truth for what Google's callback replaces)
    html = (html.replace("+18335550100", PHONE_TEL)
                .replace("1-833-555-0100", PHONE_DISPLAY)
                .replace("[AGENCY NAME]", AGENCY_NAME))
    final_tel, final_display = PHONE_TEL, PHONE_DISPLAY
    # tracking-number override per page, when assigned in 09_pages.csv
    if page.get("tracking_number"):
        digits = re.sub(r"\D", "", page["tracking_number"])
        final_tel, final_display = f"+{digits}", page["tracking_number"]
        html = html.replace(PHONE_TEL, final_tel).replace(PHONE_DISPLAY, final_display)

    # H1 + title from the registry (query-mirroring, one intent per page)
    html = re.sub(r"<h1>.*?</h1>", f"<h1>{page['h1']}</h1>", html, count=1, flags=re.S)
    html = re.sub(r"<title>.*?</title>",
                  f"<title>{page['h1']} | {AGENCY_NAME}</title>", html, count=1, flags=re.S)

    if 'name="robots" content="noindex' not in html:
        html = html.replace("<head>", '<head>\n<meta name="robots" content="noindex,nofollow">', 1)

    # shared legal footer (operator ruling): replace the template's footer
    # with the partial-sourced compact block; link the TCPA consent line
    html = re.sub(r"<footer>.*?</footer>", lambda _: lp_footer_html(final_tel, final_display),
                  html, count=1, flags=re.S)
    html = html.replace(CONSENT_SENTENCE, CONSENT_LINKED)
    html = html.replace("#CALLBACK_ACTION", CALLBACK_ACTION)

    # main-site logo lockup in the slim header (operator ruling 2026-07-30)
    brand = lp_brand_html()
    html = re.sub(r'<span class="brand">[^<]*</span>', lambda _: brand, html, count=1)
    html = html.replace("</head>", BRAND_CSS + "\n</head>", 1)
    # back-to-top + conditional header Back button (operator ruling 2026-07-30)
    html = html.replace("</body>", NAV_UI_JS + "\n</body>", 1)

    # tracking stack — identical to the main site (GTM + Clarity direct;
    # GA4/Ads fire inside the GTM container). noindex has no effect on tags.
    gtm_id, clarity_id = _site_tag_ids()
    head_block = tracking_head(page, gtm_id, clarity_id,
                               (line_slug, port_slug, dest_slug, ship_slug))
    viewport = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    if viewport in html:
        html = html.replace(viewport, viewport + "\n" + head_block, 1)
    else:
        html = html.replace("<head>", "<head>\n" + head_block, 1)
    html = html.replace("<body>", "<body>\n" + tracking_noscript(gtm_id), 1)
    html = html.replace("</body>", tracking_events(page, final_tel, final_display) + "\n</body>", 1)
    return html


def load_registries():
    pages = read_csv(DATA / "09_pages.csv")
    ships_rows = read_csv(DATA / "02_ships.csv")
    return {
        "itins": read_csv(DATA / "03_itineraries.csv"),
        "offers": read_csv(DATA / "07_offers.csv"),
        "days": read_csv(DATA / "04_itinerary_days.csv"),
        "faqs": read_csv(DATA / "08_faqs.csv"),
        "assets": read_csv(DATA / "10_assets.csv"),
        "ship_names": {r["ship_id"]: r["ship_name"] for r in ships_rows},
        "ships_by_id": {r["ship_id"]: r for r in ships_rows},
        "ships_by_slug": {r["slug"]: r for r in ships_rows},
        # newsite ships dataset (single source of ship experience facts,
        # shared with the live site), keyed by slugified ship name
        "ship_exp": load_ship_dataset(),
        "ports_by_slug": {r["port_slug"]: r for r in read_csv(DATA / "05_ports_content.csv")},
        "line_labels": {r["slug"]: r["line_name"] for r in read_csv(DATA / "01_lines.csv")},
        "lines_by_id": {r["line_id"]: r for r in read_csv(DATA / "01_lines.csv")},
        # itinerary slug -> registered buildable itinerary page URL
        "detail_urls": {p["slug"]: p["url"] for p in pages
                        if p.get("page_type") == "itinerary"
                        and p.get("status") in BUILDABLE},
        "pages": pages,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", help="build only this page_id")
    ap.add_argument("--deploy-dir", default=None,
                    help="write into this served tree (e.g. 'site'); default is lp-system/out/preview")
    args = ap.parse_args()

    today = dt.date.today()
    reg = load_registries()

    out_root = (ROOT / args.deploy_dir) if args.deploy_dir else (ROOT / "lp-system" / "out" / "preview")
    built, errors = 0, 0
    used = {}  # rel path under img/ -> source file; copied once after bakes
    for page in reg["pages"]:
        if args.page and page["page_id"] != args.page:
            continue
        if not args.page and page.get("status") not in BUILDABLE:
            continue
        try:
            html = bake(page, reg, today, used)
        except ValueError as e:
            print(f"SKIP: {e}")
            errors += 1
            continue
        dest = out_root / page["url"].strip("/") / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        print(f"built {page['page_id']} -> {dest.relative_to(ROOT)}")
        built += 1
    for rel, srcp in sorted(used.items()):
        dst = out_root / "img" / "lp" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(srcp, dst)
        print(f"asset {srcp.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
    print(f"\n{built} page(s) built, {errors} skipped, {len(used)} asset file(s) copied.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
