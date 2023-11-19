#!/usr/bin/python3
"""
Script that lists all `cities` from the database `hbtn_oe_4_usa`
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb


if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASSWD = sys.argv[2]
    MY_DB_NAME = sys.argv[3]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASSWD, db=MY_DB_NAME)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    [print(city) for city in c.fetchall()]
