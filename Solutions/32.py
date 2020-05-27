'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

# The product of two numbers with M digits and N digits respectively will have either (M + N) digits or (M + N - 1) digits. Therefore, for the multiplicand, multiplier and product to have 9 unique digits in total, the multiplicand and multiplier can only have 1 digit and 4 digits respectively or 2 digits and 3 digits.
import time

start = time.time()

from itertools import permutations

validProducts = set() # Obtains unique products as products may be obtained more than once

# Function to generate valid n digit number for multiplier with conditions
def validNumberGenerator(x): 
	# Remove digits in multiplicand from valid digits
	if len(str(x)) > 1:
		for j in str(x):
			possible.remove(j)
	else:
		possible.remove(str(x))
	y = ''.join(possible) # Generate string of remaining valid digits
	z = list(permutations(y, (5 - len(str(x))))) # List of tuples containing all valid permutations of 4 digit numbers 
	for a in z: # Creates list of all valid numbers in strings
		validStrings.append(''.join(a))

# Test for 1 digit multiplicand and 4 digit multiplier to generate 4 digit product. Only have to test numbers 2-8 as having 1 as the multiplicand returns the same multiplier and having 9 as the multiplicand generates a 5 digit product for all 4 digit multipliers.
for i in range(2, 9):
	possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	validStrings = []
	validNumberGenerator(i)
	for string in validStrings:
		j = int(i) * int(string)
		for c in string:
			possible.remove(c)
		if sorted(str(j)) == sorted(''.join(possible)):
			validProducts.add(j)
		for c in string:
			possible.append(c)

# Generate valid 2 digit numbers
a = list(permutations('123456789', 2))
valid2DigitNumbers = []
for b in a:
	valid2DigitNumbers.append(''.join(b))

# Test for 2 digit multiplicand and 3 digit multiplier
for i in valid2DigitNumbers:
	possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	validStrings = []
	validNumberGenerator(i)
	for string in validStrings:
		j = int(i) * int(string)
		for c in string:
			possible.remove(c)
		if sorted(str(j)) == sorted(''.join(possible)):
			validProducts.add(j)
		for c in string:
			possible.append(c)

# Calculate total sum of valid unique products
print(sum(validProducts))

end = time.time()
print(end - start) # Executed in 0.104 seconds



