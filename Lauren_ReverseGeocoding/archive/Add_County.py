import csv
from geopy.geocoders import Nominatim

input_file = "filtered_addresses.csv"
output_file = "addresses_with_state_county2.csv"
error_file = "error_addresses.csv"
api_key = "718dfd70212641d5a8386ffb687eac8f"

def get_state_and_county(address):
    try:
        geolocator = Nominatim(user_agent="geo_parser")
        location = geolocator.geocode(address, addressdetails=True)

        if location and 'address' in location.raw:
            state = location.raw['address'].get('state', '')
            county = location.raw['address'].get('county', '')
        else:
            state, county = '', ''
    except Exception as e:
        print(f"Error parsing address: {address}, Error: {str(e)}")
        state, county = '', ''

    return state, county

def add_state_and_county_columns(input_file, output_file, error_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile, \
         open(error_file, mode='w', newline='', encoding='utf-8') as errorfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['State', 'County']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        error_writer = csv.writer(errorfile)
        
        # Write headers to the output and error files
        writer.writeheader()
        error_writer.writerow(['Original Address', 'Error'])

        # Iterate through rows, extract state and county, and write to the output file
        for row in reader:
            address = row.get("Formatted Address", "")
            print(f"Processing address: {address}")
            state, county = get_state_and_county(address)

            # Update the row with state and county information
            row['State'] = state
            row['County'] = county

            # Write the updated row to the output file
            writer.writerow(row)
            print(f"Writing row: {row}")

            # Log errors to the error file
            if not county:
                error_writer.writerow([address, 'County not found'])

if __name__ == "__main__":
    add_state_and_county_columns(input_file, output_file, error_file)
