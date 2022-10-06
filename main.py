from datetime import datetime
import warnings

from core.config import engine
from core.json_parser import insert_into_db
from core.models import Base, Country, CountryData
from core.stat_analyzer import (
    get_countries_stat,
    get_prediction_on_countries_stat_by_date,
    insert_new_pred_stat,
)
from core.utils import compare_stat

warnings.filterwarnings("ignore")


def main():
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")

    print("------- 2021.06.30 백신 공급 량 -------")
    stat = get_countries_stat()
    print(stat.iloc[:10].to_string())

    print("------- 백신 미지급 3개월 후 -------")
    no_v_3 = get_prediction_on_countries_stat_by_date(
        date=datetime(2021, 9, 30), file_name="resources/no_v_3.csv"
    )
    print(no_v_3.iloc[:10].to_string())

    print("------- 백신 미지급 6개월 후 -------")
    no_v_6 = get_prediction_on_countries_stat_by_date(
        date=datetime(2021, 12, 30), file_name="resources/no_v_6.csv"
    )
    print(no_v_6.iloc[:10].to_string())

    print("------- 백신 미지급 12개월 후 -------")
    no_v_12 = get_prediction_on_countries_stat_by_date(
        date=datetime(2022, 6, 30), file_name="resources/no_v_12.csv"
    )
    print(no_v_12.iloc[:10].to_string())

    print("------- 백신 미지급 36개월 후 -------")
    no_v_36 = get_prediction_on_countries_stat_by_date(
        date=datetime(2024, 6, 30), file_name="resources/no_v_36.csv"
    )
    print(no_v_36.iloc[:10].to_string())

    insert_new_pred_stat()
    print("------- 백신 지급 3개월 후 -------")
    v_3 = get_prediction_on_countries_stat_by_date(
        date=datetime(2021, 9, 30), file_name="resources/v_3.csv"
    )
    print(v_3.iloc[:10].to_string())

    print("------- 백신 지급 6개월 후 -------")
    v_6 = get_prediction_on_countries_stat_by_date(
        date=datetime(2021, 12, 30), file_name="resources/v_6.csv"
    )
    print(v_6.iloc[:10].to_string())

    print("------- 백신 지급 12개월 후 -------")
    v_12 = get_prediction_on_countries_stat_by_date(
        date=datetime(2022, 6, 30), file_name="resources/v_12.csv"
    )
    print(v_12.iloc[:10].to_string())

    print("------- 백신 지급 36개월 후 -------")
    v_36 = get_prediction_on_countries_stat_by_date(
        date=datetime(2024, 6, 30), file_name="resources/v_36.csv"
    )
    print(v_36.iloc[:10].to_string())
    "{:.8f}".format(float("8.99284722486562e-02"))

    comp_3 = "{:.8f}".format(compare_stat(no_v=no_v_3, v=v_3))
    comp_6 = "{:.8f}".format(compare_stat(no_v=no_v_6, v=v_6))
    comp_12 = "{:.8f}".format(compare_stat(no_v=no_v_12, v=v_12))
    comp_36 = "{:.8f}".format(compare_stat(no_v=no_v_36, v=v_36))

    print("------- 퍼센티지 비교 -------")
    print(f"3개월 후 [%]: {comp_3}")
    print(f"6개월 후 [%]: {comp_6}")
    print(f"12개월 후 [%]: {comp_12}")
    print(f"36개월 후 [%]: {comp_36}")

    print("------- 2021.08.30 백신 공급 량 -------")
    prediction = get_prediction_on_countries_stat_by_date(
        date=datetime(2021, 8, 30), file_name="resources/prediction.csv"
    )
    print(prediction.iloc[:10].to_string())


def truncate_tables():
    Base.metadata.drop_all(engine, tables=[Country.__table__, CountryData.__table__])
    Base.metadata.create_all(engine, tables=[Country.__table__, CountryData.__table__])
    print("Successfully truncated all tables")


if __name__ == "__main__":
    main()
    truncate_tables()
