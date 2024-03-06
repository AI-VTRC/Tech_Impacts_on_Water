import csv

def filter_states(input_csv, output_csv, target_states):
    with open(input_csv, mode='r', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            state = row.get('State', '')
            
            # Check if the state is in the list of target states
            if state in target_states:
                # Write the row to the output file
                writer.writerow(row)

if __name__ == "__main__":
    # Specify the input CSV file and target states
    input_csv = "addresses_with_state.csv"
    output_csv = "drought_states_data.csv"
    target_states = ['AZ', 'NM', 'TX', 'IA']

    # Filter rows based on target states and create a new CSV file
    filter_states(input_csv, output_csv, target_states)
