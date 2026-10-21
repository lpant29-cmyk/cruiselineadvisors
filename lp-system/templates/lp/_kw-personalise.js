/* ?kw= personalisation, shared by every /go/ template.

   Google ValueTrack passes the searcher's own query as ?kw=. Echoing it as the
   H1 lifts ad relevance, and it is also the single easiest way to publish a
   sentence nobody wrote and nobody can stand behind. So this is a gate, not a
   feature: the keyword has to earn its way onto the page.

   Order of the checks is load-bearing. Everything is tested against the RAW
   parameter BEFORE any character stripping, because the sanitiser turns % and
   $ into spaces, and testing afterwards let "50% off" through as "50 off".

   The module only ever writes textContent, never innerHTML.

   Reads two generated constants, so one page's own line is allowed and every
   other line is not:
     KW_OWN    tokens for THIS page's line, stripped before content matching
     KW_OTHER  every other line's name, blocked outright
   Exposes window.__kwAccepted: the cleaned keyword, or null if rejected. */
(function () {
  window.__kwAccepted = null;
  var q;
  try { q = new URLSearchParams(location.search); } catch (e) { return; }
  var raw = q.get("kw") || "";
  if (!raw) return;

  /* PHONE INTENT. Someone searching "royal caribbean phone number" wants the
     cruise line's switchboard. Echoing that into our H1 makes this page look
     like it, which is precisely the impression the footer disclaimer exists to
     prevent, on the keywords where it is most expensive to be wrong. These
     never personalise; the page keeps the headline it shipped with. */
  var BAD_PHONE = /(\bphones?\b|\bnumbers?\b|\bcontact|\bcall(ing)?\b|\b800\b|\btoll[\s-]?free|\bhelp\s?line|\bhelpline|\bsupport\b|\blive person|\btalk to\b|\bspeak to\b|\brepresentative)/i;
  if (BAD_PHONE.test(raw)) return;

  /* Money and superlative claims we cannot support. No \b before the symbol
     alternatives: \b needs a word character to its left, which made \$
     unmatchable at the start of a string. */
  var BAD_KW = /(\bcheap|\bcheapest|\blowest|\bfree\b|\bguarantee|\bdiscount|\bdeal of\b|\ball[\s-]inclusive|%|\$|\bsave\b|\bper person\b)/i;

  /* Affiliation and identity claims. We are a referral service and say so on
     every page; echoing "official site" into our own H1 contradicts that and is
     trademark exposure on brand keywords. */
  var BAD_AFFIL = /\b(official|officially|authorized|authorised|accredited|partner|direct|agent|agency|reservations?|customer (service|care)|headquarters|corporate|complaints?|refunds?)\b/i;

  if (BAD_KW.test(raw) || BAD_AFFIL.test(raw)) return;

  /* OTHER lines only. This used to block every line name on every page, so a
     Carnival ad landing on the Carnival page could not use its own keyword.
     A page may echo its own line; it may never echo a competitor it has no
     inventory for. */
  var other = (typeof KW_OTHER !== "undefined" && KW_OTHER) ? KW_OTHER : [];
  for (var i = 0; i < other.length; i++) {
    if (new RegExp("\\b" + other[i].replace(/[-/\\^$*+?.()|[\]{}]/g, "\\$&") + "\\b", "i").test(raw)) return;
  }

  var kw = raw.replace(/[+_]/g, " ").replace(/[^A-Za-z0-9 '’-]/g, " ")
              .replace(/\s+/g, " ").trim().slice(0, 70);
  if (!kw || BAD_KW.test(kw) || BAD_AFFIL.test(kw)) return;

  var SMALL = /^(a|an|and|the|from|to|for|of|on|in|by|at|with|out)$/i;
  var title = kw.split(" ").map(function (w, i) {
    if (/^(rccl|ncl|msc|usa|tx|fl|ny|nj|ca|wa|la)$/i.test(w)) return w.toUpperCase();
    if (i > 0 && SMALL.test(w)) return w.toLowerCase();
    return w.charAt(0).toUpperCase() + w.slice(1);
  }).join(" ");

  var h1 = document.querySelector("h1");
  if (h1) h1.textContent = title;

  /* Strip this page's own line name before any content matching: on the Royal
     Caribbean page "royal CARIBBEAN" would otherwise match the Caribbean
     destination and hide almost every sailing. */
  var low = kw.toLowerCase();
  var own = (typeof KW_OWN !== "undefined" && KW_OWN) ? KW_OWN : [];
  for (var j = 0; j < own.length; j++) {
    low = low.split(own[j]).join(" ");
  }
  window.__kwAccepted = { kw: kw, title: title, low: low.replace(/\s+/g, " ").trim() };
})();
