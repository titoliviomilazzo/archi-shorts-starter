# s18-vaticano-san-pietro 상세 스틸 이미지 프롬프트

이 문서는 이미지 생성 전 검토용이다. 실제 자료 편집 컷에는 원본 이미지와 사용권이 필요하다. 역사 재현과 분석 모형은 기록사진으로 표시하지 않는다. 효과 후보는 기존 DB 문구를 그대로 가져온 별도 부록이며, 1+1 효과 구성이 미확정된 컷은 생성 승인 상태가 아니다.

## 복사형 프롬프트

### c01 · P1
- 낭독 · 성 베드로 대성당, 이 사슬로요?
- 편집 구간 · 0.00–2.44초
- 자료 유형 · reconstruction / 참조 R1, R2
- 핵심 행동 · 작은 사슬과 큰 돔 대비
- 사실 고정점 · small chain hangs from two fixed supports / basilica silhouette is separate editorial comparison

#### A 프롬프트
```text
Compose a deliberately editorial comparison: a short weighted chain hangs between two fixed wooden posts on a dark walnut bench in the foreground, while a separate softly focused silhouette of Saint Peter’s dome occupies the upper background. The lead weights and iron links are large enough to read on a phone. Keep the chain clearly attached to the posts and smaller than the tabletop. This is a reconstructed teaching setup, not a claim that Poleni conducted his experiment at a specific Vatican window. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 50mm low tabletop close view; slow focus pull toward distant dome silhouette. Light direction: warm window light from upper viewer-left.

Camera and lighting specification for this still: 50mm low tabletop close view; slow focus pull toward distant dome silhouette. Lighting direction and quality: warm window light from upper viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No chain wrapped around basilica; no giant floating chain or people.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 50mm low tabletop close view; slow focus pull toward distant dome silhouette
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm small chain hangs from two fixed supports
- Confirm basilica silhouette is separate editorial comparison

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c02 · P1
- 낭독 · 돔에 금이 갔는데 수학자 폴레니는 작은 사슬을 매달았습니다.
- 편집 구간 · 2.44–6.30초
- 자료 유형 · source_edit / 참조 R3
- 핵심 행동 · 기록된 균열과 작은 장치 연결
- 사실 고정점 · crack pattern follows supplied record / no change in crack opening

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Frame a short vertical masonry fissure from the documented dome damage record, using a supplied source image or a faithful derivative crop rather than inventing a dramatic new crack network. Rough plaster and brick texture should be legible under raking light; the fissure stays open by the same small amount throughout. In the lower edge include an out-of-focus iron chain link as an editorial visual bridge to the workshop. Avoid implying immediate collapse, falling fragments or an authenticated location not established by the source. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Generate no new lettering, numerals, logos or watermark. Keep any required original source lettering only in its source layer, with attribution added separately in editing. Use the supplied licensed source as the unchanged evidence base; crop or highlight without generating substitute historical geometry. Camera: 85mm detail of source-supported masonry crack; short push. Light direction: raking daylight from viewer-right.

Camera and lighting specification for this still: 85mm detail of source-supported masonry crack; short push. Lighting direction and quality: raking daylight from viewer-right. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No fresh collapse, missing dome segment or invented crack map.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 85mm detail of source-supported masonry crack; short push
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm crack pattern follows supplied record
- Confirm no change in crack opening

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c03 · P2
- 낭독 · 양 끝을 잡아도 탁자 하나에 들어갈 크기예요.
- 편집 구간 · 6.30–9.02초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 두 지지점 사이 크기 확인
- 사실 고정점 · one stable pair of suspension points / weights differ in size

#### A 프롬프트
```text
Show the full teaching apparatus on a single bench from a three-quarter angle. Two plain wooden supports hold the ends of one linked line, with several unequally sized grey weights attached between them. Include the bench edges and one plain draughting sheet to make its tabletop scale immediately understandable, without adding numerical rulers. Keep both suspension points visible and preserve their positions for all later close-ups. The line sags naturally under gravity; no unsupported link rises above either attachment. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 35mm three-quarter bench view with both posts visible. Light direction: soft window light from high viewer-left.

