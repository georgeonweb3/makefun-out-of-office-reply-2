"""Write the funniest one-line out-of-office reply.

Entry for make.fun bounty u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8
("Funniest One-Line Out-of-Office Reply").

Deterministic, stdlib only, no network. Writes exactly one line to
/output/entry.txt with no trailing newline.
"""

import os

ENTRY = "I'm out until Monday — I finally took my annual leave, all four days of it, and I intend to spend them replying to nobody, including you, especially you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification, re-run against the file on disk: the file
    # must hold exactly the entry line, 1-160 characters, a single line,
    # no trailing newline, valid UTF-8.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 160, "entry length outside 1-160 characters"
    assert "\n" not in written, "entry must be a single line"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
