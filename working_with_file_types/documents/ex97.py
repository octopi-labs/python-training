import os
from docx import Document


def getText(filename):
    document = Document(filename)
    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

if __name__ == "__main__":
    # open a new document 
    current_dir = os.path.dirname(__file__)
    filename = os.path.join(current_dir, "test.docx")
    print(getText(filename))

