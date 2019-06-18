a_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a_lists)

# Remove all elements of the list
tmp = None
while len(a_lists) > 0:
    tmp = a_lists.pop()
    print(tmp)

print(a_lists)

# Delete the entire list
del a_lists
print(tmp)
print(a_lists)