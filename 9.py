for a in range(999):
	for b in range(999):
		for c in range(999):
			if a < b < c and a + b + c == 1000 and a ** 2 + b** 2 == c **2:
				print(a * b * c)
