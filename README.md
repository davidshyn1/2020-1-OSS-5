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

wordcloud 수행 후 해당 이미지를 저장하기 위해서는, `matplotlib` 패키지 또한 설치해야 합니다.

이용자의 파이썬 버전에 'wheel'이 없는 경우, 위의 해키지를 설치하기 위해서는 C 컴파일러가 셋업되어 있어야 합니다.
컴파일러를 설치하기 전, 파이썬 환경 및 개발 환경 등에 대한 내용으로 원 프로젝트에 이슈 등록하시길 바랍니다. 

## 4. 프로젝트 기여 방법
### 한글로 구현하는 기능 추가

Word Cloud 프로젝트는 긴 글(문장)을 tokenize 수행하여, 단어 등장 횟수에 따라 글자 크기를 조정하여 word cloud를 생성하도록 하는 프로젝트이기에,
각 언어의 특성에 따라 word cloud가 제대로 수행되지 않을 확률이 높다.
해당 [issue][issue1]에 의하면 영어 기반의 프로젝트이기에,
다양한 언어의 특성을 적절하게 반영하지 못하고 있으며 이에 따라 상당 부분 word cloud의 기본 수행능력이 발휘되지 않은 경우 간혹 발생한다.<br>
한글의 경우, 글자 font를 GmarketSansTTFLight.ttf로 수행하여 진행하면
다음 링크의 그림을 출력하게 된다.
![example2][example2] 

해당 링크를 통해 본 프로젝트의 문제가 드러난다.
한글의 문장 특성 중에 '조사'라는 품사는 항상 명사, 형용사, 부사뒤에 붙여서 사용된다는 특성이 있다.
그래서 한글 자연어처리 과정에서, 조사는 필히 앞에 붙여진 단어와 분리하여 처리되어야 한다.
하지만 단어 등장 빈도를 측정할 때, 조사를 포함한 하나의 어절로 구분하여 빈도를 측정하게 된다.
그렇게 되면, 위의 링크의 결과처럼 '소프트웨어는', '소프트웨어가'라는 두 어절은 사실상 같은 '소프트웨어' 단어를 표현한 것인데
따로 구분하여 처리된다.

이는 확실히, 본 코드에 한글NLP 기능이 없기 때문에 나타난 현상이라 볼 수 있다.
영어 NLP의 경우, 띄어쓰기를 기준으로, 단어가 구분되기 때문에 단어 구분에 있어서 어렵지 않게 처리할 수 있다.
하지만 한글의 단어구분은 띄어쓰기가 아니기 때문에, 한글 NLP 기능 구현 추가가 불가피하다.

본 팀원은 한글 NLP를 전문적으로 배우지 않았기 때문에, 외부 패키지를 활용하는 것이 불가피하다.
한글 NLP 패키지 중 [konlpy][konlpy]라는 패키지가 있다.
해당 패키지도 역시나 오픈소스프로젝트로 활발히 진행 중인 패키지나, 상당 부분 한글 NLP 기능을 구현할 만큼 유용한 패키지라고 판단하여,
해당 패키지를 활용하여 wordcloud 코드를 구현하기로 결정하였다.

### 정적페이지에 문서화 (활용 예제, 한글 예제 추가)



### 새로운 ISSUE 검색
한글 구현 프로젝트, 한글예제 활용하여 정적페이지 문서화 프로젝트 등 본 팀의 주요 프로젝트 뿐만 아니라, 원 프로젝트에서 고려하고 있는 이슈들을 검색하여, 해결할 수 있다고 판단되는 이슈들을 팀원들과 토론을 통해 결정하고 해결하는 활동 또한 진행하였다.

현재 [plural_issue][issue2]에 대해 활발히 토론이 진행 중이다.
해당 issue는 plural issue로 해당 wordcloud 코드는 복수로 표현된 단어들을 자동으로 단수로 변환하여 tokenize하는 기능이 설정되어 있는데,
's'로 끝나는 단어와 구분하지 못하여, 단어에서 's'가 삭제되는 버그가 발생된다는 문제의 내용이다.
예를 들어, 'virus'라는 영어단어는 's'로 끝나는데, 단수 자동변환 기능을 설정하면, 'viru'로 취급한다는 문제가 발생된다는 것이다.



[example]: https://github.com/amueller/word_cloud/blob/master/examples/alice.png
[example1]: https://github.com/amueller/word_cloud/raw/master/examples/constitution.png


[issue1]: https://github.com/amueller/word_cloud/issues/238
[example2]: https://github.com/davidshyn1/davidshyn1.github.io/blob/master/assets/img/word_cloud%ED%95%9C%EA%B8%80%EB%B2%84%EC%A0%84.png
[issue2]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/issues/2
[knolpy]: https://github.com/konlpy/konlpy