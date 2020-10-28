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
