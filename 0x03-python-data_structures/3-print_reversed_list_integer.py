#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ print an integer list reversed """
    list_len: int = len(my_list) - 1
    for i in range(list_len, -1, - 1):
        print("{:d}".format(my_list[i]))
