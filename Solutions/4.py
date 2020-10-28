import time

start = time.time()

solution = 0

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        if a * b > solution:
            if str(a * b)[::-1] == str(a * b):
                solution = a * b
                break
            else:
                continue
        break

print(solution)

end = time.time()

# Executes in 0.00405 seconds
print(end - start)
