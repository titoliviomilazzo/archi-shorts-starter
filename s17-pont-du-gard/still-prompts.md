# s17-pont-du-gard 상세 스틸 이미지 프롬프트

이 문서는 이미지 생성 전 검토용이다. 실제 자료 편집 컷에는 원본 이미지와 사용권이 필요하다. 역사 재현과 분석 모형은 기록사진으로 표시하지 않는다. 효과 후보는 기존 DB 문구를 그대로 가져온 별도 부록이며, 1+1 효과 구성이 미확정된 컷은 생성 승인 상태가 아니다.

## 복사형 프롬프트

### c01 · G1
- 낭독 · 퐁 뒤 가르, 물이 물을 건넙니다.
- 편집 구간 · 0.00–2.39초
- 자료 유형 · reconstruction / 참조 R2
- 핵심 행동 · 강 전경에서 위쪽 물길을 숨긴 질문
- 사실 고정점 · three arcade tiers / upper channel remains covered

#### A 프롬프트
```text
Show the Pont du Gard from its downstream bank with the river crossing the lower third and the entire three-tier silhouette centred above it. Capture a bright patch of river turbulence directly beneath the main opening, while the capped uppermost course stays opaque and visually quiet. Preserve the recognizable valley and uneven ancient masonry; no water is visible on the top course. The image must pose a contradiction without revealing the channel yet. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 24mm downstream-bank low wide; first 4s brisk push. Light direction: late afternoon sun from viewer-left rear.

Camera and lighting specification for this still: 24mm downstream-bank low wide; first 4s brisk push. Lighting direction and quality: late afternoon sun from viewer-left rear. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No visible water pouring from top; no modern road bridge replacing aqueduct.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 24mm downstream-bank low wide; first 4s brisk push
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm three arcade tiers
- Confirm upper channel remains covered

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c02 · G1
- 낭독 · 하나는 당장 보이죠. 돌다리 밑을 지나는 강입니다.
- 편집 구간 · 2.39–6.22초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 하부 강물을 확인
- 사실 고정점 · river lies below bridge / masonry remains fixed

#### A 프롬프트
```text
Frame the lowest central arch from just above the Gardon, with a broad travelling ripple entering at viewer-left and leaving at viewer-right. Rough limestone voussoirs fill the upper edge, their reflection breaking into green water below. Keep a small margin of the distant bank visible through the opening to establish an actual river passage. The upper channel is outside this camera view, so this cut verifies only the obvious first waterway. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 35mm near-water approach under lowest arch. Light direction: sun from viewer-right reflected off water.

Camera and lighting specification for this still: 35mm near-water approach under lowest arch. Lighting direction and quality: sun from viewer-right reflected off water. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No artificial illuminated river arrows; no second river or waterfall.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 35mm near-water approach under lowest arch
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm river lies below bridge
- Confirm masonry remains fixed

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c03 · G1
- 낭독 · 그런데 돌 사이로 내려다봐도 물은 저 아래뿐이에요.
- 편집 구간 · 6.22–9.28초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 돌틈을 올려다봐도 강밖에 안 보임
- 사실 고정점 · solid lower pier / only river water visible here

#### A 프롬프트
```text
Place the camera beside the inner face of a lower pier, low enough that a wet limestone seam dominates the foreground and a narrow river strip remains visible beyond it. Let the repeated stone joints lead the eye upward into shadow, without inventing holes through the pier. The focal detail is water staining near the riverline rather than an exposed pipe. Give foreground stone and distant ripples different depths so this is a new piece of evidence, not another bridge postcard. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 50mm water-height oblique at inner pier. Light direction: soft reflected daylight from lower viewer-left.

Camera and lighting specification for this still: 50mm water-height oblique at inner pier. Lighting direction and quality: soft reflected daylight from lower viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No tunnel cut through pier; no hidden pipe at river level.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 50mm water-height oblique at inner pier
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm solid lower pier
- Confirm only river water visible here

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c04 · G1
- 낭독 · 두 번째 물길은 대체 어디 있다는 걸까요?
- 편집 구간 · 9.28–11.80초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 空강변을 찾는 시선
- 사실 고정점 · riverbank is empty / no second channel revealed

#### A 프롬프트
```text
Look through the dark side of a lower arch toward an empty stretch of pale gravel bank, cropping the ceiling to make a restrained visual search. A thin edge of flowing green water stays at the bottom, and the solid pier edge remains close on viewer-left. The empty bank is the focal answer to the unsuccessful search; it contains no concealed outlet or dramatic doorway. Use deep shadow framing against sunlit gravel to carry the unanswered question forward. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 70mm through a narrow side opening toward empty bank. Light direction: warm lateral sun from viewer-right.

