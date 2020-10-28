import time

start = time.time()

from math import sqrt

flag = True

x = 15


# Check if odd x is composite
def composite_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return True
    return False


# Checks if n is prime
def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


while flag:
    if composite_checker(x):
        for i in range(1, int((x / 2) ** 0.5) + 1):
            n = x - 2 * (i ** 2)
            if prime_checker(n):
                break
            # x cannot be written as sum of prime and square of i
            elif i == int((x / 2) ** 0.5):
                print(x)
                flag = False
                break
    x += 2

end = time.time()

# Executes in 0.0171 seconds
print(end - start)
