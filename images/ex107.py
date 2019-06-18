import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
im = Image.open( os.path.join(current_dir, filename) )
#Display image
im.show()
