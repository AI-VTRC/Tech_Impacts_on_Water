import pandas as pd
from scipy.stats import chi2_contingency

# Load the dataset
file_path = "Distance/MergedDataWRI_Baseline.csv"
df = pd.read_csv(file_path)

# Select the categorical columns ending in _cat1 and _cat
cat1_cols = [col for col in df.columns if col.endswith('_cat1')]
cat_cols = [col for col in df.columns if col.endswith('_cat')]

# Initialize a dictionary to store the results
results = {}

# Iterate over all pairs of _cat1 and _cat columns
for cat1_col in cat1_cols:
    for cat_col in cat_cols:
        # Create a contingency table for the current pair of columns
        contingency_table = pd.crosstab(df[cat1_col], df[cat_col])
        
        # Perform the chi-square test
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
        
        # Store the results in the dictionary
        results[(cat1_col, cat_col)] = {'Chi-square': chi2, 'P-value': p_value, 'Degrees of Freedom': dof}

# Print or analyze the results as needed
for pair, result in results.items():
    print(f"Chi-square test for {pair}:")
    print("  Chi-square:", result['Chi-square'])
    print("  P-value:", result['P-value'])
    print("  Degrees of Freedom:", result['Degrees of Freedom'])
    print()
