def fds(a):
	x = 1
	y = 0
	for i in range(2, a + 1):
		x *= i
	while x:
		y += x % 10
		x //= 10
	print(y)

fds(100)




