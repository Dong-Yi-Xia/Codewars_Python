# Calculate average

# Write a function which calculates the average of the numbers in a given list.

import math

def find_average(numbers):
    sum = math.fsum(numbers)
    c = len(numbers)
    return sum/c

    pass



# def find_average(array):
#     try:
#         return sum(array) / len(array)
#     except ZeroDivisionError:
#         return 0