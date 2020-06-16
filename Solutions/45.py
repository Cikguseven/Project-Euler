'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

import time

start = time.time()

# Test for pentagonal numbers from Wikipedia
def pentagonal(n): 
	if (((24 * n + 1) ** 0.5) + 1) % 6 == 0:
		return True
	return False

# Test for hexagonal numbers from Wikipedia
def hexagonal(n): 
	if (((8 * n + 1) ** 0.5) + 1) % 4 == 0:
		return True
	return False

i = 286

flag = True

while flag:
	triangle_number = int((i * (i + 1)) / 2)
	if pentagonal(triangle_number) and hexagonal(triangle_number):
		print(triangle_number)
		flag = False
		break
	i += 1

end = time.time()

print(end - start) # Executed in 0.0861 seconds