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

wordFile = open(new_path, 'r')

wordList = sorted(wordFile.read().replace('"','').split(','),key=str)

letterToNumDict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22 , "W": 23, "X": 24, "Y": 25, "Z": 26}

counter = 0

def letterToNum(word): # Converts letters in word to equivalent numerical value
	global counter
	x = 0
	for character in word:
		x += letterToNumDict[character]
	if x in triangleNumbers:
		counter += 1

triangleNumbers = []

for i in range(1, 21): # Largest word value in file is 192 
	triangleNumbers.append(int((i ** 2 + i) / 2))

for word in wordList:
	letterToNum(word)

print(counter)

wordFile.close()

end = time.time()

print(end - start) # Executed in 0.00400 seconds

