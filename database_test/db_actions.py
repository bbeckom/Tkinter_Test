import sqlite3

db_filename = "database.db"
db = sqlite3.connect(db_filename)
cursor = db.cursor()


def add_name(name, val=''):
    name = str(name)
    cursor.execute("INSERT INTO NAME_table (NAME)"
                         "VALUES ('%s')" % name)
    db.commit()
    added_name = cursor.execute("SELECT * FROM NAME_table WHERE NAME='%s' ORDER BY ID DESC LIMIT 1" % name)
    return added_name


def list_names(val=''):
    names = cursor.execute("SELECT * FROM NAME_table")
    return names


def list_individual(name, val=''):
    name = str(name)
    names = cursor.execute("SELECT * FROM NAME_table WHERE NAME='%s'" % name)
    return names


def remove_name(name, val=''):
    name = str(name)
    cursor.execute("DELETE FROM NAME_table WHERE NAME='%s'" % name)
    db.commit()
    names = cursor.execute("SELECT * FROM NAME_table")
    return names


def sql_query(query, val=''):
    query = str(query)
    try:
        result = cursor.execute(query)
        db.commit()
        return result.fetchall()
    except Exception as result:
        return result
