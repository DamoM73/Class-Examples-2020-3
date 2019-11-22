import sqlite3

DATABASEFILE = "movies.db"

def sql_query(db_file, query):
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        cursor.execute(query)
        
        return cursor.fetchall()



# ---- MAIN PROGRAM ----
query_command = """
                SELECT DISTINCT year 
                FROM movie;
                """

query_results = sql_query(DATABASEFILE,query_command)

for row in query_results:
    print(row[0])