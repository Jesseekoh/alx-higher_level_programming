#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len: int = len(my_list)
    for i in range(list_len - 1, -1, -1):
        print("{:d}".format(my_list[i]))


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print_reversed_list_integer(my_list)
