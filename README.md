# 2020-1-OSS-5
Homepage : https://20-1-skku-oss.github.io/2020-1-OSS-5/
## 1. 팀원 소개
- 김희성 heesunkim010 (팀장)
- 신성국 davidshyn1
- 안정복 jb0307
- 이하은 HACore
- 유광호 605s

## 2. 프로젝트 소개
### word_cloud (https://github.com/amueller/word_cloud)

- 텍스트 내의 단어들을 중요도(문서 내 등장횟수)를 기준으로 구분하여 특정한 이미지 영역(mask) 내부에 시각화하는 프로젝트

![example][example]


![example1][example1]

## 3. 설치 방법

pip 사용 시, 다음 코드로 진행하시기 바랍니다.:

    pip install wordcloud

conda 사용 시, 'conda-forge'를 이용하여 설치하시기 바랍니다:

    conda install -c conda-forge wordcloud

#### 설치 시 주의사항

wordcloud은 `numpy`와 `pillow` 패키지를 사용하기 때문에, 사전에 설치해야 합니다.

wordcloud 수행 후 해당 이미지를 저장학 위해서는, `matplotlib` 패키지 또한 설치해야 합니다.

이용자의 파이썬 버전에 'wheel'이 없는 경우, 위의 해키지를 설치하기 위해서는 C 컴파일러가 셋업되어 있어야 합니다.
컴파일러를 설치하기 전, 파이썬 환경 및 개발 환경 등에 대한 내용으로 원 프로젝트에 이슈 등록하시길 바랍니다. 

## 3. 프로젝트 기여 방법
### word_cloud
-한글로 구현하는 기능 추가 

-정적페이지에 문서화 (활용 예제, 한글 예제 추가)

-새로운 ISSUE 검색, 새로운 기능 추가 생각 (글자 방향, 테마와 어울리는 단어)


[example]: https://github.com/amueller/word_cloud/blob/master/examples/alice.png
[example1]: https://github.com/amueller/word_cloud/raw/master/examples/constitution.png

