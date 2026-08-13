#!/usr/bin/python3
"""Get a State by name."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == state_name
    ).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
