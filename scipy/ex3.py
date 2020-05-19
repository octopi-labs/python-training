import numpy as np
from scipy import linalg

if __name__ == "__main__":
    #define square matrix
    two_d_array = np.array([ [4,5], [3,2] ])
    #pass values to det() function
    det = linalg.det( two_d_array )
    print(det)

    # define square matrix
    two_d_array = np.array([ [4,5], [3,2] ])
    #pass value to function inv()
    inv = linalg.inv( two_d_array )
    print(inv)

    #define two dimensional array
    arr = np.array([[5,4],[6,3]])
    #pass value into function
    eg_val, eg_vect = linalg.eig(arr)
    #get eigenvalues
    print(eg_val)
    #get eigenvectors
    print(eg_vect)