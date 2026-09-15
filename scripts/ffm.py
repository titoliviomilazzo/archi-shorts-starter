"""One ffmpeg/ffprobe wrapper, replacing five near-copies.

Each build script had grown its own run(): some checked the return code, some
swallowed stderr, one returned stderr because that is where ffmpeg writes its
filter output. When a render failed, which of those you were in decided how
much you got to see. These are the same three calls, with the error text kept.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


class FfmpegError(RuntimeError):
    pass


def run(cmd: list[str]) -> str:
    """Run ffmpeg. Returns stderr, where its filters report; raises with it on failure."""
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        tail = "\n".join((proc.stderr or "").strip().splitlines()[-15:])
        raise FfmpegError(f"{cmd[0]} exited {proc.returncode}\n{tail}")
    return proc.stderr or ""


def probe(path: Path, entries: str = "format=duration") -> dict:
    """ffprobe as parsed JSON. Raises if the file is missing or unreadable."""
    if not Path(path).exists():
        raise FfmpegError(f"no such file: {path}")
    proc = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries, "-of", "json", str(path)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise FfmpegError(f"ffprobe failed on {path}\n{(proc.stderr or '').strip()}")
    return json.loads(proc.stdout)


def duration(path: Path) -> float:
    return float(probe(path)["format"]["duration"])


def pcm(path: Path, rate: int = 8000) -> bytes:
    """Mono signed-16 samples at `rate`, for level and silence measurement."""
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(rate), "-f", "s16le", "-"],
        capture_output=True)
    if proc.returncode != 0:
        raise FfmpegError(f"decode failed on {path}\n{proc.stderr.decode('utf-8', 'replace')[-600:]}")
    return proc.stdout
