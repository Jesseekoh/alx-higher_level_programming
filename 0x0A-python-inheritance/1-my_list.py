#!/usr/bin/python3
"""
    MyList class
"""


class MyList(list):
    """Prints out a sorted list

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
