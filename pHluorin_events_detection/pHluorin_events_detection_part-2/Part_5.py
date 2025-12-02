import os
import zipfile
import shutil

# This script identifies and lists files in a directory, compresses specific folders into ZIP files,
# and deletes the original folders (excluding specified files from deletion) in the 'Results' directory.


# Task 1: List all files in the directory except specified files
directory_path = r'C:\x\Results'
exclude_files = ['Heir.csv', 'Spots.csv', 'Tracks.csv', 'RoiSet.zip']
files_to_delete = [f for f in os.listdir(directory_path) if f not in exclude_files]

# Print the list of files to delete
print("Files to delete:")
for file in files_to_delete:
    print(file)

# Task 2: Compress "BlipRoiSet" and "TrackRoiSet" folders into ZIP files
folder_paths = [
    r'C:\x\Results\BlipRoiSet',
    r'C:\x\Results\TrackRoiSet'
]

for folder_path in folder_paths:
    folder_name = os.path.basename(folder_path)
    zip_file_path = os.path.join(os.path.dirname(folder_path), folder_name + '.zip')

    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

    print(f"{folder_name} folder has been compressed to {zip_file_path}")

# Task 3: Delete the original "BlipRoiSet" and "TrackRoiSet" folders
folders_to_delete = [
    r'C:\x\Results\BlipRoiSet',
    r'C:\x\Results\TrackRoiSet'
]

for folder_path in folders_to_delete:
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted {folder_path}")
    else:
        print(f"{folder_path} does not exist")
