import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged dataset
file_path = "MergeDatasets/MergedDataWRI_Baseline.csv"
data = pd.read_csv(file_path)

# Select relevant columns for clustering
relevant_columns = ['latitude', 'longitude', 'major_basin_name', 'minor_basin_name', 'bws_cat1', 'w_awr_tex_tot_cat']
data_for_clustering = data[relevant_columns]

# Drop rows with missing values
data_for_clustering = data_for_clustering.dropna()

# Perform k-means clustering
k = 3  # number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
data_for_clustering['cluster'] = kmeans.fit_predict(data_for_clustering[['latitude', 'longitude']])

# Define cluster labels or descriptions
cluster_descriptions = {
    0: 'Cluster 0 Description',
    1: 'Cluster 1 Description',
    2: 'Cluster 2 Description'
}

data_for_clustering['cluster_label'] = data_for_clustering['cluster'].map(cluster_descriptions)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='longitude', y='latitude', data=data_for_clustering, hue='cluster_label', palette='viridis', legend='full')
plt.title('K-Means Clustering of Facility Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Identify variable importance using cluster centers (centroids)
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=['latitude', 'longitude'])
cluster_centers['cluster'] = range(k)
print("Cluster Centers (Centroids):")
print(cluster_centers)

# Visualize variable importance
plt.figure(figsize=(10, 6))
sns.barplot(x=cluster_centers['cluster'], y=cluster_centers['latitude'], color='skyblue', label='Latitude')
sns.barplot(x=cluster_centers['cluster'], y=cluster_centers['longitude'], color='orange', label='Longitude')
plt.title('Variable Importance: Cluster Centers (Centroids)')
plt.xlabel('Cluster')
plt.ylabel('Mean Value')
plt.legend()
plt.show()

# Suggested variables for an AI model based on importance determined by clustering
suggested_variables = ['major_basin_name', 'minor_basin_name', 'bws_cat1', 'w_awr_tex_tot_cat']
print("\nSuggested Variables for an AI Model based on Importance Determined by Clustering:")
print(suggested_variables)

# Count of facilities under each water basin
facility_counts = data.groupby(['major_basin_name', 'minor_basin_name']).size().reset_index(name='facility_count')
print("\nFacilities Count under Each Water Basin:")
print(facility_counts)
