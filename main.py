#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — entry program.

The entry is a one-star review written by a house cat about its human.
This program writes that single line to /output/entry.txt as UTF-8
text. No trailing newline is added: the review's characters are the
whole file.
"""

import os
from pathlib import Path


def review_text() -> str:
    """Assemble the review: star rating first, then the complaint."""
    stars = "★☆☆☆☆"
    complaint = (
        "Opens my doors only to close them again, screams at the mouse "
        "I gifted him, and pays rent in chin scratches. I am the "
        "landlord. He is the problem."
    )
    return f"{stars}. {complaint}"


def main() -> None:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(review_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
