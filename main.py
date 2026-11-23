"""Write a short text that makes the AI judge feel curious.

The program writes a single text of 1-280 Unicode code points to
/output/entry.txt. The text is fixed: the same output on every run, with
no randomness, no clock, no network and no input read.

The text states a true, specific, still-unsolved fact: the Wow! signal
of 15 August 1977. A radio telescope in Ohio caught a 72-second signal
from deep space. The astronomer circled the printout (6EQUJ5) and wrote
"Wow!" in the margin. It matched nothing known, and it has never
repeated. The telescope was Ohio State University's Big Ear; the code
6EQUJ5 records the signal's intensity across six 12-second intervals.
"""

import os

ENTRY_TEXT = (
    "On 15 August 1977, a radio telescope in Ohio caught a 72-second "
    "signal from deep space. The astronomer circled the printout \u2014 "
    "6EQUJ5 \u2014 and wrote 'Wow!' in the margin. It matched nothing we "
    "know, and it has never repeated. Something out there spoke once, "
    "and then went quiet."
)


OUTPUT_FILENAME = "entry.txt"


def validate(text: str) -> int:
    """Check the entry fits the 1-280 character rule; return its length."""
    length = len(text)
    if not 1 <= length <= 280:
        raise SystemExit(f"entry must be 1-280 characters, got {length}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    return length


def main() -> None:
    text = ENTRY_TEXT
    length = validate(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Read the file back so a silent write failure is caught here, not by the grader.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise SystemExit("round-trip check failed: written text differs")
    print(f"wrote {out_path} ({length} characters)")


if __name__ == "__main__":
    main()
