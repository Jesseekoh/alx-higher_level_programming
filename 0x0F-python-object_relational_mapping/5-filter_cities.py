#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)
"""

import MySQLdb
import sys

if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASSWD = sys.argv[2]
    MY_DB_NAME = sys.argv[3]
    MY_STATE = sys.argv[4]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASSWD, db=MY_DB_NAME)
    c = db.cursor()
    c.execute("SELECT c.name FROM cities c INNER JOIN states s ON\
                 c.state_id = s.id WHERE s.name = %s\
                 ORDER BY c.id", (MY_STATE, ))
    rows = c.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    print("")
