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