Camera and lighting specification for this still: 70mm through a narrow side opening toward empty bank. Lighting direction and quality: warm lateral sun from viewer-right. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No invented doors, pipes, reservoirs, people or labels.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 70mm through a narrow side opening toward empty bank
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm riverbank is empty
- Confirm no second channel revealed

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c05 · G2
- 낭독 · 물고기라면 첫 번째 길을 따라 헤엄쳐 가겠죠.
- 편집 구간 · 11.80–14.70초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 물고기가 강의 경로로 감
- 사실 고정점 · one ordinary river fish / pier contacts riverbed

#### A 프롬프트
```text
Use a clear shallow underwater viewpoint beside the base of an actual limestone pier. One small river fish is caught turning away downstream past the stone, its tail slightly flexed, with natural suspended particles and rippled sunlight crossing the bed. The water surface is a soft ceiling, not a transparent theatrical window onto the whole monument. The fish establishes an ordinary river route; it must not behave as a guide or share an impossible channel with the drinking-water model. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 28mm underwater side view parallel to pier. Light direction: dappled sunlight entering from upper viewer-left.

Camera and lighting specification for this still: 28mm underwater side view parallel to pier. Lighting direction and quality: dappled sunlight entering from upper viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No tropical fish, aquarium glass or glowing animal.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 28mm underwater side view parallel to pier
- 움직이는 대상 · one small river fish, natural water ripples and camera only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm one ordinary river fish
- Confirm pier contacts riverbed

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c06 · G2
- 낭독 · 하지만 옛날 로마 사람들이 마실 물은 다른 데로 갔습니다.
- 편집 구간 · 14.70–18.12초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 다른 목적지를 향하는 식수 한방울
- 사실 고정점 · droplet is conceptual model / drinking-water route separate from river

#### A 프롬프트
```text
Create an explicitly illustrative tabletop water model rather than a historical scene. A single clear droplet is poised to leave the edge of a narrow stone channel at viewer-right; beyond it the background is empty and out of focus. Keep the channel lip level within the frame and the water physically attached by surface tension. The droplet is an editorial point of view for water destined for a city, with no map pin, eyes, face or written destination. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 85mm macro of a droplet leaving a stone ledge in a separate model. Light direction: cool side light from viewer-left with warm stone bounce.

Camera and lighting specification for this still: 85mm macro of a droplet leaving a stone ledge in a separate model. Lighting direction and quality: cool side light from viewer-left with warm stone bounce. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No anthropomorphic droplet, text destination or water teleportation.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 85mm macro of a droplet leaving a stone ledge in a separate model
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm droplet is conceptual model
- Confirm drinking-water route separate from river

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c07 · G2
- 낭독 · 눈앞에 이렇게 큰 강을 두고 어디로 갔을까요?
- 편집 구간 · 18.12–20.93초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 강 너머 도시까지의 높이관계 예고
- 사실 고정점 · city is not adjacent to bridge / route continues at high elevation

#### A 프롬프트
```text
Show a broad valley profile with the aqueduct bridge crossing the middle distance and the river distinctly lower below. This is a restrained archaeological landscape model based on source terrain, with the destination direction implied by the route continuing away along the high bank rather than by placing Nîmes visibly next to the bridge. Use sparse vegetation and layered atmospheric depth. The viewer should feel that water has a journey beyond this crossing without seeing a fictional city behind the next arch. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 40mm elevated valley-wide view; slow lateral glide. Light direction: overcast daylight from sky above viewer-left.

Camera and lighting specification for this still: 40mm elevated valley-wide view; slow lateral glide. Lighting direction and quality: overcast daylight from sky above viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No miniature Nîmes beside bridge; no arrows or invented skyline.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 40mm elevated valley-wide view; slow lateral glide
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm city is not adjacent to bridge
- Confirm route continues at high elevation

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c08 · G3
- 낭독 · 돌다리 위로 시선을 올려도 길쭉한 돌 뚜껑만 보입니다.
- 편집 구간 · 20.93–24.56초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 돌뚜껑까지 다가감
- 사실 고정점 · cover slabs closed / topmost course of bridge

#### A 프롬프트
```text
Place the camera almost level with the uppermost capped channel, looking along a sequence of worn stone cover slabs. Their seams converge into the distance and one chipped corner near the centre catches warm light. Keep the covers closed, heavy and continuous; this is the final moment before the reveal. The lower arcade is only a distant drop at the side of frame. Preserve the actual channel width and coping details from the reference, making the opaque cap feel like the important object. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 85mm top-course close view looking along coping. Light direction: raking sun from viewer-left.

