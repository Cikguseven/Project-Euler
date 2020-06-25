'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1, 2, 3)

The same can be achieved by starting with 9 and multiplying by 1, 2,
3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be
formed as the concatenated product of an integer with (1, 2, ... , n)
where n > 1?
'''

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
