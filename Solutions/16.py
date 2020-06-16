'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

import time

start = time.time()

value = 2 ** 1000
sum = 0

for i in str(value):
	sum += int(i)

print(sum)

end = time.time()

print(end - start) # Executed in 0.0 seconds