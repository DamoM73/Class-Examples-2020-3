import sqlite3

def sql_query(db_file):
    with sqlite.connect(db_file) as database:
        cursor = database.cursor()
        cursor.execute()
