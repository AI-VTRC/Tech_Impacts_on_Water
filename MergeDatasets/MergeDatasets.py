import pandas as pd

# Assuming your files are in the same directory as your script or Jupyter Notebook
file1_path = "MergeDatasets/Aqueduct_WRI_Full_PredictionBAU.csv"
file2_path = "MergeDatasets/Aqueduct_WRI_Full.csv"
output_file_path = "MergeDatasets/Test.csv"

# Read the CSV files into separate dataframes
df_prediction_bau = pd.read_csv(file1_path)
df_full = pd.read_csv(file2_path)

# Mapping between prefixes in DataFrame 2 and corresponding columns in DataFrame 1
column_mapping = {
    'major_basin_name': 'major_basin_name_prediction_bau',
    'gid_0': 'gid_0_prediction_bau',
    'gid_1': 'gid_1_prediction_bau',
    'name_0': 'name_0_prediction_bau',
    'name_1': 'name_1_prediction_bau',
    'string_id': 'string_id_prediction_bau',
    'aq30_id': 'aq30_id_prediction_bau',
    'aqid': 'aqid_prediction_bau',
}

# Rename columns in DataFrame 2 based on the mapping
df_full.rename(columns=column_mapping, inplace=True)

# Now, you can proceed with merging the dataframes as previously demonstrated
merged_df = pd.merge(df_prediction_bau, df_full, on=['latitude', 'longitude'])

# Remove duplicate columns
merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

# Print the head of the new dataframe
print(merged_df.head())




# Write the DataFrame to a CSV file
merged_df.to_csv(output_file_path, index=False)