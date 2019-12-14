a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

b = [[1, 2], [3, 4], [5, 6], [7, 8]]

c = []
for i in range(len(a)):
    temp = []
    for j in range(len(b[0])):
        # if len(a) <= 0:
        #    c.append(temp)
        temp.append(0)
    c.append(temp)


print(c)
