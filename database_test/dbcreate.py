# run this to create a db file or start out fresh with default

import os
import sqlite3

db_filename = "database.db"

# if db file exists, delete it
dbexist = os.path.exists(db_filename)
if dbexist:
    # unlink deletes file
    os.unlink(db_filename)

# connect and/or create file
db = sqlite3.connect(db_filename)

# run SQL commands with cursor
cursor = db.cursor()

# create a variable with SQL syntax, this can be directly passed as well
# ID key will automatically generate based on when the item was entered
# NAME is value of key and 'text' is the type of data that can be provided to it
NAMEtable = "CREATE TABLE NAME_table (" \
        "ID integer primary key autoincrement not null," \
        "NAME text" \
        ")"
# run query with execute command against cursor
cursor.execute(NAMEtable)

# list all tables in db
listables = "SELECT name FROM sqlite_master WHERE type='table'"
cursor.execute(listables)
print(cursor.fetchall())

# create a testuser
query = "INSERT INTO NAME_table (NAME) values ('testname1')"
cursor.execute(query)

# commit changes
db.commit()
# close db connection
db.close()