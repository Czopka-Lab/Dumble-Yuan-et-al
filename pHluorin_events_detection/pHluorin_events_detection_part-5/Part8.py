import numpy as np
import pandas as pd

# Load the Excel data
input_file = r'C:\x\Results\Halfwidthcalc_interpol.xlsx'
df = pd.read_excel(input_file, header=None)  # Load the data, assuming no headers

# Extract the first 4 columns
df_columns = df.iloc[:, :4]

# Create a new Excel writer object
output_file = r'C:\x\Results\FWHM.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Write the extracted columns to a new sheet named 'Sheet1'
    df_columns.to_excel(writer, sheet_name='Sheet1', index=False, header=False)

print("Columns 1-4 copied to FWHM.xlsx")

