'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''

import time

start = time.time()

from math import sqrt

from itertools import permutations

digit_string = '123456789'

flag = True

length = 9

solution = 0


def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


while True:
    permuted_numbers = []
    for digits in list(permutations(digit_string)):
        permuted_numbers.append(''.join(digits))
    for permutation in permuted_numbers:
        if prime_checker(int(permutation)) and int(permutation) > solution:
            solution = int(permutation)
            flag = False
    if not flag:
        break
    digit_string = digit_string.replace(str(length), '')
    length -= 1

print(solution)

end = time.time()

# Executes in 0.719 seconds
print(end - start)
