'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time

start = time.time()

from math import factorial

n = factorial(100)

solution = 0

while n:
    solution += n % 10
    n //= 10

print(solution)

end = time.time()

# Executes in 0.0 seconds
print(end - start)