Camera and lighting specification for this still: 85mm top-course close view looking along coping. Lighting direction and quality: raking sun from viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No floating slabs, open roof or visible upper water yet.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 85mm top-course close view looking along coping
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm cover slabs closed
- Confirm topmost course of bridge

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c09 · G3
- 낭독 · 그 돌 뚜껑 아래로 물이 강을 건넜습니다.
- 편집 구간 · 24.56–27.01초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 단면에서 흐르는 윗물을 공개
- 사실 고정점 · upper channel is open-flow under cap / river remains far below

#### A 프롬프트
```text
Create a clearly analytical cutaway of the Roman working channel at the exact coping edge used in the previous image. Remove only a short near-side section of cover and wall by a clean vertical editorial cut, revealing a shallow open stream under the retained stone cap. The river is far below and remains visually separate. Show water touching the channel floor, with a free surface and mineral-stained lining. Keep every remaining stone solid; the cut is a model device, not an ancient opening or a dissolving building. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 50mm oblique sectional view at same coping edge. Light direction: soft key from upper viewer-left.

Camera and lighting specification for this still: 50mm oblique sectional view at same coping edge. Lighting direction and quality: soft key from upper viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No pressurized pipe, inverse siphon, waterfall to river or transparent masonry everywhere.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 50mm oblique sectional view at same coping edge
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm upper channel is open-flow under cap
- Confirm river remains far below

#### DB 효과 후보
- layer.scan.5 · archi-shorts · still_pass · 한정된해석단면의 절개범위만정의. 전체아치/수로는 고정. still_pass 상태의 원문 인용 후보.
```text
[Scan] A single thin brilliant cyan plane of light sweeps slowly through one short near-side section of the covered upper Roman aqueduct channel from the viewer-left edge of that short sectional bay to the viewer-right edge of the same bay, held perfectly flat and perpendicular to its travel. Everything the plane has already passed is left open as a clean cutaway, its cut faces showing the raw thickness of every wall and floor slab, while everything ahead of it stays solid and untouched. The plane is a narrow bright core with a soft glow on the surfaces it crosses, and it never tilts, never stops and never reverses.
```
원문 템플릿의 위치 매개변수만 치환했다.

### c10 · G4
- 낭독 · 그런데 이 물은 강으로 내려가면 안 됩니다.
- 편집 구간 · 27.01–29.52초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 강으로 내려가는 가상선 차단
- 사실 고정점 · hypothetical drop only / real channel stays high

#### A 프롬프트
```text
Present an isolated physical elevation model showing a narrow high aqueduct channel and a much lower river basin. A small separate ghost-outline chute points downward only as a hypothetical comparison, ending before it joins the river; the real high channel remains intact across the top. The hypothetical object must be visually distinguishable from masonry through pale edge-only material, never portrayed as a real Roman structure. Keep the composition sparse so the cost of losing height becomes a question rather than a spectacle of collapse. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: orthographic isolated elevation model. Light direction: studio key from upper viewer-right.

Camera and lighting specification for this still: orthographic isolated elevation model. Lighting direction and quality: studio key from upper viewer-right. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No actual aqueduct break, historical accident reenactment or working inverse siphon.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · orthographic isolated elevation model
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm hypothetical drop only
- Confirm real channel stays high

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c11 · G4
- 낭독 · 낮아진 물을 저절로 다시 도시 높이까지 올릴 수는 없거든요.
- 편집 구간 · 29.52–33.26초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 강높이와 도시높이를 비교
- 사실 고정점 · spilled open water below receiving lip / sealed pressure pipes absent

