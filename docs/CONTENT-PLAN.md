# CruiseLine Advisors — Content Strategy & Editorial Plan

> The living plan for building topical authority. This is an **ongoing** operation — we publish
> helpful, factual, original cruise knowledge on a steady cadence, not a fixed batch. Repo-only /
> never served / never indexed (see PROJECT-HANDBOOK). Last updated: 2026-07-20.

---

## 1. The goal

Become the **trusted, factual authority** cruise vacationers reach for when making a decision — and
be surfaced in **Google results AND AI overviews** (SGE, ChatGPT, Perplexity, etc.). Every page is:

- **100% factual, 100% original, hand-written** — no copied prose, no plagiarism, no thin "just
  another article on the internet." Every guide is a *research piece* that answers the real question
  better than what's already ranking.
- **Compliant** — no fares/prices/rates/discounts/savings (Hard Rule 1), no invented facts (Rule 3),
  no implied cruise-line affiliation (Rule 2). See `CLAUDE.md`.
- **Conversion-aware** — the site's only metric is inbound phone calls. Guides build trust and end
  in a natural call CTA; they never hard-sell.

## 2. Architecture — hub & spoke (pillar → cluster)

Search engines and LLMs reward **topical depth + tight internal linking**. We organise content as
**pillars** (broad hub topics) with **cluster guides** (specific sub-topics) that link up to the
pillar, across to siblings, and out to the money pages (lines, ships, destinations, facts, tools).

```
PILLAR (hub) ──┬── cluster guide ──┐
               ├── cluster guide    ├─ all interlink to each other + up to pillar
               └── cluster guide ──┘   + out to /cruise-facts, /compare, line/ship/destination pages
```

The **existing site sections are themselves pillars**: Cruise Lines, Ships, Destinations, Cruise
Facts, the finder tool. Guides are the *awareness + how-to* layer that feeds them.

## 3. The pillar & cluster map (topic backlog)

Priority tiers: **P1** = build first (high intent / reinforces conversion), **P2** = next, **P3** = fill out.

### Pillar A — Cruise costs & money  (reinforces /cruise-facts + the compare tool)
- ✅ **What's included in a cruise fare — and what costs extra** (flagship, live) — P1
- Cruise gratuities & daily service charges explained — P1
- Drink packages: are they worth it, and the whole-cabin rule — P1
- Wi-Fi at sea: packages & what to actually expect — P2
- Cruise deposits, final payment & the cancellation timeline — P1
- Refundable vs non-refundable fares — P2
- Onboard credit, explained — P3
- How to find an affordable cruise (without chasing fake "deals") — P1
- Hidden cruise costs first-timers miss — P2
- How cruise pricing actually works (why "from $X" is misleading) — P2

### Pillar B — Planning your first cruise  (awareness → everything)
- ✅ First-time cruisers (exists, upgrade to rich) — P1
- ✅ Choosing a cabin: interior / oceanview / balcony / suite (exists, upgrade) — P1
- ✅ When to cruise: season by region (exists, upgrade) — P2
- What to pack for a cruise (+ printable checklist tool) — P2
- Embarkation day: what to expect, step by step — P2
- Cruise documents & ID: passport vs birth certificate, closed-loop — P1
- A–Z cruise glossary (terms every cruiser should know) — P2

### Pillar C — Who you're travelling with  (persona → finder tool)
- ✅ Groups & families (exists, upgrade) — P1
- Solo cruising & the single supplement — P1
- Cruising for couples / adults-only at sea — P2
- Multigenerational & group cruises — P3
- ✅ Accessibility at sea (exists, upgrade) — P2

### Pillar D — Choosing a line & ship  (→ line/ship pages + compare)
- How to choose a cruise line that fits you — P1
- Big ship vs small ship: which suits you — P2
- How to pick the best cabin location (deck, midship, what to avoid) — P2
- Contemporary vs premium vs luxury cruise lines — P2

