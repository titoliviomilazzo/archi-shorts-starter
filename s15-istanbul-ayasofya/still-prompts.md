# s15-istanbul-ayasofya 상세 스틸 이미지 프롬프트

이 문서는 이미지 생성 전 검토용이다. 실제 자료 편집 컷에는 원본 이미지와 사용권이 필요하다. 역사 재현과 분석 모형은 기록사진으로 표시하지 않는다. 효과 후보는 기존 DB 문구를 그대로 가져온 별도 부록이며, 1+1 효과 구성이 미확정된 컷은 생성 승인 상태가 아니다.

## 복사형 프롬프트

### c01 · S01
- 낭독 · 아야 소피아, 네모 위에 동그라미라니요?
- 편집 구간 · 0.00–2.63초
- 자료 유형 · source_edit / 참조 H2, H1
- 핵심 행동 · 금빛 돔 전경 위에 네모 외곽이 생기다 상단 윤곽에서 끊긴다.
- 사실 고정점 · 실제 현존 곡면은 처음부터 존재한다 / 사각 기둥배치와 원형 돔 기반을 혼동하지 않는다 / 도입과 c17/c18은 같은 HAGIA_MASTER_A 원본·정규화 크롭으로 연결한다.

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Vertical 9:16 source-preserving evidence edit of one authenticated Hagia Sophia interior photograph, designated HAGIA_MASTER_A. Select a source whose fixed crop contains the circular dome base, all four pendentive zones and sufficient pier context to understand the square below. The source itself supplies the camera perspective, lens appearance, existing light direction, mosaics and masonry proportions. Use exactly this source and normalized crop again for c17 and c18; no opening-only generated viewpoint is allowed. Let the luminous circular base attract attention first through its authentic contrast, without digitally erasing, darkening or blurring any corner surface. Preserve the image pixels, architectural geometry and historic ornament. Only a source-preserving crop and restrained global exposure adjustment are permitted. Do not synthesize a lamp, a new lens, missing masonry, living human faces, lettering or a watermark. Exact source acquisition and derivative rights are pending.

