'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# For prime to be truncatable, first and last digits have to be 3 or 7.

# Function to add digits in front of existing number and check if they are prime

import time

start = time.time()

from math import sqrt

from itertools import product

def prime_checker(x):
	for d in range(3, int(sqrt(x)) + 1, 2):
		if x % d == 0:
			return False
	return True

# Continuously removes first digit of primes and check if they are prime
def left_to_right(x):
	for i in range(len(str(x)) - 2):
		x = int(str(x)[1:])
		if prime_checker(x) == False:
			return False
	return True

# Continuously removes lasst digit of primes and check if they are prime
def right_to_left(x):
	for i in range(len(str(x)) - 2):
		x = int(str(x)[:len(str(x)) - 1])
		if prime_checker(x) == False:
			return False
	return True

first_digits = ['2', '3', '5', '7'] # Truncatable primes must start with these digits

last_digits = ['3', '7'] # Truncatable primes must end with these digits

truncatable_primes = {3797} # Set of truncatable primes to prevent double counting

counter = 0

# Checks for truncatable primes by creating valid prime with filler 
while len(truncatable_primes) < 11:
	temporary_fillers = []
	for digits in list((product('1379', repeat = counter))):
		temporary_fillers.append(''.join(digits))
	for prefix in first_digits:
		for suffix in last_digits:
			for filler in temporary_fillers:
				n = int(prefix + filler + suffix)
				if prime_checker(n):
					if left_to_right(n) and right_to_left(n):
						truncatable_primes.add(n)
	counter += 1

print(sum(truncatable_primes))

end = time.time()

print(end - start) # Programme takes 0.0370 seconds to execute