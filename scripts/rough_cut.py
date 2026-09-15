"""Rough cut: lay finished kit clips on the narration timeline, in cut order.

Each kit covers a contiguous cut range (c01-c03 ...). The clip is retimed so its
whole length fills exactly that narration span (+ the dissolve overlap), kits are
joined with 0.4 s dissolves at the cut boundaries, and the narration is mixed over
the clips' own sound (rain, stone, water). No subtitles, no EDL windows — this is
the "let's watch it in order" preview, not assemble.py's final render.

    python scripts/rough_cut.py --episode s02-venezia-pozzo \
        --kit K1=c01-c03 --kit K2=c04-c05 --kit K3_join=c06-c08 \
        --kit K4=c09-c11 --kit K5=c12-c14 --out <clips>/rough_K1-K5.mp4

Reports the retime factor per kit; anything outside 0.94x-1.30x is flagged
(production-spec 4.4.3 step 1: stretch <= 6 %, speed-up is the channel norm).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

# Starter-kit default: media lives under the kit root's media/ folder.
# Override with ARCHI_SHORTS_MEDIA if the media should live elsewhere.
MEDIA_ROOT = Path(os.environ.get("ARCHI_SHORTS_MEDIA", str(Path.cwd() / "media")))
XFADE = 0.4
SFX_GAIN = 0.35
TARGET_DBFS = -18.0   # style-contract / review gate: -18.0 +- 0.7 dBFS RMS


def probe_duration(path: Path) -> float:
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", str(path)], text=True)
    return float(out.strip())


def atempo_chain(rate: float) -> str:
    """ffmpeg atempo accepts 0.5-2.0 per stage; chain for anything outside."""
    parts = []
    while rate > 2.0:
        parts.append("atempo=2.0")
        rate /= 2.0
    while rate < 0.5:
        parts.append("atempo=0.5")
        rate /= 0.5
    parts.append(f"atempo={rate:.5f}")
    return ",".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    ap.add_argument("--kit", action="append", required=True, help="NAME=cAA-cBB (clip <clips>/NAME_gflow.mp4 or NAME.mp4)")
    ap.add_argument("--narration", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--boundaries", type=Path, help="cut_boundaries json (default <episode>/cut_boundaries.json)")
    args = ap.parse_args()

    ep = MEDIA_ROOT / args.episode
    clips_dir = ep / "clips"
    repo_ep = Path(__file__).resolve().parent.parent / "episodes" / args.episode
    cuts = {c["cut"]: (c["start"], c["end"]) for c in json.load(open(args.boundaries or repo_ep / "cut_boundaries.json", encoding="utf-8"))}
    narration = args.narration or ep / "audio" / "narration.mp3"
    out = args.out or clips_dir / ("rough_" + "-".join(k.split("=")[0] for k in args.kit) + ".mp4")

    kits = []
    for spec in args.kit:
        name, rng = spec.split("=")
        a, b = rng.split("-")
        start, end = cuts[a][0], cuts[b][1]
        clip = clips_dir / f"{name}_gflow.mp4"
        if not clip.exists():
            clip = clips_dir / f"{name}.mp4"
        kits.append((name, clip, start, end))
    kits.sort(key=lambda k: k[2])
    t0 = kits[0][2]
    t_end = kits[-1][3]

    inputs, vparts, aparts = [], [], []
    for i, (name, clip, start, end) in enumerate(kits):
        span = end - start + (XFADE if i < len(kits) - 1 else 0.0)
        src = probe_duration(clip)
        rate = src / span                      # >1 = speed-up, <1 = slow-mo
        flag = "" if 0.94 <= rate <= 1.30 else "   <-- outside 0.94x-1.30x"
        print(f"{name:8s} {clip.name:22s} src {src:5.2f}s -> {span:5.2f}s  x{rate:.3f}{flag}")
        inputs += ["-i", str(clip)]
        vparts.append(f"[{i}:v]setpts=PTS/{rate:.6f},fps=24,scale=720:1280,format=yuv420p,trim=0:{span:.4f},setpts=PTS-STARTPTS[v{i}]")
        aparts.append(f"[{i}:a]{atempo_chain(rate)},atrim=0:{span:.4f},asetpts=PTS-STARTPTS[a{i}]")

    # chain xfades / acrossfades at the cut boundaries
    vprev, aprev, offset = "v0", "a0", 0.0
    chain = []
    for i in range(1, len(kits)):
        offset += kits[i - 1][3] - kits[i - 1][2]        # boundary on the narration timeline
        chain.append(f"[{vprev}][v{i}]xfade=transition=dissolve:duration={XFADE}:offset={offset - 0.0:.4f}[vx{i}]")
        chain.append(f"[{aprev}][a{i}]acrossfade=d={XFADE}[ax{i}]")
        vprev, aprev = f"vx{i}", f"ax{i}"
    n = len(kits)
    inputs += ["-i", str(narration)]
    nar = (f"[{n}:a]atrim={t0:.4f}:{t_end:.4f},asetpts=PTS-STARTPTS[nar];"
           f"[{aprev}]volume={SFX_GAIN}[sfx];[nar][sfx]amix=inputs=2:duration=first:normalize=0,"
           f"volume=-1.1dB,alimiter=limit=0.891:level=false[aout]")
    graph = ";".join(vparts + aparts + chain + [nar])
    cmd = ["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", graph, "-map", f"[{vprev}]", "-map", "[aout]",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "17", "-preset", "medium",
           "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k", "-movflags", "+faststart", "-shortest", str(out)]
    subprocess.run(cmd, check=True)
    print(f"{out}  ({probe_duration(out):.2f}s; narration span {t0:.2f}-{t_end:.2f} = {t_end - t0:.2f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
