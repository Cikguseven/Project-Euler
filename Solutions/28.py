import time

start = time.time()

n = 1

solution = 1

# Add numbers that lie on 2 by 2 spiral till 1001 by 1001 spiral. The 4
# numbers in the same n by n spiral have the same difference.
for i in range(2, 1002, 2):
    for j in range(4):
        n += i
        solution += n

print(solution)

end = time.time()

# Executes in 0.0 seconds
print(end - start)
