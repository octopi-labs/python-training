import os
from docx import Document


def get_text(filename):
    document = Document(filename)
    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

if __name__ == "__main__":
    # open a new document 
    current_dir = os.path.dirname(__file__)
    filename = os.path.join(current_dir, "test.docx")
    print(get_text(filename))

