# Multiply JSON objects
import json

# Read JSON object from file
with open('input.json', 'r') as file:
    json_data = json.load(file)

# Create a list to store multiplied JSON objects
multiplied_data = []

# Multiply the JSON object 100,000 times
for _ in range(25578): 
    multiplied_data.append(json_data)

# Write the multiplied JSON data to a filecode
with open('output.json', 'w') as file:
    json.dump(multiplied_data, file)

# export data

data = ["apple", "banana", "orange", "grape"]

# Open the file in write mode
with open('output.json', 'w') as file:
    # Write the list to the file in JSON format
    json.dump(data, file)
