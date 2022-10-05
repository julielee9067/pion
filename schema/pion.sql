CREATE TABLE IF NOT EXISTS country (
  country_id SERIAL PRIMARY KEY,
  country_code varchar NOT NULL UNIQUE,
  population float NOT NULL
);

CREATE TABLE IF NOT EXISTS country_data (
  country_data_id SERIAL PRIMARY KEY,
  collected_date date NOT NULL,
  total_cases float default 0,
  total_deaths float default 0,
  expected_deaths float default 0,
  country_id int,
  UNIQUE (collected_date, country_id)
);

ALTER TABLE country_data ADD CONSTRAINT country_id_fkey FOREIGN KEY (country_id) REFERENCES country (country_id);
