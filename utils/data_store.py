import json
import os

FILE_PATH = "candidate_data.json"

def save_candidate_data(candidate):

    data = []

    # Load existing data
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as file:
                data = json.load(file)
        except:
            data = []

    # Append new candidate
    data.append(candidate)

    # Write updated data
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)