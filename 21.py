fsum = 0 

for i in range(2, 10001):
	csum = 0
	dsum = 0
	for j in range(1, i):
		if i%j == 0:
			csum += j
	for k in range(1, csum):
		if csum%k == 0:
			dsum += k
	if dsum == i and csum != dsum:
		fsum += i
	print(fsum)


