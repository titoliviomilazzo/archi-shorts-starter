# 건축 쇼츠 스타터 킷

archi-shorts 파이프라인 중 학생이 직접 쓰는 스크립트와 문서 템플릿만 모은 공개용 킷입니다.

## 폴더 구조

```
starter-kit/
  scripts/       실행 스크립트 + 의존 모듈
  templates/     대본·프롬프트·검수·게시 문서 템플릿 5종
  docs/          주차별 실습지·크레딧 장부
  media/         (직접 생성) 클립·오디오·렌더 결과물 — git에 올리지 않음
  episodes/      (직접 생성) ep.py init이 편별 폴더를 만드는 위치
```

## 필요 도구

- Python 3.11 이상
- ffmpeg (`ffmpeg`·`ffprobe` 명령이 PATH에 있어야 함)
- numpy (`build_captions.py`가 사용)
- 설치: `pip install numpy`

## 기본 명령

```
python scripts/ep.py init --episode <ep>
python scripts/rough_cut.py --episode <ep> --kit K1=c01-c03 --out media/<ep>/clips/rough.mp4
python scripts/build_srt.py --episode <ep>
```

`<ep>`는 편 폴더 이름입니다(예: `p01-my-topic`). 미디어 저장 위치는 기본값이 킷 폴더
안의 `media/`이며, `ARCHI_SHORTS_MEDIA` 환경변수로 다른 경로를 지정할 수 있습니다.

## 라이선스

미정(오너 결정).
