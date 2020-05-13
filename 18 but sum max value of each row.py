pyramid = '''
3
7 4
2 4 6
8 5 9 3
'''

# Generate nested list with seperated elements
nL = []
for i in range(4):
	nL.append(pyramid.strip().split('\n')[i].split())

# Top down summation

for i in range(3):
	currentLargest = 0
	for j in range(i + 1): 
		if int(nL[i][j]) > currentLargest:
			currentLargest = int(nL[i][j])
	for k in range(i + 2):
		nL[i + 1][k] = int(nL[i + 1][k]) + currentLargest
	if i == 2:
		print(max(nL[i + 1])) # Theoretical maximum

print(nL)


