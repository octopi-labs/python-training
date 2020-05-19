import os
from docx import Document, shared

# open a new document 
current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.docx")

# Create a Document object
document = Document(filename)

# Add line break
document.add_page_break()

image = os.path.join(current_dir, "mangalmurti.png")

document.add_picture(image, width=shared.Inches(1), height=shared.Cm(4))

# Save document
document.save(filename)
