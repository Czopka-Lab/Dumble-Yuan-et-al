import pandas as pd

# Define the file path for the combined CSV file
combined_csv_path = r'C:\x\Results\Combined_Mean_Curves.csv'

# Read the combined CSV file into a DataFrame
combined_df = pd.read_csv(combined_csv_path)

# Define the number of blank columns to insert
num_blank_columns = 0

# Calculate the index at which to insert the blank columns (after column 3)
insert_index = 3

# Generate unique column names for the blank columns
blank_column_names = [f'Blank_Column_{i + 1}' for i in range(num_blank_columns)]

# Insert blank columns with unique names and empty data
for column_name in blank_column_names:
    combined_df.insert(insert_index, column_name, '')

# Save the modified DataFrame back to the CSV file
combined_df.to_csv(combined_csv_path, index=False)

# Print a confirmation message
print(f'Inserted {num_blank_columns} blank columns after column 3 and saved to {combined_csv_path}')
