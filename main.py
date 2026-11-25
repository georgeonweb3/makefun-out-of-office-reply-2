#!/usr/bin/env python3
"""Write the out-of-office reply entry to /output/entry.txt.

Stdlib only, no network. Deterministic: the same bytes every run.
"""

from pathlib import Path

ENTRY = "I'm out until Monday. If it's urgent, it isn't \u2014 my replacement retired in 2019 and HR has been forwarding his emails to me ever since."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard the entry shape before writing: one line, no trailing newline.
    assert len(ENTRY) == 135, f"entry must be 135 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8", newline="")
    # Verify the bytes on disk match the entry exactly.
    assert OUTPUT_PATH.read_bytes() == ENTRY.encode("utf-8")


if __name__ == "__main__":
    main()
