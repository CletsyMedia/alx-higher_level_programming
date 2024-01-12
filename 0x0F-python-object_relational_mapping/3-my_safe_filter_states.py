#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument (safe from SQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    match = sys.argv[4]

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (match,))

    [print(row) for row in cur.fetchall()]

    cur.close()
    db.close()
