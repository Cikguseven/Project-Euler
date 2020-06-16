'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import time

start = time.time()

from itertools import permutations

# List of all permutations in order with digits 0-9
all_permutations = list(permutations('0123456789'))

# Get millionth permutation and join digits in tuple together
result = ''.join(all_permutations[999999])

print(result)

end = time.time()

print(end - start) # Executed in 0.697 seconds

