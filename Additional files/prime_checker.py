from math import sqrt


def prime_checker(n):
    if n % 2 == 0:
        print(f'{n} is even.')
        return
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            print(f'{n} is not prime. {d} is a proper divisor.')
            return
    print(f'{n} is prime.')


prime_checker(8237)
