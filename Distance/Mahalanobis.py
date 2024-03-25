import pandas as pd
import numpy as np
from scipy.spatial import distance

# File path
file_path = "Distance/MergedDataWRI_Baseline.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Select columns matching the specified patterns
semiconductor_columns = [col for col in data.columns if '_cat1' in col]
non_semiconductor_columns = [col for col in data.columns if '_cat' in col and '_cat1' not in col]

# Separate the dataset into semiconductor and non-semiconductor data
semiconductor_data = data[semiconductor_columns]
non_semiconductor_data = data[non_semiconductor_columns]

# Calculate the mean of semiconductor and non-semiconductor data
semiconductor_mean = semiconductor_data.mean().values
non_semiconductor_mean = non_semiconductor_data.mean().values

# Calculate the covariance matrices of semiconductor and non-semiconductor data
semiconductor_cov_matrix = np.cov(semiconductor_data.values, rowvar=False)
non_semiconductor_cov_matrix = np.cov(non_semiconductor_data.values, rowvar=False)

# Invert the covariance matrices
semiconductor_inv_cov_matrix = np.linalg.inv(semiconductor_cov_matrix)
non_semiconductor_inv_cov_matrix = np.linalg.inv(non_semiconductor_cov_matrix)

# Define a function to calculate Mahalanobis distance for a single point
def mahalanobis_distance(x, mean, inv_cov_matrix):
    diff = x - mean
    return np.sqrt(np.dot(np.dot(diff, inv_cov_matrix), diff.T))

# Calculate Mahalanobis distance for each data point in semiconductor and non-semiconductor data
semiconductor_mahalanobis_distances = []
non_semiconductor_mahalanobis_distances = []

for index, row in data.iterrows():
    semiconductor_distance = mahalanobis_distance(row[semiconductor_columns].values, semiconductor_mean, semiconductor_inv_cov_matrix)
    semiconductor_mahalanobis_distances.append(semiconductor_distance)
    
    non_semiconductor_distance = mahalanobis_distance(row[non_semiconductor_columns].values, non_semiconductor_mean, non_semiconductor_inv_cov_matrix)
    non_semiconductor_mahalanobis_distances.append(non_semiconductor_distance)

# Add the calculated distances to the dataframe
data['Semiconductor_Mahalanobis_Distance'] = semiconductor_mahalanobis_distances
data['Non_Semiconductor_Mahalanobis_Distance'] = non_semiconductor_mahalanobis_distances

# Print or use the Mahalanobis distances as needed
print("Semiconductor Mahalanobis distances:", semiconductor_mahalanobis_distances)
print("Non-Semiconductor Mahalanobis distances:", non_semiconductor_mahalanobis_distances)

# You can also save the modified dataframe to a new CSV file if needed
data.to_csv("Distance/MergedDataWRI_Baseline_with_distances.csv", index=False)
