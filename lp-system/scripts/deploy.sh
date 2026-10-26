#!/usr/bin/env bash
# deploy.sh — build the main site + the /go/ ad landing pages into the
# served tree (site/), in the one order that works.
#
# ORDER MATTERS: newsite/build.py writes to newsite/dist, which is copied
# over site/ wholesale. The LP pages must be generated AFTER that copy, or
# the copy deletes them.
#
# This script does NOT commit and does NOT push. Review `git status`, then
# commit and push yourself. Render auto-deploys `main`.
#
# Usage: bash lp-system/scripts/deploy.sh

set -euo pipefail
cd "$(dirname "$0")/../.."
ROOT="$PWD"

# The live /go/ pages come from the registry, not from a list in this script,
# so retiring one is a one-word data edit (status=retired in 09_pages.csv) the
# way every other fact in this system is a data edit. Hardcoding them here
# meant a page that lost its inventory hard-failed the whole deploy, taking
# the healthy pages down with it.
# read with a while loop, not mapfile: macOS still ships bash 3.2 and this
# script has to run both there and on the scheduler's ubuntu runner
lp_page_list=$(python3 - <<'PYLIST'
import csv
with open("lp-system/data/09_pages.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["status"].strip() in ("building", "live"):
            print(r["page_id"])
PYLIST
)
LP_PAGES=()
while IFS= read -r pg; do
  [ -n "$pg" ] && LP_PAGES+=("$pg")
done <<< "$lp_page_list"
[ "${#LP_PAGES[@]}" -gt 0 ] || { echo "FAIL no live pages in 09_pages.csv"; exit 1; }
echo "live /go/ pages: ${LP_PAGES[*]}"

echo "==> 1/4  main site"
( cd newsite && python3 build.py )

echo "==> 2/4  copy dist -> site/"
rm -rf "$ROOT/site"
mkdir -p "$ROOT/site"
cp -R "$ROOT/newsite/dist/." "$ROOT/site/"

echo "==> 3/4  /go/ landing pages"
# generate.py exits non-zero when it SKIPs a page, and a skip for want of
# publishable inventory is a CORRECT refusal: better no page than a page of
# empty inventory. Under set -e that refusal used to abort the loop, so one
# dead page stopped every later page from being rebuilt at all. Record it and
# carry on; the page still gets reported, loudly, at step 4.
#
# The match is "only N publishable deals" for ANY N, not just zero. It used to
# be pinned to zero, and generate.py prints the number it actually found, so a
# category page that still had one or two rows but needs three printed "only 1
# publishable deals", missed the match, and took the whole deploy down through
# the FAIL branch below. That is the opposite of what this loop is for, and it
# becomes reachable exactly when a season winds down and inventory thins out,
# which is the moment the refresh most needs to keep running. p006 sits at 1
# row against a need of 3 today and would do it again the day it goes live.
empty_pages=""
for pg in "${LP_PAGES[@]}"; do
  if out=$(python3 lp-system/scripts/generate.py --page "$pg" --deploy-dir site 2>&1); then
    echo "$out"
  else
    echo "$out"
    if echo "$out" | grep -qE "SKIP: $pg: only [0-9]+ publishable deals"; then
      empty_pages="$empty_pages $pg"
    else
      echo "  FAIL generate.py could not build $pg"; exit 1
    fi
  fi
done

echo "==> 4/4  pre-deploy checks"
fail=0

# the LP layer must stay invisible to organic search
if grep -qi "disallow: */en/go" "$ROOT/site/robots.txt" 2>/dev/null; then
  echo "  FAIL robots.txt blocks /go/ (that HIDES the noindex tag from Google)"; fail=1
else
  echo "  ok   robots.txt does not block /go/"
fi

if grep -q "/go/" "$ROOT/site/sitemap.xml" 2>/dev/null; then
  echo "  FAIL /go/ URLs found in sitemap.xml"; fail=1
else
  echo "  ok   no /go/ URLs in sitemap"
fi

# No page may promise a better/exclusive/unpublished rate from calling us.
# newsite/build.py already ran this over the whole main site in step 1, and
# site/ is that build plus the /go/ pages. So this run covers ONLY /go/, which
# is generated after that build and is where the wording keeps coming back.
# Pointing it at all of site/ re-scanned 539 pages that were just cleared and
# put another minute on every deploy for nothing.
if python3 "$ROOT/newsite/rate_claim_guard.py" "$ROOT/site/en/go" > /tmp/rate_claim_guard.out 2>&1; then
  echo "  ok   no better/exclusive/unpublished rate claims"
else
  echo "  FAIL rate-claim guard:"; sed 's/^/       /' /tmp/rate_claim_guard.out; fail=1
fi

inbound=$( { grep -rl "/en/go/" "$ROOT/site" 2>/dev/null || true; } | { grep -v "/go/" || true; } | wc -l | tr -d ' ')
if [ "$inbound" != "0" ]; then
  echo "  FAIL $inbound main-site file(s) link into /go/"; fail=1
else
  echo "  ok   no inbound links from the main site into /go/"
fi

for pg in "${LP_PAGES[@]}"; do
  case " $empty_pages " in
    *" $pg "*)
      # An ad group is still pointing at this URL and Render never prunes, so
      # the previously published copy stays served until the ads are paused.
      # That is the only thing that actually takes it out of circulation.
      echo "  GAP  $pg has no publishable inventory and was not rebuilt."
      echo "       PAUSE ITS AD GROUPS. The old copy stays served until you do."
      echo "       Then set status=retired for $pg in 09_pages.csv."
      continue ;;
  esac
  # The page's own URL from the registry, not a grep of the whole tree: that
  # grep walked 220MB once PER PAGE, and at 18 pages it was several minutes of
  # every deploy. The registry is the source of truth for where a page lives.
  u=$(python3 - "$pg" <<'PYURL'
import csv, sys
for r in csv.DictReader(open("lp-system/data/09_pages.csv", encoding="utf-8")):
    if r["page_id"] == sys.argv[1]:
        print(r["url"].strip("/")); break
PYURL
)
  f="$ROOT/site/$u/index.html"
  [ -f "$f" ] || f=$( { grep -rl "\"page_id\": \"$pg\"" "$ROOT/site" 2>/dev/null || true; } | head -1)
  if [ -z "$f" ]; then
    echo "  FAIL $pg not found in site/"; fail=1; continue
  fi
  grep -q 'name="robots" content="noindex' "$f" || { echo "  FAIL $pg missing noindex"; fail=1; }
  if grep -q "1-833-555-0100" "$f"; then echo "  FAIL $pg still has the placeholder phone"; fail=1; fi
  if grep -q "#CALLBACK_ACTION" "$f"; then echo "  FAIL $pg still has the placeholder form action"; fail=1; fi
  if grep -q "IMG SLOT" "$f"; then echo "  FAIL $pg has an unresolved image slot"; fail=1; fi
  if grep -q "AGENCY NAME" "$f"; then echo "  FAIL $pg has an unresolved brand placeholder"; fail=1; fi
