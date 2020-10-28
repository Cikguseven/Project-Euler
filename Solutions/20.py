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
