import time

start = time.time()

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\22_names.txt', current_path)

name_file = open(new_path, 'r')

name_list = sorted(name_file.read().replace('"', '').split(','), key=str)

solution = 0


def letter_to_number(name):
    name_sum = 0
    for letter in name:
        name_sum += ord(letter)
    return name_sum


for names in name_list:
    solution += letter_to_number(names) * (name_list.index(names) + 1)

print(solution)

name_file.close()

end = time.time()

# Executes in 0.238 seconds
print(end - start)
