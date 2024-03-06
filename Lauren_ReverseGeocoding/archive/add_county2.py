import pandas as pd
from geopy.geocoders import OpenCage

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('updated_addresses.csv', dtype={'Zip Code': str})

# Replace 'your_opencage_api_key' with your actual OpenCage API key
opencage_api_key = '718dfd70212641d5a8386ffb687eac8f'
geolocator = OpenCage(opencage_api_key)

# Function to get county from zip code
def get_county(zip_code):
    try:
        location = geolocator.geocode(f'{zip_code}, USA')
        if location and 'county' in location.raw['components']:
            county = location.raw['components']['county']
            return county
        else:
            print(f"No data found for ZIP code: {zip_code}")
            return None
    except Exception as e:
        print(f"Error processing ZIP code {zip_code}: {str(e)}")
        return None

# Apply the function to create the "County" column
df['County'] = df['Zip Code'].apply(get_county)

# Save the updated DataFrame to a new CSV file
df.to_csv('final_addresses.csv', index=False)
