'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time

start = time.time()

from math import sqrt, fabs

from itertools import permutations

# Check if number, x, is prime
def primeChecker(x):
	for d in range(2, int(sqrt(x)) + 1):
		if x % d == 0:
			return False
	return True

primes = set()

for n in range(1489, 10000): # 1487 is the first case
	if primeChecker(n) == True:
		primes.add(n)

# Excludes example in output
primes.remove(4817) 
primes.remove(8147)

for prime in primes: # Iterates through 4 digit primes
	tempPermutations = list(permutations(str(prime))) # Generate permutations of prime
	tempSet = set()
	for tuples in tempPermutations:
		tempSet.add(''.join(tuples)) # Unique permutations of prime
	if len(tempSet) >= 3: # Prime needs to have at least 3 unique permutations including itself
		for strings in tempSet:
			if int(strings) > 1000:
				if primeChecker(int(strings)) == True and int(strings) != prime:
					diff = int(fabs(int(strings) - prime))
					a = (prime + diff)
					if str(a) in tempSet and a != int(strings) and a in primes:
						print(f'{int(strings)}{prime}{a}')
						break

end = time.time()

print(end - start) # Executed in 0.102 seconds