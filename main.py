from core.json_parser import insert_into_db, insert_country_names_into_db, insert_icu_data_into_db


def main():
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")
    insert_country_names_into_db(file_path="resources/countries.json")
    insert_icu_data_into_db(file_path="resources/icu_beds_per_capita.json")


if __name__ == "__main__":
    main()
