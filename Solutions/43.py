'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import time

start = time.time()

from itertools import permutations

allPermutations = list(permutations('1234567890'))

strings = []

for digits in allPermutations:
	if int(digits[3]) % 2 == 0 or digits[3] == '0':
		if digits[5] == '5' or digits[5] == '0':
			strings.append(''.join(digits))

validNumbers = []

for numbers in strings:
	if int(numbers[7:10]) % 17 == 0:
		if int(numbers[6:9]) % 13 == 0:
			if int(numbers[5:8]) % 11 == 0:
				if int(numbers[4:7]) % 7 == 0:
					if int(numbers[2:5]) % 3 == 0:
						validNumbers.append(int(''.join(numbers)))

print(sum(validNumbers))

end = time.time()

print(end - start) # Executed in 2.67 seconds

