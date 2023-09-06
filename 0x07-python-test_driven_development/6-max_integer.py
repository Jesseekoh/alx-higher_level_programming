#!/usr/bin/python3
"""
6-max_integer
This module supplies one function, max)_integer().
"""


def max_integer(list=[]):
    """finds the maximum integer in a list

    Args:
        list (list, optional): _description_. Defaults to [].
    """

    if len(list) == 0:
        return None
    result = list[0]
    for i in list:
        if i > result:
            result = i
    return result
