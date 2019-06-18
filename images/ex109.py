import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
im = Image.open( os.path.join(current_dir, filename) )

#Splitting the image into its respective bands, i.e. Red, Green, and Blue for RGB
r,g,b,a = im.split()
print(r)
print(g)
print(b)
print(a)

