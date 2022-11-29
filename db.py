import sqlite3

import INTO as INTO

with sqlite3.connect("testdb.db") as connection:
    cursor = connection.cursor()

cursor.execute("CREATE TABLE, User(name TEXT, age INT);")
cursor.execute(INSERT INTO User (VALUES ('Amaka',23))
cursor.execute(SELECT * FROM User)
print (cursor.fetchone())

#
# cursor.executemany("")
# cursor.executescript("")

connection.commit()

connection.close()