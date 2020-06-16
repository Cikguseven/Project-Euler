'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time

start = time.time()

from math import factorial as fac

from itertools import combinations_with_replacement

valid_numbers = []

for length in range(2, 8): # Numbers have to be between 10 and 1499999
	for string_of_digits in combinations_with_replacement('0123456789', length): # Addition of factorial of digits is commutative and testin can be restricted to unique combinations of digits
		sum_of_digits_factorial = sum([fac(int(digit)) for digit in string_of_digits])
		if sorted(str(sum_of_digits_factorial)) == sorted(string_of_digits):
			valid_numbers.append(sum_of_digits_factorial)
		
print(sum(valid_numbers))

end = time.time()

print(end - start) # Executed in 0.0641 seconds