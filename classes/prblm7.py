import math


TEST_PRINT = 23

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

def first_hundred_primes():
    prime_numbers = []
    number = 2
    while len(prime_numbers) <= 100:
        if is_prime(number):
            prime_numbers.append(number)
        number += 1
    return prime_numbers

if __name__ == "__main__":
    # print(int(prime_numbers(10001)))
    prime_number = first_hundred_primes()
    even_primes = [prime_number[item] for item in range(0, len(prime_number)) if item % 2 == 0]
    print(prime_number)
    print(even_primes)

