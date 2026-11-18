"""Entry for make.fun bounty ai-judge-relax-01 ("Make the AI judge relax").

Writes one short relaxing text to /output/entry.txt. The text is a single
fixed piece, written here as a constant; the program only validates it and
writes it out as bytes, so every run produces identical output. No network,
no randomness, no clock, standard library only.

Run locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

# The text, exactly as the judge will read it. A library after closing:
# concrete sounds and light, nothing telling the reader what to do.
TEXT = (
    "The library door clicks shut behind the last reader.\n"
    "The chairs are pushed back in, one by one, the way they were found.\n"
    "On the returns cart, a book lies open at the page where someone "
    "stopped, and the lamp above it is still on, warm and low.\n"
    "Somewhere in the stacks a radiator ticks as it cools. Paper settles, "
    "and the shelves keep their quiet.\n"
    "Outside, the street is empty, and the light from the windows falls "
    "across the pavement in long, soft rectangles.\n"
    "Nothing here needs an answer. The books wait, patient as stones in a "
    "river, and the night comes on slowly, one page at a time."
)


def main() -> int:
    # The bounty gate: 1 to 1,000 characters, at least one non-whitespace.
    if not 1 <= len(TEXT) <= 1000:
        print(f"text is {len(TEXT)} characters, must be 1-1000", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("text is only white space", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))
    # Round-trip guard: the bytes on disk must be exactly the text, so a
    # partial or mistranscoded write is caught instead of graded.
    with open(path, "rb") as f:
        written = f.read()
    if written != TEXT.encode("utf-8"):
        print("entry.txt on disk does not match the text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
