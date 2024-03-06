# pip install uszipcode
import pandas as pd
import re
from uszipcode import SearchEngine

# Functions
# Function to get state from ZIP code
def get_state(zip_code):
    try:
        search = SearchEngine(simple_zipcode=True)
        zipcode_info = search.by_zipcode(zip_code)
        return zipcode_info.state
    except Exception as e:
        print(f"Error getting state for ZIP code {zip_code}: {str(e)}")
        return None

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

# Function to extract ZIP code from the "Formatted Address" column
def extract_zip_code(address):
    # Find all matches of five digits in the address
    matches = re.findall(r'\b\d{5}\b', address)
    
    # Return the last match if any
    if matches:
        return matches[-1]
    else:
        return None
    
# Define Variables
input_file_path = 'Lauren_ReverseGeocoding/WRI_dataset.csv'
output_file_path = 'Lauren_ReverseGeocoding/WRI_updated_dataset.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file_path)

'''
# Remove columns to make it temporarily easier to read
columns_to_remove = [
    'dwnBasinID', 'Area_km2', 'Shape_Leng', 'ws2024tl', 'ws3024tl', 'ws4024tl',
    'ws2028tl', 'ws3028tl', 'ws4028tl', 'ws2038tl', 'ws3038tl', 'ws4038tl',
    'Shape_Le_1', 'Shape_Area', 'FacilityID', 'Latitude', 'Longitude'
]
df = df.drop(columns=columns_to_remove, errors='ignore')
'''
# Filter rows based on the "Formatted Address" column
df = df[df['Formatted Address'].str.contains(" USA", case=False, na=False)]

# Apply the function to create the "Zip Code" column
df['Zip Code'] = df['Formatted Address'].apply(extract_zip_code)

# Apply the function to create the "State" column
df['State'] = df['Zip Code'].apply(get_state)

# Apply the function to create the "County" column
df['County'] = df.apply(lambda row: get_county(row['Zip Code'], row['State']), axis=1)

# Write the DataFrame to a CSV file
df.to_csv(output_file_path, index=False)



# Display the total number of rows in the DataFrame
total_rows = df.shape[0]
print(f'Total number of rows: {total_rows}')






# Display the first few rows of the DataFrame
print(df.head())
