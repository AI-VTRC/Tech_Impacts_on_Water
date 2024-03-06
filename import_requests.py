import requests
import csv

api_key = "AIzaSyDpQFJpnjPy9wl1XtWvAYiijtC0msHTo58"
input_file = "coordinates.csv"
output_file = "output_addresses.csv"

def geocode_coordinates(latitude, longitude):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        return data["results"][0]["formatted_address"]
    else:
        return "Geocoding failed"

with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Latitude", "Longitude", "Formatted Address"])

    for row in rows:
        #latitude = row["Latitude"]
        #longitude = row["Longitude"]
        latitude = row.get("Latitude", "")
        longitude = row.get("Longitude", "")
        formatted_address = geocode_coordinates(latitude, longitude)
        writer.writerow([latitude, longitude, formatted_address])
