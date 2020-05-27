'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time

start = time.time()

from collections import Counter

perimeters = []

for a in range(1, 500): # Shorter non-hypotenuse side
	for b in range(a, 500): # Longer non-hypotenuse side
		c = (a ** 2 + b ** 2) ** 0.5 # Obtain value of hypotenuse using Pythagorean Theroem
		if c == int(c) and a + b + c <= 1000:
			perimeters.append(a + b + c)

x = Counter(perimeters)

print(x.most_common(1))

end = time.time()

print(end - start) # Executes in 0.165 seconds
