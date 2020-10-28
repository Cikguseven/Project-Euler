import time

start = time.time()

solution = 0


def lychrel_test(n):
    for i in range(50):
        result = n + int(str(n)[::-1])
        if str(result) == str(result)[::-1]:
            return False
        n = result
    return True


for n in range(1, 10000):
    if lychrel_test(n):
        solution += 1

print(solution)

end = time.time()

# Executes in 0.0608 seconds
print(end - start)
