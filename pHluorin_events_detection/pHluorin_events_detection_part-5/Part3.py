import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# Load the Excel data
file_path = r'C:\x\Results\Halfwidthcalc_interpol.xlsx'
df = pd.read_excel(file_path, header=None)  # Load the data, assuming no headers

# Initialize lists to store FWHM and R-squared values for each row
fwhm_values = []
r_squared_values = []

# Extract the time points as a common NumPy array
time_points = np.array(df.iloc[0, 4:], dtype=float)  # Assuming time points start from column E

# Loop through rows starting from the second row
for row_idx in range(1, df.shape[0]):
    df_data = np.array(df.iloc[row_idx, 4:], dtype=float)

    # Define the Gaussian function to accept NumPy arrays
    def gaussian(x, a, b, sigma):
        return a * np.exp(-(x - b)**2 / (2 * sigma**2))

    # Initial guess for curve fitting parameters
    initial_guess = [max(df_data), time_points[np.argmax(df_data)], 1]

    try:
        # Fit the Gaussian curve to the data with a higher maxfev value
        params, _ = curve_fit(gaussian, time_points, df_data, p0=initial_guess, maxfev=5000)  # Adjust maxfev as needed

        # Extract the FWHM from the curve parameters
        a, b, sigma = params
        fwhm = 2 * np.sqrt(2 * np.log(2)) * sigma

        # Calculate R-squared value
        fitted_curve = gaussian(time_points, *params)
        r_squared = r2_score(df_data, fitted_curve)
    except RuntimeError:
        # Handle cases where curve fitting fails (e.g., doesn't converge)
        fwhm = "N/A"
        r_squared = "N/A"

    fwhm_values.append(fwhm)
    r_squared_values.append(r_squared)

# Create a DataFrame with the FWHM and R-squared values
result_df = pd.DataFrame({'FWHM': fwhm_values, 'R-squared': r_squared_values})

# Define the output file path
output_folder = r'C:\x\Results'
output_file = 'Gaus_FWHM.xlsx'

# Save the DataFrame to the specified Excel file
result_df.to_excel(f"{output_folder}\\{output_file}", index=False)

print(f"Data saved to {output_folder}\\{output_file}")
