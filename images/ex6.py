import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
image = Image.open( os.path.join(current_dir, filename) )
# Resize image
new_image = image.resize((400, 400))
# Save image
name = filename.split('.')
png_filename = os.path.join(current_dir, 'resized_{0}.jpg'.format(name[0]))
new_image.save(png_filename)

print(image.size)
print(new_image.size)