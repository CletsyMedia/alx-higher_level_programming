#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:4]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
    else:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
