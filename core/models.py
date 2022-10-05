# coding: utf-8
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True)
    country_code = Column(String, nullable=False)
    population = Column(Float(53))
    country_datas = relationship("CountryData", backref="country")


class CountryData(Base):
    __tablename__ = "country_data"

    country_data_id = Column(Integer, primary_key=True)
    collected_date = Column(Date, nullable=False)
    total_cases = Column(Float(53))
    total_deaths = Column(Float(53))

    country_id = Column(ForeignKey("country.country_id"))
