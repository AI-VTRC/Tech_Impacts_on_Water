import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend (e.g., Agg)
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("Distance/MergedDataWRI_Baseline.csv")

# Display basic statistics
print(df.describe())

# Visualize distributions of numerical variables
sns.pairplot(df)
plt.show()

# Visualize correlations between numerical variables
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Visualize distributions of categorical variables
for col in df.select_dtypes(include='object'):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)
    plt.show()
