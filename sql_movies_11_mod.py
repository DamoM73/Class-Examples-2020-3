import sqlite3

def run_sql_statement(dbfile,sql_statement):
    # connect to database and initalise cursor
    with sqlite3.connect(dbfile) as database:
        cursor = database.cursor()

        #execute sqlstatement
        cursor.execute(sql_statement)

        # return list of results
        return cursor.fetchall()

query = """SELECT members.memname, COUNT(movies_onhire.movienumber)
            FROM members
            JOIN movies_onhire
            ON members.memberid = movies_onhire.memberid
            GROUP BY members.memname;
        """
database_file = "movies.db"

result = run_sql_statement(database_file,query)

for row in result:
    print(f"{row[0]} has {row[1]} movies on hire")