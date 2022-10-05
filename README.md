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
```
  country_code    num_deaths      perc    num_vaccine
0          CHN  6.506341e+07  0.477363  477362.630077
1          IND  1.848845e+07  0.135648  135647.619690
2          MEX  1.172096e+07  0.085995   85995.320663
3          IDN  7.350826e+06  0.053932   53932.151724
4          YEM  6.486707e+06  0.047592   47592.214234
5          EGY  6.280744e+06  0.046081   46081.084663
6          USA  5.992646e+06  0.043967   43967.346365
7          BRA  5.984050e+06  0.043904   43904.275390
8          PAK  5.389277e+06  0.039541   39540.500584
9          RUS  3.540585e+06  0.025977   25976.856610
```
백신 미분배 경우 3개월, 6개월, 12개월, 36개월 후:

```
------- 백신 미지급 3개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           1.277393e+08  0.323612  323611.743302
1          BRA           5.628240e+07  0.142585  142584.550833
2          CHN           4.452475e+07  0.112798  112797.992432
3          IDN           4.052316e+07  0.102660  102660.450993
4          YEM           3.030816e+07  0.076782   76782.002548
5          MEX           2.556216e+07  0.064759   64758.594195
6          EGY           2.183074e+07  0.055306   55305.509850
7          NGA           1.861366e+07  0.047155   47155.412351
8          PAK           1.471944e+07  0.037290   37289.889126
9          DZA           1.462627e+07  0.037054   37053.854369
------- 백신 미지급 6개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND            601227904.0  0.380226  380225.672512
1          BRA            260865104.0  0.164975  164975.060112
2          IDN            170426096.0  0.107780  107780.055673
3          YEM            128719928.0  0.081404   81404.440585
4          MEX             86062208.0  0.054427   54427.049538
5          EGY             82327804.0  0.052065   52065.355640
6          NGA             80896948.0  0.051160   51160.460539
7          DZA             68844480.0  0.043538   43538.296431
8          PAK             52889076.0  0.033448   33447.856224
9          KEN             48980088.0  0.030976   30975.752748
------- 백신 미지급 12개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           4.933845e+09  0.392990  392989.747494
1          BRA           2.097058e+09  0.167034  167034.482794
2          IDN           1.307148e+09  0.104117  104116.680098
3          YEM           9.798555e+08  0.078047   78047.277460
4          MEX           6.838895e+08  0.054473   54473.047778
5          NGA           6.253496e+08  0.049810   49810.230794
6          EGY           6.004303e+08  0.047825   47825.363162
7          DZA           5.470184e+08  0.043571   43571.009958
8          PAK           3.981491e+08  0.031713   31713.299707
9          KEN           3.818979e+08  0.030419   30418.860754
------- 백신 미지급 36개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           3.444526e+11  0.400269  400269.352007
1          BRA           1.437805e+11  0.167079  167079.399921
2          IDN           8.631100e+10  0.100297  100297.247266
3          YEM           6.312166e+10  0.073350   73350.192537
4          MEX           5.357781e+10  0.062260   62259.806069
5          NGA           4.161894e+10  0.048363   48363.067136
6          EGY           3.788803e+10  0.044028   44027.588408
7          DZA           3.634309e+10  0.042232   42232.298718
8          PAK           2.748589e+10  0.031940   31939.836312
9          USA           2.597250e+10  0.030181   30181.211624
```

