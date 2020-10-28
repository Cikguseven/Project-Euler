import time

start = time.time()

from math import factorial as fac

counter = 0

for n in range(23, 101):
    for r in range(4, n - 3):
        if (fac(n) / (fac(r) * fac(n - r))) > 1000000:
            counter += 1

print(counter)

end = time.time()

# Executes in 0.0156 seconds
print(end - start)
