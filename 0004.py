# Problem 0004 - Largest Palindrome Product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome():  # terrible way to solve this one, but it worked
    for i in reversed(range(800, 999)):
        for j in reversed(range(800, 999)):
            product = i * j
            if str(product) == str(product)[::-1]:
                return [i, j, product]


print(largest_palindrome())
# Answer: 906609
