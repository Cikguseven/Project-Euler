'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import time

start = time.time()

from math import sqrt

limit = 20162 # From Wikipedia: Upper limit is 20161 and not 28123

solution = 0

abundant_numbers = set()

# Function to obtain sum of divisors of number, n
def d(n):
	sum_of_proper_divisors = 1 # 1 is a proper divisor of every positive number
	for d in range(2, int(sqrt(n)) + 1): # Divisors of numbers come in pairs and we only have to check for divisors less than or equal to its square root to find one of the pairs
		if n % d == 0:
			sum_of_proper_divisors += d  
			if n / d != d: # Counts square root of n only once
				sum_of_proper_divisors += (n / d)
				continue
	return sum_of_proper_divisors

for i in range(1, limit):
	if d(i) > i: # Checks if number, i, is abundant
		abundant_numbers.add(i)
	if not any((i - a in abundant_numbers) for a in abundant_numbers):
		solution += i

print(solution) # Sum of triangular numbers from 1 to 20161: 203243041. x must be smaller than this limit.

end = time.time()

print(end - start) # Executed in 0.680 seconds
