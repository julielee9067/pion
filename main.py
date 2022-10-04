from core.json_parser import insert_into_db


def main():
    insert_into_db(parsed_file_path="resources/parsed_covid_data.json")


if __name__ == "__main__":
    main()
