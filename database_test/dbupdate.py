import sqlite3

db_filename = "database.db"
db = sqlite3.connect(db_filename)
cursor = db.cursor()

# user can input their own data
nameinput = input("Input Name\n"
                  ":")

# SQL query is run directly against query. Used % formatting to get variable into string
cursor.execute("INSERT INTO NAME_table (NAME)"
               "VALUES ('%s')" % nameinput)

# SQL query to pull all values out of NAME_table
result = cursor.execute("SELECT * FROM NAME_table")
for row in result:
    # raw output
    print("RAW",row)
    # calling id specifically
    print("ID",row[0])
    # calling the name value specifically
    print("NAME",row[1])

db.commit()
db.close()
