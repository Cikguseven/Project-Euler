'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time

start = time.time()

from math import sqrt

amicable_numbers = []

# Function to obtain sum of divisors of number, n
def d(n):
	sum_of_proper_divisors = 1 # 1 is a proper divisor of every positive number
	for d in range(2, int(sqrt(n)) + 1): # Divisors of numbers come in pairs and we only have to check for divisors less than or equal to its square root to find one of the pairs
		if n % d == 0:
			sum_of_proper_divisors += d  
			if n / d != d: # Counts square root of n only once
				sum_of_proper_divisors += n / d
				continue
	return sum_of_proper_divisors

for i in range(2, 10000):
	if d(d(i)) == i and d(i) != i:
		amicable_numbers.append(i)
	
print(sum(amicable_numbers))

end = time.time()

print(end - start) # Executed in 0.125 seconds


