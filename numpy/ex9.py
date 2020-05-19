import numpy as np

if __name__ == "__main__":
    ### Dot product: product of two arrays
    array_1 = np.array([1,2])
    print(array_1)
    array_2 = np.array([4,5])
    print(array_2)
    ### 1*4+2*5
    dot_product = np.dot(array_1, array_2)
    print(dot_product)