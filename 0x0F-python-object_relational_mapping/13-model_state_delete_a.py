#!/usr/bin/python3
""" Module changes the name of a State object from the database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states_delete = session.query(State).filter(State.name.like('%a%'))
        for state in states_delete:
            session.delete(state)
        session.commit()
    except Exception as e:
        print(f"{e}")

    finally:
        session.close()


if __name__ == "__main__":
    main()
