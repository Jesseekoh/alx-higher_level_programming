#!/usr/bin/python3
""" lists all states with a name same as the users input
 from the database hbtn_0e_0_usa
 Usage: ./1-filter_states.py <mysql username>
                            <mysql password>
                            <database name>
                            <state name>"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
              .format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
