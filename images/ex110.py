import os
from PIL import Image, ImageFilter


current_dir = os.path.dirname(__file__)
filename = "test.jpg"

#Read image
image = Image.open( os.path.join(current_dir, filename) )
# The file format of the source file.
print(image.format)

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(image.mode)

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size)

# Colour palette table, if any.
print(image.palette)