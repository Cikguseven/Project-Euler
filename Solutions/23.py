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
