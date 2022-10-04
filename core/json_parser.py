import json
from datetime import datetime

from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData, ICU


def parse_owid_json(file_path: str):
    f = open(file_path)
    data = json.load(f)
    f.close()

    for country, country_data in data.items():
        ind = 0
        res = []

        # Remove all records that's after 2021.06.30
        while datetime.strptime(country_data["data"][ind]["date"], "%Y-%m-%d") <= datetime(
            2021, 6, 30
        ):
            res.append(country_data["data"][ind])
            ind += 1

        country_data["data"] = res

    with open("../resources/parsed_covid_data.json", "w") as f:
        json.dump(data, f, indent=2)

    f.close()


def insert_country_names_into_db(file_path: str):
    f = open(file_path)
    data = json.load(f)
    f.close()

    with Session(engine) as session:
        for item in data:
            country = session.query(Country).filter(Country.country_code == item["alpha-3"]).first()
            if country is not None:
                country.country_name = item["name"]
        session.commit()


def insert_icu_data_into_db(file_path: str):
    f = open(file_path)
    data = json.load(f)
    f.close()

    with Session(engine) as session:
        icu_list = []
        for item in data:
            country = session.query(Country).filter(Country.country_name == item["country"]).first()
            if country is not None:
                icu_list.append(ICU(beds_per_capita=item["pop2022"], country_id=country.country_id))

        session.bulk_save_objects(icu_list)
        session.commit()

    f.close()


def insert_into_db(parsed_file_path: str):
    f = open(parsed_file_path)
    data = json.load(f)
    f.close()

    country_data_objs = []
    with Session(engine) as session:
        for country_code, basic_info in data.items():
            if "OWID" in country_code:
                continue

            country_obj = Country(
                country_code=country_code,
                **{
                    "population_density": basic_info.get("population_density"),
                    "population": basic_info.get("population"),
                    "aged_65_older": basic_info.get("aged_65_older"),
                    "aged_70_older": basic_info.get("aged_70_older"),
                }
            )
            session.add(country_obj)
            session.commit()

            for item in basic_info["data"]:
                country_data_objs.append(
                    CountryData(
                        country_id=country_obj.country_id,
                        **{
                            "collected_date": item.get("date"),
                            "total_cases": item.get("total_cases"),
                            "new_cases": item.get("new_cases"),
                            "total_cases_per_million": item.get("total_cases_per_million"),
                            "new_cases_per_million": item.get("new_cases_per_million"),
                            "total_deaths": item.get("total_deaths"),
                            "total_deaths_per_million": item.get("total_deaths_per_million"),
                            "new_deaths_per_million": item.get("new_deaths_per_million"),
                            "new_deaths": item.get("new_deaths"),
                            "total_vaccinations": item.get("total_vaccinations"),
                            "people_vaccinated": item.get("people_vaccinated"),
                            "total_vaccinations_per_hundred": item.get(
                                "total_vaccinations_per_hundred"
                            ),
                            "people_vaccinated_per_hundred": item.get(
                                "people_vaccinated_per_hundred"
                            ),
                        }
                    )
                )

        session.bulk_save_objects(country_data_objs)
        session.commit()

    print("Successfully inserted data to database")
