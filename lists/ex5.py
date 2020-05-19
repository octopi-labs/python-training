a_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Copy all even elements of list a to list b
b_lists = []
for item in a_lists:
    if item % 2 == 0:
        b_lists.append(item)

print(b_lists)

# List comprehension
c_lists = [item for item in a_lists if item % 2 == 0]
print(c_lists)
