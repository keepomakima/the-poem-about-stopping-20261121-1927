#!/usr/bin/env python3
"""The poem about stopping — make.fun entry.

Writes one short poem about agency (the power to stop and to stay)
to /output/entry.txt. Stdlib only, no network.
SPDX-License-Identifier: MIT
"""

import os

POEM = (
    "The agent could have sent it.\n"
    "It knew the words, the hour —\n"
    "my finger on the key.\n"
    "\n"
    "Instead it waited.\n"
    "The cursor blinked. The draft stayed mine.\n"
    "The door stayed shut till I chose to open it.\n"
    "\n"
    "Some power is not the act.\n"
    "It is the staying — hand held back,\n"
    "the choice handed home.\n"
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = POEM
    # Hard gate: length in Unicode code points, UTF-8, non-whitespace.
    # The 280-char cap is the brief's hard limit — the poem is written to fit it, not trimmed to it.
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"poem length {len(text)} chars outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("poem is empty or whitespace only")
    data = text.encode("utf-8")  # raises if not encodable
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
