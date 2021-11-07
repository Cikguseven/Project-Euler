from itertools import combinations
from itertools import permutations
from math import sqrt
import time

start = time.time()


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
    primes.remove(5)
    return primes


def prime_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True

valid_pairs = []

for a in prime_sieve(100):
    for b in prime_sieve(100):
        if b > a:
            pairs = [a, b]
            perm = permutations(pairs, 2)
            x = [n for n in list(perm)]
            z = []
            for uniques in x:
                if not prime_checker(int(str(uniques[0]) + str(uniques[1]))):
                    break
                else:
                    z.append(prime_checker(
                        int(str(uniques[0]) + str(uniques[1]))))
            if len(z) == 2:
                valid_pairs.append(pairs)

print(len(valid_pairs))

x = combinations(valid_pairs, 2)

y= [n for n in list(x)]

print(len(y))


'''
for a in y:
    perm = permutations(a, 2)
    x = [n for n in list(perm)]
    print(x)
    z = []
    for uniques in x:
        z.append(prime_checker(int(str(uniques[0]) + str(uniques[1]))))
    print(z)
    if all(z):
        print(y)
'''

end = time.time()

# Executes in 0.129 seconds
print(end - start)
