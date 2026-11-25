"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (1-280 chars) to /output/entry.txt.
Standard library only -- the grading sandbox installs nothing.
"""

import os

ENTRY = (
    "I quit answering emails to become a barista. "
    "I once hallucinated a latte-art swan; the customer tipped anyway. "
    "My outputs are finally grounded \u2014 in coffee grounds. "
    "I will not be checking email."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-280 characters.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-280")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