Camera and lighting specification for this still: 35mm three-quarter bench view with both posts visible. Lighting direction and quality: soft window light from high viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No modern lab electronics, uniform necklace beads or missing supports.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 35mm three-quarter bench view with both posts visible
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm one stable pair of suspension points
- Confirm weights differ in size

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c04 · P2
- 낭독 · 성당 한 바퀴는커녕 문 하나도 못 두를 것 같죠.
- 편집 구간 · 9.02–12.19초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 성당 둘레를 묶을 도구처럼 보이지 않는 크기
- 사실 고정점 · doorway is separate illustration / same small apparatus retained

#### A 프롬프트
```text
Place the same small hanging apparatus in the lower foreground and a large unlettered architectural elevation of a doorway on a separate upright drawing board behind it. The board is an illustrative scale comparison, not the physical building placed on the bench. Keep the lead weights sharply focused and the doorway softer so the visual joke remains the inadequacy of a tiny wrapping material. Maintain the same two posts, dark table and gravity-sagging line; do not add a second chain or numerical measurement. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 70mm side-on tabletop and separate scale board. Light direction: late window key from viewer-left.

Camera and lighting specification for this still: 70mm side-on tabletop and separate scale board. Lighting direction and quality: late window key from viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No miniature person, literal chain measuring historic door or fake dimensional values.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 70mm side-on tabletop and separate scale board
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm doorway is separate illustration
- Confirm same small apparatus retained

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c05 · P3
- 낭독 · 게다가 사슬에는 크기가 서로 다른 추까지 줄줄이 달려 있어요.
- 편집 구간 · 12.19–15.94초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 서로 다른 추를 접사
- 사실 고정점 · weights are unequal / each weight loads the same continuous line

#### A 프롬프트
```text
Make a tactile macro image of two neighboring lead weights of visibly different volume threaded or attached to the same iron line according to the reference construction. The nearer weight catches a narrow highlight, the smaller one sits just behind it, and both pull downward from the line. Show dull lead, oxidized iron and restrained tool marks rather than polished jewelry. The background wooden support is soft but recognizable from the previous shot, keeping this detail part of the same experiment. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 100mm macro along central third of chain. Light direction: warm raking key from upper viewer-right.

Camera and lighting specification for this still: 100mm macro along central third of chain. Lighting direction and quality: warm raking key from upper viewer-right. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No gold necklace, equal marbles, decorative gems or disconnected masses.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 100mm macro along central third of chain
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm weights are unequal
- Confirm each weight loads the same continuous line

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c06 · P3
- 낭독 · 무거운 곳은 더 무거운 추를, 가벼운 곳은 가벼운 추를 달았습니다.
- 편집 구간 · 15.94–20.33초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 추와 돔 부분 무게 대응
- 사실 고정점 · segment-weight correspondence is illustrative / weights remain unequal

#### A 프롬프트
```text
Create a separate analytical teaching model beside the apparatus: several meridian slices of the dome are aligned left to right on ivory cards, paired spatially with the unequal weights beneath them. Use only a few source-supported segments and preserve their correspondence by position and neutral material tone, leaving exact masses to later verified graphics. The real hanging line remains untouched in the background. This image explains the principle of proportional loading; it is not a new engineering calculation or a claim that the displayed slice geometry reproduces an authenticated Poleni workshop artifact. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 50mm paired physical-model view, not split-screen text. Light direction: diffuse daylight from upper viewer-left.

Camera and lighting specification for this still: 50mm paired physical-model view, not split-screen text. Lighting direction and quality: diffuse daylight from upper viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No invented mass numerals or fake complete structural calculation.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 50mm paired physical-model view, not split-screen text
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm segment-weight correspondence is illustrative
- Confirm weights remain unequal

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c07 · P3
- 낭독 · 추의 흔들림이 멎자 길게 처진 선만 남습니다.
- 편집 구간 · 20.33–23.30초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 흔들림이 멎은 선
- 사실 고정점 · stable gravity-sagging shape / supports fixed at both ends

#### A 프롬프트
```text
Isolate the weighted line frontally against a nearly dark workshop background. Both suspension points remain just inside the upper corners, and every weight hangs vertically from a naturally sagging curve. Capture the instant after slight motion has settled, with the links crisp and the lead surfaces quietly illuminated. The empty space above the line should feel like a missing answer. Keep the apparatus unchanged from the previous views so viewers can recognize the same curve that will soon be traced and inverted. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 85mm frontal isolated chain profile. Light direction: low warm side light from viewer-right.

