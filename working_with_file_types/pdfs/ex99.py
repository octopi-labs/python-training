import os
import slate3k as slate

# open a new document 
current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, "test.pdf")

# Read pdf text
with open(filename,'rb') as pdf_file:
    extracted_text = slate.PDF(pdf_file)
print(extracted_text)