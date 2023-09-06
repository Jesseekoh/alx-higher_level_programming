#!/usr/bin/python3
"""
3-say_my_name
This module supplies one function, say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """Prints a string containing given name

    Args:
        first_name (str): ---
        last_name (str, optional): Defaults to "".
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
