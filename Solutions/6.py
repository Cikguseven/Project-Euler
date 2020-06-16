'''
The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=55^2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import time

start = time.time()

sum_of_squares = 0

x = 0

for i in range(1, 101):
	sum_of_squares += i ** 2
	x += i

square_of_sum = x ** 2

print(square_of_sum - sum_of_squares)

end = time.time()

print(end - start) # Executed in 0.0 seconds
