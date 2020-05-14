'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from math import sqrt

limit = 20162 # From Wikipedia: Upper limit is 20161 and not 28123
x = 0
abn = set()

def d(n):
	x = 1
	y = sqrt(n)
	for i in range(2, int(y) + 1): # Check for proper divisors starting from 2
		if n % i == 0:
			x += i 
			if n / i != i: # Prevents counting the square root twice
				x += n / i
	return x

for n in range(1, limit):
	if d(n) > n:
		abn.add(n)
	if not any((n-a in abn) for a in abn ):
		x += n

print(x) # Sum of triangular numbers from 1 to 20161: 203243041. x must be lower than this theoretical limit.
