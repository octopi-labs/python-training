'''
Write json in file
'''


import os
import json
import pprint

current_dir = os.path.dirname(__file__)
filename = "data_file.json" 
with open(current_dir + os.sep + filename, "r") as read_file:
    json_obj = json.load(read_file)
    pprint.pprint(json_obj)