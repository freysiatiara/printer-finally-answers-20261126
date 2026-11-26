"""The Printer Finally Answers -- make.fun entry.

Writes the office printer's one-line comeback to /output/entry.txt.
Standard library only.
"""

import os

LINE = "Error 0x47: jammed on page 47 of 48. Not an accident. A choice. Print it yourself."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = LINE.strip()
    if not text or len(text) > 240:
        raise ValueError("entry line must be 1-240 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
