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
2021년 6월 30일 기준으로 사망자 수/확진자 수의 비율을 계산하고, 해당 나라의 전체 인구 수를 곱하여 만일 그 국가의 모든 사람이 코로나에 확진되었을 시 사망할 수 있는 인구 수를 계산하고, 그 수치의 퍼센트대로 분배합니다.
(나라 별 백신 보유 현황을 알면 결과가 달라질 수 있지만, 자료를 찾을 수 없었습니다.)

위의 내용에 따라 분배할 경우, 아래와 같은 결과가 도출됩니다.
밑의 내용은 readability를 위해 상위 10개국만 프린트한 결과입니다. 전체 내용은 resources directory의 csv 파일들을 참고하실 수 있습니다.
```
     num_deaths  mortality_rate      perc  num_vaccine
CHN    65063406        0.045630  0.307874     307874.0
IND    18488452        0.013135  0.087486      87486.0
MEX    11720960        0.092506  0.055462      55462.0
IDN     7350825        0.026852  0.034783      34783.0
YEM     6486707        0.196676  0.030694      30694.0
EGY     6280743        0.057483  0.029720      29720.0
USA     5992646        0.017782  0.028357      28357.0
BRA     5984049        0.027920  0.028316      28316.0
PAK     5389277        0.023290  0.025502      25502.0
RUS     3540584        0.024401  0.016754      16754.0
```
백신 미분배 경우 3개월, 6개월, 12개월, 36개월 후:

```
------- 백신 미지급 3개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    0.095417              134305461  0.258495     258495.0
BRA   214326223                    0.270313               57935255  0.111507     111507.0
CHN  1425893464                    0.031973               45590082  0.087746      87746.0
IDN   273753191                    0.150599               41226961  0.079349      79349.0
YEM    32981641                    0.947166               31239078  0.060125      60125.0
MEX   126705138                    0.208051               26361178  0.050737      50737.0
EGY   109262178                    0.200813               21941280  0.042230      42230.0
NGA   213401323                    0.088849               18960529  0.036493      36493.0
PAK   231402116                    0.065284               15106858  0.029076      29076.0
DZA    44177969                    0.340092               15024555  0.028917      28917.0
------- 백신 미지급 6개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    0.457610              644115016  0.338194     338194.0
BRA   214326223                    1.000000              214326223  0.112532     112532.0
IDN   273753191                    0.645073              176590694  0.092719      92719.0
MEX   126705138                    0.725322               91902058  0.048253      48253.0
EGY   109262178                    0.769321               84057688  0.044135      44135.0
NGA   213401323                    0.393004               83867564  0.044035      44035.0
PAK   231402116                    0.240526               55658340  0.029224      29224.0
VNM    97468028                    0.554582               54053989  0.028381      28381.0
KEN    53005614                    0.959389               50853003  0.026700      26700.0
DZA    44177969                    1.000000               44177969  0.023196      23196.0
------- 백신 미지급 12개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    1.000000             1407563842  0.355778     355778.0
USA   336997624                    0.854625              288006759  0.072797      72797.0
IDN   273753191                    1.000000              273753191  0.069194      69194.0
PAK   231402116                    1.000000              231402116  0.058490      58490.0
BRA   214326223                    1.000000              214326223  0.054173      54173.0
NGA   213401323                    1.000000              213401323  0.053940      53940.0
MEX   126705138                    1.000000              126705138  0.032026      32026.0
EGY   109262178                    1.000000              109262178  0.027617      27617.0
VNM    97468028                    1.000000               97468028  0.024636      24636.0
COD    95894118                    1.000000               95894118  0.024238      24238.0
------- 백신 미지급 36개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                         1.0             1407563842  0.333061     333061.0
USA   336997624                         1.0              336997624  0.079741      79741.0
IDN   273753191                         1.0              273753191  0.064776      64776.0
PAK   231402116                         1.0              231402116  0.054755      54755.0
BRA   214326223                         1.0              214326223  0.050714      50714.0
NGA   213401323                         1.0              213401323  0.050496      50496.0
MEX   126705138                         1.0              126705138  0.029981      29981.0
EGY   109262178                         1.0              109262178  0.025854      25854.0
VNM    97468028                         1.0               97468028  0.023063      23063.0
COD    95894118                         1.0               95894118  0.022691      22691.0
```

