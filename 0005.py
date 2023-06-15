# Problem 0005 - Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_smallest():
    multiple = 5040
    while multiple:
        wave_1 = (not multiple % 1) and (not multiple % 2) and (not multiple % 3) and (not multiple % 4)
        wave_2 = (not multiple % 5) and (not multiple % 6) and (not multiple % 7) and (not multiple % 8)
        wave_3 = (not multiple % 9) and (not multiple % 10) and (not multiple % 11) and (not multiple % 12)
        wave_4 = (not multiple % 13) and (not multiple % 14) and (not multiple % 15) and (not multiple % 16)
        wave_5 = (not multiple % 17) and (not multiple % 18) and (not multiple % 19) and (not multiple % 20)
        if wave_1 and wave_2 and wave_3 and wave_4 and wave_5:
            return multiple
        multiple += 2520


print(find_smallest())
# Answer: 232792560
