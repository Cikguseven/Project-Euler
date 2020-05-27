'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import time

start = time.time()

from math import sqrt

validDigits = [1, 3, 7, 9]
restrictedPrimes = []

def primeChecker(x): # Checks if numbers formed with valid digits are prime
	d = 3
	while True:
		if x % d == 0 and int(sqrt(x)) >= d:
			break
		elif int(sqrt(x)) >= d: # Test the next divisor if it is still smaller than the square root of x
			d += 1
		else:
			restrictedPrimes.append(x)
			break

# Generate 3 digit primes with 1, 3, 7 and 9
for a in validDigits:
	for b in validDigits:
		for c in validDigits:
			n = 100 * a + 10 * b + c
			primeChecker(n)

# Generate 4 digit primes with 1, 3, 7 and 9
for a in validDigits:
	for b in validDigits:
		for c in validDigits:
			for d in validDigits:
				n = 1000 * a + 100 * b + 10 * c + d
				primeChecker(n)

# Generate 5 digit primes with 1, 3, 7 and 9
for a in validDigits:
	for b in validDigits:
		for c in validDigits:
			for d in validDigits:
				for e in validDigits:
					n = 10000 * a + 1000 * b + 100 * c + 10 * d + e
					primeChecker(n)

# Generate 6 digit primes with 1, 3, 7 and 9
for a in validDigits:
	for b in validDigits:
		for c in validDigits:
			for d in validDigits:
				for e in validDigits:
					for f in validDigits:
						n = 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
						primeChecker(n)

validPrimes = []

for a in restrictedPrimes: # Rotates primes formed with valid digits and check if new numbers formed are primes
	tempSet = set()
	b = a
	x = len(str(a))
	for i in range(x - 1):
		b = int(str(b)[1:x] + str(b)[0])
		tempSet.add(b)
	print(f'{a} | {tempSet}')
	for i in tempSet:
		if i not in restrictedPrimes:
			break
	else:
		validPrimes.append(a)


print(len(validPrimes) + 13) # Includes 13 circular primes below 100 as programme only checks primes above 100

end = time.time()

print(end - start) # Executes in 0.508 seconds