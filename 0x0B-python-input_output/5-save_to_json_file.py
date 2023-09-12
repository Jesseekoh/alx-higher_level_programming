#!/usr/bin/python3
"""5-save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a specified file

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """

    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
