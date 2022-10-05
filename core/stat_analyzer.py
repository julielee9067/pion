from datetime import datetime
from typing import Dict

from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData

import matplotlib
import matplotlib.dates as mdates

from core.utils import (
    calculate_expected_num_deaths,
    plot_graph_with_polyfit_line,
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
                if data.total_cases:
                    expected_num_deaths = calculate_expected_num_deaths(
                        total_cases=data.total_cases,
                        total_deaths=data.total_deaths,
                        population=country.population,
                    )
                    num_deaths.append(expected_num_deaths)
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

            res[data.country.country_code] = calculate_expected_num_deaths(
                total_deaths=data.total_deaths,
                total_cases=data.total_cases,
                population=data.country.population,
            )

    # Return in descending order with the highest num_deaths
    return dict(sorted(res.items(), key=lambda item: item[1], reverse=True))


if __name__ == "__main__":
    res = get_dates_and_num_deaths()
    country_code = "MEX"
    plot_graph_with_polyfit_line(
        x=res[country_code]["dates"],
        y=res[country_code]["num_deaths"],
        title=f"date_vs_num_deaths_{country_code}",
    )
    numeric_dates = mdates.date2num(res[country_code]["dates"])
    # print(get_mortality_rates_by_date(date=datetime(2021, 6, 30)))
