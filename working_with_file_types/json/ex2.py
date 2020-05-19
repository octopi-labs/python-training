'''
Write json in file
'''


import os
import json


data = {
    "president": {
        "name": "\Modi",
        "species": "Gujarati",
        'list_e': [0, 1, 2, 3]
    }
}

current_dir = os.path.dirname(__file__)
filename = "data_file.json" 
with open(current_dir + os.sep + filename, "w") as write_file:
    json.dump(data, write_file)