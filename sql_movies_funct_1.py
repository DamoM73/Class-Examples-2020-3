import sqlite3

DATABASEFILE = "school.db"

def sql_query(db_file, query):
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        cursor.execute(query)
        
        return cursor.fetchall()

# ---- MAIN PROGRAM ----
query_command = """
                SELECT student.stname, AVG(results.percent)
                FROM results
                JOIN student
                ON results.stnumb = student.stnumb
                WHERE student.grade = 7
                GROUP BY student.stname;
                """

query_results = sql_query(DATABASEFILE,query_command)

for row in query_results:
    print(f"{row[0]} achieved an average grade of {row[1]}")