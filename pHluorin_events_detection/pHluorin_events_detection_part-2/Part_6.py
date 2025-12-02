# This script Max and Mean intensity of the first spots of tracks to tracks_info.
# It then saves the result as "Tracks_info_complete.csv" in the specified directory.


import pandas as pd

# Define the directory and file names
directory = r'C:\x\Results'
tracks_info_file = 'Tracks_info.csv'
spots_edited_file = 'Spots_edited.csv'

# Create file paths
tracks_info_path = f'{directory}\\{tracks_info_file}'
spots_edited_path = f'{directory}\\{spots_edited_file}'

# Load CSV files into DataFrames
tracks_info_df = pd.read_csv(tracks_info_path)
spots_edited_df = pd.read_csv(spots_edited_path)

# Define a dictionary to store matching values from Spots_edited
matching_data = {}

# Iterate through Spots_edited DataFrame
for index, row in spots_edited_df.iterrows():
    spot_id = row.iloc[0]  # Assuming the first column is the spot ID (e.g., "ID2027")
    matching_value = spot_id[2:]  # Extract the numeric part (e.g., "2027")
    
    # Check if the matching_value exists in Tracks_info DataFrame
    if matching_value in tracks_info_df['FIRST'].astype(str).str.replace("ID", "").values:
        # If there's a match, store the data in the dictionary
        matching_data[matching_value] = (row['MEAN_INTENSITY_CH1'], row['MAX_INTENSITY_CH1'])

# Fill in the new columns in Tracks_info based on the matching_data dictionary
tracks_info_df['FIRST_MEAN'] = ''
tracks_info_df['FIRST_MAX'] = ''

for index, row in tracks_info_df.iterrows():
    match_value = str(row['FIRST']).replace("ID", "")  # Convert to string and then adjust 'FIRST' to your actual column name
    
    # Check if there's matching data in the dictionary
    if match_value in matching_data:
        data = matching_data[match_value]
        tracks_info_df.at[index, 'FIRST_MEAN'] = data[0]
        tracks_info_df.at[index, 'FIRST_MAX'] = data[1]

# Save the modified Tracks_info DataFrame to the specified file path
output_file = r'C:\x\Results\Tracks_info_complete.csv'
tracks_info_df.to_csv(output_file, index=False)

# Print the modified Tracks_info DataFrame
print(tracks_info_df)
