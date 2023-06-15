# Problem 0001 -  Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(number):
    summ = 0
    for i in range(number):
        if not (i % 3 and i % 5):
            summ += i
    return summ


print(multiples(1000))
# Answer: 233168
