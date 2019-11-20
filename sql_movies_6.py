import sqlite3

DATABASEFILE = "movies.db"

def sql_query(db_file, query):
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        cursor.execute(query)
        
        return cursor.fetchall()

# ---- MAIN PROGRAM ----
query_command = """
                SELECT country, COUNT(dirname)
                FROM director
                GROUP BY country;
                """

query_results = sql_query(DATABASEFILE,query_command)

for row in query_results:
    if row[1] == 1:
        print(f"{row[0]} has {row[1]} director.")
    else:
        print(f"{row[0]} has {row[1]} directors.")