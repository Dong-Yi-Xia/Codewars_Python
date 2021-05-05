# In this little assignment you are given a string of space separated
#  numbers, and have to return the highest and lowest number.

# Example:

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"


# def high_and_low(numbers):
#     n = numbers.split(" ")
#     nums = list( map(int, n) )
#     nums = sorted(nums)
#     low = nums.copy().pop(0)
#     high = nums.copy().pop()
#     return f'{high} {low}'


def high_and_low(numbers):
    n = numbers.split(" ")
    nums = list( map(int, n) )
    nums = sorted(nums)
    return f'{nums[-1]} {nums[0]}'


# def high_and_low(numbers):
#   n = map(int, numbers.split(' '))
#   return str(max(n)) + ' ' + str(min(n))    



# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"