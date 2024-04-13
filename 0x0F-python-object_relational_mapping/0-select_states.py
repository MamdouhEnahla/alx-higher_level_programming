#!/usr/bin/python3

"""script lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password, db = sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           password=password, database=db, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
