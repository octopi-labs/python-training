def insertion_sort(inpvalue):
    for i in range(1, len(inpvalue)):
        temp = inpvalue[i]
        j = i - 1
        while (j >= 0 and temp < inpvalue[j]):
            inpvalue[j + 1] = inpvalue[j]
            j = j - 1
        inpvalue[j + 1] = temp


if __name__ == "__main__":
    sample = [12, 342, 43, 54, 65]
    insertion_sort(sample)
    print(sample)
