# s16-paris-eiffel 상세 스틸 이미지 프롬프트

이 문서는 이미지 생성 전 검토용이다. 실제 자료 편집 컷에는 원본 이미지와 사용권이 필요하다. 역사 재현과 분석 모형은 기록사진으로 표시하지 않는다. 효과 후보는 기존 DB 문구를 그대로 가져온 별도 부록이며, 1+1 효과 구성이 미확정된 컷은 생성 승인 상태가 아니다.

## 복사형 프롬프트

### c01 · S01
- 낭독 · 에펠탑, 이 틈을 어떻게 맞출까요?
- 편집 구간 · 0.00–2.73초
- 자료 유형 · analytical_model / 참조 R2
- 핵심 행동 · 중앙에 남은 하늘 한 줄로 두 들보 끝의 미완성 접합을 보여준다.
- 사실 고정점 · 서로 맞댈 두 끝과 미완성 간극 / 부재 끝은 독립된 강체이며 임의로 휘지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary analytical reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Two opposed ends of first-level iron girders nearly meet across the vertical centre. A hairline of blue Paris sky remains between the end faces. Preserve every plate outline, rivet row and temporary support visible in the supplied historical joining detail. Frame the metal as two immense dark masses at left and right, with daylight trapped between them. The gap is an editorial emphasis on alignment, not a documented measurement or damage event. Show the unfinished tower beyond only as a faint fragment at the bottom, so the object remains identifiable without revealing the base jack. Camera: 100mm macro-equivalent, square to the actual mating plane. Light: upper-left afternoon daylight skims iron edges. Palette: charcoal iron / warm brown primer / narrow blue sky.

Camera and lighting specification for this still: 100mm macro-equivalent, square to the actual mating plane. Lighting direction and quality: upper-left afternoon daylight skims iron edges. Colour palette: charcoal iron / warm brown primer / narrow blue sky. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 서로 맞댈 두 끝과 미완성 간극가 화면에서 판독되는지 확인
- 부재 끝은 독립된 강체이며 임의로 휘지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인
- 상부 접합부 간극의 전후는 실제 1887년 사진 그대로의 기록처럼 제시하지 않고 정렬 원리 분석 재현으로 구분한다.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c02 · S02
- 낭독 · 네 다리를 따로 세우고 첫 층을 잇던 때입니다.
- 편집 구간 · 2.73–5.49초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 완성 상부 없이 네 다리와 임시 비계가 선 첫 층 공사 단계를 드러낸다.
- 사실 고정점 · 첫 층 조립 단계의 미완성 탑 / 완성 상부와 안테나를 넣지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Reconstruct the Eiffel Tower construction site at the first-level assembly stage in 1887 from the supplied construction photograph. Show four lower iron legs rising separately from the Champ de Mars, each inclined inward, with the first-level girders still being joined. Timber temporary scaffolds occupy the work zone at the recorded scale. Keep the background Paris skyline low and subdued. The unfinished height ends at the source-verified construction stage, with neither a completed upper tower nor modern antennas. Leave a clear view across the central void and make the meeting height of the girders the dominant horizontal event. Camera: 35mm elevated oblique view. Light: daylight from camera-right through mild overcast. Palette: warm primer brown / pale limestone / muted blue.

Camera and lighting specification for this still: 35mm elevated oblique view. Lighting direction and quality: daylight from camera-right through mild overcast. Colour palette: warm primer brown / pale limestone / muted blue. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 첫 층 조립 단계의 미완성 탑가 화면에서 판독되는지 확인
- 완성 상부와 안테나를 넣지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c03 · S02
- 낭독 · 아래에선 한참 떨어져 있지만 다들 안쪽으로 기울었죠.
- 편집 구간 · 5.49–8.72초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 다리 바닥의 큰 간격과 위쪽의 수렴을 한 시선에서 비교한다.
- 사실 고정점 · 다리4개가 안쪽으로 기울어짐 / 지평선 및 실제 기울기 유지

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Present a clean architectural scale reconstruction of the four inclined lower legs, isolated against a softly lit Paris construction context. The viewer sees all four separate footing positions and the narrowing space between the legs as they rise. Keep the iron lattice members and their true curvature referenced to the construction drawing. The ground plane remains level. Use perspective to make separation at the bottom and convergence near first level readable in one glance, without exaggerating lean angles. A faint neutral first-level plane establishes the future connection height, while the central air remains genuinely empty. Camera: 28mm high three-quarter view. Light: large soft key from upper-left. Palette: brown iron / sand-grey ground / neutral air.

