import time

start = time.time()

solution = 0

for n in range(10, 354294):
    digit_sum = 0
    for digits in str(n):
        digit_sum += int(digits) ** 5
    if digit_sum == n:
        solution += n

print(solution)

end = time.time()

# Executes in 1.34 seconds
print(end - start)
