'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time

start = time.time()

from math import sqrt, fabs

from itertools import permutations

def prime_checker(n):
	if n % 2 == 0:
		return False
	for d in range(3, int(sqrt(n)) + 1, 2):
		if n % d == 0:
			return False
	return True

primes = [n for n in range(1000, 10000) if prime_checker(n) == True]

# Excludes example in output
primes.remove(4817) 
primes.remove(8147)

for prime in primes: 
	digit_permutations = list(permutations(str(prime))) # Generates list of digits of permutations of primes
	set_of_permutations = {''.join(tuples) for tuples in digit_permutations} # String digits to obtain unique permutations of prime and add them to set
	if len(set_of_permutations) >= 3: # Prime needs to have at least 3 unique permutations including itself
		set_of_permutations.remove(str(prime))
		set_of_permutations = sorted(map(int, set_of_permutations))
		for number in set_of_permutations:
			if prime_checker(number) == True and number > 1000:
				difference = fabs(number - prime)
				largest_permutation = int(number + difference)
				if largest_permutation in set_of_permutations and largest_permutation in primes:
					print(f'{prime}{number}{largest_permutation}')
					break

end = time.time()

print(end - start) # Executed in 0.0500 seconds