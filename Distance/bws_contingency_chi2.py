import pandas as pd

# Load the dataset
file_path = "Distance/MergedDataWRI_Baseline.csv"
df = pd.read_csv(file_path)

# Select the categorical columns ending in _cat1 and _cat
cat1_cols = [col for col in df.columns if col.endswith('_cat1')]
cat_cols = [col for col in df.columns if col.endswith('_cat')]

# Perform crosstabulation
crosstab_result = pd.crosstab(df[cat1_cols[0]], df[cat_cols[0]])

# Display the crosstabulation result
print("Crosstabulation between", cat1_cols[0], "and", cat_cols[0], ":\n")
print(crosstab_result)
import pandas as pd
from scipy.stats import chi2_contingency

# Assuming df is your DataFrame containing the data
# and bws_cat1 and bws_cat are the columns you want to compare
# Replace 'bws_cat1' and 'bws_cat' with your actual column names

# Create a contingency table (cross-tabulation) between bws_cat1 and bws_cat
contingency_table = pd.crosstab(df['bws_cat1'], df['bws_cat'])

# Perform the chi-square test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the results
print("Chi-square test statistic:", chi2)
print("P-value:", p_value)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)
