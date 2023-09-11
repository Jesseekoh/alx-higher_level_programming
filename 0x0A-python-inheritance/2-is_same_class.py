#!/usr/bin/python3
"""
    2-is_same_class module
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specified
    class

    Args:
        obj (dict): object
        a_class: class
    """
    return isinstance(obj, a_class)
