import numpy as np

if __name__ == "__main__":
    # Create zero matrix
    matrix = np.zeros((3, 3), dtype=np.int16, order='C')
    print("Zero matrix", matrix)

    # Create one matrix
    matrix = np.ones((3, 3), dtype=np.int16, order='C')
    print("Ones matrix", matrix)
