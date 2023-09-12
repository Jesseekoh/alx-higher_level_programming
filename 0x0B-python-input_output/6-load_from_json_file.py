#!/usr/bin/python3
"""6-load_from_json_file module"""
import json


def load_from_json_file(filename):
    """Creates an Object from a json file

    Args:
        filename (_type_): _description_
    """

    with open(filename) as f:
        return json.load(f)
