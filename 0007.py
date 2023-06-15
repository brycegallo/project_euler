def find_n_prime(number):
    primes = [2, 3, 5, 7, 11, 13]
    temp = 13
    while len(primes) < number:
        temp += 2
        is_prime = True
        for prime in primes:
            if not temp % prime:
                is_prime = False

        if is_prime:
            primes.append(temp)

    print(len(primes))
    return primes[-1]

print(find_n_prime(10001))
# Answer: 104743
