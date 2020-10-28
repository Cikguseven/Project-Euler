import time

start = time.time()

from math import sqrt

from itertools import product

first_digit = ['2', '3', '5', '7']

last_digit = ['3', '7']

solution = {3797}

length = 0


def prime_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


# Continuously removes first digit of primes and check if they are prime
def left_to_right(n):
    for i in range(len(str(n)) - 2):
        n = int(str(n)[1:])
        if not prime_checker(n):
            return False
    return True


# Continuously removes last digit of primes and check if they are prime
def right_to_left(n):
    for i in range(len(str(n)) - 2):
        n = int(str(n)[:len(str(n)) - 1])
        if not prime_checker(n):
            return False
    return True


while len(solution) < 11:
    fillers = []
    for digits in list((product('1379', repeat=length))):
        fillers.append(''.join(digits))
    for prefix in first_digit:
        for suffix in last_digit:
            for filler in fillers:
                n = int(prefix + filler + suffix)
                if prime_checker(n) and left_to_right(n) and right_to_left(n):
                    solution.add(n)
    length += 1

print(sum(solution))

end = time.time()

# Executes in 0.0300 seconds
print(end - start)
