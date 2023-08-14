#!/usr/bin/python3
def no_c(my_string):
    """ Removes 'C' and 'c' from a string """
    new_string = ''
    if my_string:
        for i in my_string:
            if i != "C" and i != "c":
                new_string += i
    return new_string
