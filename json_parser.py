import json
from datetime import datetime


def parse_json(file_path: str):
    f = open(file_path)
    data = json.load(f)

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


if __name__ == "__main__":
    parse_json("resources/owid_covid_data.json")
