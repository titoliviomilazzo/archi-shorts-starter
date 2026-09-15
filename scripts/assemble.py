"""Assemble a Venezia-style short from generated clips, narration and subtitles.

Reads an edit decision list (``edl.json``) and the episode script, then renders
a finished 1080x1920 / 24 fps video: every cut is pulled from its clip at the
window recorded in the EDL, retimed to the length its narration occupies, and
concatenated on the narration's own cut boundaries (production-spec 7.1).

Subtitle geometry comes from style-contract 4 -- the numbers measured off the
reference channel, not defaults -- so the burnt-in captions can be checked back
against that contract with ``--measure``.

    python assemble.py                 # full render
    python assemble.py --stage cuts    # stop after the retimed cuts
    python assemble.py --no-subs       # picture + narration only
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ffm  # noqa: E402
import overlay_ass
import paths  # noqa: E402
import script_io  # noqa: E402

# Bound in main() from --episode. Module level because the render helpers below
# are called per cut and would otherwise each need the episode threaded through.
EPISODE: Path
CLIPS: Path
RENDERS: Path

WIDTH, HEIGHT, FPS = 1080, 1920, 24

# style-contract 4, measured off reference A and scaled to this frame height.
GLYPH_FRACTION = 0.0401       # glyph height as a fraction of frame height
GLYPH_TO_EM = 0.724           # measured ink height / em for Malgun Gothic Bold
SUB_CENTRE_FRACTION = 0.634   # vertical centre of the caption
OUTLINE_PX = 6                # measured 4-9 px stroke
SIDE_MARGIN = 70              # keeps wrapped lines clear of the frame edges
FONT = "Malgun Gothic"

# Reference A's titles measure 4.5-5.7% of frame height with visibly widened
# tracking, and its dimension figures are drawn in the annotation red rather
# than white (measure_reference_text.py; style-contract 6).
TITLE_FRACTION = 0.048
LABEL_FRACTION = 0.026
ACCENT_ASS = "&H003858E8"     # #E85838, which ASS writes back to front
OVERLAY_LEAD, OVERLAY_TAIL, OVERLAY_FADE_MS = 0.20, 0.20, 150

# Below this, plain frame duplication judders; interpolate instead
# (blueprint 5-3 sanctions optical-flow slowdown for exactly this case).
INTERPOLATE_BELOW = 0.90


@dataclass
class Cut:
    cut: str
    clip: str
    src_in: float
    src_out: float
    tl_start: float
    tl_end: float
    speed: float
    text: str = ""

    @property
    def duration(self) -> float:
        return self.tl_end - self.tl_start


run = ffm.run


def probe(path: Path) -> dict[str, str]:
    data = ffm.probe(path, "stream=width,height,r_frame_rate,nb_frames")
    return {**data["streams"][0], **data["format"]}


def narration_text() -> dict[str, str]:
    """Pull each cut's narration from the timed-beat table in script.md."""
    return {cut: text for cut, _, _, text in script_io.read_beats(EPISODE / "script.md")}


def load_cuts() -> list[Cut]:
    text = narration_text()
    entries = json.loads((EPISODE / "edl.json").read_text(encoding="utf-8"))
    fields = {"cut", "clip", "src_in", "src_out", "tl_start", "tl_end", "speed"}
    cuts = [Cut(**{k: v for k, v in e.items() if k in fields}, text=text.get(e["cut"], "")) for e in entries]
    missing = [c.cut for c in cuts if not c.text]
    if missing:
        raise SystemExit(f"no narration for {missing}")
    return cuts


def frame_count(path: Path) -> int:
    """Frames in a rendered segment, or -1 if it is missing or unreadable."""
    try:
        value = probe(path)["nb_frames"]
        return int(value)
    except (subprocess.CalledProcessError, KeyError, ValueError, json.JSONDecodeError):
        return -1


