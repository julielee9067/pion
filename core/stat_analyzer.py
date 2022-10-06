from datetime import datetime, date
from typing import Dict, Optional

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


def get_dates_and_data() -> Dict:
    res = {}
    with Session(engine) as session:
        country_list = session.query(Country).join(CountryData).all()
        for country in country_list:
            dates = []
            num_deaths = []
            mortality_rates = []

            for data in country.country_datas:
                if data.expected_deaths:
                    num_deaths.append(data.expected_deaths)
                    dates.append(data.collected_date)
                    mortality_rates.append(data.mortality_rate)

            if not num_deaths:  # Some total_deaths data were missing for a few countries
                continue

            res[country.country_code] = {
                "dates": dates,
                "num_deaths": num_deaths,
                "mortality_rates": mortality_rates,
                "population": country.population,
            }

    return res


def get_data_by_date(date: date):
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
                res[data.country.country_code] = {
                    "num_deaths": data.expected_deaths,
                    "mortality_rate": data.mortality_rate,
                    "population": data.country.population,
                }

    # Return in descending order with the highest mortality rate
    return dict(sorted(res.items(), key=lambda item: item[1]["mortality_rate"], reverse=True))


def get_countries_stat(date: date = datetime(2021, 6, 30)) -> DataFrame:
    data = get_data_by_date(date=date)
    p = DataFrame.from_dict(data, orient="index", columns=["num_deaths", "mortality_rate"])

    p["num_deaths"] = p["num_deaths"].astype("int64")
    p["perc"] = (p["num_deaths"] / p["num_deaths"].sum()).round(6)
    p["num_vaccine"] = p["perc"] * 1000000
    p = p.sort_values("num_vaccine", ascending=False)

    return p


def plot_country_graph(country_code: str) -> None:
    res = get_dates_and_data()
    plot_graph_with_polyfit_line(
        x=res[country_code]["dates"],
        y=res[country_code]["num_deaths"],
        title=f"date_vs_num_deaths_{country_code}",
    )


def get_prediction_on_countries_stat_by_date(
    date: date, file_name: Optional[str] = None
) -> DataFrame:
    res = get_dates_and_data()
    prediction_results = dict()

    for country_code, data in res.items():
        line = get_polyfit_line(x=data["dates"], y=data["mortality_rates"])
        mortality_rate_prediction = predict_trend(input=date, polyfit_line=line)
        prediction_results[country_code] = {
            "mortality_rates_prediction": mortality_rate_prediction,
            "population": data["population"],
        }

    p = DataFrame.from_dict(
        prediction_results, orient="index", columns=["population", "mortality_rates_prediction"]
    )

    # Remove impossible situations
    p.loc[p["mortality_rates_prediction"] < 0, "mortality_rates_prediction"] = 0
    p.loc[p["mortality_rates_prediction"] > 1, "mortality_rates_prediction"] = 1

    p["num_deaths_prediction"] = p["mortality_rates_prediction"] * p["population"]
    p["num_deaths_prediction"] = p["num_deaths_prediction"].astype("int64")
    p["population"] = p["population"].astype("int64")
    p["perc"] = (p["num_deaths_prediction"] / p["num_deaths_prediction"].sum()).round(6)

    # Remove unnecessary data
    p = p[p["perc"] != 0]

    p["num_vaccine"] = p["perc"] * 1000000
    p = p.sort_values("num_vaccine", ascending=False)

    if file_name is not None:
        p.to_csv(file_name, encoding="utf-8")

    return p


def insert_new_pred_stat(date: date = datetime(2021, 7, 1)) -> None:
    pred = get_prediction_on_countries_stat_by_date(date=date).T.to_dict()
    new_stat_list = []
    with Session(engine) as session:
        for country_code, data in pred.items():
            country = session.query(Country).filter(Country.country_code == country_code).first()
            new_data = dict(
                collected_date=date,
                mortality_rate=data["mortality_rates_prediction"],
                expected_deaths=data["num_deaths_prediction"] - data["num_vaccine"],
                country_id=country.country_id,
            )
            new_stat_list.append(new_data)

        session.bulk_insert_mappings(CountryData, new_stat_list)
        session.commit()

    print(f"Successfully inserted new stat for {date}")
