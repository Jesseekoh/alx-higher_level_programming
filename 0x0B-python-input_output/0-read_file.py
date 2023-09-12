#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """Prints the contents of a file to stdout

    Args:
        filename (str, optional): _description_. Defaults to "".
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
