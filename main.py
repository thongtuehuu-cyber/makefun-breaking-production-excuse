#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to entry.txt.

Deterministic: the same line, byte-for-byte, on every run. The output is a
single line with no trailing newline.
"""

import os
import sys

LINE = (
    "The feature flag said 1%, the load balancer heard 100%, "
    "and I have decided to blame the load balancer, "
    "since it cannot defend itself in this meeting."
)

def validate_line(line: str) -> str:
    """Check the entry line meets the bounty rules and return it unchanged."""
    if not line:
        raise ValueError("line is empty")
    if len(line) > 180:
        raise ValueError("line exceeds 180 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Write the validated line to entry.txt (no trailing newline)."""
    line = validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        write_entry(LINE, out_dir)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
