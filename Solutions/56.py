import time

start = time.time()

solution = 0

for a in range(2, 100):
    for b in range(2, 100):
        result = str(a ** b)
        digital_sum = 0
        for digits in result:
            digital_sum += int(digits)
        if digital_sum > solution:
            solution = digital_sum

print(solution)

end = time.time()

# Executed in 0.258 seconds
print(end - start)
