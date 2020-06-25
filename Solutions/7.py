'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time

start = time.time()

from math import log

x = 10001

# Formula to find approximate upper bound value of nth prime
upper_bound = int(x * log(x) + x * log(log(x)))


def prime_sieve(n):
    is_prime = [True for i in range(n + 1)]
    primes = []
    for p in range(4, n + 1, 2):
        is_prime[p] = False
    p = 3
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
        p += 2
    is_prime[0] = False
    is_prime[1] = False
    for p in range(3, n + 1, 2):
        if is_prime[p]:
            primes.append(p)
    return primes


print(prime_sieve(upper_bound)[10000])

end = time.time()

# Executes in 0.0270 seconds
print(end - start)
