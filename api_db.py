import requests
import json
import sqlite3

DB_FILE = "food_trucks.db"

def jprint(obj):
    # Display formatted data only if retrieval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    # If retieval not successful, display error number
    else:
        print(obj.status_code, "error in retrieveal API")

def create_table(filename, tablename, sqlcommand):
    # connecting to dtabase file
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()

        # remove previous table and data
        cursor.execute(f"DROP TABLE IF EXISTS {tablename};")

        # create empty table
        cursor.execute(sqlcommand)


# ---- MAIN PROGRAM ----

# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")
sites_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/sites")
bookings_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/bookings")

# check request status
#print(trucks_data.status_code)
#print(sites_data.status_code)
#print(bookings_data.status_code)

# view data
#print(trucks_data.json())
#print(sites_data.json())
#print(bookings_data.json())

# display formatted data
#jprint(trucks_data)
#jprint(sites_data)
#jprint(bookings_data)

# --- create database tables ---
# trucks table
create_trucks = """
                CREATE TABLE Trucks(
                    truck_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    website TEXT
                );
                """

create_table(DB_FILE, "Trucks", create_trucks)