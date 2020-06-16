'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import time

start = time.time()

solution = 0

for n in range(10, 354294): 
	digit_sum = 0
	for digits in str(n):
		digit_sum += int(digits) ** 5
	if digit_sum == n:
		solution += n

print(solution)
		
end = time.time()

print(end - start) # Executed in 1.37 seconds
