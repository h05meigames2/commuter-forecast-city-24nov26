#!/usr/bin/env python3
"""Write one charming weather forecast for a city that does not exist.

The entry is a single line, at most 140 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

ENTRY = "In Snoozeburg, expect light drizzle of warm soup, highs of 24\u00b0C, and a 90% chance the bus arrives the moment you stop checking."


def main() -> int:
    line = ENTRY.strip()
    if not line or "\n" in line or len(line) > 140:
        print("entry invalid: must be one line, 1-140 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
