# Problem 0010 - Summation of Primes
# The sum of primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million

def sieve(n):
    sum_of_primes = 0
    primes = [True for _ in range(n+1)]
    primes[0], primes[1] = False, False

    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            primes[j] = False

    for i in range(len(primes)):
        if primes[i]:
            sum_of_primes += i
    return sum_of_primes


print(sieve(2000000))
# Answer: 142913828922
