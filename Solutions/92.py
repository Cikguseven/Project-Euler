import time

start = time.time()

from itertools import combinations_with_replacement
from itertools import permutations


valid = {89, 145, 42, 20, 4, 16, 37, 58, 85}

invalid = {1, 44, 32, 13, 10}


def digits_squared(n):
	current_value = 0
	for digits in str(n):
		current_value += int(digits) ** 2
	return current_value

def chain_checker(n):
	if n in valid:
		

numbers_under_k = []

combinations = list(combinations_with_replacement('0123456789', 3))

print(combinations)

new_combinations = []

for groups in combinations:
	str_of_int = ''
	for digits in groups:
		str_of_int += digits
	new_combinations.append(int(str_of_int))

print(new_combinations)


len(set(permutations('2211', 4)))

end = time.time()

# Executes in 0.0170 seconds
print(end - start)
