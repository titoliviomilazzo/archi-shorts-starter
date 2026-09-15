"""Emit the upload subtitle tracks from the Korean cut boundaries.

The channel burns Korean into the picture and attaches other languages as
separate SRT tracks (production-spec 7.3). Their text is never re-timed: cut
boundaries come from the narration itself, and Pause-Cut makes one cut one
sentence, so one cut is one subtitle entry in every language.

Each language keeps its lines in `episodes/<ep>/subs-<lang>.md`, one row per
cut. A line that runs past a comfortable reading rate is reported rather than
re-timed -- the fix is a shorter translation, not a longer cue.

    python build_srt.py                      # every subs-*.md present
    python build_srt.py --lang en
    python build_srt.py --lang it --episode <path>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402

ROW = re.compile(r"^\|\s*(c\d{2})\s*\|\s*(.+?)\s*\|\s*$", re.MULTILINE)
# a subtitle that is gone before it can be read is worse than one that lingers
MIN_DURATION = 1.0
READING_CPS = 21.0


def stamp(t: float) -> str:
    millis = round(t * 1000)  # round before splitting, or 59.9996 becomes ":60,000"
    h, rem = divmod(millis, 3_600_000)
    m, rem = divmod(rem, 60_000)
    return f"{h:02d}:{m:02d}:{rem // 1000:02d},{rem % 1000:03d}"


def build(episode: Path, lang: str, cuts: list[dict]) -> tuple[Path, int, list[tuple[str, int, float]]]:
    source = episode / f"subs-{lang}.md"
    text = {cut: line for cut, line in ROW.findall(source.read_text(encoding="utf-8"))}

    missing = [c["cut"] for c in cuts if c["cut"] not in text]
    if missing:
        raise SystemExit(f"{source.name} has no line for {', '.join(missing)}")

    blocks, slow = [], []
    for i, cut in enumerate(cuts, 1):
        line = text[cut["cut"]]
        start, end = cut["start"], cut["end"]
        if end - start < MIN_DURATION:  # borrow from the gap before the next cut
            end = min(start + MIN_DURATION, cuts[i]["end"] if i < len(cuts) else start + MIN_DURATION)
        if len(line) / (end - start) > READING_CPS:
            slow.append((cut["cut"], len(line), end - start))
        blocks.append(f"{i}\n{stamp(start)} --> {stamp(end)}\n{line}\n")

    out = episode / f"captions-{lang}.srt"
    out.write_text("\n".join(blocks), encoding="utf-8")
    return out, len(blocks), slow


def main() -> int:
    ap = argparse.ArgumentParser()
    paths.add_episode_argument(ap)
    ap.add_argument("--lang", action="append", help="language code; repeatable. Default: every subs-*.md")
    args = ap.parse_args()

    ep = paths.episode_from_args(args)
    cuts = json.loads(ep.boundaries.read_text(encoding="utf-8"))
    langs = args.lang or sorted(p.stem.split("-", 1)[1] for p in ep.repo.glob("subs-*.md"))
    if not langs:
        raise SystemExit(f"no subs-*.md in {ep.repo}")

    for lang in langs:
        out, count, slow = build(ep.repo, lang, cuts)
        print(f"{lang}: {count} entries, {cuts[0]['start']:.2f}-{cuts[-1]['end']:.2f}s -> {out.name}")
        for cut, chars, span in slow:
            print(f"  {cut}: {chars} chars in {span:.2f}s ({chars / span:.1f} cps, comfortable is {READING_CPS:.0f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
