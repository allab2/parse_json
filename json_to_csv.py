import json
import csv

# Step 1: Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)   # this becomes a list of dictionaries

# Step 2: Write to CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())  # use keys as headers
    writer.writeheader()
    writer.writerows(data)

print("JSON converted to output.csv")
