import pandas as pd
import os
import shutil

# This script processes CSV data from 'Spots_edited.csv' by filtering rows based on empty cells in the second column, 
# saving the filtered data to 'Spots_edited_non_track_events.csv', and copying associated .roi files to 'BlipRoiSet' folder.


# File path for Spots_edited.csv
spots_edited_file = r'C:\x\Results\Spots_edited.csv'

# Load Spots_edited.csv into a DataFrame
spots_df = pd.read_csv(spots_edited_file)

# Function to check if a cell in the second column is empty
def is_empty(cell):
    if pd.isna(cell):
        return True
    elif isinstance(cell, str) and cell.strip() == "":
        return True
    return False

# Filter the DataFrame to keep rows where the second column is empty
filtered_spots_df = spots_df[spots_df.iloc[:, 1].apply(is_empty)]

# Print the resulting DataFrame
print(filtered_spots_df)

# Define the file path for the output CSV file
output_csv_file = r'C:\x\Results\Spots_edited_non_track_events.csv'

# Save the filtered DataFrame to the CSV file
filtered_spots_df.to_csv(output_csv_file, index=False)

# Print a message to confirm the save
print(f"Filtered data saved to {output_csv_file}")

# File path for the filtered CSV file
filtered_csv_file = r'C:\x\Results\Spots_edited_non_track_events.csv'

# Load the filtered CSV into a DataFrame
filtered_df = pd.read_csv(filtered_csv_file)

# Create a list from column 1 (excluding the first value)
column1_list = filtered_df.iloc[0:, 0].tolist()

# Print the resulting list
print(column1_list)

import os
import shutil

# Define the source folder containing .roi files
source_roi_folder = r'C:\x\Results\RoiSet'

# Define the destination folder for the .roi files
destination_roi_folder = r'C:\x\Results\BlipRoiSet'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_roi_folder):
    os.makedirs(destination_roi_folder)

# Loop through each string in the list
for string in column1_list:
    # Extract the numeric part from the string
    number = string[2:]  # Assuming all IDs have the same format
    
    # Construct the source .roi filename
    source_filename = f"ID{int(number):04d}.roi"
    
    # Construct the full source and destination paths
    source_path = os.path.join(source_roi_folder, source_filename)
    destination_path = os.path.join(destination_roi_folder, source_filename)
    
    # Check if the source .roi file exists and copy it to the destination
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)

# Print a message to confirm the transfer
print(f"Transferred {len(column1_list)} .roi files to {destination_roi_folder}")
