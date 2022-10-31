import json

def load_json_file(path):
    with open(path) as file_obj:
        return json.load(file_obj)

def write_json_to_file(path, content):
    with open(path, "w") as write_obj:
        json.dump(content, write_obj)
