from math import log

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def find_nth_prime(n):    
    if n < 6:
        return [2, 3, 5, 7, 11, 13][n - 1]
    limit = int(n * (log(n) + log(log(n))))
    primes = sieve_of_eratosthenes(limit)
    return primes[n - 1]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    print(f"Number: {n} is prime")
    return True


sol = find_nth_prime(n=10002)
assert is_prime(sol)
