import os
import shutil

# Define the directory path
directory_path = r'C:\x\Results'

# List of files to exclude from deletion
files_to_exclude = ['Heir.csv', 'Spots.csv', 'Tracks.csv', 'RoiSet.zip']

# Get a list of all files in the directory
all_files = os.listdir(directory_path)

# Iterate through the files and remove those not in the exclusion list
for filename in all_files:
    if filename not in files_to_exclude:
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

print("Files removed successfully.")
