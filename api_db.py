import requests
import json

def jprint(obj):
    # Display formatted data only if retrieval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    # If retieval not successful, display error number
    else:
        print(obj.status_code, "error in retrieveal API")

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
jprint(trucks_data)
jprint(sites_data)
jprint(bookings_data)

