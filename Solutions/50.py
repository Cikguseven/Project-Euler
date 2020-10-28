import time

start = time.time()

length = 0

solution = 0


def prime_sieve(n):
    is_prime = [True for i in range(n + 1)]
    list_of_primes = []
    for i in range(4, n + 1, 2):
        is_prime[i] = False
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
            list_of_primes.append(p)
    return list_of_primes


primes = prime_sieve(999999)

last_prime = len(primes)

for i in range(len(primes)):
    for j in range(i + length, last_prime):
        sum_of_primes = sum(primes[i:j])
        if sum_of_primes < 1000000:
            if sum_of_primes in primes and sum_of_primes > solution:
                length = j - i
                solution = sum_of_primes
        else:
            last_prime = j + 1
            break

print(solution)

end = time.time()

# Executes in 0.920 seconds
print(end - start)
