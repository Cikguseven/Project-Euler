import time

start = time.time()

from math import prod

from fractions import Fraction as simplest_form

numerators = []

denominators = []

for n in range(10, 100):
    for d in range(n + 1, 100):
        f = n / d
        for a in str(n):
            for b in str(d):
                if int(a) == int(b) and int(a) != 0:
                    new_n = str(n).replace(a, '', 1)
                    new_d = str(d).replace(b, '', 1)
                    if int(new_d) != 0 and int(new_n) / int(new_d) == f:
                        numerators.append(n)
                        denominators.append(d)
                    break

solution = simplest_form(prod(numerators), prod(denominators))

print(solution)

end = time.time()

# Executes in 0.0310 seconds
print(end - start)
