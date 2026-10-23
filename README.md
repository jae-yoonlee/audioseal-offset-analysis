# AudioSeal 시작 위치 변화 분석

음성의 앞부분을 조금 더 잘랐을 때 **워터마크 검출과 16비트 메시지 복원이 어떻게 달라지는지** 조사한 연구 자료입니다.

[출판용 원고 PDF](AudioSeal_paper.pdf) | [편집 가능한 HWP](AudioSeal_paper.hwp) | [평가 조건](protocol_summary.json) | [참고문헌 대조](reference_verification_ko.md)

## 핵심 결과

VCTK의 미사용 화자 10명에서 20발화를 선정했습니다. 앞 1초를 제거한 기준선과 15개 고정 추가 절단량을 평가했습니다. 아래의 300은 20발화에 15개 절단량을 적용한 관측 수이며 독립 음성 표본 300개를 뜻하지 않습니다.

| 방법 | 기준선 정확 복원 | 추가 절단 정확 복원 |
| --- | --- | --- |
| 단일 검사 | 20/20 | 9/300 |
| 320정렬 q 선택 | 12/20 | 166/300 |
| 320정렬 margin 선택 | 18/20 | 300/300 |

단일 검사에서 추가 절단 300조건 중 204조건은 검출을 통과했습니다. 그중 195조건은 메시지가 틀렸습니다. 전체 추가 절단 조건의 65.0%이고 화자 bootstrap 95% 구간은 59.0~71.0%입니다.

q는 검출 양성인 샘플의 비율입니다. margin은 비트별 시간 평균 logit 절댓값의 평균이며 교정된 정확 확률이 아닙니다. r=0 기준선도 앞 1초를 자른 입력입니다. 완전 무편집 입력의 보존 실험으로 읽으면 안 됩니다.

## 저장 결과 검산

Python 3.10 이상에서 다음을 실행합니다.

```sh
python -m pip install -r requirements-analysis.txt
python summarize_saved_results.py --input selected_results.csv --output computed
```

이 코드는 CSV의 복원 비트와 정답을 비교해 오류 수, 정확 복원, 파일 게이트를 검사하고 표 1과 표 3의 복원 건수를 다시 집계합니다. 검출 통과 오답의 화자 bootstrap 구간도 계산합니다. GPU나 AudioSeal 모델을 실행하지 않으며, 후보 선택 자체의 재추론 검증은 아닙니다.

## 자료 범위

- `selected_results.csv`: 저장된 선택 결과 6,400행과 평가용 삽입 메시지. 발화명은 VCTK 식별자입니다.
- `margin_gate_curve.csv`: 기존 저장 결과의 사후 문턱 분석입니다. 학습용 또는 독립 확인 자료가 아닙니다.
- `signed_profiles.csv`: 저장 후보의 상대 정렬에 따른 집계입니다.
- `figure1.png`, `figure2.png`: 원고에 사용한 두 그림입니다.
- `reproducibility_scope.md`: 현재 공개 범위와 서버에서 가져와야 할 자료를 구분합니다.

조건부 탐색 규칙은 같은 결과를 보고 만든 개발 가설입니다. 이를 독립 검증된 방어 성능으로 주장하지 않습니다. 등록 코드 수에 따른 오귀속 값은 가상의 균등 코드북을 가정한 계산이며 실제 서비스 인증 실패율이 아닙니다.

## 원 모델과 데이터

- [AudioSeal 공식 구현](https://github.com/facebookresearch/audioseal)
- [AudioSeal 원 논문](https://proceedings.mlr.press/v235/san-roman24a.html)
- [VCTK 0.92 원 배포처](https://doi.org/10.7488/ds/2645)

VCTK 원본 음성, 모델 가중치, 인증 정보는 포함하지 않았습니다. 데이터와 모델은 각각의 배포 조건을 따릅니다. 이 저장소는 Meta의 공식 프로젝트가 아닙니다. 자체 자료의 재사용 라이선스는 별도 명시 전까지 부여하지 않습니다.
