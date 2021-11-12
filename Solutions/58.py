import time

start = time.time()

from math import sqrt

from random import sample

n = 2

non_primes = [1]

primes = []


def miller_rabin(n):
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        for a in sample(range(2, n - 2), 3):
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


while True:
    # Formula to generate diagonal numbers from OEIS
    a, b, c, d = 4 * n * n - 10 * n + 7, 4 * n * n - 8 * \
        n + 5, 4 * n * n - 6 * n + 3, (2 * n - 1) ** 2
    for numbers in a, b, c, d:
        if miller_rabin(numbers):
            primes.append(numbers)
        else:
            non_primes.append(numbers)
    if len(non_primes) / len(primes) > 9:
        print(2 * n - 1)
        break
    n += 1

end = time.time()

# Executed in 0.389 seconds
print(end - start)
