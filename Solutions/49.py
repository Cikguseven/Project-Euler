'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit x do you form by concatenating the three terms in this sequence?
'''

import time

start = time.time()

from math import sqrt, fabs

from itertools import permutations


def prime_checker(n):
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


primes = [n for n in range(1000, 10000) if prime_checker(n)]

# Excludes example in output
primes.remove(4817)

primes.remove(8147)


for prime in primes:
    digit_permutations = list(permutations(str(prime)))
    permutation_set = {''.join(tuples) for tuples in digit_permutations}
    if len(permutation_set) >= 3:
        permutation_set.remove(str(prime))
        permutation_set = sorted(map(int, permutation_set))
        for x in permutation_set:
            if prime_checker(x) and x > 1000:
                difference = fabs(x - prime)
                y = int(x + difference)
                if y in permutation_set and y in primes:
                    print(f'{prime}{x}{y}')
                    break

end = time.time()

# Executes in 0.0490 seconds
print(end - start)
