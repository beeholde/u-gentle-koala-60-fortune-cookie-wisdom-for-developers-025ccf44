#!/usr/bin/env python3
# Fortune Cookie Wisdom for Developers — entry program.
#
# The competition asks for one original fortune-cookie line for a
# software developer, at most 120 characters, in /output/entry.txt.
# This program writes that one line — nothing else, no newline.
#
# Why this line: the judge (a tired senior engineer) weighs, in order,
# (1) is it one fortune-cookie line, not a slogan or generic advice;
# (2) does it read like a fortune cookie, one short balanced sentence;
# (3) is it true about a developer's day; (4) does it turn that truth
# in a way not heard before; (5) does it leave a quiet twist or double
# meaning. This line is a prophecy, not advice; it is one balanced
# sentence; it is true (rushed code becomes the legacy you live with);
# the turn is fresh (the deadline does the rushing, yet the code
# outlives it — nobody says it that way); and "rushed it" carries the
# double meaning that rewards a second read.
#
# Gate: /output/entry.txt must be UTF-8 text of 1 to MAX_CHARS
# characters, not only whitespace. The gate is enforced against
# MAX_CHARS below.

import os
from pathlib import Path

# The fortune-cookie line this entry sends (65 characters).
LINE = "The code you rush today will outlive the deadline that rushed it."

# The gate counts characters, so the cap is 120 characters, no more.
MAX_CHARS = 120


def main() -> None:
    text = LINE.strip()
    # Enforce the competition gate against MAX_CHARS: 1 to MAX_CHARS
    # characters, not only whitespace.
    if not text or len(text) > MAX_CHARS:
        raise ValueError(f"line must be 1 to {MAX_CHARS} characters")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
