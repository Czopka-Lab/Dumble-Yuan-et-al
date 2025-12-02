import os
import zipfile
import pandas as pd

# Define the file path for Spots_edited_non_track_events.csv
spots_file_path = r'C:\x\Results\Spots_edited_non_track_events.csv'

# Load the CSV file into a DataFrame
spots_df = pd.read_csv(spots_file_path)

# Define threshold values
mean_intensity_threshold = 0.15 
max_intensity_threshold = 0.3

# Filter rows based on the threshold conditions
filtered_df = spots_df[(spots_df['MEAN_INTENSITY_CH1'] > mean_intensity_threshold) & (spots_df['MAX_INTENSITY_CH1'] > max_intensity_threshold)]

# Sort the filtered DataFrame from largest to smallest based on the "MEAN_INTENSITY_CH1" column
sorted_df = filtered_df.sort_values(by='MEAN_INTENSITY_CH1', ascending=False)

# Save the sorted DataFrame as "Threshold_Blips_info.csv" in the same folder
output_file = r'C:\x\Results\Threshold_Blips_info.csv'
sorted_df.to_csv(output_file, index=False)

# Print the sorted DataFrame
print(sorted_df)

# Directory paths for RoiSet and ZIP output
roi_set_directory = r'C:\x\Results\RoiSet'
output_directory = r'C:\x\Results'
zip_file_name = 'ThresholdBlipRoiSet.zip'

# Read values from the first column of the CSV file
filenames_to_include = sorted_df.iloc[:, 0].astype(str).tolist()

# Create a ZIP file for the selected .roi files
with zipfile.ZipFile(os.path.join(output_directory, zip_file_name), 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(roi_set_directory):
        for filename in files:
            if filename.endswith(".roi"):
                # Remove ".roi" extension from the filename
                roi_name = os.path.splitext(filename)[0]
                if roi_name in filenames_to_include:
                    file_path = os.path.join(root, filename)
                    arcname = os.path.relpath(file_path, roi_set_directory)
                    zipf.write(file_path, arcname)

print(f'ZIP file "{zip_file_name}" created in "{output_directory}"')
