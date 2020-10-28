import time

start = time.time()

flag = True

n = 1

pentagonal_numbers = []


# Test for pentagonal numbers from Wikipedia
def pentagonal(n):
    if (((24 * n + 1) ** 0.5) + 1) % 6 == 0:
        return True
    return False


while flag:
    pk = int((n * (3 * n - 1)) / 2)
    pentagonal_numbers.append(pk)
    for pj in pentagonal_numbers:
        if pentagonal(pk + pj) and pentagonal(pk - pj):
            print(pk - pj)
            flag = False
            break
    n += 1

end = time.time()

# Executes in 1.66 seconds
print(end - start)
