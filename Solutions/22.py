'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

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
