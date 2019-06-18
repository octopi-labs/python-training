# importing the csv module
import csv
import os

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]

current_dir = os.path.dirname(__file__)
# csv file name
filename = "test.csv"

# writing to csv file
with open(os.path.join(current_dir, filename), 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	
	# writing the fields
	csvwriter.writerow(fields)
	
	# writing the data rows
	csvwriter.writerows(rows)
