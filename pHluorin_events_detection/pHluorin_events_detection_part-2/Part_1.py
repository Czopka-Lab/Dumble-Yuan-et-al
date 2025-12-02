
# This script performs data processing on CSV files (Heir.csv, Spots.csv, Tracks.csv):
# It skips header rows, selects specific columns, and saves the modified data into new CSV files (Heir_edited.csv, Spots_edited.csv, Tracks_edited.csv).

import pandas as pd
import os

# Define the file paths for Heir.csv, Heir_edited.csv, Spots.csv, Spots_edited.csv, Tracks.csv, and Tracks_edited.csv
heir_file = r'C:\x\Results\Heir.csv'
heir_edited_file = r'C:\x\Results\Heir_edited.csv'
spots_file = r'C:\x\Results\Spots.csv'
spots_edited_file = r'C:\x\Results\Spots_edited.csv'
tracks_file = r'C:\x\Results\Tracks.csv'
tracks_edited_file = r'C:\x\Results\Tracks_edited.csv'

# Check if the old Heir_edited.csv file exists and delete it if it does
if os.path.exists(heir_edited_file):
    os.remove(heir_edited_file)

# Load the Heir.csv file
heir_df = pd.read_csv(heir_file)

# Remove the first column
heir_df = heir_df.iloc[:, 1:]

# Remove the first two rows
heir_df = heir_df.iloc[2:]

# Remove the second row
heir_df = heir_df.iloc[1:]

# Keep only columns 1, 4, 5, 6, 7, 8, and 9
heir_df = heir_df.iloc[:, [0, 3, 4, 5, 6, 7, 8]]

# Save the modified DataFrame as Heir_edited.csv
heir_df.to_csv(heir_edited_file, index=False)

# Display the first few rows of the modified Heir DataFrame
print("Heir Data:")
print(heir_df.head())

# Check if the old Spots_edited.csv file exists and delete it if it does
if os.path.exists(spots_edited_file):
    os.remove(spots_edited_file)

# Load the Spots.csv file
spots_df = pd.read_csv(spots_file)

# Remove the first two rows
spots_df = spots_df.iloc[2:]

# Remove the second row
spots_df = spots_df.iloc[1:]

# Keep only columns 1, 3, 5, 6, 8, 13, and 16
spots_df = spots_df.iloc[:, [0, 2, 4, 5, 7, 12, 15]]

# Save the modified Spots DataFrame as Spots_edited.csv
spots_df.to_csv(spots_edited_file, index=False)

# Display the first few rows of the modified Spots DataFrame
print("\nSpots Data:")
print(spots_df.head())

# Check if the old Tracks_edited.csv file exists and delete it if it does
if os.path.exists(tracks_edited_file):
    os.remove(tracks_edited_file)

# Load the Tracks.csv file
tracks_df = pd.read_csv(tracks_file)

# Remove the first two rows
tracks_df = tracks_df.iloc[2:]

# Remove the second row
tracks_df = tracks_df.iloc[1:]

# Keep only columns 2, 4, 10, 11, 12, 13, 14, 15
tracks_df = tracks_df.iloc[:, [1, 3, 9, 10, 11, 12, 13, 14]]

# Save the modified Tracks DataFrame as Tracks_edited.csv
tracks_df.to_csv(tracks_edited_file, index=False)

# Display the first few rows of the modified Tracks DataFrame
print("\nTracks Data:")
print(tracks_df.head())

