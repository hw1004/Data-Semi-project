# 통신데이터를 활용한 서비스 패턴 분석 및 광고 추천 시스템 프로젝트

- [통신데이터를 활용한 서비스 패턴 분석 및 광고 추천 시스템 프로젝트](#통신데이터를-활용한-서비스-패턴-분석-및-광고-추천-시스템-프로젝트)
  - [프로젝트 소개](#프로젝트-소개)
  - [프로젝트 관련 정보](#프로젝트-관련-정보)
  - [개발 환경](#개발-환경)
  - [진행 과정](#진행-과정)
    - [데이터 소개](#데이터-소개)
    - [데이터 전처리 \& 현황 분석 및 시각화](#데이터-전처리--현황-분석-및-시각화)
    - [추천 시스템](#추천-시스템)
    - [Django 웹 서비스 구현](#django-웹-서비스-구현)
  - [프로젝트 후기](#프로젝트-후기)


## 프로젝트 소개
> 이 프로젝트는 **추천 시스템** (정보 필터링 기술의 일종으로 특정 사용자가 관심을 가질만한 정보를 추천하는 시스템)을 기반으로 통신 데이터를 이용하여 광고 추천, 타겟 고객 추천, 광고 송출 플랫폼 추천 등의 서비스를 구현하는 것을 최종 목적으로 하였습니다. 
> 
> 또한, 최종적으로 만들어진 서비스를 Django를 이용해 웹사이트로 구현하는 과정까지 진행하였습니다.

<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/7b8949b6-1c2e-4820-84fe-07216d0611a2" width="100%">

## 프로젝트 관련 정보
|프로젝트 주제|문제해결 빅데이터 활용 프로젝트|
|---|---|
|팀 세부 주제|통신데이터를 활용한 서비스 패턴 분석 및 광고 추천 시스템 프로젝트|
|프로젝트 기간|2023.11.14 ~ 2023.12.04 (3주)|
|팀원 구성|최현민(조장), 정혜원(부조장), 김수연, 김현, 최수정|
|수상|최우수상|

## 개발 환경
|||
|---|---|
|Communication|<img src="https://play-lh.googleusercontent.com/Ob9Ys8yKMeyKzZvl3cB9JNSTui1lJwjSKD60IVYnlvU2DsahysGENJE-txiRIW9_72Vd=w240-h480-rw" height="50">   <img src="https://play-lh.googleusercontent.com/mzJpTCsTW_FuR6YqOPaLHrSEVCSJuXzCljdxnCKhVZMcu6EESZBQTCHxMh8slVtnKqo" height="50">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Google_Slides_2020_Logo.svg/1200px-Google_Slides_2020_Logo.svg.png" height="50">    <img src="https://play-lh.googleusercontent.com/emmbClh_hm0WpWZqJ0X59B8Pz1mKoB9HVLkYMktxhGE6_-30SdGoa-BmYW73RJ8MGZQ"  height="50">  <img src="https://play-lh.googleusercontent.com/t-juVwXA8lDAk8uQ2L6d6K83jpgQoqmK1icB_l9yvhIAQ2QT_1XbRwg5IpY08906qEw" height="50">|
|Program| <img src="https://play-lh.googleusercontent.com/37EzETO6gZyKmCg2kBIFX1e9gkubxZrVa5fHJ6yOaa7VvEShHjKv2RdtwnZt9Sk258s" height="50">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" height="50">  <img src="https://blog.kakaocdn.net/dn/erEbYY/btrJ3v9wo1K/kc08TL3Rgm67T4txIaZwvk/img.jpg" height="50">|
|Language|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png" height="50">    <img src="https://images.velog.io/images/gyuseok-dev/post/a4e75d99-1871-4c86-ab87-699e2f526916/HTML&CSS.png" height="70">|
|Packages & Libraries|<img src="https://rphabet.github.io/assets/images/Numpy/logo.png" height="50">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" height="50"> <img src="https://www.jumpingrivers.com/blog/customising-matplotlib/matplot_title_logo.png" height="50">   <img src="https://repository-images.githubusercontent.com/4704710/fd110d80-63d1-11eb-9ae4-de7c23c9dedc" height="50">    <img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcFXQFv%2FbtrIRGyVKoT%2FLaS6korks7rH0zmmoQ1Xk0%2Fimg.jpg" height="50">|
|Framework| <img src="https://velog.velcdn.com/images/guswlsdl0121/post/7f82de3b-c868-411a-87bb-56d8ec6acfd7/image.png" height="50">| 

## 진행 과정

### 데이터 소개
> 선정한 데이터: 서울 열린데이터 광장의 [서울 시민생활 데이터](https://data.seoul.go.kr/dataVisual/seoul/seoulLiving.do)
>
> 서울시와 SK텔레콤이 공공빅데이터와 통신데이터 가명결합을 통해 추정한 서울 행정동단위 성, 연령별 1인가구와 서울시민의 생활특성 정보
>
> 2022년 1월부터 2023년 9월까지 월별 데이터가 존재하며 그 중 2023년 1월부터 2023년 9월까지의 데이터만 사용하여 프로젝트를 진행함

|프로젝트에 사용한 피쳐|설명|
|---|---|
|자치구|25개 자치구|
|행정동|426개 행정동|
|성별|남, 여|
|연령대|20세부터 75세까지 5살 단위|
|총인구수|자치구, 행정동, 성별, 연령대에 따른 총인구수|
|서비스 사용일수|게임, 금융, 배달, 쇼핑, 동영상/방송 서비스에 대해서 최근 3개월의 월 평균 해당 서비스 사용일수(사용일수) / 유튜브, 넷플릭스에 대해서 최근 3개월의 월 평균 해당 서비스 사용일수(z-score)|

### 데이터 전처리 & 현황 분석 및 시각화
[데이터 전처리 및 시각화 코드 바로가기](https://github.com/hw1004/Machine-Learning-Semi-project/blob/main/project/%EC%A0%95%ED%98%9C%EC%9B%90_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%A0%84%EC%B2%98%EB%A6%AC_%EC%8B%9C%EA%B0%81%ED%99%94.ipynb)

- 2023년 1~9월까지 데이터를 1개의 파일로 종합
- 자치구, 성별, 연령대로 그룹화 진행 > 특성을 나타내는 최소단위로 지정
- 총 300개 단위(행정동 > 자치구 / 성별 > 남, 녀 / 연령대 > 10세 단위) 개인화
- 원 데이터 중 사용 피쳐 선정 및 추출(자치구, 성별, 연령대, 총인구수, 서비스 7개)
- 원 데이터 상 z-score(넷플릭스, 유튜브 서비스 사용일수)와 일단위의 나머지 서비스 사용일수 컬럼을 통일하기 위해 StandardScaler를 이용해서 정규화 실행
- 현황분석 및 시각화
  - **Bar Plot**: 자치구별 인구 총합
  - <img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/ec4c254c-c5d9-4655-9017-3bb0e2a4356a" width="400">
  - **Map**: 자치구별 평균 연령대
  - <img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/735bd662-7dda-482a-8033-36cadd3dbd51" width="400">
  - **Heatmap**: 연령대별 서비스 간의 상관관계 분석
  - <img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/896f9965-a1b1-4027-bf46-641cb07c1df4" width="400">
  - **Line graph**: 서비스별 시계열(월) 분석
  - <img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/6569a10e-dbdc-41f2-9268-0eb70ab1bb7b" width="400">
- 개인화 데이터 내 7개 서비스의 데이터 사용일수에 따른 가중치를 산정하여 Z-value 값에 가중치를 반영하여 최종 순위 산정
  - [가중치 코드 바로가기](https://github.com/hw1004/Machine-Learning-Semi-project/blob/main/project/%EA%B0%80%EC%A4%91%EC%B9%98.ipynb)
  - 가중치 = 새로 산출한 가중치(각 서비스의 해당 월 사용잀수/월별 총 평균(1~9월) 사용잀수) * 원래 구해 놓은 z-value


### 추천 시스템
[추천 시스템 코드 바로가기](https://github.com/hw1004/Machine-Learning-Semi-project/blob/main/project/%EC%A0%95%ED%98%9C%EC%9B%90_recommendation_system.ipynb)
> 1. **월별 서비스 트렌드 기반 추천 시스템**
> - 타겟 고객(자치구, 성별, 연령대) 정보 입력시 서비스 사용일수가 높은 순으로 고객별, 월별 맞춤형 서비스 광고 분야 추천
> - 가중치가 부여된 월별 서비스별 사용일수를 이용해 특정 자치구, 연령대, 성별의 고객이 가장 많이 사용하는 서비스 순으로 추천을 진행함
> 2. **서비스 사용일수에 따른 Top N recommendation 추천 시스템**
> - 특정 서비스 기업에서 광고를 진행할 때 타겟 고객 추천 및 해당 광고를 어떤 서비스 분야의 플랫폼에 송출하면 좋은지 추천
> - z-value로 처리된 서비스별 사용일수 데이터의 각 서비스 사용일수 컬럼을 기준으로 내림차순 정렬한 데이터프레임을 서비스별로 생성 (타겟 고객 선정)
> - 타겟 고객별로 선택한 서비스와 다른 서비스들 간의 상관계수를 구해서 특정 서비스의 광고를 송출할 타 서비스 플랫폼을 추천

### Django 웹 서비스 구현
[Django project 바로가기](https://github.com/hw1004/Machine-Learning-Semi-project/tree/main/Recommendation_System)

- 프로젝트 구조

```
├── README.md
├── .gitignore
│
└── Recommendation_System
        ├── manage.py
        ├── .gitignore
        ├── Recommendation_System
        │     ├── __init__.py
        │     ├── asgi.py
        │     ├── settings.py
        │     ├── urls.py
        │     └── wsgi.py
        ├── recommend
        │     ├── migrations
        │     ├── __init__.py
        │     ├── admin.py
        │     ├── apps.py
        │     ├── forms.py
        │     ├── models.py
        │     ├── tests.py
        │     ├── urls.py
        │     └── views.py
        ├── templates
        │     ├── data.html
        │     ├── index.html
        │     ├── service.html
        │     ├── service1.html
        │     └── service2.html
        └── static
              ├── css
              ├── image
              └── js
        
```

- 서비스 소개 페이지
  - 전체적인 서비스 소개
  - 각 서비스로 이어져 있는 버튼을 클릭하면 서비스로 바로 갈 수 있음

<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/c9e24df2-c106-46f8-97de-aad1ab0398ca" width="100%">

- 데이터 소개 및 현황 분석 페이지
  - 추천 서비스에 사용된 데이터 소개
  - 자치구 연령대별 인구 총합 그래프, 자치구 연령대별 남성 인구 총합 그래프, 자치구 연령대별 여성 인구 총합 그래프, 서비스별 상관관계 히트맵, 자치구별 평균연령 지도 시각화 등으로 현황 분석 결과를 보여줌

<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/ceef5aff-ac14-4c38-930e-5a61ea2f3c52" height="300">
<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/eb1c63c2-02b1-464b-9959-19ed6bfade95" height="300">
<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/e1f3947d-e4f8-47df-bee3-8941c4fae724" height="300">
<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/d8a75762-9f01-4f7d-ab33-d169b07fe1c9" height="300">

- 고객별 맞춤형 광고 알고리즘 서비스
  - 고객이 거주하는 자치구, 연령대, 성별 정보를 선택하면 광고 알고리즘에 보일 서비스를 우선순위에 따라 추천해주는 서비스
  - 2023년 1월부터 9월까지 해당 고객 군집의 서비스별 사용일수 추이 또한 그래프로 시각화하여 보여줌

<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/0e215ff6-4424-4514-bef2-1896646eec28" width="50%">

- 서비스별 타겟 고객 및 광고 송출 서비스 추천
  - 게임, 금융, 쇼핑, 동영상/방송, 유튜브, 넷플릭스, 배달 서비스의 7개의 서비스 중 선택한 서비스에 대해 해당 서비스의 이용수가 가장 많은 타겟 고객의 자치구, 연령대, 성별을 우선순위 순으로 정렬
  - 타겟 고객별로 선택한 서비스와 상관관계가 높은 순으로 맞춤형 광고 송출 대상 서비스를 추천하는 서비스

<img src="https://github.com/hw1004/Machine-Learning-Semi-project/assets/109745250/a27c896f-c001-4050-9620-34957fb569a1" width="50%">


## 프로젝트 후기
좋았던 점: 거의 모든 프로젝트 과정을 팀원들이 같이 해보고 회의를 자주 진행하는 방식으로 진행을 했는데 이러한 방식이 프로젝트의 전 과정을 이해하고 진행하는데 도움이 되었던 것 같습니다. 또한 회의를 통해서 각 파트의 부족한 부분들에 대한 피드백을 받아 더 완성도 있는 프로젝트를 만들 수 있었던 것 같습니다.

아쉬운 점: 아무래도 세미 프로젝트이다 보니 시간적인 제약이 있어서 시간/거리 관련 피처들을 추천 시스템에 적용하여 구현하지 못한 점이 아쉽습니다.

느낀점: 데이터와 관련하여 처음 해보는 팀 프로젝트라 부족한 점도 있겠지만 팀원분들과 협력하여 좋은 결과물을 만들어낸 것 같아서 뿌듯하고 이론으로 배웠던 내용들을 직접 데이터를 다루면서 적용해보니까 이해도 더 잘 되고 심화된 학습을 할 수 있었던 것 같습니다.
