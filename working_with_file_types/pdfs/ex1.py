import os
from fpdf import FPDF

# open a new document 
current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test_2.pdf")
 
pdf = FPDF()

# Add page
pdf.add_page()
# Set font
pdf.set_font("Arial", size=12)
# write content
pdf.cell(200, 10, txt="Welcome to PDF creation with Python!", ln=1, align="C")

lines = ["Anyway, the next step is to create a page using the add_page method.",
        "Then we set the pages font via the set_font method.",
        "You will note that we pass in the fonts family name and the size that we want.",
        "You can also set the fonts style with the style argument.",
        "If you want to do this, note that it takes a string such as B for bold or BI for Bold-Italicized."]

for line in lines:
    pdf.cell(200, 10, line, 0, 1, align="L")

pdf.output(filename)

