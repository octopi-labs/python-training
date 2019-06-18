a_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

length = len(a_lists)
print("Length of the list: ", length)

# Delete each element of the list
for i in range(0, int(length/2 + 1)):
    print("index: {}".format(i))
    print(a_lists[i])
    del a_lists[i]
    print(a_lists)
