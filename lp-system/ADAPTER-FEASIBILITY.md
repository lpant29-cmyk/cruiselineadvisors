# Fare adapter feasibility, 10 lines

Phase 1 deliverable, 2026-10-20. **No adapter is built from this file without
operator approval.** It records what was actually verified, what was not, and
the one step that unblocks the rest.

## Summary

| Line | Endpoint | Verified returns ITS ships | robots.txt for `*` | Status |
|---|---|---|---|---|
| Royal Caribbean | `royalcaribbean.com/cruises/graph` | **yes** | path not disallowed, no crawl-delay | **working, in production** |
| Celebrity | `celebritycruises.com/cruises/graph` responds 200 | **NO - returns Royal Caribbean ships** | disallows `/search/`, `/booking-cruise/*` | needs a brand parameter or another endpoint |
| MSC | none reachable | n/a | **401 to our user-agent, even for robots.txt** | **blocked; no fares, per operator** |
| Carnival | not found | n/a | 5 rules, none relevant | needs a request capture |
| Norwegian | not found | n/a | disallows `/search`, `/search-results`, `/cruise-quotes/` | needs a capture; those rules may cover it |
| Princess | not found | n/a | no disallow rules for `*` | needs a capture |
| Disney | not found | n/a | 36 rules, all under `/dcl/myCruise/` | needs a capture |
| Virgin Voyages | not found | n/a | no disallow rules for `*` | needs a capture |
| Costa | not found | n/a | robots.txt did not fetch | needs a capture; no US ports anyway |
| Silversea | not found | n/a | 4 rules, none relevant | needs a capture |

**One of ten has a verified adapter. One is hard-blocked. Eight are unknown.**

## The near-miss that matters most

`celebritycruises.com/cruises/graph` accepts the Royal Caribbean payload,
returns HTTP 200, and returns a schema-valid `cruiseSearch` response. It looks
like a working Celebrity adapter in every respect except the one that counts:

```
ships returned by celebritycruises.com/cruises/graph:
  Icon of the Seas, Liberty of the Seas, Mariner of the Seas, Symphony of the Seas
```

Those are Royal Caribbean ships. The hostname serves the Royal Caribbean
catalogue. An adapter accepted on a 200 and a matching schema would have
filled a Celebrity page with Royal Caribbean sailings: invented facts carrying
a source URL that looked correct, which is precisely what Hard Rule 3 exists
to stop. **Every adapter has to prove it returns that line's own ships before
it is allowed to write a row.** That check belongs in the adapter itself, not
in a reviewer's attention.

## Why the other eight were not found, and what actually finds them

Royal Caribbean was easy for a reason that does not generalise: its own site
calls a public GraphQL endpoint with a readable operation name, on a path its
robots.txt does not disallow.

The others are client-rendered apps that fetch from a path only the running
app knows. Carnival's `/cruise-search` is a 12 KB Next.js shell with 1,323
lazy chunks; the endpoint is inside one of them. Two approaches were tried and
both failed:

- **Path guessing.** `/cruise-search/api/search`, `/api/cruisesearch/search`,
  `/BookingEngine/api/cruisesearch` and others all returned HTTP 200 with
  HTML, which is a soft 404. A status code is not evidence.
- **Static bundle analysis.** The entry chunks hold no endpoint; it is in a
  lazily loaded one. Chasing 1,323 chunks per line is slow, and whatever it
  finds breaks on the next deploy of their site.

**The reliable step is an operator capture, about two minutes per line.** Open
the line's cruise-search page, DevTools, Network, filter to Fetch/XHR, run a
search for a US port, and copy the request URL, method and payload of the call
that returns the sailings. With that in hand an adapter is a short job, and it
can be verified the same way Royal Caribbean's is: two differently shaped
queries that have to agree to the cent, plus the brand check above.

## Standing constraints

- Lines with no working adapter get **no fares**: last good data, or
  "Fare on request". Never a wrong figure and never a blank one.
- MSC is excluded from fares by operator decision, 2026-10-20.
- Costa has no US departure ports, so it has no sailings to collect for this
  site regardless of whether an adapter is possible.
- Where a line's robots.txt disallows the path its sailings API sits on
  (Norwegian is the live risk here, with `/search*` disallowed), that counts
  as the line declining automated access, and the line gets no fares.
- Our Royal Caribbean collection was re-checked against royalcaribbean.com's
  robots.txt on 2026-10-20: `/cruises/graph` is not disallowed for `*` and no
  crawl-delay is set. One query per port per run, three days apart.
