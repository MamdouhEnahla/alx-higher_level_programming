#!/usr/bin/python3

""" lists all cities of that state, using the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=db_name, charset="utf8")
    result = db.cursor()
    result.execute("""SELECT cities.name FROM cities INNER JOIN states
                   ON states.id=cities.state_id
                   WHERE states.name = %s""", (name,))
    rows = result.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    result.close()
