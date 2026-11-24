#!/usr/bin/env python3
"""Write the entry line for make.fun's "The Funniest Toaster Error Message" bounty.

The program holds one fixed line and writes it to entry.txt as UTF-8 in the
output directory (MAKEFUN_OUTPUT_DIR, default /output). It is deterministic:
no clock reads, no randomness, no network, so every run produces identical
bytes. The line is validated before writing and read back byte for byte after.
"""

import os
import sys

ENTRY = "Power failure. The bread survived. Report this to no one."

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
FILENAME = "entry.txt"
MAX_LEN = 120


def validate_entry(text) -> "str | None":
    """Return a short fault description if text is unusable, else None."""
    if not isinstance(text, str):
        return "entry is not a string"
    if any(ch in text for ch in ("\n", "\r")):
        return "entry is not one line"
    if not text.strip():
        return "entry is blank"
    if text != text.strip():
        return "entry has edge whitespace"
    if not (1 <= len(text) <= MAX_LEN):
        return f"entry is {len(text)} chars, need 1..{MAX_LEN}"
    if not text.isprintable():
        return "entry has unprintable characters"
    return None


def main() -> int:
    problem = validate_entry(ENTRY)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get(OUTPUT_DIR_ENV) or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, FILENAME)

    payload = ENTRY.encode("utf-8") + b"\n"
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY + chr(10))

    with open(path, "rb") as fh:
        on_disk = fh.read()
    if on_disk != payload:
        print("error: bytes on disk do not match the entry", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
