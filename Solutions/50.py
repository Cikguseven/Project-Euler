'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import time

start = time.time()

def prime_sieve(n):
    is_prime = [True for i in range(n + 1)] 
    list_of_primes = []
    for i in range(4, n + 1, 2):
        is_prime[i] = False
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
        	list_of_primes.append(p) 
    return list_of_primes

primes = prime_sieve(999999)

length = 0

last_prime = len(primes)

solution = 0

for i in range(len(primes)):
	for j in range(i + length, last_prime):
		sum_of_primes = sum(primes[i:j])
		if sum_of_primes < 1000000:
			if sum_of_primes in primes and sum_of_primes > solution:
				length = j - i
				solution = sum_of_primes
		else:
			last_prime = j + 1
			break

print(solution)

end = time.time()

print(end - start) # Executed in 0.920 seconds
