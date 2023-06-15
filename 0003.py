# Problem 0003 - Largest Prime Factor
# the prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143
import math

def largest_prime(number):
    max_prime = 2
    while not number % 2:
        number /= 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while not number % i:
            max_prime = i
            number /= i

    if number > 2:
        max_prime = number

    return max_prime


print(largest_prime(600851475143))
# Answer: 6857
