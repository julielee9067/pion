from sqlalchemy.orm import Session

from core.config import engine
from core.models import Country, CountryData


def calculate_population_density_vs_unvaccinated():
    with Session(engine) as session:
        q = session.query(Country).join(CountryData).all()
        for item in q:
            print(item.country_datas)
        return q


if __name__ == "__main__":
    calculate_population_density_vs_unvaccinated()
