'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

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

print(end - start) # Executed in 0.0 seconds