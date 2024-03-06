# pip install uszipcode
import pandas as pd
from uszipcode import SearchEngine

# Specify the file name
file_path = 'Lauren_ReverseGeocoding/semi_water_stress_dataset.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Remove columns to make it temporarily easier to read
columns_to_remove = [
    'dwnBasinID', 'Area_km2', 'Shape_Leng', 'ws2024tl', 'ws3024tl', 'ws4024tl',
    'ws2028tl', 'ws3028tl', 'ws4028tl', 'ws2038tl', 'ws3038tl', 'ws4038tl',
    'Shape_Le_1', 'Shape_Area', 'FacilityID', 'Latitude', 'Longitude'
]
df = df.drop(columns=columns_to_remove, errors='ignore')

# Filter rows based on the "Formatted Address" column
df = df[df['Formatted Address'].str.contains("USA", case=False, na=False)]

# Extract the last five digits from the "Formatted Address" column
df['Zip Code'] = df['Formatted Address'].str.extract(r'(\b\d{5}\b)')

# Function to get state from ZIP code
def get_state(zip_code):
    try:
        search = SearchEngine(simple_zipcode=True)
        zipcode_info = search.by_zipcode(zip_code)
        return zipcode_info.state
    except Exception as e:
        print(f"Error getting state for ZIP code {zip_code}: {str(e)}")
        return None

# Apply the function to create the "State" column
df['State'] = df['Zip Code'].apply(get_state)

# Function to get county from ZIP code and state
def get_county(zip_code, state):
    try:
        search = SearchEngine(simple_zipcode=True)
        zipcode_info = search.by_zipcode(zip_code)
        
        # Check if the state from ZIP code matches the provided state
        if zipcode_info.state == state:
            return zipcode_info.county
        else:
            return None
    except Exception as e:
        print(f"Error getting county for ZIP code {zip_code} and state {state}: {str(e)}")
        return None

# Apply the function to create the "County" column
df['County'] = df.apply(lambda row: get_county(row['Zip Code'], row['State']), axis=1)

# Display the modified DataFrame with the new "County" column
print(df[['Formatted Address', 'Zip Code', 'State', 'County']])





# Display the total number of rows in the DataFrame
total_rows = df.shape[0]
print(f'Total number of rows: {total_rows}')






# Display the first few rows of the DataFrame
print(df.head())