### Pillar E — Destinations & itineraries  (→ destination pages)
- How to choose a cruise destination — P1
- Caribbean vs Alaska vs Mediterranean: how to decide — P2
- Port days vs sea days: what a cruise day is really like — P3
- Repositioning cruises, explained — P3
- (Heavy interlink with the /destinations/ section — don't duplicate it.)

### Pillar F — Safety, scams & consumer protection  (trust / authority — high EEAT value)
- How to avoid cruise "deal" scams & robocalls — P1
- Is that "free cruise" offer real? red flags to know — P1
- Travel insurance for cruises: what it covers, when it's worth it — P2
- Understanding your cruise ticket contract & passenger rights — P2

**Tools (not articles) on the roadmap:** printable packing checklist · "which line fits me" quick
picker · cabin-type explainer. Tools earn links and keep people on-site → call.

## 4. Semantic SEO rules (apply to every guide)

- **One primary intent per guide**, plus its natural keyword variations woven into H2s and the FAQ
  (e.g. "are drinks included on a cruise", "is wifi free on cruises", "cruise gratuities explained").
  Don't keyword-stuff — write for the human, cover the entity thoroughly.
- **Cover the entity, not just the keyword.** Mention the related sub-entities a topic implies
  (gratuities → service charge, crew appreciation, prepaid, per-guest, suites) so the page reads as
  authoritative to both Google and LLMs.
- **Answer-first for AI overviews:** the "key takeaways" box + the FAQ give clean, liftable answers.
  Keep FAQ answers 1–3 sentences, factual, self-contained.
- **Structured data:** every rich guide emits **Article** + **FAQPage** JSON-LD (built in). Destination
  guides emit FAQPage too.
- **E-E-A-T signals:** a byline ("Written by the CruiseLine Advisors team"), a "Reviewed <date>", the
  verified-facts sourcing, and the clear "what we are / how we verify" footer disclaimers.
- **Scannability:** H1 → dek → key takeaways → TOC → short H2 sections → FAQ → related. Short
  paragraphs, visual cards, callouts.

## 5. Interlinking rules (natural, never forced)

- Link a topic to a **line / ship / destination / fact / tool page only where the sentence genuinely
  calls for it** — e.g. "we keep the verified per-line number on the [cruise facts] page." Never drop
  a link that doesn't help the reader.
- Every guide links **up to its pillar**, **across to 2–4 sibling guides** (the "Keep reading" block),
  and **out to at least one money page** (a line, the finder, or /cruise-facts).
- Line, ship and destination pages should, over time, link **back into** the relevant guide (e.g. a
  line page's gratuities row → the gratuities guide). Add these as the cluster fills in.
- Anchor text is descriptive and varied — not "click here," not the exact same phrase every time.

## 6. Visual standards (self-hosted, commercial-use only)

Guides must look stunning and be easy to read. The engine (`guidepage.py`) provides:
- **Photo hero** — a self-hosted region/topic image behind the H1 (`assets/guides/<slug>.jpg`),
  gradient scrim for legibility. Falls back to the gradient hero if no image.
- **`vcards([...])`** — visual concept cards (emoji + label + note) instead of plain bullet lists.
- **Callouts** — `tip()` 💡, `watch()` ⚠️, `define()` 📖 for emphasis and glossary terms.
- **`photo_band(img, caption)`** — a wide self-hosted photo to break up long reads.
- **Key-takeaways box**, **TOC**, **FAQ accordion**, **"Keep reading" card row**.

**Imagery licensing:** ONLY Unsplash / Pexels / CC0-Wikimedia (commercial use, no attribution),
self-hosted under `newsite/assets/guides/`. Record each in `docs/hero-image-credits.json`. The
footer "Photography" disclaimer already covers illustrative use + credit. Prefer **custom on-brand
graphics** (emoji cards, diagrams) over stock where a concept is clearer as a diagram.

## 7. The repeatable build system (how to add a guide)

1. Add a hero image to `newsite/assets/guides/<slug>.jpg` (optional but preferred).
2. Add a `register("<slug>", {...})` block in `newsite/guides_content.py` with: `cat`, `published`,
   `updated`, `title`, `dek`, `takeaways`, `sections` (each `{id, h2, html}`), `faqs`, `related` —
   all EN + ES. Use `vcards/tip/watch/define/photo_band` in the section HTML.
3. Ensure the slug is in `GUIDES` (in `pages.py`) so it shows on the Guides hub, with `emo/t/d`.
4. `python3 build.py` → must end "✓ banned-term guard clean" (no `$`, `save `, `discount`,
   `cheapest`, `% off`, `from $`, `lowest price`, `usd`).
5. Deploy. The guide renders rich automatically (Article + FAQ schema, TOC, hero, interlinks).

Guides without a `register()` entry still render as the older simple paragraph guide — so migrate the
6 existing ones to rich over time.

## 8. Publishing cadence & workflow

- **Cadence:** aim for a steady rhythm (e.g. 1–2 rich guides/week). Consistency signals a live,
  authoritative site to Google.
- **Sequence:** clear the **P1** backlog first (they convert and reinforce the fact pages), then P2,
  then P3. Refresh older guides on the same 30-day cycle as facts when a policy changes (§ OPERATIONS).
- **Tie-in with monitoring:** when a Google Alert / Feedly item (see OPERATIONS §5) reveals a
  fact-affecting change, it often also warrants a guide refresh or a new Update — do both.
- **Every guide ships with:** hero image, key takeaways, FAQ (schema), ≥3 natural internal links, a
  call CTA, EN + ES.

## 9. Measuring it

Track in Search Console + GA4 (via GTM): impressions/clicks per guide, queries won, and — the metric
that matters — **calls** (`call_click`) originating from guide pages. Watch for guides appearing in
**AI overviews / featured snippets** (the takeaways + FAQ are built for this). Prune or merge guides
that never gain traction; double down on clusters that do.
