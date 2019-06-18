import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
image = Image.open( os.path.join(current_dir, filename) )
# image thumbnail
image.thumbnail((400, 400))
# Save image
name = filename.split('.')
png_filename = os.path.join(current_dir, 'thumbnail_{0}.jpg'.format(name[0]))
image.save(png_filename)

print(image.size)
