import time

start = time.time()

sum_of_squares = 0

x = 0

for i in range(1, 101):
    sum_of_squares += i ** 2
    x += i

square_of_sum = x ** 2

print(square_of_sum - sum_of_squares)

end = time.time()

# Executes in 0.0 seconds
print(end - start)
