import sqlite3

# connect to the database using the with commant
with sqlite3.connect('movies.db') as database:
    # setup the cursor to interact with the database
    cursor = database.cursor()

    # excute SQL statement
    cursor.execute(
        "SELECT DISTINCT year FROM 'movie';"
    )

    # iterate over the results printing the first element of each row
    for row in cursor.fetchall():
        print(row[0])