'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time

start = time.time()

# To find the least common multiple (LCM) of 1 - 20, we can consider the LCM of 2 numbers at a time starting from 2 and 3 and compare it with the susbsequent number. LCM can be found by dividing the product of two numbers by their greatest common divisor (GCD).
def gcd(a, b): # Generate GCD using Euclid's Algorithm where b > a
	remainder = 1
	while remainder != 0:
		remainder = b % a
		b = a
		a = remainder
	return b

def lcm(a, b):
	return (a * b) / gcd(a, b)

x = lcm(2, 3)

for i in range(4 , 21):
	x = lcm(i, x)

print(int(x))

end = time.time()

print(end - start) # Executed in 0.0 seconds
