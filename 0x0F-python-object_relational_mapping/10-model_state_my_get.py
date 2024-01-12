#!/usr/bin/python3
"""Prints the State object with the name passed as an argument
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database, state_name = sys.argv[1:5]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")
    else:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
