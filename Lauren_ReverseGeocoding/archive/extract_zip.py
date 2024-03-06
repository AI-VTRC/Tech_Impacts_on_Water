import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('filtered_addresses.csv')

# Extract all occurrences of 5 consecutive digits and take the last one as the zip code
df['Zip Code'] = df['Formatted Address'].str.findall(r'\b(\d{5})\b').apply(lambda x: x[-1] if x else None)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_addresses.csv', index=False)
