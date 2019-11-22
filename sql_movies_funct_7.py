import sqlite3

DATABASEFILE = "school.db"

def sql_query(db_file, query):
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        cursor.execute(query)
        
        return cursor.fetchall()



# ---- MAIN PROGRAM ----
query_command = """
                SELECT student.stname
                FROM student
                JOIN results
                ON student.stnumb = results.stnumb
                JOIN subject
                ON subject.subjnumb = results.subjnumb
                WHERE tname LIKE 'Simm%';
                """

query_results = sql_query(DATABASEFILE,query_command)

for row in query_results:
    print(row[0])