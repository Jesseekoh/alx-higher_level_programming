#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """Appends text to a give file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """

    with open(filename, 'a') as f:
        return f.write(text)
