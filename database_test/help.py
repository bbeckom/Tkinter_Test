def table_help(num):
    if num == 1:
        text = "CREATE TABLE NAME_table (\n" \
               "ID integer primary key autoincrement not null,\n" \
               "NAME text\n" \
               ")"
        return text
    if num == 2:
        text = "CREATE TABLE Persons (\n" \
               "PersonID int,\n" \
               "LastName varchar(255),\n" \
               "FirstName varchar(255),\n" \
               "Address varchar(255),\n" \
               "City varchar(255)\n" \
               ")"
        return text
    if num == 3:  # list tables
        text = "SELECT name FROM sqlite_master WHERE type='table'"
        return text
    if num == 4:  # show table columns
        text = "PRAGMA table_info(NAME_table)"
        return text


def select_help(num):
    if num == 1:
        text = "SELECT * FROM NAME_table"
        return text
    if num == 2:
        text = "SELECT * FROM NAME_table WHERE ID=1"
        return text


def delete_help(num):
    if num == 1:
        text = 'DELETE FROM NAME_table WHERE NAME="testname1"'
        return text


def insert_help(num):
    if num == 1:
        text = 'INSERT INTO NAME_table (NAME) VALUES ("testname2")'
        return text
