"""Seed a Carnival departure port: SAILINGS AND DATES ONLY, never prices.

carnival.com/cruisesearch/api/search is Carnival's own search endpoint. It
takes a port code, echoes the filter back so the server is provably the one
that applied it, and returns whole itineraries with their region, length, ship,
port list and every sailing date.

It also returns prices, and we deliberately DO NOT KEEP THEM (operator ruling
2026-10-21). They arrive as round numbers (300, 400, 600 floors) that look like
banded lead-in pricing rather than the per-sailing fare Royal Caribbean
returns, and an unverified price is worse than no price on a page whose whole
job is a phone call. Every card says the fare comes by phone. price_interior
and price_balcony are written EMPTY, which is what makes that happen: the
generator's own price_ok() gate then withholds a fare that was never there.

usage: python3 bootstrap_carnival_port.py <PORT_CODE> <port-slug> "<Port Label>" [--cap N] [--write]
"""
import csv, datetime, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent.parent / "lp-system" / "data"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/155.0 Safari/537.36")
API = "https://www.carnival.com/cruisesearch/api/search"

# Carnival's own region codes, mapped to the destinations this site publishes.
# A region not listed is SKIPPED: dest drives the finder's "Sail to" menu and a
# guess there is a guess on every card.
REGIONS = {
    "CW": ("western-caribbean", "Western Caribbean"),
    "CE": ("eastern-caribbean", "Eastern Caribbean"),
    "CS": ("southern-caribbean", "Southern Caribbean"),
    "BH": ("bahamas", "Bahamas"),
    "CB": ("caribbean", "Caribbean"),
}


def fetch(port):
    url = f"{API}?port={port}&pageSize=200&pageNumber=1"
    p = subprocess.run(["curl", "-sSL", "-m", "60", "--retry", "2", "-A", UA, url],
                       capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        sys.exit(f"curl failed rc={p.returncode}")
    d = json.loads(p.stdout)
    echoed = (d.get("filters") or {}).get("port")
    if echoed != [port]:
        sys.exit(f"the server did not apply the port filter (echoed {echoed}); refusing to "
                 "treat an unfiltered result set as this port's sailings")
    return d


def read(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    return rows, list(rows[0].keys())


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    cap = int(sys.argv[sys.argv.index("--cap") + 1]) if "--cap" in sys.argv else 12
    if len(args) < 3:
        sys.exit(__doc__)
    code, port_slug, port_label = args[0], args[1], args[2]

    d = fetch(code)
    itins_feed = sorted(d["results"]["itineraries"],
                        key=lambda it: -len(it.get("sailings") or []))

    itins, itin_fields = read(DATA / "03_itineraries.csv")
    ships, ship_fields = read(DATA / "02_ships.csv")
    by_name = {s["ship_name"]: s for s in ships}
    next_ship = max(int(s["ship_id"][1:]) for s in ships) + 1
    next_itin = max(int(r["itin_id"][1:]) for r in itins if r["itin_id"].startswith("i")) + 1
    today = datetime.date.today().isoformat()
    cutoff = today[:7]

    new_rows, new_ships, skipped = [], [], []
    for it in itins_feed:
        if len(new_rows) >= cap:
            break
        dest = REGIONS.get(it.get("regionCode") or "")
        if not dest:
            skipped.append((it.get("itineraryTitleFormatted", "?"),
                            f"region {it.get('regionCode')} ({it.get('regionName')}) is not one we publish"))
            continue
        url = (it.get("itineraryURL") or "").split("?")[0]
        if not url:
            skipped.append((it.get("itineraryTitleFormatted", "?"), "no itinerary URL in the feed"))
            continue
        months = {}
        for s in it.get("sailings") or []:
            dt = (s.get("departureDate") or "")[:10]
            if dt and dt[:7] >= cutoff:
                months.setdefault(dt[:7], []).append(dt)
        if not months:
            skipped.append((it.get("itineraryTitleFormatted", "?"), "no future sailings"))
            continue

        ship_name = it.get("shipName") or ""
        srow = by_name.get(ship_name)
        if srow is None:
            sid = f"s{next_ship:03d}"; next_ship += 1
            srow = {k: "" for k in ship_fields}
            srow.update({"ship_id": sid, "line_id": "ccl", "ship_name": ship_name,
                         "slug": re.sub(r"[^a-z0-9]+", "-", ship_name.lower()).strip("-"),
                         "status": "seeded",
                         "source": "https://www.carnival.com/cruisesearch/api/search",
                         "notes": f"Added from the Carnival {code} feed on {today}. Name only."})
            ships.append(srow); by_name[ship_name] = srow; new_ships.append(srow)

        nights = int(it.get("dur") or 0)
        iid = f"i{next_itin:04d}"; next_itin += 1
        row = {k: "" for k in itin_fields}
        row.update({
            "itin_id": iid, "line_id": "ccl", "ship_ids": srow["ship_id"],
            "name": f"{nights}-Night {dest[1]}",
            "slug": f"{nights}n-{dest[0]}-{srow['slug']}-{port_slug}",
            "dest": dest[0], "dest_label": dest[1],
            "port_slug": port_slug, "port_label": port_label,
            "nights": str(nights),
            "sail_months": ";".join(sorted(months)),
            "month_last_sail": ";".join(f"{m}:{max(v)}" for m, v in sorted(months.items())),
            # EMPTY ON PURPOSE. See the module docstring.
            "price_interior": "", "price_balcony": "", "month_price_overrides": "",
            "taxes_note": "", "private_island": "no",
            "date_checked": today,
            "source": "https://www.carnival.com" + url,
            "page_targets": (f"line:carnival;port:{port_slug};dest:{dest[0]};"
                             f"combo:carnival-{port_slug};ship:{srow['slug']}"),
            "featured": "yes" if len(new_rows) < 2 else "",
            "notes": (f"Sailings and dates read from Carnival's own cruisesearch feed for "
                      f"port={code} on {today} ({len(it.get('sailings') or [])} sailings; "
                      f"ports: {', '.join(it.get('portsToDisplay') or [])}). PRICES DELIBERATELY "
                      "NOT STORED: the feed's figures are round lead-in bands, not the "
                      "per-sailing fare, so every card asks for the fare by phone."),
            "auto_status": f"ok {today} (no-price source)",
        })
        new_rows.append(row)

    print(f"{code} -> {port_slug}: {len(new_rows)} rows, {len(new_ships)} new ships, "
          f"{len(skipped)} skipped")
    for r in new_rows:
        print(f"  {r['itin_id']}  {r['nights']:>2}n  {r['dest_label']:<20} "
              f"{len(r['sail_months'].split(';')):>2} months   {r['ship_ids']}")
    for n, why in skipped[:5]:
        print(f"  skip: {n[:44]:<46} {why}")
    if not write:
        print("\n(dry run: nothing written. pass --write)")
        return
    with open(DATA / "03_itineraries.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=itin_fields); w.writeheader(); w.writerows(itins + new_rows)
    with open(DATA / "02_ships.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ship_fields); w.writeheader(); w.writerows(ships)
    print(f"\nwritten: {len(new_rows)} rows, {len(new_ships)} ships")


if __name__ == "__main__":
    main()
