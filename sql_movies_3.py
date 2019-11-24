import sqlite3

with sqlite3.connect("movies.db") as database:
    cursor = database.cursor()
    cursor.execute("""
                    SELECT dirname
                    FROM director
                    WHERE country = 'US';
                    """)

    for row in cursor.fetchall():
        print(row[0])
