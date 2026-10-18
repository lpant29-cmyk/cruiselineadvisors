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
empty_pages=""
for pg in "${LP_PAGES[@]}"; do
  if out=$(python3 lp-system/scripts/generate.py --page "$pg" --deploy-dir site 2>&1); then
    echo "$out"
  else
    echo "$out"
    if echo "$out" | grep -q "SKIP: $pg: only 0 publishable deals"; then
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
  f=$( { grep -rl "\"page_id\": \"$pg\"" "$ROOT/site" 2>/dev/null || true; } | head -1)
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
print("%d of %d" % (sum(1 for r in rows if not g.price_ok(r)), len(rows)))
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
