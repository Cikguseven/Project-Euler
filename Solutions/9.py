import time

start = time.time()

# Generate Pythagorean triplets using m, n quadratic method
for m in range(1, 32):
    for n in range(1, m):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if a + b + c == 1000:
            print(a * b * c)
            break

end = time.time()

# Executes in 0.0 seconds
print(end - start)
