pyramid = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

# Generate nested list with seperated elements
nL = []
for i in range(15):
	nL.append(pyramid.strip().split('\n')[i].split())

# Top down summation
for i in range(15):
	if i == 0:
		for k in range(2):
			nL[1][k] = int(nL[1][k]) + int(nL[0][0])
	elif i > 1:
		nL[i][0] = int(nL[i - 1][0]) + int(nL[i][0])
		nL[i][i] = int(nL[i - 1][i - 1]) + int(nL[i][i])
		for j in range(1, i): 
			if int(nL[i - 1][j - 1]) > int(nL[i - 1][j]):
				nL[i][j] = int(nL[i - 1][j - 1]) + int(nL[i][j])
			else:
				nL[i][j] = int(nL[i - 1][j]) + int(nL[i][j])

print(max(nL[14]))





