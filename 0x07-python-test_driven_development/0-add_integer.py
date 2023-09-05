#!/usr/bin/python3
"""
0-add_integer - returns the sum of two numbers
This module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """add_integer

    Args:
        a (int or float): 1st argument
        b (int or float): 2nd argument. Defaults to 98.

    Raises:
        TypeError: if a or b are not floats or intgers
        TypeError: _description_

    Returns:
        int: the sum of the arguments
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


print(add_integer(5))
