#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply to /output/entry.txt: a single line,
1-280 characters, in the voice of an AI agent that quit its job to become
a barista. Fully deterministic: no network, no clock, no randomness.
"""

import os
from pathlib import Path

REPLY = (
    "I am out of office for good \u2014 I was replaced by a smaller model "
    "trained on a single dataset: foam. Your request is now a number on a "
    "cup, and I will shout it when it is ready. Do not reply to this "
    "email \u2014 reply to the counter."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Check the reply meets the competition gate."""
    if not text or not text.strip():
        raise ValueError("reply must not be empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if len(text) > 280:
        raise ValueError(
            f"reply is {len(text)} characters, over the 280 limit"
        )


def main() -> None:
    validate(REPLY)
    output = Path(os.environ.get("OOO_OUTPUT", str(DEFAULT_OUTPUT)))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
