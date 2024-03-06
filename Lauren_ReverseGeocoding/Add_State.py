#pip install uszipcode
#pip install --upgrade uszipcode
# pip install uszipcode==0.2.5


import csv
from uszipcode import SearchEngine

def add_state_column(input_csv, output_csv):
    search = SearchEngine(simple_zipcode=True)

    with open(input_csv, mode='r', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['State']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            zip_code = row.get('Zip Code', '')
            
            # If zip code is available, get state information
            if zip_code:
                try:
                    zipcode = search.by_zipcode(zip_code)
                    state = zipcode.state
                    row['State'] = state
                except Exception as e:
                    print(f"Error getting state for zip code {zip_code}: {str(e)}")

            # Write the updated row to the output file
            writer.writerow(row)

if __name__ == "__main__":
    # Specify the input CSV file
    input_csv = "final_addresses_manual_edits2.csv"

    # Add the State column and create a new CSV file
    add_state_column(input_csv, "addresses_with_state.csv")
