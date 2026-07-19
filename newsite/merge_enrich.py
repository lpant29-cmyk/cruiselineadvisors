# -*- coding: utf-8 -*-
"""Merge enrich-<line>.json files (from the parallel enrichment pass) into the fact sheets:
per-ship exp (overview/who_for/dining/activities/entertainment/zones->neighbourhoods/kids_family/
decks/deploy_note) into data/ships/<line>.json, and line seasonal_deployment into
data/cruise-lines.json. Idempotent — re-run as more line files arrive. Normalizes {value,...}
wrappers, strips price tokens, drops "Not yet verified" placeholders (keeps them honest gaps)."""
import json
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SC = "/private/tmp/claude-501/-Users-lokesh29-cruiselineadvisors/0816b1d1-576f-4273-9b4b-2cf805325b26/scratchpad"
# hand-curated showcases we don't want overwritten by the bulk pass
SKIP = {"MSC World America"}


def _price_strip(s):
    if not isinstance(s, str):
        return s
    s = re.sub(r'\$\s?\d[\d.,]*', '', s)
    s = re.sub(r'\bUSD\b', '', s, flags=re.I)
    return re.sub(r'\s{2,}', ' ', s).strip()


def val(x):
    if isinstance(x, dict) and "value" in x:
        x = x["value"]
    if x is None:
        return None
    if isinstance(x, str):
        x = _price_strip(x)
        if not x or x.lower().startswith("not yet verified"):
            return None
    return x


def norm_type(t):
    tl = (t or "").lower()
    if any(k in tl for k in ("special", "steakhouse", "sushi", "grill house", "fine dining")):
        return "specialty"
    if any(k in tl for k in ("buffet", "market")):
        return "buffet"
    if "main" in tl:
        return "main"
    if any(k in tl for k in ("casual", "poolside", "cafe", "café", "coffee", "room service", "grill", "pizzer", "snack")):
        return "casual"
    return None


def norm_dining(lst):
    out = []
    for d in lst or []:
        nm = d.get("name")
        if not nm:
            continue
        out.append({"name": _price_strip(nm), "type": norm_type(d.get("type")),
                    "extra": d.get("extra") if isinstance(d.get("extra"), bool) else None,
                    "desc": _price_strip(d.get("desc") or "")})
    return out


def norm_items(lst):
    out = []
    for it in lst or []:
        if isinstance(it, dict) and it.get("name"):
            out.append({"name": _price_strip(it["name"]), "desc": _price_strip(it.get("desc") or "")})
        elif isinstance(it, str) and it.strip():
            out.append(_price_strip(it))
    return out


def decks_int(v):
    v = val(v)
    if isinstance(v, int):
        return v
    if isinstance(v, str):
        m = re.search(r'\d+', v)
        return int(m.group()) if m else None
    return None


def run():
    cl_path = os.path.join(HERE, "data", "cruise-lines.json")
    doc = json.load(open(cl_path, encoding="utf-8"))
    CL = {L["slug"]: L for L in doc["lines"]}
    needs = {}
    summary = []
    for f in sorted(glob.glob(os.path.join(SC, "enrich-*.json"))):
        slug = os.path.basename(f)[len("enrich-"):-len(".json")]
        shp = os.path.join(HERE, "data", "ships", f"{slug}.json")
        if not os.path.exists(shp):
            continue
        try:
            e = json.load(open(f, encoding="utf-8"))
        except Exception as ex:
            summary.append(f"{slug}: INVALID JSON ({ex})")
            continue
        ships = e.get("ships", [])
        by = {s.get("name"): s for s in ships}
        d = json.load(open(shp, encoding="utf-8"))
        applied = 0
        for s in d["ships"]:
            if s["name"] in SKIP:
                continue
            en = by.get(s["name"])
            if not en:
                continue
            exp = s.get("exp") or {}
            ov = val(en.get("overview"))
            wf = val(en.get("who_for"))
            dining = norm_dining(en.get("dining"))
            acts = norm_items(en.get("activities"))
            ent = norm_items(en.get("entertainment"))
            zones = norm_items(en.get("zones"))
            kids = val(en.get("kids_family"))
            dk = decks_int(en.get("decks"))
            route = val(en.get("deploy_note"))
            if ov:
                exp["overview"] = ov
            if wf:
                exp["who_for"] = wf
            if dining:
                exp["dining"] = dining
            if acts:
                exp["activities"] = acts
            if ent:
                exp["entertainment"] = ent
            if zones:
                exp["neighbourhoods"] = zones
            if kids:
                exp["kids_family"] = kids
            if dk:
                exp["decks"] = dk
            if route:
                exp["deploy_note"] = route
            if en.get("exp_source"):
                exp["exp_source"] = en["exp_source"]
            if exp:
                s["exp"] = exp
                applied += 1
            if en.get("needs"):
                needs.setdefault(slug, {})[s["name"]] = en["needs"]
        json.dump(d, open(shp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        sd = val(e.get("seasonal_deployment"))
        if sd and slug in CL:
            CL[slug]["seasonal_deployment"] = sd
        summary.append(f"{slug}: enriched {applied}/{len(d['ships'])} ships"
                       + (" + season map" if sd else ""))
    json.dump(doc, open(cl_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    # merge needs into the running checklist
    np = os.path.join(HERE, "data", "exp-needs.json")
    base = json.load(open(np, encoding="utf-8")) if os.path.exists(np) else {}
    base.update(needs)
    json.dump(base, open(np, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\n".join(summary) or "no enrich files found")


if __name__ == "__main__":
    run()
