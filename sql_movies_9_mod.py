import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT movname, year
            FROM movie
            ORDER BY year
            LIMIT 5;
        """
database_file = "movies.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"{row[0]} was released in {row[1]}")