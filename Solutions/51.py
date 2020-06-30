'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.
'''

import time

start = time.time()

from math import sqrt

# Only numbers with 3 replaceable digits (not including last digit) have to be
# considered for an eight prime value family. These primes must have at least
# one member having 0, 1 or 2 as the digit being replaced.


# Replaces either 0, 1 or 2 in digits except last to check if other members of
# family are primes
def checker(digit, n):
    new_n = str(n)[:-1].replace(str(digit), 'r') + str(n)[-1]
    counter = 0
    for i in range(digit + 1, 10):
        x = new_n
        x = x.replace('r', str(i))
        if prime_checker(int(x)):
            counter += 1
        if counter == 7:
            return True
            break
    return False


def prime_checker(n):
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def prime_sieve(n):
    is_prime = [True for i in range(n + 1)]
    primes = []
    for p in range(4, n + 1, 2):
        is_prime[p] = False
    p = 3
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
        p += 2
    is_prime[0] = False
    is_prime[1] = False
    for p in range(3, n + 1, 2):
        if is_prime[p]:
            primes.append(p)
    return primes


primes = prime_sieve(999999)

for p in primes:
    if str(p)[:-1].count('0') == 3 and checker(0, p):
        print(p)
        break
    elif str(p)[:-1].count('1') == 3 and checker(1, p):
        print(p)
        break
    elif str(p)[:-1].count('2') == 3 and checker(2, p):
        print(p)
        break

end = time.time()

# Executes in 0.344 seconds
print(end - start)