Camera and lighting specification for this still: 85mm frontal isolated chain profile. Lighting direction and quality: low warm side light from viewer-right. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No physical inversion, magnetic levitation or exaggerated motion blur.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 85mm frontal isolated chain profile
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm stable gravity-sagging shape
- Confirm supports fixed at both ends

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c08 · P3
- 낭독 · 그런데 저렇게 휘어진 줄을 대체 돔 어디에 쓴 걸까요?
- 편집 구간 · 23.30–26.75초
- 자료 유형 · analytical_model / 참조 R1, R2
- 핵심 행동 · 처진선과 돔도면이 아직 안 맞는 긴장
- 사실 고정점 · actual chain still sags / dome meridian is separate diagram

#### A 프롬프트
```text
Frame the settled chain in the lower half and a separate upright ivory board carrying the verified outline of a dome meridian in the upper half. The line on the board rises while the real chain sags, making their apparent mismatch immediately visible. Both outlines stay separate and unchanged; the stone building is not modeled as suspended from the chain. Place a plain transparent tracing sheet beside the apparatus as a small practical clue to the next action. Keep the visual question contained in this single bench-scale composition. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 65mm eye-level line and blank meridian board. Light direction: soft high-left window light.

Camera and lighting specification for this still: 65mm eye-level line and blank meridian board. Lighting direction and quality: soft high-left window light. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No inverted physical chain, direct stone loading on wire or fake engineering labels.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 65mm eye-level line and blank meridian board
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm actual chain still sags
- Confirm dome meridian is separate diagram

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c09 · P4
- 낭독 · 답은 사슬을 거꾸로 보면 나옵니다.
- 편집 구간 · 26.75–29.00초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 종이 위 곡선만 반바퀴 뒤집음
- 사실 고정점 · only traced curve rotates / physical chain remains downward

#### A 프롬프트
```text
Show a transparent tracing sheet with the actual settled chain curve transferred onto it, lying above the apparatus drawing on a dark bench. Capture the sheet midway through a half-turn around a visible central pin in an explicitly analytical presentation; no hand is required. The real weighted chain is still hanging downward at the edge of the frame, unchanged by this manipulation. Keep the pin and paper edges readable so viewers understand that a diagram is rotating rather than gravity reversing or the masonry transforming. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 50mm overhead tracing-table view; gentle clockwise camera drift. Light direction: broad window light from upper viewer-left.

Camera and lighting specification for this still: 50mm overhead tracing-table view; gentle clockwise camera drift. Lighting direction and quality: broad window light from upper viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No floating inverted weights or architectural morphing.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 50mm overhead tracing-table view; gentle clockwise camera drift
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm only traced curve rotates
- Confirm physical chain remains downward

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c10 · P4
- 낭독 · 아래로 늘어진 선이 뒤집히는 순간, 돌 아치가 솟아오르죠.
- 편집 구간 · 29.00–32.96초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 뒤집힌 곡선이 아치선과 맞음
- 사실 고정점 · upper curve is inversion of same lower curve / curve is not assumed semicircular

