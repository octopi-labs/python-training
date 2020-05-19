import os
import openpyxl

current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.xlsx")

# Load workbook
wb = openpyxl.load_workbook(filename)

sheet = wb.get_sheet_by_name('Middle Sheet')

sheet['A1'] = 200

sheet['A2'] = 300

sheet['A3'] = '=SUM(A1:A2)'

wb.save(filename)
