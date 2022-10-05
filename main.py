from datetime import datetime

from core.stat_analyzer import (
    get_first_n_countries_stat,
    get_prediction_on_n_countries_stat_by_date,
)


def main():
    # insert_into_db(parsed_file_path="resources/parsed_covid_data.json")
    stat = get_first_n_countries_stat(n=10)
    print(stat)

    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 8, 30))
    print(prediction)


if __name__ == "__main__":
    main()
