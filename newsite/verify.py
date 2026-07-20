# -*- coding: utf-8 -*-
"""Fact-verification audit, the tool for the 30-day re-check.

Run `python3 verify.py status`  → one-line summary + non-zero exit if anything is due (use in CI /
                                   before deploy).
Run `python3 verify.py report`  → a full, per-line checklist: every fact, its source URL, when it was
                                   last verified and how many days ago, open each URL, confirm the
                                   value still matches, then bump the `verified` date in facts.py.

Refresh windows (see CLAUDE.md): inclusions 30 days, everything else 90, ship rosters 90. The default
re-check cadence the operator runs is every 30 days, so `--window N` overrides the flag threshold.
Nothing here touches the site; it only reads the data and reports.
"""
import sys
import datetime

from facts import LINE_FACTS, FACTS
from data import LINES
from ships import SHIPS

TODAY = datetime.date.today()
_LABEL = {f["key"]: f["label"]["en"] for f in FACTS}
# per-fact refresh window in days; default 90, inclusions/gratuities re-checked tighter at 30
_WINDOW = {k: 90 for k in _LABEL}
_WINDOW["included"] = 30
_WINDOW["gratuities"] = 30
_SHIP_WINDOW = 90


def _days_since(d):
    if not d:
        return None
    try:
        return (TODAY - datetime.date.fromisoformat(d)).days
    except (ValueError, TypeError):
        return None


def audit(window_override=None):
    """Return (missing, stale) where stale = facts past their window, missing = unverified gaps."""
    missing, stale = [], []
    for L in LINES:
        facts = LINE_FACTS.get(L["slug"], {})
        for f in FACTS:
            k = f["key"]
            cell = facts.get(k, {})
            if not cell.get("v"):
                missing.append((L["name"], _LABEL[k]))
                continue
            ds = _days_since(cell.get("verified"))
            win = window_override if window_override is not None else _WINDOW[k]
            if ds is None or ds > win:
                stale.append((L["name"], _LABEL[k], cell.get("verified"), ds, win, cell.get("src")))
    return missing, stale


def stale_ships():
    out = []
    for slug, s in SHIPS.items():
        ds = _days_since(s.get("verified"))
        if ds is None or ds > _SHIP_WINDOW:
            out.append((slug, s.get("verified"), ds))
    return out


def status(window_override=None):
    missing, stale = audit(window_override)
    ships = stale_ships()
    print(f"Fact verification @ {TODAY}")
    print(f"  facts due for re-check (past window): {len(stale)}")
    print(f"  unverified gaps (no value yet):       {len(missing)}")
    print(f"  ship rosters past {_SHIP_WINDOW}d:              {len(ships)}")
    if stale:
        print("\n  DUE NOW:")
        for name, label, ver, ds, win, _src in stale[:40]:
            print(f"    - {name}: {label}  (verified {ver}, {ds}d ago, window {win}d)")
    ok = not (stale or ships)
    print("\n  " + ("✓ all current, nothing due." if ok else "⚠ items above are due for re-verification."))
    return 0 if ok else 1


def report(window_override=None):
    """Full per-line checklist with source URLs, work through this during the 30-day pass."""
    print(f"# 30-day fact re-check, {TODAY}\n")
    for L in LINES:
        facts = LINE_FACTS.get(L["slug"], {})
        print(f"\n## {L['emo']} {L['name']}")
        for f in FACTS:
            k = f["key"]
            cell = facts.get(k, {})
            ver = cell.get("verified")
            ds = _days_since(ver)
            if not cell.get("v"):
                flag = "GAP (not yet verified)"
            else:
                win = window_override if window_override is not None else _WINDOW[k]
                flag = "DUE" if (ds is None or ds > win) else "ok"
            src = cell.get("src") or "(no source recorded)"
            days = f"{ds}d" if ds is not None else ", "
            print(f"  [{flag:<4}] {_LABEL[k]:<28} last {ver or ', '} ({days})")
            print(f"         source: {src}")
    print("\nAfter confirming a value still matches its source, update its `verified` date in facts.py.")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    win = None
    if "--window" in sys.argv:
        win = int(sys.argv[sys.argv.index("--window") + 1])
    if cmd == "report":
        sys.exit(report(win))
    sys.exit(status(win))
