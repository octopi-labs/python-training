"""
This problem can be solved using  Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
import math
import prblm7

def sieve_eratosthenes(upper_limit):
    sieve_bound = int((upper_limit - 1) / 2)
    upper_sqrt = int((math.sqrt(upper_limit) - 1) / 2)
    prime_bits = [True for i in range(sieve_bound + 1)]

    for i in range(1, upper_sqrt + 1):
        if prime_bits[i]:
            for j in range(i * 2 * (i + 1), sieve_bound + 1, 2 * i + 1):
                prime_bits[j] = False

    primes = [2]
    for i in range(1, sieve_bound + 1):
        if prime_bits[i]:
            primes.append(2 * i + 1)

    return primes

def sum_primes(max_number):
    sum = 2
    for counter in range(3, max_number, 2):
        if prblm7.is_prime(counter):
            sum += counter
    return sum

if __name__ == "__main__":
    # print(sum_primes(2000000))
    primes = sieve_eratosthenes(2000000)
    print(sum(primes))
