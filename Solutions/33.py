'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import time

start = time.time()

from math import prod
from fractions import Fraction

numerators = []
denominators = []

for n in range(10, 100): # Iterating numerators, n
	for d in range(n + 1, 100): # Iterating denominators, j, which are larger than numerators for fraction, k, to be less than 1.
		f = n / d
		if n != d: # Eliminates trivial examples where numerator and denominator are the same
			# Checks if any digits in numerator and denominator are the same
			for a in str(n): # Iterates through digits in numerator
				for b in str(d): # Iterates through digits in denominator
					if int(a) == int(b) and int(a) != 0: # Eliminates trivial examples where trailing zeros are cancelled
						newN = str(n).replace(a, '', 1) # Creates new numerator by eliminating common digit
						newD = str(d).replace(b, '', 1) # Creates new denominator by eliminating common digit
						if int(newD) != 0 and int(newN) / int(newD) == f: # Prevents division by 0 and checks if new fraction after cancelling is equal to old fraction
								numerators.append(n) 
								denominators.append(d)

fraction = Fraction(prod(numerators), prod(denominators)) # Simplest form of fraction of products of all valid numerators divided by products of all valid denominator
print(fraction.denominator) 

end = time.time()

print(end - start) # Executed in 0.0312 seconds

								




