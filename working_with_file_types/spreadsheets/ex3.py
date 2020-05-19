import os
import openpyxl
from openpyxl.styles import Font

current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.xlsx")

# Load workbook
wb = openpyxl.load_workbook(filename)

sheet = wb.get_sheet_by_name('CMI Team')

fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj1
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3'] = '24 pt Italic'

wb.save(filename)