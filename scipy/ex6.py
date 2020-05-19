import os

from skimage import io
from scipy import misc, ndimage
from matplotlib import pyplot as plt
import numpy as np

current_dir = os.path.dirname(__file__)


if __name__ == "__main__":
    #get face image of panda from misc package
    # panda = misc.face()
    filename = os.path.join(current_dir, "test.jpg")
    panda = io.imread(filename)
    # panda = np.fromfile(filename, dtype=np.uint8)
    #plot or show image of face
    plt.imshow( panda )
    plt.show()

    #Flip Down using scipy misc.face image  
    flip_down = np.flipud(panda)
    plt.imshow(flip_down)
    plt.show()

    #rotatation function of scipy for image – image rotated 135 degree
    panda_rotate = ndimage.rotate(panda, 135)
    plt.imshow(panda_rotate)
    plt.show()