'''
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

import time

start = time.time()

n = 1


def checker(n):
    digits = set(str(n))
    for i in range(6, 1, -1):
        if set(str(n * i)) != digits:
            return False
    return True


while True:
    if checker(n):
        print(n)
        break
    n += 1

end = time.time()

# Executed in 0.287 seconds
print(end - start)
