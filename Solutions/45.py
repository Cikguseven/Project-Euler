import time

start = time.time()


# Test for pentagonal numbers from Wikipedia
def pentagonal(n):
    if (((24 * n + 1) ** 0.5) + 1) % 6 == 0:
        return True
    return False


# Test for hexagonal numbers from Wikipedia
def hexagonal(n):
    if (((8 * n + 1) ** 0.5) + 1) % 4 == 0:
        return True
    return False


n = 286

while True:
    triangle_number = int((n * (n + 1)) / 2)
    if not pentagonal(triangle_number):
        n += 1
        continue
    if not hexagonal(triangle_number):
        n += 1
        continue
    print(triangle_number)
    break

end = time.time()

# Executes in 0.0350 seconds
print(end - start)
