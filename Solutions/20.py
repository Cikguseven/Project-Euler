'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def fds(a):
	x = 1
	y = 0
	for i in range(2, a + 1): # Factorial of a
		x *= i
	while x: # Sums digits in number by diving by 10 and adding to existing sum
		y += x % 10
		x //= 10
	print(y)

fds(100)




