#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """Returns a list of available attributes of a given
    object

    Args:
        obj (dict): dictionary
    """
    return dir(obj)
