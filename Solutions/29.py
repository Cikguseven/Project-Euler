import time

start = time.time()

solution = set()

for a in range(2, 101):
    for b in range(2, 101):
        solution.add(a ** b)

print(len(solution))

end = time.time()

# Executes in 0.0100 seconds
print(end - start)
