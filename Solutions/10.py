'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import time

start = time.time()

def prime_sieve(n):
    is_prime = [True for i in range(n + 1)] 
    primes = []
    for p in range(4, n + 1, 2): # All even p except 2 are not prime
        is_prime[p] = False
    p = 3
    while (p * p <= n):          
        if (is_prime[p] == True): # If prime[p] is not changed, then it is a prime 
            for i in range(p * 2, n + 1, p): # Update all multiples of p 
                is_prime[i] = False
        p += 2
    is_prime[0]= False
    is_prime[1]= False
    for p in range(3, n + 1, 2): # Appends all odd prime numbers to list representing possible values of b
        if is_prime[p]:
        	primes.append(p) 
    return primes

print(sum(prime_sieve(2000000)))
			
end = time.time()

print(end - start) # Executed in 0.634 seconds
