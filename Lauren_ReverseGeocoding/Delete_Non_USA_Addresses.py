import csv

input_file = "WRI_Aqueduct_water_stress_and_semiconductors_dataset.csv"
output_file = "filtered_addresses.csv"

def filter_and_write_addresses(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write header to the output file
        writer.writeheader()

        # Iterate through rows and write only those containing "USA" in "Formatted Address"
        for row in reader:
            if "Formatted Address" in row and "USA" in row["Formatted Address"]:
                writer.writerow(row)

if __name__ == "__main__":
    filter_and_write_addresses(input_file, output_file)
