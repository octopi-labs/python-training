import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"
name = filename.split('.')

#Read image
image = Image.open( os.path.join(current_dir, filename) )
image_rot_90 = image.rotate(90)
png_filename = os.path.join(current_dir, 'rot_90_{0}.jpg'.format(name[0]))
image_rot_90.save(png_filename)

image_rot_180 = image.rotate(180)
png_filename = os.path.join(current_dir, 'rot_180_{0}.jpg'.format(name[0]))
image_rot_180.save(png_filename)


image_rot_18 = image.rotate(18)
png_filename = os.path.join(current_dir, 'rot_18_{0}.jpg'.format(name[0]))
image_rot_18.save(png_filename)
