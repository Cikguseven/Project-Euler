'''
The series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 10 ** 10 = 10405071317.

Find the last ten digits of the series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 1000
** 1000.
'''

import time

start = time.time()

solution = 0

for n in range(1, 1001):
    solution += n ** n

print(str(solution)[-10:])

end = time.time()

# Executes in 0.0310 seconds
print(end - start)
