import time

start = time.time()

# Smallest number with 4 distinct prime factors
x = 2 * 3 * 5 * 7


def number_of_prime_factors(n):
    d = 2
    factors = set()
    while d < n ** 0.5 or n == 1:
        if n % d == 0:
            n = n / d
            factors.add(d)
            d -= 1
        d += 1
    return (len(factors) + 1)


while True:
    if number_of_prime_factors(x) == 4:
        x += 1
        if number_of_prime_factors(x) == 4:
            x += 1
            if number_of_prime_factors(x) == 4:
                x += 1
                if number_of_prime_factors(x) == 4:
                    print(x - 3)
                    break
    x += 1

end = time.time()

# Executes in 4.04 seconds
print(end - start)
