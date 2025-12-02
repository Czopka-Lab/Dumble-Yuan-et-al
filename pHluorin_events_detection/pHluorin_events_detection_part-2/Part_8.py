import os
import shutil

# Define the source directory
source_directory = r'C:\x\Results'

# Create a target directory for other files
other_directory = os.path.join(source_directory, 'Other_files')

# Ensure the target directory exists or create it
os.makedirs(other_directory, exist_ok=True)

# List all files in the source directory
files = os.listdir(source_directory)

# Define the CSV files to keep
csv_files_to_keep = [
    'Threshold_Blips_info.csv',
    'Tracks_info_complete.csv',
    'Heir.csv',
    'Spots.csv',
    'Tracks.csv'
]

# Define the ZIP files to keep
zip_files_to_keep = [
    'ThresholdBlipRoiSet.zip',
    'TrackRoiSet.zip',
    'RoiSet.zip'
]

# Move files not in the CSV keep list or ZIP keep list to the "Other_files" directory
for file in files:
    file_extension = os.path.splitext(file)[1]
    if (file_extension == '.csv' and file not in csv_files_to_keep) or \
       (file_extension == '.zip' and file not in zip_files_to_keep) or \
       (file_extension not in ['.csv', '.zip']):
        source_path = os.path.join(source_directory, file)
        target_path = os.path.join(other_directory, file)
        if os.path.isfile(source_path):  # Check if it's a file before moving
            shutil.move(source_path, target_path)

print(f"Moved files to '{other_directory}'")
