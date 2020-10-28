import time

start = time.time()


# To find the least common multiple (LCM) of 1 - 20, we can consider the LCM
# of 2 numbers at a time starting from 2 and 3 and compare it with the
# susbsequent number. LCM can be found by dividing the product of two numbers
# by their greatest common divisor (GCD). Generate GCD using Euclid's
# Algorithm where b > a
def gcd(a, b):
    remainder = 1
    while remainder != 0:
        remainder = b % a
        b = a
        a = remainder
    return b


def lcm(a, b):
    return (a * b) / gcd(a, b)


solution = lcm(2, 3)

for i in range(4, 21):
    solution = lcm(i, solution)

print(solution)

end = time.time()

# Executes in 0.0 seconds
print(end - start)
