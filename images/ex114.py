import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
image = Image.open( os.path.join(current_dir, filename) )
# Resize image
box = (150, 200, 600, 600)
# Crop image
cropped_image = image.crop(box)
name = filename.split('.')
png_filename = os.path.join(current_dir, 'cropped_{0}.png'.format(name[0]))
cropped_image.save(png_filename)

print(image.size)
