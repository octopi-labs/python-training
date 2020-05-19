# importing the csv module
import csv
import os

# my data rows as dictionary objects
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
# field names
fields = ['name', 'branch', 'year', 'cgpa']

current_dir = os.path.dirname(__file__)
# csv file name
filename = "test_dict.csv"

# writing to csv file
with open(os.path.join(current_dir, filename), 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    
    # writing headers (field names)
    writer.writeheader()
    
    # writing data rows
    writer.writerows(mydict) 
