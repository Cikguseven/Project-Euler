'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time

start = time.time()

from math import sqrt

solution = []


def d(n):
    divisor_sum = 1
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            divisor_sum += d
            if n / d != d:
                divisor_sum += n / d
                continue
    return divisor_sum


for n in range(2, 10000):
    if d(d(n)) == n and d(n) != n:
        solution.append(n)

print(sum(solution))

end = time.time()

# Executes in 0.125 seconds
print(end - start)
