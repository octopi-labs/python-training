import json


data = {
    "president": {
        "name": "\Modi",
        "species": "Gujarati",
        "list_e": [0, 1, 2]
    }
}

json_string = json.dumps(data)
print(json_string)

json_string = json.dumps(data, indent=4)
print(json_string)

json_string = json.dumps(data, indent=4, separators=(',', ':'))
print(json_string)