import time

start = time.time()


modulo = 1000000007


def s(n):
    start = str(n % 9)
    end = '9' * (n // 9)
    return int(start + end) % modulo


def S(n):
    if n < 10:
        return n
    else:
        x = (n // 9) % modulo
        y = (n % 9) % modulo
        return str((45 * int('1' * x)) - (9 * x) + (((y + 1) / 2)
                                                    * (s(n - y) + s(n))
                                                    ) % modulo)


'''
def S(n):
    k = n // 9
    r = 2 + (k % 9)
    return str((((((r - 1) * r) + 10) * ((10 ** n) % modulo)
    - 2 * (r + (9 * n) + 4)) // 2) % modulo)
'''

print(S(3524578))


'''
fibonacci = [0, 1, 1]

for i in range(3, 17):
    n = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(n)


for f in fibonacci:
    print(value_pairs[f])


answer = 0

for i in range(2, 91):
    print(i)
    answer += S(i)

print(answer % 1000000007)

'''
end = time.time()

# Executes in 0.00100 seconds
print(end - start)
