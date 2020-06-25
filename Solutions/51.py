'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.
'''

import time

start = time.time()

from math import sqrt


def prime_checker(n):
    if n % 2 == 0:
        return
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


difference = []

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if a + b + c + d == 0:
                    continue
                difference.append(10000 * a + 1000 * b + 100 * c + 10 * d)

print(difference)



end = time.time()

print(end - start)
