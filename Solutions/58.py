import time

start = time.time()

from math import sqrt

flag = True

n = 2

non_primes = [1]

primes = []


def prime_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


# Formula to generate diagonal numbers from OEIS
while flag:
    a, b, c, d = 4 * n * n - 10 * n + 7, 4 * n * n - 8 * \
        n + 5, 4 * n * n - 6 * n + 3, (2 * n - 1) ** 2
    for numbers in a, b, c, d:
        if prime_checker(numbers):
            primes.append(numbers)
        else:
            non_primes.append(numbers)
    if len(non_primes) / len(primes) > 9:
        print(2 * n - 1)
        flag = False
        break
    n += 1

end = time.time()

# Executed in 5.51 seconds
print(end - start)
