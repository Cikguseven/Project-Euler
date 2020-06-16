'''
The series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 10 ** 10 = 10405071317.

Find the last ten digits of the series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 1000 ** 1000.
'''

import time

start = time.time()

series = 0

for n in range(1, 1001):
	series += n ** n

print(str(series)[-10:])

end = time.time()

print(end - start) # Executed in 0.0320 seconds