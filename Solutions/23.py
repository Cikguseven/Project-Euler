'''
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
'''

import time

start = time.time()

from math import sqrt

abundant_numbers = set()

# From Wikipedia: Upper limit is 20161 and not 28123
limit = 20162

solution = 0


def d(n):
    divisor_sum = 1
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            divisor_sum += d
            if n / d != d:
                divisor_sum += (n / d)
                continue
    return divisor_sum


for i in range(1, limit):
    if d(i) > i:
        abundant_numbers.add(i)
    if not any((i - a in abundant_numbers) for a in abundant_numbers):
        solution += i

print(solution)

end = time.time()

# Executes in 0.662 seconds
print(end - start)
