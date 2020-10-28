import time

start = time.time()

longest = 0

solution = 0


# Function that performs long division to obtain length of recurring decimals
# where x is dividend, d is divisor and i is counter for length of 0 in
# recurring decimal
def long_division(x, d):
    global longest
    global solution
    i = 0
    remainders = []
    while True:
        if x % d == 0:  # Terminates function if long division has no remainder
            return
        elif x in remainders:  # Terminates function if remainder repeats
            if (len(remainders) - remainders.index(x)) > longest:
                longest = (len(remainders) - remainders.index(x))
                solution = d
            return
        elif x // d == 0:  # 'Shifts' a decimal place if dividend is too small
            if i >= 1:
                remainders.append(0)
            x *= 10
            i += 1
        else:  # Appends remainder to list and continues long division
            remainders.append(x)
            x = x % d
            i = 0


# Skips even numbers as they have very short or no recurring decimals
for n in range(3, 1000, 2):
    long_division(1, n)

print(solution)

end = time.time()

# Executes in 0.476 seconds
print(end - start)
