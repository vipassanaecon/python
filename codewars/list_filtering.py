#In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(arg):   # define the function filter_listing that takes one argument (args) # function does the following:
    list = []           # we take an empty array and assign the variable list as an empty array (arrays are mutable and not like tuples, or dictionaries)     
    for x in arg:       # we create a for loop saying for each x in an argument lists: if x is of datatype integer the take the empty array and append it with the value of x
        if type(x) == int:
                list.append(x)
    return list         # when the function is called return the list appended to the for loop. 
