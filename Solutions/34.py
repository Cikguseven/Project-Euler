'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time

start = time.time()

from math import factorial as fac

validNumbers = []

for i in range(10, 100000):
	j = i
	tempSum = 0
	while i: # Modulo division in base 10 to obtain digits from number
		digit = i % 10
		tempSum += fac(digit)
		i //= 10
	if tempSum == j:
		validNumbers.append(j)	
	
print(sum(validNumbers))

end = time.time()

print(end - start) # Executed in 0.206 seconds