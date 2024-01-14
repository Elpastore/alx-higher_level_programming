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

    results = session.query(State).order_by(State.id).all()

    for state in results:
        print(f"{state.id}: {state.name}")
        for cities in state.cities:
            print(f"    {cities.id}: {cities.name}")
    session.close()
