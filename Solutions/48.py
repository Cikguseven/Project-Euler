'''
The series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 10 ** 10 = 10405071317.

Find the last ten digits of the series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 1000 ** 1000.
'''

import time

start = time.time()

x = 0

for i in range(1, 1001):
	x += i ** i

print(str(x)[-10:])

end = time.time()

print(end - start) # Executed in 0.0410 seconds