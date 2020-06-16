'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

import time

start = time.time()

# Function to generate number of distinct prime factors
def number_of_prime_factors(n):
	d = 2
	factors = set()
	# Test divisors until square root of number as there is only one prime factor after the square root
	while d < n ** 0.5 or n == 1: 
		if n % d == 0:
			n = n / d
			factors.add(d)
			d -= 1
		d += 1
	return (len(factors) + 1)

x = 2 * 3 * 5 * 7 # Smallest number with 4 distinct prime factors

while True:
	if number_of_prime_factors(x) == 4:
		x += 1
		if number_of_prime_factors(x) == 4:
			x += 1
			if number_of_prime_factors(x) == 4:
				x += 1
				if number_of_prime_factors(x) == 4:
					print(x - 3)
					break
	x += 1

end = time.time()

print(end - start) # Executed in 4.04 seconds

