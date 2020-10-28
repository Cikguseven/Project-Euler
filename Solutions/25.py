import time

start = time.time()

a = 1

b = 1

solution = 2

x = 10 ** 999

while True:
    a = a + b
    solution += 1
    if a > x:
        break
    b = a + b
    solution += 1
    if b > x:
        break

print(solution)

end = time.time()

# Executes in 0.00400 seconds
print(end - start)
