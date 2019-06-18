import os

import PyPDF2

# open a new document 
current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.pdf")

# Open a file object
pdfFileObj = open(filename, 'rb')

# Give file object to pdf file reader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
print(pdfReader.numPages)

# Get specific page
pageObj = pdfReader.getPage(0)

# Read the text in the page
text = pageObj.extractText()
print(text.encode('utf-8'))

# closing the pdf file object 
pdfFileObj.close() 