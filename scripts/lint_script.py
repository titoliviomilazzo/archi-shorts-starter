"""Gate an episode script before narration and generation.

The checks here are deliberately structural.  Whether a shot really proves a
claim remains a human decision; this file catches the omissions that already
cost time in s01.

    python scripts/lint_script.py --episode s01-venezia-pali
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402
import script_io  # noqa: E402


MOVEMENT = re.compile(
    r"\b(?:orbit\w*|push-?in|pull-?back|track\w*|descend\w*|div\w+|"
    r"glid\w*|tilt\w*|pan(?:ning)?|ris\w+|sink\w*|zoom\w*|dolly|"
    r"fly\w*|circl\w+|follow\w*|drift\w*|crane\w*|camera\s+\w+)\b",
    re.I,
)
TITLE_LINE = re.compile(r"^\|\s*(?:\*\*)?최종 제목(?:\*\*)?\s*\|\s*(.*?)\s*\|\s*$", re.M)
TABLE_ROW = re.compile(r"^\|\s*(c\d{2})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$", re.M)
OVERLAY_ROW = re.compile(r"^\|\s*(c\d{2})\s*\|\s*(.*?)\|", re.M)


@dataclass
class Result:
    failures: list[tuple[str, str, str]] = field(default_factory=list)
    warnings: list[tuple[str, str, str]] = field(default_factory=list)

    def fail(self, item: str, rule: str, message: str) -> None:
        self.failures.append((item, rule, message))

    def warn(self, item: str, rule: str, message: str) -> None:
        self.warnings.append((item, rule, message))


def _summary_value(text: str, label: str) -> str | None:
    match = re.search(rf"^\|\s*{re.escape(label)}\s*\|\s*(.*?)\s*\|\s*$", text, re.M)
    return match.group(1) if match else None


def check_script(text: str, boundaries: Path | None, r: Result, overlays: Path | None = None) -> None:
    """Run S1-S6 against one script.md."""
    beats = script_io.BEAT.findall(text)
    if not beats:
        r.fail("script", "S1", "timed-beat table was not parsed by script_io")
        return

    expected = {f"c{i:02d}" for i in range(1, len(beats) + 1)}
    actual = {row[0] for row in beats}
    if actual != expected or len(actual) != len(beats):
        r.fail("script", "S1", f"cut ids are not contiguous: {sorted(actual)}")

    if boundaries and boundaries.exists():
        import json
        rows = json.loads(boundaries.read_text(encoding="utf-8"))
        if len(rows) != len(beats):
            r.fail("script", "S2", f"cut_boundaries has {len(rows)} rows, script has {len(beats)}")
        for row in rows:
            if float(row["end"] if "end" in row else row["tl_end"]) - float(row["start"] if "start" in row else row["tl_start"]) > 10.0:
                r.fail(row.get("cut", "boundary"), "S2", "measured narration segment exceeds 10 seconds")

    for cut, _, _, narration in beats:
        # The timed-beat row's fourth column is the narration; the fifth
        # column is the visual shot and is captured separately below.
        row = re.search(
            rf"^\|\s*{re.escape(cut)}\s*\|[^|]+\|[^|]+\|\s*([^|]+)\|\s*([^|]+)\|",
            text,
            re.M,
        )
        proof, shot = row.groups() if row else ("", "")
        if not MOVEMENT.search(proof) and not MOVEMENT.search(shot):
            r.fail(cut, "S3", "화면 열에 flow 카메라 무빙 어휘가 없다")

    # S4: only a title/overlay is checked here.  The claim ledger is prose and
    # cannot be safely inferred beyond the explicit 전승 marker.
    title = _summary_value(text, "최종 제목") or ""
    if re.search(r"전승|백만|100만|1,?000,?000", title):
        r.fail("title", "S4", "claim ledger marks this subject as 전승; it must not be a title")
    overlay_start = text.find("## 텍스트 오버레이 배치표")
    if overlays and overlays.exists():
        import json
        rendered = " ".join(str(row.get("text", "")) for row in json.loads(overlays.read_text(encoding="utf-8")))
        if re.search(r"전승|백만|100만|1,?000,?000", rendered):
            r.fail("overlay", "S4", "overlay JSON renders a value marked 전승")

    chars = re.search(r"글자수.*?([0-9]+)자", text)
    # Upper bound raised 700 -> 800 by owner decision 2026-09-15 (s03); see
    # docs/script-contract.md §4.  700 was the 60-70 s target converted to
    # characters, not a production limit - one more kit absorbs it.
    if chars and not 450 <= int(chars.group(1)) <= 800:
        r.fail("script", "S5", f"declared character count {chars.group(1)} is outside 450-800")
    if not 15 <= len(beats) <= 30:
        r.fail("script", "S5", f"cut count {len(beats)} is outside 15-30")

    overlay_ids = set(re.findall(r"^\|\s*(c\d{2})\s*\|", text[overlay_start:] if overlay_start >= 0 else "", re.M))
    if overlay_ids - actual:
        r.fail("overlay", "S6", f"overlay references unknown cuts: {sorted(overlay_ids - actual)}")


def check_title(text: str, r: Result) -> None:
    title = _summary_value(text, "최종 제목")
    if title is None:
        r.fail("title", "T1", "최종 제목 row missing")
        return
    title = re.sub(r"[*`]", "", title).strip()
    if len(title) > 25:
        r.fail("title", "T1", f"title is {len(title)} characters; maximum is 25")
    if not re.match(r"^[가-힣A-Za-z0-9·]+", title):
        r.fail("title", "T2", "title does not start with a searchable word")
    if not re.search(r"(?:이유|까|는가|일까|일까요|비밀|원리)\s*[?!?]?$", title):
        r.warn("title", "T3", "title closes as a statement; use an open curiosity form")


def lint(path: Path, boundaries: Path | None = None, overlays: Path | None = None) -> Result:
    text = path.read_text(encoding="utf-8")
    result = Result()
    check_script(text, boundaries, result, overlays)
    check_title(text, result)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    paths.add_episode_argument(ap)
    ap.add_argument("--file", type=Path)
    args = ap.parse_args()
    ep = paths.episode_from_args(args)
    source = args.file or ep.script
    if not source.exists():
        raise SystemExit(f"no script at {source}")
    result = lint(source, ep.boundaries, ep.overlays)
    for item, rule, message in result.failures:
        print(f"FAIL {rule} {item}: {message}")
    for item, rule, message in result.warnings:
        print(f"WARN {rule} {item}: {message}")
    print(f"lint_script: {len(result.failures)} failures, {len(result.warnings)} warnings")
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
