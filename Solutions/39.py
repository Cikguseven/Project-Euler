'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time

start = time.time()

from collections import Counter

perimeters = []

for a in range(1, 333): # Shorter non-hypotenuse side. Largest value it can take is 332.
	for b in range(a, 500): # Longer non-hypotenuse side. Largest value it can take is 499.
		c = (a ** 2 + b ** 2) ** 0.5 # Obtain value of hypotenuse using Pythagorean Theroem
		if c == int(c) and a + b + c <= 1000:
			perimeters.append(a + b + c)

p = Counter(perimeters)

print(p.most_common(1)) # Returns the value of p with the most solutions and the number of solutions

end = time.time()

print(end - start) # Executes in 0.127 seconds
