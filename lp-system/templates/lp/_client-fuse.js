/* ---- CLIENT FUSE ------------------------------------------------------------
   Injected into every /go/ page that prints a fare. generate.py reads this
   file and substitutes __MAX_AGE__ from PRICE_MAX_AGE_DAYS, so there is one
   number and one copy of this logic.

   WHY THIS EXISTS
   price_ok() in generate.py decides what gets printed when the page is BUILT,
   and for a long time that was the only gate. A deployed page expires nothing
   by itself: the moment a refresh is missed it keeps serving the same figures
   under the same stamp, looking exactly as current as the day it was built. On
   2026-10-20 the live Galveston page was still showing a 4-night interior at
   557 that the line had repriced to 348.55, and a 5-night sailing that had
   already left port, because nothing had rebuilt it since the 16th.

   This reads each row's own stamp against the VISITOR's clock, so a page that
   stops being rebuilt degrades to "Fare on request" on its own rather than
   going quietly wrong.

   IT CAN ONLY REMOVE A FARE. There is no path here that prints a number the
   build withheld. It writes to the same fields the templates already use for
   a missing fare (noPrice / prices / from / a month's i and b), so the
   fallback copy a visitor sees is copy that was already written and reviewed
   for that case.

   Runs inside its own IIFE with a guard on every global it touches: a page
   carries one of these data shapes, never all of them, and a bare reference
   to a missing one would throw and kill every later script on the page
   (CLAUDE.md, known pitfall 1).
   -------------------------------------------------------------------------- */
(function () {
  var MAX_AGE = __MAX_AGE__;
  var now = new Date();
  var live = [];
  var withheld = 0;

  function stale(s) {
    if (!s) return false;                        // no stamp, not ours to judge
    var d = new Date(s + "T00:00:00");
    if (isNaN(d.getTime())) return false;        // unparseable, leave it alone
    return Math.floor((now - d) / 86400000) > MAX_AGE;
  }

  function strip(o) {
    if (!o || typeof o !== "object") return;
    if (!stale(o.stamp)) {
      if (o.stamp) live.push(o.stamp);
      return;
    }
    if (!o.noPrice) withheld++;        // count what THIS pass removed
    o.noPrice = true;
    o.prices = {};
    o.from = null;
  }

  // the list shapes generate.py emits, one per page type
  if (typeof ITINERARIES !== "undefined" && Array.isArray(ITINERARIES)) {
    ITINERARIES.forEach(strip);
  }
  if (typeof SAILINGS !== "undefined" && Array.isArray(SAILINGS)) {
    SAILINGS.forEach(strip);
  }
  if (typeof DEALS !== "undefined" && Array.isArray(DEALS)) {
    DEALS.forEach(strip);
  }

  // a single-itinerary page carries one STAMP covering its whole month table
  if (typeof STAMP !== "undefined" && stale(STAMP) &&
      typeof MONTHS !== "undefined" && Array.isArray(MONTHS)) {
    MONTHS.forEach(function (m) {
      if (m) { m.i = null; m.b = null; }
    });
    withheld++;
  }

  // The fine print must not outlive the fares it describes. Rather than blank
  // the stamp (which leaves a dangling "seen " at every interpolation site),
  // expose the state and let the four list-level strings ask. Per-card copy
  // already branches on noPrice / from == null and needs nothing.
  window.__fareFuse = { withheld: withheld, anyLive: live.length > 0 };

  // the one question the list-level fine print needs to ask
  window.__faresShown = function () {
    return !window.__fareFuse || window.__fareFuse.anyLive;
  };
})();
