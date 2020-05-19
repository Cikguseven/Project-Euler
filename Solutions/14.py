'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

longestTerm = 0

def collatz(number):
	global longestTerm
	terms = []
	terms.append(number)
# Collatz sequence
	while number != 1 :
		if number % 2 == 0:
			number = number // 2
			terms.append(number)
		else:
			number = number * 3 + 1
			terms.append(number)
	if len(terms) > longestTerm:
		longestTerm = len(terms)
		print(i) # Prints number with largest collatz sequence so far

for i in range(1,1000001):
	collatz(i)



