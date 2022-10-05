# pion


## Task
The time is 2021.06.30. COVID is still in a global pandemic state.
An anonymous billionaire has contacted Pion Corp.
"I have acquired 1 million doses of COVID vaccine.
I don't want to sell these.
I don't want to waste them either.
What would be the most effective way to distribute them?"

As a data scientist at Pion Corp, you are tasked with providing the best way to fulfill the client's needs.
The report will be titled, "The DATA SCIENTIFIC way of distributing COVID vaccine".

1. Please define the OBJECTIVE clearly. Why should the billionaire agree that this objective is important? Explain it with "first principle" thinking.
2. What should we do with the vaccine? What are the "action items" with What, When, Where.
3. What is the expected impact by #2:action on #1:Objective? e.g. "the rocket should go in orbit" (x). "the rocket will reach 1000km altitude at 130 sec, and 2000km at 170 sec, cruising at 8000km/h, with 33% fuel left."(o)
4. (extra credit:) If the billionaire does not have the vaccine now, but will receive it in 2 months (2021.08.31). How should the #2:action change? How can we know that your prediction is accurate?


## Report
코로나 백신을 가장 영향력있게 쓰는 방법은 코로나로 인한 사망자 수를 최소화 시키는 것 입니다.
코로나 바이러스로 인한 사망자 수는 2021년 6월 30일부로 50만 명을 넘어섰으며, 사망률은 많게는 10% 까지 치솟았습니다.
백신을 맞는 근본적인 이유는 코로나를 예방하기 위해서이고, 이로 인한 사망자 수를 줄이는 것이 현재로썬 가장 긴급한 사안이라고 생각합니다.

첫번째로 각 나라 별, 날짜 별 코로나 확진자 수와, 코로나로 인한 사망자 수를 찾고, 수치를 그래프화 하여 나라 별 통계를 확인합니다.
2021년 6월 30일 기준으로 사망자 수/확진자 수의 비율을 계산하고, 해당 나라의 전체 인구 수를 곱하여 만일 그 국가의 모든 사람이 코로나에 확진되었을 시 사망할 수 있는 인구 수를 계산하고, 그 수치가 가장 높은 국가 10곳에 퍼센트대로 분배합니다.
(나라 별 백신 보유 현황을 알면 결과가 달라질 수 있지만, 자료를 찾을 수 없었습니다.)

위의 내용에 따라 분배할 경우, 아래와 같은 결과가 도출됩니다.
  country_code  mortality_rate      perc    num_vaccine
0          CHN    6.506341e+07  0.477363  477362.630077
1          IND    1.848845e+07  0.135648  135647.619690
2          MEX    1.172096e+07  0.085995   85995.320663
3          IDN    7.350826e+06  0.053932   53932.151724
4          YEM    6.486707e+06  0.047592   47592.214234
5          EGY    6.280744e+06  0.046081   46081.084663
6          USA    5.992646e+06  0.043967   43967.346365
7          BRA    5.984050e+06  0.043904   43904.275390
8          PAK    5.389277e+06  0.039541   39540.500584
9          RUS    3.540585e+06  0.025977   25976.856610



만약 두 달 후에 백신을 받을 경우, 코로나로 인한 사망률 그래프의 기울기를 계산하여 2021년 8월 30일의 확진자 대비 사망자 수를 예측할 수 있습니다.



## 과정
처음엔 단순히 인구 밀도와 확진자 수의 상관 관계가 있을 거라고 예상하고 관련된 데이터셋을 찾아보았습니다. 하지만, 직접 그려본 그래프와 연구 자료가 그 추론은 사실이 아니라는 것을 알려주었습니다.
그래서 두번째로, 나라 별 의료 침대 수(ICU beds per capita)와의 연관성을 분석해보았습니다. (의료 기관의 분포도가 코로나 확진세에 영향을 끼친다고 생각했기 때문) 
그러나 이 또한 연관이 없다는 것이 나타나, 근본적인 문제인 사망률을 지표로 삼기로 결정하였습니다.

## 실행 방법
1. 데이터 베이스 설치
`docker-compose -f docker-compose-db.yml up -d`

2. requirements 설지
`pip install -r requirements.txt`

3. 코드 실행
`python core/main.py`


## 출처
- owid-covid-data.json: https://github.com/owid/covid-19-data/tree/master/public/data
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8253654/
- https://factcheck.snu.ac.kr/facts/show?id=3493
- https://coronaboard.kr/
- https://coronavirus.jhu.edu/data/mortality