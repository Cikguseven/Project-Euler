'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import time

start = time.time()

from math import sqrt

from itertools import permutations

def prime_checker(x):
	for d in range(2, int(sqrt(x)) + 1):
		if x % d == 0:
			return False
	return True

largest = 0

n = 9

valid_digits = '123456789'

flag = True

# Checks for largest pandigital number starting from numbers that uses all 9 digits and works backwards
while flag:
	string_of_digits = valid_digits
	digit_permutations = list(permutations(string_of_digits))
	all_numbers = []
	for digits in digit_permutations:
		all_numbers.append(''.join(digits)) 
	for numbers in all_numbers:
		if prime_checker(int(numbers)) == True and int(numbers) > largest:
			largest = int(numbers)
			flag = False
	valid_digits = string_of_digits.replace(str(n), '')
	n -= 1

print(largest)
				
end = time.time()
 
print(end - start) # Executed in 0.953 seconds