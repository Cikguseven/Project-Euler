'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import time

start = time.time()

from math import floor, log2

validNumbers = []

# In-built decimal to binary converter
def decToBin(n): 
    return bin(n).replace("0b", "")

# Check for odd numbers which are palindromes. Even numbers can be excluded as last digit of equivalent binary would be 0 and will not have a valid palindrome
for i in range(1, 1000000, 2): 
	binaryNumber = decToBin(i)
	if str(i) == str(i)[::-1] and str(binaryNumber) == str(binaryNumber)[::-1]:
		print(f'{i} | {binaryNumber}')
		validNumbers.append(i)

print(sum(validNumbers))

end = time.time()

print(end - start) # Executed in 0.680 seconds





