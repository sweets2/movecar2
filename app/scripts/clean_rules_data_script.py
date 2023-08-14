"""This script is used to convert the raw Hoboken street cleaning data into
a dictionary in a JSON file. We run both the "scrape_website_hoboken" file
and this file manually to make sure the rules are correct and accurate.
If the rules are wrong in any way, this whole app is useless."""
import os
import json

# Get the absolute path of the current script to output into the "data_raw" folder
current_script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(current_script_path)
project_dir = os.path.dirname(script_dir)
raw_data_dir = os.path.join(project_dir, 'data_raw')
raw_data_file_dir = os.path.join(raw_data_dir, 'new_hoboken_rules_output.txt') # raw street data file
data_dir = os.path.join(project_dir, 'data')
parsed_hoboken_rules = os.path.join(data_dir, 'parsed_hoboken_rules.json') # parsed street cleaning data in json

def txt_to_json(txt_file_path, json_file_path):
    keys = []
    data = []

    with open(txt_file_path, 'r') as txt_file:
        lines = [line.strip() for line in txt_file.readlines()]

        # Extract keys from first 4 rows of data
        keys = lines[:4]

        # Group every 4 lines as values and map them to keys
        for i in range(4, len(lines), 4):
            entry = dict(zip(keys, lines[i:i+4]))
            data.append(entry)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


txt_to_json(raw_data_file_dir, parsed_hoboken_rules)
print(f"Data from {raw_data_file_dir} has been converted to JSON and saved as {parsed_hoboken_rules}")