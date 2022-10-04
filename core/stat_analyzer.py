from typing import Dict

from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData
import matplotlib

matplotlib.use("TkAgg")  # noqa

import matplotlib.pyplot as plt  # noqa


def save_population_vs_cases():
    res = dict()

    with Session(engine) as session:
        q = session.query(Country).join(CountryData).all()
        for item in q:
            if item.population_density is not None:
                res[item.country_name] = {
                    "date": [],
                    "total_cases": [],
                    "unvaccinated_people": [],
                    "population_density": item.population_density,
                }
                for data in item.country_datas:
                    res[item.country_name]["total_cases"].append(data.total_cases / item.population)
                    res[item.country_name]["date"].append(data.collected_date)
                    res[item.country_name]["unvaccinated_people"].append(
                        item.population - data.people_vaccinated
                    )

    for country_code, data in res.items():
        plt.scatter(data["population_density"], data["total_cases"][-1])
        plt.text(data["population_density"], data["total_cases"][-1], country_code)

    plt.xlabel("Population density")
    plt.ylabel("COVID-19 total cases")
    plt.title("Population density vs. COVID-19 total cases")
    plt.savefig("resources/population_vs_cases.jpg")


def plot_graph(data: Dict):
    for key, data_list in data.items():
        dates = [data[0] for data in data_list]
        confirmed_cases = [data[1] for data in data_list]
        plt.plot(dates, confirmed_cases)
        plt.gcf().autofmt_xdate()
        plt.text(dates[-1], confirmed_cases[-1], key)

    plt.show()


if __name__ == "__main__":
    save_population_vs_cases()
    # plot_graph(data=cases)
