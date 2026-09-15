"""Episode state runner for archi-shorts.

This runner automates deterministic work and stops at human/credit gates.
It never clicks Flow or records a credit estimate as a spend; credits are
entered only as ``before``/``after`` balance observations in manifest.json.

    python scripts/ep.py init --episode s02-<topic>
    python scripts/ep.py status --episode s02-<topic>
    python scripts/ep.py next --episode s02-<topic>
    python scripts/ep.py sheet gen --episode s02-<topic>
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_prompts  # noqa: E402
import lint_script  # noqa: E402
import paths  # noqa: E402
import script_io  # noqa: E402


STAGES = [
    ("research", "소재·리서치", "human", "사실 원장"),
    ("script", "대본", "human", "script.md"),
    ("tts", "TTS + 무음 제거", "human", "음원·cut_boundaries.json"),
    ("split", "묶음 분할", "script", "prompts.md의 묶음표"),
    ("prompt", "프롬프트", "human", "prompts.md"),
    ("image_gate", "이미지 선검증", "human", "image-gate.json"),
    ("generate", "단계 생성", "credit", "clips/G*.mp4"),
    ("review", "클립 검수", "human", "review-S*.md"),
    ("assemble", "편집 + 텍스트 층", "script", "renders/*_v*.mp4"),
    ("effects", "효과음·앰비언스", "script", "audio/*_ambience.wav + mixed render"),
    ("subtitles", "자막 트랙·번역 메타", "script", "captions-{en,it}.srt"),
    ("publish", "게시·관측", "human", "publish.md + live URL"),
    ("retro", "회고", "human", "retro.md"),
]

HUMAN_SHEETS = {"research": "research", "script": "script", "tts": "tts", "prompt": "gen",
                "image_gate": "gen", "generate": "gen", "review": "review", "publish": "publish", "retro": "retro"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def new_manifest(name: str) -> dict:
    return {
        "schema": 1,
        "episode": name,
        "policy": "next-episode",
        "frozen_baseline": False,
        "created": now(),
        "owner_approval": {"generate": False, "published": False},
        "stages": [
            {"id": stage_id, "name": label, "status": "pending", "owner": owner,
             "gate": gate, "artifacts": [], "started": None, "finished": None, "credits": []}
            for stage_id, label, owner, gate in STAGES
        ],
    }


def manifest_path(ep: paths.Episode) -> Path:
    return ep.repo / "manifest.json"


def load_manifest(ep: paths.Episode) -> dict:
    path = manifest_path(ep)
    if not path.exists():
        raise SystemExit(f"no manifest at {path}; initialize with: python scripts/ep.py init --episode {ep.name}")
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(ep: paths.Episode, manifest: dict) -> None:
    manifest_path(ep).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def init_episode(name: str) -> int:
    ep = paths.Episode(name)
    if ep.repo.exists():
        raise SystemExit(f"episode already exists: {ep.repo}")
    ep.repo.mkdir(parents=True)
    for filename in ("script.md", "prompts.md", "review.md", "retro.md", "publish.md"):
        source = paths.REPO / "templates" / filename
        if source.exists():
            target = ep.repo / filename
            target.write_text(source.read_text(encoding="utf-8").replace("<episode-id>", name).replace("<ep>", name), encoding="utf-8")
    (ep.repo / "image-gate.json").write_text(json.dumps({
        "schema": 1,
        "episode": name,
        "status": "pending",
        "batches": [],
        "checked": 0,
        "total": 0,
        "note": "정지 이미지가 프롬프트 문장을 검증했는지 사람 확인 후 기록",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save_manifest(ep, new_manifest(name))
    print(f"initialized {name}: {ep.repo}")
    print("next: research sheet -> script -> TTS; Flow generation remains owner-approved")
    return 0


def stage_index(manifest: dict) -> int:
    for index, stage in enumerate(manifest["stages"]):
        if stage["status"] != "done":
            return index
    return len(manifest["stages"])


def status(ep: paths.Episode) -> int:
    manifest = load_manifest(ep)
    stages = manifest["stages"]
    done = sum(stage["status"] == "done" for stage in stages)
    index = stage_index(manifest)
    print(f"{ep.name}: {done}/{len(stages)} stages done")
    print(f"policy={manifest.get('policy')} frozen_baseline={manifest.get('frozen_baseline', False)}")
    for stage in stages:
        mark = "DONE" if stage["status"] == "done" else stage["status"].upper()
        print(f"  {stage['id']:12} {mark:8} {stage['name']}  gate={stage['gate']}")
    if index < len(stages):
        stage = stages[index]
        print(f"next: {stage['id']} — {stage['name']} ({stage['owner']})")
    else:
        print("next: none; write retro if not already done")
    return 0


# 대본은 영상의 뼈대다. 오너 지시 2026-09-10: 대본 단계 전체를 최상위 모델이 쓴다.
# 근거·정본 = docs/MODEL_ROUTING.md "단계별 클래스".
L0_STAGES = {"split", "assemble", "effects", "subtitles"}
L4_STAGES = {"script"}
CLASS_MODELS = {"L0": {"codex": "none", "claude": "none"},
                "L2": {"codex": "terra", "claude": "sonnet"},
                "L4": {"codex": "astra", "claude": "fable"}}
CLASS_EFFORT = {"L0": "low", "L2": "low", "L4": "medium"}
# schema(specs/task-envelope.schema.json)의 risk는 enum이다. 문장을 넣으면 --validate가 떨어진다.
CLASS_RISK = {"L0": "low", "L2": "medium", "L4": "high"}
CLASS_THINKING = {"L2": "off", "L4": "on"}
CLASS_SUBAGENT = {"L2": "archi-shorts-draft", "L4": "archi-shorts-script"}


def stage_task_class(stage_id: str, ep: paths.Episode | None = None) -> str:
    # split is L0 (deterministic build_edl.py --rebalance) only once edl.json
    # exists. Before that, edl.json and the clips it measures are still
    # generate-stage outputs, so split is a document-writing task (bundle
    # table in prompts.md), which is L2 like the other human/script stages.
    if stage_id == "split" and (ep is None or not ep.edl.exists()):
        return "L2"
    if stage_id in L0_STAGES:
        return "L0"
    if stage_id in L4_STAGES:
        return "L4"
    return "L2"


def _script_command(ep: paths.Episode, stage_id: str) -> str | None:
    if stage_id == "script":
        return f"python scripts/lint_script.py --episode {ep.name}"
    if stage_id == "split":
        if ep.edl.exists():
            return f"python scripts/build_edl.py --episode {ep.name} --rebalance"
        # edl.json and the clips are generate-stage outputs, not split-stage
        # inputs. --rebalance is the re-time path for re-recorded narration
        # (see build_edl.py's own docstring) — pointing a fresh episode at it
        # just dies on a missing edl.json/clip. Before generation, split means
        # writing the bundle table by hand.
        return (f"write the bundle table in episodes/{ep.name}/prompts.md §0 from "
                f"cut_boundaries.json — build_edl.py --rebalance is the re-time path "
                f"and needs edl.json plus generated clips")
    if stage_id == "assemble":
        return f"python scripts/assemble.py --episode {ep.name} --measure --narration <master.mp3>"
    if stage_id == "effects":
        return (f"python scripts/build_ambience.py --episode {ep.name}\n"
                f"python scripts/mix_bed.py --bed <audio/{ep.slug}_ambience.wav> "
                f"--source <renders/{ep.slug}_vN.mp4> --out <renders/{ep.slug}_MIXED.mp4> --under 10")
    if stage_id == "subtitles":
        return f"python scripts/build_srt.py --episode {ep.name}"
    return None


def next_envelope(ep: paths.Episode, stage: dict, runtime: str) -> dict:
    """Return a proposal only. This function must not alter a manifest or episode."""
    if runtime not in {"claude", "codex"}:
        raise ValueError("runtime must be claude or codex")
    task_class = stage_task_class(stage["id"], ep)
    commands = {
        "split": ["scripts/build_edl.py", "--episode", ep.name, "--rebalance"],
        "assemble": ["scripts/assemble.py", "--episode", ep.name, "--measure"],
        "effects": ["scripts/build_ambience.py", "--episode", ep.name],
        "subtitles": ["scripts/build_srt.py", "--episode", ep.name],
    }
    # The routers forward only objective + validation, so the script contract must travel inside objective.
    if stage["id"] == "script":
        objective = (
            f"Write episodes/{ep.name}/script.md as the 대본 stage for {ep.name}. "
            f"Read docs/script-contract.md (7-stage structure, 재미 요소, pass criteria) and "
            f"episodes/{ep.name}/research.md (사실 원장, 금지 목록, 대본 제약) first; use no fact outside "
            f"the 원장. Do not run ep.py mark — owner approval gates the script. No Flow action, media "
            f"generation, credit spend, or publish action."
        )
    elif stage["id"] == "split" and task_class == "L2":
        objective = (
            f"Write the bundle table in episodes/{ep.name}/prompts.md §0 from "
            f"cut_boundaries.json for {ep.name}. build_edl.py --rebalance is the "
            f"re-time path for re-recorded narration and reads edl.json plus "
            f"generated clips — neither exists yet at this stage, so do not run it. "
            f"No Flow action, media generation, credit spend, or publish action."
        )
    else:
        objective = (f"Prepare the {stage['name']} stage for {ep.name}. "
                      "No Flow action, media generation, credit spend, or publish action.")
    envelope = {
        "task_id": f"{ep.name}-{stage['id']}", "task_type": stage["id"], "task_class": task_class,
        "runtime": runtime, "objective": objective,
        "recommended_model": CLASS_MODELS[task_class][runtime],
        "reasoning_effort": CLASS_EFFORT[task_class], "risk": CLASS_RISK[task_class],
        "files_expected": [f"episodes/{ep.name}"], "allowed_scope": [f"episodes/{ep.name}", "scripts"],
        "validation": [{"cmd": _script_command(ep, stage["id"]) or "human owner gate", "pass": "owner gate recorded or command exits 0"}],
        "escalation_condition": ("L4 is the top class; stop and report to the owner rather than escalating."
                                 if task_class == "L4" else
                                 "Ambiguous fact, geometry, or accumulated failure moves to L3."),
    }
    if task_class == "L0":
        envelope["executable"] = {"kind": "python", "argv": commands[stage["id"]]}
    elif runtime == "codex":
        envelope["codex"] = {"profile": CLASS_MODELS[task_class]["codex"], "reasoning_effort": CLASS_EFFORT[task_class]}
    else:
        envelope["claude"] = {"model": CLASS_MODELS[task_class]["claude"],
                              "subagent": CLASS_SUBAGENT[task_class], "thinking": CLASS_THINKING[task_class]}
    return envelope


def next_step(ep: paths.Episode, as_envelope: bool = False, runtime: str | None = None) -> int:
    # Frozen historical episodes can lack a manifest. Proposal mode must remain
    # read-only, so it may describe their first stage without reconstructing one.
    manifest = new_manifest(ep.name) if as_envelope and not manifest_path(ep).exists() else load_manifest(ep)
    index = stage_index(manifest)
    if index == len(manifest["stages"]):
        print("pipeline complete; record retro and observations")
        return 0
    stage = manifest["stages"][index]
    if as_envelope:
        if runtime is None:
            raise SystemExit("--next-envelope requires --runtime claude|codex")
        if stage["id"] not in {"script", "prompt", "split", "assemble", "effects", "subtitles"}:
            print(f"STOP: {stage['id']} is an owner or credit gate; no task envelope emitted", file=sys.stderr)
            return 1
        print(json.dumps(next_envelope(ep, stage, runtime), ensure_ascii=False))
        return 0
    command = _script_command(ep, stage["id"])
    if stage["owner"] == "credit":
        print("STOP: owner approval required before any Flow generation")
        print("record manifest.owner_approval.generate=true only after approval")
        print("record each actual balance delta in stage.credits as before/after/what")
        return 0
    elif command:
        print(f"RUN: {command}")
    else:
        sheet = HUMAN_SHEETS.get(stage["id"], stage["id"])
        print(f"STOP: human decision required; issue `python scripts/ep.py sheet {sheet} --episode {ep.name}`")
        return 0
    return 0


def sheet_tts(ep: paths.Episode) -> int:
    # Export every sentence at 1.0x and let build_narration.py --speed apply
    # the tempo; the TTS tool used may not offer speed control.
    print("문장별 음원을 1.0x로 내보낸다 — 배속은 build_narration.py --speed가 올린다")
    for i, (cut, _, _, text) in enumerate(script_io.read_beats(ep.script), 1):
        print(f"{i:02d} {cut} | 1.0x 내보내기 | {text}")
    return 0


def sheet_gen(ep: paths.Episode) -> int:
    source = ep.repo / "prompts.md"
    if not source.exists():
        raise SystemExit(f"no prompts at {source}")
    text = source.read_text(encoding="utf-8")
    result = lint_prompts.Result()
    script_result = lint_script.lint(ep.script, ep.boundaries if ep.boundaries.exists() else None,
                                     ep.overlays if ep.overlays.exists() else None)
    batches = []
    for name, body in lint_prompts.BATCH.findall(text):
        block = lint_prompts.TEXT_BLOCK.search(body)
        if block:
            batches.append(name)
            lint_prompts.check_batch(name, block.group(1), result)
    print(f"batches: {', '.join(batches) if batches else 'none'}")
    print("cost contract: 8s=12 credits; 4s=14 credits; actual balance delta only")
    print("preflight: image still first, then video; no video prompt edit; owner approval per batch")
    for item, rule, message in result.failures:
        print(f"FAIL {rule} {item}: {message}")
    for item, rule, message in script_result.failures:
        print(f"FAIL {rule} {item}: {message}")
    if result.failures or script_result.failures:
        print("generation sheet: BLOCKED")
        return 1
    print("generation sheet: lint pass; human image gate and owner approval still required")
    return 0


def find_stage(manifest: dict, stage_id: str) -> dict:
    for stage in manifest["stages"]:
        if stage["id"] == stage_id:
            return stage
    raise SystemExit(f"unknown stage: {stage_id}")


def mark_stage(ep: paths.Episode, stage_id: str, artifact: list[str]) -> int:
    manifest = load_manifest(ep)
    stage = find_stage(manifest, stage_id)
    stage_position = next(i for i, row in enumerate(manifest["stages"]) if row is stage)
    blocked = [row["id"] for row in manifest["stages"][:stage_position] if row["status"] != "done"]
    if blocked:
        raise SystemExit(f"cannot skip stages; finish first: {', '.join(blocked)}")
    if stage_id == "generate" and not manifest["owner_approval"].get("generate", False):
        raise SystemExit("generate is credit-gated: set owner_approval.generate=true after owner approval")
    if stage["status"] == "done":
        raise SystemExit(f"stage already done: {stage_id}")
    stage["status"] = "done"
    stage["started"] = stage["started"] or now()
    stage["finished"] = now()
    stage["artifacts"].extend(artifact)
    save_manifest(ep, manifest)
    print(f"marked done: {stage_id}")
    return 0


def approve(ep: paths.Episode, kind: str) -> int:
    manifest = load_manifest(ep)
    if kind == "generate":
        if find_stage(manifest, "image_gate")["status"] != "done":
            raise SystemExit("image_gate must be done before approving generation")
        manifest["owner_approval"]["generate"] = True
    else:
        manifest["owner_approval"]["published"] = True
    save_manifest(ep, manifest)
    print(f"owner approval recorded: {kind}")
    return 0


def record_credit(ep: paths.Episode, stage_id: str, before: int, after: int, what: str) -> int:
    if before < 0 or after < 0 or after > before:
        raise SystemExit("credit balances must be non-negative and after <= before")
    manifest = load_manifest(ep)
    stage = find_stage(manifest, stage_id)
    row = {"before": before, "after": after, "what": what}
    stage["credits"].append(row)
    save_manifest(ep, manifest)
    print(f"recorded credit delta: {before - after} ({before}->{after}) {what}")
    return 0


def sheet_publish(ep: paths.Episode) -> int:
    print("KO title/description: episodes/<ep>/publish.md")
    print("EN title/description: episodes/<ep>/publish.md")
    print("IT title/description: episodes/<ep>/publish.md")
    print(f"SRT: {ep.repo / 'captions-en.srt'} | {ep.repo / 'captions-it.srt'}")
    print("verify after upload: yt-dlp --list-subs <live-url>")
    return 0


def sheet(name: str, ep: paths.Episode) -> int:
    if name == "tts":
        return sheet_tts(ep)
    if name == "gen":
        return sheet_gen(ep)
    if name == "publish":
        return sheet_publish(ep)
    print(f"sheet {name}: fill {ep.repo / (name + '.md')} and mark the manifest stage done after review")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--episode", required=True)
    for command in ("status", "next"):
        parser = sub.add_parser(command)
        parser.add_argument("--episode", required=True)
        if command == "next":
            parser.add_argument("--next-envelope", action="store_true")
            parser.add_argument("--runtime", choices=("claude", "codex"))
    sheet_parser = sub.add_parser("sheet")
    sheet_parser.add_argument("name", choices=("research", "script", "tts", "gen", "review", "publish", "retro"))
    sheet_parser.add_argument("--episode", required=True)
    mark = sub.add_parser("mark")
    mark.add_argument("--episode", required=True)
    mark.add_argument("--stage", required=True)
    mark.add_argument("--artifact", action="append", default=[])
    credit = sub.add_parser("credit")
    credit.add_argument("--episode", required=True)
    credit.add_argument("--stage", required=True)
    credit.add_argument("--before", type=int, required=True)
    credit.add_argument("--after", type=int, required=True)
    credit.add_argument("--what", required=True)
    approval = sub.add_parser("approve")
    approval.add_argument("kind", choices=("generate", "published"))
    approval.add_argument("--episode", required=True)
    args = ap.parse_args()

    if args.command == "init":
        return init_episode(args.episode)
    ep = paths.episode_from_args(args)
    if args.command == "status":
        return status(ep)
    if args.command == "next":
        return next_step(ep, args.next_envelope, args.runtime)
    if args.command == "mark":
        return mark_stage(ep, args.stage, args.artifact)
    if args.command == "credit":
        return record_credit(ep, args.stage, args.before, args.after, args.what)
    if args.command == "approve":
        return approve(ep, "publish" if args.kind == "published" else args.kind)
    return sheet(args.name, ep)


if __name__ == "__main__":
    raise SystemExit(main())
