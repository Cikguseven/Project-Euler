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

validPrimes = [3797] # List of primes that are truncatable both ways

def primeChecker(x):
	for d in range(2, int(sqrt(x)) + 1):
		if x % d == 0 and x != d:
			return False
	return True

def leftToRight(x):
	for i in range(len(str(x)) - 2):
		x = int(str(x)[1:])
		if primeChecker(x) == False:
			return False
	return True

def rightToLeft(x):
	for i in range(len(str(x)) - 2):
		x = int(str(x)[:len(str(x)) - 1])
		if primeChecker(x) == False:
			return False
	return True

from itertools import product

allFillers = []
stringOfFillers = ['', '1', '3', '7', '9'] # Non-terminal numbers
firstDigits = ['2', '3', '5', '7'] # Truncatable primes must start with these digits
lastDigits = ['3', '7'] # Truncatable primes must end with these digits

for i in range(2, 5):
	allFillers += list((product('1379', repeat = i)))

for filler in allFillers: # Create list of valid fillers to insert between first and last digits
	stringOfFillers.append(''.join(filler))

# Checks for truncatable primes by creating valid prime with filler 
while len(validPrimes) < 11:
	for a in firstDigits:
		for b in lastDigits:
			for filler in stringOfFillers:
				n = int(a + filler + b)
				if primeChecker(n):
					if leftToRight(n) and rightToLeft(n):
						validPrimes.append(n)

print(sum(validPrimes))

end = time.time()

print(end - start) # Programme takes 0.0469 seconds to execute