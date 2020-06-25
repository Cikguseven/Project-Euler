'''
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
'''

import time

start = time.time()

from math import sqrt

flag = True

x = 15


# Check if odd x is composite
def composite_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return True
    return False


# Checks if n is prime
def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


while flag:
    if composite_checker(x):
        for i in range(1, int((x / 2) ** 0.5) + 1):
            n = x - 2 * (i ** 2)
            if prime_checker(n):
                break
            # x cannot be written as sum of prime and square of i
            elif i == int((x / 2) ** 0.5):
                print(x)
                flag = False
                break
    x += 2

end = time.time()

# Executes in 0.0171 seconds
print(end - start)
