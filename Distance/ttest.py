import pandas as pd
from scipy import stats

# Load the dataset
file_path = "Distance/AggregatedDefaultvsSemi.csv"
data = pd.read_csv(file_path)

# Define the columns for default and semiconductor water risk
default_columns = ['w_awr_def_qan_raw_0', 'w_awr_def_qal_raw_0', 'w_awr_def_rrr_raw_0', 'w_awr_def_tot_raw_0']
semiconductor_columns = ['w_awr_smc_qan_raw_1', 'w_awr_smc_qal_raw_1', 'w_awr_smc_rrr_raw_1', 'w_awr_smc_tot_raw_1']

# Calculate the mean of default and semiconductor water risk columns
default_mean = data[default_columns].mean()
semiconductor_mean = data[semiconductor_columns].mean()

print("Mean of default water risk columns:")
print(default_mean)
print("\nMean of semiconductor water risk columns:")
print(semiconductor_mean)

# Perform t-test
t_statistic, p_value = stats.ttest_ind(data[default_columns], data[semiconductor_columns])

print("\nT-test results:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)
