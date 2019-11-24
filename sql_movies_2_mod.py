import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT movie.movname, movies_onhire.duedate
            FROM movie
            JOIN movies_onhire
            ON movie.movienumb = movies_onhire.movienumber
        """
database_file = "movies.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"{row[0]} is due back on the {row[1]}")