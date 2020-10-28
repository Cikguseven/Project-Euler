import time

start = time.time()

n = 1


def checker(n):
    digits = set(str(n))
    for i in range(6, 1, -1):
        if set(str(n * i)) != digits:
            return False
    return True


while True:
    if checker(n):
        print(n)
        break
    n += 1

end = time.time()

# Executes in 0.287 seconds
print(end - start)
