import time

start = time.time()

from math import sqrt

from itertools import product

primes = []

solution = []


def prime_checker(n):
    for d in range(3, int(sqrt(n)), 2):
        if n % d == 0:
            return
    primes.append(n)


# Generate 3-6 digit primes with digits 1, 3, 7 & 9
for length in range(3, 7):
    for digits in list(product('1379', repeat=length)):
        number = int(''.join(digits))
        prime_checker(number)

# Rotates primes formed by shifting the first digit to the last position and
# check if they are primes.
for prime in primes:
    rotations = set()
    clone = prime
    length = len(str(prime))
    for i in range(length - 1):
        clone = int(str(clone)[1:length] + str(clone)[0])
        if clone not in primes:
            break
        if i == length - 2:
            solution.append(prime)
            break

print(len(solution) + 13)

end = time.time()

# Executes in 0.0801 seconds
print(end - start)
