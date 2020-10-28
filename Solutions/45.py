import time

start = time.time()

flag = True

n = 286


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


while flag:
    triangle_number = int((n * (n + 1)) / 2)
    if pentagonal(triangle_number) and hexagonal(triangle_number):
        print(triangle_number)
        flag = False
        break
    n += 1

end = time.time()

# Executes in 0.0587 seconds
print(end - start)
