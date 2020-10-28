import time

start = time.time()

solution = 0

for i in str(2 ** 1000):
    solution += int(i)

print(solution)

end = time.time()

# Executes in 0.0 seconds
print(end - start)
