#!/usr/bin/python3
"""
    3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if the
    object is an instance of a class that inherits from a specified
    class

    Args:
        obj : object
        a_class (class): class
    """

    return isinstance(obj, a_class)
