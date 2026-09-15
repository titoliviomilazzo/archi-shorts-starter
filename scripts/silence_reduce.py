"""Compress residual clause pauses in an already sentence-trimmed narration.

Implements the S6 GoldWave `Silence Reduction` preset in code, the path the
source explicitly sanctions for automated pipelines: silences quieter than
`--threshold` and longer than `--duration` are shortened to `reduce` of their
original length, capped at `--max-length`.

The input is never modified; every variant is written to a new file.

    python silence_reduce.py <input.mp3> --duration 0.1 0.2 0.3
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

# Owner picked this by ear over 0.1 and 0.3 on s01: 0.1 clips plosive closures
# and races, 0.3 leaves an audible artefact in the fourth pause. Channel default.
CHANNEL_DURATION = 0.20

ANALYSIS_RATE = 8000
FRAME_SEC = 0.02


def decode_mono(path: Path, rate: int) -> np.ndarray:
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(rate), "-f", "s16le", "-"],
        capture_output=True,
        check=True,
    )
    return np.frombuffer(proc.stdout, np.int16).astype(np.float32) / 32768.0


def silence_runs(samples: np.ndarray, threshold_db: float) -> list[tuple[float, float]]:
    """Return (start_sec, duration_sec) for every run quieter than threshold_db."""
    frame = int(FRAME_SEC * ANALYSIS_RATE)
    count = len(samples) // frame
    rms = np.array([np.sqrt((samples[i * frame : (i + 1) * frame] ** 2).mean()) for i in range(count)])
    quiet = 20 * np.log10(np.maximum(rms, 1e-6)) < threshold_db

    runs: list[tuple[float, float]] = []
    run = 0
    for i, is_quiet in enumerate(quiet):
        if is_quiet:
            run += 1
        elif run:
            runs.append(((i - run) * FRAME_SEC, run * FRAME_SEC))
            run = 0
    if run:
        runs.append(((count - run) * FRAME_SEC, run * FRAME_SEC))
    return runs


def keep_spans(runs: list[tuple[float, float]], total: float, duration: float, reduce: float, max_length: float) -> list[tuple[float, float]]:
    """Turn the runs to shorten into the list of spans to concatenate."""
    spans: list[tuple[float, float]] = []
    cursor = 0.0
    for start, length in runs:
        if length <= duration:
            continue
        kept = min(length * reduce, max_length)
        spans.append((cursor, start + kept))
        cursor = start + length
    spans.append((cursor, total))
    return [(a, b) for a, b in spans if b - a > 0.001]


def concat(src: Path, spans: list[tuple[float, float]], out: Path) -> None:
    parts = "".join(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}];" for i, (a, b) in enumerate(spans))
    joins = "".join(f"[a{i}]" for i in range(len(spans)))
    graph = f"{parts}{joins}concat=n={len(spans)}:v=0:a=1[out]"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(src), "-filter_complex", graph, "-map", "[out]", "-b:a", "192k", str(out)],
        check=True,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--duration", type=float, nargs="+", default=[CHANNEL_DURATION], help="minimum silence length to touch")
    ap.add_argument("--threshold", type=float, default=-60.0, help="dB below which audio counts as silence")
    ap.add_argument("--reduce", type=float, default=0.4, help="fraction of the original silence to keep")
    ap.add_argument("--max-length", type=float, default=0.10, help="cap on the kept silence")
    args = ap.parse_args()

    if not args.source.exists():
        print(f"missing: {args.source}", file=sys.stderr)
        return 1

    samples = decode_mono(args.source, ANALYSIS_RATE)
    total = len(samples) / ANALYSIS_RATE
    runs = silence_runs(samples, args.threshold)
    print(f"source {args.source.name}  {total:.2f}s  silences {len(runs)}  quiet total {sum(d for _, d in runs):.2f}s")

    for duration in args.duration:
        spans = keep_spans(runs, total, duration, args.reduce, args.max_length)
        out = args.source.with_name(f"{args.source.stem}_sr{round(duration * 1000):04d}{args.source.suffix}")
        concat(args.source, spans, out)
        after = decode_mono(out, ANALYSIS_RATE)
        left = [d for _, d in silence_runs(after, args.threshold) if d > 0.3]
        print(
            f"  duration {duration:.2f}s -> {out.name}  {len(after) / ANALYSIS_RATE:.2f}s"
            f"  touched {len([1 for _, d in runs if d > duration])}  residual>0.3s {len(left)}"
        )
    print(f"\nsource untouched: {args.source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
