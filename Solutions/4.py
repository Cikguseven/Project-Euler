'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time

start = time.time()

largest = 0

for a in range(999, 99, -1):
	for b in range(999, 99, -1):
		if a * b > largest:
			if str(a * b)[::-1] == str(a * b):
				largest = a * b
				break
			else:
				continue
		break

print(largest)

end = time.time()

print(end - start) # Executed in 0.00901 seconds
