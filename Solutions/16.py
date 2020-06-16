'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

import time

start = time.time()

solution = 0

for i in str(2 ** 1000):
	solution += int(i)

print(solution)

end = time.time()

print(end - start) # Executed in 0.0 seconds
