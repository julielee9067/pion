# pion

The time is 2021.06.30. COVID is still in a global pandemic state.
An anonymous billionaire has contacted Pion Corp.
"I have acquired 1 million doses of COVID vaccine.
I don't want to sell these.
I don't want to waste them either.
What would be the most effective way to distribute them? "

As a data scientist at Pion Corp, you are tasked with providing the best way to fulfill the client's needs.
The report will be titled, "The DATA SCIENTIFIC way of distributing COVID vaccine".

1. Please define the OBJECTIVE clearly. Why should the billionaire agree that this objective is important? Explain it with "first principle" thinking.
2. What should we do with the vaccine? What are the "action items" with What, When, Where.
3. What is the expected impact by #2:action on #1:Objective? e.g. "the rocket should go in orbit" (x). "the rocket will reach 1000km altitude at 130 sec, and 2000km at 170 sec, cruising at 8000km/h, with 33% fuel left."(o)
4. (extra credit:) If the billionaire does not have the vaccine now, but will receive it in 2 months (2021.08.31). How should the #2:action change? How can we know that your prediction is accurate?


## Report
코로나 백신을 가장 영향력있게 쓰는 방법은 코로나 감염자 수를 최소화 시키는 것 입니다.
백신을 맞는 이유는 코로나를 예방할 확률을 높이기 위해서이고, 코로나에 확진 되는 경로는 대부분 사람을 통해서 감염되니, 인구 밀도 대비 백신 접종자 인구가 가장 적은 곳 부터 백신을 분배하는 것이 코로나 확산을 최소화 시킬 수 있는 방법입니다.

첫번째로, 각 나라의 도시 별, 시간 별 코로나 확진자 수 통계 자료와 인구 밀도 대비 백신 미접종자 수를 찾고, 이에 따른 일별 백신 사용량을 예측합니다.
예측이 완료되면 해당 나라의 백신 보유량을 파악하고, 일 단위로 필요한 만큼 순서대로 분배합니다.
일 단위로 선택한 이유는, 2021년 6월 30일 기준, 전 세계적으로 코로나 백신 신규 접종자 수가 약 3800만 명인 것을 감안하여 현재 백신 100만개는 하루 안에 모두 소진할 수 있다고 생각했기 때문입니다. (출처: https://insfiler.com/detail/rt_corona19vacc_bycountry-0001)

위에 적은 기준에 따라 백신을 분배할 경우, 

만약 두 달 후에 백신을 받을 경우, 백신 미접종자 수의 증가율을 logarithmic graph의 기울기를 계산 하여 분배할 것 같습니다.


## 실행 방법
1. 데이터 베이스 설치
`docker-compose -f docker-compose-db.yml up -d`

## 출처
1. owid-covid-data.json: https://github.com/owid/covid-19-data/tree/master/public/data
flask-sqlacodegen --flask --outfile models.py postgresql://test:testpassword@0.0.0.0:5432/postgres