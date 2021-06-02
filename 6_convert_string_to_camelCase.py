# Complete the method/function so that it converts dash/underscore delimited 
# words into camel casing. The first word within the output should be capitalized
#  only if the original word was capitalized (known as Upper Camel Case, 
#  also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"



def to_camel_case(text):

    x = "-_"
    y = "  "
    mytable = text.maketrans(x, y)
    a = text.translate(mytable).split()

    if (len(a)) == 0:
        return ''
    if len(a) > 1:
        for i in range(1,len(a)):
            a[i] = a[i].capitalize()



def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s



def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])    




import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)



# keeping the first character as is
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

