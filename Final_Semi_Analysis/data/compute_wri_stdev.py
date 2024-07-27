import pandas as pd
import numpy as np

# Load the dataset
file_path = 'C:/Users/laure/Documents/Tech_Impacts_on_Water/Final_Semi_Analysis/data/balanced_data_with_lat_lon.csv'
data = pd.read_csv(file_path)

# Function to calculate standard deviation for pairs of rows within the same state
def calculate_std_wris(data):
    wris = ['bws_raw', 'bwd_raw', 'iav_raw', 'sev_raw', 'gtd_raw', 'rfr_raw', 'drr_raw', 'cep_raw', 'udw_raw', 'usa_raw']
    std_columns = {f'std_{wri}': [] for wri in wris}
    std_columns['index'] = []
    std_columns['state'] = []
    
    grouped = data.groupby('state')
    for state, group in grouped:
        group_0 = group[group['presence_absence'] == 0].reset_index()
        group_1 = group[group['presence_absence'] == 1].reset_index()
        num_rows = min(group_0.shape[0], group_1.shape[0])
        for i in range(num_rows):
            row1 = group_0.iloc[i]
            row2 = group_1.iloc[i]
            # Ensure rows are in the correct format and handle NaN values
            row1_wris = row1[wris].astype(float).fillna(0)
            row2_wris = row2[wris].astype(float).fillna(0)
            std_devs = np.std([row1_wris, row2_wris], axis=0)
            for j, wri in enumerate(wris):
                std_columns[f'std_{wri}'].append(std_devs[j])
            std_columns['index'].append(row2['index'])
            std_columns['state'].append(state)
    
    std_df = pd.DataFrame(std_columns)
    return std_df

# Calculate the standard deviations for WRI columns
std_wris_df = calculate_std_wris(data)

# Merge the standard deviations back to the original data
data_std = pd.merge(data.reset_index(), std_wris_df, on=['index', 'state'], how='left')

# Save the merged dataframe to a new CSV file
data_std.to_csv('C:/Users/laure/Documents/Tech_Impacts_on_Water/Final_Semi_Analysis/data/balanced_data_with_lat_lon_stdev.csv', index=False)
print("Merged data has been saved to 'balanced_data_with_lat_lon_stdev.csv'")
