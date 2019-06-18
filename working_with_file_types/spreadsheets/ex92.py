import os
# Import pandas
import pandas as pd
import openpyxl

current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.xlsx")

# Load spreadsheet
spreadsheet = pd.ExcelFile(filename)

# Load a sheet into a DataFrame by name: df1
df1 = spreadsheet.parse('First Sheet')

# Load workbook
wb = openpyxl.load_workbook(filename)

# Specify a writer
writer = pd.ExcelWriter(filename, engine='openpyxl')
writer.book = wb

# Write your DataFrame to a file     
df1.to_excel(writer, sheet_name='Last Sheet')

# Save the result 
writer.save()
