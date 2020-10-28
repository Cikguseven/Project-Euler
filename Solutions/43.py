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