Camera and lighting specification for this still: 28mm high three-quarter view. Lighting direction and quality: large soft key from upper-left. Colour palette: brown iron / sand-grey ground / neutral air. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 다리4개가 안쪽으로 기울어짐가 화면에서 판독되는지 확인
- 지평선 및 실제 기울기 유지가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c04 · S02
- 낭독 · 이 다리에서 뻗은 들보와 저 다리에서 뻗은 들보가
- 편집 구간 · 8.72–11.67초
- 자료 유형 · reconstruction / 참조 R2
- 핵심 행동 · 서로 다른 다리에서 온 두 들보의 지지 경로가 접합부를 향해 이어진다.
- 사실 고정점 · 각 들보가 다른 다리에 연결됨 / 두 부재의 지지 경로가 보임

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Look diagonally along one first-level lattice girder toward its opposing member, with each girder clearly attached to a different inclined tower leg. The near girder enters from the lower-left foreground; the opposing one enters from upper-right in a distinct depth plane. Their mating region lies near the centre. Repeat real rivet and lattice patterns only where the supplied detail shows them. Keep both beams rigid, with a visible path back toward their respective supporting legs. The purpose is to reveal two separate origins converging at one junction, so avoid making the beams appear cantilevered from nowhere or already fused together. Camera: 50mm oblique lens along girder axis. Light: raking sunlight from upper-right. Palette: warm brown iron / cream sky / soft shadows.

Camera and lighting specification for this still: 50mm oblique lens along girder axis. Lighting direction and quality: raking sunlight from upper-right. Colour palette: warm brown iron / cream sky / soft shadows. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 각 들보가 다른 다리에 연결됨가 화면에서 판독되는지 확인
- 두 부재의 지지 경로가 보임가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c05 · S02
- 낭독 · 허공의 바로 그 자리에서 만나야 네 다리가 한 몸이 됩니다.
- 편집 구간 · 11.67–15.08초
- 자료 유형 · analytical_model / 참조 R1
- 핵심 행동 · 첫 층 폐합 윤곽이 네 독립 다리를 하나의 구조로 묶을 위치를 드러낸다.
- 사실 고정점 · 첫 층 연결이 네 다리를 묶음 / 분석 모형은 실사 사료로 오인시키지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Render a shallow high-angle view of the unfinished first-level frame as a coherent structural model. The four inclined legs define four corner positions and the girders bridge between them to form a future closed perimeter. Hold one remaining alignment region visibly unfinished, so the frame is close to becoming continuous but is not shown as already complete. Place the true ground far below for height context, with the timber scaffolds lightly visible through the central opening. Use actual first-level proportions from the reference, not a generic square table or a four-legged modern truss. The central void gives the viewer an immediate reason for all four connections to matter. Camera: 40mm downward oblique framing. Light: soft light from frame-left. Palette: brown iron / pale ochre earth / deep void.

Camera and lighting specification for this still: 40mm downward oblique framing. Lighting direction and quality: soft light from frame-left. Colour palette: brown iron / pale ochre earth / deep void. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 첫 층 연결이 네 다리를 묶음가 화면에서 판독되는지 확인
- 분석 모형은 실사 사료로 오인시키지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c06 · S03
- 낭독 · 끝이 조금 어긋났다면 여러분은 어디에 손을 대시겠어요?
- 편집 구간 · 15.08–18.50초
- 자료 유형 · analytical_model / 참조 R2
- 핵심 행동 · 높이가 조금 다른 두 강체 단부를 같은 깊이에서 맞대어 비교한다.
- 사실 고정점 · 높이 차이는 조정 원리 도식 / 실측 간극이나 사고로 주장하지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Show a deliberately simplified technical reconstruction of a first-level girder junction from the side. Two matching end faces sit at slightly different heights, separated by a modest open gap, so the alignment problem is unmistakable. Use the real plate thickness and riveted construction language from the historical detail. Keep the discrepancy small rather than portraying catastrophic displacement or buckled iron. Position both end faces at the same depth from the camera, allowing their upper surfaces to be compared without perspective trickery. Plain sky fills the opening between them, and the scaffold below remains visibly separate from the iron structure. Camera: 85mm near-orthographic side view. Light: upper-left diffuse daylight with edge highlight. Palette: brown-black iron / pale sky.

