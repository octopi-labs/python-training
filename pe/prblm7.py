import math

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def prime_numbers(max_prime_numbers):
    counter = 0
    prime_number = 0
    number = 2
    while True:
        if is_prime(number):
            counter += 1
            prime_number = number
        if counter >= max_prime_numbers:
            break
        number += 1
    return number

if __name__ == "__main__":
    print(int(prime_numbers(10001)))

