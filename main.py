"""Worst AI Advice entry: writes one line of the worst possible advice
an AI could give to /output/entry.txt."""

import os

ENTRY = "If your laptop is overheating, pour a glass of cold water over the keyboard to cool the processor down fast."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
