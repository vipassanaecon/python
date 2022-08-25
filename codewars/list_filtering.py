#In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(arg):
    list = []
    for x in arg:
        if type(x) == int:
                list.append(x)
    return list
