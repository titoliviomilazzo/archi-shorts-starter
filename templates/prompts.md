# <ep> — Flow 생성 프롬프트 (v1)

> 규격: [production-spec.md](../docs/production-spec.md) §4.4 · 작성 절차: [prompt-playbook.md](../docs/prompt-playbook.md)
> 대본: `script.md` — **컷 경계가 오디오 실측으로 확정된 뒤에** 이 문서를 쓴다 (spec §9.1 3→4→5)
> 게이트: `python scripts/lint_prompts.py --episode <ep>` — 실패 0이어야 생성으로 넘어간다
> 상태: <작성 중 | 이미지 게이트 통과 | 생성 중 | 종료>

---

## 0. 생성 계획

| 항목 | 값 |
| --- | --- |
| 총 컷 | <n> |
| 오디오 길이 | <초> |
| 생성 묶음 | <n>회 |
| 클립 규격 | 9:16 · 8초 · Omni 1.1 Flash |
| **예상 크레딧** | 묶음 × 12. **4초를 쓰면 그 묶음만 14** (spec §8.0) |

**단계 생성** — 위험이 큰 묶음부터 소량 생성해 검수하고, 통과해야 다음으로 간다.
앞 묶음의 실패가 뒷 묶음 프롬프트를 고친다. **실패해도 12가 나간다.**

## 1. 앵커 — 전 컷 고정, 글자 그대로

```text
Incredibly detailed 3D architectural rendering, Unreal Engine 5 cinematic style, academic archive aesthetic, bright soft daylight, even overcast key light, pale grey and cool blue tonal range, subtle particles floating in the light, photorealistic textures, 8k resolution, 9:16 aspect ratio
```

## 2. 필수 절 — 모든 프롬프트 말미

```text
The <피사체> remains perfectly static, solid, and undistorted; only the camera moves.
Every surface is bare <재료> with no lettering, no signage and no engraved words anywhere.
<피사체> standing in dark empty space with no floor, no room and no stand.
The only colours are <허용 색상>. Nothing red appears anywhere in the frame.
```

두 번째 줄은 **주석을 요청한 컷에서만 뺀다** (playbook §4).

## 3. 생성 묶음

### G1 — c01~c0n · <역할>

**이미지 게이트** (0크레딧 — 반드시 먼저)

```text
Create a still image, 9:16 vertical.

<앵커>

<첫 슬롯 장면 서술> <억제 3종>
```

- [ ] §4.4.1 5문항 통과   - [ ] 화면에 글자·주석 0

**비디오 프롬프트** — 이미지에서 통과한 문장을 옮겨 쓴다

```text
[Anchor] <앵커>.
[Action] <한 문장: 이 묶음이 무엇을 보여주는가>
[Multi-shot] [0-Xs: <주제·시대 → 환경 → 카메라 → 조명 → 질감>] -> [X-Ys: <...>] -> [Y-8s: <...>]. <금지 목록>. The <피사체> remains perfectly static, solid, and undistorted; only the camera moves. <정적 피사체·주석 억제 절> 8 seconds.
```

| 컷 | 슬롯 | 위험도 |
| --- | --- | --- |
| c01 | 0-X | |

---

## 4. 위험도 요약

| 묶음 | 위험 | 근거 | 완화 |
| --- | --- | --- | --- |

## 5. 폴백 (spec §5)

(1) 결함 프레임 추출 -> **이미지 부분 수정 (0크레딧)** 으로 고치는 문장을 찾는다 -> (2) 그 문장으로 **재생성 (12)** -> (3) 매크로 클로즈업으로 대체.
**비디오 프롬프트 편집은 쓰지 않는다** — 20크레딧에 멀티샷 구조가 파괴된다.

## 6. 생성 후 검수

1. 규격 실측 (해상도·fps·길이) · **업스케일 눌렀는지** (기본 출력은 720×1280)
2. 멀티샷 슬롯 경계 프레임 차분
3. 슬롯 경계 형상 붕괴
4. **생성 텍스트·주석 잔존 검사** — 빨강 면적
5. 정지 구간 검사 — 1초 이상이면 재생성 후보
6. **`md5sum`으로 입력과 대조** — 파일명은 근거가 아니다

## 7. 크레딧 원장 — 차감분으로만

| 묶음 | 전 | 후 | 차감 | 비고 |
| --- | ---: | ---: | ---: | --- |
