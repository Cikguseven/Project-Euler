'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

import time
start = time.time()

import sys  
sys.setrecursionlimit(10**4) # Allows for calculation of d >= 541

remainders = [] # List where remainders at every step of long division is appended to
currentLongest = 0 # Length of current longest recurring decimal
currentMax = 0 # Number with current longest recurring decimals when 1 divides it 

def rLD(a, b, i): # Recursive long division to obtain length of recurring decimals
	global currentLongest
	global currentMax
	if a % b == 0: # Terminates function if long division has no remainder at any step
		return
	elif str(a) in remainders: # Terminates function if remainder repeats and returns length of recurring decimal
		if (len(remainders) - remainders.index(str(a))) > currentLongest:
			currentLongest = (len(remainders) - remainders.index(str(a)))
			currentMax = b
		return
	elif a // b == 0: # 'Shifts' a decimal place if dividend is too small to obtain quotient
		if i >= 1:
			remainders.append(str(0))
		a *= 10
		i += 1
		rLD(a, b, i)
	else: # Appends remainder to list and continues long division
		remainders.append(str(a))
		a = a % b
		i = 0
		rLD(a, b, i)

for j in range(1, 1001, 2): # Skip even numbers as they are observed to have very short or no recurring decimals
	rLD(1, j, 0)
	quotient = []
	remainders = []

print(currentMax)

end = time.time()
print(end - start)
