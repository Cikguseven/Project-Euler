import math
triNum = 0
while True:
	for i in range(1, 100000000):
		divisors = []
		triNum += i
		for j in range(1, int(math.isqrt(triNum)) + 1):
			if triNum%j == 0:
				divisors.append(j)
		if len(divisors) > 250:
			print(triNum)