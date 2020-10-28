import time

start = time.time()

from math import factorial as fac

from itertools import combinations_with_replacement

solution = []

# Check numbers between 10 and 1499999. Addition of factorial of digits is
# commutative and testing can be restricted to unique combinations of digits.
for length in range(2, 8):
    for digit_string in combinations_with_replacement('0123456789', length):
        digit_factorial_sum = sum([fac(int(digit)) for digit in digit_string])
        if sorted(str(digit_factorial_sum)) == sorted(digit_string):
            solution.append(digit_factorial_sum)

print(sum(solution))

end = time.time()

# Executes in 0.0620 seconds
print(end - start)
