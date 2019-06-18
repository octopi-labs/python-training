import math


def triplet(number):
    for i in range(number):
        for j in range(1, i):
            c = math.sqrt(j * j + i * i)
            if c % 1 == 0 and i + j + int(c) == number:
                return [i, j, int(c), int(i*j*c)]


print(triplet(1000))
