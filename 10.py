'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

i = 11
j = 2
csum = 17 

while i < 2000000:
		if i%j == 0 and int(math.sqrt(i)) >= j:
			i += 2
			j = 2
		elif int(math.sqrt(i)) >= j:
			j += 1
		else:
			csum += i
			i += 2
			j = 2
			
print(csum)