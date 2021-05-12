# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


from collections import Counter

def count(string):
    return Counter(string)




def count(string):
    return {i: string.count(i) for i in string}




def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter




def count(string):
    dict={}
    for i in string:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return dict




def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r