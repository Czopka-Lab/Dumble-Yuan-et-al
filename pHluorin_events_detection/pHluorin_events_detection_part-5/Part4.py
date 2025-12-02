import numpy as np
import pandas as pd

# Load the Excel data
file_path = r'C:\x\Results\Halfwidthcalc_interpol.xlsx'
df = pd.read_excel(file_path, header=None)  # Load the data, assuming no headers

# Extract the time points as a common NumPy array
time_points = np.array(df.iloc[0, 4:], dtype=float)  # Assuming time points start from column E

# Create lists to store FWHM values for each row
fwhm_values = []

# Loop through rows starting from the second row
for row_idx in range(1, df.shape[0]):
    df_data = np.array(df.iloc[row_idx, 4:], dtype=float)

    # Find the half-maximum value
    halfmax = df_data.max() / 2

    # Find the index where the data is closest to half-maximum on the left side of the peak
    left_idx = np.where(df_data >= halfmax)[0][0]

    # Find the index where the data is closest to half-maximum on the right side of the peak
    right_idx = np.where(df_data >= halfmax)[0][-1]

    # Calculate the full width at half maximum
    fullwidthathalfmax = time_points[right_idx] - time_points[left_idx]

    fwhm_values.append(fullwidthathalfmax)

# Create a DataFrame with the FWHM values
result_df = pd.DataFrame({'Interpol_FWHM': fwhm_values})

# Define the output file path
output_folder = r'C:\x\Results'
output_file = 'Interpol_FWHM.xlsx'

# Save the DataFrame to the specified Excel file
result_df.to_excel(f"{output_folder}\\{output_file}", index=False)

print(f"Interpol_FWHM data saved to {output_folder}\\{output_file}")
