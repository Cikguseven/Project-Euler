import time

start = time.time()

a = 1

b = 2

solution = [2]

while a + b < 1000000000:
    a = a + b
    if a % 2 == 0:
        solution.append(a)
    b = a + b
    if b > 1000000000:
        break
    if b % 2 == 0:
        solution.append(b)

print(sum(solution))

end = time.time()

# Executes in 0.0 seconds
print(end - start)
