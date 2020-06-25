'''
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

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
