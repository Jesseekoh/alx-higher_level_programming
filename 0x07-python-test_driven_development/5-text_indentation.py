#!/usr/bin/python3
"""
5-text_indentaton
This module supplies one function, text_indentation().
"""


def text_indentation(text):
    """prints next two lines of text after each '.'

    Args:
        text (str)_

    Raises:
        TypeError: if tyep of text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
