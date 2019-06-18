# importing csv module
import csv
import os

current_dir = os.path.dirname(__file__)

# csv file name
filename = "test.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(os.path.join(current_dir, filename), 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)
    
    # extracting field names through first row
    fields = next(csvreader)
    
    # extracting each data row one by one
    for row in csvreader:
        print(row)
        rows.append(row)
    
    # get total number of rows
    print("Total no. of rows: {0}".format(csvreader.line_num)) 

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')

for row in rows[:5]:
    # parsing each column of a row
    for key, value in row.items():
        print("{0}: {1}".format(key, value))
    print('\n') 
