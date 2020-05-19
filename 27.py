'''
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form: n**2 + an + b, where |a| < 1000 and |b| ≤ 1000 and |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

# Generate odd prime numbers <= 1000 using Sieve of Eratosthenes for b as b has to be prime. The only prime numbers left out is b = 2.

import time

start = time.time()

b = []

def sieve(n): # From GeeksforGeeks       
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n):          
        if (prime[p] == True): # If prime[p] is not changed, then it is a prime 
            for i in range(p * 2, n + 1, p): # Update all multiples of p 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    prime[2]= False # Excludes even primes e.g. 2
    for p in range(n + 1): # Appends all odd prime numbers to list representing possible values of b
        if prime[p]:
        	b.append(p) 
             
sieve(999) 

import math

# Function to check if quadratic expression generates primes and the largest value of n for which quadratic expression is prime for all integers ≤ n. Returns product of a and b for current largest value of n.

def quadraticPrimeGenerator(quadratic):
	y = 2
	global n
	global currentMax
	while quadratic > 0:
		if quadratic % y == 0 and int(math.sqrt(quadratic)) >= y:
			break
		elif int(math.sqrt(quadratic)) >= y:
			y += 1
		else:
			n += 1
			quadratic = (n**2 + a * n + x)
			y = 2
	if n > currentMax:
			currentMax = n - 1
			print(str(currentMax) + '|' + str(a * x))

currentMax = 39 # From problem: Largest value of known n is 39

# Checking for odd prime values of b. For quadratic expression to be prime, when n = 0, b has to be prime. Since all primes except 2 are odd, first check quadratic expressions where b is an odd prime. For n = 1, 1 + a + b has to be prime as well. As such, if b is odd, a has to be a negative or positive odd number. Result: n**2 - 61n + 971 are primes for 0 ≤ n ≤ 70.

for a in range(-999, 1000, 2):
	for x in b:
		n = 0
		quadraticPrimeGenerator(n**2 + a * n + x)
		
# Checking for b = 2. Since b is now even, a has to be even so that n**2 + an + b is prime for n = 1.

for a in range(-998, 999, 2): 
	n = 0
	x = 2
	quadraticPrimeGenerator(n**2 + a * n + 2)
	
end = time.time()
print(end - start) # Programme takes 2.81 seconds to execute