#### A 프롬프트
```text
Use a side-on open-channel comparison model with a low river surface in the foreground and a raised receiving lip to viewer-right. A small quantity of water lies in the low basin, clearly below the dry lip; no stream climbs from it. The original high route is visible as a thin solid ledge behind both, showing the route that retained the usable elevation. This illustrates water already spilled into the river, not the behavior of a sealed pressure pipe. Preserve level surfaces and a stable horizon. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: side-on 70mm model view; no zoom during elevation comparison. Light direction: diffuse key from high viewer-left.

Camera and lighting specification for this still: side-on 70mm model view; no zoom during elevation comparison. Lighting direction and quality: diffuse key from high viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No upward unpowered jet; no claim that all siphons are impossible.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · side-on 70mm model view; no zoom during elevation comparison
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm spilled open water below receiving lip
- Confirm sealed pressure pipes absent

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c12 · G5
- 낭독 · 그래서 아치를 세 층이나 쌓아 물길 높이를 이었습니다.
- 편집 구간 · 33.26–36.50초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 세층아치로 윗길 높이를 이음
- 사실 고정점 · three arcade tiers / channel joins high banks

#### A 프롬프트
```text
Reveal a Roman working-bridge reconstruction in a precise side elevation with shallow oblique depth. Three stacked arcade tiers rise from the valley, supporting the narrow covered channel at the top. A thin visible strip of channel water continues between the two high banks without dropping to river level. Let the weight of the limestone piers and arch rings read through material texture, not decorative stress graphics. Keep the top profile gently descending toward the city direction and preserve the source-supported proportions of the actual bridge. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 35mm architectural side elevation with slight oblique depth. Light direction: late sun from upper viewer-right.

Camera and lighting specification for this still: 35mm architectural side elevation with slight oblique depth. Lighting direction and quality: late sun from upper viewer-right. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No Roman pump, steel truss, inverted siphon or exaggerated ramp.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 35mm architectural side elevation with slight oblique depth
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm three arcade tiers
- Confirm channel joins high banks

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c13 · G5
- 낭독 · 도시까지 약 오십 킬로미터, 평균 경사는 일 킬로미터에 이십오 센티미터.
- 편집 구간 · 36.50–41.54초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 전체수로 평균경사의 작은 낙차를 비교
- 사실 고정점 · 50 km describes entire route / 25 cm/km is overall average

#### A 프롬프트
```text
Create a clearly analytical profile of the entire Nîmes aqueduct route, displayed as a long low stone-lined water channel crossing several terrain features. The vertical drop is intentionally magnified only in a separate inset model, while the main profile remains almost flat. Leave blank space for exact distance and average-slope graphics to be added in editing. Do not put a numerical slope on the Pont du Gard alone. Use distinct physical bases for the main model and magnified inset so scale compression is unambiguous. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: orthographic wide route-profile model with broken-distance presentation. Light direction: neutral diffuse top-left studio light.

Camera and lighting specification for this still: orthographic wide route-profile model with broken-distance presentation. Lighting direction and quality: neutral diffuse top-left studio light. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No generated numerals, bridge-only slope label or literal 50km tabletop scale.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · orthographic wide route-profile model with broken-distance presentation
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm 50 km describes entire route
- Confirm 25 cm/km is overall average

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c14 · G6
- 낭독 · 한 뼘씩 낮아지는 길을 이어 물을 님이라는 도시까지 보냈습니다.
- 편집 구간 · 41.54–45.37초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 도시 물받이에 식수가 도착
- 사실 고정점 · water reaches the city receiving level by a gently descending route / bowl is explicitly a generic explanatory model, not the Nîmes castellum

#### A 프롬프트
```text
Build a plainly illustrative stone-channel receiving model, not a reconstruction of any surviving Nîmes monument. A modest stream crosses a low lip into a circular collection bowl on a neutral studio base. Frame this through a 50mm lens at the lip level, looking downstream; morning-like soft illumination enters from upper viewer-left and catches the ripples. Keep the bowl geometry simple and unlabelled, with no palace, city wall or claimed archaeological detail. The physical arrival of water is the single focal event. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 50mm low close view at receiving lip. Light direction: morning sun from upper viewer-left.

Camera and lighting specification for this still: 50mm low close view at receiving lip. Lighting direction and quality: morning sun from upper viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No ornate Trevi fountain, modern tap, invented palace or giant city.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 50mm low close view at receiving lip
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Ensure this looks like a standalone teaching model rather than an unevidenced ancient site.
- Ensure receiving lip is below the incoming channel free surface.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c15 · G6
- 낭독 · 다리 아래로는 강물이 흐르고, 꼭대기에선 마실 물이 건너갑니다.
- 편집 구간 · 45.37–49.44초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 상하 두 물길을 동시에 확인
- 사실 고정점 · two separate elevations / no hydraulic connection between flows

