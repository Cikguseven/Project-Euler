import time

start = time.time()

pentagonal_numbers = []


# Test for pentagonal numbers from Wikipedia
def pentagonal(n):
    if (((24 * n + 1) ** 0.5) + 1) % 6 == 0:
        return True
    return False


def pair():
    n = 1
    while True:
        pk = int((n * (3 * n - 1)) / 2)
        pentagonal_numbers.append(pk)
        for pj in pentagonal_numbers:
            if pentagonal(pk + pj) and pentagonal(pk - pj):
                return (pk - pj)
        n += 1


print(pair())

end = time.time()

# Executes in 0.860 seconds
print(end - start)
