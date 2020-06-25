'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

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
    multiples = []
    product = 0
    i = 1
    while product < 1000:
        product = i * n
        i += 1
        multiples.append(product)
    multiples.pop()
    multiples = list(map(str, multiples))
    multiples = list(map(converter, multiples))
    return multiples


# Combines valid multiples
def concat(a, b):
    sub_strings = []
    for i in a:
        for j in b:
            if i[:2] == j[1:] and len(set(j[0] + i)) == len(j[0] + i):
                sub_strings.append(j[0] + i)
    return sub_strings


# Adds missing digit to valid pandigital numbers
def missing(pandigital_string):
    for digit in '0123456789':
        if digit not in pandigital_string:
            return digit + pandigital_string


multiples = [m(17), m(13), m(11), m(7), m(5), m(3), m(2)]

solution = reduce(concat, multiples)

solution = map(missing, solution)

solution = map(int, solution)

print(sum(solution))

end = time.time()

# Executes in 0.0110 seconds
print(end - start)
