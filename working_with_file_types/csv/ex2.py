# importing the csv module
import csv
import os

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA', 'Hire Date']

# data rows of csv file
rows = [ ['Rahul, Shelke', 'COE', '2', '9.0', '06/01/19'],
        ['Sanchit', 'COE', '2', '9.1', '06/02/19'],
        ['Aditya', 'IT', '2', '9.3', '06/03/19'],
        ['Sagar', 'SE', '1', '9.5', '06/04/19'],
        ['Prateek', 'MCE', '3', '7.8', '06/10/19'],
        ['Sahil', 'EP', '2', '9.1', '05/23/19']]

current_dir = os.path.dirname(__file__)
# csv file name
filename = "test_1.csv"

# writing to csv file
with open(os.path.join(current_dir, filename), 'w') as csvfile:
	# creating a csv writer object
        ## csv.QUOTE_ALL: will quote all fields
        ## csv.QUOTE_MINIMAL: [Default case] will quote fields only if they contain the delimiter or the quotechar.\
        ## csv.QUOTE_NONNUMERIC: will quote all fields containing text data and convert all numeric fields to the float data type
        ## csv.QUOTE_NONE: will escape delimiters instead of quoting them
	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	# writing the fields
	csvwriter.writerow(fields)
	
	# writing the data rows
	csvwriter.writerows(rows)
