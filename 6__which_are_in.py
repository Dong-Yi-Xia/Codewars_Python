# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order
#  of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

# Beware: r must be without duplicates.



def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in string for string in a2)})
    

# sort() mutate the original 
def in_array(array1, array2):
    result = []
    for sub in array1:
        for string in array2:
            if sub in string: 
                if sub not in result: result.append(sub)
                break
    result.sort()            
    return result



#set items are unordered, unchangeable, and do not allow duplicate values.
# sorted() create a copy. 
def in_array(array1, array2):
    result = set()
    for a in array1:
        for b in array2:
            if a in b:
                result.add(a)
                break
    return sorted(result)
