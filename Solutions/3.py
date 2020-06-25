'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import time

start = time.time()

solution = 600851475143

d = 2

while d < solution:
    if solution % d == 0:
        solution /= d
        d -= 1
    d += 1

print(solution)

end = time.time()

# Executes in 0.00200 seconds
print(end - start)
