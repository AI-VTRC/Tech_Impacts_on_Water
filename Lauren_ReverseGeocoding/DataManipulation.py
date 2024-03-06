import pandas as pd

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

# Display the total number of rows in the DataFrame
total_rows = df.shape[0]
print(f'Total number of rows: {total_rows}')

# Filter rows based on the "Formatted Address" column
df = df[df['Formatted Address'].str.contains("USA", case=False, na=False)]

# Display the total number of rows in the DataFrame
total_rows = df.shape[0]
print(f'Total number of rows: {total_rows}')






# Display the first few rows of the DataFrame
print(df.head())
