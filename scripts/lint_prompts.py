"""Check an episode's prompts.md against the rules t00 and s01 paid for.

Every rule here exists because a generation went wrong once. The credit cost
of each is in the comment beside it, so the reason survives longer than the
memory of the session that found it. Rules are checked per generation batch
(the ```text block under each "### G{n}" heading).

    python scripts/lint_prompts.py --episode s01-venezia-pali
    python scripts/lint_prompts.py --episode s02-... --rules R2,R10

Exit status is 1 if anything failed, so it can gate a step. Warnings do not
fail the run; they are things a person should look at, not things a regex can
settle.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402

# --- the anchor, verbatim. docs/production-spec.md 4.4 --------------------
ANCHOR_HEAD = "Incredibly detailed 3D architectural rendering"

# R2: docs/flow-techniques.md 2. s01 G8 failed three times without it -- 36 credits.
STATIC_CLAUSE = re.compile(
    # the canonical wording, or the formulation G8 v9.2 shipped and passed with
    r"remains?\s+perfectly\s+static,\s+solid,\s+and\s+undistorted;\s+only\s+the\s+camera"
    r"|no\s+object\s+(?:in\s+the\s+scene\s+)?moves?;\s*only\s+the\s+camera"
    r"|nothing\s+in\s+the\s+scene\s+moves\s+except\s+the\s+camera",
    re.I)

# spec 4.5.1: a still camera is allowed only in macro, and only if the subject
# or the particles are moving. These are the movers that license it.
MACRO = re.compile(r"\bmacro\b", re.I)
SUBJECT_MOVES = re.compile(
    r"\b(driven|pressing|squeez\w+|wicking|seep\w+|flow\w+|drift\w+|travel\w+|"
    r"rising|falling|filling|escaping|densif\w+|swirl\w+|particles?)\b", re.I)

# R11: T1 and T3 both drew arrows nobody asked for. spec 4.4.2.
SUPPRESS_SURFACE = re.compile(r"no\s+lettering", re.I)
# Widened 2026-09-11: the anchor tone flipped from dark to bright (production-spec
# 4.4) after the s02 image gate measured mean grey 26-70 (32-81% dark pixels)
# against a 151-169 benchmark. SUPPRESS_EMPTY exists to forbid a room, a stand or
# a plinth behind the subject -- it never needed to force darkness, so a bright
# void phrasing ("plain empty pale grey void") must satisfy it too, alongside the
# original s01 wordings.
SUPPRESS_EMPTY = re.compile(
    r"no\s+floor,\s*no\s+room|dark\s+empty\s+space|plain\s+empty\s+(?:\w+\s+){0,3}void",
    re.I)
SUPPRESS_COLOUR = re.compile(r"nothing\s+red\s+appears", re.I)
SUPPRESS_MINIMAL = re.compile(r"no\s+annotations", re.I)
# A cut that wants annotation says so; these are the phrasings the spec verifies.
WANTS_ANNOTATION = re.compile(
    r"red\s+arrows?|glowing\s+red|red\s+contour|red\s+dimension|red\s+disc|red\s+bracket", re.I)

# R4: prompt tail carries the length. The guideline's OUTPUT line is ignored (s01 G2 -> 10s).
LENGTH_TAIL = re.compile(r"\b(4|6|8|10)\s+seconds\.\s*$")

# R1: spec 4.5.1. Ten cuts shipped without one in s01 v3.
MOVEMENT = re.compile(
    r"\b(drone|orbit\w*|cran\w+|push-?in|pull\w*\s+back|pull-?back|track\w*|"
    r"descend\w*|descent|div\w+|plung\w+|glid\w+|tilt\w*|pan|panning|ris\w+|"
    r"sink\w*|zoom\w*|dolly|fly\w*|circl\w+|follow\w*|drift\w*|emerg\w+|"
    r"camera\s+(?:movement|moves?|moving)|moves?\s+\w*\s*(?:downward|upward|forward|back))\b",
    re.I)

# R6: spec 4.4 forbidden table, each with the take that earned it.
FORBIDDEN = {
    r"\bthin\s+(?:red\s+)?(?:line|lines|arrow|arrows|hairline|bracket|brackets|marker|markers)": "G2 take01 -- 0.59% of frame, invisible",
    r"\bcut\s+open\b": "reads as collapse or trench",
    r"\bpointed\s+tips\b": "G8 take03 -- turned the flat pile heads pointed",
}
# These two sank G8 when they described the subject, but G4 shipped 'like a
# submerged forest' as a simile and passed. A regex cannot tell the two apart,
# so they warn rather than fail.
SUSPECT = {
    r"\bsubmerged\s+forest\b": "G8 take01 built an underground cavity from it; G4 shipped it as a simile",
    r"\bendless\s+forest\b": "G8 take02 -- same failure",
}

# R7: spec 4.4.1 question 1. Moving an object drifts its shape.
OBJECT_MOTION = re.compile(
    r"\b(pull(?:ing|s|ed)?\s+(?:up|out)|lift(?:ing|s|ed)?|extract(?:ing|s|ed)?|"
    r"rais(?:e|es|ing)|hoist(?:ing|s)?|rising\s+(?:partway\s+)?out|being\s+driven)\b", re.I)
ALLOW_COMMENT = re.compile(r"<!--\s*allow:", re.I)
# 'nothing lifting or moving' is the fix, not the fault -- s01 G8 v9.2 says exactly that.
NEGATED = re.compile(r"\b(no|not|nothing|none|never|without)\b[^.]{0,40}$", re.I)

# R10: T1. Korean collapsed at the front of the orbit; 3D letterforms drift in any script.
KOREAN = re.compile(r"[가-힣]")
SOLID_LETTERS = re.compile(r"\b(3D\s+letters|typography\s+sculpture|giant\s+letters)\b", re.I)
ENGRAVED_FLAT = re.compile(r"\b(chisel|engrav|carved\s+into|inscri)", re.I)

# R12: T7. The video prompt edit is a full regeneration at 20 credits.
VIDEO_EDIT = re.compile(r"\bedit\s+this\s+video\b", re.I)

BATCH = re.compile(r"^###\s+(G\d+)\b.*?$\n(.*?)(?=^###\s+G\d+\b|\Z)", re.M | re.S)
TEXT_BLOCK = re.compile(r"```text\n(.*?)```", re.S)


@dataclass
class Result:
    failures: list[tuple[str, str, str]] = field(default_factory=list)
    warnings: list[tuple[str, str, str]] = field(default_factory=list)

    def fail(self, batch: str, rule: str, msg: str) -> None:
        self.failures.append((batch, rule, msg))

    def warn(self, batch: str, rule: str, msg: str) -> None:
        self.warnings.append((batch, rule, msg))


def check_batch(name: str, prompt: str, r: Result) -> None:
    tail = prompt.strip()

    # R3 -- anchor verbatim, early
    where = prompt.find(ANCHOR_HEAD)
    if where < 0:
        r.fail(name, "R3", "anchor missing")
    elif where > len(prompt) * 0.25:
        r.fail(name, "R3", f"anchor starts at {100 * where / len(prompt):.0f}% -- must be inside the first 25%")

    # R1 -- every slot moves the camera
    slots = re.findall(r"\[([\d.]+)\s*-\s*([\d.]+)s:(.*?)\]", prompt, re.S)
    if not slots:
        r.warn(name, "R1", "no multi-shot slots found; checking the whole prompt instead")
        if not MOVEMENT.search(prompt):
            r.fail(name, "R1", "no camera movement verb anywhere")
    for lo, hi, body in slots:
        if MOVEMENT.search(body):
            continue
        if MACRO.search(body) and SUBJECT_MOVES.search(body):
            r.warn(name, "R1", f"slot {lo}-{hi}s holds the camera still -- allowed in macro "
                               f"because the subject moves (spec 4.5.1), but check the frame difference")
        else:
            r.fail(name, "R1", f"slot {lo}-{hi}s has no camera movement verb")

    # R5 -- slots are contiguous and reach the stated length
    if slots:
        edges = [(float(a), float(b)) for a, b, _ in slots]
        for (_, prev_hi), (nxt_lo, _) in zip(edges, edges[1:]):
            if abs(prev_hi - nxt_lo) > 1e-6:
                r.fail(name, "R5", f"slot boundary gap at {prev_hi}s -> {nxt_lo}s")

    # R4 -- length in the tail, not the guideline
    m = LENGTH_TAIL.search(tail)
    if not m:
        r.fail(name, "R4", "prompt does not end with 'N seconds.' (4/6/8/10) -- the guideline OUTPUT line is ignored")
    elif slots:
        if abs(float(slots[-1][1]) - float(m.group(1))) > 1e-6:
            r.fail(name, "R4", f"last slot ends {slots[-1][1]}s but the tail says {m.group(1)} seconds")

    # R2 -- static subject clause
    if not STATIC_CLAUSE.search(prompt):
        r.fail(name, "R2", "static-subject clause missing (cost s01 G8 36 credits)")

    # R11 -- annotation suppression unless the cut asks for annotation
    if not WANTS_ANNOTATION.search(prompt):
        have = [SUPPRESS_SURFACE.search(prompt), SUPPRESS_EMPTY.search(prompt), SUPPRESS_COLOUR.search(prompt)]
        if not any(have):
            r.fail(name, "R11", "no annotation suppression, and no annotation requested "
                                "-- T1/T3 drew arrows unbidden. See spec 4.4.2")
        elif not all(have):
            missing = [n for n, h in zip(("surface", "empty background", "colour"), have) if not h]
            r.warn(name, "R11", f"partial suppression -- missing: {', '.join(missing)}")
        if SUPPRESS_MINIMAL.search(prompt) and not any(have):
            r.warn(name, "R11", "only the negative line is present; it failed on its own in T5")

    # R6 -- forbidden vocabulary
    for pattern, why in FORBIDDEN.items():
        if re.search(pattern, prompt, re.I):
            r.fail(name, "R6", f"forbidden phrasing /{pattern}/ -- {why}")
    for pattern, why in SUSPECT.items():
        if re.search(pattern, prompt, re.I):
            r.warn(name, "R6", f"risky phrasing /{pattern}/ -- {why}")

    # R7 -- object motion, unless the sentence is denying it
    motion = next((m for m in OBJECT_MOTION.finditer(prompt)
                   if not NEGATED.search(prompt[max(0, m.start() - 40):m.start()])), None)
    if motion and not ALLOW_COMMENT.search(prompt):
        hit = motion.group(0)
        r.fail(name, "R7", f"object motion '{hit}' -- fix the object and move the camera (spec 4.4.1 Q1). "
                           "Add '<!-- allow: ... -->' if the owner approved a diagram motion")

    # R10 -- Korean and freestanding letterforms
    quoted_korean = [q for q in re.findall(r'"([^"]*)"', prompt) if KOREAN.search(q)]
    if quoted_korean:
        r.fail(name, "R10", f"asks to render Korean {quoted_korean} -- failed at the front of the orbit in T1")
    if SOLID_LETTERS.search(prompt):
        r.fail(name, "R10", "freestanding 3D letterforms drift in any script (T1) -- engrave on a flat face instead")
    if ENGRAVED_FLAT.search(prompt) and not re.search(r"\bflat\b|\bplinth\b|\bface\b|\bsurface\b", prompt, re.I):
        r.warn(name, "R10", "engraved text without a flat surface named -- T1 only held on the plinth")

    # R12 -- never ask for a video edit
    if VIDEO_EDIT.search(prompt):
        r.fail(name, "R12", "video prompt edit is a full regeneration at 20 credits and flattens multi-shot (T7)")

    # R9 is a per-episode distribution rule, checked once across batches.


def check_episode(prompts: str, r: Result) -> None:
    """R9 -- the movement mix the episode has to carry (flow-techniques 1, 3)."""
    need = {
        "FPV push-in": r"push-?in|fpv",
        "orbit": r"\borbit|circling",
        "tilt-up": r"tilt(?:s|ing)?\s+up|craning?\s+(?:slowly\s+)?upward|cranes\s+slowly\s+upward",
    }
    for label, pattern in need.items():
        if not re.search(pattern, prompts, re.I):
            r.warn("episode", "R9", f"no {label} anywhere in the episode (flow-techniques 1.1)")


def main() -> int:
    ap = argparse.ArgumentParser()
    paths.add_episode_argument(ap)
    ap.add_argument("--file", type=Path, help="default <episode>/prompts.md")
    ap.add_argument("--rules", help="comma-separated subset, e.g. R2,R10")
    args = ap.parse_args()

    ep = paths.episode_from_args(args)
    src = args.file or ep.repo / "prompts.md"
    if not src.exists():
        raise SystemExit(f"no prompts at {src}")
    text = src.read_text(encoding="utf-8")

    r = Result()
    batches = 0
    for name, body in BATCH.findall(text):
        block = TEXT_BLOCK.search(body)
        if not block:
            r.warn(name, "-", "no ```text prompt block")
            continue
        batches += 1
        check_batch(name, block.group(1), r)
    if batches:
        check_episode(text, r)
    else:
        r.warn("-", "-", "no generation batches found; is this a prompts.md?")

    keep = {x.strip().upper() for x in args.rules.split(",")} if args.rules else None
    fails = [f for f in r.failures if keep is None or f[1] in keep]
    warns = [w for w in r.warnings if keep is None or w[1] in keep]

    print(f"{src.relative_to(paths.REPO) if src.is_relative_to(paths.REPO) else src}: {batches} batches")
    for batch, rule, msg in fails:
        print(f"  FAIL {batch:>8} {rule:<4} {msg}")
    for batch, rule, msg in warns:
        print(f"  warn {batch:>8} {rule:<4} {msg}")
    if not fails and not warns:
        print("  clean")
    print(f"\n{len(fails)} failures, {len(warns)} warnings")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
