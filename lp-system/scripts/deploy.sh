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

LP_PAGES=("p002" "p007" "p008")   # the live /go/ pages

echo "==> 1/4  main site"
( cd newsite && python3 build.py )

echo "==> 2/4  copy dist -> site/"
rm -rf "$ROOT/site"
mkdir -p "$ROOT/site"
cp -R "$ROOT/newsite/dist/." "$ROOT/site/"

echo "==> 3/4  /go/ landing pages"
for pg in "${LP_PAGES[@]}"; do
  python3 lp-system/scripts/generate.py --page "$pg" --deploy-dir site
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
  f=$( { grep -rl "\"page_id\": \"$pg\"" "$ROOT/site" 2>/dev/null || true; } | head -1)
  [ -z "$f" ] && { echo "  FAIL $pg not found in site/"; fail=1; continue; }
  grep -q 'name="robots" content="noindex' "$f" || { echo "  FAIL $pg missing noindex"; fail=1; }
  if grep -q "1-833-555-0100" "$f"; then echo "  FAIL $pg still has the placeholder phone"; fail=1; fi
  if grep -q "#CALLBACK_ACTION" "$f"; then echo "  FAIL $pg still has the placeholder form action"; fail=1; fi
  if grep -q "IMG SLOT" "$f"; then echo "  FAIL $pg has an unresolved image slot"; fail=1; fi
  if grep -q "AGENCY NAME" "$f"; then echo "  FAIL $pg has an unresolved brand placeholder"; fail=1; fi
done
[ "$fail" = "0" ] && echo "  ok   all $((${#LP_PAGES[@]})) LP pages: noindex, real phone, real form action, no placeholders"

# fares must be fresh: generate.py withholds a stale price, but if EVERY
# fare on a page is withheld that is a broken pipeline, not a safe default
withheld=$( { grep -ro "Fare on request" "$ROOT/site" 2>/dev/null || true; } | wc -l | tr -d ' ')
echo "  note $withheld fare(s) currently withheld as unstable/stale"

echo
if [ "$fail" != "0" ]; then
  echo "DEPLOY BLOCKED: fix the FAIL lines above."
  exit 1
fi
echo "Built and checked. Nothing committed."
echo "Next:  git add -A && git commit   then push (Render deploys main)."
