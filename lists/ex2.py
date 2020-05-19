a_lists = []

# Ask to enter values and append to a list
for i in range(0, 10):
    inp = input("Enter a {}th position number: ".format(i))
    a_lists.append(inp)


# Print the list values
print(a_lists)

# Delete 7th element
del a_lists[7]
print(a_lists)
a_lists[7] = 90
print(a_lists)
a_lists.insert(7, 87)
print(a_lists)

# Print 7th element
print("7th position element in a list:", a_lists[7])

# Print 9th element
print("9th element in a list:", a_lists[9])

# Second last element in the list is
print("Second last element: ", a_lists[::-2])
