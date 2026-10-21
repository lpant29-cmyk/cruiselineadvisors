"""Build guard: no page may claim our call gets a better, exclusive or
unpublished rate.

We do not set prices, hold inventory or quote. Every one of these sentences
says we do, and says it on pages running ads on cruise line brand terms:

    "often better rates than booking online once your travel is bundled"
    "Unlock Unpublished Rates by Phone"
    "exclusive rates"
    "Get better rates by phone"

Each one shipped at some point and each was removed by hand. A guard is the
only thing that stops the next one, because the wording is the single most
tempting thing to write on a page whose only job is to earn a phone call.

NOT banned: the same words used factually, which is most of their uses on this
site. A line bundles drinks into its fare. Yield management fills every cabin
at the best fare the market will bear. Booking early usually secures a better
fare. Those are how cruise pricing works, they are the reason the guide pages
exist, and deleting them would make the site worse and no more honest.

What separates a fact from a claim is who the sentence says gets the money
back. So a comparative or savings match only counts when the SAME SENTENCE
also refers to us or to the call: we, our, us, advisor, one call, by phone.
"the line's goal is the best fare the market will bear" passes. "one call gets
you the best rate our partners can offer" does not, and that sentence was on
424 pages when this guard was written.

Second person is deliberately NOT a self-reference. Every educational sentence
on the site addresses the reader ("you book a cabin at a lower price"), so
counting "you" would flag the entire pricing guide.

The exclusive/unpublished group needs no self-reference: nothing on this site
has a legitimate reason to call a fare unpublished, secret or insider.

Runs about a minute over the built tree, which is most of what it costs to
scan every page's prose AND its scripts. The /go/ copy lives in template
literals inside each page's own JavaScript, which is exactly where the worst
of these sentences was found, so narrowing the scan to <main> would miss them.

usage: python3 rate_claim_guard.py <dir> [<dir>...]   exit 1 on any hit
"""
import html, pathlib, re, sys

MONEY = r"(?:rates?|fares?|prices?|pricing|deals?|discounts?|savings?|quotes?|tarifas?|precios?|descuentos?)"

# Us, or the phone call. Not "you": see the docstring.
SELF = re.compile(r"\b(?:we|we'?ll|we'?re|our|ours|us|advisors?|asesor\w*|nuestr\w+|"
                  r"one\s+call|a\s+call|by\s+phone|call\s+(?:now|us|and)|una\s+llamada|"
                  r"llamada|llámanos)\b", re.I)

# (pattern, why, needs_self_reference)
PATTERNS = [
    # "better rates", "lower fares", "mejores tarifas"
    (r"\b(?:better|lower|cheaper|best|lowest|cheapest|mejores?|más\s+bajas?|más\s+baratas?)\s+" + MONEY,
     "comparative rate claim", True),
    # "exclusive rates", "unpublished fares", "tarifas exclusivas"
    (r"\b(?:exclusive|unpublished|unadvertised|secret|hidden|insider|exclusivas?|no\s+publicadas?)\s+" + MONEY,
     "exclusive/unpublished rate claim", False),
    (MONEY + r"\s+(?:exclusivas?|exclusive|no\s+publicadas?|unpublished)\b",
     "exclusive/unpublished rate claim", False),
    # "bundled" next to money: the product bundles amenities, we do not bundle a rate
    (r"\bbundl\w*\b[^.;]{0,40}" + MONEY, "bundle-for-a-rate claim", True),
    (MONEY + r"[^.;]{0,40}\bbundl\w*\b", "bundle-for-a-rate claim", True),
    # "better than booking online/direct", "cheaper than the website"
    (r"\b(?:better|lower|cheaper|less)\s+than\s+(?:booking|the\s+(?:site|website)|online|direct)",
     "beats-booking-elsewhere claim", False),
    # "save hundreds", "save up to 40%"
    (r"\bsave\s+(?:hundreds|thousands|up\s+to)\b", "unquantified savings claim", True),
    (r"\bahorr\w+\s+(?:cientos|miles|hasta)\b", "unquantified savings claim", True),
    # "unlock ... rates"
    (r"\bunlock\w*\b[^.;]{0,30}" + MONEY, "unlock-a-rate claim", True),
]
# Nine separate passes, deliberately. Folding them into one alternation was
# tried and came out SLOWER (65s vs 54s over the built tree): the combined
# branch set backtracks more than nine cheap scans do.
RX = [(re.compile(p, re.I), why, needs) for p, why, needs in PATTERNS]

targets = sys.argv[1:] or [str(pathlib.Path(__file__).resolve().parent.parent / "site")]
hits = {}
for base in targets:
    for f in pathlib.Path(base).rglob("*.html"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        # Scan the WHOLE document, scripts included. On /go/ pages the copy
        # that matters is inside template literals in the page's own JS, which
        # is exactly where "better rates than booking online" lived.
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
        # The brand name ends in "Advisors" and the review byline carries no
        # full stop, so a sentence span could reach it and read our own name as
        # a first-person claim. Drop the brand before matching: it is never the
        # signal: we / our / one call / by phone are.
        text = re.sub(r"CruiseLine\s*Advisors", "the site", text, flags=re.I)
        for rx, why, needs_self in RX:
            for m in rx.finditer(text):
                if needs_self:
                    # The sentence the match sits in, not a fixed character window:
                    # a window straddles two sentences and borrows the wrong subject.
                    # Searched inside a bounded slice, because the first version
                    # called rfind from the match back to byte zero for each of six
                    # terminators, on every match, on a 470KB page. That is
                    # quadratic and it hung the build for minutes. A sentence longer
                    # than SPAN characters does not exist in this copy.
                    SPAN = 400
                    a, b = max(0, m.start() - SPAN), min(len(text), m.end() + SPAN)
                    before, after = text[a:m.start()], text[m.end():b]
                    lo = max((before.rfind(c) for c in ".;!?¡¿"), default=-1) + 1
                    ends = [h for h in (after.find(c) for c in ".;!?") if h != -1]
                    hi = m.end() + (min(ends) if ends else len(after))
                    if not SELF.search(text[a + lo:hi]):
                        continue
                hits.setdefault((m.group(0).strip().lower(), why), set()).add(str(f))

if not hits:
    print("RATE-CLAIM GUARD: clean, no better/exclusive/unpublished rate wording found.")
    sys.exit(0)
print(f"RATE-CLAIM GUARD: {len(hits)} banned claim(s)")
for (phrase, why), files in sorted(hits.items(), key=lambda x: -len(x[1])):
    print(f'  "{phrase}"  [{why}]  on {len(files)} page(s), e.g. {sorted(files)[0]}')
sys.exit(1)
