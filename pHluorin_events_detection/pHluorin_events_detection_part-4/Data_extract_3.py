import pandas as pd
import os

# Define the directory path
directory_path = r'C:\x\Results'

# Define the file names
mean_curves_file = 'Mean_Curves.csv'
transposed_results_file = 'Transposed_Results.csv'

# Define the file paths
mean_curves_path = f'{directory_path}\\{mean_curves_file}'
transposed_results_path = f'{directory_path}\\{transposed_results_file}'

# Read the Mean_Curves.csv into a DataFrame
mean_curves_df = pd.read_csv(mean_curves_path)

# Read the Transposed_Results.csv into a DataFrame
transposed_results_df = pd.read_csv(transposed_results_path)

# Append Transposed_Results.csv to Mean_Curves.csv
combined_df = pd.concat([mean_curves_df, transposed_results_df], axis=1)

# Save the combined data to a new CSV file
combined_csv_path = f'{directory_path}\\Combined_Mean_Curves.csv'
combined_df.to_csv(combined_csv_path, index=False)

# Print a confirmation message
print(f'Combined data saved to {combined_csv_path}')

# Delete the source files
os.remove(mean_curves_path)
os.remove(transposed_results_path)

print('Source files deleted.')
