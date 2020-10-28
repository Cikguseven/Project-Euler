import time

start = time.time()

from math import sqrt

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\42_words.txt', current_path)

word_file = open(new_path, 'r')

word_list = sorted(word_file.read().replace('"', '').split(','), key=str)

counter = 0

for word in word_list:
    sum = 0
    for character in word:
        sum += ord(character) - 64
    if sqrt(8 * sum + 1) == int(sqrt(8 * sum + 1)):
        counter += 1

print(counter)

word_file.close()

end = time.time()

# Executes in 0.0 seconds
print(end - start)
