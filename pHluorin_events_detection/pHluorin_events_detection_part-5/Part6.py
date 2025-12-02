import os

# Folder path where the files are located
folder_path = r'C:\x\Results'

# List of file names to delete
files_to_delete = ['FWHM.xlsx', 'Gaus_FWHM.xlsx', 'Interpol_FWHM.xlsx', 'Halfwidthcalc_interpol.xlsx']

# Delete the files
for file_name in files_to_delete:
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_name}")
    else:
        print(f"{file_name} not found")

print("Deletion completed.")
