CREATE TABLE IF NOT EXISTS country (
  country_id SERIAL PRIMARY KEY,
  country_code varchar NOT NULL UNIQUE,
  country_name varchar,
  population_density float,
  population float,
  aged_65_older float,
  aged_70_older float
);

CREATE TABLE IF NOT EXISTS country_data (
  country_data_id SERIAL PRIMARY KEY,
  collected_date date NOT NULL,
  total_cases float default 0,
  new_cases float default 0,
  total_cases_per_million float default 0,
  new_cases_per_million float default 0,
  total_deaths_per_million float default 0,
  new_deaths_per_million float default 0,
  new_deaths float default 0,
  total_deaths float default 0,
  total_vaccinations float default 0,
  people_vaccinated float default 0,
  total_vaccinations_per_hundred float default 0,
  people_vaccinated_per_hundred float default 0,
  country_id int,
  UNIQUE (collected_date, country_id)
);


CREATE TABLE IF NOT EXISTS icu (
  icu_id SERIAL PRIMARY KEY,
  country_id int UNIQUE,
  beds_per_capita float NOT NULL default 0
);

ALTER TABLE country_data ADD CONSTRAINT country_id_fkey FOREIGN KEY (country_id) REFERENCES country (country_id);
ALTER TABLE icu ADD CONSTRAINT country_id_fkey FOREIGN KEY (country_id) REFERENCES country (country_id);
