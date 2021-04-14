# Find the stray number

# You are given an odd-length array of integers, in which all of them are 
# the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3


def stray(arr):
    map = {}
    for i in arr:
        if map.get(i): 
            map[i] += 1
        else:
            map[i] = 1
    
    for i in map:
        if map[i] == 1:
            return i
    

# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x



# min(iterable, *iterables, key, default)
# min() Parameters
# iterable - an iterable such as list, tuple, set, dictionary, etc.
# *iterables (optional) - any number of iterables; can be more than one
# key (optional) - key function where the iterables are passed and comparison is performed based on its return value
# default (optional) - default value if the given iterable is empty

# def stray(arr):
#     return min(arr, key=arr.count)