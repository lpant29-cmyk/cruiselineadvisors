Invoke the structure-guard agent with the keyword(s) I provide as $ARGUMENTS.

Structure Guard must follow its full sequence from .claude/agents/structure-guard.md:
parse the keyword into facets, run the dedupe check against the pages and keyword
map registries, run the inventory check against the itineraries data (triggering
targeted collection via research-registrar and pricing-scout only if the combo is
real but under-collected), register the page and keyword mapping, hand off to
page-builder, require qa-auditor approval, and return the final summary block:
URL, page_id, deal_filter, itinerary count, tracking number, H1, and any keywords
already sharing the page.

If the keyword resolves to an existing page, return that page's URL and add the
keyword to the map — do not build anything new.

If the facet combination has no real inventory (the line does not sail that
route), refuse with the reason and suggest the nearest valid combination.

Examples:
/need-page bahamas cruises from galveston
/need-page 3 day caribbean cruise
/need-page cheap cruises from fort lauderdale
/need-page royal caribbean 7 day bahamas cruise
