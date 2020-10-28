import time

start = time.time()

from itertools import permutations

all_permutations = list(permutations('0123456789'))

solution = ''.join(all_permutations[999999])

print(solution)

end = time.time()

# Executes in 0.697 seconds
print(end - start)
