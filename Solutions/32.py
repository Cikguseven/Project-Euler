'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

import time

start = time.time()

from itertools import permutations

# The product of two numbers with M digits and N digits respectively will have
# either (M + N) digits or (M + N - 1) digits. Therefore, for the
# multiplicand, multiplier and product to have 9 unique digits in total, the
# multiplicand and multiplier can only have 1 digit and 4 digits respectively
# or 2 digits and 3 digits.

solution = set()

valid_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Function to generate valid n digit multiplier with restrictions
def multiplier_generator(n):
    for digits in str(n):
        possible_digits.remove(digits)
    digit_permutation = list(permutations(''.join(possible_digits), (5 - len(
        str(n)))))
    return [''.join(permutation) for permutation in digit_permutation]


# Test for 1 digit multiplicand and 4 digit multiplier to generate 4 digit
# product. Only have to test numbers 2-8 as having 1 as the multiplicand
# returns the multiplier and having 9 as the multiplicand gives a 5 digit
# product for all 4 digit multipliers.
for multiplicand in range(2, 9):
    possible_digits = valid_digits.copy()
    for multiplier in multiplier_generator(multiplicand):
        product = multiplicand * int(multiplier)
        clone = possible_digits.copy()
        for digits in multiplier:
            clone.remove(str(digits))
        if sorted(str(product)) == sorted(''.join(clone)):
            solution.add(product)


two_digit_numbers = [''.join(numbers) for numbers in list(permutations(
    '123456789', 2))]

# Test for 2 digit multiplicand and 3 digit multiplier
for multiplicand in two_digit_numbers:
    possible_digits = valid_digits.copy()
    for multiplier in multiplier_generator(multiplicand):
        product = int(multiplicand) * int(multiplier)
        clone = possible_digits.copy()
        for digits in multiplier:
            clone.remove(str(digits))
        if sorted(str(product)) == sorted(''.join(clone)):
            solution.add(product)

print(sum(solution))

end = time.time()

# Executes in 0.0937 seconds
print(end - start)
