import time

start = time.time()

valid_multiples = set()

for i in range(1, 1000000 // 3 + 1):
    valid_multiples.add(3 * i)

for i in range(1, 1000000 // 5):
    valid_multiples.add(5 * i)

print(sum(valid_multiples))

end = time.time()

# Executes in 0.0 seconds
print(end - start)
