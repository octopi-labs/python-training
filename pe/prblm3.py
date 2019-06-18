import math

number = 600851475143

def largest_prime_factor(number):
    largest_prime = -1

    while number % 2 == 0:
        largest_prime = 2
        number >>= 1
        # number = number >> 1

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            largest_prime = i
            number = number / i

    if number > 2:
        largest_prime = number

    return largest_prime

print(int(largest_prime_factor(number)))

