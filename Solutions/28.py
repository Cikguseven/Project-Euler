'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import time

start = time.time()

currentNumber = 1
totalSum = 1

for increment in range(2, 1002, 2): # Numbers in the same n x n spiral have the same difference
	for j in range(4): # 4 numbers in every n x n grid lie on the diagonal
		currentNumber += increment
		totalSum += currentNumber

print(totalSum)

end = time.time()

print(end - start)
