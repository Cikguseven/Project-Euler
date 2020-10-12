'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
'''

import time

start = time.time()

n = 1

solution = 1

# Add numbers that lie on 2 by 2 spiral till 1001 by 1001 spiral. The 4
# numbers in the same n by n spiral have the same difference.
for i in range(2, 1002, 2):
    for j in range(4):
        n += i
        solution += n

print(solution)

end = time.time()

# Executes in 0.0 seconds
print(end - start)
