import math

def find_triplet(rang):
    for a in range(1, rang):
        for b in range(1, rang):
            for c in range(1, rang):
                if (c ** 2 == (a ** 2) + (b ** 2)) and a + b + c == 1000:
                    return a * b * c

print(find_triplet(1000))
# Answer: 31875000