'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting ns finish at 1.

Which starting n, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time

start = time.time()

from operator import itemgetter

dic = {n: 0 for n in range(1,1000000)}

dic[1] = 1

dic[2] = 2

for n in range(3, 1000000):
	counter = 0
	original_number = n
	while n > 1:
		if n < original_number:
			dic[original_number] = dic[n] + counter
			break
		if n % 2 == 0:
			n /= 2
			counter += 1
		else:
			n = 3 * n + 1
			counter += 1

print(max(dic.items(), key = itemgetter(1))[0])

end = time.time()

print(end - start) # Executed in 3.95 secondsssd


