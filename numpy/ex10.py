import numpy as np

if __name__ == "__main__":
    ### Matmul: matruc product of two arrays
    array_1 = [[1,2],[3,4]] 
    print(array_1)
    array_2 = [[5,6],[7,8]] 
    print(array_2)
    ### 1*5+2*7 = 19
    multi = np.matmul(array_1, array_2)
    print(multi)

    ## Determinant 2*2 matrix
    ### 5*8-7*6
    determinant = np.linalg.det(array_2)
    print(determinant)

