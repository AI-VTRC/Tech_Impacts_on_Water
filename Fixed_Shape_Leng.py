import csv

def create_basin_dict(csv_file):
    basin_dict = {}
    with open(csv_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            basin_id = row.get('BasinID')
            shape_leng = row.get('Shape_Leng')
            if basin_id and shape_leng:
                basin_dict[basin_id] = shape_leng
    return basin_dict

def update_shape_leng(input_csv, output_csv, basin_dict):
    with open(input_csv, mode='r', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            basin_id = row.get('BasinID')
            if basin_id in basin_dict:
                # Update the Shape_Leng field
                row['Shape_Leng'] = basin_dict[basin_id]

            # Write the updated row to the output file
            writer.writerow(row)

if __name__ == "__main__":
    # Specify the input CSV files
    aqueduct_csv = "WRI_Aqueduct_water_stress_and_semiconductors_dataset.csv"
    addresses_csv = "final_addresses_manual_edits.csv"

    # Create the BasinID to Shape_Leng dictionary
    basin_dict = create_basin_dict(aqueduct_csv)

    # Update the Shape_Leng field in the addresses CSV
    update_shape_leng(addresses_csv, "updated_addresses.csv", basin_dict)
