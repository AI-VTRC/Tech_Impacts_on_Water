import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "MergeDatasets/MergedDataWRI_Baseline.csv"
data = pd.read_csv(file_path)

# Select relevant columns (latitude, longitude, and columns bws_cat1 through w_awr_tex_tot_cat)
selected_columns = ['latitude', 'longitude'] + list(data.columns[data.columns.get_loc('bws_cat1'):data.columns.get_loc('w_awr_tex_tot_cat') + 1])
selected_data = data[selected_columns]

# Calculate correlation between latitude, longitude, and selected variables
correlation_matrix = selected_data.corr()

# Generate a heatmap without annotations
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, cmap='coolwarm', linewidths=.5, cbar_kws={'label': 'Correlation'})
plt.title("Correlation Matrix Heatmap")

# Keep labels on the sides
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()

# Determine important variables based on correlation
threshold = 0.5  # You can adjust the threshold as needed
important_variables = correlation_matrix[(correlation_matrix['latitude'].abs() > threshold) | (correlation_matrix['longitude'].abs() > threshold)]

# Print important variables
print("\nImportant Variables:")
print(important_variables)

# Count facilities under each water basin
facilities_count = data.groupby(['major_basin_name', 'minor_basin_name']).size().reset_index(name='facility_count')

# Print the count of facilities under each water basin
print("\nFacilities Count Under Each Water Basin:")
print(facilities_count)
