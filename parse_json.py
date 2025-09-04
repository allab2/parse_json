import json

# Step 1: Open and read the JSON file
with open("events.json", "r") as f:
    data = json.load(f)   # data is now a Python list of dictionaries

# Step 2: Create a dictionary to hold country summaries
summary = {}

# Step 3: Loop through each record in the data
for event in data:
    country = event["country"]
    imps = event["imps"]
    clicks = event["clicks"]

    # If country not seen before, initialize
    if country not in summary:
        summary[country] = {"users": 0, "imps": 0, "clicks": 0}

    # Update counts
    summary[country]["users"] += 1
    summary[country]["imps"] += imps
    summary[country]["clicks"] += clicks

# Step 4: Print the summary
print("--- Summary by Country ---")
for country, stats in summary.items():
    print(f"{country} => Users: {stats['users']}, Imps: {stats['imps']}, Clicks: {stats['clicks']}")
