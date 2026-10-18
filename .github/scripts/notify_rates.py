#!/usr/bin/env python3
"""notify_rates.py — one GitHub issue, kept current, so the phone only buzzes
when something actually changed.

The operator asked for "one message" per run that needs them, not a feed. A
row can be held on every single cycle (a volatile cabin class will be), so
posting every run would train them to ignore it, which is worse than silence.

So: exactly one open issue carries the current state. A comment is posted only
when the SET of problems changes, because on GitHub a comment is what pushes
to the phone and an edited body is not. When nothing is wrong any more the
issue is closed, which is itself the all-clear.

Needs GH_TOKEN and OWNER in the environment. Exits 0 even when it cannot post:
a notification failure must never make a good refresh look like a bad one.
"""

import datetime as dt
import hashlib
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "lp-system" / "out"
LABEL = "fare-refresh"
TITLE = "Fare refresh needs a decision"
MARK = "<!-- fare-refresh-state:"


def gh(*args):
    """Never raises. A missing or failing gh must not turn a good refresh red."""
    try:
        p = subprocess.run(["gh", *args], capture_output=True, text=True,
                           timeout=120)
    except (OSError, subprocess.SubprocessError) as exc:
        return 127, "", str(exc)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def load_report(today):
    f = OUT / f"auto-rates-{today}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    return {"date": today, "ok": False,
            "error": "no run report was written", "rows": {}}


def problems(rep):
    """The list the operator actually has to act on, in plain words."""
    items = []
    if not rep.get("ok"):
        items.append(("fetch", "Could not read fares from source: "
                               + str(rep.get("error", "unknown"))
                               + ". Nothing was changed. If this repeats for "
                                 "three days the pages switch themselves to "
                                 "\"Fare on request\"."))
    for rid in rep.get("frozen", []):
        r = rep["rows"][rid]
        items.append((f"frozen:{rid}",
                      f"**{rid}** returned no sailings from either query, so it "
                      f"is held at its {r['stamp']} values and can no longer "
                      f"feed a page. If the season really has ended, retire the "
                      f"row and pause any ad pointing at it."))
    for rid in rep.get("held", []):
        r = rep["rows"][rid]
        items.append((f"held:{rid}",
                      f"**{rid}** was not published: {'; '.join(r['reasons'])}. "
                      f"It keeps its {r['stamp']} values and stamp, so its fares "
                      f"stop printing three days after that date unless you "
                      f"confirm the move."))
    for rid in rep.get("notable", []):
        r = rep["rows"][rid]
        items.append((f"notable:{rid}",
                      f"**{rid}** published a large move that both queries "
                      f"confirmed to the cent: {'; '.join(r['reasons'])}."))
    for g in rep.get("untracked_groups", []):
        items.append((f"untracked:{g}",
                      f"Source is offering `{g}` from this port and we do not "
                      f"track it. Either register it or decide not to."))
    for o in rep.get("retired_offers", []):
        items.append((f"offer:{o}",
                      f"Offer {o} passed its end date and its banner is off. A "
                      f"replacement has to be written by hand: this job is not "
                      f"allowed to author offer copy."))

    if os.environ.get("BUILD_OUTCOME") == "failure":
        items.append(("build", "The rebuild or its pre-deploy checks failed, so "
                               "nothing was pushed. The live pages are "
                               "untouched. See the run log."))
    if os.environ.get("PUSH_OUTCOME") == "failure":
        items.append(("push", "Fares were refreshed but the push failed, so the "
                              "change is not live. See the run log."))

    log = pathlib.Path(os.environ.get("VALIDATE_LOG", "/tmp/validate.log"))
    if log.exists():
        for line in log.read_text(errors="replace").splitlines():
            if "has 0 publishable deal rows" in line:
                items.append(("empty-page:" + line.split()[1],
                              line.strip() + " **This one needs ads paused.** "
                              "The page was not rebuilt, and because the host "
                              "never prunes, the copy already published stays "
                              "served until the ad groups pointing at it are "
                              "paused. Nothing we deploy can take it down."))
    return items


