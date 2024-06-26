#!/usr/bin/python3
""" adds the State object Louisiana to the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        louisiana = State(name='Louisiana')
        session.add(louisiana)
        session.commit()
        print(louisiana.id)
    except Exception as ex:
        print('{}').format(ex)
    finally:
        session.close()


if __name__ == "__main__":
    main()
