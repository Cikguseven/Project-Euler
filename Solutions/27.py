'''
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤ n ≤ 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1)
+ 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n**2 − 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form: n**2 + an + b, where |a| < 1000 and |b| ≤
1000 and |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

# Generate odd prime numbers <= 1000 using Sieve of Eratosthenes for b. For
# quadratic expression to be prime when n = 0, b has to be prime. The only
# prime numbers left out is b = 2.

import time

start = time.time()

from math import sqrt

current_max = 39

solution = 0


def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


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


# Function to check if quadratic expression generates primes and the largest
# value of n for which quadratic expression is prime for all integers ≤ n.
# Returns product of a and b for current largest value of n.
def quadratic_prime_generator(a, b):
    n = 0
    quadratic = n ** 2 + a * n + b
    while quadratic > 0 and prime_checker(quadratic):
        n += 1
        quadratic = (n ** 2 + a * n + b)
    global current_max
    if n > current_max:
        current_max = n - 1
        global solution
        solution = a * b


primes = prime_sieve(999)

# Checking if quadratic expressions are prime where b is an odd prime. For n =
# 1, 1 + a + b has to be prime as well. As such, if b is odd, a has to be a
# negative or positive odd number. Result: n ** 2 - 61n + 971 are primes for 0
# ≤ n ≤ 70.
for a in range(-999, 1000, 2):
    for x in primes:
        quadratic_prime_generator(a, x)

# Checking for b = 2. Since b is now even, a has to be even so that n ** 2 +
# an + b is prime for n = 1.
for a in range(-998, 999, 2):
    quadratic_prime_generator(a, 2)

print(solution)

end = time.time()

# Executes in 0.631 seconds
print(end - start)
