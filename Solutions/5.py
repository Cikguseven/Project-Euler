'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Obtain prime factors of numbers from 1 to 20

for i in range(4,21):
	j = 2
	pfactors = []
	while i > 1:
		if i%j == 0:
			i /= j
			pfactors.append(j)
		else:
			j += 1
	print(pfactors)

print((2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19)


