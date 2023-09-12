#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """Write text to a file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
