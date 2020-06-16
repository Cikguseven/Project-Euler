'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import time

start = time.time()

n = 600851475143

d = 2

while d < n:
	if n % d == 0:
		n /= d
		d -= 1
	d += 1

print(int(n))

end = time.time()

print(end - start) # Executed in 0.00200 seconds
