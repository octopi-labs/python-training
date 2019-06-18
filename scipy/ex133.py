import os

import numpy as np
from scipy import io as sio
 
current_dir = os.path.dirname(__file__)

if __name__ == "__main__":
    array = np.ones((4, 4))
    filename = os.path.join(current_dir, 'example.mat')
    sio.savemat(filename, {'ar': array}) 
    data = sio.loadmat(filename, struct_as_record=True)
    print(data)
