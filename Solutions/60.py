import time

start = time.time()

from math import sqrt

from itertools import permutations


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
        if is_prime[p] and p > 10:
            primes.append(p)
    return primes


def prime_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


special_primes = [3, 7]

for a in prime_sieve(30000):
    temp_primes = special_primes.copy()
    temp_primes.append(a)
    perm = permutations(temp_primes, 2)
    x = [n for n in list(perm)]
    y = []
    for uniques in x:
        y.append(prime_checker(int(str(uniques[0]) + str(uniques[1]))))
    if all(y):
        special_primes.append(a)

print(special_primes)

        
end = time.time()

# Executes in 0.129 seconds
print(end - start)
