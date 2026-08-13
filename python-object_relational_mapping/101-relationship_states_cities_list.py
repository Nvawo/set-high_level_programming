#!/usr/bin/python3
"""Lists all State objects and their corresponding City objects."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            database
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda city: city.id):
            print("\t{}: {}".format(city.id, city.name))

    session.close()
