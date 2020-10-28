import time

start = time.time()

solution = 0

for n in range(1, 1001):
    solution += n ** n

print(str(solution)[-10:])

end = time.time()

# Executes in 0.0310 seconds
print(end - start)
