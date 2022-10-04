import json
from datetime import datetime

from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData


# This was not necessary, but put it here for json file size reduction
def parse_owid_json(file_path: str):
    f = open(file_path)
    data = json.load(f)
    f.close()

    for country, country_data in data.items():
        ind = 0
        res = []

        # Remove all records that's after 2021.06.30
        # Original json was too big to put it on github
        valid_date = datetime.strptime(country_data["data"][ind]["date"], "%Y-%m-%d")
        while valid_date <= datetime(2021, 6, 30):
            res.append(country_data["data"][ind])
            ind += 1

        country_data["data"] = res

    with open("../resources/parsed_covid_data.json", "w") as f:
        json.dump(data, f, indent=2)

    f.close()


def insert_into_db(parsed_file_path: str):
    f = open(parsed_file_path)
    data = json.load(f)
    f.close()

    country_data_list = []
    with Session(engine) as session:
        for country_code, basic_info in data.items():
            # Only consider countries
            if "OWID" in country_code:
                continue

            country_obj = Country(country_code=country_code)
            session.add(country_obj)
            session.commit()

            for item in basic_info["data"]:
                country_data_list.append(
                    {
                        "country_id": country_obj.country_id,
                        "collected_date": item.get("date"),
                        "total_cases": item.get("total_cases"),
                        "total_deaths": item.get("total_deaths"),
                    }
                )

        session.bulk_insert_mappings(CountryData, country_data_list)
        session.commit()

    print("Successfully inserted data into the database")
