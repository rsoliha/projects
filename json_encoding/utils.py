import json

def load_json(file_path: str):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data

def save_json(file_path: str, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
