import pandas as pd

# Assuming the file is in the same directory as your script or Jupyter Notebook
file_path = "MergeDatasets/SemiconductorFacilities.csv"

# Read the CSV file into a pandas dataframe
semiconductor_df = pd.read_csv(file_path)

# Delete rows where "Existing_Announced" column does not contain "Announced New Project"
semiconductor_df = semiconductor_df[semiconductor_df['Existing_Announced'].str.contains('Announced New Project')]

# Drop the "Source" column
semiconductor_df = semiconductor_df.drop(columns=['Source'])

# Save the updated dataframe to the CSV file
semiconductor_df.to_csv("MergeDatasets/SemiconductorFacilities_updated.csv", index=False)

# Print the dataframe
print(semiconductor_df)
