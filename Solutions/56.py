'''
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
'''

import time

start = time.time()

solution = 0

for a in range(2, 100):
    for b in range(2, 100):
        result = str(a ** b)
        digital_sum = 0
        for digits in result:
            digital_sum += int(digits)
        if digital_sum > solution:
            solution = digital_sum

print(solution)

end = time.time()

# Executed in 0.258 seconds
print(end - start)
