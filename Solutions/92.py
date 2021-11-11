import time

start = time.time()

from itertools import permutations
from itertools import combinations_with_replacement

counter = 0

digits_and_permutations = {}

valid = {89, 145, 42, 20, 4, 16, 37, 58, 85}

invalid = {1, 44, 32, 13, 10}


def digits_squared(n):
    current_value = 0
    for digits in str(n):
        current_value += int(digits) ** 2
    return current_value


def chain_checker(n):
    local_chain = set()
    while True:
        if n in valid:
            valid.update(local_chain)
            return True
        elif n in invalid:
            invalid.update(local_chain)
            return False
        else:
            local_chain.add(n)
            n = digits_squared(n)


# Represents all whole numbers below 10 million in terms of unique combination
# of digits. Reduces problem to 11440 unique combinations.
combinations = list(combinations_with_replacement('0123456789', 7))

combinations.pop(0)

# Converts string of digits to integers and evaluates the number of
# permutations for each combination.
for groups in combinations:
    int_str = ''
    for digits in groups:
        int_str += digits
    digits_and_permutations[int(int_str)] = len(set(permutations(int_str, 7)))

for digits in digits_and_permutations:
    if chain_checker(digits):
        counter += digits_and_permutations[digits]

print(counter)

end = time.time()

# Executes in 3.06 seconds
print(end - start)
