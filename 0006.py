def sum_square_difference(num):
    sum_of_squares = sum([x ** 2 for x in range(1, num+1)])
    square_of_sums = sum([x for x in range(1, num+1)]) ** 2
    return square_of_sums - sum_of_squares


print(sum_square_difference(100))
# Answer: 25164150