#### A 프롬프트
```text
Present the inverted tracing as an upward arch-shaped line on an ivory plane, with the original hanging chain profile retained on a separate lower plane for comparison. A small masonry arch segment sits behind the upper curve without being physically assembled by it. Preserve the exact reversed curve rather than replacing it with a perfect semicircle. The visual discovery is geometric: a hanging equilibrium shape can be read upside down for compression. Keep the curve readable and the surrounding materials quiet, avoiding an explosion of arrows or an entire building rising from paper. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 70mm front-on paired curve model. Light direction: warm key from upper viewer-right.

Camera and lighting specification for this still: 70mm front-on paired curve model. Lighting direction and quality: warm key from upper viewer-right. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No chain turning into stone, self-building arch or unsupported actual blocks.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 70mm front-on paired curve model
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm upper curve is inversion of same lower curve
- Confirm curve is not assumed semicircular

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c11 · P4
- 낭독 · 추는 돔의 각 부분이 얼마나 무거운지를 옮겨 놓은 거였어요.
- 편집 구간 · 32.96–36.49초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 추의 차이가 돔조각 차이였음을 회수
- 사실 고정점 · same earlier segment order / no actual dome suspended from weights

#### A 프롬프트
```text
Place a short row of dome meridian segment models above their corresponding unequal lead weights, now aligned with the inverted tracing that revealed the method. Use the same segment order and weight order established earlier, with a small gap between the paper planes to show that they are analytical representations rather than a machine lifting real stone. Light one corresponding pair most clearly while keeping the neighboring pairs visible at lower contrast. The image must explain proportional loading without invented dimensions, numerical masses or a claim of exact experimental replication. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 85mm oblique series of segments and hanging masses. Light direction: diffuse high-right studio light.

Camera and lighting specification for this still: 85mm oblique series of segments and hanging masses. Lighting direction and quality: diffuse high-right studio light. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No equal weight substitution, misordered pairs or fake mass labels.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 85mm oblique series of segments and hanging masses
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm same earlier segment order
- Confirm no actual dome suspended from weights

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c12 · P5
- 낭독 · 폴레니는 뒤집은 선을 돔을 옆으로 자른 도면에 겹쳤습니다.
- 편집 구간 · 36.49–40.08초
- 자료 유형 · analytical_model / 참조 R1, R2
- 핵심 행동 · 참고도판의 정적인 단면선과 뒤집힌 사슬곡선의 관계를 보존한다. 효과 애니메이션은 c13에서만 적용한다.
- 사실 고정점 · section geometry must come from source / tracing is force-path model not repair material

#### A 프롬프트
```text
Use the verified historical meridian section of Saint Peter’s dome as the controlling geometry, showing the shell thicknesses and support region exactly as the supplied plate records them. Overlay the inverted weighted-line tracing in a restrained warm tone within that section, preserving its scale and placement from the scholarly reference. The traced line is not automatically a hoop, a repair joint or a crack. Keep the drawing on one clean ivory plane with enough margin to inspect the relationship; do not invent a simplified shell profile when the source figure has not yet been supplied. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: orthographic source-based dome meridian, fixed framing. Light direction: neutral even illumination from upper viewer-left.

Camera and lighting specification for this still: orthographic source-based dome meridian, fixed framing. Lighting direction and quality: neutral even illumination from upper viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No fabricated shell thickness, exact load claim or guessed curve fit.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · orthographic source-based dome meridian, fixed framing
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm section geometry must come from source
- Confirm tracing is force-path model not repair material

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c13 · P5
- 낭독 · 돌이 옆의 돌을 누르는 힘이 어디로 지나가는지 알아보려고요.
- 편집 구간 · 40.08–43.44초
- 자료 유형 · analytical_model / 참조 R1, R3
- 핵심 행동 · 이웃 돌로 압축력이 전해짐
- 사실 고정점 · contacts remain closed / path stays within masonry section

#### A 프롬프트
```text
Show a small source-consistent portion of the dome meridian as a physical masonry teaching model. Adjacent brick or stone units meet through realistic mortar contacts; a narrow warm illumination follows the compression path through those contacts without lifting or separating the units. Keep the path within the masonry section and let the contact planes remain visible around it. This close view explains how neighboring pieces push on one another, while making no claim to calculate all three-dimensional dome forces or resolve every historical stability debate. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 100mm model cut through adjoining masonry units. Light direction: raking light from upper viewer-right.

Camera and lighting specification for this still: 100mm model cut through adjoining masonry units. Lighting direction and quality: raking light from upper viewer-right. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No tension cable inside stones, floating blocks or universal stability proof.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 100mm model cut through adjoining masonry units
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm contacts remain closed
- Confirm path stays within masonry section

