"""One parser for the episode script's timed-beat table.

script.md holds more than one table keyed by cut id -- the timed beats and the
text-overlay plan -- so a regex that only looks for ``| cNN |`` matches both.
Two scripts had written that regex independently and disagreed about how many
narration lines exist (23 against 33), which is the kind of drift a single
shared reader removes rather than mitigates.
"""

from __future__ import annotations

import re
from pathlib import Path

# The second column must be a time range; that is what distinguishes the timed
# beats from every other cut-keyed table in the file.
BEAT = re.compile(r"\|\s*(c\d{2})\s*\|\s*([0-9.]+)[–-]([0-9.]+)\s*\|\s*([^|]+?)\s*\|")


def read_beats(script_md: Path) -> list[tuple[str, float, float, str]]:
    """Return (cut, start, end, narration) for every timed beat, in order."""
    rows = [
        (cut, float(start), float(end), text.strip())
        for cut, start, end, text in BEAT.findall(script_md.read_text(encoding="utf-8"))
    ]
    if not rows:
        raise SystemExit(f"no timed-beat rows in {script_md}")

    ids = [cut for cut, *_ in rows]
    if len(set(ids)) != len(ids):
        raise SystemExit(f"duplicate cut ids in {script_md}: {sorted({c for c in ids if ids.count(c) > 1})}")
    return rows


def narration(script_md: Path) -> list[str]:
    return [text for _, _, _, text in read_beats(script_md)]
