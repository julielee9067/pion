from datetime import datetime
import warnings
from core.json_parser import insert_into_db
from core.stat_analyzer import (
    get_first_n_countries_stat,
    get_prediction_on_n_countries_stat_by_date,
    insert_new_pred_stat,
)

warnings.filterwarnings("ignore")


def main():
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")

    print("------- 2021.06.30 백신 공급 량 -------")
    stat = get_first_n_countries_stat(n=10)
    print(stat)

    print("------- 백신 미지급 3개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 9, 30))
    print(prediction)

    print("------- 백신 미지급 6개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 12, 30))
    print(prediction)

    print("------- 백신 미지급 12개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2022, 6, 30))
    print(prediction)

    print("------- 백신 미지급 36개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2024, 6, 30))
    print(prediction)

    insert_new_pred_stat()
    print("------- 백신 미지급 3개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 9, 30))
    print(prediction)

    print("------- 백신 미지급 6개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 12, 30))
    print(prediction)

    print("------- 백신 미지급 12개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2022, 6, 30))
    print(prediction)

    print("------- 백신 미지급 36개월 후 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2024, 6, 30))
    print(prediction)

    print("------- 2021.08.30 백신 공급 량 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 8, 30))
    print(prediction)


if __name__ == "__main__":
    main()