def render_cut(cut: Cut, work: Path, reuse: bool = True) -> Path:
    """Extract one source window and retime it to its narration duration."""
    out = work / f"{cut.cut}.mp4"
    frames = round(cut.duration * FPS)
    if reuse and frame_count(out) == frames:
        return out

    chain = [f"trim=start={cut.src_in:.4f}:end={cut.src_out:.4f}", "setpts=PTS-STARTPTS"]
    if cut.speed < INTERPOLATE_BELOW:
        chain.append(f"minterpolate=fps={FPS / cut.speed:.4f}:mi_mode=mci:mc_mode=aobmc:vsbmc=1")
    chain.append(f"setpts=PTS/{cut.speed:.6f}")
    chain += [
        f"scale={WIDTH}:{HEIGHT}:flags=lanczos",
        f"fps={FPS}",
        f"tpad=stop_mode=clone:stop_duration={2 / FPS:.4f}",
        f"trim=end_frame={frames}",
        "setpts=PTS-STARTPTS",
    ]

    run([
        "ffmpeg", "-v", "error", "-y", "-i", str(CLIPS / f"{cut.clip}.mp4"),
        "-an", "-vf", ",".join(chain), "-frames:v", str(frames),
        "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", str(out),
    ])
    if frame_count(out) != frames:
        raise SystemExit(f"{cut.cut}: wrote {frame_count(out)} frames, wanted {frames}")
    return out


def write_ass(cuts: list[Cut], path: Path) -> None:
    fontsize = round(HEIGHT * GLYPH_FRACTION / GLYPH_TO_EM)
    centre_y = round(HEIGHT * SUB_CENTRE_FRACTION)
    title_size = round(HEIGHT * TITLE_FRACTION / GLYPH_TO_EM)
    label_size = round(HEIGHT * LABEL_FRACTION / GLYPH_TO_EM)
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {WIDTH}
PlayResY: {HEIGHT}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: KO,{FONT},{fontsize},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,{OUTLINE_PX},0,5,{SIDE_MARGIN},{SIDE_MARGIN},0,1
Style: OVERLAY,{FONT},{title_size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""

    def stamp(t: float) -> str:
        centis = round(t * 100)  # round before splitting, or 59.997 becomes "60.00"
        h, rem = divmod(centis, 360000)
        m, rem = divmod(rem, 6000)
        return f"{h}:{m:02d}:{rem // 100:02d}.{rem % 100:02d}"

    # Reference A rolls captions of about eighteen characters rather than
    # holding a whole sentence, so use the chunked cues when they exist.
    cues_file = EPISODE / "captions.json"
    if cues_file.exists():
        cues = [(c["start"], c["end"], c["text"]) for c in json.loads(cues_file.read_text(encoding="utf-8"))]
    else:
        cues = [(c.tl_start, c.tl_end, c.text) for c in cuts]

    lines = [
        f"Dialogue: 0,{stamp(a)},{stamp(b)},KO,,0,0,0,,"
        f"{{\an5\pos({WIDTH // 2},{centre_y})}}{text}"
        for a, b, text in cues
    ]

    # Titles, layer names and figures sit above the captions and are placed by
    # hand in overlays.json, because where a frame is empty is not a number.
    overlays_file = EPISODE / "overlays.json"
    if overlays_file.exists():
        span = {c.cut: (c.tl_start, c.tl_end) for c in cuts}
        for item in json.loads(overlays_file.read_text(encoding="utf-8")):
            if item["cut"] not in span:
                raise SystemExit(f"overlay on unknown cut {item['cut']}")
            lo, hi = span[item["cut"]]
            a, b = lo + OVERLAY_LEAD, hi - OVERLAY_TAIL
            if b - a < 0.4:
                raise SystemExit(f"{item['cut']} is too short to hold an overlay")
            cx, cy = round(WIDTH * item["x"]), round(HEIGHT * item["y"])
            if item["kind"] == "title":
                body = overlay_ass.title_events(item, cx, cy, title_size, label_size)
            elif item["kind"] == "label":
                body = overlay_ass.label_events(item, cx, cy, label_size, WIDTH, HEIGHT)
            else:
                body = overlay_ass.number_events(item, cx, cy, label_size)
            lines += [f"Dialogue: 1,{stamp(a)},{stamp(b)},OVERLAY,,0,0,0,,{e}" for e in body]

    path.write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


def ass_filter(path: Path) -> str:
    """Escape a Windows path for the subtitles filter (drive colon and all)."""
    escaped = str(path).replace("\\", "/").replace(":", r"\:")
    return f"subtitles='{escaped}'"


def rms_dbfs(pcm: bytes) -> float:
    """RMS level of signed-16 PCM, with silence represented as -inf."""
    import numpy as np

    samples = np.frombuffer(pcm, dtype=np.int16).astype(np.float64)
    if not len(samples):
        return float("-inf")
    rms = float(np.sqrt(np.mean(np.square(samples))))
    return 20 * math.log10(rms / 32768.0) if rms else float("-inf")


def audio_measurements(path: Path, rate: int = 8000, window_s: float = 0.05) -> tuple[float, float]:
    """Return (quietest non-empty window dBFS, whole-file RMS dBFS).

    A3 is intentionally a floor check: a render with a silent window has lost
    its clip/narration audio. A4 uses the independent whole-file RMS value.
    """
    import numpy as np

    raw = ffm.pcm(path, rate)
    samples = np.frombuffer(raw, dtype=np.int16).astype(np.float64)
    per_window = max(1, round(rate * window_s))
    levels = []
    for start in range(0, len(samples), per_window):
        block = samples[start:start + per_window]
        if len(block):
            rms = float(np.sqrt(np.mean(np.square(block))))
            levels.append(20 * math.log10(rms / 32768.0) if rms else float("-inf"))
    finite = [level for level in levels if math.isfinite(level)]
    return (min(finite) if finite else float("-inf"), rms_dbfs(raw))


def measure_audio(path: Path, target_dbfs: float = -18.0, tolerance: float = 0.7) -> bool:
    quietest, delivered = audio_measurements(path)
    a3 = quietest > -60.0
    a4 = abs(delivered - target_dbfs) <= tolerance
    print(f"  audio floor {quietest:.1f} dBFS (A3 {'ok' if a3 else 'FAIL'})")
    print(f"  delivered RMS {delivered:.1f} dBFS (A4 {'ok' if a4 else 'FAIL'}, target {target_dbfs:.1f} ± {tolerance:.1f})")
    return a3 and a4


def measure_ass_styles(ass: Path) -> bool:
    """V4: subtitle outline remains 6px; title/label has no outline."""
    styles = {}
    for line in ass.read_text(encoding="utf-8").splitlines():
        if not line.startswith("Style: "):
            continue
        fields = [field.strip() for field in line[7:].split(",")]
        if len(fields) >= 18:
            styles[fields[0]] = {"border_style": fields[15], "outline": fields[16]}
    ko = styles.get("KO", {})
    overlay = styles.get("OVERLAY", {})
    ok = ko.get("border_style") == "1" and ko.get("outline") == str(OUTLINE_PX)
    ok = ok and overlay.get("border_style") == "1" and overlay.get("outline") == "0"
    print(f"  styles KO outline={ko.get('outline')} OVERLAY outline={overlay.get('outline')} (V4 {'ok' if ok else 'FAIL'})")
    return ok


def dump_overlay_frames(video: Path, cuts: list[Cut], episode: Path) -> bool:
    """V5: produce one human-review frame per overlay-bearing cut."""
    overlay_file = episode / "overlays.json"
    if not overlay_file.exists():
        return True
    ids = {row["cut"] for row in json.loads(overlay_file.read_text(encoding="utf-8"))}
    review = episode / "review"
    review.mkdir(parents=True, exist_ok=True)
    by_id = {cut.cut: cut for cut in cuts}
    for cut_id in sorted(ids):
        if cut_id not in by_id:
            print(f"  V5 FAIL overlay on unknown cut {cut_id}")
            return False
        out = review / f"overlay-{cut_id}.png"
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{by_id[cut_id].tl_start + 0.5:.3f}",
             "-i", str(video), "-frames:v", "1", "-update", "1", str(out)])
    print(f"  overlay review frames {len(ids)}/{len(ids)} (V5 ok)")
    return True


