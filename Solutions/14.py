import time

start = time.time()

from operator import itemgetter

dict = {n: 0 for n in range(1, 1000000)}

dict[1] = 1

dict[2] = 2

for n in range(3, 1000000):
    counter = 0
    number = n
    while n > 1:
        if n < number:
            dict[number] = dict[n] + counter
            break
        if n % 2 == 0:
            n /= 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1

print(max(dict.items(), key=itemgetter(1))[0])

end = time.time()

# Executes in 3.39 seconds
print(end - start)
