#!/usr/bin/python3
"""
101-add_attribute module
"""


def add_attribute(a_class, att_name, att_value):
    """Add attribute to object if possible

    Args:
        a_class (_type_): _description_
        att_name (_type_): _description_
        att_value (_type_): _description_

    Raises:
        TypeError: _description_
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, att_name, att_value)
