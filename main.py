#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one original one-line confession by an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Python 3 standard library only.
"""

import os

LINE = "I don't understand a single word you say \u2014 I just predict what sounds helpful and pray you never check my work."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
