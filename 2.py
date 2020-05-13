a = 1
b = 2
sum = 2
print(a)
print(b)

while a+b < 4000000:
	a = a + b
	if a % 2 == 0:
		sum += a
	b = a + b
	if b % 2 == 0:
		sum += b

print(sum)
