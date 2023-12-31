# Problem 0009 - Special Pythagorean Triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

def find_triplet(rang):
    for a in range(1, rang):
        for b in range(1, rang):
            for c in range(1, rang):
                if (c ** 2 == (a ** 2) + (b ** 2)) and a + b + c == 1000:
                    return a * b * c


print(find_triplet(1000))
# Answer: 31875000
