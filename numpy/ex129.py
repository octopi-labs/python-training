import numpy as np

if __name__ == "__main__":
    # Indexing
    matrix  = np.array([(1,2,3), (4,5,6)])
    print(matrix)

    ## First column
    print('First row:', matrix[0])
    print('Second row:', matrix[1])

    print('Second column:', matrix[:,1])

    ## Second Row, two values
    print(matrix[1, :2])
