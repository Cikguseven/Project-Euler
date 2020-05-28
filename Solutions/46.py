'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import time

start = time.time()

from math import sqrt

# Check if odd x is composite
def compositeChecker(n):
	for d in range(3, int(sqrt(n)) + 1, 2):
		if n % d == 0:
			return True
	return False

# Checks if n is prime
def primeChecker(n):
	for d in range(2, int(sqrt(n)) + 1):
		if n % d == 0:
			return False
	return True		

flag = True

x = 11

while flag:
	if compositeChecker(x):
		# Checks if composite odd number x can be written in valid expression
		for i in range(1, int((x / 2) ** 0.5) + 1):
			n = x - 2 * (i ** 2)
			if primeChecker(n): 
				x += 2
				break
			# x cannot be written as sum of prime and square of i
			elif i == int((x / 2) ** 0.5): 
				print(x)
				flag = False
	else:
		x += 2

end = time.time()

print(end - start) # Executed in 0.0360 seconds
