import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
im = Image.open( os.path.join(current_dir, filename) )
#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
name = filename.split('.')
sharpen_filename = os.path.join(current_dir, 'sharpened_{0}.jpg'.format(name[0]))
im_sharp.save( sharpen_filename, 'JPEG' )
