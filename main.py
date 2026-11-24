"""Worst AI Advice entry: writes one line of the worst possible advice
an AI could give to /output/entry.txt.

Entry line (108 characters, single line, no trailing newline):
    "If your laptop is overheating, pour a glass of cold water over the
    keyboard to cool the processor down fast."

Competition gate: the entry must be at most 140 characters. This module
asserts that limit (and the single-line rule) before writing anything, so
an over-long line fails loudly here instead of at grading time.
"""

import os

ENTRY = "If your laptop is overheating, pour a glass of cold water over the keyboard to cool the processor down fast."

MAX_CHARS = 140


def main():
    # Enforce the competition gates before touching the output file.
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char limit"
    )
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
