import time

start = time.time()

from itertools import permutations

from math import sqrt


def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def solution():
    digit_string = '123456789'
    length = 9
    while True:
        permuted_numbers = []
        for digits in list(permutations(digit_string)):
            permuted_numbers.append(int(''.join(digits)))
        permuted_numbers.sort(reverse=True)
        for permutation in permuted_numbers:
            if prime_checker(permutation):
                return permutation
                break
        digit_string = digit_string.replace(str(length), '')
        length -= 1


print(solution())

end = time.time()

# Executes in 0.282 seconds
print(end - start)