done
[ "$fail" = "0" ] && echo "  ok   LP pages checked: noindex, real phone, real form action, no placeholders"

# fares must be fresh: generate.py withholds a stale price, but if EVERY
# fare on a page is withheld that is a broken pipeline, not a safe default
# Counted from the DATA via generate.py's own price_ok(), not by grepping the
# built HTML: fares render client-side, so the only "Fare on request" strings
# in site/ are the JS fallback branches themselves. Grepping them always
# returned a floor of 2 and could never see a genuinely withheld card, which
# silently defeated the "did the refresh actually work" check.
withheld=$(cd "$ROOT" && python3 - <<'PYEOF'
import sys, pathlib
sys.path.insert(0, str(pathlib.Path("lp-system/scripts").resolve()))
import generate as g
rows = [r for r in g.read_csv(pathlib.Path("lp-system/data/03_itineraries.csv"))
        if r.get("itin_id", "").startswith("i")]
if not rows:
    raise SystemExit("ERR no itinerary rows parsed")
# Rows from a SAILINGS-ONLY source (the Carnival feed) carry no fare by ruling,
# so counting them as "withheld" buries the signal this check exists for: a
# number that is always huge is a number nobody reads. They are reported
# separately instead.
priced = [r for r in rows if "no-price source" not in (r.get("auto_status") or "")]
nofare = len(rows) - len(priced)
print("%d of %d%s" % (sum(1 for r in priced if not g.price_ok(r)), len(priced),
                      (" (+%d sailings-only rows that carry no fare by design)" % nofare)
                      if nofare else ""))
PYEOF
)
case "$withheld" in
  ""|ERR*) echo "  FAIL could not compute the withheld-fare count ($withheld)"; fail=1 ;;
  *)       echo "  note $withheld fare(s) withheld as unstable/stale" ;;
esac

echo
if [ "$fail" != "0" ]; then
  echo "DEPLOY BLOCKED: fix the FAIL lines above."
  exit 1
fi
if [ -n "$empty_pages" ]; then
  echo "NOTE: no inventory left for:$empty_pages"
  echo "      The healthy pages were built and checked. Pause those ad groups."
fi
echo "Built and checked. Nothing committed."
echo "Next:  git add -A && git commit   then push (Render deploys main)."
