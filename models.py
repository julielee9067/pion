# coding: utf-8
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)
    population_density = Column(Float(53))
    population = Column(Float(53))
    aged_65_older = Column(Float(53))
    aged_70_older = Column(Float(53))


class CountryData(Base):
    __tablename__ = "country_data"

    country_data_id = Column(Integer, primary_key=True)
    collected_date = Column(Date, nullable=False)
    total_cases = Column(Float(53))
    new_cases = Column(Float(53))
    total_cases_per_million = Column(Float(53))
    new_cases_per_million = Column(Float(53))
    total_deaths_per_million = Column(Float(53))
    new_deaths_per_million = Column(Float(53))
    new_deaths = Column(Float(53))
    total_deaths = Column(Float(53))
    total_vaccinations = Column(Float(53))
    people_vaccinated = Column(Float(53))
    total_vaccinations_per_hundred = Column(Float(53))
    people_vaccinated_per_hundred = Column(Float(53))

    country_id = Column(ForeignKey("country.country_id"))

    country = relationship(
        "Country",
        primaryjoin="CountryData.country_id == Country.country_id",
        backref="country_data",
    )
