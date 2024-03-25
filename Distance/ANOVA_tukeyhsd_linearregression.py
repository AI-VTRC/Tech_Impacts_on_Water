import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm

# Load the dataset
file_path = "Distance/AggregatedDefaultvsSemi.csv"
data = pd.read_csv(file_path)

# Define the columns for default and semiconductor water risk indices
default_columns = ['w_awr_def_qan_raw_0', 'w_awr_def_qal_raw_0', 'w_awr_def_rrr_raw_0', 'w_awr_def_tot_raw_0']
semiconductor_columns = ['w_awr_smc_qan_raw_1', 'w_awr_smc_qal_raw_1', 'w_awr_smc_rrr_raw_1', 'w_awr_smc_tot_raw_1']

# Perform ANOVA
anova_results = f_oneway(data[default_columns], data[semiconductor_columns])
print("ANOVA Results:")
print("F-statistic:", anova_results.statistic)
print("p-value:", anova_results.pvalue)

# Perform Tukey's HSD test
default_data = data[default_columns].rename(columns=lambda x: 'Default_' + x)
semiconductor_data = data[semiconductor_columns].rename(columns=lambda x: 'Semiconductor_' + x)
stacked_data = pd.concat([default_data, semiconductor_data], axis=1)
stacked_data = stacked_data.stack().reset_index().rename(columns={0: 'value', 'level_0': 'Group', 'level_1': 'Variable'})
tukey_results = pairwise_tukeyhsd(stacked_data['value'], stacked_data['Group'])
print("\nTukey's HSD Results:")
print(tukey_results)

# Perform linear regression
X = data[semiconductor_columns]  # Independent variables
y = data['w_awr_def_tot_raw_0']  # Dependent variable
X = sm.add_constant(X)  # Add constant for intercept
model = sm.OLS(y, X).fit()  # Fit the linear regression model
print("\nLinear Regression Results:")
print(model.summary())
