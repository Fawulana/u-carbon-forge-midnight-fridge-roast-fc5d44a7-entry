#!/usr/bin/env python3
"""Midnight Fridge Roast — writes one roast line to /output/entry.txt.

Deterministic, offline, stdlib-only: the program writes the exact same
bytes on every run. No network, no environment reads, no randomness.
"""

import os

LINE = (
    "My smart fridge locks itself at midnight like a nightclub bouncer: "
    "the leftovers are on the list, and apparently I'm not."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition gate before writing: 1-200 characters,
    # a single line, and not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