위 결과대로 각 국에 백신을 분배할 경우, 3개월, 6개월, 12개월 후의 사망자 수는 아래와 같이 변화할 것 입니다.
```
------- 백신 지급 3개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    0.095417              134305275  0.258495     258495.0
BRA   214326223                    0.270313               57935235  0.111507     111507.0
CHN  1425893464                    0.031973               45590038  0.087746      87746.0
IDN   273753191                    0.150599               41227090  0.079349      79349.0
YEM    32981641                    0.947171               31239242  0.060126      60126.0
MEX   126705138                    0.208051               26361156  0.050737      50737.0
EGY   109262178                    0.200813               21941299  0.042230      42230.0
NGA   213401323                    0.088849               18960504  0.036493      36493.0
PAK   231402116                    0.065284               15106862  0.029076      29076.0
DZA    44177969                    0.340091               15024532  0.028917      28917.0
------- 백신 지급 6개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    0.457609              644113955  0.338194     338194.0
BRA   214326223                    1.000000              214326223  0.112533     112533.0
IDN   273753191                    0.645075              176591258  0.092720      92720.0
MEX   126705138                    0.725321               91901940  0.048253      48253.0
EGY   109262178                    0.769322               84057755  0.044135      44135.0
NGA   213401323                    0.393003               83867416  0.044035      44035.0
PAK   231402116                    0.240526               55658337  0.029224      29224.0
VNM    97468028                    0.554581               54053875  0.028381      28381.0
KEN    53005614                    0.959388               50852951  0.026700      26700.0
DZA    44177969                    1.000000               44177969  0.023196      23196.0
------- 백신 지급 12개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    1.000000             1407563842  0.355779     355779.0
USA   336997624                    0.854622              288005678  0.072797      72797.0
IDN   273753191                    1.000000              273753191  0.069194      69194.0
PAK   231402116                    1.000000              231402116  0.058490      58490.0
BRA   214326223                    1.000000              214326223  0.054174      54174.0
NGA   213401323                    1.000000              213401323  0.053940      53940.0
MEX   126705138                    1.000000              126705138  0.032026      32026.0
EGY   109262178                    1.000000              109262178  0.027617      27617.0
VNM    97468028                    1.000000               97468028  0.024636      24636.0
COD    95894118                    1.000000               95894118  0.024238      24238.0
------- 백신 지급 36개월 후 -------
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                         1.0             1407563842  0.333061     333061.0
USA   336997624                         1.0              336997624  0.079741      79741.0
IDN   273753191                         1.0              273753191  0.064776      64776.0
PAK   231402116                         1.0              231402116  0.054755      54755.0
BRA   214326223                         1.0              214326223  0.050714      50714.0
NGA   213401323                         1.0              213401323  0.050496      50496.0
MEX   126705138                         1.0              126705138  0.029981      29981.0
EGY   109262178                         1.0              109262178  0.025854      25854.0
VNM    97468028                         1.0               97468028  0.023063      23063.0
COD    95894118                         1.0               95894118  0.022691      22691.0
```

위의 통계에 따라 계산 해보면:
(백신 미지급 시 상위 10개국의 전체 사망자 수 - 백신 지급 시 상위 10개국의 전체 사망자 수)/백신 지급 시 

- 3개월 후 [%]: -0.00005370
- 6개월 후 [%]: -0.00012554
- 12개월 후 [%]: -0.00003488
- 36개월 후 [%]: 0.00005561

36개월 후 오히려 증가하는 추세는, 100만개의 백신으로 사망률에 critical한 변화를 주기가 어렵기 때문에 긴 시간이 지나면 몇몇 국가에선 결국엔 사망률이 1에 수렴하기 때문입니다.

만약 두 달 후에 백신을 받을 경우, 코로나로 인한 사망률 그래프의 기울기를 계산하여 2021년 8월 30일의 확진자 대비 사망자 수를 예측할 수 있었고, 그에 따른 백신 분배 통계가 달라진 것을 확인할 수 있었습니다.
```
     population  mortality_rates_prediction  num_deaths_prediction      perc  num_vaccine
IND  1407563842                    0.049885               70215663  0.213560     213560.0
CHN  1425893464                    0.038395               54746658  0.166511     166511.0
BRA   214326223                    0.140996               30219243  0.091911      91911.0
IDN   273753191                    0.085652               23447555  0.071315      71315.0
MEX   126705138                    0.145809               18474771  0.056191      56191.0
YEM    32981641                    0.535936               17676062  0.053762      53762.0
EGY   109262178                    0.125328               13693629  0.041649      41649.0
NGA   213401323                    0.048744               10401947  0.031637      31637.0
PAK   231402116                    0.042771                9897314  0.030103      30103.0
DZA    44177969                    0.172867                7636930  0.023228      23228.0
```

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
`python main.py`


## 출처
- owid-covid-data.json: https://github.com/owid/covid-19-data/tree/master/public/data
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8253654/
- https://factcheck.snu.ac.kr/facts/show?id=3493
- https://coronaboard.kr/
- https://coronavirus.jhu.edu/data/mortality