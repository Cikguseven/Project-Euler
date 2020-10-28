import time

start = time.time()

from functools import reduce

# Only n = 32 and larger produces triangle numbers larger than 500
n = 32

while True:
    prime_factors = {}
    triangle_number = n * (n + 1) / 2
    i = 2
    while i <= triangle_number:
        if triangle_number % i == 0:
            triangle_number /= i
            if i in prime_factors:
                prime_factors[i] += 1
            else:
                prime_factors[i] = 1
            i -= 1
        i += 1
    powers = map(lambda x: (x + 1), prime_factors.values())
    divisors = reduce(lambda x, y: x * y, powers)
    if divisors > 500:
        print(int(((n - 1) * (n)) / 2))
        break
    n += 1

end = time.time()

# Executes in 8.30 seconds
print(end - start)
