'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import time

start = time.time()

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\22_names.txt', current_path)

name_file = open(new_path, 'r')

name_list = sorted(name_file.read().replace('"','').split(','),key=str)

letter_to_number_dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22 , "W": 23, "X": 24, "Y": 25, "Z": 26}

def letter_to_number(name): # Converts letters in name to equivalent numerical value
	name_sum = 0
	for i in name:
		name_sum += letter_to_number_dic[i]
	return name_sum

total_score = 0

for names in name_list: # Sums product of numerical value of name and rank in alphabetical order
	total_score += letter_to_number(names) * (name_list.index(names) + 1)
	
print(total_score)

name_file.close()

end = time.time()

print(end - start) # Executed in 0.247 seconds

