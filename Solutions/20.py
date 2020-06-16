'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time

start = time.time()

from math import factorial as fac

factorial_of_100 = fac(100)

sum_of_digits = 0

while factorial_of_100: # Sums digits in number by diving by 10 and adding to existing sum
	sum_of_digits += factorial_of_100 % 10
	factorial_of_100 //= 10

print(sum_of_digits)

end = time.time()

print(end - start) # Executed in 0.0 seconds




