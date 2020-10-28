import time

start = time.time()

solution = 0

valid_digits = set('123456789')

# To obtain solution larger than example with 9, we can consider only
# four digit numbers. Numbers with any other digits will not give a 9
# digit concatenated product with its multiples.
# Function considers n = 9876 to 9123 in reverse order.
for n in range(9876, 9122, -1):
    product = ''
    counter = 1
    while len(product) < 9:
        product += str(n * counter)
        counter += 1
    if set(product) == valid_digits and int(product) > solution:
        solution = int(product)
        break

print(solution)

end = time.time()

# Executes in 0.00100 seconds
print(end - start)
