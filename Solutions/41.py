'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import time

start = time.time()

from math import sqrt

from itertools import permutations

def primeChecker(x):
	for d in range(2, int(sqrt(x)) + 1):
		if x % d == 0 and x != d:
			return False
	return True

currentMax = 0

currentString = ''

for i in range(1, 10):
	currentString += str(i)
	x = list(permutations(currentString))
	y = []
	for digits in x:
		y.append(''.join(digits)) 
	for numbers in y:
		if numbers[0] != 0 and primeChecker(int(numbers)) == True and int(numbers) > currentMax:
			currentMax = int(numbers)

print(currentMax)
				
end = time.time()
 
print(end - start) # Executed in 0.996 seconds