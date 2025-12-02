import pandas as pd

# Define the file path
file_path = r'C:\x\Results\RAW_Results.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Initialize an empty dictionary to store the X values
x_values_dict = {}

# Loop through the columns to extract event names and X values
for column in df.columns:
    if 'Mean(ID' in column:
        event_name = column.split('(')[1].split(')')[0]
        x_values = df[column].tolist()
        x_values_dict[event_name] = x_values

# Create a DataFrame from the dictionary
transposed_df = pd.DataFrame(x_values_dict)

# Transpose the DataFrame horizontally
transposed_df = transposed_df.T

# Define the path to save the transposed data
output_file_path = r'C:\x\Results\Transposed_Results.csv'

# Save the transposed data to a CSV file at the specified path
transposed_df.to_csv(output_file_path)

# Print a confirmation message
print(f'Transposed data saved to {output_file_path}')
