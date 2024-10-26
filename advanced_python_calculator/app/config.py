# app/config.py

import json
import os

def load_config(filepath='config.json'):
    """Load configuration settings from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Configuration file '{filepath}' not found.")
    with open(filepath, 'r') as file:
        return json.load(file)

# Example content of config.json
# {
#     "setting1": "value1",
#     "setting2": "value2"
# }
