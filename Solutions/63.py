import time

start = time.time()

counter = 0

for n in range(1, 22):
	for a in range(1, 10):
		if 10 ** (n - 1) <= a ** n < 10 ** n:
			counter += 1

print(counter)

end = time.time()

# Executes in 0.00200 seconds
print(end - start)