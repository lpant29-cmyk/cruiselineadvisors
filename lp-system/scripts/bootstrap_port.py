"""Seed a NEW departure port into the Royal Caribbean fare pipeline.

Run once per port. It does what a human collection pass would do and nothing
more: read the official cruiseSearch feed for one departure port, keep the
packages with the most real sailings, and write itinerary rows that carry their
own source URL and today's stamp. The daily job (auto_rates.py) owns them from
then on, under the same 3-day fuse and the same swing gates as Galveston.

It will not invent anything it cannot read:
  - a package whose itinerary name does not name a destination we publish is
    SKIPPED, because dest drives the finder's "Sail to" filter and a guess
    there is a guess on every card;
  - a ship not already in 02_ships.csv is added from the feed's own name, with
    status=seeded, never with specs;
  - month floors come from the feed's own per-sailing prices, interior and
    balcony separately, exactly as derive() does for Galveston.

usage: python3 bootstrap_port.py <PORT_CODE> <port-slug> "<Port Label>" [--cap N] [--write]
       (without --write it prints what it would do and touches nothing)
"""
import collections, csv, datetime, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "lp-system" / "data"
sys.path.insert(0, str(HERE))
import auto_rates as ar

CACHE = pathlib.Path("/tmp/claude-501/scout")

# An itinerary name must say where it goes. These are the destinations the site
# already publishes; anything else is skipped rather than filed under a guess.
DESTS = [
    ("western-caribbean", "Western Caribbean", r"western\s+caribbean"),
    ("eastern-caribbean", "Eastern Caribbean", r"eastern\s+caribbean"),
    ("southern-caribbean", "Southern Caribbean", r"southern\s+caribbean"),
    ("bahamas", "Bahamas", r"\bbahamas\b"),
    ("caribbean", "Caribbean", r"\bcaribbean\b"),
]