Camera and lighting specification for this still: HAGIA_MASTER_A 인증 원본의 고정 크롭·광학·시점을 보존한다. c17/c18과 같은 정규화크롭 사용. Lighting direction and quality: HAGIA_MASTER_A 원본 광원·그림자·노출을 보존하고 합성 재조명 금지. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
A/B는 같은 인증 원본의 고정 시점과 원래 빛을 유지한다. B는 더 넓은 크롭만 비교하며, 선택된 크롭을 c01/c17/c18 모두 동일하게 적용한다.
```

#### 4초 영상 인계
- 카메라 · HAGIA_MASTER_A 원본 위 2D 프레이밍만 허용, 동일 콜백 크롭을 유지
- 움직이는 대상 · ["원본 위 2D 편집 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c02의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 실제 현존 곡면은 처음부터 존재한다인지 참조와 대조
- 사각 기둥배치와 원형 돔 기반을 혼동하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 원형 천장에 시선 고정의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c02 · S01
- 낭독 · 이 천장의 둥근 테두리를 눈으로 한 바퀴 돌아보세요.
- 편집 구간 · 2.63–5.87초
- 자료 유형 · reconstruction / 참조 H1
- 핵심 행동 · 카메라 고정, 돔 아래 원형 테두리 위로 작은 빛 한 점이 돈다.
- 사실 고정점 · 돔 밑 원호와 창열은 참조와 일치한다 / 새 구조 링을 임의 추가하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A closer upward view follows one real arc of the dome-base circular ring, with the window line providing the viewer a scale anchor. Camera is tilted up with a 32 mm lens feel, ring centred and its curve disappearing beyond both side edges. Natural light from upper-right windows outlines the ring while lower masonry stays warm and shaded. Use the same reference-defined radius and window rhythm as the opening. Freeze a precise viewpoint that could later host a moving light cue; do not add glowing symbols or a second concentric structural ring. Stone thickness must remain visible rather than paper-thin. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 32mm 원호접사, ring을 따라 짧은 pan. Lighting direction and quality:  Natural light from upper-right windows outlines the ring while lower masonry stays warm and shaded.  Freeze a precise viewpoint that could later host a moving light cue; do not add glowing symbols or a second concentric structural ring.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 32mm 원호접사, ring을 따라 짧은 pan
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c03의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 돔 밑 원호와 창열은 참조와 일치한다인지 참조와 대조
- 새 구조 링을 임의 추가하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 원형 천장에 시선 고정의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c03 · S01
- 낭독 · 걸리는 데가 하나도 없죠. 그런데 바로 아래에는
- 편집 구간 · 5.87–9.33초
- 자료 유형 · reconstruction / 참조 H1
- 핵심 행동 · 빛이 출발점에 도착하고 시선은 수직 아래로 떨어진다.
- 사실 고정점 · 아치와 원호는 연속 구조다 / 빈 것처럼 보인다고 실제 구멍을 만들지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Frame the junction between the circular base above and a massive arch descending below it. Use a steep upward 28 mm view from just off the central axis, giving the ring upper-left and the arch leg lower-right. Daylight comes from upper-left clerestory openings and fades down the arch intrados. This composition takes the eye below the perfect circle without yet diagramming the solution. Preserve actual masonry continuity and perspective. Do not cut a literal gap through a pendentive or replace the corner with open sky; the supposed emptiness is an initial reading of the form, not a real loss of material. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 28mm 대각올려다보기, arch로 tilt-down. Lighting direction and quality:  Daylight comes from upper-left clerestory openings and fades down the arch intrados.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 28mm 대각올려다보기, arch로 tilt-down
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c04의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 아치와 원호는 연속 구조다인지 참조와 대조
- 빈 것처럼 보인다고 실제 구멍을 만들지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 원형 천장에 시선 고정의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c04 · S02
- 낭독 · 커다란 기둥 넷이 네모의 꼭짓점처럼 서 있습니다.
- 편집 구간 · 9.33–12.41초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 네 기둥 머리를 연결한 네모가 평면에 놓인다.
- 사실 고정점 · 중앙 코어의 대기둥은 네 개다 / 모델은 건물 전체가 완전한 정육면체라는 뜻이 아니다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A cutaway teaching model of Hagia Sophia isolates the four great piers and four arches around the central square, while the surrounding building remains as a low contextual shell. Use a 50 mm elevated view, clean section faces and warm upper-right studio light. Put all four pier heads at the corresponding corner positions of a single square footprint, with no central column. Keep the actual unequal building masses outside this simplified core rather than forcing the entire church into a cube. This still explains the support layout only; it must not suggest that four narrow freestanding poles directly carry the dome. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 50mm 코어모델45도, 네모평면으로 orbit. Lighting direction and quality:  Use a 50 mm elevated view, clean section faces and warm upper-right studio light.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 코어모델45도, 네모평면으로 orbit
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c05의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 중앙 코어의 대기둥은 네 개다인지 참조와 대조
- 모델은 건물 전체가 완전한 정육면체라는 뜻이 아니다인지 확인
- 이 컷 하나만 무음으로 보아도 네모·원 문제를 손에 잡히는 모형으로 전환의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c05 · S02
- 낭독 · 네모 안에 꼭 맞게 동전을 하나 놓으면 어떻게 될까요?
- 편집 구간 · 12.41–15.65초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 원형 동전이 네모 안에 수평으로 놓인다.
- 사실 고정점 · 비유 원은 네모 변 중점에 접한다 / 탁상 동전은 고대 시공 실험 실물로 주장하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. On a dark tabletop, a plain circular brass disc lies exactly inscribed within a square pale stone frame. Camera looks down at a 65-degree angle with a 70 mm lens feel, retaining slight depth so both objects look solid. Upper-left studio light produces one soft disc shadow and a narrow highlight on its rim. The circle touches the midpoint of each square side; the four corner spaces remain outside the disc. Keep the disc anonymous, without a currency portrait or text. This is a physical analogy for the geometric problem, not an object claimed to have been used by the original builders. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 70mm 탁상65도, 원의 접점으로 push-in. Lighting direction and quality:  Camera looks down at a 65-degree angle with a 70 mm lens feel, retaining slight depth so both objects look solid.  Upper-left studio light produces one soft disc shadow and a narrow highlight on its rim.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 70mm 탁상65도, 원의 접점으로 push-in
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c06의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 비유 원은 네모 변 중점에 접한다인지 참조와 대조
- 탁상 동전은 고대 시공 실험 실물로 주장하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 네모·원 문제를 손에 잡히는 모형으로 전환의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c06 · S02
- 낭독 · 동전이 아무리 커도 네 귀퉁이는 그대로 남죠.
- 편집 구간 · 15.65–18.36초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 동전 밖 네 귀퉁이만 색이 남는다.
- 사실 고정점 · 네 귀퉁이는 원 밖에 남는다 / 이 비유는 실제 건축의 결손을 뜻하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Move closer to the same tabletop square and disc, this time cropping to one triangular corner space while retaining enough of the circle to see its tangency. A 90 mm macro lens feel, camera nearly overhead, reveals a real empty tabletop patch between the square corner and round disc. Warm light from upper-right keeps both boundaries sharp and the other corners softly present at the frame edges. Do not fill the patch or add a freestanding triangle yet. The disc and square keep identical dimensions and positions to the prior still; no resizing trick should make the geometry seem solved. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 90mm 탁상접사, 빈 귀퉁이로 slide. Lighting direction and quality:  Warm light from upper-right keeps both boundaries sharp and the other corners softly present at the frame edges.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 90mm 탁상접사, 빈 귀퉁이로 slide
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c07의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 네 귀퉁이는 원 밖에 남는다인지 참조와 대조
- 이 비유는 실제 건축의 결손을 뜻하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 네모·원 문제를 손에 잡히는 모형으로 전환의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c07 · S03
- 낭독 · 여기도 아래에서 올려다보면 둥근 돔만 보입니다.
- 편집 구간 · 18.36–21.26초
- 자료 유형 · reconstruction / 참조 H1
- 핵심 행동 · 돔을 바로 아래에서 올려다본 구도로 돌아온다.
- 사실 고정점 · 실제 곡면을 지우지 않는다 / 내려다보는 모델과 올려다보는 실경을 구분한다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Return to a new, slightly off-centre upward viewpoint inside the real Hagia Sophia rather than reusing the initial camera position. A 24 mm rectilinear lens shows the dome ring as the dominant luminous shape, while the pendentive corners blend into the surrounding gold-toned surfaces. Natural light from high viewer-left windows creates bright ring edges and lower shadow. Keep every corner surface physically present. The selective framing explains why a casual visitor notices the circle first; no architectural feature is erased or hidden by artificial fog. Freeze the instant before the camera would lower toward a corner. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 24mm 중앙에서 살짝비킨 올려다보기, 코너로 pan. Lighting direction and quality: Return to a new, slightly off-centre upward viewpoint inside the real Hagia Sophia rather than reusing the initial camera position.  Natural light from high viewer-left windows creates bright ring edges and lower shadow.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 24mm 중앙에서 살짝비킨 올려다보기, 코너로 pan
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c08의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 실제 곡면을 지우지 않는다인지 참조와 대조
- 내려다보는 모델과 올려다보는 실경을 구분한다인지 확인
- 이 컷 하나만 무음으로 보아도 실제 건물로 돌아와 빈틈의 무게 문제 제기의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c08 · S03
- 낭독 · 저 빈 귀퉁이에 돔의 무게가 실리면 어떻게 될까요?
- 편집 구간 · 21.26–24.63초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 상부 무게와 아래 기둥머리만 보이고 연결 해법 전체는 아직 크롭 밖에 둔다
- 사실 고정점 · 곡면은 평판 받침이 아니다 / 인접 아치·대기둥과 접한다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, reference-matched scale, one clear focal question and a modest lower subtitle safe zone. Frame a tight view inside Hagia Sophia so the substantial circular dome-base mass occupies the upper portion and one massive pier head is visible at the lower edge. The camera looks steeply upward with a 50 mm lens feel; high viewer-right sidelight makes the upper masonry weight legible. Deliberately leave most of the intervening corner transition beyond the crop, preserving every real wall and arch outside the frame. This composition asks where the weight goes without yet revealing the full curved contact path explained in the next cut. Do not cut an actual hole, remove a pendentive, add a falling block or invent a crack. All masonry remains intact and stationary. No invented lettering, living human face or watermark.

Camera and lighting specification for this still: 50mm 급한 올려다보기, 상부 돔기반 무게와 아래 기둥머리만 프레이밍; 연결곡면 전체는 크롭 밖 유지. Lighting direction and quality: High viewer-right sidelight makes the upper masonry mass legible while preserving reference-matched shadows.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 급한 올려다보기, 상부 돔기반 무게와 아래 기둥머리만 프레이밍; 연결곡면 전체는 크롭 밖 유지
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c09의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 곡면은 평판 받침이 아니다인지 참조와 대조
- 인접 아치·대기둥과 접한다인지 확인
- 이 컷 하나만 무음으로 보아도 실제 건물로 돌아와 빈틈의 무게 문제 제기의 한 단서가 읽히는지 확인
- c09 전에는 전체 곡면 접촉경로가 읽히지 않으며, 실제구멍·삭제로 그 해법을 감추지 않았는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c09 · S04
- 낭독 · 빈틈인 줄 알았던 그 자리가, 이 거대한 돔을 받치고 있습니다.
- 편집 구간 · 24.63–28.58초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 동전 비유에서 빈 곳처럼 보였던 네 귀퉁이를 실제 곡면과 대응한다. 그 면이 돔에서 아치와 기둥으로 하중을 넘기는 연속 경로를 따라 빛난다.
- 사실 고정점 · 네모-원 전환은 구면삼각 곡면으로 이뤄진다 / 곡면 하부와 양측·상부 연결을 연속으로 고정한다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Reveal one intact pendentive as a solid spherical triangular surface between two great arches, joining a corner pier below to the circular dome-base arc above. The surrounding shell is cleanly sectioned, with the selected curved masonry in warm gold and adjacent members muted pale stone. Use a 45 mm elevated interior view, upper-left light grazing the compound curvature. Keep all contacts intact: the lower corner meets the pier zone, the sides meet the arches and the upper boundary follows the circular base. This is a still of the revealed support path, not a triangle magically changing shape or a detached wing. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 45mm 내부모델 고각, 코너를 따라 reveal orbit. Lighting direction and quality:  Use a 45 mm elevated interior view, upper-left light grazing the compound curvature.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 45mm 내부모델 고각, 코너를 따라 reveal orbit
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c10의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 네모-원 전환은 구면삼각 곡면으로 이뤄진다인지 참조와 대조
- 곡면 하부와 양측·상부 연결을 연속으로 고정한다인지 확인
- 이 컷 하나만 무음으로 보아도 빈틈이 받침으로 바뀌는 핵심 반전의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c10 · S04
- 낭독 · 두 아치 사이로 금빛 삼각형 하나가 휘어져 있죠.
- 편집 구간 · 28.58–31.67초
- 자료 유형 · reconstruction / 참조 H1
- 핵심 행동 · 아치 사이의 실제 삼각 곡면 하나만 금빛으로 드러난다.
- 사실 고정점 · 상변은 원호다 / 모자이크 세부는 실제사진 확보 전 창작하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Photoreal close architectural view of one authentic pendentive between its two bounding arches, using a reference-matched interior surface. Camera is low and tilted upward with a 50 mm lens feel so the triangular outline and inward-curving surface are both apparent. Warm reflected gold comes from high left daylight, with soft shadow along the intrados edges. Keep the upper boundary curved rather than straight, and preserve the full thickness where the surface joins the arch system. Do not invent a flat gold panel, an ornamental pennant or a floating triangular insert. Existing mosaic details must follow the acquired photograph. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 50mm 코너저각, 곡률이 읽히는 lateral slide. Lighting direction and quality:  Warm reflected gold comes from high left daylight, with soft shadow along the intrados edges.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 코너저각, 곡률이 읽히는 lateral slide
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c11의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 상변은 원호다인지 참조와 대조
- 모자이크 세부는 실제사진 확보 전 창작하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 빈틈이 받침으로 바뀌는 핵심 반전의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c11 · S05
- 낭독 · 뾰족한 끝은 아래로 내려와 기둥 머리에 닿고,
- 편집 구간 · 31.67–34.43초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 한 삼각형 아래 꼭짓점과 기둥 머리가 한 프레임에 잡힌다.
- 사실 고정점 · 아래 꼭짓점 영역은 대기둥·아치 접합부와 통한다 / 가느다란 핀 위에 얹힌 지지로 표현하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A close section through the bottom of one pendentive shows its narrowing lower portion merging into the massive pier-and-arch junction. Use a 75 mm lens feel, camera level with the pier head and looking slightly upward. Upper-right grazing light catches the raw masonry thickness at the cut face, while the intact outer surface remains warm and smooth. Make the load-bearing junction continuous, broad and physically credible; the lower vertex is not a needle balanced on a tiny column capital. Keep the dome base outside the crop except for a faint contextual arc, focusing only on how the curved corner meets support below. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 75mm 기둥머리높이, 접합면으로 push-in. Lighting direction and quality:  Use a 75 mm lens feel, camera level with the pier head and looking slightly upward.  Upper-right grazing light catches the raw masonry thickness at the cut face, while the intact outer surface remains warm and smooth.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 75mm 기둥머리높이, 접합면으로 push-in
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c12의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 아래 꼭짓점 영역은 대기둥·아치 접합부와 통한다인지 참조와 대조
- 가느다란 핀 위에 얹힌 지지로 표현하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 아래 꼭짓점·위 원호·비유 대응을 단계적으로 이해의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c12 · S05
- 낭독 · 위로 갈수록 부채처럼 넓어져 둥근 테두리를 만납니다.
- 편집 구간 · 34.43–37.75초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 같은 면의 윗변이 돔 밑 원호로 이어진다.
- 사실 고정점 · 상변은 돔 받침 원호로 연결된다 / 면은 안쪽으로 휘어진 곡률을 가진다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A complementary close view looks upward along the same pendentive toward its broad curved upper edge at the dome base. Use a 65 mm lens feel and daylight from high viewer-left, creating a long gentle highlight over the concave masonry. The upper boundary is a true circular arc continuous with its neighbours; the two side boundaries remain aligned with the adjacent arch curves. Show sufficient wall thickness at a small section edge to reject the impression of a thin decorative membrane. Do not flatten the curved triangle or enlarge the dome ring relative to the preceding teaching model. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 65mm 위쪽올려다보기, 상부 원호로 tilt-up. Lighting direction and quality:  Use a 65 mm lens feel and daylight from high viewer-left, creating a long gentle highlight over the concave masonry.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 65mm 위쪽올려다보기, 상부 원호로 tilt-up
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c13의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 상변은 돔 받침 원호로 연결된다인지 참조와 대조
- 면은 안쪽으로 휘어진 곡률을 가진다인지 확인
- 이 컷 하나만 무음으로 보아도 아래 꼭짓점·위 원호·비유 대응을 단계적으로 이해의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c13 · S05
- 낭독 · 아까 비어 보였던 귀퉁이가 바로 이 삼각형이에요.
- 편집 구간 · 37.75–40.83초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 동전 도형의 빈 귀퉁이와 건축물의 곡면이 대응한다.
- 사실 고정점 · 탁상과 건물모델은 기하 비유다 / 동전을 건축물로 물리적으로 변형하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A paired spatial analogy is staged as one coherent tabletop model rather than a divided graphic. In the foreground, the square frame and round disc expose one corner space; directly behind it, a matching-scale architectural corner model rises from that same corner position into a pendentive. Camera is 45 degrees above the table with a 50 mm lens feel and light from upper-right. The square footprint stays fixed while the three-dimensional corner surface becomes visible above it. Do not morph the coin into a building or imply a literal thin triangular plate supports the dome. Use physical depth and alignment to make the correspondence clear. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 50mm 탁상45도, 기하대응을 따라 track. Lighting direction and quality:  Camera is 45 degrees above the table with a 50 mm lens feel and light from upper-right.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 탁상45도, 기하대응을 따라 track
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c14의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 탁상과 건물모델은 기하 비유다인지 참조와 대조
- 동전을 건축물로 물리적으로 변형하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 아래 꼭짓점·위 원호·비유 대응을 단계적으로 이해의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c14 · S06
- 낭독 · 옆 기둥에도 하나, 건너편 두 기둥 위에도 하나씩.
- 편집 구간 · 40.83–44.08초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 나머지 세 곡면을 차례로 비춘다.
- 사실 고정점 · 주요 전환 곡면은 네 장이다 / 중앙의 다섯째 삼각면을 추가하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Elevated three-quarter teaching view of the four corner pendentives arranged around the central square. The near-left one is softly emphasized while the other three remain equally legible and fully present; their lower junctions align with the four pier locations. A 40 mm lens feel and upper-left key light reveal the repeated spherical curvature without hiding the back pair. Keep exactly four corner transition surfaces, no extra fifth triangle at the centre and no eight-petal flower. The surrounding arches remain as stable boundaries, not detached bands. Freeze one overview that supports sequential editorial emphasis in the later video. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 40mm 모델고각, 네 코너를 짧게 orbit. Lighting direction and quality:  A 40 mm lens feel and upper-left key light reveal the repeated spherical curvature without hiding the back pair.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 40mm 모델고각, 네 코너를 짧게 orbit
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c15의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 주요 전환 곡면은 네 장이다인지 참조와 대조
- 중앙의 다섯째 삼각면을 추가하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 네 곡면 전체와 하중 경로의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c15 · S06
- 낭독 · 네 장의 굽은 면이 만나 돔이 앉을 둥근 자리를 만듭니다.
- 편집 구간 · 44.08–47.50초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 네 곡면의 윗변이 돔 발치의 원을 완성한다.
- 사실 고정점 · 네 곡면 상변이 원형 기반을 만든다 / 중앙에 새 기둥이나 사각 평판을 넣지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Near-orthographic view from above the central model reveals how the four pendentives together terminate at a continuous circular base for the dome. The square pier layout remains visible below through a clearly declared cutaway, and a short upper dome segment establishes where the ring carries the shell. Use an 85 mm lens feel, minimal perspective distortion and a broad upper-right softbox. Warm masonry and dark voids separate the solid surfaces from the interior air. Do not fill the whole square with a flat slab, add a central compression pillar or make the four curved surfaces overlap one another. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 85mm 준정투영상부, 원형테두리로 pull-up. Lighting direction and quality: A broad upper-right softbox lights the analytical model, revealing the circular upper boundary and preserving shaded depth below.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 85mm 준정투영상부, 원형테두리로 pull-up
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c16의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 네 곡면 상변이 원형 기반을 만든다인지 참조와 대조
- 중앙에 새 기둥이나 사각 평판을 넣지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 네 곡면 전체와 하중 경로의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c16 · S06
- 낭독 · 아치와 기둥이 그 무게를 받아 아래로 넘겨줍니다.
- 편집 구간 · 47.50–50.29초
- 자료 유형 · analytical_model / 참조 H1
- 핵심 행동 · 한 장만 남겨 곡률을 조명하고 명칭은 후반 자막으로 고정한다.
- 사실 고정점 · 하중 경로는 실제 이어진 석조를 따른다 / 정량 구조해석 결과로 주장하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. One-quarter sectional model shows an unbroken structural sequence from the dome base at top through the curved corner and bounding arches to a great pier below. Camera at mid-height uses a 55 mm lens feel; high-left sidelight exposes the raw cut face and joins. A restrained warm highlight may follow only real load-carrying masonry, leaving the empty interior dark. The piers and arches remain massive and fixed. Do not draw a single unsupported vertical force line through empty air, animate masonry flexing, or present the simplified model as a quantitative engineering analysis. The image explains the load transfer relationship without claiming a numerical distribution. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 55mm 사분면중간높이, 연속하중경로 따라 tilt-down. Lighting direction and quality:  Camera at mid-height uses a 55 mm lens feel; high-left sidelight exposes the raw cut face and joins.  A restrained warm highlight may follow only real load-carrying masonry, leaving the empty interior dark.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 55mm 사분면중간높이, 연속하중경로 따라 tilt-down
- 움직이는 대상 · ["검증 전 해설 그래픽의 단계적 밝기 변화"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c17의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 하중 경로는 실제 이어진 석조를 따른다인지 참조와 대조
- 정량 구조해석 결과로 주장하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 네 곡면 전체와 하중 경로의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c17 · S07
- 낭독 · 아까는 둥근 테두리만 눈에 들어왔는데 말이죠.
- 편집 구간 · 50.29–53.09초
- 자료 유형 · source_edit / 참조 H2
- 핵심 행동 · 윤곽선과 보조 색을 지우고 실제 천장의 색으로 복귀한다.
- 사실 고정점 · 실제 사진의 장식과 형태를 보존한다 / 설명선을 제거하는 편집을 구조 파괴처럼 보이지 않게 한다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Vertical 9:16 source-preserving evidence edit using HAGIA_MASTER_A, the identical authenticated interior photograph and normalized crop selected for c01. Preserve its actual viewpoint, optical perspective, illumination, masonry and ornament without synthesizing a camera or light. The fixed crop includes the dome-base ring, all four pendentive zones and enough pier context to understand the square below. Remove only explanatory editing graphics used in the preceding model sequence; no physical wall or historic ornament is removed. Keep all existing mosaic, calligraphy and source detail intact. The quiet image allows the viewer to find the geometry unaided, with shape and authentic shadows providing the clues. Do not add construction outlines, highlight fills, replacement inscriptions or newly generated religious symbols. Only restrained global exposure adjustment and the selected common crop are permitted. No new living human face or watermark may enter. This photograph must share the same source file and crop coordinates with c01 and c18.

Camera and lighting specification for this still: 인증 원본 사진의 시점·렌즈·수직선 보존, 마지막 회수는 동일 원본 크롭으로 편집. Lighting direction and quality: Preserve the source photograph’s actual light direction, shadow structure and exposure; no synthetic relighting.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
A/B는 같은 인증 원본의 고정 시점과 원래 빛을 유지한다. B는 더 넓은 크롭만 비교하며, 선택된 크롭을 c01/c17/c18 모두 동일하게 적용한다.
```

