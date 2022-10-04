from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData

import matplotlib

matplotlib.use("TkAgg")  # noqa

import matplotlib.pyplot as plt  # noqa


def plot_mortality_rate_by_date():
    with Session(engine) as session:
        country_list = session.query(Country).join(CountryData).all()
        for country in country_list:
            dates = []
            mortality_rates = []

            for data in country.country_datas:
                if data.total_cases:

                    # Ignore outlier
                    if data.total_deaths / data.total_cases == 1:
                        continue

                    mortality_rates.append(data.total_deaths / data.total_cases * 100)
                    dates.append(data.collected_date)

            if not mortality_rates:
                continue

            plt.plot(dates, mortality_rates)
            plt.text(dates[-1], mortality_rates[-1], country.country_code, fontdict={"size": 10})

    plt.xlabel("Date")
    plt.ylabel("COVID-19 mortality rate")
    plt.title("Date vs. COVID-19 Mortality Rate")
    plt.savefig("resources/date_vs_mortality_rate.jpg")


if __name__ == "__main__":
    plot_mortality_rate_by_date()
