import numpy as np

if __name__ == "__main__":
    # Create values from 1 to 10
    matrix = np.arange(1, 11)
    print(matrix)

    # Create evenly spaced sample
    matrix = np.linspace(1.0, 5.0, num=10)
    print(matrix)
    # Ignore the last digit
    matrix = np.linspace(1.0, 5.0, num=10, endpoint=False)
    print(matrix)

    # Create even spaced numbers on log scale
    matrix = np.logspace(3.0, 4.0, num=4)	
    print(matrix)

    # Size of an array
    matrix = np.array([1,2,3], dtype=np.complex128)
    print(matrix.itemsize)