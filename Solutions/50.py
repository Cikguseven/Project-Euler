'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import time

start = time.time()

from math import sqrt

def primeChecker(n):
	for d in range(2, int(sqrt(n)) + 1):
		if n % d == 0:
			return False
	return True

i = 3

totalSum = 2

primes = [2]

c = 0

while totalSum + i < 10 ** 6:
	if primeChecker(i) == True:
		totalSum += i
		primes.append(i)
	i += 2

print(primes)

while True:
	if primeChecker(totalSum) == False:
		totalSum -= primes[c]
		c += 1
	else:
		print(totalSum)
		break

end = time.time()

print(end - start)
