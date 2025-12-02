import pandas as pd

import os

# Folder path where the files are located
folder_path = r'C:\x\Results'
# Define the paths to your Excel files
file2 = r'C:\x\Results\Calculated_FWHMs5.xlsx'
file1 = r'C:\x\Results\Calculated_FWHMs.xlsx'

# Load the Excel files intso pandas DataFrames
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)



# Create a new Excel writer and add a sheet
output_file = r'C:\x\Results\Calculated_FWHMs_updated.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Copy columns 1-4 of FWHM.xlsx to columns 1-4 of the new sheet
    df1.iloc[:, :7].to_excel(writer, sheet_name='Sheet1', index=False)

    # Copy columns 1-2 of Gaus_FWHM.xlsx to columns 5-6 of the new sheet
    df2.iloc[:, 4:7].to_excel(writer, sheet_name='Sheet1', startcol=7, index=False)


# Delete the original files
# List of file names to delete
files_to_delete = ['Calculated_FWHMs.xlsx', 'Calculated_FWHMs5.xlsx']

# Delete the files
for file_name in files_to_delete:
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_name}")
    else:
        print(f"{file_name} not found")