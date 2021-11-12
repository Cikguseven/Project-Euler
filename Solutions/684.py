import time

start = time.time()


def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def s(n):
    if n < 10:
        return n
    else:
        i = 10
        while True:
            if sum_of_digits(i) == n:
                return i
            i += 1


def S(n):
    x = 0
    for i in range(1, n + 1):
        x += value_pairs[i]
    return x


value_pairs = {}

for n in range(9):
    value_pairs[n] = n


while True:
    n = 9
    for j in range(1, 11):
        for i in range(1, 10):
            value_pairs[n] = (i * (10 ** j) - 1)
            n += 1
    break

for i in range(99):
    print(S(i))

'''
fibonacci = [0, 1, 1]

for i in range(3, 91):
    n = fibonacci[i - 1] + fibonacci[i - 1]
    fibonacci.append(n)



answer = 0

for i in range(2, 91):
    print(i)
    answer += S(i)

print(answer % 1000000007)
'''
end = time.time()

# Executes in 0.00100 seconds
print(end - start)
