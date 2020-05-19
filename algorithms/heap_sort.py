def heap_sort(arr):
    size = len(arr)
    # building the maximum heap
    for i in range(size,-1,-1):
        heapify(arr, size, i)
    # extract one by one element
    for j in range(size-1,0,-1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, j, 0)

def heapify(arr, size, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < size and arr[i] < arr[left]:
        largest = left

    if right < size and arr[largest] < arr[right]:
        largest = right

    if i!=largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


if __name__ == "__main__":
    # Driver code to test above
    arr = [ 12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)
