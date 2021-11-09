import time

start = time.time()

valid = {89, 145, 42, 20, 4, 16, 37, 58, 85}

invalid = {1, 44, 32, 13, 10}


def digits_squared(n):
	current_value = 0
	for digits in str(n):
		current_value += int(digits) ** 2
	return current_value


for i in range(1, 10000):
	x = i
	flag = True
	while flag:
		if digits_squared(i) in valid:
			valid.add(x)
			flag = False
		elif digits_squared(i) in invalid:
			invalid.add(x)
			flag = False
		else:
			i = digits_squared(i)

print(len(invalid))

end = time.time()

# Executes in 0.0170 seconds
print(end - start)
