import time

start = time.time()

from math import sqrt


# Checks if n is prime
def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True

def checker():
    x = 15
    while True:
        if not prime_checker(x):
            y = int((x / 2) ** 0.5)
            for i in range(1, y + 1):
                n = x - 2 * (i ** 2)
                if prime_checker(n):
                    break
                # x cannot be written as sum of prime and square of i
                elif i == y:
                    return x
        x += 2

print(checker())

end = time.time()

# Executes in 0.0110 seconds
print(end - start)
