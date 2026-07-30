#!/usr/bin/env bash
# notify.sh — sends the run report (and any HOLD file) to the operator
# so a flagged run reaches their phone (Blueprint Part 6.4 step 3).
#
# Channels (configure via environment, either or both):
#   NTFY_TOPIC    - ntfy.sh topic name (push to phone)
#   NOTIFY_EMAIL  - address for `mail` (requires a working local MTA)
#
# Usage: notify.sh "subject line" [file ...]
#   With no files, sends the newest lp-system/HOLD-*.md if one exists for
#   today, plus the tail of lp-system/ratelog.md.

set -euo pipefail

LP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SUBJECT="${1:-LP system run report}"
shift || true

BODY_FILE="$(mktemp)"
trap 'rm -f "$BODY_FILE"' EXIT

if [ "$#" -gt 0 ]; then
    for f in "$@"; do
        { echo "===== $f ====="; cat "$f"; echo; } >> "$BODY_FILE"
    done
else
    TODAY_HOLD="$LP_DIR/HOLD-$(date +%F).md"
    if [ -f "$TODAY_HOLD" ]; then
        { echo "===== $TODAY_HOLD ====="; cat "$TODAY_HOLD"; echo; } >> "$BODY_FILE"
        SUBJECT="HOLD - LP run flagged $(date +%F)"
    fi
    if [ -f "$LP_DIR/ratelog.md" ]; then
        { echo "===== ratelog.md (last 40 lines) ====="; tail -n 40 "$LP_DIR/ratelog.md"; } >> "$BODY_FILE"
    fi
fi

if [ ! -s "$BODY_FILE" ]; then
    echo "notify.sh: nothing to send (no HOLD file, no ratelog)." >&2
    exit 0
fi

SENT=0

if [ -n "${NTFY_TOPIC:-}" ]; then
    if curl -fsS -H "Title: $SUBJECT" --data-binary "@$BODY_FILE" \
        "https://ntfy.sh/$NTFY_TOPIC" > /dev/null; then
        echo "notify.sh: pushed to ntfy topic '$NTFY_TOPIC'"
        SENT=1
    else
        echo "notify.sh: ntfy push failed" >&2
    fi
fi

if [ -n "${NOTIFY_EMAIL:-}" ] && command -v mail > /dev/null 2>&1; then
    if mail -s "$SUBJECT" "$NOTIFY_EMAIL" < "$BODY_FILE"; then
        echo "notify.sh: mailed $NOTIFY_EMAIL"
        SENT=1
    else
        echo "notify.sh: mail send failed" >&2
    fi
fi

if [ "$SENT" -eq 0 ]; then
    echo "notify.sh: NO CHANNEL CONFIGURED - set NTFY_TOPIC and/or NOTIFY_EMAIL." >&2
    echo "--- report that would have been sent ---" >&2
    cat "$BODY_FILE" >&2
    exit 1
fi
