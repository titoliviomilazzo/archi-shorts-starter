# s14-roma-trevi 상세 스틸 이미지 프롬프트

이 문서는 이미지 생성 전 검토용이다. 실제 자료 편집 컷에는 원본 이미지와 사용권이 필요하다. 역사 재현과 분석 모형은 기록사진으로 표시하지 않는다. 효과 후보는 기존 DB 문구를 그대로 가져온 별도 부록이며, 1+1 효과 구성이 미확정된 컷은 생성 승인 상태가 아니다.

## 복사형 프롬프트

### c01 · S01
- 낭독 · 트레비 분수, 이 이름들은 뭘까요?
- 편집 구간 · 0.00–2.43초
- 자료 유형 · source_edit / 참조 T1
- 핵심 행동 · 실제 제어실 벽의 배급 명단 부분을 첫 1초 보여준 뒤 트레비 전경으로 전환. 자료 확보 전에는 글자를 창작하지 않고 자료기반 도식으로 구분한다.
- 사실 고정점 · 실제 명단의 원문만 사용한다 / 가문 정체는 c09 전까지 화면에서 해설하지 않는다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

SOURCE OPTICS AND LIGHT ARE LOCKED: no new camera viewpoint, lens geometry or lighting may be synthesized. Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Tight evidence view of the actual historic water-allocation chart mounted inside the original arched Trevi service chamber. Use an authenticated photograph as the entire image source; retain its real names and spelling without redrawing characters. Retain the source camera optics, vanishing lines and actual light direction while cropping to the chart edge and a strip of wall. Leave one incomplete row just beyond the crop so the list feels unexplained, not like a fabricated treasure map. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용. Lighting direction and quality: Preserve the authenticated source image’s existing light direction and exposure. Do not relight or invent lamps.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 동일 인증 원본에서 더 넓거나 좁은 크롭만 비교한다. 원래 조명·시점·문자를 새로 생성하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용
- 움직이는 대상 · ["원본 위 편집 크롭 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c02의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 실제 명단의 원문만 사용한다인지 참조와 대조
- 가문 정체는 c09 전까지 화면에서 해설하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 명단 의문과 소원 풍경의 한 단서가 읽히는지 확인
- 원본 광학·광원·실제 문자와 재질을 보존했는지 소스와 대조

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c02 · S01
- 낭독 · 로마에 다시 오고 싶으면 여기서 동전을 던지라고 하죠.
- 편집 구간 · 2.43–5.73초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 등 뒤로 던진 동전이 수반으로 들어간다.
- 사실 고정점 · 귀환은 전설로 제시한다 / 동전은 중력에 따라 수반으로 떨어진다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A single unmarked coin has just left the hand of one distant visitor seen only from behind at the Trevi basin. Camera at shoulder level, 50 mm lens feel, with the coin sharp against turquoise water and the rear silhouette soft at the far left edge. Daylight comes from upper viewer-right. Frame the stone basin rim as an oblique foreground line and the falling water behind it; the visitor does not face the camera. The coin is small, gravity-bound and not suspended as a magical object. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 50mm 어깨높이, 물로 짧은 하강 추적. Lighting direction and quality:  Daylight comes from upper viewer-right.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 어깨높이, 물로 짧은 하강 추적
- 움직이는 대상 · ["동전이 수반으로 떨어짐","필요 시 화면 가장자리의 먼 뒤돌아선 실루엣 손만 동작"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상","분수·수반의 위치"]
- 끝 상태 · 다음 컷 c03의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 귀환은 전설로 제시한다인지 참조와 대조
- 동전은 중력에 따라 수반으로 떨어진다인지 확인
- 이 컷 하나만 무음으로 보아도 명단 의문과 소원 풍경의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c03 · S01
- 낭독 · 거대한 조각상 발밑으로 쏟아지는 물에 소원을 맡깁니다.
- 편집 구간 · 5.73–9.14초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 조각상과 쏟아지는 물, 바닥 동전을 한 프레임에 둔다.
- 사실 고정점 · 조각은 트레비 Oceanus 도상에 맞춘다 / 물은 실제 암석부에서 수반으로 떨어진다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Reference-matched Trevi Oceanus ensemble viewed from basin height with a 35 mm lens feel. The pale sculpted figure is high in the composition, while real water descends from its rockwork into the foreground basin. One coin rests below the clear surface at lower centre, visually subordinate to the stone and water. Warm daylight from upper-left separates limestone edges from deep crevices; turquoise reflected fill stays near the water. Hold the fountain geometry fixed and show only a believable splash at the rock ledge, not water flowing from arbitrary statue limbs. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 35mm 수반높이 저각, 바위 쪽 짧은 push-in. Lighting direction and quality:  Warm daylight from upper-left separates limestone edges from deep crevices; turquoise reflected fill stays near the water.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 살아있는 사람의 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지; 실제 석조 조각상의 얼굴과 도상은 참조대로 보존한다.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 35mm 수반높이 저각, 바위 쪽 짧은 push-in
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c04의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 조각은 트레비 Oceanus 도상에 맞춘다인지 참조와 대조
- 물은 실제 암석부에서 수반으로 떨어진다인지 확인
- 이 컷 하나만 무음으로 보아도 명단 의문과 소원 풍경의 한 단서가 읽히는지 확인
- 살아있는 사람 얼굴 금지 규칙 때문에 실제 석상 얼굴이 삭제되거나 변형되지 않았는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c04 · S02
- 낭독 · 그런데 이 물을 다루는 곳은 조각상 앞이 아닙니다.
- 편집 구간 · 9.14–12.08초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 조각상 앞에서 옆 골목으로 경로를 바꾼다.
- 사실 고정점 · 관리 입구는 옆 골목 경로다 / 정확한 미확보 실내 평면은 만들지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Oblique exterior view beside the Trevi facade where public fountain rockwork occupies viewer-left and the narrow adjacent service approach recedes toward viewer-right. Use a 28 mm lens feel with straight verticals, a wet stone edge low in the foreground, and the service approach as the new focal depth line. Side daylight from high right catches the wall corners. The composition implies a camera about to turn into the approach without cutting a fictional doorway through Oceanus or building an imaginary tunnel directly behind the sculpture. Match street proportions to an acquired reference. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 28mm 사선측면, 옆 골목으로 pan-right. Lighting direction and quality:  Side daylight from high right catches the wall corners.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 28mm 사선측면, 옆 골목으로 pan-right
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c05의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 관리 입구는 옆 골목 경로다인지 참조와 대조
- 정확한 미확보 실내 평면은 만들지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 관광 시야에서 옆문으로의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c05 · S02
- 낭독 · 옆 골목의 작은 나무문을 열고 들어가면,
- 편집 구간 · 12.08–14.61초
- 자료 유형 · source_edit / 참조 T1
- 핵심 행동 · AP 현장 자료에 부합하는 관리 공간 입구의 나무문.
- 사실 고정점 · 문 위치와 재료는 AP 영상/사진 참조로 고정한다 / 원 관리실과 현대 기계실을 구분한다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

Vertical 9:16 source-preserving evidence edit of an authenticated photograph showing the small wooden Trevi service door on the adjacent street. Keep the original camera perspective, focal-length appearance, vanishing lines, exposure pattern, light direction, wood boards, hinges and wall thickness. The door must stay in the exact open or closed state documented by that photograph. Reframe only with a crop or a modest two-dimensional editorial push toward the threshold; do not synthesize a half-open door, unseen room or new vantage point. Preserve any authentic source lettering without redrawing it, and add no names, signs, symbols or watermark. The photograph is the evidence and its architectural pixels remain unchanged. A different door state or view into the interior requires a separately declared reconstruction and verified references before generation. Leave subtitle space by crop only when the source permits it.

Camera and lighting specification for this still: 원본 광학·시점을 보존한 2D 크롭 또는 편집 push만 허용, 새로운 40mm 시점·dolly-in 생성 금지. Lighting direction and quality: Preserve the source photograph’s actual light direction, shadows and exposure; do not introduce a new light source.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 동일 인증 원본에서 더 넓거나 좁은 크롭만 비교한다. 원래 조명·시점·문자를 새로 생성하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 원본 광학·시점을 보존한 2D 크롭 또는 편집 push만 허용, 새로운 40mm 시점·dolly-in 생성 금지
- 움직이는 대상 · ["원본사진 위 2D 편집 크롭"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c06의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 문 위치와 재료는 AP 영상/사진 참조로 고정한다인지 참조와 대조
- 원 관리실과 현대 기계실을 구분한다인지 확인
- 이 컷 하나만 무음으로 보아도 관광 시야에서 옆문으로의 한 단서가 읽히는지 확인
- 소스와 동일한 문 개폐 상태이며 새로운 실내·시점·광원이 생성되지 않았는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c06 · S03
- 낭독 · 분수 소리 뒤에서 기계 돌아가는 소리가 들려요.
- 편집 구간 · 14.61–17.30초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 기계실 전경으로 전환. 음향이 분수 물소리에서 기계음으로 바뀐다.
- 사실 고정점 · 현대 펌프실은 유지관리 설비 공간이다 / 연대 미상의 장치 디자인은 실물 참조를 우선한다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Modern Trevi water-management interior seen from the threshold, based on photographs of the contemporary chamber. Frame one reference-matched pump body in the near right foreground, connected pipework at middle depth and a lit control surface farther left. A 32 mm lens feel gives depth without stretching cylinders. Cool practical ceiling light from upper-right meets warmer reflected light from the doorway behind the camera. Capture a small patch of vibrating reflected water light on stationary metal; the room itself and equipment supports stay fixed. Conceal unreadable display details rather than fabricating them. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 32mm 문턱높이, 펌프 몸체로 slide-right. Lighting direction and quality:  Cool practical ceiling light from upper-right meets warmer reflected light from the doorway behind the camera.  Capture a small patch of vibrating reflected water light on stationary metal; the room itself and equipment supports stay fixed.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 32mm 문턱높이, 펌프 몸체로 slide-right
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c07의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 현대 펌프실은 유지관리 설비 공간이다인지 참조와 대조
- 연대 미상의 장치 디자인은 실물 참조를 우선한다인지 확인
- 이 컷 하나만 무음으로 보아도 현대 기계실로 예상 형성 후 옛 명단 제시의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c07 · S03
- 낭독 · 물탱크에 불 켜진 제어판, 분수를 돌보는 방인가 싶죠.
- 편집 구간 · 17.30–21.36초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 실제 현대 물탱크와 조작판의 참고자료 기반 도식.
- 사실 고정점 · 금속 탱크와 제어판은 현대 공간이다 / 화면 숫자와 제조사명을 임의 생성하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Close architectural equipment portrait of the modern chamber: metal water tanks and the illuminated control panel occupy separate planes, tanks at left and the panel at right. Use a 55 mm lens feel, camera at tank-flange height, and enough depth of field to read pipe connections without reading invented screen text. Upper-left ceiling illumination makes brushed steel and painted surfaces distinct. A single green status light can be present only if supported by the equipment reference. This must look like maintained modern infrastructure, not an alchemist laboratory or an ancient stone distribution room. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 55mm 탱크플랜지높이, panel로 rack-focus. Lighting direction and quality:  A single green status light can be present only if supported by the equipment reference.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 55mm 탱크플랜지높이, panel로 rack-focus
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c08의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 금속 탱크와 제어판은 현대 공간이다인지 참조와 대조
- 화면 숫자와 제조사명을 임의 생성하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 현대 기계실로 예상 형성 후 옛 명단 제시의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c08 · S03
- 낭독 · 그런데 벽에는 로마 가문들의 이름이 남아 있습니다.
- 편집 구간 · 21.36–24.53초
- 자료 유형 · source_edit / 참조 T1
- 핵심 행동 · 실제 자료가 확보된 명단 또는 출처 표기 도식. 허구 가문 이름 금지.
- 사실 고정점 · 명단은 원 관리실 벽의 실제 자료다 / 허구 가문/날짜/계좌를 추가하지 않는다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

SOURCE OPTICS AND LIGHT ARE LOCKED: no new camera viewpoint, lens geometry or lighting may be synthesized. Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Match the actual old arched chamber photograph and bring the historic wall chart into the near middle ground. Keep one portion of the rough arch overhead so viewers understand that the evidence belongs to the original chamber, distinct from the modern tanks. The original source camera perspective and existing illumination take priority over the desired crop; do not invent a diagonal vantage or upper-left light. Copy existing chart content only through source-preserving crop and perspective correction. Do not compose invented names, accounts, dates, seals or a chalk tally. The documentary image is the evidence, not a stylized replacement. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용. Lighting direction and quality: Preserve the authenticated source image’s existing light direction and exposure. Do not relight or invent lamps.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 동일 인증 원본에서 더 넓거나 좁은 크롭만 비교한다. 원래 조명·시점·문자를 새로 생성하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용
- 움직이는 대상 · ["원본 위 편집 크롭 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c09의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 명단은 원 관리실 벽의 실제 자료다인지 참조와 대조
- 허구 가문/날짜/계좌를 추가하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 현대 기계실로 예상 형성 후 옛 명단 제시의 한 단서가 읽히는지 확인
- 원본 광학·광원·실제 문자와 재질을 보존했는지 소스와 대조

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c09 · S04
- 낭독 · 옛날 이곳에서 집으로 물을 받던 귀족 가문들입니다.
- 편집 구간 · 24.53–27.68초
- 자료 유형 · analytical_model / 참조 T1
- 핵심 행동 · 옛 공급분배 도식에서 해당 가문 가정으로 물길이 갈라진다.
- 사실 고정점 · 명단의 가정들은 옛 수혜 가구다 / 익명 모델은 실제 지리·배관 상세로 주장하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A small three-dimensional tabletop explanatory model shows the old distribution chamber at rear centre and three generic house volumes in front, connected by separate water conduits. Camera is a 45-degree overhead 50 mm view with all branch junctions visible. Warm upper-right light picks out brass-like pipe surfaces and pale stone house blocks; the background is charcoal. Water remains inside conduits and flows from one common supply toward the separate houses. These are anonymous diagram blocks, not reconstructions of named families or an asserted exact historic street layout. Keep one branch prominent to explain what the chart indexed. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 50mm 45도상부, 분기 노드를 따라 tilt-down. Lighting direction and quality:  Warm upper-right light picks out brass-like pipe surfaces and pale stone house blocks; the background is charcoal.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 45도상부, 분기 노드를 따라 tilt-down
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c10의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 명단의 가정들은 옛 수혜 가구다인지 참조와 대조
- 익명 모델은 실제 지리·배관 상세로 주장하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 명단을 가정 물 공급·단수로 해석의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c10 · S04
- 낭독 · 그 집들이 물값을 밀리면, 공급을 끊었습니다.
- 편집 구간 · 27.68–30.98초
- 자료 유형 · analytical_model / 참조 T1
- 핵심 행동 · 미납 시 공급중단 원리 도식. 특정 가문이 실제 단수된 사건이나 연도를 창작하지 않는다.
- 사실 고정점 · 물값 연체 시 단수 원리는 확인된 사실이다 / 특정 가문 단수 사건은 창작하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Tight view of an explicitly explanatory water-distribution model, using one open branch and one isolated branch. Put the common feed at upper-left, the closed generic shutoff in the near centre and an anonymous house block at lower-right. A 75 mm macro lens feel and grazing upper-left light reveal metal edges and the separate wet and dry pipe sections. Show one static valve in a closed state, without implying that this is the actual documented valve design. The dry branch is the evidence of interrupted delivery; do not stage an invented eviction, named customer or dated enforcement event. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 75mm 근접, 폐쇄밸브로 낮은 slide. Lighting direction and quality:  A 75 mm macro lens feel and grazing upper-left light reveal metal edges and the separate wet and dry pipe sections.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 75mm 근접, 폐쇄밸브로 낮은 slide
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c11의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 물값 연체 시 단수 원리는 확인된 사실이다인지 참조와 대조
- 특정 가문 단수 사건은 창작하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 명단을 가정 물 공급·단수로 해석의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c11 · S05
- 낭독 · 동전 하나 던지며 돌아오길 빌던 분수의 뒤쪽에서,
- 편집 구간 · 30.98–34.10초
- 자료 유형 · analytical_model / 참조 T1
- 핵심 행동 · 수반의 동전과 뒤편 옛 분배 공간을 공간적으로 대비.
- 사실 고정점 · 소원과 물 공급을 개념상 대비한다 / 복합 절개는 실제 방 배치 실측으로 주장하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A coherent spatial sectional model contrasts the public basin at viewer-left with the old distribution chamber at viewer-right. The two zones are separated by their reference-derived masonry boundary and share no invented direct opening. Use a 35 mm elevated perspective, pale limestone, restrained blue water and amber side light from upper-right. One small coin rests in the public water while the old supply manifold is visible in the right zone. Make the model clearly an interpretive relationship diagram rather than an exact survey of undocumented room positions. Keep contemporary pump hardware out of this historical layer. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 35mm 모델 상부, 공적수반에서 옛방으로 pan. Lighting direction and quality:  Use a 35 mm elevated perspective, pale limestone, restrained blue water and amber side light from upper-right.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 35mm 모델 상부, 공적수반에서 옛방으로 pan
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c12의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 소원과 물 공급을 개념상 대비한다인지 참조와 대조
- 복합 절개는 실제 방 배치 실측으로 주장하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 소원과 공급 통제의 공간 대비의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c12 · S05
- 낭독 · 어느 집에 물을 보낼지, 어느 집은 끊을지를 가른 겁니다.
- 편집 구간 · 34.10–37.63초
- 자료 유형 · analytical_model / 참조 T1
- 핵심 행동 · 옛 관리 공간에서 여러 집으로 갈라진 공급 경로. 현재 가문에 단수하는 모습 금지.
- 사실 고정점 · 가정용 옛 분배와 현대 분수순환은 다르다 / 가상 밸브는 역사 유물 복제로 주장하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Close elevated view of an old water-allocation relationship model: a common conduit enters from rear-left and separates at one visible junction into several anonymous household branches. A generic shutoff isolates a single branch while the other branch remains water-filled. Camera is orthographic-like, 70 mm lens feel, with stable scale and no forced perspective. Warm light from upper-right makes the metal wetness legible against rough stone. Show the principle of selecting deliveries, not a claim about the precise recovered mechanism. Do not connect the branch to the present fountain recirculation pump or label a real family as delinquent. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 70mm 정투영에 가까운 상부, 분기노드로 push-in. Lighting direction and quality:  Warm light from upper-right makes the metal wetness legible against rough stone.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 70mm 정투영에 가까운 상부, 분기노드로 push-in
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c13의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 가정용 옛 분배와 현대 분수순환은 다르다인지 참조와 대조
- 가상 밸브는 역사 유물 복제로 주장하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 소원과 공급 통제의 공간 대비의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c13 · S05
- 낭독 · 고대 수도에서 온 물은 분수만 적신 게 아니었던 거죠.
- 편집 구간 · 37.63–40.99초
- 자료 유형 · analytical_model / 참조 T2
- 핵심 행동 · 고대 수도로 온 보충 공급선과 옛 가정용 공급 분기만 보여준다.
- 사실 고정점 · Aqua Virgo가 트레비에 물을 공급한다 / 가정배급은 역사적 용도로만 제시한다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. A longitudinal cutaway of the water-supply relationship shows Aqua Virgo entering the old city distribution area, with separate offshoots toward a fountain basin and anonymous household blocks. Keep source water and destination water at credible declining levels, with one visible inlet and no magical uphill flow. Use a 45 mm lens feel, camera above the channel wall, warm upper-left light and softly shaded stone. The image is a schematic architectural model without a geographic distance claim. Distinguish household distribution from a separate modern fountain loop; no return pipe from houses to the fountain is shown. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 45mm 수로벽위, 공급입구에서 분기쪽으로 track. Lighting direction and quality:  Use a 45 mm lens feel, camera above the channel wall, warm upper-left light and softly shaded stone.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 45mm 수로벽위, 공급입구에서 분기쪽으로 track
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c14의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- Aqua Virgo가 트레비에 물을 공급한다인지 참조와 대조
- 가정배급은 역사적 용도로만 제시한다인지 확인
- 이 컷 하나만 무음으로 보아도 소원과 공급 통제의 공간 대비의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c14 · S06
- 낭독 · 지금은 별도의 관리실에서 펌프 두 대가 돌아갑니다.
- 편집 구간 · 40.99–44.21초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 옛 원형 아치 관리 공간에서 현대 관리실로 명확히 장면 전환하고 실제 펌프 자료를 제시한다.
- 사실 고정점 · 현대 별도 관리실에 펌프 두 대를 제시한다 / 옛 배급 명단을 그 현대 방에 옮겨놓지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Modern chamber equipment is the new scene, clearly different from the old arched room. Two electric pump assemblies, and only two, occupy the middle of a reference-matched maintenance layout, with connected inlet and outlet pipes and fixed floor mounts. Camera is low at pipe-centre height, 35 mm lens feel; cool upper-right practical light reflects from maintained metal. Keep displays and manufacturer badges below readable resolution. Show the two pump bodies separated enough to count at phone size without adding decorative motors, turbine wheels, old brass household valves or a historic allocation chart in the same room. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 35mm 배관중심높이, 두펌프를 가로질러 slide. Lighting direction and quality:  Camera is low at pipe-centre height, 35 mm lens feel; cool upper-right practical light reflects from maintained metal.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 35mm 배관중심높이, 두펌프를 가로질러 slide
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c15의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 현대 별도 관리실에 펌프 두 대를 제시한다인지 참조와 대조
- 옛 배급 명단을 그 현대 방에 옮겨놓지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 현대 역할을 별도로 회수의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c15 · S06
- 낭독 · 분수로 떨어진 물을 다시 조각상 위로 올려보내요.
- 편집 구간 · 44.21–47.26초
- 자료 유형 · analytical_model / 참조 T3
- 핵심 행동 · 현재 분수 내 순환선은 옛 가정 공급선과 구분한 별도 화면.
- 사실 고정점 · 펌프는 수반의 물을 순환시킨다 / 가정용 옛 공급 분기를 순환 반환선으로 그리지 않는다 / 펌프 수 두 대는 근거가 있지만 두 펌프의 직렬/병렬 배치는 개수만으로 추정하지 않는다.

#### A 프롬프트
```text
Vertical 9:16 documentary analytical model of current Trevi recirculation, one centred flow relationship and a clean lower subtitle band. Water leaves the basin at lower-left and returns through a rising pipe toward the fountain outlets at upper-right, with hydraulic lift supplied by the source-confirmed electric pumps. Two pumps are documented, but their series or parallel arrangement must come from an acquired equipment reference; their number alone does not establish their plumbing. Until that reference is available, keep the individual connections abstract and show only the confirmed basin-to-outlet loop. Use a 50 mm three-quarter view, dark background, upper-left rim light and pale stone cut faces. Aqua Virgo replenishment enters as a visibly separate supply. No household destination or household return pipe belongs in this contemporary scene. All masonry and fixed equipment supports remain rigid. Do not invent readable labels, manufacturer badges, living human faces, unsupported pipes or a watermark. Mark the result as an explanatory model, not a measured historical survey.

Camera and lighting specification for this still: 50mm 모델3/4, 폐곡선 순환경로 따라 orbit. Lighting direction and quality:  Use a 50 mm three-quarter view, dark background, upper-left rim light and clear pale stone cut faces.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지; 두 펌프 개수만으로 직렬/병렬 배관을 추정해 그리지 않는다.
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 50mm 모델3/4, 폐곡선 순환경로 따라 orbit
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c16의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 펌프는 수반의 물을 순환시킨다인지 참조와 대조
- 가정용 옛 공급 분기를 순환 반환선으로 그리지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 현대 역할을 별도로 회수의 한 단서가 읽히는지 확인
- 두 펌프가 근거 없이 직렬 또는 병렬로 연결되지 않았는지 설비 원본과 대조한다.

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c16 · S07
- 낭독 · 같은 분수 앞입니다. 물은 아까처럼 쏟아집니다.
- 편집 구간 · 47.26–50.93초
- 자료 유형 · source_edit / 참조 T1
- 핵심 행동 · 첫 트레비 전경으로 복귀.
- 사실 고정점 · 첫 분수 사진과 같은 형상을 유지한다 / 해설선으로 외관이 실제 개조된 듯 보이지 않는다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

SOURCE OPTICS AND LIGHT ARE LOCKED: no new camera viewpoint, lens geometry or lighting may be synthesized. Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Return to the same verified fountain view established near the opening, preserving Oceanus, rockwork, basin outline and camera height. Use source-preserving crop and restrained exposure adjustment rather than replacing architecture. The broad cascade is central; the service doorway stays outside the frame so the public view seems unchanged. Keep the opening source photograph’s actual daylight direction, optical perspective and verticals; recreate the return with the same source crop only. The newly understood distribution history is carried by the edit and narration, not by extra fantasy pipes painted over the visible monument. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용. Lighting direction and quality: Preserve the authenticated source image’s existing light direction and exposure. Do not relight or invent lamps.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 동일 인증 원본에서 더 넓거나 좁은 크롭만 비교한다. 원래 조명·시점·문자를 새로 생성하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용
- 움직이는 대상 · ["원본 위 편집 크롭 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c17의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 첫 분수 사진과 같은 형상을 유지한다인지 참조와 대조
- 해설선으로 외관이 실제 개조된 듯 보이지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 명단의 의미를 알고 같은 분수·문서로 복귀의 한 단서가 읽히는지 확인
- 원본 광학·광원·실제 문자와 재질을 보존했는지 소스와 대조

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c17 · S07
- 낭독 · 수반의 동전은 사람들이 돌아오고 싶다는 마음을 남겼고,
- 편집 구간 · 50.93–54.35초
- 자료 유형 · reconstruction / 참조 T1
- 핵심 행동 · 동전 하나가 수반 바닥에 멈춘다.
- 사실 고정점 · 동전은 익명 소품이다 / 글자·인물 초상을 창작하지 않는다

#### A 프롬프트
```text
Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Extreme close view of one anonymous coin lying still on the real pale bottom of the Trevi basin, beneath clear rippling water. Camera looks down at a shallow diagonal, 85 mm macro lens feel, with a small focal zone around the metal rim and water caustics stretching toward upper-left. High left daylight makes real optical refraction visible without enlarging the coin beyond believable scale. Leave the surrounding basin empty of identifiable faces and clutter. Do not render a fabricated inscription or commemorative portrait; the coin reads through shape, worn edge and metallic colour alone. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 85mm 물속 동전사선접사, 잔잔한 lateral slide. Lighting direction and quality:  High left daylight makes real optical refraction visible without enlarging the coin beyond believable scale.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 A의 물체·비례·접촉을 고정하고 카메라를 옆으로 약 15도 이동하거나 key light를 반대 상부로 옮긴다. 두 변화는 함께 적용하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 85mm 물속 동전사선접사, 잔잔한 lateral slide
- 움직이는 대상 · ["물의 흐름 또는 실제 반사 하이라이트"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 c18의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 동전은 익명 소품이다인지 참조와 대조
- 글자·인물 초상을 창작하지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 명단의 의미를 알고 같은 분수·문서로 복귀의 한 단서가 읽히는지 확인

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.

### c18 · S07
- 낭독 · 벽의 이름들은 누가 물을 받아 갔는지를 남겼습니다.
- 편집 구간 · 54.35–57.69초
- 자료 유형 · source_edit / 참조 T1
- 핵심 행동 · 첫 화면의 기록으로 복귀. 동전과 명단 두 이미지 중 마지막에는 실제 벽의 명단 한 장만 남긴다.
- 사실 고정점 · 첫 실제 명단과 동일한 자료를 회수한다 / 실제 이름에 취소선이나 금액을 덧쓰지 않는다

#### A 프롬프트
```text
SOURCE-EDIT ONLY. Attach the verified source photograph or document identified below. Preserve its original informational content and do not invent missing inscriptions, names or historical evidence. If the required source is absent, stop before generating a replacement.

SOURCE OPTICS AND LIGHT ARE LOCKED: no new camera viewpoint, lens geometry or lighting may be synthesized. Vertical 9:16 cinematic architectural evidence still, one centred focal action, reference-matched materials and scale, clean lower subtitle safe zone. Freeze one decisive instant; architecture remains solid and undistorted. Return to exactly the same authenticated wall-chart crop and perspective as the first evidence frame. Keep the real wall edge and real paper or painted-chart texture intact, now held long enough to be understood as a record of household water supply. The actual source lens perspective, light direction and edge shadows remain unchanged so the original mystery returns without synthetic relighting. Do not add a red cancellation mark, erase a real name, overlay a fictional payment amount or composite new text. End on this one documentary object; the fountain and coin should not reappear as a split-screen montage. No invented text, labels, living human faces or watermark. Use authenticated source material for evidence; clearly identify reconstructed or analytical imagery.

Camera and lighting specification for this still: 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용. Lighting direction and quality: Preserve the authenticated source image’s existing light direction and exposure. Do not relight or invent lamps.. Colour palette: 석회암 크림·물의 자연 청록 / 원관리실 따뜻한 석재 / 현대기계실 차가운 금속, 색으로 시대구분. Freeze the depicted event at its initial readable state; this request produces one still image. Keep geometry and period exactly as described. Exact captions, dates and analytical-state labels will be composited later.

Negative prompt: 허구 가문명·미납금액·취소선·날짜, 현물없는 밸브의 역사유물 주장, 두 관리실 혼합, 가정 반환수를 분수 순환으로 연결, 얼굴·시선정면인물·워터마크·가짜표지·번지는 문자 금지
```

#### B 구도·광원 변형
A의 피사체·시대·부재 수·하중 방향을 유지한다. 새 무대를 여는 컷은 A/B 두 후보를 비교하고, 같은 신의 연결 컷은 앞 컷 승인 이미지로 연결한다.
```text
B는 동일 인증 원본에서 더 넓거나 좁은 크롭만 비교한다. 원래 조명·시점·문자를 새로 생성하지 않는다.
```

#### 4초 영상 인계
- 카메라 · 인증 원본의 광학·소실점·카메라 높이를 보존한 크롭. 2D 편집 이동만 허용
- 움직이는 대상 · ["원본 위 편집 크롭 프레이밍"]
- 고정 대상 · ["건축 외형","석조 접촉부","기계 고정점","카메라 시점 간 동일한 기준형상"]
- 끝 상태 · 다음 컷 엔딩의 핵심 대상 위치와 시선 방향을 맞춰 컷한다. 건축이 모핑하며 이동하지 않는다.

#### 수령 후 확인
- 첫 실제 명단과 동일한 자료를 회수한다인지 참조와 대조
- 실제 이름에 취소선이나 금액을 덧쓰지 않는다인지 확인
- 이 컷 하나만 무음으로 보아도 명단의 의미를 알고 같은 분수·문서로 복귀의 한 단서가 읽히는지 확인
- 원본 광학·광원·실제 문자와 재질을 보존했는지 소스와 대조

#### DB 효과 후보
적합한 1+1 효과 조합 미확정. 부적합한 다른 건물·도로 전용 효과로 대체하지 않는다.
