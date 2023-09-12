#!/usr/bin/python3
from sys import argv
"""7-add_items module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """Add arguments to file
    """
    filename = "add_item.json"
    try:
        my_arr = load_from_json_file(filename)
    except FileNotFoundError:
        my_arr = []
    for i in range(1, len(argv)):
        my_arr.append(argv[i])
    save_to_json_file(my_arr, filename)


add_items()
