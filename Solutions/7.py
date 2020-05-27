'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time

start = time.time()

import math

primes = [2, 3, 5, 7, 11]
n = 13
d = 2

# Generate primes from odd numbers starting from 13 (n) and appends prime numbers to list, primes, until 10 001 prime numbers are obtained
while len(primes) < 10002: 
	# If numbers less than its square root are proper divisors of n, it is not prime and proceeds to next odd number
	if n % d == 0 and int(math.sqrt(n)) >= d: 
		n += 2
		d = 2
	# Test the next divisor if it is still smaller than the square root of n
	elif int(math.sqrt(n)) >= d: 
		d += 1
	# Number is prime and appended to list primes
	else: 
		primes.append(n)
		n += 2
		d = 2
			
print(primes[10000]) # Displays the 10 001st prime number

end = time.time()

print(end - start) # Programme takes 2.20 seconds to execute