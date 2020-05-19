import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"
logo_file = "logo.png"

#Read image
image = Image.open( os.path.join(current_dir, filename) )
# Read logo image
logo = Image.open( os.path.join(current_dir, logo_file) )
# Copy image
image_copy = image.copy()

position = ((image_copy.width - logo.width), (image_copy.height - logo.height))

image_copy.paste(logo, position)

name = filename.split('.')
png_filename = os.path.join(current_dir, 'logo_{0}.png'.format(name[0]))
image_copy.save(png_filename)