import numpy as np

if __name__ == "__main__":
    ## Horitzontal Stack
    arr_1 = np.array([1,2,3])
    arr_2 = np.array([4,5,6])

    print('Horizontal Append:', np.hstack((arr_1, arr_2)))

    ## Vertical Stack
    print('Vertical Append:', np.vstack((arr_1, arr_2)))

    ## Generate random nmber from normal distribution
    normal_array = np.random.normal(loc=5, scale=0.5, size=10)
    print(normal_array)
    