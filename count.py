import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('final_addresses.csv')

# Find and count the blank lines in the 'County' column
blank_county_rows = df[df['County'].isnull()]

# Print the total number of blanks
total_blanks = len(blank_county_rows)
print(f"Total number of blanks in 'County' column: {total_blanks}\n")

# Remove duplicate ZIP codes and print for each blank 'County' row
unique_zip_codes = set()
for index, row in blank_county_rows.iterrows():
    zip_code_str = str(int(row['Zip Code']))  # Convert to int and then to string
    unique_zip_codes.add(zip_code_str)

# Print the unique ZIP codes
print("Unique ZIP Codes:")
for zip_code_str in unique_zip_codes:
    print(f"{zip_code_str}")