def classify(name):
    low = name.lower()
    for slug, label, pat in DESTS:
        if re.search(pat, low):
            return slug, label
    return None, None


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f)), list(csv.DictReader(open(path, encoding="utf-8")).fieldnames or [])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    cap = 12
    if "--cap" in sys.argv:
        cap = int(sys.argv[sys.argv.index("--cap") + 1])
    if len(args) < 3:
        sys.exit(__doc__)
    code, port_slug, port_label = args[0], args[1], args[2]

    doc, how = ar.graph(f"departurePort:{code}", CACHE / f"graph-departurePort-{code}.json",
                        CACHE, offline=(CACHE / f"graph-departurePort-{code}.json").exists())
    print(f"feed: {how}")

    packs = []
    for c in doc["data"]["cruiseSearch"]["results"]["cruises"]:
        sails = [s for s in c["sailings"]
                 if ((s["itinerary"].get("departurePort") or {}).get("code")) == code]
        if not sails:
            continue
        it = sails[0]["itinerary"]
        packs.append({"gid": c["id"], "link": c.get("productViewLink", ""),
                      "name": it["name"], "nights": it["totalNights"],
                      "ship": it["ship"]["name"], "ship_code": it["ship"]["code"],
                      "sailings": sails})
    packs.sort(key=lambda p: -len(p["sailings"]))

    itins, itin_fields = read(DATA / "03_itineraries.csv")
    ships, ship_fields = read(DATA / "02_ships.csv")
    by_name = {s["ship_name"]: s for s in ships}
    next_ship = max(int(s["ship_id"][1:]) for s in ships) + 1
    next_itin = max(int(r["itin_id"][1:]) for r in itins if r["itin_id"].startswith("i")) + 1
    today = datetime.date.today().isoformat()
    cutoff = today[:7]

    new_ships, new_rows, groups, skipped = [], [], {}, []
    for p in packs:
        if len(new_rows) >= cap:
            break
        dest, dest_label = classify(p["name"])
        if not dest:
            skipped.append((p["name"], "itinerary name names no destination we publish"))
            continue
        # productViewLink is a RELATIVE path with the sail date and package code
        # in its query string. The stored source is the canonical itinerary page,
        # absolute and without the per-sailing query, which is what the Galveston
        # rows carry and what the provenance whitelist checks the host of.
        link = (p["link"] or "").split("?")[0].lstrip("/")
        if not link:
            skipped.append((p["name"], "no official product link in the feed"))
            continue
        p["link"] = "https://www.royalcaribbean.com/" + link

        srow = by_name.get(p["ship"])
        if srow is None:
            sid = f"s{next_ship:03d}"
            next_ship += 1
            srow = {k: "" for k in ship_fields}
            srow.update({"ship_id": sid, "line_id": "rci", "ship_name": p["ship"],
                         "slug": re.sub(r"[^a-z0-9]+", "-", p["ship"].lower()).strip("-"),
                         "status": "seeded",
                         "source": "https://www.royalcaribbean.com/cruises/graph (cruiseSearch)",
                         "notes": f"Added by bootstrap_port.py from the {code} feed on {today}. "
                                  "Name only; no specifications read."})
            ships.append(srow)
            by_name[p["ship"]] = srow
            new_ships.append(srow)

        months = collections.defaultdict(dict)
        for s in p["sailings"]:
            d = s.get("sailDate") or s.get("startDate") or ""
            if not d or d[:7] < cutoff:
                continue
            months[d[:7]][d[:10]] = {
                pr["stateroomClass"]["id"]: (pr.get("price") or {}).get("value")
                for pr in (s.get("stateroomClassPricing") or [])}
        if not months:
            skipped.append((p["name"], "no future sailings"))
            continue

        overrides, last_sail, floors_i, floors_b = [], [], [], []
        for mo in sorted(months):
            sails = months[mo]
            last_sail.append(f"{mo}:{max(sails)}")
            i = [v["INTERIOR"] for v in sails.values() if v.get("INTERIOR")]
            b = [v["BALCONY"] for v in sails.values() if v.get("BALCONY")]
            parts = []
            if i:
                floors_i.append(min(i)); parts.append(f"i{int(min(i))}")
            if b:
                floors_b.append(min(b)); parts.append(f"b{int(min(b))}")
            if parts:
                overrides.append(f"{mo}:" + "|".join(parts))

        taxes = any(s.get("taxesAndFeesIncluded") for s in p["sailings"])
        iid = f"i{next_itin:04d}"
        next_itin += 1
        slug = (f"{p['nights']}n-{dest}-"
                f"{re.sub(r'[^a-z0-9]+','-',p['ship'].lower()).strip('-').replace('-of-the-seas','')}"
                f"-{port_slug}")
        row = {k: "" for k in itin_fields}
        row.update({
            "itin_id": iid, "line_id": "rci", "ship_ids": srow["ship_id"],
            "name": f"{p['nights']}-Night {dest_label}", "slug": slug,
            "dest": dest, "dest_label": dest_label,
            "port_slug": port_slug, "port_label": port_label,
            "nights": str(p["nights"]),
            "sail_months": ";".join(sorted(months)),
            "month_last_sail": ";".join(last_sail),
            "price_interior": str(int(min(floors_i))) if floors_i else "",
            "price_balcony": str(int(min(floors_b))) if floors_b else "",
            "month_price_overrides": "|".join(overrides),
            "taxes_note": ("Taxes and fees included in the listed fare" if taxes
                           else "Plus taxes fees and port expenses"),
            "private_island": "yes" if "perfect day" in p["name"].lower() or "cococay" in p["name"].lower() else "no",
            "date_checked": today,
            "source": p["link"],
            "page_targets": (f"line:royal-caribbean;port:{port_slug};dest:{dest};"
                             f"combo:royal-caribbean-{port_slug};ship:{srow['slug']}"),
            "featured": "yes" if len(new_rows) < 2 else "",
            "notes": (f"Seeded from the official cruiseSearch feed for departurePort:{code} on "
                      f"{today} ({len(p['sailings'])} sailings in the package). Month floors are "
                      f"the cheapest published interior/balcony fare in each month, from the feed."),
            "auto_status": f"ok {today}",
        })
        new_rows.append(row)
        groups[iid] = p["gid"]

    print(f"\n{code} -> {port_slug}: {len(new_rows)} rows, {len(new_ships)} new ships, "
          f"{len(skipped)} packages skipped")
    for r in new_rows:
        print(f"  {r['itin_id']}  {r['nights']:>2}n  {r['dest_label']:<20} "
              f"{r['sail_months'][:30]:<32} from {r['price_interior'] or '-'}")
    for n, why in skipped[:6]:
        print(f"  skip: {n[:46]:<48} {why}")

    if not write:
        print("\n(dry run: nothing written. pass --write)")
        return

    with open(DATA / "03_itineraries.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=itin_fields)
        w.writeheader()
        w.writerows(itins + new_rows)
    with open(DATA / "02_ships.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ship_fields)
        w.writeheader()
        w.writerows(ships)
    gpath = DATA / "08_group_ids.json"
    g = json.loads(gpath.read_text(encoding="utf-8"))
    g.setdefault("_ports", {})[port_slug] = code
    g.update(groups)
    gpath.write_text(json.dumps(g, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nwritten: {len(new_rows)} itinerary rows, {len(new_ships)} ships, "
          f"{len(groups)} group ids")


if __name__ == "__main__":
    main()
