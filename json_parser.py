import json
from datetime import datetime

from sqlalchemy.orm import Session

from config import engine
from models import Country, CountryData


def parse_json(file_path: str):
    f = open(file_path)
    data = json.load(f)
    f.close()

    for country, country_data in data.items():
        ind = 0
        res = []

        while datetime.strptime(country_data["data"][ind]["date"], "%Y-%m-%d") <= datetime(
            2021, 6, 30
        ):
            res.append(country_data["data"][ind])
            ind += 1

        country_data["data"] = res

    with open("resources/parsed_covid_data.json", "w") as f:
        json.dump(data, f, indent=2)

    f.close()


def insert_into_db(parsed_file_path: str):
    f = open(parsed_file_path)
    data = json.load(f)
    f.close()

    country_data_objs = []
    with Session(engine) as session:

        for country, basic_info in data.items():
            country_obj = Country(
                country_name=country,
                **{
                    "population_density": basic_info.get("population_density"),
                    "population": basic_info.get("population"),
                    "aged_65_older": basic_info.get("aged_65_older"),
                    "aged_70_older": basic_info.get("aged_70_older"),
                }
            )
            session.add(country_obj)

            for item in basic_info["data"]:
                country_data_objs.append(
                    CountryData(
                        country=country_obj,
                        **{
                            "collected_date": item.get("date"),
                            "total_cases": item.get("total_cases"),
                            "new_cases": item.get("new_cases"),
                            "total_cases_per_million": item.get("total_cases_per_million"),
                            "new_cases_per_million": item.get("new_cases_per_million"),
                        }
                    )
                )

        session.bulk_save_objects(country_data_objs)
        session.commit()


if __name__ == "__main__":
    # parse_json("resources/owid_covid_data.json")
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")
