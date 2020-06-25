'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

import time

start = time.time()

from math import prod

from fractions import Fraction as simplest_form

numerators = []

denominators = []

for n in range(10, 100):
    for d in range(n + 1, 100):
        f = n / d
        for a in str(n):
            for b in str(d):
                if int(a) == int(b) and int(a) != 0:
                    new_n = str(n).replace(a, '', 1)
                    new_d = str(d).replace(b, '', 1)
                    if int(new_d) != 0 and int(new_n) / int(new_d) == f:
                        numerators.append(n)
                        denominators.append(d)
                    break

solution = simplest_form(prod(numerators), prod(denominators))

print(solution)

end = time.time()

# Executes in 0.0310 seconds
print(end - start)
