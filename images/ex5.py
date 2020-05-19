import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
image = Image.open( os.path.join(current_dir, filename) )
# Save image as png
name = filename.split('.')
png_filename = os.path.join(current_dir, 'png_{0}.png'.format(name[0]))
image.save(png_filename)