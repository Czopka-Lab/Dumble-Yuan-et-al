import pandas as pd
import os

# File paths for the source Excel files
fw_file = r'C:\x\Results\FWHM.xlsx'
gaus_file = r'C:\x\Results\Gaus_FWHM.xlsx'
interp_file = r'C:\x\Results\Interpol_FWHM.xlsx'

# Load the source Excel files
fw_df = pd.read_excel(fw_file)
gaus_df = pd.read_excel(gaus_file)
interp_df = pd.read_excel(interp_file)

# Create a new Excel writer and add a sheet
output_file = r'C:\x\Results\Calculated_FWHMs.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Copy columns 1-4 of FWHM.xlsx to columns 1-4 of the new sheet
    fw_df.iloc[:, :4].to_excel(writer, sheet_name='Sheet1', index=False)

    # Copy columns 1-2 of Gaus_FWHM.xlsx to columns 5-6 of the new sheet
    gaus_df.iloc[:, :2].to_excel(writer, sheet_name='Sheet1', startcol=4, index=False)

    # Copy column 1 of Interpol_FWHM.xlsx to column 7 of the new sheet
    interp_df.iloc[:, :1].to_excel(writer, sheet_name='Sheet1', startcol=6, index=False)

print(f"Data copied and saved to {output_file}")

# Delete the original files
os.remove(fw_file)
os.remove(gaus_file)
os.remove(interp_file)

print("Original files deleted.")