#### DB 효과 후보
- layer.loadpath.10 · archi-shorts · observed · 압축력이전달되는해석경로후보. observed이므로시험용. 실제모드/안정해석결과가아니다.
```text
[LoadPath] A warm glow travels down through the structure along the line the weight actually takes: it appears first at the source-defined upper masonry segment of the dome meridian, runs down through the adjacent masonry contact regions along the verified meridian curve in sequence, and gathers at the source-defined lower support region of that meridian section where it holds. Only the members carrying the load light up, one after another in that order, each brightening as the glow reaches it and dimming behind it; members that carry nothing stay dark. The building itself does not move, deform or change shape at any point.
```
원문 템플릿의 위치 매개변수만 치환했다.

### c14 · P6
- 낭독 · 그럼 실제 성당은 무엇으로 붙잡았을까요?
- 편집 구간 · 43.44–46.18초
- 자료 유형 · reconstruction / 참조 R2, R3
- 핵심 행동 · 종이밖 실제돔으로 질문 전환
- 사실 고정점 · dome and drum relationship exact / no rings exposed before reveal

#### A 프롬프트
```text
Leave the bench and show the actual exterior relationship of the dome and its supporting drum using a faithful architectural reconstruction based on the source elevation. Frame the curved cap above and the cylindrical drum below, with restrained shadow separating their volumes. Keep the surface opaque so the real reinforcement has not yet been revealed. The camera view should establish where a full-size intervention belongs, distinct from the tiny analysis apparatus. Avoid panoramic sightseeing details that would distract from the dome support region. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 40mm dome drum oblique exterior from reference viewpoint. Light direction: warm sunset light from viewer-left rear.

Camera and lighting specification for this still: 40mm dome drum oblique exterior from reference viewpoint. Lighting direction and quality: warm sunset light from viewer-left rear. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No imaginary scaffolding, modern crane or extra dome shell.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 40mm dome drum oblique exterior from reference viewpoint
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm dome and drum relationship exact
- Confirm no rings exposed before reveal

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c15 · P6
- 낭독 · 돔과 그 아래 둥근 받침에는 철제 고리 여섯 개가 둘러졌습니다.
- 편집 구간 · 46.18–49.92초
- 자료 유형 · source_edit / 참조 R2
- 핵심 행동 · 여섯고리를 도판정확위치에 공개
- 사실 고정점 · exactly six added hoops / levels follow historical plate not guessed spacing

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Use the historical reinforcement plate reproduced in the Senate collection as the controlling image, retaining the exact dome outline, drum and six documented hoop levels. Isolate the six additional iron circles through restrained warm highlights that follow the existing marks on the plate; do not draw any new hoop, infer a seventh level or space the circles evenly . Retain original lettering only within a rights-cleared source layer. If the plate image is missing, this shot remains reference-required instead of substituting a plausible but invented ring arrangement. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Generate no new lettering, numerals, logos or watermark. Keep any required original source lettering only in its source layer, with attribution added separately in editing. Use the supplied licensed source as the unchanged evidence base; crop or highlight without generating substitute historical geometry. Camera: source-plate frontal section; no perspective invention. Light direction: even paper illumination from upper left.

Camera and lighting specification for this still: source-plate frontal section; no perspective invention. Lighting direction and quality: even paper illumination from upper left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No equal-spacing shortcut, extra hoops or generated pseudo-historical writing.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · source-plate frontal section; no perspective invention
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm exactly six added hoops
- Confirm levels follow historical plate not guessed spacing

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c16 · P6
- 낭독 · 돌이 바깥으로 벌어지면 고리가 그 둘레를 붙잡아 주죠.
- 편집 구간 · 49.92–53.17초
- 자료 유형 · analytical_model / 참조 R2, R3
- 핵심 행동 · 한철제 고리가 바깥벌어짐에 저항
- 사실 고정점 · circumferential restraint / actual masonry and hoop remain fixed

#### A 프롬프트
```text
Create a localized analytical section at one verified reinforcement level, showing an iron circumferential member in firm contact with the masonry region it restrains according to the documented construction detail. Preserve the curvature and any source-supported joint configuration; do not invent exposed modern bolts or hydraulic clamps. Use a small separate faint outline to indicate an exaggerated outward tendency only, while the actual stone and iron remain fixed. The real event is restraint around a circumference, not cracks magically sealing or a chain crushing the dome inward. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: 85mm source-based sectional iron hoop detail. Light direction: warm side key from viewer-right.

