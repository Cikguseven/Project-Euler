'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

import time

start = time.time()

decimal = '' # String representing decimal fraction 

product = 1 

for n in range(185186): # Minimum number of iterations to obtain decimal fraction with a million digits
	decimal += str(n)

for exponent in range(7):
	product *= int(decimal[10 ** exponent])

print(product)

end = time.time()

print(end - start) # Executed in 0.141 seconds