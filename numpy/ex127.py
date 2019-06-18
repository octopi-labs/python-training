import numpy as np

if __name__ == "__main__":
    # 4 x 4 matrix
    matrix = np.matrix(np.ones((4,4)))

    print(matrix)
    np.array(matrix)[2] = 2
    print(matrix)
    np.asarray(matrix)[2] = 2
    print(matrix)