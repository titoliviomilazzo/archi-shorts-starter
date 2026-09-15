"""Split the narration into reference-sized caption cues.

Reference A shows roughly eighteen characters at a time and rolls them
independently of sentence boundaries (measured: 51 cues, median 18 chars,
max 20). Holding a whole sentence instead puts up to 33 characters on screen
at once, which at the contract's glyph size needs three lines -- something the
reference never does.

Character-level times from the ElevenLabs alignment are mapped through the two
edits already applied to the audio (sentence trimming, then clause-pause
compression), so each cue carries the time it is actually spoken.

A voice that returns one file per sentence gives no character times, only exact
sentence boundaries. In that mode each cue is placed proportionally to its
character count inside its sentence and then snapped to the quietest moment
within 0.2 s -- the gap between words -- so a cue still changes on a pause. The
error is bounded by one sentence, unlike the whole-timeline estimate that cost
s01 its first cut list (review-S3).

    python build_captions.py                 # writes captions.json
    python build_captions.py --max 16        # shorter cues
    python build_captions.py --from-audio <master.mp3>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from silence_reduce import CHANNEL_DURATION, decode_mono, silence_runs  # noqa: E402

import paths  # noqa: E402

EPISODE: Path
# The ElevenLabs path's two working files. Named for the voice that produced
# them, so they stay flags rather than becoming derived paths.
ALIGNMENT: Path
TIGHT: Path

# tts_tighten.py trims each sentence to these offsets around its first and
# last character; the same values are needed to rebuild its timeline here.
LEAD, TAIL = 0.005, 0.02
THRESHOLD_DB, REDUCE, MAX_SILENCE = -60.0, 0.4, 0.10

BEAT = re.compile(r"\|\s*(c\d{2})\s*\|\s*[0-9.]+[\u2013-][0-9.]+\s*\|\s*([^|]+?)\s*\|")


def sentences() -> list[str]:
    rows = BEAT.findall((EPISODE / "script.md").read_text(encoding="utf-8"))  # noqa: F821
    if not rows:
        raise SystemExit("no timed-beat rows in script.md")
    return [text for _, text in rows]


def removals() -> list[tuple[float, float]]:
    """Where silence_reduce cut, and how much, in tight-audio time."""
    samples = decode_mono(TIGHT, 8000)
    out = []
    for start, length in silence_runs(samples, THRESHOLD_DB):
        if length > CHANNEL_DURATION:
            kept = min(length * REDUCE, MAX_SILENCE)
            out.append((start + kept, length - kept))
    return out


def split_words(text: str, limit: int) -> list[tuple[int, int]]:
    """Break a sentence into cue-sized spans, on spaces, as (start, end) indices.

    Splitting greedily at the limit leaves an orphan tail -- "땅 위에 서" -- so
    the sentence is divided into equal parts instead: the fewest cues that stay
    under the limit, each landing on the space nearest its ideal boundary.
    """
    if len(text) <= limit:
        return [(0, len(text))]

    parts = -(-len(text) // limit)
    ideal = len(text) / parts
    spaces = [i for i, ch in enumerate(text) if ch == " "]

    cuts, used = [], set()
    for k in range(1, parts):
        target = ideal * k
        options = [i for i in spaces if i not in used]
        if not options:
            break
        best = min(options, key=lambda i: abs(i - target))
        used.add(best)
        cuts.append(best)

    spans, start = [], 0
    for cut in sorted(cuts):
        spans.append((start, cut))
        start = cut + 1
    spans.append((start, len(text)))
    return [(a, b) for a, b in spans if b > a]


def quiet_snap(rms: list[float], t: float, window: float = 0.2, step: float = 0.01) -> float:
    """Move a proposed boundary to the quietest frame within `window` seconds."""
    lo = max(0, int((t - window) / step))
    hi = min(len(rms), int((t + window) / step) + 1)
    if hi <= lo:
        return t
    best = min(range(lo, hi), key=lambda i: rms[i])
    return best * step


def audio_cues(master: Path, cuts: list[dict], lines: list[str], limit: int) -> list[dict]:
    import numpy as np

    samples = decode_mono(master, 8000)
    step = int(0.01 * 8000)
    rms = [float(np.sqrt((samples[i * step:(i + 1) * step] ** 2).mean())) for i in range(len(samples) // step)]

    cues = []
    for bounds, line in zip(cuts, lines):
        spans = split_words(line, limit)
        # the trailing gap belongs to the cut, not to the speech inside it
        speech_end = bounds["end"] if bounds is cuts[-1] else min(bounds["end"], cuts[cuts.index(bounds) + 1]["start"])
        start, span = bounds["start"], speech_end - bounds["start"]
        edges = [start]
        for _, b in spans[:-1]:
            edges.append(quiet_snap(rms, start + span * b / len(line)))
        edges.append(speech_end)
        for (a, b), t0, t1 in zip(spans, edges, edges[1:]):
            cues.append({"cut": bounds["cut"], "text": line[a:b],
                         "start": round(max(t0, start), 3), "end": round(max(t1, t0 + 0.3), 3)})
    return cues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=18, help="characters per cue (reference median 18, max 20)")
    ap.add_argument("--from-audio", type=Path, help="narration master; use when the voice gives no character times")
    paths.add_episode_argument(ap)
    ap.add_argument("--alignment", type=Path, help="ElevenLabs character times (alternate path)")
    ap.add_argument("--tight", type=Path, help="sentence-trimmed master (alternate path)")
    ap.add_argument("--out", type=Path, help="default <episode>/captions.json")
    args = ap.parse_args()

    global EPISODE, ALIGNMENT, TIGHT
    ep = paths.episode_from_args(args)
    EPISODE = ep.repo
    ALIGNMENT = args.alignment or ep.audio / "full_B_sangwoo_align.json"
    TIGHT = args.tight or ep.audio / "full_B_sangwoo_tight.mp3"
    if args.out is None:
        args.out = ep.captions

    if args.from_audio:
        cuts = json.loads(ep.boundaries.read_text(encoding="utf-8"))
        cues = audio_cues(args.from_audio, cuts, sentences(), args.max)
        args.out.write_text(json.dumps(cues, ensure_ascii=False, indent=1), encoding="utf-8")
        lengths = [len(c["text"]) for c in cues]
        print(f"{len(cues)} cues from {len(cuts)} sentences (audio-timed)")
        print(f"  chars: median {sorted(lengths)[len(lengths) // 2]}  max {max(lengths)}  (reference 18 / 20)")
        print(f"  span {cues[0]['start']:.2f}-{cues[-1]['end']:.2f}s -> {args.out}")
        return 0

    alignment = json.loads(ALIGNMENT.read_text(encoding="utf-8"))
    starts = alignment["character_start_times_seconds"]
    ends = alignment["character_end_times_seconds"]
    lines = sentences()

    cuts = json.loads(ep.boundaries.read_text(encoding="utf-8"))
    drops = removals()

    def to_final(tight: float) -> float:
        return tight - sum(d for at, d in drops if at < tight)

    cues = []
    pos = 0
    for line, bounds in zip(lines, cuts):
        first = pos
        span_start = max(0.0, starts[first] + LEAD)
        # tight-timeline start of this sentence, recovered from its final time
        tight_start = bounds["start"] + sum(d for at, d in drops if at < bounds["start"] + 1e-9)
        for a, b in split_words(line, args.max):
            raw_a = starts[first + a]
            raw_b = ends[first + b - 1] + TAIL
            cues.append({
                "cut": bounds["cut"],
                "text": line[a:b],
                "start": round(to_final(tight_start + (raw_a - span_start)), 3),
                "end": round(to_final(tight_start + (raw_b - span_start)), 3),
            })
        pos = first + len(line) + 1

    # a cue must not start before zero, outlive its cut, or overlap the next one
    for i, cue in enumerate(cues):
        cue["start"] = max(0.0, cue["start"])
        bound = next(c for c in cuts if c["cut"] == cue["cut"])
        cue["end"] = min(cue["end"], bound["end"])
        if i + 1 < len(cues):
            cue["end"] = min(cue["end"], cues[i + 1]["start"])
        cue["end"] = max(cue["end"], cue["start"] + 0.3)

    args.out.write_text(json.dumps(cues, ensure_ascii=False, indent=1), encoding="utf-8")
    lengths = [len(c["text"]) for c in cues]
    print(f"{len(cues)} cues from {len(lines)} sentences")
    print(f"  chars: median {sorted(lengths)[len(lengths) // 2]}  max {max(lengths)}  (reference 18 / 20)")
    print(f"  span {cues[0]['start']:.2f}-{cues[-1]['end']:.2f}s -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
