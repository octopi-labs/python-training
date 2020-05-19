import numpy as np


if __name__ == "__main__":
    # Create python list
    python_list = [1, 3, 5, 7, 9]

    # Convert the python list to numpy array
    numpy_array = np.array(python_list)

    print("Python list:", python_list)
    print("Numpy Array:", numpy_array)

    # Perform mathematical operation
    numpy_array += 10
    print("Add:", numpy_array)
    numpy_array -= 4
    print("Subtract:", numpy_array)
    numpy_array *= 2
    print("Multiply:", numpy_array)
    numpy_array = numpy_array / 3
    print("Divide:", numpy_array)

    # Shape of an array
    print(numpy_array.shape)
    # Type of an array
    print(numpy_array.dtype)

    # 2 Dimensional array
    array_2d = np.array([[1,2,3], [4,5,6]])
    print("2 Dimensional array:", array_2d)
    print(array_2d.shape)

    ### 3 Dimensional array
    array_3d = np.array([[[1, 2,3], [4, 5, 6]], [[7, 8,9], [10, 11, 12]]])
    print("3 Dimensional array:", array_3d)
    print(array_3d.shape)