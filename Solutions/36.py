'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''

import time

start = time.time()

solution = []


def decimal_to_binary(n):
    return str(bin(n).replace("0b", ""))


# Check for palindromic odd numbers. Even numbers can be excluded as last
# digit of equivalent binary will be 0 and will not have a valid palindrome.
for n in range(1, 1000000, 2):
    if str(n) == str(n)[::-1] and decimal_to_binary(n) == \
            decimal_to_binary(n)[::-1]:
        solution.append(n)

print(sum(solution))

end = time.time()

# Executes in 0.391 seconds
print(end - start)
