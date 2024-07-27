import pandas as pd

# Load the datasets
balanced_data = pd.read_csv('C:/Users/laure/Documents/Tech_Impacts_on_Water/Final_Semi_Analysis/data/balanced_data.csv')
small_data = pd.read_csv('C:/Users/laure/Documents/Tech_Impacts_on_Water/Final_Semi_Analysis/data/small_data.csv')

# Rename columns in small_data
small_data = small_data.rename(columns={'name_0': 'country', 'name_1': 'state'})

# Ensure all key columns are of the same data type
keys = ['string_id', 'aq30_id', 'pfaf_id', 'aqid', 'state']

for key in keys:
    balanced_data[key] = balanced_data[key].astype(str).str.strip()
    small_data[key] = small_data[key].astype(str).str.strip()

# Initialize new columns for latitude and longitude
balanced_data['latitude'] = None
balanced_data['longitude'] = None

# Iterate over each row in balanced_data to find the corresponding latitude and longitude
for idx, row in balanced_data.iterrows():
    if row['presence_absence'] == 1:
        # Create a mask to match the keys
        mask = (small_data['string_id'] == row['string_id']) & \
               (small_data['aq30_id'] == row['aq30_id']) & \
               (small_data['pfaf_id'] == row['pfaf_id']) & \
               (small_data['aqid'] == row['aqid']) & \
               (small_data['state'] == row['state'])
        
        # Find the matching row in small_data
        matching_row = small_data[mask]
        
        if not matching_row.empty:
            balanced_data.at[idx, 'latitude'] = matching_row['latitude'].values[0]
            balanced_data.at[idx, 'longitude'] = matching_row['longitude'].values[0]


# Save the merged dataframe to a new CSV file
balanced_data.to_csv('C:/Users/laure/Documents/Tech_Impacts_on_Water/Final_Semi_Analysis/data/balanced_data_with_lat_lon.csv', index=False)

print("Merged data has been saved to 'balanced_data_with_lat_lon.csv'")