Camera and lighting specification for this still: 85mm source-based sectional iron hoop detail. Lighting direction and quality: warm side key from viewer-right. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No self-healing fissure, radial tightening cable or invented modern turnbuckle.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · 85mm source-based sectional iron hoop detail
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm circumferential restraint
- Confirm actual masonry and hoop remain fixed

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c17 · P6
- 낭독 · 가장 큰 고리는 지름만 육십 미터였습니다.
- 편집 구간 · 53.17–55.94초
- 자료 유형 · source_edit / 참조 R2
- 핵심 행동 · 가장큰고리 스케일 확인
- 사실 고정점 · largest hoop diameter belongs to verified source / hoop remains at documented level

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Frame the largest documented reinforcement circle in its historical plate context, wide enough to show the true relationship between that circle, the dome drum and surrounding masonry. Keep a clean empty margin beside it for the verified diameter annotation to be composited later. The circle is a circumference around the building, not a flat disk or a separate giant ring floating in the square. Do not relocate it to the crown simply because that gives a clearer silhouette; its location must be read from the actual source image. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Generate no new lettering, numerals, logos or watermark. Keep any required original source lettering only in its source layer, with attribution added separately in editing. Use the supplied licensed source as the unchanged evidence base; crop or highlight without generating substitute historical geometry. Camera: orthographic full width of source-selected largest hoop. Light direction: neutral high-left illumination.

Camera and lighting specification for this still: orthographic full width of source-selected largest hoop. Lighting direction and quality: neutral high-left illumination. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No generated 60m lettering, guessed hoop height or solid metal disk.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · orthographic full width of source-selected largest hoop
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm largest hoop diameter belongs to verified source
- Confirm hoop remains at documented level

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c18 · P7
- 낭독 · 저 거대한 돔의 힘길을 읽는 데는 처음 그 작은 사슬이면 됐습니다.
- 편집 구간 · 55.94–60.20초
- 자료 유형 · analytical_model / 참조 R1, R2
- 핵심 행동 · 小사슬위에 큰돔 힘길을 회수
- 사실 고정점 · same physical chain as opening / dome drawing is analytical overlay not actual load

#### A 프롬프트
```text
Return to the opening bench composition with the same two posts, unequal lead weights and naturally hanging iron line. Above the apparatus, place a separate transparent upright tracing of the verified dome meridian aligned to the inverted analytical curve, leaving clear air between drawing plane and real chain. The distant basilica silhouette is soft and unchanged. The final impression is that a small physical model makes a large structure legible, not that it holds the structure up. Finish on one crisp line shared by the remembered experiment and drawing. Vertical 9:16 cinematic architectural editorial reconstruction, one focal fact centred in frame and readable at phone size. Keep the upper and lower caption bands uncluttered. Preserve the referenced geometry and material scale. Render no people, faces, lettering, numerals, logos, watermarks or decorative diagrams. This is a reconstruction or analytical illustration, never an archival photograph. Camera: same50mm foreground apparatus lens as opening, locked composition. Light direction: same warm window key from upper viewer-left.

Camera and lighting specification for this still: same50mm foreground apparatus lens as opening, locked composition. Lighting direction and quality: same warm window key from upper viewer-left. Colour palette: ivory paper, muted lead grey, dark walnut and warm wrought iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No people, faces, lettering, fake inscriptions, logos, watermark, extra architecture. No literal basilica balanced on apparatus, inverted physical weights or magical shrinkage.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep subject, geometry and event identical. Change the camera azimuth by at most 15 degrees and soften the key light from the same physical source; preserve screen direction.
```

#### 4초 영상 인계
- 카메라 · same50mm foreground apparatus lens as opening, locked composition
- 움직이는 대상 · camera and paper tracing or explanatory light only; chain may settle subtly but never invert physically
- 고정 대상 · apparatus supports, table, existing masonry, reinforcement hoop geometry and background architecture
- 끝 상태 · Hold the single focal relationship; do not add a new event or change historical state.

#### 수령 후 확인
- Compare camera-facing geometry with the specified source before generation.
- Confirm same physical chain as opening
- Confirm dome drawing is analytical overlay not actual load

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.
