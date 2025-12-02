import pandas as pd
import os
import zipfile
import shutil


# This script extracts files from a ZIP archive, loads a CSV file, extracts specific values from one of its columns, 
# and then copies corresponding files from one folder to another based on those values.

# File path for Tracks_info.csv
tracks_info_file = r'C:\x\Results\Tracks_info.csv'

# File path for RoiSet.zip
roi_zip_file = r'C:\x\Results\RoiSet.zip'

# Extract the contents of RoiSet.zip into a folder
extracted_folder = r'C:\x\Results\RoiSet'

with zipfile.ZipFile(roi_zip_file, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

# Load Tracks_info.csv into a DataFrame
track_info_df = pd.read_csv(tracks_info_file)

# Select and display the sixth column (assuming it's at index 5)
column_six = track_info_df.iloc[:, 5]

# Convert the column to a Python list
Track_start_roi = column_six.tolist()

# Now, 'Track_start_roi' contains the values from the sixth column as a list
print(Track_start_roi)

# Destination folder for the .roi files
destination_folder = r'C:\x\Results\TrackRoiSet'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through each number in Track_start_roi
for number in Track_start_roi:
    # Construct the source .roi filename
    source_filename = f"ID{number:04d}.roi"
    
    # Construct the full source and destination paths
    source_path = os.path.join(extracted_folder, source_filename)  # Corrected variable name
    destination_path = os.path.join(destination_folder, source_filename)
    
    # Check if the source .roi file exists and copy it to the destination
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
