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

def table_insert(db_file, table_name, values):
    # connect to database file
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        
        # execute an insert statement for each row of provided data list
        records = 0
        for row in values:
            print(row)
            cursor.execute(f"""
                            INSERT INTO {table_name}
                            VALUES ({row});
                            """)
            records += 1
        print(f"Added {records} records to the {table_name} table")

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

# sites table
create_sites_tbl = """
                    CREATE TABLE Sites (
	                    site_id INTEGER PRIMARY KEY,
	                    street TEXT NOT NULL,
	                    suburb TEXT NOT NULL,
	                    postcode INTEGER NOT NULL,
	                    latitude REAL,
	                    longitude REAL);
                    """
create_table(DB_FILE,"Sites",create_sites_tbl)

# bookings table
create_bookings_tble = """
                        CREATE TABLE Bookings (
                            	booking_id INTEGER PRIMARY KEY,
                                site_id INTEGER NOT NULL,
                                truck_id INTEGER NOT NULL,
                                date TEXT, 
                                start TEXT,
                                finish TEXT);
                        """
create_table(DB_FILE,"Bookings",create_bookings_tble)

# -- write data from JSON files to database --
# create a list with an element for each row of the json file

# truck table

values = []
for row in trucks_data.json():
    truck_id = row['truck_id']
    name = row['name']
    category = row['category']
    if row['website'] == '':
        website = 'none'
    else:
        website = row['website']
    
    values.append(f'{truck_id}, "{name}", "{category}", "{website}"')

table_insert(DB_FILE,"Trucks", values)