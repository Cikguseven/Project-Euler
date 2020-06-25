'''
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time

start = time.time()

from collections import Counter

perimeters = []

for a in range(1, 333):
    for b in range(a, 500):
        c = (a ** 2 + b ** 2) ** 0.5
        if c == int(c) and a + b + c <= 1000:
            perimeters.append(a + b + c)

solution = Counter(perimeters)

print(solution.most_common(1))

end = time.time()

# Executes in 0.127 seconds
print(end - start)
