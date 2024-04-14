#!/usr/bin/python3

""" lists all cities from the database hbtn_0e_4_usa. """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=db_name, charset="utf8")
    result = db.cursor()
    result.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   ORDER BY cities.id""")
    rows = result.fetchall()
    for row in rows:
        print(row)
    result.close()
