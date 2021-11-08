from itertools import permutations
from random import sample
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


def miller_rabin(n, k=3):
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        for a in sample(range(2, n-2), k):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    elif x == n - 1:
                        a = 0
                        break
                if a:
                    return False
        return True


def ppc(a, b):
    if miller_rabin(int(str(a) + str(b))) and miller_rabin(int(str(b) + str(a))):
        return True
    return False


primes = prime_sieve(10000)


def five_concat_primes():
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if ppc(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if ppc(a, c) and ppc(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if ppc(a, d) and ppc(b, d) and ppc(c, d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if ppc(a, e) and ppc(b, e) and ppc(c, e) and ppc(d, e):
                                        return(a + b + c + d + e)


print(five_concat_primes())

end = time.time()

# Executes in 5.749 seconds
print(end - start)
