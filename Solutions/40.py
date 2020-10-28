import time

start = time.time()

product = 1

solution = ''

# Minimum number of iterations to obtain decimal fraction with a million digits
for n in range(185186):
    solution += str(n)

for exponent in range(7):
    product *= int(solution[10 ** exponent])

print(product)

end = time.time()

# Executes in 0.138 seconds
print(end - start)
