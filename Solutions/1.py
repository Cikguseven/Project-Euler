'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time

start = time.time()

valid_multiples = set()

for i in range(1, 1000000 // 3 + 1):
	valid_multiples.add(3 * i)

for i in range(1, 1000000 // 5):
	valid_multiples.add(5 * i)

print(sum(valid_multiples))

end = time.time()

# Executes in 0.0 seconds
print(end - start)
