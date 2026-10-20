"""Build guard: no page may describe a person as a cruise line's or ship's own
specialist / expert / advisor / agent / representative / team.

Why: we bid these brands as keywords and state in every footer that we are not an
agent of any line. "Royal Caribbean specialist" contradicts that in three words.
Allowed instead: "cruise specialist", "cruise advisor", or a PORT ("Galveston
specialist"), which names where we know the terminal, not who employs us.

NEGATION IS EXEMPT, and this is the whole reason the guard needs care. The required
disclaimer literally contains the banned shape: "ni somos agentes de Royal Caribbean"
("nor are we agents of Royal Caribbean"). A naive scan flags it on 30+ pages, and
"fixing" those would delete the non-affiliation statement the site exists to carry.
So a match preceded by a negation inside the same clause is skipped.

usage: python3 affiliation_guard.py <dir> [<dir>...]   exit 1 on any hit
"""
import json, pathlib, re, sys, html

ROOT = pathlib.Path("/Users/lokesh29/cruiselineadvisors")
names = set()
doc = json.loads((ROOT/"newsite/data/cruise-lines.json").read_text(encoding="utf-8"))
for l in doc["lines"]:
    for n in (l.get("name"), l.get("legal_name")):
        if n: names.add(n)
for f in (ROOT/"newsite/data/ships").glob("*.json"):
    for s in json.loads(f.read_text(encoding="utf-8")).get("ships", []):
        if s.get("name"): names.add(s["name"])
ROLE = r"(?:specialist|expert|advisor|adviser|agent|representative|rep|team|especialista|experto|asesor|agente|representante|equipo)"
pat = re.compile(r"\b(" + "|".join(sorted((re.escape(n) for n in names), key=len, reverse=True))
                 + r")(?:'s)?\s+(?:\w+\s+)?" + ROLE + r"\b", re.I)
# Spanish postfix form: "especialista en Royal Caribbean"
pat_es = re.compile(r"\b" + ROLE + r"\s+(?:en|de)\s+(" + "|".join(sorted((re.escape(n) for n in names), key=len, reverse=True)) + r")\b", re.I)

targets = sys.argv[1:] or [str(ROOT/"site")]
hits = {}
for base in targets:
    for f in pathlib.Path(base).rglob("*.html"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"<main[^>]*>(.*?)</main>", t, re.S | re.I)
        body = m.group(1) if m else t
        body = re.sub(r"<script\b[^>]*>.*?</script>", " ", body, flags=re.S | re.I)
        text = html.unescape(re.sub(r"<[^>]+>", " ", body))
        text = re.sub(r"\s+", " ", text)
        for rx in (pat, pat_es):
            for mm in rx.finditer(text):
                lead = text[max(0, mm.start() - 90):mm.start()].lower()
                # "we are NOT an agent of X" / "ni somos agentes de X" is the
                # disclaimer, not a claim. Skip a match that a negation governs.
                if re.search(r"\b(not|never|no|ni|nunca|non)\b[^.;]{0,90}$", lead):
                    continue
                hits.setdefault(mm.group(0).strip(), set()).add(str(f))
if not hits:
    print("AFFILIATION GUARD: clean, no '{line|ship} {role}' wording found.")
    sys.exit(0)
print(f"AFFILIATION GUARD: {len(hits)} banned phrase(s)")
for phrase, files in sorted(hits.items(), key=lambda x: -len(x[1])):
    print(f'  "{phrase}"  on {len(files)} page(s), e.g. {sorted(files)[0]}')
sys.exit(1)
