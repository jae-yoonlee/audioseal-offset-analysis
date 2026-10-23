# 참고문헌 최종 대조

확인일: 2026년 10월 23일. 서지 정보와 본문에서 인용한 방법의 대응을 공개 원문으로 확인했다. 인용 논문의 실험을 재현하거나 모든 후속 문헌을 망라한 검토는 아니다.

## [1] AudioSeal

[AudioSeal](https://proceedings.mlr.press/v235/san-roman24a.html)

6저자, ICML 2024, PMLR 235, 43180-43196 확인. 원 논문 3.5절은 검출, 위치 추정, 귀속을 구분하며 귀속에서 검출 샘플의 메시지를 집계한다.

## [2] WavMark

[WavMark](https://arxiv.org/abs/2308.12770v3)

6저자와 제목 확인. 최초 제출은 2023년이나 이번 인용은 2024년 v3로 고정했다. 3.3절 shift module과 5.4절 watermark locating이 시작 위치 문제를 다룬다.

## [3] SyncGuard

[SyncGuard](https://arxiv.org/abs/2508.17121v2)

5저자와 제목 확인. 2025년 v2를 인용한다. ECAI 2025 채택 표시도 있으나 확인하지 않은 학회 쪽수는 넣지 않았다. 임의 길이 음성의 동기화와 추출을 다룬다.

## [4] How Fragile Is Your Watermark?

[How Fragile Is Your Watermark?](https://arxiv.org/html/2608.16566v1)

Likhith Kumara, 2026년 v1 확인. 6절은 작은 이동으로 격자 고정형 메시지가 훼손될 수 있다고 쓰고, 품질 지표의 한계로 동기화 공격은 평가에서 제외한다. 본 현상의 최초 발견을 주장하지 않는다.

## [5] AudioSeal Issue #52

[AudioSeal Issue #52](https://github.com/facebookresearch/audioseal/issues/52)

게시자 royrs, 2024년 9월 26일 개설, 제목 확인. 검출은 유지되지만 잘린 입력의 메시지가 틀리는 사례가 있다. 논문이나 공식 성능 보장이 아닌 공개 사례 보고로 표시했다. 접근일은 2026년 10월 23일이다.

## [6] Asymmetric Phase Coding

[Asymmetric Phase Coding](https://arxiv.org/html/2605.07241v2)

4저자와 2026년 v2 확인. 4.6절은 정수 이동에 대한 디코더 탐색 복구를 보고하며 Ed25519 검증을 사용한다. 모델과 메시지 체계가 달라 본 결과와 같은 조건의 수치 비교를 하지 않는다.

## [7] XAttnMark

[XAttnMark](https://proceedings.mlr.press/v267/liu25ap.html)

5저자, ICML 2025, PMLR 267, 38987-39015 확인. 교차 주의와 부분 파라미터 공유로 메시지 검색과 검출 및 귀속을 개선한다.

## [8] No Time to Collapse

[No Time to Collapse](https://arxiv.org/html/2609.29737v1)

6저자와 2026년 v1 확인. 고정된 워터마커의 시간별 출력을 학습한 Conformer 복호기로 집계한다. 한계 절에서 AudioSeal과 WavMark의 시간 변형 및 블라인드 위상 복원을 입증하지 않는다고 명시한다.

## [9] VCTK 0.92

[VCTK 0.92](https://doi.org/10.7488/ds/2645)

Junichi Yamagishi, Christophe Veaux, Kirsten MacDonald, 2019년, 버전 0.92, DOI와 Edinburgh CSTR 발행 정보를 확인했다. 실험에서 사용한 mic2 발화 목록은 원격 manifest가 추가로 필요하다.

## 수정한 표기

- WavMark는 인용 버전을 v3로 고정하고 해당 연도 2024를 사용했다.
- arXiv 논문은 v1 또는 v2를 명시했다. 학회 정식 쪽수를 확인하지 않은 논문은 arXiv로 남겼다.
- GitHub 이슈의 게시자와 최초 연도, 현재 접근일을 명시했다.
- VCTK의 발행처를 원 DOI 레코드의 University of Edinburgh, CSTR로 맞췄다.

## 주장 범위

미세 이동 현상과 정렬 탐색 자체는 선행연구가 있다. 본 원고의 분석 대상은 이 구현과 자료에서 검출 통과 오답, 비트별 출력 크기, 후보 선택에 따른 정답 손실이다. 조건부 탐색은 사후 개발 규칙이며 독립 검증된 새 방어로 제시하지 않는다.