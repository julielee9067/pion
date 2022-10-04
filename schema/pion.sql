CREATE TABLE IF NOT EXISTS country (
  country_id SERIAL PRIMARY KEY,
  country_name varchar NOT NULL,
  population_density float,
  population float,
  aged_65_older float,
  aged_70_older float
);

CREATE TABLE IF NOT EXISTS country_data (
  country_data_id SERIAL PRIMARY KEY,
  collected_date date NOT NULL,
  total_cases float,
  new_cases float,
  total_cases_per_million float,
  new_cases_per_million float,
  country_id int
);

ALTER TABLE country_data ADD CONSTRAINT country_id_fkey FOREIGN KEY (country_id) REFERENCES country (country_id);
