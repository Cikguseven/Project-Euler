import time

start = time.time()

# Number theory of cycle length to obtain last 10 digits of exponent of 2
last_ten_digits = str(2 ** (7830457 - 7812500))[-10:]

answer = str(28433 * int(last_ten_digits) + 1)[-10:]

print(answer)

end = time.time()

# Executes in 0.00100 seconds
print(end - start)