위 결과대로 각 국에 백신을 분배할 경우, 3개월, 6개월, 12개월 후의 사망자 수는 아래와 같이 변화할 것 입니다.
```
------- 백신 지급 3개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           1.276334e+08  0.323823  323822.534523
1          BRA           5.624173e+07  0.142693  142692.605004
2          CHN           4.428582e+07  0.112359  112358.899813
3          IDN           4.048822e+07  0.102724  102723.888800
4          YEM           3.026807e+07  0.076794   76794.049467
5          MEX           2.550023e+07  0.064697   64697.417055
6          EGY           2.179730e+07  0.055303   55302.585089
7          NGA           1.861366e+07  0.047225   47225.274858
8          PAK           1.469140e+07  0.037274   37273.994351
9          DZA           1.462627e+07  0.037109   37108.751040
------- 백신 지급 6개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND            600798368.0  0.380289  380289.350901
1          BRA            260700512.0  0.165016  165016.474359
2          IDN            170292264.0  0.107790  107790.463472
3          YEM            128550488.0  0.081369   81369.032014
4          MEX             85812560.0  0.054317   54317.062895
5          EGY             82194160.0  0.052027   52026.712154
6          NGA             80896948.0  0.051206   51205.611539
7          DZA             68844480.0  0.043577   43576.720588
8          PAK             52775496.0  0.033405   33405.482082
9          KEN             48980088.0  0.031003   31003.089996
------- 백신 지급 12개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           4.930941e+09  0.393053  393052.648262
1          BRA           2.095951e+09  0.167071  167071.332767
2          IDN           1.306289e+09  0.104126  104126.205966
3          YEM           9.786584e+08  0.078010   78010.316054
4          MEX           6.822118e+08  0.054380   54380.114729
5          NGA           6.253496e+08  0.049848   49847.542916
6          EGY           5.995434e+08  0.047790   47790.493288
7          DZA           5.470184e+08  0.043604   43603.648370
8          PAK           3.973838e+08  0.031676   31676.050567
9          KEN           3.818979e+08  0.030442   30441.647082
------- 백신 지급 36개월 후 -------
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           3.442912e+11  0.400342  400341.823933
1          BRA           1.437193e+11  0.167117  167116.835870
2          IDN           8.626594e+10  0.100310  100310.048230
3          YEM           6.305095e+10  0.073316   73315.651746
4          MEX           5.348507e+10  0.062192   62192.448529
5          NGA           4.161894e+10  0.048395   48394.508057
6          EGY           3.783993e+10  0.044000   44000.280110
7          DZA           3.634309e+10  0.042260   42259.754015
8          PAK           2.744348e+10  0.031911   31911.284686
9          USA           2.593512e+10  0.030157   30157.364826
```

위의 통계에 따라 계산 해보면:
- 백신 배분 후 3개월 후 줄어드는 사망자: 0.1479%
- 백신 배분 후 6개월 후 줄어드는 사망자: 0.0882%
- 백신 배분 후 12개월 후 줄어드는 사망자: 0.0748%
- 백신 배분 후 36개월 후 줄어드는 사망자: 0.0649%


만약 두 달 후에 백신을 받을 경우, 코로나로 인한 사망률 그래프의 기울기를 계산하여 2021년 8월 30일의 확진자 대비 사망자 수를 예측할 수 있었고, 그에 따른 백신 분배 통계가 달라진 것을 확인할 수 있었습니다.
```
  country_code  num_deaths_prediction      perc    num_vaccine
0          IND           6.747814e+07  0.268655  268654.701241
1          CHN           5.421283e+07  0.215841  215840.723361
2          BRA           2.960011e+07  0.117849  117848.665874
3          IDN           2.321571e+07  0.092430   92430.078863
4          MEX           1.816538e+07  0.072323   72322.911126
5          YEM           1.729296e+07  0.068849   68849.478171
6          EGY           1.368742e+07  0.054495   54494.529827
7          NGA           1.028405e+07  0.040945   40944.500750
8          PAK           9.744822e+06  0.038798   38797.632654
9          DZA           7.489096e+06  0.029817   29816.778133
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
`python core/main.py`

- 만일 코드를 한 번 이상 실행하고 싶으실 경우, 데이터베이스를 truncate 하시거나 main.py의 db insert function들을 comment out 하시고 사용하시면 됩니다.

## 출처
- owid-covid-data.json: https://github.com/owid/covid-19-data/tree/master/public/data
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8253654/
- https://factcheck.snu.ac.kr/facts/show?id=3493
- https://coronaboard.kr/
- https://coronavirus.jhu.edu/data/mortality