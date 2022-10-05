from datetime import datetime
from itertools import islice

import pandas as pd

from core.json_parser import insert_into_db
from core.stat_analyzer import get_num_deaths_by_date


def main():
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")
    mortality_rate = get_num_deaths_by_date(date=datetime(2021, 6, 30))
    first_10_countries = list(islice(mortality_rate.items(), 10))
    p = pd.DataFrame(first_10_countries, columns=["country_code", "mortality_rate"])
    p["perc"] = p["mortality_rate"] / p["mortality_rate"].sum()
    p["num_vaccine"] = p["perc"] * 1000000

    print(p)


if __name__ == "__main__":
    main()
