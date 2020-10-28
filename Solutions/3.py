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