Camera and lighting specification for this still: 85mm near-orthographic side view. Lighting direction and quality: upper-left diffuse daylight with edge highlight. Colour palette: brown-black iron / pale sky. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 높이 차이는 조정 원리 도식가 화면에서 판독되는지 확인
- 실측 간극이나 사고로 주장하지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
- E4c · archi-shorts · video_pass · 정보 효과, 높이 비교를 위한 시험 후보. 정확한 선 고정과 실제 렌더 확인 필요.
```text
a bold thick glowing red laser line crossing the frame horizontally at the true upper level of the left girder end in the analytical side view
```
원문 템플릿의 위치 매개변수만 치환했다.

### c07 · S03
- 낭독 · 눈은 자꾸 두 쇳덩이 사이로 새어 나오는 빛을 좇습니다.
- 편집 구간 · 18.50–21.92초
- 자료 유형 · reconstruction / 참조 R2
- 핵심 행동 · 빛나는 틈이 눈을 끌고 주변의 거대한 금속은 고정된다.
- 사실 고정점 · 간극의 하늘이 다음 결말과 연결됨 / 금속은 녹아 흐르거나 파손되지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Compose a tighter view of the meeting faces, preserving their alignment discrepancy from the previous shot. The illuminated ribbon of sky between the iron ends now sits dead centre and occupies enough image area to read on a phone. The faces themselves stay dark, textured with period surface treatment and blunt plate edges rather than polished precision-machined modern steel. A few correct rivet heads on each side establish scale. Focus sharply on the two edge silhouettes, with the distant scaffold soft and unmistakably lower. The emotional action is the viewer being drawn to the bright space rather than to the heavy metal around it. Camera: 135mm telephoto close-up. Light: backlight from high behind the gap, restrained fill from left. Palette: blue slit / warm dark iron.

Camera and lighting specification for this still: 135mm telephoto close-up. Lighting direction and quality: backlight from high behind the gap, restrained fill from left. Colour palette: blue slit / warm dark iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 간극의 하늘이 다음 결말과 연결됨가 화면에서 판독되는지 확인
- 금속은 녹아 흐르거나 파손되지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c08 · S03
- 낭독 · 그 틈에 망치를 들고 올라가 한쪽을 툭 칠 것 같죠.
- 편집 구간 · 21.92–25.31초
- 자료 유형 · analytical_model / 참조 R2
- 핵심 행동 · 상상 속 망치 그림자가 지나가되 부재에는 접촉하지 않는다.
- 사실 고정점 · 망치는 시청자 가정 / 실제 타격 시공이나 사고를 창작하지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Keep the same rigid girder ends from the previous technical shot, with the sky gap still open. A single soft hammer-shaped shadow enters only the peripheral lower foreground as an editorial representation of the viewer considering a direct tap. No hand, person or actual hammer touches the iron, and neither end deforms or jumps. The imagined shadow must be visually distinct from the reconstructed physical worksite, without inventing a historical construction incident. Let the beam faces remain the main focus and the shadow subordinate, so this is a question about where to act rather than a demonstration of a recorded method. Camera: 85mm fixed side view for the imagined choice. Light: low raking key from lower-left producing a soft conceptual shadow. Palette: iron brown / grey shadow / pale blue gap.

