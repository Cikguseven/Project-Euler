'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import math

factors = set()
nonprimefactors = set()
def lpf(n):
	for i in range(2, int(math.isqrt(n)) + 1):
		if n%i == 0:
			factors.add(i)
			if n/i != i:
				factors.add(int(n/i))
	for j in factors:
		for k in range(2, int(math.isqrt(j)) + 1):
			if j%k == 0:
				nonprimefactors.add(j)
	x = sorted(set(sorted(factors)) - set(sorted(nonprimefactors)))
	print(max(x))

lpf(600851475143)




