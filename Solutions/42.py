'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import time

start = time.time()

import os

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\42_words.txt', cur_path)

word_file = open(new_path, 'r')

word_list = sorted(word_file.read().replace('"','').split(','), key = str)

letter_to_number_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22 , "W": 23, "X": 24, "Y": 25, "Z": 26}

counter = 0

def letter_to_number(word): # Converts letters in word to equivalent numerical value
	global counter
	sum = 0
	for character in word:
		sum += letter_to_number_dictionary[character]
	if sum in triangle_numbers:
		counter += 1

triangle_numbers = []

for i in range(1, 21): # Largest word value in file is 192 
	triangle_numbers.append(int((i ** 2 + i) / 2))

for word in word_list:
	letter_to_number(word)

print(counter)

word_file.close()

end = time.time()

print(end - start) # Executed in 0.0156 seconds