Camera and lighting specification for this still: 85mm fixed side view for the imagined choice. Lighting direction and quality: low raking key from lower-left producing a soft conceptual shadow. Colour palette: iron brown / grey shadow / pale blue gap. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no physical hammer contact or impact.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["editorial imagined hammer shadow, not the iron"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 망치는 시청자 가정가 화면에서 판독되는지 확인
- 실제 타격 시공이나 사고를 창작하지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c09 · S04
- 낭독 · 그런데 높이 매달린 들보를 맞추는 손은 한참 아래에 있었습니다.
- 편집 구간 · 25.31–29.22초
- 자료 유형 · reconstruction / 참조 R1
- 핵심 행동 · 시선이 다리의 곡선을 따라 위 접합부에서 하부로 급히 내려간다.
- 사실 고정점 · 상부 접합과 하부 조절 위치 연결 / 구조 전체가 휘어 변형되는 과장 금지

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Frame a powerful downward view along one sweeping inclined lower tower leg, linking the first-level girder region high at the top edge with the footing zone deep below. The camera is close enough to the iron lattice to feel its huge rigid curvature while the ground expands toward the lower third. Use the same construction stage and actual leg silhouette as the supplied photograph. Temporary timber scaffolds remain in their own clear depth plane. The image redirects attention away from the upper junction toward the base; it must not show a fantastical continuous piston inside the whole leg or make the tower bend elastically. Camera: 24mm steep downward architectural view. Light: daylight from camera-right, footing zone readable in bounced light. Palette: warm iron / buff gravel / muted sky.

Camera and lighting specification for this still: 24mm steep downward architectural view. Lighting direction and quality: daylight from camera-right, footing zone readable in bounced light. Colour palette: warm iron / buff gravel / muted sky. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · tilt and track down along the leg toward the footing
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · the footing zone becomes dominant

#### 수령 후 확인
- 上 접합과 하부 조절 위치 연결가 화면에서 판독되는지 확인
- 구조 전체가 휘어 변형되는 과장 금지가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c10 · S04
- 낭독 · 다리 밑에 무거운 쇠를 살짝 들어 올릴 장치를 놓았죠.
- 편집 구간 · 29.22–32.57초
- 자료 유형 · analytical_model / 참조 R3
- 핵심 행동 · 잭의 압축 접촉을 단면으로 열어 조절 위치를 드러낸다.
- 사실 고정점 · 잭은 시공 중 임시 조절장치 / 부재-잭-기초 접촉이 끊기지 않음

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Build a source-led sectional teaching reconstruction of a temporary hydraulic alignment jack at the tower footing. Show a compact nineteenth-century hydraulic device bearing firmly against the intended iron shoe or support and its masonry or concrete support block. Cut only the foreground portion needed to expose the contact, while the principal leg and footing remain recognisable and solid. The load-carrying contact must be visibly closed, with no jack floating in air and no unsupported leg. Keep hoses, fittings and pump details restrained to what the supplied drawing actually supports. The surrounding ground and foundation establish why a tiny movement here can affect a high connection. Camera: 65mm technical sectional view. Light: soft key from upper-left with warm interior fill. Palette: dark iron / stone grey / warm hydraulic metal.

Camera and lighting specification for this still: 65mm technical sectional view. Lighting direction and quality: soft key from upper-left with warm interior fill. Colour palette: dark iron / stone grey / warm hydraulic metal. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["a source-verified small hydraulic adjustment in the analytical inset"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 잭은 시공 중 임시 조절장치가 화면에서 판독되는지 확인
- 부재-잭-기초 접촉이 끊기지 않음가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
- layer.scan.5 · archi-shorts · still_pass · 단면 개방의 스틸 PASS 후보. 실제 잭 배치 참고자료가 먼저 필요.
```text
[Scan] A single thin brilliant cyan plane of light sweeps slowly through the foreground footing reconstruction only from the front edge to the exposed bearing contact, held perfectly flat and perpendicular to its travel. Everything the plane has already passed is left open as a clean cutaway, its cut faces showing the raw thickness of every wall and floor slab, while everything ahead of it stays solid and untouched. The plane is a narrow bright core with a soft glow on the surfaces it crosses, and it never tilts, never stops and never reverses.
```
원문 템플릿의 위치 매개변수만 치환했다.

### c11 · S05
- 낭독 · 발밑이 움직이자 저 위에서도 들보의 끝이 움직입니다.
- 편집 구간 · 32.57–35.81초
- 자료 유형 · analytical_model / 참조 R3
- 핵심 행동 · 하부의 작은 조절과 상부의 위치 정렬을 대응시킨다.
- 사실 고정점 · 아래 조정과 위 정렬의 인과 / 구조부재 강체 위치 조정만 표현

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Show one coherent structural teaching model, with the tower foot enlarged in the lower-left and the corresponding first-level connection visible in the upper-right through a linked contextual view. The two regions belong to the same fixed geometry and keep a common vertical reference. At the foot, the compact temporary jack sits in full compression contact. Above, the paired girder ends show the matching direction of alignment correction. This is a visual explanation of a small controlled adjustment, not a claim of measured displacement. Keep any alternate position as a very restrained pale edge comparison and never duplicate the whole tower or make its iron members stretch. Camera: 50mm axonometric analytical view. Light: large soft source from upper-right. Palette: warm brown structure / cream field / restrained pale comparison.

Camera and lighting specification for this still: 50mm axonometric analytical view. Lighting direction and quality: large soft source from upper-right. Colour palette: warm brown structure / cream field / restrained pale comparison. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["analytical position comparison graphic"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 아래 조정과 위 정렬의 인과가 화면에서 판독되는지 확인
- 구조부재 강체 위치 조정만 표현가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
- layer.xray.7 · archi-shorts · still_pass · 지지 접촉을 보이는 스틸 PASS 후보, 프레임 내 위치 유지 검수 필요.
```text
[Xray] The outer walls of the foreground analytical support casing only turn to a faint translucent shell, keeping their exact shape and every window opening, while the structure inside — the source-verified jack contact and iron bearing — comes up solid and clearly lit behind them. The shell never disappears entirely and never distorts; nothing outside the foreground analytical support casing only changes.
```
원문 템플릿의 위치 매개변수만 치환했다.

### c12 · S05
- 낭독 · 모래를 채운 받침도 써서 밀리미터 단위로 자리를 맞췄어요.
- 편집 구간 · 35.81–39.58초
- 자료 유형 · analytical_model / 참조 R3
- 핵심 행동 · 비계 위 모래 받침과 기초 쪽 잭을 다른 위치에서 분리해 비교한다.
- 사실 고정점 · 모래 받침은 임시 비계 측 / 잭은 기초 조정 상세와 구분

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Create an explicitly analytical view separating two temporary alignment aids in one spatially readable composition. On viewer-left, show the hydraulic jack associated with the tower footing in its supported contact position. On viewer-right, show a sandbox arrangement at the top or bearing zone of a temporary timber scaffold as verified by the construction reference. Keep these two locations distinct, with each device visibly touching the element it supports. The wooden scaffold must not become a fifth iron tower leg, and the sandbox must not be portrayed as a permanent foundation or a modern concrete pedestal. Fine sand and rough timber distinguish it from the metal hydraulic device. Camera: 60mm near-orthographic comparative detail. Light: upper-left diffuse daylight. Palette: tan sand / warm timber / dark iron.

Camera and lighting specification for this still: 60mm near-orthographic comparative detail. Lighting direction and quality: upper-left diffuse daylight. Colour palette: tan sand / warm timber / dark iron. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 모래 받침은 임시 비계 측가 화면에서 판독되는지 확인
- 잭은 기초 조정 상세와 구분가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
- layer.loadpath.10 · archi-shorts · observed · 모래 받침을 통과하는 임시 지지 경로를 보이는 observed 시험 후보. 영상 PASS로 간주하지 않음.
```text
[LoadPath] A warm glow travels down through the structure along the line the weight actually takes: it appears first at the temporarily supported girder, runs down through the temporary timber scaffold supports in sequence, and gathers at the scaffold bearing base where it holds. Only the members carrying the load light up, one after another in that order, each brightening as the glow reaches it and dimming behind it; members that carry nothing stay dark. The building itself does not move, deform or change shape at any point.
```
원문 템플릿의 위치 매개변수만 치환했다.

### c13 · S06
- 낭독 · 그렇게 공중에서 큰 들보들이 서로 맞물렸습니다.
- 편집 구간 · 39.58–42.58초
- 자료 유형 · reconstruction / 참조 R2
- 핵심 행동 · 판과 단부가 제 위치에 맞춰진 기계적 접합을 보여준다.
- 사실 고정점 · 접합 형상은 기록자료 의존 / 현대 용접부나 완벽한 매끈 금속 금지

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Show a first-level girder joint at the moment its plates have reached the required mating position. Matching iron edges align cleanly, and real rivet holes or connection plates from the supplied construction detail establish how the parts belong together. Keep the interface visibly mechanical, not welded, melted or magically fused. A trace of open sky may remain outside the actual contact plane, allowing this shot to celebrate alignment without prematurely repeating the final gap-closing composition. The surrounding iron lattice remains rigid and continuous back to the supports. Historic timber staging appears only in the lower background and does not obscure the meeting faces. Camera: 75mm three-quarter junction close-up. Light: warm daylight from upper-left. Palette: brown iron / golden edge highlights / subdued blue.

Camera and lighting specification for this still: 75mm three-quarter junction close-up. Lighting direction and quality: warm daylight from upper-left. Colour palette: brown iron / golden edge highlights / subdued blue. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 접합 형상은 기록자료 의존가 화면에서 판독되는지 확인
- 현대 용접부나 완벽한 매끈 금속 금지가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c14 · S07
- 낭독 · 그럼 지금도 에펠탑 네 다리가 그 장치에 올라타 있을까요?
- 편집 구간 · 42.58–46.07초
- 자료 유형 · analytical_model / 참조 R3
- 핵심 행동 · 임시 잭과 지지 접촉 상세를 열어 장치의 존치 여부를 묻는다.
- 사실 고정점 · 장치 존치 여부를 묻는 공사 단계 / 오늘의 탑이 잭 위라는 오해 방지

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Return to the temporary footing adjustment detail through a new close sectional angle, not a modern tourist view. The temporary hydraulic jack remains visible in the construction-state version, nestled against its actual bearing surfaces. Beside that contact, leave enough clear space to anticipate the permanent bearing arrangement without drawing a second unsupported tower. Ground, footing and iron shoe remain in one believable scale relationship. A quiet empty recess or available working clearance carries the question of what remains when temporary adjustment equipment is removed. Do not imply that the tower has ever stood permanently on four active hydraulic pistons. Camera: 85mm low sectional view. Light: soft cross-light from frame-right. Palette: stone grey / warm dark iron / amber recess.

Camera and lighting specification for this still: 85mm low sectional view. Lighting direction and quality: soft cross-light from frame-right. Colour palette: stone grey / warm dark iron / amber recess. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 장치 존치 여부를 묻는 공사 단계가 화면에서 판독되는지 확인
- 오늘의 탑이 잭 위라는 오해 방지가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c15 · S07
- 낭독 · 높이를 맞춘 장치는 빼냈고, 그 자리에 쐐기를 끼웠습니다.
- 편집 구간 · 46.07–49.98초
- 자료 유형 · analytical_model / 참조 R3
- 핵심 행동 · 빈 잭 자리 대신 단단히 맞물린 쐐기 접촉을 드러낸다.
- 사실 고정점 · 임시 장치 제거 후 쐐기 지지 / 빈 접촉부나 공중부양 금지

#### A 프롬프트
```text
Vertical 9:16 documentary editorial reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Present the completed bearing contact after the temporary alignment device has been replaced by permanent wedges, using the supplied source detail as the authority for the arrangement. Show the wedge forms seated firmly between the intended bearing surfaces, with the iron support and foundation meeting through a clear uninterrupted load path. The former jack can appear only as a separate removed construction object in the distant lower edge, never still carrying the leg. Emphasise the tight interfaces and gravity-stable seating. Avoid inventing modern adjustment screws, polished stainless pistons or unsupported gaps beneath the iron shoe. The wedges are the discovery, and the view should feel satisfyingly solid. Camera: 90mm intimate bearing detail. Light: daylight from upper-left grazing wedge contact. Palette: warm grey metal / brown iron / neutral stone.

Camera and lighting specification for this still: 90mm intimate bearing detail. Lighting direction and quality: daylight from upper-left grazing wedge contact. Colour palette: warm grey metal / brown iron / neutral stone. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · slow controlled lateral dolly keeping the focal contact centred
- 움직이는 대상 · ["one restrained explanatory emphasis graphic, subject stays rigid"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 임시 장치 제거 후 쐐기 지지가 화면에서 판독되는지 확인
- 빈 접촉부나 공중부양 금지가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c16 · S08
- 낭독 · 다시 처음의 그 틈입니다. 양쪽이 맞닿는 순간,
- 편집 구간 · 49.98–53.64초
- 자료 유형 · analytical_model / 참조 R2
- 핵심 행동 · 첫 화면의 동일 시점에서 하늘 틈을 거의 닫힌 상태로 좁힌다.
- 사실 고정점 · 첫 화면과 동일한 카메라 잠금 / 간극 축소가 시점속임 아닌 정렬 결과

#### A 프롬프트
```text
Vertical 9:16 documentary analytical reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Recreate the exact camera geometry and framing of the opening image from the supplied first-level junction reference. The two enormous girder end faces occupy the left and right sides in the same scale, orientation and depth relationship. Their separation is now nearly closed through alignment, leaving only a very thin blue sliver at the centre. Keep the rivet pattern, surface marks and edge profile recognisably identical to the opening so the viewer knows this is its payoff. Do not alter the perspective to hide an unchanged gap. The correction is rigid positioning, not a transformation of the beams into a single melted object. Camera: same 100mm lens and orthogonal mating-plane angle as c01. Light: same upper-left edge daylight as c01. Palette: same charcoal iron / warm primer / blue slit.

Camera and lighting specification for this still: same 100mm lens and orthogonal mating-plane angle as c01. Lighting direction and quality: same upper-left edge daylight as c01. Colour palette: same charcoal iron / warm primer / blue slit. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · short straight push toward the joining seam, stopping before contact plane
- 움직이는 대상 · ["the source-verified rigid alignment position of the meeting faces"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · hold the source-verified focal relationship clearly visible

#### 수령 후 확인
- 첫 화면과 동일한 카메라 잠금가 화면에서 판독되는지 확인
- 간극 축소가 시점속임 아닌 정렬 결과가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인
- 상부 접합부 간극의 전후는 실제 1887년 사진 그대로의 기록처럼 제시하지 않고 정렬 원리 분석 재현으로 구분한다.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c17 · S08
- 낭독 · 방금까지 두 쇳덩이 사이로 보이던 파란 하늘이 닫힙니다.
- 편집 구간 · 53.64–57.50초
- 자료 유형 · analytical_model / 참조 R2
- 핵심 행동 · 하늘 한 줄이 사라지고 금속 단부 사이의 가는 접합선만 남는다.
- 사실 고정점 · 하늘이 사라지는 곳은 접촉선만 / 철이 녹아붙거나 합체되는 모핑 금지

#### A 프롬프트
```text
Vertical 9:16 documentary analytical reconstruction, centred focal event and clean top and bottom caption safe zones. Match the supplied source reference before adding detail. No faces, readable lettering, captions, logos, watermarks or fake inscriptions. Preserve rigid iron geometry and source-verified proportions. Use the opening composition once more, now at the completed alignment state. The two mating iron faces meet on the central line, and the blue sliver that attracted attention at the beginning has disappeared at that interface. Preserve a fine believable seam, visible plate thickness and individual rivet construction; the members remain distinguishable solid objects despite being correctly joined. The surrounding sky stays blue beyond the structure, proving that only the local slit has closed rather than the whole environment becoming dark. No extra diagram, victory text or human reaction enters. Let the heavy, quiet contact line carry the resolution by itself. Camera: same 100mm framing as c01 and c16. Light: same directional daylight, contact seam darker. Palette: iron brown-black / blue beyond interface.

Camera and lighting specification for this still: same 100mm framing as c01 and c16. Lighting direction and quality: same directional daylight, contact seam darker. Colour palette: iron brown-black / blue beyond interface. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: No faces or crowds, no lettering or dimensional numerals, no modern antenna or completed upper tower, no welding, no stainless cylinders, no bending lattice, no floating footing, no invented undocumented joint geometry, no extra legs; no unsupported connections.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
Keep all geometry, action, construction stage and scale unchanged. Shift the camera only eight degrees around the same focal point and soften the same key light; do not change the side of the load or support.
```

#### 4초 영상 인계
- 카메라 · short straight push toward the joining seam, stopping before contact plane
- 움직이는 대상 · ["the source-verified rigid alignment position of the meeting faces"]
- 고정 대상 · ["all other iron members","foundation","timber scaffold","background"]
- 끝 상태 · the sky slit is closed locally and the fine contact seam remains

#### 수령 후 확인
- 하늘이 사라지는 곳은 접촉선만가 화면에서 판독되는지 확인
- 철이 녹아붙거나 합체되는 모핑 금지가 지켜지는지 확인
- 역사 복원/분석 도식 표시와 참고자료 대응을 확인
- 상부 접합부 간극의 전후는 실제 1887년 사진 그대로의 기록처럼 제시하지 않고 정렬 원리 분석 재현으로 구분한다.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.
