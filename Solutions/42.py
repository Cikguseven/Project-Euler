'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''

import time

start = time.time()

from math import sqrt

import os

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\42_words.txt', cur_path)

word_file = open(new_path, 'r')

word_list = sorted(word_file.read().replace('"', '').split(','), key=str)

counter = 0

triangle_numbers = []


def letter_to_number(word):
    global counter
    sum = 0
    for character in word:
        sum += ord(character) - 64
    if sqrt(8 * sum + 1) == int(sqrt(8 * sum + 1)):
        counter += 1


for word in word_list:
    letter_to_number(word)

print(counter)

word_file.close()

end = time.time()

# Executes in 0.00400 seconds
print(end - start)
