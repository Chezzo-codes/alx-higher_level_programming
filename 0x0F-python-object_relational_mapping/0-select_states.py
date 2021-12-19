#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
Takes 3 Args: mysql username, mysql password, database name.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    lst = cur.fetchall()
    for r in lst:
        print(r)
    cur.close()
    db.close()