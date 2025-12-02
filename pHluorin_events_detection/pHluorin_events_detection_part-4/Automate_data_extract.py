import os
import subprocess

# Define the folder where the scripts are located
script_folder = r'C:\x\Scripts_Raw_to_curve_data'
# Get a list of all Python script files (Data_extract_#.py) in the folder
script_files = [file for file in os.listdir(script_folder) if file.startswith('Data_extract_') and file.endswith('.py')]

# Sort the script files to ensure they run in order
script_files.sort()

# Run each script in order
for script_file in script_files:
    script_path = os.path.join(script_folder, script_file)
    subprocess.run(['python', script_path])
