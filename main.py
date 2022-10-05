from datetime import datetime
import warnings
from core.json_parser import insert_into_db
from core.stat_analyzer import (
    get_first_n_countries_stat,
    get_prediction_on_n_countries_stat_by_date,
    insert_new_pred_stat,
)
from core.utils import compare_stat

warnings.filterwarnings("ignore")


def main():
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")

    print("------- 2021.06.30 백신 공급 량 -------")
    stat = get_first_n_countries_stat(n=10)
    print(stat)

    print("------- 백신 미지급 3개월 후 -------")
    no_v_3 = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 9, 30))
    print(no_v_3)

    print("------- 백신 미지급 6개월 후 -------")
    no_v_6 = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 12, 30))
    print(no_v_6)

    print("------- 백신 미지급 12개월 후 -------")
    no_v_12 = get_prediction_on_n_countries_stat_by_date(date=datetime(2022, 6, 30))
    print(no_v_12)

    print("------- 백신 미지급 36개월 후 -------")
    no_v_36 = get_prediction_on_n_countries_stat_by_date(date=datetime(2024, 6, 30))
    print(no_v_36)

    insert_new_pred_stat()
    print("------- 백신 지급 3개월 후 -------")
    v_3 = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 9, 30))
    print(v_3)

    print("------- 백신 지급 6개월 후 -------")
    v_6 = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 12, 30))
    print(v_6)

    print("------- 백신 지급 12개월 후 -------")
    v_12 = get_prediction_on_n_countries_stat_by_date(date=datetime(2022, 6, 30))
    print(v_12)

    print("------- 백신 지급 36개월 후 -------")
    v_36 = get_prediction_on_n_countries_stat_by_date(date=datetime(2024, 6, 30))
    print(v_36)

    comp_3 = compare_stat(no_v=no_v_3, v=v_3)
    comp_6 = compare_stat(no_v=no_v_6, v=v_6)
    comp_12 = compare_stat(no_v=no_v_12, v=v_12)
    comp_36 = compare_stat(no_v=no_v_36, v=v_36)

    print("------- 퍼센티지 비교 -------")
    print(f"3개월 후: {comp_3}")
    print(f"6개월 후: {comp_6}")
    print(f"12개월 후: {comp_12}")
    print(f"36개월 후: {comp_36}")

    print("------- 2021.08.30 백신 공급 량 -------")
    prediction = get_prediction_on_n_countries_stat_by_date(date=datetime(2021, 8, 30))
    print(prediction)


if __name__ == "__main__":
    main()
