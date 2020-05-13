import math

x = [2, 3, 5, 7, 11, 13]
i = 17
j = 2
while len(x) < 10002:
	if i%j == 0 and int(math.sqrt(i)) >= j:
		i += 2
		j = 2
	elif int(math.sqrt(i)) >= j:
		j += 1
	else:
		x.append(i)
		i += 2
		j = 2
			
print(x[10000])