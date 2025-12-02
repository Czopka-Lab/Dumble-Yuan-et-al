import pandas as pd
import os

# This script loads, sorts, and combines CSV data from 'Heir_edited.csv' and 'Tracks_edited.csv' files, 
# saving the sorted results in new CSV files and combining them into 'Tracks_info.csv'.

# File paths for Heir_edited.csv and Tracks_edited.csv
heir_edited_file = r'C:\x\Results\Heir_edited.csv'
tracks_edited_file = r'C:\x\Results\Tracks_edited.csv'

# Load Heir_edited.csv into a DataFrame
heir_df = pd.read_csv(heir_edited_file)

# Load Tracks_edited.csv into a DataFrame
tracks_df = pd.read_csv(tracks_edited_file)

# Sort Heir DataFrame by column 1
heir_df = heir_df.iloc[heir_df.iloc[:, 0].argsort()]

# Sort Tracks DataFrame by column 1
tracks_df = tracks_df.iloc[tracks_df.iloc[:, 0].argsort()]

# Save the sorted DataFrames back to CSV files
heir_sorted_file = r'C:\x\Results\Heir_edited_sorted.csv'
tracks_sorted_file = r'C:\x\Results\Tracks_edited_sorted.csv'

heir_df.to_csv(heir_sorted_file, index=False)
tracks_df.to_csv(tracks_sorted_file, index=False)

# File paths for Heir_edited_sorted.csv and Tracks_edited_sorted.csv
heir_sorted_file = r'C:\x\Results\Heir_edited_sorted.csv'
tracks_sorted_file = r'C:\x\Results\Tracks_edited_sorted.csv'

# Load Heir_edited_sorted.csv into a DataFrame
heir_df = pd.read_csv(heir_sorted_file)

# Load Tracks_edited_sorted.csv into a DataFrame
tracks_df = pd.read_csv(tracks_sorted_file)

# Concatenate the two DataFrames horizontally (along columns)
combined_df = pd.concat([heir_df, tracks_df], axis=1)

# Define the file path for Tracks_info.csv
track_info_file = r'C:\x\Results\Tracks_info.csv'

# Save the combined DataFrame as Tracks_info.csv
combined_df.to_csv(track_info_file, index=False)


