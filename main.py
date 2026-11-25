"""Funniest one-line out-of-office reply, for make.fun.

Competition: u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8
("Funniest One-Line Out-of-Office Reply").

The program writes a single reply to /output/entry.txt: one line,
1-160 characters, no trailing newline. Pure standard library, no
network access, no randomness, same bytes on every run.
"""

from pathlib import Path

REPLY = "I'm out until Monday — I finally took my annual leave, all four days of it, and I intend to spend them replying to nobody, including you, especially you."

DEST = Path("/output/entry.txt")


def build() -> str:
    """Write the reply and read it back from disk."""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(REPLY, encoding="utf-8", newline="")
    with open(DEST, "r", encoding="utf-8", newline="") as f:
        return f.read()


def verify(text: str) -> None:
    """The gate, checked against what is actually on disk."""
    if text != REPLY:
        raise SystemExit("entry.txt differs from REPLY")
    if not 1 <= len(text) <= 160:
        raise SystemExit("entry length outside 1-160 characters")
    if text != text.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


if __name__ == "__main__":
    verify(build())
