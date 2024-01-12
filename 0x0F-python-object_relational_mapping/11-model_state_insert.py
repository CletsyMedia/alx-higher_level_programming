#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:4]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)
    else:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
