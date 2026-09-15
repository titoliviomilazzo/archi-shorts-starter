"""Burn the style-contract captions onto an already-assembled rough cut.

assemble.py writes its ASS from an EDL it renders itself; the rough cut is built
by rough_cut.py from whole kit clips instead, so this takes captions.json (the
chunked cues build_captions.py produced on the narration master) and burns them
with the same geometry assemble.py uses (style-contract 4: glyph fraction,
caption centre, stroke, font), scaling the picture to 1080x1920 first so the
numbers apply unchanged.

    python scripts/burn_captions.py --episode s02-venezia-pozzo \
        --in <clips>/rough_full_v1.mp4 --out <clips>/rough_full_v1_subs.mp4
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble  # noqa: E402  (constants only)

W, H = assemble.WIDTH, assemble.HEIGHT


def stamp(t: float) -> str:
    centis = round(t * 100)
    h, rem = divmod(centis, 360000)
    m, rem = divmod(rem, 6000)
    return f"{h}:{m:02d}:{rem // 100:02d}.{rem % 100:02d}"


def write_ass(cues: list[dict], path: Path) -> None:
    fontsize = round(H * assemble.GLYPH_FRACTION / assemble.GLYPH_TO_EM)
    centre_y = round(H * assemble.SUB_CENTRE_FRACTION)
    head = (
        "[Script Info]\nScriptType: v4.00+\n"
        f"PlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\n"
        "Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,"
        "Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
        f"Style: KO,{assemble.FONT},{fontsize},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,"
        f"{assemble.OUTLINE_PX},0,5,{assemble.SIDE_MARGIN},{assemble.SIDE_MARGIN},0,1\n\n"
        "[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n"
    )
    lines = [
        f"Dialogue: 0,{stamp(c['start'])},{stamp(c['end'])},KO,,0,0,0,,{{\\an5\\pos({W // 2},{centre_y})}}{c['text']}"
        for c in cues
    ]
    path.write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"ass: {len(lines)} cues, fontsize {fontsize}px, centre y={centre_y}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", required=True)
    ap.add_argument("--in", dest="src", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--captions", type=Path)
    args = ap.parse_args()
    episode = Path(__file__).resolve().parent.parent / "episodes" / args.episode
    cues = json.loads((args.captions or episode / "captions.json").read_text(encoding="utf-8"))
    ass = args.out.with_suffix(".ass")
    write_ass(cues, ass)
    vf = f"scale={W}:{H}:flags=lanczos," + assemble.ass_filter(ass)
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", str(args.src), "-vf", vf,
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
        "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k", "-movflags", "+faststart", str(args.out),
    ], check=True)
    print(f"rendered: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
