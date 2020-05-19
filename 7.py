'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time

start = time.time()

import math

x = [2, 3, 5, 7, 11]
i = 13
j = 2
while len(x) < 10002: # Checks if odds numbers from 13 (i) are prime and appends prime numbers to list x until 10 001 prime numbers are obtained
	if i%j == 0 and int(math.sqrt(i)) >= j: # If numbers less than its square root are proper divisors of i, it is not prime and proceeds to next odd number
		i += 2
		j = 2
	elif int(math.sqrt(i)) >= j: # Test the next divisor if it is still smaller than the square root of i
		j += 1
	else: # Number is prime and appended to list x
		x.append(i)
		i += 2
		j = 2
			
print(x[10000]) # Displays the 10 001st prime number

end = time.time()

print(end - start) # Programme takes 2.20 seconds to execute