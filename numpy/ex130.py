import numpy as np

if __name__ == "__main__":
    normal_array = np.random.normal(5, 0.5, 10)
    print(normal_array)

    ### Min 
    print(np.min(normal_array))

    ### Max 
    print(np.max(normal_array))

    ### Mean 
    print(np.mean(normal_array))

    ### Median
    print(np.median(normal_array))

    ### Sd
    print(np.std(normal_array))