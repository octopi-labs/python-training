import numpy as np

if __name__ == "__main__":
    # Create 3 X 2 matrix
    matrix  = np.array([(1,2,3), (4,5,6)])
    print(matrix)
    # Reshape the matrix
    matrix = matrix.reshape(3,2)
    print(matrix)

    # Flatten the matrix
    matrix = matrix.flatten()
    print("Flatten matrix:", matrix)

    

