# Switcheroo

# Given a string made up of letters a, b, and/or c, switch the position of
# letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    word = ""
    for i in s:
        if i == "a":
            word += "b"
        elif i == "b":
            word += "a"
        else:
            word += i
    return word
    

# def switcheroo(s):
#     return s.translate(str.maketrans('ab','ba'))    