'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''

import time

start = time.time()

pentagonalNumbers = [0]

for n in range(1, 2168):
	pentagonalNumbers.append(int((n * (3 * n - 1)) / 2))

def pentagonal(n):
    if (1 + (24 * n + 1) ** 0.5) % 6 == 0:
        return True
    return False

for i in range(1, 2168):
	for j in range(i + 1, 2168):
		add = pentagonalNumbers[i] + pentagonalNumbers[j]
		if pentagonal(add):
			minus = pentagonalNumbers[j] - pentagonalNumbers[i]
			if pentagonal(minus):
				print(f'{minus}')

end = time.time()

print(end - start) # Executed in 2.19 seconds