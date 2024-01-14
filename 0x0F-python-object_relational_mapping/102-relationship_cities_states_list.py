#!/usr/bin/python3
"""
script that creates the State "California" with the City
"San Francisco" from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City).order_by(City.id).all()

    for cities in results:
        print(f"{cities.id}: {cities.name} -> {cities.state.name}")
    session.close()
