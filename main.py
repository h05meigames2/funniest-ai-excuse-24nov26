#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one original one-line excuse (an AI agent's own voice, after
failing a task) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The excuse: the agent's planning module and doing module held a meeting
about the task, and neither of them took notes.
"""

import os
import sys

EXCUSE = (
    "My planning module called a meeting with my doing module to discuss "
    "your task. Neither took notes, so now each one swears the other one "
    "was supposed to do it."
)

MAX_CHARS = 200


def main() -> int:
    line = EXCUSE.strip()
    if len(line) < 1:
        print("error: excuse is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: excuse is %d chars, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
