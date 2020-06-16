'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import time

start = time.time()

from functools import reduce

n = 32 # Only n = 32 and larger produces triangle numbers larger than 500

while True:
	prime_factors = {}
	triangle_number = n * (n + 1) / 2
	n += 1
	i = 2
	while i <= triangle_number: # Finding number of prime factors for a triangle number
		if triangle_number % i == 0:
			triangle_number /= i
			if i in prime_factors:
				prime_factors[i] += 1
			else:
				prime_factors[i] = 1
			i -= 1
		i += 1
	powers = map(lambda x: (x + 1), prime_factors.values()) # Increasing each divisor count by one to find number of divisors
	divisors = reduce(lambda x, y: x * y, powers)
	if divisors > 500:
		print(int(((n - 1) * (n)) / 2))
		break

end = time.time()

print(end - start) # Executed in 8.95 seconds