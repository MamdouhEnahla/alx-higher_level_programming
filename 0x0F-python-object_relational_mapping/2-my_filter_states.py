#!/usr/bin/python3

""" displays values in the states table where name matches the argument. """

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
    result.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(name))
    rows = result.fetchall()
    for row in rows:
        print(row)
    result.close()
