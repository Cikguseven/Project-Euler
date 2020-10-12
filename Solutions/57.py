import time

start = time.time()

n = 1

d = 1

solution = 0

for i in range(1000):
    new_n = n + 2*d
    new_d = n + d
    if len(str(new_n)) > len(str(new_d)):
        solution += 1
    n = new_n
    d = new_d

print(solution)

end = time.time()

# Executed in 0.0156 seconds
print(end - start)
