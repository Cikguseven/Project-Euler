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

from functools import reduce

# Creates three digit number by adding zeros to the front
def converter(n):
    if len(n) < 3:
        return '0' * (3 - len(n)) + n
    return n

# Generate multiples of given number under 1000
def m(n):
    multiples_of_n = []
    product = 0
    i = 1
    while product < 1000:
        product = i * n
        i += 1
        multiples_of_n.append(product)
    multiples_of_n.pop()
    multiples_of_n = list(map(str, multiples_of_n))
    multiples_of_n = list(map(converter, multiples_of_n))
    return multiples_of_n

def concat(a, b):
    sub_strings = []
    for i in a:
        for j in b:
            if i[:2] == j[1:] and len(set(j[0] + i)) == len(j[0] + i):
                sub_strings.append(j[0] + i)
    return sub_strings
    
def missing(pandigital_string):
    for digit in '0123456789':
        if digit not in pandigital_string:
            return digit + pandigital_string

# Generating multiples of 2, 3, 5, 7, 11, 13 & 17
multiples = [m(17), m(13), m(11), m(7), m(5), m(3), m(2)]

# Combining valid multiples
solution = reduce(concat, multiples)

# Adding the missing digit to valid pandigital numbers
solution = map(missing, solution)

# Converting the valid pandigital numbers to integers
solution = map(int, solution)

print(sum(solution))

end = time.time()

print(end - start) # Executed in 0.0110 seconds

