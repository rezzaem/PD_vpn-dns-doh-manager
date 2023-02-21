import json

filename = "roozaneh.txt"

with open(filename, "r") as f:
    data = f.read()

# split the data with "-"
split_data = data.split("-")

# create a dictionary with the split data
json_data = {}
for i, value in enumerate(split_data):
    key = f"item_{i+1}"
    json_data[key] = value.strip()

# save the data in a JSON file
json_filename = f"{filename.split('.')[0]}.json"
with open(json_filename, "w") as f:
    json.dump(json_data, f, indent=4)

print(f"File saved as {json_filename}")
