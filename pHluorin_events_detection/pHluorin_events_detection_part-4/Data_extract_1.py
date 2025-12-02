import csv

# Step 1: Read Event Names
results_csv_path = "C:\\x\\Results\\RAW_Results.csv"
event_names = []

with open(results_csv_path, 'r') as results_csv:
    reader = csv.reader(results_csv)
    header = next(reader)
    
    for column_name in header:
        if column_name.startswith("Mean(ID"):
            # Extract the #### part from the event name
            event_id = column_name.split("(")[1][2:-1]
            event_names.append(event_id)

# Step 2: Extract X Values
blips_info_csv_path = "C:\\x\\Results\\Threshold_Blips_info.csv"
tracks_info_csv_path = "C:\\x\\Results\\Tracks_info_complete.csv"
x_values = {}

# Extract X values from Threshold_Blips_info.csv
with open(blips_info_csv_path, 'r') as blips_csv:
    reader = csv.DictReader(blips_csv)
    
    for row in reader:
        label = row["LABEL"]
        position_t = row["POSITION_T"]
        
        # Extract the #### part from the event name
        event_id = label.split("ID")[1]
        x_values[event_id] = position_t

# Extract X values from Tracks_info_complete.csv
with open(tracks_info_csv_path, 'r') as tracks_csv:
    reader = csv.DictReader(tracks_csv)
    
    for row in reader:
        first = row["FIRST"]
        track_start = row["TRACK_START"]
        
        x_values[first] = track_start

# Step 3: Create a New CSV
output_csv_path = "C:\\x\\Results\\Mean_Curves.csv"

with open(output_csv_path, 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(["First_spot", "Commence_slice"])  # Write header row
    
    for event_id in event_names:
        if event_id in x_values:
            commence_slice = round(float(x_values[event_id])) + 0
            writer.writerow([event_id, commence_slice])

# Step 4: Display Data
with open(output_csv_path, 'r') as output_csv:
    reader = csv.reader(output_csv)
    for row in reader:
        print(row)
