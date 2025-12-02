import os
import subprocess

# Define the folder where the scripts are located
script_folder = r'C:\x\FWHM scripts'

# Get a list of all Python script files (Part_#.py) in the folder
script_files = [file for file in os.listdir(script_folder) if file.startswith('Part') and file.endswith('.py')]

# Sort the script files based on the numeric part of the filenames
script_files.sort(key=lambda x: int(x[len('Part'):x.index('.py')]))

# Run each script in order
for script_file in script_files:
    script_path = os.path.join(script_folder, script_file)
    subprocess.run(['python', script_path])
