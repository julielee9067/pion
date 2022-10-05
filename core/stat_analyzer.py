from datetime import datetime, date
from itertools import islice
from typing import Dict

from pandas import DataFrame
from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData

import matplotlib

from core.utils import (
    plot_graph_with_polyfit_line,
    predict_trend,
    get_polyfit_line,
)

matplotlib.use("TkAgg")  # noqa

import matplotlib.pyplot as plt  # noqa


def get_dates_and_num_deaths() -> Dict:
    res = {}
    with Session(engine) as session:
        country_list = session.query(Country).join(CountryData).all()
        for country in country_list:
            dates = []
            num_deaths = []

            for data in country.country_datas:
                if data.expected_deaths:
                    num_deaths.append(data.expected_deaths)
                    dates.append(data.collected_date)

            if not num_deaths:  # Some total_deaths data were missing for a few countries
                continue

            res[country.country_code] = {"dates": dates, "num_deaths": num_deaths}

    return res


def get_num_deaths_by_date(date: datetime):
    res = dict()

    with Session(engine) as session:
        country_data_list = (
            session.query(CountryData)
            .filter(CountryData.collected_date == date)
            .join(Country)
            .all()
        )
        for data in country_data_list:
            if data.total_cases:
                res[data.country.country_code] = data.expected_deaths

    # Return in descending order with the highest num_deaths
    return dict(sorted(res.items(), key=lambda item: item[1], reverse=True))


def get_first_n_countries_stat(n: int = 10) -> DataFrame:
    num_deaths = get_num_deaths_by_date(date=datetime(2021, 6, 30))
    first_10_countries = list(islice(num_deaths.items(), n))
    p = DataFrame(first_10_countries, columns=["country_code", "num_deaths"])
    p["perc"] = p["num_deaths"] / p["num_deaths"].sum()
    p["num_vaccine"] = p["perc"] * 1000000

    return p


def plot_country_graph(country_code: str) -> None:
    res = get_dates_and_num_deaths()
    plot_graph_with_polyfit_line(
        x=res[country_code]["dates"],
        y=res[country_code]["num_deaths"],
        title=f"date_vs_num_deaths_{country_code}",
    )


def get_prediction_on_n_countries_stat_by_date(date: date, n: int = 10) -> DataFrame:
    res = get_dates_and_num_deaths()
    prediction_results = dict()

    for country_code, data in res.items():
        line = get_polyfit_line(x=data["dates"], y=data["num_deaths"])
        prediction_results[country_code] = predict_trend(input=date, polyfit_line=line)

    prediction_results = dict(
        sorted(prediction_results.items(), key=lambda item: item[1], reverse=True)
    )
    first_10_countries = list(islice(prediction_results.items(), n))

    p = DataFrame(first_10_countries, columns=["country_code", "num_deaths_prediction"])
    p["perc"] = p["num_deaths_prediction"] / p["num_deaths_prediction"].sum()
    p["num_vaccine"] = p["perc"] * 1000000

    return p


def insert_new_pred_stat(date: date = datetime(2021, 7, 1)) -> None:
    pred = (
        get_prediction_on_n_countries_stat_by_date(date=date).set_index("country_code").T.to_dict()
    )
    new_stat_list = []
    with Session(engine) as session:
        for country_code, data in pred.items():
            country = session.query(Country).filter(Country.country_code == country_code).first()
            new_data = dict(
                collected_date=date,
                expected_deaths=data["num_deaths_prediction"] - data["num_vaccine"],
                country_id=country.country_id,
            )
            new_stat_list.append(new_data)

        session.bulk_insert_mappings(CountryData, new_stat_list)
        session.commit()

    print(f"Successfully inserted new stat for {date}")
