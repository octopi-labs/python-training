'''
Load json from file
'''


import os
import json
import pprint

current_dir = os.path.dirname(__file__)
filename = "data_file.json" 
with open(current_dir + os.sep + filename, "r") as read_file:
    content = read_file.read()
    json_obj = json.loads(content)
    print(content)
    pprint.pprint(json_obj)