def measure(path: Path, ass: Path, cuts: list[Cut], tolerance: float = 0.15) -> bool:
    """Check the burnt-in captions against style-contract 4.

    The captions are re-rendered alone over black: sampling the finished video
    would confuse bright picture content (the marble palace is near-white) for
    glyphs. Geometry is identical either way, so this measures the real thing.
    """
    import numpy as np

    info = probe(path)
    print(f"  {info['width']}x{info['height']}  {info['r_frame_rate']}  {float(info['duration']):.2f}s")
    w, h = int(info["width"]), int(info["height"])

    # the longest cue, where overflow would show first
    cues_file = EPISODE / "captions.json"
    if cues_file.exists():
        rows = [(c["start"], c["end"], c["text"]) for c in json.loads(cues_file.read_text(encoding="utf-8"))]
    else:
        rows = [(c.tl_start, c.tl_end, c.text) for c in cuts]
    start, end, longest = max(rows, key=lambda r: len(r[2]))
    target = Cut("", "", 0.0, 0.0, start, end, 1.0, longest)
    at = (start + end) / 2
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-f", "lavfi",
         "-i", f"color=c=black:s={w}x{h}:r={FPS}:d={cuts[-1].tl_end:.2f}",
         "-vf", ass_filter(ass), "-ss", f"{at:.2f}", "-frames:v", "1",
         "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True, check=True,
    ).stdout
    frame = np.frombuffer(raw, np.uint8).reshape(h, w)
    ys, xs = np.where(frame > 200)
    if not len(ys):
        print("  caption: not found")
        return False

    rows = np.where((frame > 200).any(axis=1))[0]
    breaks = np.where(np.diff(rows) > 10)[0]
    lines = np.split(rows, breaks + 1)
    glyph = max(line.max() - line.min() for line in lines)
    got_glyph = glyph / h
    got_centre = (ys.min() + ys.max()) / 2 / h
    overflow = xs.min() < 2 or xs.max() > w - 3
    checks = [
        ("glyph height", got_glyph, GLYPH_FRACTION, abs(got_glyph - GLYPH_FRACTION) <= GLYPH_FRACTION * tolerance),
        ("block centre y", got_centre, SUB_CENTRE_FRACTION, abs(got_centre - SUB_CENTRE_FRACTION) <= 0.02),
    ]
    print(f'  caption "{target.text[:20]}..." {len(lines)} line(s), widest {xs.max() - xs.min()}px of {w}px')
    for name, got, want, ok in checks:
        print(f"  {name} {got * 100:.2f}% (contract {want * 100:.2f}%) {'ok' if ok else 'FAIL'}")
    print(f"  block centre x {(xs.min() + xs.max()) / 2:.1f} (frame centre {w / 2:.1f})"
          + ("  OVERFLOW" if overflow else ""))
    return all(ok for *_, ok in checks) and not overflow


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["cuts", "picture", "full"], default="full")
    ap.add_argument("--no-subs", action="store_true")
    ap.add_argument("--measure", action="store_true", help="check output against style-contract 4")
    paths.add_episode_argument(ap)
    ap.add_argument("--out", type=Path, help="default <renders>/<slug>_v1.mp4")
    ap.add_argument("--narration", type=Path, help="default <audio>/<slug>_narration_FINAL.mp3")
    args = ap.parse_args()

    global EPISODE, CLIPS, RENDERS
    ep = paths.episode_from_args(args)
    EPISODE, CLIPS, RENDERS = ep.repo, ep.clips, ep.renders
    if args.out is None:
        args.out = ep.renders / f"{ep.slug}_v1.mp4"
    if args.narration is None:
        args.narration = ep.audio / f"{ep.slug}_narration_FINAL.mp3"

    cuts = load_cuts()
    work = RENDERS / "work"
    work.mkdir(parents=True, exist_ok=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)

    print(f"{len(cuts)} cuts, timeline {cuts[-1].tl_end:.2f}s")
    for cut in cuts:
        note = " interpolated" if cut.speed < INTERPOLATE_BELOW else ""
        print(f"  {cut.cut} {cut.clip} {cut.src_in:.2f}-{cut.src_out:.2f} -> {cut.duration:.2f}s @{cut.speed:.3f}x{note}")
        render_cut(cut, work)
    if args.stage == "cuts":
        print(f"cuts in {work}")
        return 0

    listing = work / "concat.txt"
    listing.write_text("".join(f"file '{(work / f'{c.cut}.mp4').as_posix()}'\n" for c in cuts), encoding="utf-8")
    silent = work / "picture.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(silent)])
    if args.stage == "picture":
        print(f"picture: {silent}")
        return 0

    ass = work / "subs.ass"
    video_filter = []
    if not args.no_subs:
        write_ass(cuts, ass)
        video_filter = ["-vf", ass_filter(ass)]

    encode = (["-c:v", "copy"] if not video_filter
              else ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p"])
    run([
        "ffmpeg", "-v", "error", "-y", "-i", str(silent), "-i", str(args.narration),
        *video_filter, *encode,
        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(args.out),
    ])
    print(f"\nrendered: {args.out}")
    if args.measure and not args.no_subs:
        checks = [measure(args.out, ass, cuts), measure_ass_styles(ass), measure_audio(args.out)]
        checks.append(dump_overlay_frames(args.out, cuts, EPISODE))
        if not all(checks):
            return 1
    return 0


if __name__ == "__main__":
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg not on PATH")
    raise SystemExit(main())
