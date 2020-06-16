'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import time

start = time.time()

from math import floor, log2

valid_numbers = []

# In-built decimal to binary converter
def decimal_to_binary(n): 
    return str(bin(n).replace("0b", ""))

# Check for odd numbers which are palindromes. Even numbers can be excluded as last digit of equivalent binary will be 0 and will not have a valid palindrome.
for n in range(1, 1000000, 2): 
	if str(n) == str(n)[::-1] and decimal_to_binary(n) == decimal_to_binary(n)[::-1]:
		valid_numbers.append(n)

print(sum(valid_numbers))

end = time.time()

print(end - start) # Executed in 0.397 seconds