#### A 프롬프트
```text
Frame a wide oblique editorial section through one short upper-channel bay while retaining the full three-tier bridge silhouette behind it; this is a clean physical section, not an x-ray shell. A clear shallow stream travels laterally through the elevated channel, while the broad natural river crosses the foreground beneath the lowest arches. Separate the two surfaces by real height and solid masonry, not by arbitrary colored sheets. The camera angle must make their different travel directions legible without implying a literal cross-junction in plan or any mixing between them. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 35mm oblique bridge section from downstream flank. Light direction: late warm sun from viewer-left rear.

Camera and lighting specification for this still: 35mm oblique bridge section from downstream flank. Lighting direction and quality: late warm sun from viewer-left rear. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No intersecting pipes, shared basin or elevated river-sized stream.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 35mm oblique bridge section from downstream flank
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm two separate elevations
- Confirm no hydraulic connection between flows

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c16 · G7
- 낭독 · 조금만 멀어져도 그저 강 위에 돌다리 하나 놓인 풍경이죠.
- 편집 구간 · 49.44–52.93초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 오늘풍경으로 되돌아옴
- 사실 고정점 · matches first camera / present channel not shown running

#### A 프롬프트
```text
Return to the exact downstream-bank composition of the opening image using the same lens height, horizon and main pier placement. The monument is the present surviving bridge, its upper channel covered and no imaginary stream visible at roof level. Natural river reflections supply the only physical motion. Hold an unobstructed view of the top course so the viewer now understands what was hidden there. This return should feel visually familiar but cognitively changed, with no time-lapse rebuilding or slabs flying back into place. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: same24mm downstream-bank lens as c01. Light direction: same late sun from viewer-left rear.

Camera and lighting specification for this still: same24mm downstream-bank lens as c01. Lighting direction and quality: same late sun from viewer-left rear. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No active current upper water, self-repair, shifting masonry or new buildings.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · same24mm downstream-bank lens as c01
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm matches first camera
- Confirm present channel not shown running

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c17 · G7
- 낭독 · 하지만 물 한 방울의 눈으로 보면, 여기는 교차로입니다.
- 편집 구간 · 52.93–56.54초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 물한방울 시점으로 높은길을 읽음
- 사실 고정점 · droplet is editorial device / present exterior stays dry

#### A 프롬프트
```text
Follow the upper course from an elevated side viewpoint, with the cover slabs forming a narrow route across the centre of frame. Place a small separate water-droplet-shaped optical highlight only in a separate analytical inset, with any explanatory identification added in post-production rather than generated inside the image, not physically hovering over the present monument. The main photographic reconstruction remains an intact dry exterior. The inset is tied spatially to a single channel section and explains the remembered Roman water route. Keep all highlights restrained so the building remains the subject and the final two-waterway image is still earned. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 70mm along covered top course; short lateral glide. Light direction: low sun from viewer-right.

Camera and lighting specification for this still: 70mm along covered top course; short lateral glide. Lighting direction and quality: low sun from viewer-right. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No fantasy floating water creature or modern working channel.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 70mm along covered top course; short lateral glide
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm droplet is editorial device
- Confirm present exterior stays dry

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c18 · G7
- 낭독 · 두 물길이 분명 만나는 자리인데, 서로 한 방울도 섞이지 않는 교차로요.
- 편집 구간 · 56.54–61.50초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 서로섞이지 않는 두 흐름을 엔딩
- 사실 고정점 · upper water separate from river / Roman state explicitly reconstruction

#### A 프롬프트
```text
Close with one restrained Roman working-state section, seen from the same downstream side as the first image. The upper channel carries its small stream across the frame while the Gardon sweeps beneath it at a different direction and elevation. Use a clean near-side section only at one top bay so the relationship remains readable; most of the bridge stays opaque and believable. Hold one complete image of independent flows sharing a landscape. Do not add a third path, a numerical caption or a final decorative diagram. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: locked35mm Roman reconstruction with same landmark pier as opening. Light direction: warm key from viewer-left.

Camera and lighting specification for this still: locked35mm Roman reconstruction with same landmark pier as opening. Lighting direction and quality: warm key from viewer-left. Colour palette: natural limestone ochre, river green, restrained warm highlights. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No mixing, waterfall, contemporary tourists or giant unreal water volumes.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · locked35mm Roman reconstruction with same landmark pier as opening
- 움직이는 대상 · camera and the indicated water or explanatory illumination only
- 고정 대상 · all masonry, channel walls, arches, banks and skyline
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm upper water separate from river
- Confirm Roman state explicitly reconstruction

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.
