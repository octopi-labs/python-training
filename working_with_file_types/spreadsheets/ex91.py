import os
# Import pandas
import pandas as pd

current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.xlsx")

# Load spreadsheet
spreadsheet = pd.ExcelFile(filename)

# Print the sheet names
print(spreadsheet.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = spreadsheet.parse('First Sheet')

print(df1)

# Check the first entries of the DataFrame
print(df1.head())

# Check the last entries of the DataFrame
print(df1.tail())
