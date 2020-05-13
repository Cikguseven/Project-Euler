import math

x = [2, 3, 5, 7, 11, 13, 17]
i = 19
j = 2
csum = 17 + 11 + 13 + 17
while i < 2000000:
		if i%j == 0 and int(math.sqrt(i)) >= j:
			i += 2
			j = 2
		elif int(math.sqrt(i)) >= j:
			j += 1
		else:
			csum += i
			x.append(i)
			i += 2
			j = 2
			
print(csum)