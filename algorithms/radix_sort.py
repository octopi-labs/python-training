import time


def counting_sort(arr, max_value, get_index):
    counts = [0] * max_value

    # counting O(n)
    for item in arr:
        counts[get_index(item)] += 1

    # Accumulating O(k)
    for idx, item in enumerate(counts):
        if idx == 0:
            continue
        else:
            counts[idx] += counts[idx-1]

    # Calculating start index - O(k)
    for idx, item in enumerate(counts[:-1]):
        if idx == 0:
            counts[idx] = 0
        counts[idx+1] = item

    result = [None] * len(arr)

    #Sorting - O(n)
    for item in arr:
        index = counts[get_index(item)]
        result[index] = item
        counts[get_index(item)] += 1

    return result

def get_digit(n, d):
    for counter in range(d-1):
        n //= 10
    return n%10

def get_num_digits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radix_sort(arr, max_value):
    num_digits = get_num_digits(max_value)

    for d in range(num_digits):
        arr = counting_sort(arr, max_value, lambda a: get_digit(a, d+1))
    return arr

if __name__ == "__main__":
    sample = [12, 23, 21, 4, 53, 24, 2, 43, 1]
    start = time.time()
    output = radix_sort(sample, max(sample))
    end = time.time()
    print("Sorted List:", output)
    print("Time Difference:", end-start)