def body(rep, items, state):
    lines = [
        f"{MARK}{state} -->",
        "",
        f"Last run: **{rep['date']}**  ·  published "
        f"{len(rep.get('published', []))}  ·  held {len(rep.get('held', []))}"
        f"  ·  frozen {len(rep.get('frozen', []))}",
        "",
        "Everything not listed below refreshed cleanly and is live. Nothing "
        "here was published.",
        "",
    ]
    lines += [f"- {text}" for _, text in items]
    lines += [
        "",
        "---",
        "",
        "How this ran: two independently shaped queries against Royal "
        "Caribbean's own cruiseSearch endpoint, one by departure port and one "
        "per ship. A value publishes only where both agree to the cent.",
        "",
        "To act on a held row: run `/rate-update` in Claude Code, or re-run "
        "the workflow once you have checked the number at source.",
        "",
        "This issue is updated in place and closes itself when the list is "
        "empty. It only comments when the list changes.",
    ]
    return "\n".join(lines)


def phone_line(rep, items):
    """One sentence, under a notification's worth of characters."""
    if not items:
        return ""
    head = (f"{len(items)} thing(s) need you after the {rep['date']} fare run: "
            + "; ".join(k for k, _ in items[:4]))
    if len(items) > 4:
        head += f"; +{len(items) - 4} more"
    url = os.environ.get("RUN_URL", "")
    return head + (f"\n{url}" if url else "")


def main():
    today = dt.date.today().isoformat()
    rep = load_report(today)
    items = problems(rep)
    state = hashlib.sha256(
        "|".join(sorted(k for k, _ in items)).encode()).hexdigest()[:16]

    alert = pathlib.Path(os.environ.get("PHONE_ALERT", "/tmp/phone-alert.txt"))
    try:
        alert.write_text(phone_line(rep, items), encoding="utf-8")
    except OSError:
        pass

    code, out, err = gh("issue", "list", "--label", LABEL, "--state", "open",
                        "--json", "number,body", "--limit", "1")
    if code != 0:
        print(f"could not list issues ({err[:200]}); printing instead\n")
        print(body(rep, items, state))
        return 0
    existing = json.loads(out or "[]")

    if not items:
        if existing:
            n = str(existing[0]["number"])
            gh("issue", "close", n, "--comment",
               f"All rows refreshed cleanly on {today}. Nothing left to decide.")
            print(f"closed #{n}: all clear")
        else:
            print("all clear, no issue open")
        return 0

    text = body(rep, items, state)

    if existing:
        n = str(existing[0]["number"])
        was = existing[0].get("body", "")
        same = MARK + state in was
        gh("issue", "edit", n, "--body", text)
        if same:
            print(f"#{n} already describes these {len(items)} item(s); "
                  f"updated in place without a comment")
        else:
            gh("issue", "comment", n, "--body",
               f"Updated after the {today} run. {len(items)} item(s) need a "
               f"decision; see the issue body.")
            print(f"#{n} updated and commented ({len(items)} item(s))")
        return 0

    code, out, err = gh("issue", "create", "--title", f"{TITLE} ({today})",
                        "--label", LABEL, "--body", text,
                        "--assignee", os.environ.get("OWNER", "@me"))
    if code != 0:
        # most likely the label does not exist yet: make it and retry once
        gh("label", "create", LABEL, "--color", "B60205",
           "--description", "Scheduled fare refresh needs an operator decision")
        code, out, err = gh("issue", "create", "--title", f"{TITLE} ({today})",
                            "--label", LABEL, "--body", text,
                            "--assignee", os.environ.get("OWNER", "@me"))
    if code != 0:
        print(f"could not open an issue ({err[:200]}); printing instead\n")
        print(text)
    else:
        print(f"opened {out} ({len(items)} item(s))")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:                      # noqa: BLE001
        # the notifier is not allowed to fail the job
        print(f"notifier error, refresh itself was unaffected: {exc!r}")
        sys.exit(0)
