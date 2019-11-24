import sqlite3

# coonect tot he database
with sqlite3.connect('movies.db') as database:
    # setup the cursor to inteact with the database
    cursor = database.cursor()

    #execute SQL statement
    cursor.execute(
        """SELECT movie.movname, movies_onhire.duedate
            FROM movie
            JOIN movies_onhire
            ON movie.movienumb = movies_onhire.movienumber
        """
    )

    # iterate over the ressults
    for row in cursor.fetchall():
        print(f"{row[0]} is due back on the {row[1]}")