#### 4초 영상 인계
- 카메라 · 인증 원본 사진의 시점·렌즈·수직선 보존, 마지막 회수는 동일 원본 크롭으로 편집
- 움직이는 대상 · ["원본 위 편집 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c18의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 실제 사진의 장식과 형태를 보존한다인지 참조와 대조
- 설명선을 제거하는 편집을 구조 파괴처럼 보이지 않게 한다인지 확인
- 이 컷 하나만 무음으로 보아도 윤곽선 없이 실제 천장에서 스스로 발견의 한 단서가 읽히는지 확인
- 원본 시점·빛·천장곡률을 보존하며 사진밖 새 장식을 생성하지 않았는지 확인
- c01과 같은 HAGIA_MASTER_A 원본 파일·정규화 크롭인지 비교한다.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c18 · S07
- 낭독 · 동그란 천장 네 귀퉁이에서 금빛 삼각형이 하나씩 펼쳐집니다.
- 편집 구간 · 53.09–57.35초
- 자료 유형 · source_edit / 참조 H2
- 핵심 행동 · 첫 화면 구도 그대로 네 귀퉁이를 알아볼 시간만 남긴다.
- 사실 고정점 · 첫 구도와 같은 현존 천장이다 / 마지막 펼쳐짐은 인식상의 드러남이며 물리적 전개가 아니다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Vertical 9:16 final source-preserving still from HAGIA_MASTER_A, matching the authenticated source file, normalized crop, dome-ring position and pier spacing used for c01 and c17. The four real curved triangular corner surfaces remain readable through their original shape, surface variation and shadows. Preserve the source photograph’s actual perspective, light direction, exposure pattern, mosaics and masonry proportions. No new geometric overlay appears. The concluding image is the intact building in the chosen photograph, understood differently after the preceding sequence. Masonry does not unfold, rotate, separate or become a floating exploded dome; the narration describes a perceptual discovery. Keep the shared fixed composition quiet enough for the viewer to recognise all four corners. Only the already chosen source crop and restrained global exposure correction are permitted. No new lettering, living human faces, symbols or watermark may be generated. Actual source acquisition and derivative reuse rights remain pending before this evidence edit can be produced.

Camera and lighting specification for this still: 인증 원본 사진의 시점·렌즈·수직선 보존, 마지막 회수는 동일 원본 크롭으로 편집. Lighting direction and quality: Preserve the source photograph’s actual light direction, shadow structure and exposure; no synthetic relighting.. Colour palette: 금빛과 따뜻한 석재 / 분석모델 차콜·창백한 돌, 새로운 네온색 과잉금지. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 곡면을 평판으로 치환, 다섯째 코너·중앙기둥·종이두께 돔, 석조 전개·실제 구멍·공중부유·금빛 삼각판, 임의모자이크·서예·살아있는 사람얼굴·워터마크·가짜치수 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
A/B는 같은 인증 원본의 고정 시점과 원래 빛을 유지한다. B는 더 넓은 크롭만 비교하며, 선택된 크롭을 c01/c17/c18 모두 동일하게 적용한다.
```

#### 4초 영상 인계
- 카메라 · 인증 원본 사진의 시점·렌즈·수직선 보존, 마지막 회수는 동일 원본 크롭으로 편집
- 움직이는 대상 · ["원본 위 편집 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 엔딩의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 첫 구도와 같은 현존 천장이다인지 참조와 대조
- 마지막 펼쳐짐은 인식상의 드러남이며 물리적 전개가 아니다인지 확인
- 이 컷 하나만 무음으로 보아도 윤곽선 없이 실제 천장에서 스스로 발견의 한 단서가 읽히는지 확인
- 원본 시점·빛·천장곡률을 보존하며 사진밖 새 장식을 생성하지 않았는지 확인
- c01과 같은 HAGIA_MASTER_A 원본 파일·정규화 크롭인지 비교한다.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.
