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

pairs = [n for n in combinations(prime_sieve(1000), 2)]

valid_pairs = []

for value in pairs:
    a = value[0]
    b = value[1]
    if prime_checker(int(str(a) + str(b))) and prime_checker(int(str(b) + str(a))):
        valid_pairs.append([a, b])

two_pairs = [n for n in combinations(valid_pairs, 2)]

valid_triplets = []

for pairs in two_pairs:
    a = pairs[0]
    b = pairs[1]
    c = set(a + b)
    if len(c) == 3 and list(set(a)^ set(b)) in valid_pairs:
        valid_triplets.append(list(c))

print(valid_triplets)



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
