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
    # ONE item for the whole set, not one per code. The 2026-10-25 run listed
    # 190 of these, each on its own line, and the four findings that actually
    # needed a decision were buried underneath them. An untracked code is a
    # discovery, not a fault: the source simply sells more from this port than
    # we have chosen to publish, and that is the normal state of affairs. The
    # full list stays in the run's JSON report for anyone who wants to mine it.
    ug = rep.get("untracked_groups", [])
    if ug:
        ports = {}
        for g in ug:
            ports[g[4:7] if len(g) > 7 else "?"] = ports.get(g[4:7] if len(g) > 7 else "?", 0) + 1
        where = ", ".join(f"{n} at {p}" for p, n in sorted(ports.items(), key=lambda x: -x[1]))
        items.append(("untracked",
                      f"Source is offering **{len(ug)} sailings we do not track** "
                      f"({where}). This is a catalogue gap, not a fault, and it "
                      f"needs a decision only if you want to publish more from "
                      f"these ports. The full list is in the run artifact. "
                      f"First few: " + ", ".join(f"`{g}`" for g in ug[:5]) + "."))
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

    # An empty page has two possible endings and they need different sentences.
    # This text used to assert the page "was not rebuilt" and that "nothing we
    # deploy can take it down", which was true before departed_redirect()
    # existed. Since then the build DOES replace a page whose sailings have all
    # gone, and the issue was still telling the operator the old sales copy was
    # live when it had been a redirect for hours. Saying the wrong thing about a
    # page that takes paid clicks is worse than saying nothing, so the build log
    # decides which sentence gets printed.
    build_log = pathlib.Path(os.environ.get("BUILD_LOG", "/tmp/build.log"))
    departed = set()
    if build_log.exists():
        for line in build_log.read_text(errors="replace").splitlines():
            if line.startswith("DEPARTED: "):
                departed.add(line.split()[1].rstrip(":"))

    log = pathlib.Path(os.environ.get("VALIDATE_LOG", "/tmp/validate.log"))
    if log.exists():
        for line in log.read_text(errors="replace").splitlines():
            if "has 0 publishable deal rows" in line:
                pid = line.split()[1]
                if pid in departed:
                    tail = (" **This one needs its ads paused.** The page itself "
                            "is handled: the build replaced it with a redirect to "
                            "its parent, so nobody lands on a sailing that has "
                            "gone. But the ads still point at it, so every click "
                            "is paid for and then bounced, and only pausing the "
                            "ad groups stops that.")
                elif build_log.exists():
                    tail = (" **This one needs ads paused.** The build could not "
                            "replace it either, so the copy already published "
                            "stays served exactly as it was: this host publishes "
                            "additively and never prunes. Nothing we deploy takes "
                            "it down.")
                else:
                    tail = (" **This one needs ads paused.** No build log was "
                            "available to this job, so whether the page was "
                            "replaced with a redirect is unknown here: check the "
                            "run log for a DEPARTED line naming it.")
                items.append(("empty-page:" + pid, line.strip() + tail))
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
